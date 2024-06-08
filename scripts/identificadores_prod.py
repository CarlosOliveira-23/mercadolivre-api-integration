# Identificadores com GTIN

import json

import requests

ACCESS_TOKEN = ''
CATEGORY_ID = ''

url = 'https://api.mercadolibre.com/items'

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

data = {
    "title": "Bicicleta Mtb Totem By Topmega R29 Producto Test",
    "category_id": "MLA6143",
    "price": 99999,
    "currency_id": "ARS",
    "available_quantity": 2,
    "sale_terms": [
        {
            "id": "WARRANTY_TIME",
            "value_name": "6 meses"
        },
        {
            "id": "WARRANTY_TYPE",
            "value_name": "Garantía de fábrica"
        }
    ],
    "buying_mode": "buy_it_now",
    "listing_type_id": "gold_pro",
    "condition": "new",
    "pictures": [
        {
            "source": "http://http2.mlstatic.com/D_608172-MLA53351140125_012023-O.jpg"
        },
        {
            "source": "http://http2.mlstatic.com/D_714634-MLA53351124241_012023-O.jpg"
        },
        {
            "source": "http://http2.mlstatic.com/D_878513-MLA53351118304_012023-O.jpg"
        }
    ],
    "attributes": [
        {
            "id": "BICYCLE_FRAME_MATERIALS",
            "value_name": "aluninio"
        },
        {
            "id": "BICYCLE_TYPE",
            "value_name": "Mountain bike"
        },
        {
            "id": "BRAND",
            "value_name": "Totem"
        },
        {
            "id": "FRONT_BRAKE_TYPE",
            "value_name": "Disco mecánico"
        },
        {
            "id": "GENDER",
            "value_name": "Sin género"
        },
        {
            "id": "MODEL",
            "value_name": "Totem"
        },
        {
            "id": "REAR_BRAKE_TYPE",
            "value_name": "Disco mecánico"
        },
        {
            "id": "GTIN",
            "value_name": "7898945080293"
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Falha na solicitação:', response.status_code)

# Adição de Identificadores

url = 'https://api.mercadolibre.com/items/{id_item}/'

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

data = {
    "variations": [
        {
            "id": 177163823616,
            "attributes": [
                {
                    "id": "GTIN",
                    "value_name": "7898945080293"
                }
            ]
        }
    ]
}

response = requests.put(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Falha na solicitação:', response.status_code)
