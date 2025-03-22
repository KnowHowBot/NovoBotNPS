from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

INSTANCIA = "3DE8910478AF3063BBAB32C54B267657"
TOKEN = "4C238699A42CC1F7AC28584D"

def enviar_mensagem(numero, mensagem):
    if not numero:
        print("❌ Número de telefone está vazio ou inválido!")
        return {"error": "Número vazio"}

    if not mensagem:
        print("❌ Mensagem está vazia!")
        return {"error": "Mensagem vazia"}

    url = f"https://api.z-api.io/instances/{INSTANCIA}/token/{TOKEN}/send-text"

    payload = {
        "phone": numero,
        "message": mensagem,
        "delayMessage": 15
    }

    headers = {
        'Content-Type': 'application/json',
        'Client-Token': 'F1c5ff3be2f5b4fa3a28ee04372cb674aS'
        
    }
    print(f"📦 Payload enviado: {payload}")

    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=payload, headers=headers)
        resposta_json = response.json()

        print(f"✅ Resposta da Z-API: {resposta_json}")

        return resposta_json
    except Exception as e:
        print(f"❌ Erro ao enviar mensagem: {e}")
        return None

@app.route('/')
def home():
    return 'Bot NPS rodando com sucesso no Render!'

@app.route('/webhook', methods=['POST'])
def webhook():
    dados = request.json

    print("✅ Webhook acionado!")
    print(f"📩 Dados recebidos: {dados}")

    # Captura e valida o número
    numero = dados.get('phone')
    numero = str(numero).strip() if numero else None

    # Captura e valida a mensagem recebida
    mensagem = dados.get('text', {}).get('message')
    mensagem = str(mensagem).strip() if mensagem else None

    # Verificações básicas
    if not numero:
        print("❌ Número não encontrado nos dados recebidos.")
        return jsonify({"status": "número não encontrado"})

    if not mensagem:
        print("❌ Mensagem não encontrada nos dados recebidos.")
        return jsonify({"status": "mensagem não encontrada"})

    print(f"➡️ Mensagem recebida de {numero}: {mensagem}")

    # Monta a resposta
    resposta = f"Obrigado pelo seu feedback: '{mensagem}'!"

    # Envia a resposta
    resultado = enviar_mensagem(numero, resposta)

    return jsonify({
        "status": "mensagem recebida e resposta enviada!",
        "resultado": resultado
    })
