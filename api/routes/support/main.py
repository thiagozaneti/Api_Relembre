from flask import jsonify, Blueprint, request
import requests  # Certifique-se de instalar requests: pip install requests

URL_MAQUINA_LOCAL = "http://192.168.1.16:5000/iniciar"

bp_suport = Blueprint("support", __name__)

@bp_suport.route("/status", methods=["POST"])
def status():
    # Lendo o JSON do corpo da requisição
    data = request.get_json()

    # Verificando se o JSON contém o campo "comando"
    if not data or "comando" not in data:
        return jsonify({"message": "error", "details": "Campo 'comando' é obrigatório"}), 400

    try:
        # Enviando o JSON para a máquina local
        response = requests.post(URL_MAQUINA_LOCAL, json=data)

        # Verificando a resposta da máquina local
        if response.status_code == 200:
            return jsonify({"message": "success", "response": response.json()}), 200
        else:
            return jsonify({"message": "failed", "status_code": response.status_code, "details": response.text}), 500
    except requests.exceptions.RequestException as e:
        # Tratando erros de requisição
        return jsonify({"message": "error", "details": str(e)}), 500