from flask import Flask, request, jsonify
import requests
import unicodedata
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

EVOLUTION_URL = "http://localhost:8080"
INSTANCE_NAME = "oficina"
API_KEY = os.getenv("EVOLUTION_API_KEY")

catalogo = [
    {"nome": "Troca de Óleo", "preco": 120.0},
    {"nome": "Alinhamento", "preco": 80.0},
    {"nome": "Balanceamento", "preco": 100.0},
    {"nome": "Revisão Completa", "preco": 250.0},
]

def normalizar(texto):
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return texto

def contem(msg, palavras):
    return any(palavra in msg for palavra in palavras)

def menu():
    return (
        "Olá! 👋 Sou o assistente da Oficina Mecânica.\n\n"
        "Como posso te ajudar?\n\n"
        "1️⃣ Serviços\n"
        "2️⃣ Preços\n"
        "3️⃣ Horário\n"
        "4️⃣ Endereço\n"
        "5️⃣ Telefone\n"
        "6️⃣ Agendamento\n\n"
        "Você pode responder com o número ou escrever o que precisa."
    )

def listar_precos():
    itens = sorted(catalogo, key=lambda item: item["preco"])
    texto = "Aqui estão nossos serviços, do menor para o maior preço:\n\n"

    for item in itens:
        texto += f"• {item['nome']} — R$ {item['preco']:.2f}\n"

    texto += "\nPara agendar, envie: quero agendar."
    return texto

def processar_mensagem(mensagem):
    msg = normalizar(mensagem)

    if contem(msg, ["oi", "ola", "bom dia", "boa tarde", "boa noite", "menu", "inicio"]):
        return menu()

    if msg in ["1"] or contem(msg, ["servico", "servicos", "fazem", "oferecem"]):
        return (
            "Oferecemos os seguintes serviços:\n\n"
            "• Troca de óleo\n"
            "• Alinhamento\n"
            "• Balanceamento\n"
            "• Revisão completa\n\n"
            "Digite preços para ver os valores."
        )

    if msg in ["2"] or contem(msg, ["preco", "precos", "valor", "valores", "catalogo", "quanto custa"]):
        return listar_precos()

    if msg in ["3"] or contem(msg, ["horario", "horarios", "funciona", "aberto", "abre", "fecha"]):
        return "Funcionamos de segunda a sexta, das 8h às 17h."

    if msg in ["4"] or contem(msg, ["endereco", "localizacao", "onde fica", "local"]):
        return "Estamos na Av. Principal, 456 - Centro."

    if msg in ["5"] or contem(msg, ["telefone", "contato", "whatsapp", "numero"]):
        return "Nosso telefone é: (75) 98888-0000."

    if msg in ["6"] or contem(msg, ["agendar", "agendamento", "marcar", "horario disponivel"]):
        return (
            "Claro! Para agendar, me envie estas informações:\n\n"
            "• Nome\n"
            "• Modelo do veículo\n"
            "• Serviço desejado\n"
            "• Melhor dia e horário\n\n"
            "Exemplo:\n"
            "João, Gol 2018, troca de óleo, amanhã pela manhã."
        )

    if contem(msg, ["oleo"]):
        return "A troca de óleo custa R$ 120,00. Deseja agendar?"

    if contem(msg, ["alinhamento"]):
        return "O alinhamento custa R$ 80,00. Deseja agendar?"

    if contem(msg, ["balanceamento"]):
        return "O balanceamento custa R$ 100,00. Deseja agendar?"

    if contem(msg, ["revisao", "revisao completa"]):
        return "A revisão completa custa R$ 250,00. Deseja agendar?"

    if contem(msg, ["obrigado", "obrigada", "valeu"]):
        return "De nada! 😊 Quando precisar, é só chamar."

    return (
        "Desculpe, não entendi muito bem. 😕\n\n"
        "Digite uma das opções abaixo:\n\n"
        "1️⃣ Serviços\n"
        "2️⃣ Preços\n"
        "3️⃣ Horário\n"
        "4️⃣ Endereço\n"
        "5️⃣ Telefone\n"
        "6️⃣ Agendamento"
    )

def responder_texto(numero, texto):
    url = f"{EVOLUTION_URL}/message/sendText/{INSTANCE_NAME}"

    payload = {
        "number": numero,
        "text": texto
    }

    headers = {
        "apikey": API_KEY,
        "Content-Type": "application/json"
    }

    try:
        requests.post(url, json=payload, headers=headers, timeout=30)
    except requests.RequestException as erro:
        print("Erro ao enviar mensagem:", erro)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    try:
        mensagem = data["data"]["message"].get("conversation")

        if not mensagem:
            return jsonify({"status": "ignored", "reason": "mensagem sem texto"})

        numero = data["data"]["key"]["remoteJid"].replace("@s.whatsapp.net", "")

        resposta = processar_mensagem(mensagem)
        responder_texto(numero, resposta)

    except Exception as erro:
        print("Erro ao processar mensagem:", erro)

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)