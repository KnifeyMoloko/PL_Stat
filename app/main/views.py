"""
View functions for the main PL_Stats page.
Author: Maciej Cisowski
"""
from flask import render_template
from . import main


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')
