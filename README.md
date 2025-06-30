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

