# api/__init__.py

from flask import Blueprint

routes = Blueprint('routes', __name__)

from . import routes
