# 🔔 Sistema de Notificações via Webhook

Este projeto implementa um sistema de **notificações desacopladas** baseado em **webhooks** usando Django REST Framework.

Ele recebe eventos de outro sistema via requisições HTTP `POST` com dados estruturados em JSON, processa esses dados e pode executar ações como envio de e-mails, mensagens no WhatsApp, ou integração com outros serviços.

---

## 📌 Visão Geral

- 🔄 Sistema principal envia eventos para este serviço de webhook
- 📩 Este sistema recebe os eventos (ex: saída de produto)
- ⚙️ Os dados recebidos são processados e podem disparar:
  - E-mails
  - Mensagens no WhatsApp
  - Integrações com APIs externas
  - Armazenamento em banco de dados
  - Qualquer outro tipo de automação

---

## 🚀 Funcionalidades

- ✅ Endpoint RESTful para recebimento de eventos
- ✅ Comunicação entre serviços via JSON
- ✅ Separação clara entre envio e processamento
- ✅ Base para arquitetura orientada a eventos
- 🔒 Validação e segurança configuráveis

---

## 🛠️ Tecnologias Utilizadas

- Python 3.12+
- Django 5.2
- Django REST Framework
- Requests (cliente HTTP)
- Docker (para o sistema principal, opcional)
- Webhook.site (para testes)

---

## ⚙️ Funcionamento

### 🔁 Fluxo de evento:
[ Sistema Principal ] ─── POST /api/v1/webhooks/order/ ───▶ [ Notifica (este projeto) ] ──▶ ações: email, WhatsApp, etc.

### 📥 Exemplo de evento recebido:

```json
{
  "event_type": "outflow",
  "timestamp": "2025-06-29 13:45:00",
  "product": "Café",
  "product_selling_price": 12.5,
  "quantity": 3,
  "description": "Venda balcão"
}
```

## ⚙️ Como utilizar
```bash
Clone o repositório:
git clone https://github.com/seu-usuario/webhook-notify.git
cd webhook-notify
```

```bash
Crie um ambiente virtual e instale as dependências:
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

```bash
Inicie o servidor:
python manage.py runserver 8001
```

Acessar a aplicação http://localhost:8001
