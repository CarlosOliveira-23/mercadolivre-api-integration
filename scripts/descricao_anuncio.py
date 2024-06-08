import requests

ACCESS_TOKEN = ""
ITEM_ID = "seu_item_id"

# URL para obter e atualizar a descrição do item
url_get_description = f"https://api.mercadolibre.com/items/{ITEM_ID}/description"
url_update_description = f"https://api.mercadolibre.com/items/{ITEM_ID}/description?api_version=2"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

response = requests.get(url_get_description, headers=headers)

if response.status_code == 200:
    description_data = response.json()
    print("Descrição atual do item:")
    print(description_data)
else:
    print(f"Erro ao obter a descrição do item. Código de status: {response.status_code}")

new_description_data = {
    "plain_text": "Descrição com Texto Plano\n"
}

response_put = requests.put(url_update_description, headers=headers, json=new_description_data)

if response.status_code == 200:
    print("Descrição do item atualizada com sucesso.")
else:
    print(f"Erro ao atualizar a descrição do item. Código de status: {response.status_code}")

# Substituir Descrição Existente


url_update_description = f"https://api.mercadolibre.com/items/{ITEM_ID}/description?api_version=2"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

new_description_data = {
    "plain_text": "Test."
}

response = requests.put(url_update_description, headers=headers, json=new_description_data)

if response.status_code == 200:
    print("Descrição do item atualizada com sucesso.")
else:
    print(f"Erro ao atualizar a descrição do item. Código de status: {response.status_code}")

url_update_description = f"https://api.mercadolibre.com/items/$ITEM_ID/description?api_version=2"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

new_description_data = {
    "plain_text": "Update Test."
}

if response.status_code == 200:
    print("Descrição do item modificada sucesso.")
else:
    print(f"Erro ao modificar descrição do item")
