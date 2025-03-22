from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    dados = request.json
    
    # Logs para verificar que o webhook foi acionado
    print("✅ Webhook acionado!")
    print(f"📩 Dados recebidos: {dados}")

    return jsonify({"status": "mensagem recebida!"})
    
