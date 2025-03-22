from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot NPS rodando com sucesso no Render!'

@app.route('/webhook', methods=['POST'])
def webhook():
    dados = request.json
    print("✅ Webhook acionado!")
    print(f"📩 Dados recebidos: {dados}")

    return jsonify({"status": "mensagem recebida!"})

