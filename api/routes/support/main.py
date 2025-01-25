from flask import jsonify, Blueprint, request
##import requests

bp_suport = Blueprint("support", __name__)


@bp_suport.route("/status", methods=["POST"])
def status():
    return jsonify({"message": "succes"}), 200