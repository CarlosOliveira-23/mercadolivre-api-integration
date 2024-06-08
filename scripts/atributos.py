# Consultar atributos
import json

import requests

ACCESS_TOKEN = ''
CATEGORY_ID = ''

url = 'https://api.mercadolibre.com/categories/$CATEGORY_ID/attributes'

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',

}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)  # Imprimir os dados obtidos da API
else:
    print(f'Falha na solicitação:, response.status_code')

# Atributos obrigatórios

url = 'https://api.mercadolibre.com/categories/$CATEGORY_ID/technical_specs/input'

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',

}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)  # Imprimir os dados obtidos da API
else:
    print(f'Falha na solicitação:, response.status_code')

# Recurso /categories/$CATEGORY_ID/technical_specs/output para publicações organizadas

url = 'https://api.mercadolibre.com/categories/$CATEGORY_ID/technical_specs/output'

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Falha na solicitação:, response.status_code')

# Atributos obrigatórios por condição

url = f'https://api.mercadolibre.com/categories/$CATEGORY_ID/attributes/conditional'

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
}

response = requests.post(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Falha na solicitação:, response.status_code')

# Identificar itens penalizados

url = f'https://api.mercadolibre.com/users/$USER_ID/items/search?tags=incomplete_technical_specs'

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Falha na solicitação:, response.status_code')

# Especificar atributos que não aplicam

url = f'https://api.mercadolibre.com/items/$ITEM_ID?attributes=attributes&include_internal_attributes=true'

headres = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Falha na solicitação:, response.status_code')

# Criar anúncios com atributos N/A

url = 'https://api.mercadolibre.com/your_endpoint'

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

# Corpo da requisição (dados a serem enviados)
data = {
    "site_id": str,
    "title": str,
    "category_id": str,
    "price": str,
    "currency_id": "BR",
    "buying_mode": str,
    "listing_type_id": str,
    "condition": str,
    "available_quantity": str,
    "attributes": [
        {
            "id": "COLOR",
            "value_id": str,
        },
        {
            "id": "VOLTAGE",
            "value_name": str
        },
        {
            "id": "DIAMETER",
            "value_id": "-1",
            "value_name": None
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    response_data = response.json()
    print(response_data)
else:
    print(f"Erro ao fazer a requisição: {response.status_code}")

# Modificar uma publicação ativa e indicar que um atributo não se aplica (N/A)

url = 'https://api.mercadolibre.com/your_endpoint'

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

data = {
    "attributes": [
        {
            "id": "COLOR",
            "value_id": str,
        },
        {
            "id": "VOLTAGE",
            "value_name": str,
        },
        {
            "id": "DIAMETER",
            "value_id": "-1",
            "value_name": None
        },
        {
            "id": "LATERAL_OSCILLATION",
            "value_id": str
        }
    ]
}

response = requests.put(url, headers=headers)

if response.status_code == 200:
    response_data = response.json()
    print(response_data)
else:
    print(f"Erro ao fazer a requisição: {response.status_code}")

# Criar item com atributos

url = 'https://api.mercadolibre.com/items'

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

data = {
    "site_id": "MLA",
    "title": "Item de testeo, por favor no contactar --kc:off",
    "category_id": "MLA125703",
    "price": 4000,
    "currency_id": "ARS",
    "buying_mode": "buy_it_now",
    "listing_type_id": "gold_special",
    "condition": "new",
    "available_quantity": 10,
    "attributes": [
        {
            "id": "MODEL",
            "value_name": "B228D"
        },
        {
            "id": "VOLUME_CAPACITY",
            "value_name": "28 L"
        }
    ]
}

response = requests.post(url, data=json.dumps(data))

if response.status_code == 200:
    response_data = response.json()
    print(response_data)
else:
    print(f"Erro ao fazer a requisição: {response.status_code}")

# Modificar e/ou adicionar atributos

url = 'https://api.mercadolibre.com/items/$ITEM_ID'

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}'
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Falha na solicitação:, response.status_code')
