import json
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework import views, response, status
from webhooks.models import Webhook
from webhooks.messages import outflow_message
from services.callmebot import CallMeBot


# Recebe eventos de um sistema externo (Receptador)
class WebhookOrderView(views.APIView):
    
    def post(self, request):
        data = request.data

        # Cadastra o webhook na base de dados
        Webhook.objects.create(
            event_type = data.get('event_type'),
            event=json.dumps(data, ensure_ascii=False)
        )

        # Desestrutura e captura todos os dados
        product_name = data.get('product')
        quantity = int(data.get('quantity', 0))
        product_cost_price = float(data.get('product_cost_price', 0.0))
        product_selling_price = float(data.get('product_selling_price', 0.0))
        
        total_value = product_selling_price * quantity
        profit_value = total_value - (product_cost_price * quantity)

        # Montagem da mensagem
        message = outflow_message.format(
            product_name,
            quantity,
            total_value,
            profit_value,
        )

        # Instancio o serviço e chamo a mensagem
        callmebot = CallMeBot()
        callmebot.send_message(message)

        # Adicionando novos dados nos dados da requisição
        data['total_value'] = total_value
        data['profit_value'] = profit_value
        send_mail(
            subject='Nova Saída - Gestão de Controle de Estoque',
            message='',
            from_email=f'Gestão de Controle de Estoque - <{settings.EMAIL_HOST_USER}>',
            recipient_list=[settings.EMAIL_ADMIN_RECEIVER],
            html_message=render_to_string('email_outflow.html', data),
            fail_silently=False,
        )

        return response.Response(
            data=data,
            status=status.HTTP_200_OK
        )
