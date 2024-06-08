import mercadopago.sdk

client = mercadopago.sdk.SDK("ENV_ACCESS_TOKEN")

# Atualizar Status de pagamento
payment_id = 'your_payment_id'
payment_data = {
    "status": "cancelled"
}

payment_response = client.payment().update(payment_id, payment_data)
payment = payment_response["response"]
