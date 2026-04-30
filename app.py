from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

EVOLUTION_URL = "http://localhost:8080"
INSTANCE_NAME = "oficina"
API_KEY = "SuaChaveAPIaqui"

respostas = {
    "oi": "Olá! Sou o assistente da Oficina Simas Turbo. Digite: serviços, horário, endereço ou telefone.",
    "Oi": "Olá! Sou o assistente da Oficina Simas Turbo. Digite: serviços, horário, endereço ou telefone.",
    "Olá": "Olá! Sou o assistente da Oficina Simas Turbo. Digite: serviços, horário, endereço ou telefone.",
    "servicos": "Oferecemos: troca de óleo, alinhamento, balanceamento e revisão completa.",
    "Serviços": "Oferecemos: troca de óleo, alinhamento, balanceamento e revisão completa.",
    "horario": "Funcionamos de segunda a sexta, das 8h às 17h.",
    "Horário": "Funcionamos de segunda a sexta, das 8h às 17h.",
    "Horários": "Funcionamos de segunda a sexta, das 8h às 17h.",
    "endereco": "Av. Principal, 456 - Centro.",
    "Endereço": "Av. Principal, 456 - Centro.",
    "telefone": "(75) 98888-0000",
    "Telefone": "(75) 98888-0000",
    "Contato": "(75) 98888-0000"
}

catalogo = [
    [3, "Troca de Óleo", 120.0],
    [1, "Alinhamento", 80.0],
    [4, "Balanceamento", 100.0],
    [2, "Revisão Completa", 250.0]
]

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

    requests.post(url, json=payload, headers=headers)


def processar_mensagem(msg):
    msg = msg.strip().lower()

    if msg in respostas:
        return respostas[msg]

    if msg == "precos" or msg == "catálogo" or msg == "catalogo":
        catalogo.sort(key=lambda x: x[2])
        texto = "Aqui estão nossas opções mais acessíveis primeiro:\n\n"
        for item in catalogo:
            texto += f"{item[1]} - R$ {item[2]:.2f}\n"
        return texto

    return "Desculpe, não entendi. Digite: serviços, preços, horário, endereço ou telefone."


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    try:
        mensagem = data["data"]["message"]["conversation"]
        numero = data["data"]["key"]["remoteJid"].replace("@s.whatsapp.net", "")

        resposta = processar_mensagem(mensagem)
        responder_texto(numero, resposta)

    except Exception as erro:
        print("Erro ao processar mensagem:", erro)

    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(port=5000, debug=True)