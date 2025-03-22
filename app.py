from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Substitua pelos seus dados REAIS da Z-API (com aspas)
INSTANCIA = "3DE8910478AF3063BBAB32C54B267657"
TOKEN = "4C238699A42CC1F7AC28584D"

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

    # Captura o número do remetente
    numero = dados.get('phone')

    # Corrigido: Captura a mensagem dentro de 'text' ➜ 'message'
    mensagem = dados.get('text', {}).get('message')

    # Verificações básicas
    if not numero:
        print("❌ Número não encontrado nos dados recebidos.")
        return jsonify({"status": "número não encontrado"})

    if not mensagem:
        print("❌ Mensagem não encontrada nos dados recebidos.")
        return jsonify({"status": "mensagem não encontrada"})

    print(f"➡️ Mensagem recebida de {numero}: {mensagem}")

    resposta = f"Obrigado pelo seu feedback: '{mensagem}'!"

    resultado = enviar_mensagem(numero, resposta)

    return jsonify({
        "status": "mensagem recebida e resposta enviada!",
        "resultado": resultado
    })
