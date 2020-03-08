"""
Blueprint orchestrator for main views and errors.
Author: Maciej Cisowski
"""
from flask import Blueprint

main = Blueprint('main', __name__)
from . import views, errors
