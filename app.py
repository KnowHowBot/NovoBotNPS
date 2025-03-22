from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Dados da sua instância Z-API
INSTANCIA = “3DE8910478AF3063BBAB32C54B267657”
TOKEN = “4C238699A42CC1F7AC28584D

# Função para enviar mensagem automática via Z-API
def enviar_mensagem(numero, mensagem):
	https://api.z-api.io/instances/3DE8910478AF3063BBAB32C54B267657/token/4C238699A42CC1F7AC28584D/send-text
    payload = {
        "phone": numero,
        "message": mensagem
    }

    response = requests.post(url, json=payload)

    print("Resposta da Z-API:", response.json())
    return response.json()

@app.route('/')
def home():
    return 'Bot NPS rodando com sucesso no Render!'

@app.route('/webhook', methods=['POST'])
def webhook():
    dados = request.json
    
    print("✅ Webhook acionado!")
    print(f"📩 Dados recebidos: {dados}")

    # Extrair número e mensagem recebida
    numero = dados.get('phone')   # número do cliente
    mensagem = dados.get('message')  # mensagem recebida

    # Aqui vai a lógica simples de resposta
    if mensagem:
        resposta = f"Obrigado pelo seu feedback: {mensagem}!"
        
        # Enviar resposta automática
        enviar_mensagem(numero, resposta)

    return jsonify({"status": "mensagem recebida e respondida!"})

