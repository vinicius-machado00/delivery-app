from flask import Blueprint

viewer_bp = Blueprint('viewer',__name__)

@viewer_bp.route('/')
def hello_world():
    return '<h1>Its Alive but now using Blueprints</h1>'

