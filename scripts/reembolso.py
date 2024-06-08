import mercadopago

sdk = mercadopago.SDK('TOKEN')

sdk.refund().create('id_pagamento')

# Parcial

sdk = mercadopago.SDK('TOKEN')

refund_object = {
    'amount': 0.0
}

sdk.refund().create('id_pagamento', refund_object)

# Especifico

refunds_response = sdk.refund().list_all(sdk)
refunds = refunds_response["response"]
