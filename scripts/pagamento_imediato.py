import json

import requests

ACCESS_TOKEN = ''

# URL da API
url = 'https://api.mercadolibre.com/items'

# Cabeçalhos da solicitação, incluindo o token de autorização e o tipo de conteúdo
headers = {
    'Authorization': 'Bearer ' + ACCESS_TOKEN,
    'Content-Type': 'application/json'
}

# Dados a serem enviados na solicitação POST
data = {
    "title": "Item de teste - Não Comprar",
    "category_id": "MLB437616",
    "price": 10,
    "currency_id": "BRL",
    "available_quantity": 1,
    "buying_mode": "buy_it_now",
    "listing_type_id": "gold_special",
    "condition": "new",
    "description": "Publicação de teste, não comprar",
    "video_id": "YOUTUBE_ID_HERE",
    "tags": [
        "immediate_payment"
    ],
    "sale_terms": [
        {
            "id": "WARRANTY_TYPE",
            "value_name": "Garantia do vendedor"
        },
        {
            "id": "WARRANTY_TIME",
            "value_name": "90 días"
        }
    ],
    "pictures": [
        {
            "source": "https://www.motorino.com.br/site/wp-content/uploads/2018/01"
                      "/produto_de_teste_amarelo_4_2_20171020224326-400x400.jpg"
        }
    ]
}

# Enviar solicitação POST e obter resposta
response = requests.post(url, headers=headers, data=json.dumps(data))

# Verificar se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    data = response.json()
    print(data)  # Imprimir os dados obtidos da API
else:
    print('Falha na solicitação:', response.status_code)

# Categorias com PGTO Imediato


category_id = 'seu_id_de_categoria'

# URL da API
url = f'https://api.mercadolibre.com/sites/categories/{category_id}'

# Enviar solicitação GET e obter resposta
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    immediate_payment = data.get('immediate_payment', 'not found')
    item_conditions = data.get('item_conditions', [])

    print("Immediate Payment:", immediate_payment)
    print("Item Conditions:", item_conditions)
else:
    print('Falha na solicitação:', response.status_code)
