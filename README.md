# 🤖 Chatbot WhatsApp - Oficina Mecânica

Projeto de chatbot integrado ao WhatsApp utilizando **Python (Flask)** + **Evolution API**, com funcionalidades de atendimento automatizado para uma oficina mecânica.

---

## 🚀 Tecnologias utilizadas

* Python 3
* Flask
* Docker
* Evolution API (Baileys)
* PostgreSQL
* Redis
* ngrok (exposição local)

---

## 📌 Funcionalidades

* Atendimento automático via WhatsApp
* Menu interativo
* Consulta de serviços e preços
* Simulação de agendamento
* Estrutura de chatbot com lógica de estados

---

## ⚙️ Instalação e configuração

### 1. Instalar dependências

```bash
pip install flask requests
```

---

### 2. Instalar o Docker

Baixe e instale o Docker Desktop:
https://www.docker.com/products/docker-desktop/

---

### 3. Subir a Evolution API

Crie um arquivo `docker-compose.yml` com o conteúdo abaixo:

```yaml
services:
  postgres:
    image: postgres:15
    container_name: evolution_postgres
    restart: always
    environment:
      POSTGRES_DB: evolution
      POSTGRES_USER: evolution
      POSTGRES_PASSWORD: evolution123
    volumes:
      - evolution_postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7
    container_name: evolution_redis
    restart: always
    command: redis-server --appendonly yes
    volumes:
      - evolution_redis_data:/data

  evolution:
    image: evoapicloud/evolution-api:v2.3.5
    container_name: evolution
    restart: always
    ports:
      - "8080:8080"
    depends_on:
      - postgres
      - redis
    environment:
      SERVER_URL: http://localhost:8080
      AUTHENTICATION_API_KEY: "SuaChaveAPIaqui"

      DATABASE_ENABLED: "true"
      DATABASE_PROVIDER: postgresql
      DATABASE_CONNECTION_URI: postgresql://evolution:evolution123@postgres:5432/evolution

      CACHE_REDIS_ENABLED: "false"
      CACHE_LOCAL_ENABLED: "true"

      CONFIG_SESSION_PHONE_CLIENT: Oficina
      CONFIG_SESSION_PHONE_NAME: Chrome
      CONFIG_SESSION_PHONE_VERSION: "2.3000.1033773198"
      WEB_VERSION: "2.3000.1033773198"
      DEL_INSTANCE: "false"

    volumes:
      - evolution_instances:/evolution/instances

volumes:
  evolution_postgres_data:
  evolution_redis_data:
  evolution_instances:
```

---

### 4. Rodar a API

```bash
docker compose up -d
```

Verifique se está rodando:

```bash
docker ps
```

Acesse o painel:

```text
http://localhost:8080/manager
```

---

### 5. Criar instância WhatsApp

No painel:

* Name: `oficina`
* Channel: `baileys`
* Token: qualquer valor
* Number: deixar vazio

Clique em **Create** → depois **Connect**

👉 Escaneie o QR Code no WhatsApp

---

### 6. Criar servidor Flask

Exemplo básico (`app.py`):

```python
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_URL = "http://localhost:8080"
INSTANCE = "oficina"
API_KEY = "sua-chave-aqui"

def enviar_resposta(numero, texto):
    requests.post(
        f"{API_URL}/message/sendText/{INSTANCE}",
        json={"number": numero, "text": texto},
        headers={"apikey": API_KEY}
    )

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    try:
        msg = data["data"]["message"]["conversation"]
        numero = data["data"]["key"]["remoteJid"].replace("@s.whatsapp.net", "")

        if msg.lower() == "oi":
            resposta = "Olá! Digite 1 para serviços ou 2 para preços."
        elif msg == "1":
            resposta = "Serviços: troca de óleo, alinhamento, revisão."
        elif msg == "2":
            resposta = "Preços a partir de R$80."
        else:
            resposta = "Não entendi."

        enviar_resposta(numero, resposta)

    except Exception as e:
        print("Erro:", e)

    return jsonify({"status": "ok"})

app.run(port=5000)
```

---

### 7. Expor servidor com ngrok

Baixe: https://ngrok.com/download

Execute:

```bash
ngrok http 5000
```

Copie a URL gerada:

```text
https://xxxx.ngrok-free.app
```

---

### 8. Configurar webhook na Evolution

No painel da Evolution:

* Webhook URL:

```text
https://xxxx.ngrok-free.app/webhook
```

* Ativar evento:

```text
MESSAGES_UPSERT
```

---

### 9. Testar

Envie mensagens no WhatsApp:

```text
oi
1
2
```

---

## 👨‍💻 Autor

Projeto desenvolvido para fins de estudo e prática em automação de atendimento via WhatsApp.

---
