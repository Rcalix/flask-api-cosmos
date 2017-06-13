"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskProject import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return "Hello Flask in Azure World"
