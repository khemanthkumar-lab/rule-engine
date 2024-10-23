# Rule Engine Application

## Overview

This application is a simple 3-tier rule engine designed to determine user eligibility based on attributes like age, department, income, and spend. The system uses an Abstract Syntax Tree (AST) to represent conditional rules, allowing dynamic creation, combination, and modification of rules.

The application provides a web-based UI and a REST API to create and evaluate rules. It is built using **Flask** for the web framework and **SQLite** for the database. Rules are stored as AST structures in the database and are evaluated dynamically against user data.

---

## Features

- **Create Rule**: Dynamically generate a rule based on user-provided criteria (age, department, salary, etc.).
- **Evaluate Rule**: Evaluate rules against user attributes to determine if they satisfy eligibility conditions.
- **AST-based Rule Representation**: Rules are stored and processed as an Abstract Syntax Tree (AST).
- **Error Handling**: Handles invalid rule strings, missing attributes, and data validation errors.

---

## Project Structure

├── app.py # Flask application setup ├── models.py # Database models ├── rule_engine.py # Core logic for rule creation, evaluation, and AST handling ├── templates/ │ └── index.html # Basic UI for rule input and evaluation ├── static/ │ └── style.css # Styles for the UI ├── database_setup.py # Script to initialize the database ├── requirements.txt # Project dependencies ├── Dockerfile # Docker setup to containerize the application
