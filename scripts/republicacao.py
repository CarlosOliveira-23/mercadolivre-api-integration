import requests

ACCESS_TOKEN = "seu_access_token"
ITEM_ID = ""
url = f"https://api.mercadolibre.com/items/{ITEM_ID}/relist"

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

data = {
    "price": None,
    "quantity": None,
    "listing_type_id": str
}

response = requests.post(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Erro: {response.status_code}")
