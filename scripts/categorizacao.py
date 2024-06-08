# Categorização dos produtos
import requests

ACCESS_TOKEN = "seu_access_token"
SITE_ID = "seu_site_id"
Q = "sua_pesquisa"

url = f"https://api.mercadolibre.com/sites/{SITE_ID}/domain_discovery/search?q={Q}"

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()

    # Processar os dados
    for item in data['results']:
        domain_id = item['domain_id']
        domain_name = item['domain_name']
        category_id = item['category_id']
        category_name = item['category_name']
        attributes = item['attributes']

        print(f"domain_id: {domain_id}")
        print(f"domain_name: {domain_name}")
        print(f"category_id: {category_id}")
        print(f"category_name: {category_name}")
        print(f"attributes: {attributes}")
else:
    print(f"Erro: {response.status_code}")

# Categoria por site


url = f"https://api.mercadolibre.com/sites/{SITE_ID}/categories"

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:

    data = response.json()

    for category in data:
        category_id = category['id']
        category_name = category['name']

        print(f"category_id: {category_id}")
        print(f"category_name: {category_name}")
else:
    print(f"Erro: {response.status_code}")

# Detalhe de uma categoria Isolada

url = 'https://api.mercadolibre.com/categories/$CATEGORY_ID'

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    category_id = data['id']
    category_name = data['name']
    print(f"category_id: {category_id}")
    print(f"category_name: {category_name}")
else:
    print(f"Erro: {response.status_code}")

# Atributo para uma etiqueta simples, pois nao pode ser usado etiqueta para buscar produtos, buscar usando ID de
# categorias...

url = "https://api.mercadolibre.com/sites/MLA/search?category=MLA5726"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()

else:
    print(f"Erro: {response.status_code}")
