from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Rule(db.Model):
    __tablename__ = 'rules'
    id = db.Column(db.Integer, primary_key=True)
    rule_string = db.Column(db.Text, nullable=False)
    ast = db.Column(db.JSON, nullable=False)  # Store AST as JSON
