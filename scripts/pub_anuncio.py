import requests

# Substitua 'ACCESS_TOKEN' pelo seu token de acesso
ACCESS_TOKEN = ''

# URL para a qual você está enviando a solicitação POST
url_post = 'https://api.mercadolibre.com/items'

# URL para a qual você está enviando a solicitação GET para obter detalhes do item
url_item_details = 'https://api.mercadolibre.com/items/YOUR_ITEM_ID'

# URL para a qual você está enviando a solicitação GET para obter detalhes da categoria
url_category_details = 'https://api.mercadolibre.com/categories/YOUR_CATEGORY_ID'

# Cabeçalho padrão para incluir no pedido
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}


# Publicar produtos
def get_item_info(access_token, item_id):
    url = f"https://api.mercadolibre.com/items/{item_id}"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        item_info = response.json()
        return item_info
    else:
        print(f"Erro ao obter informações do item {item_id}")
        return None


ACCESS_TOKEN = "TEST-fd03783f-59cd-4b7f-b160-b8300ac76220"
ITEM_ID = "seu_item_id"

item_info = get_item_info(ACCESS_TOKEN, ITEM_ID)

if item_info:
    title = item_info.get("title", "N/A")
    category = item_info.get("category", "N/A")
    pictures = item_info.get("pictures", [])
    price = item_info.get("price", "N/A")
    city = item_info.get("city", "N/A")
    sold_quantity = item_info.get("sold_quantity", "N/A")
    questions = item_info.get("questions", [])
    sellers_reputation = item_info.get("sellers_reputation", "N/A")

    print("Informações do Item:")
    print(f"Título: {title}")
    print(f"Categoria: {category}")
    print(f"Fotos: {pictures}")
    print(f"Preço: {price}")
    print(f"Cidade: {city}")
    print(f"Quantidade vendida: {sold_quantity}")
    print(f"Perguntas: {questions}")
    print(f"Reputação do vendedor: {sellers_reputation}")

# Solicitação POST para criar um item
response_post = requests.post(url_post, headers=headers, json={})
if response_post.status_code == 201:
    print("Item criado com sucesso!")
    print("ID do item:", response_post.json()['id'])
else:
    print("Falha ao criar o item. Código de status:", response_post.status_code)

# Solicitação GET para obter detalhes do item
response_get_item = requests.get(url_item_details, headers=headers)
if response_get_item.status_code == 200:
    item_data = response_get_item.json()
    print("Detalhes do Item:")
    print("ID:", item_data['id'])
    print("Título:", item_data['title'])
    print("Preço:", item_data['price'])
    print("Disponibilidade:", item_data['available_quantity'])
    print("Condição:", item_data['condition'])
else:
    print("Falha ao obter detalhes do item. Código de status:", response_get_item.status_code)

# Solicitação GET para obter detalhes da categoria
response_get_category = requests.get(url_category_details, headers=headers)
if response_get_category.status_code == 200:
    category_data = response_get_category.json()
    print("Detalhes da Categoria:")
    print("ID:", category_data['id'])
    print("Nome:", category_data['name'])
    print("Imagem:", category_data['picture'])
    print("Total de itens nesta categoria:", category_data['total_items_in_this_category'])
else:
    print("Falha ao obter detalhes da categoria. Código de status:", response_get_category.status_code)
