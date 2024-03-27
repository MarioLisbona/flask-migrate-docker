from flask import jsonify, Blueprint

# Create a blueprint fior the home routes
home_bp = Blueprint('home', __name__)

# ======================================================================================================
# route for home / index
# ======================================================================================================
@home_bp.route('/')
def home():
    return jsonify({
        "msg": "Welcome"
    })