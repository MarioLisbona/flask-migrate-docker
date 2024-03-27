from flask import jsonify, Blueprint

msg_bp = Blueprint('msg', __name__)

# ======================================================================================================
# route to return message
# ======================================================================================================
@msg_bp.route("/msg", methods=["GET"])
def get_api_base_url():
    return jsonify({
        "msg": "todos api is up",
        "success": True,
        "data": None
    }), 200