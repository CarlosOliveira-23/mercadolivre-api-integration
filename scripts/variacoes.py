# Este arquivo se refere as variações que os produtos podem ocorrer dentro do produto Exemplo : Peso Bruto / Peso
# Liquido / Comprimento / Largura

import requests

# Defina a variável ACCESS_TOKEN
ACCESS_TOKEN = "TEST-fd03783f-59cd-4b7f-b160-b8300ac76220"
ITEM_ID = "seu_item_id"
# URL para obter os atributos da categoria MLA126186
url_get_attributes = "https://api.mercadolibre.com/categories/MLA126186/attributes"

# Cabeçalhos para incluir no pedido
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

# Requisição GET para obter os atributos da categoria
response = requests.get(url_get_attributes, headers=headers)

# Verifica se a solicitação GET foi bem-sucedida
if response.status_code == 200:
    attributes_data = response.json()
    print("Atributos da categoria MLA126186:")
    print(attributes_data)
else:
    print(f"Erro ao obter os atributos da categoria. Código de status: {response.status_code}")

# Consulta variações

# URL para obter informações sobre o item
url_get_item_info = f"https://api.mercadolibre.com/items/{ITEM_ID}"

# Cabeçalhos para incluir no pedido
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

# Requisição GET para obter informações sobre o item
response = requests.get(url_get_item_info, headers=headers)

# Verifica se a solicitação GET foi bem-sucedida
if response.status_code == 200:
    item_info = response.json()
    print("Informações do item:")
    print(item_info)
else:
    print(f"Erro ao obter informações do item. Código de status: {response.status_code}")

# A seguinte chamada, com a qual a resposta anterior será diretamente filtrada para mostrar apenas as variações:


# URL para obter as variações do item
url_get_variations = f"https://api.mercadolibre.com/items/{ITEM_ID}/variations"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

# Requisição GET para obter as variações do item
response = requests.get(url_get_variations, headers=headers)

# Verifica se a solicitação GET foi bem-sucedida
if response.status_code == 200:
    variations_data = response.json()
    print("Variações do item:")
    print(variations_data)
else:
    print(f"Erro ao obter as variações do item. Código de status: {response.status_code}")

# Consulta de ID em particular adicionando o variation_id no fim da chamada

# URL para obter as variações do item em particular
url_get_variations = f"https://api.mercadolibre.com/items/{ITEM_ID}/variations/$VARIATION_ID"
url_get_attributes = f"https://api.mercadolibre.com/items/MLA640992661?include_attributes=all"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

# Requisição GET para obter as variações do item em particular
if response.status_code == 200:
    variations_data = response.json()
    print("Variações do item especifico:")
    print(variations_data)
else:
    print(f"Erro ao obter as variações do item especifico. Código de status: {response.status_code}")

# Adicionar novas variações


# URL para adicionar variações ao item
url_add_variations = f"https://api.mercadolibre.com/items/{ITEM_ID}/variations"

# Cabeçalhos para incluir no pedido
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# Dados para adicionar variações em formato de dicionário
variation_data = {
    "attribute_combinations": [
        {
            "id": "COLOR",
            "value_id": "52035"
        }
    ],
    "price": 100,
    "available_quantity": 10,
    "sold_quantity": 0,
    "picture_ids": [
        "553111-MLA20482692355_112015"
    ]
}

# Requisição POST para adicionar variações ao item
response = requests.post(url_add_variations, headers=headers, json=variation_data)

# Verifica se a solicitação POST foi bem-sucedida
if response.status_code == 200:
    print("Variações adicionadas com sucesso ao item.")
else:
    print(f"Erro ao adicionar variações ao item. Código de status: {response.status_code}")

# Modificar alterações

# URL para modificar variações
url_update_variations = "https://api.mercadolibre.com/items/MLA658778048"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# Dados para atualizar variações em formato de dicionário
variations_data = {
    "variations": [
        {
            "id": 15092589430,
            "attribute_combinations": [
                {
                    "id": "COLOR",
                    "value_id": "52005"
                },
                {
                    "id": "VOLTAGE",
                    "value_id": "198812"
                }
            ]
        },
        {
            "id": 15093506680,
            "attribute_combinations": [
                {
                    "id": "COLOR",
                    "value_id": "52035"
                },
                {
                    "id": "VOLTAGE",
                    "value_id": "198813"
                }
            ]
        }
    ]
}

# Requisição PUT para atualizar variações do item
response = requests.put(url_update_variations, headers=headers, json=variations_data)

# Verifica se a solicitação PUT foi bem-sucedida
if response.status_code == 200:
    print("Variações do item atualizadas com sucesso.")
else:
    print(f"Erro ao atualizar variações do item. Código de status: {response.status_code}.")

# Modificar Preço


# URL para atualizar preços do item
url_update_variations = "https://api.mercadolibre.com/items/MLA658778048"

# Cabeçalhos para incluir no pedido
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# Dados para atualizar as variações em formato de dicionário
variations_data = {
    "variations": [
        {
            "id": 15092589430,
            "price": 300
        },
        {
            "id": 15092544559,
            "price": 300
        },
        {
            "id": 15091378470,
            "price": 300
        }
    ]
}

# Requisição PUT para atualizar alterações de preço do item
response = requests.put(url_update_variations, headers=headers, json=variations_data)

# Verifica se a solicitação PUT foi bem-sucedida
if response.status_code == 200:
    print("Variações do item atualizadas com sucesso.")
else:
    print(f"Erro ao atualizar variações do item. Código de status: {response.status_code}")

# Modificar Estoque


# URL para modificar Estoque
url = 'https://api.mercadolibre.com/items/MLA658778048'

# Dados para atualizar estoque
data = {
    "variations": [{
        "id": 15092589430,
        "available_quantity": 10
    }]
}

headers = {
    'Authorization': 'Bearer ' + ACCESS_TOKEN,
    'Content-Type': 'application/json'
}

# Requisição PUT para modificar Estoque
response = requests.put(url, json=data, headers=headers)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    print("PUT request successful")
else:
    print("PUT request failed with status code:", response.status_code)
    print("Response content:", response.text)

# Remover variações


url_delete_variations = 'https://api.mercadolibre.com/items/MLA599099879/variations/10449631060'

headers = {
    'Autorization': 'Bearer' + ACCESS_TOKEN,
}

# Requisição Delete para remover variações

response = requests.delete(url_delete_variations, headers=headers)

# Verifica se a requisição foi bem-sucedida

if response.status_code == 200:
    print("DELETE realizado com sucesso")
else:
    print("Falha ao realizar DELETE Código de tatus:", response.status_code)
    print("Response content:", response.text)

# Anunciar ou modificar produtos com variações com caracteristicas personalizadas


# URL para modificação
url = 'https://api.mercadolibre.com/items/MLA658778048'

data = {
    "variations": [
        {
            "attribute_combinations": [
                {
                    "name": "Diseño",
                    "value_name": "Buho",
                    "value_struct": None,
                    "values": [
                        {
                            "id": None,
                            "name": "Buho",
                            "struct": None
                        }
                    ]
                }
            ],
            "price": 100,
            "available_quantity": 10
        },
        {
            "attribute_combinations": [
                {
                    "name": "Diseño",
                    "value_name": "Flamenco",
                    "value_struct": None,
                    "values": [
                        {
                            "id": None,
                            "name": "Flamenco",
                            "struct": None
                        }
                    ]
                }
            ],
            "price": 100,
            "available_quantity": 10
        },
        {
            "attribute_combinations": [
                {
                    "name": "Diseño",
                    "value_name": "Cocodrilo",
                    "value_struct": None,
                    "values": [
                        {
                            "id": None,
                            "name": "Cocodrilo",
                            "struct": None
                        }
                    ]
                }
            ],
            "price": 100,
            "available_quantity": 10
        }
    ]
}

headers = {
    'Authorization': 'Bearer ' + ACCESS_TOKEN,
    'Content-Type': 'application/json'
}

# Requisição PUT para caracteristica personalizada
response = requests.put(url, json=data, headers=headers)

# Verifica se a reequisição foi bem-sucedida
if response.status_code == 200:
    print("Personalização realizada com Sucesso")
else:
    print("Falha ao realizar Personalização Código de Status:", response.status_code)
    print("Response content:", response.text)
