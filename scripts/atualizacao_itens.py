import requests

access_token = ""
ITEM_ID = ""
url = f"https://api.mercadolibre.com/items/{ITEM_ID}"

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

data = {
    "title": "Title",
    "price": float,
    "statuses": ["active", "paused", "closed"],
    "deleted": False,
    "avaliable_quatity": float
}

response = requests.put(url, headers=headers)

if response.status_code == 200:
    print("Item atualizado com sucesso!")
    print(data)
else:
    print(f"Falha ao atualizar Item: {response.status_code}")

# Consulta para tempo de disponibilidade de estoque

access_token = ""
CATEGORY_ID = ""
url = f"https://api.mercadolibre.com/categories/{CATEGORY_ID}/sale_terms"

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
}

data = {
    "site_id": str,
    "title": str,
    "category_id": str,
    "price": float,
    "currency_id": "BR",
    "pictures": [{
        "source": "link da imagem"
    }],
    "buying_mode": str,
    "listing_type_id": str,
    "condition": ["new", "used"],
    "available_quantity": 10,
    "sale_terms": [{
        "id": "MANUFACTURING_TIME",
        "value_name": str
    }]
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Consulta de disponibilidade realizada com sucesso")
    print(response.text)
else:
    print(f"Erro ao consultar disponibilidade com Sucesso!: {response.status_code}")

# Modificar disponibilidade de estoque

access_token = ""
ITEM_ID = ""
url = f"https://api.mercadolibre.com/items/{ITEM_ID}"

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
}

data = {
    "sale_terms": [{
        "id": "MANUFACTURING_TIME",
        "value_name": str,
    }]
}

response = requests.put(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
    print("Modificação de estoque realizada com sucesso")
    print(response.text)

else:
    print(f"Erro ao modificar estoque com Sucesso!: {response.status_code}")

# Consultar tempo de disponibilidade de Estoque

access_token = ""
CATEGORY_ID = ""
url = f"https://api.mercadolibre.com/categories/{CATEGORY_ID}/sale_terms"

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Consulta de tempo de disponibilidade realizada com sucesso!")
    print(response.text)

else:
    print(f"Erro ao realizar consulta de tempo de disponibilidade com Sucesso!: {response.status_code}")
