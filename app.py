from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# INSIRA SUA INSTÂNCIA E TOKEN AQUI (não esquece das aspas!)
INSTANCIA = "3DE8910478AF3063BBAB32C54B267657"
TOKEN = "4C238699A42CC1F7AC28584D"

# Função para enviar mensagem via Z-API
def enviar_mensagem(numero, mensagem):
    url = f"https://api.z-api.io/instances/{INSTANCIA}/token/{TOKEN}/send-message"

    payload = {
        "phone": numero,
        "message": mensagem
    }

    print(f"➡️ Enviando mensagem para {numero}: {mensagem}")

    try:
        response = requests.post(url, json=payload)
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

    # Captura o número e a mensagem do cliente
    numero = dados.get('phone')
    mensagem = dados.get('message')

    # Valida se os dados vieram corretos
    if not numero:
        print("❌ Número do cliente não encontrado.")
        return jsonify({"status": "número não encontrado"})

    if not mensagem:
        print("❌ Mensagem do cliente não encontrada.")
        return jsonify({"status": "mensagem não encontrada"})

    # Monta a resposta
    resposta = f"Obrigado pela sua mensagem: '{mensagem}'! Em breve entraremos em contato."

    # Envia a resposta automática
    resultado = enviar_mensagem(numero, resposta)

    return jsonify({"status": "mensagem recebida e resposta enviada!", "resultado": resultado})
