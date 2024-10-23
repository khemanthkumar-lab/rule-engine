from flask import Flask, request, jsonify, render_template
from models import db, Rule  # Import your database models
from rule_engine import create_rule, combine_rules, evaluate_rule  # Import rule logic
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rules.db'  # SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable warning for modifications
db.init_app(app)  # Initialize DB with Flask app

# Initialize database on first run
with app.app_context():
    db.create_all()  # Create tables based on your models

@app.route('/')
def index():
    return render_template('index.html')  # Serve the UI form if you have one

# API to create a rule
@app.route('/create_rule', methods=['POST'])
def create_rule_api():
    try:
        # Expecting JSON data
        rule_string = request.json.get('rule')  # Get rule from the request body
        if not rule_string:
            return jsonify({"error": "Rule string is missing"}), 400

        # Generate AST for the rule
        ast = create_rule(rule_string)  # Your create_rule function should return the AST
        rule = Rule(rule_string=rule_string, ast=json.dumps(ast, default=lambda o: o.__dict__))  # Save AST as JSON in DB

        # Add rule to the database
        db.session.add(rule)
        db.session.commit()

        return jsonify({"message": "Rule created", "ast": ast.__dict__}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API to evaluate a rule with user data
@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_api():
    try:
        # Expecting JSON data
        rule_id = request.json.get('rule_id')
        user_data = request.json.get('user_data')  # Get user data as a dictionary

        if not rule_id or not user_data:
            return jsonify({"error": "Rule ID and user data are required"}), 400

        # Fetch the rule by ID from the database
        rule = Rule.query.get(rule_id)
        if not rule:
            return jsonify({"error": "Rule not found"}), 404

        # Evaluate the rule
        ast = json.loads(rule.ast)  # Load the AST from the DB (stored as JSON string)
        result = evaluate_rule(ast, user_data)  # Your evaluate_rule function processes AST and user data

        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
