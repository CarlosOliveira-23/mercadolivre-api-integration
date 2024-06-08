import requests


def get_sale_price(access_token, item_id, channel, loyalty_level):
    url = f"https://api.mercadolibre.com/items/{item_id}/sale_price"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "context": f"{channel},{loyalty_level}"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        salepriceinfo = response.json()
        return salepriceinfo
    else:
        print(f"Erro ao obter informações do preço de venda do item {item_id}")
        return None


ACCESS_TOKEN = "seu_access_token"
ITEM_ID = "seu_item_id"
CHANNEL = "seu_canal"
LOYALTY_LEVEL = "seu_nivel_de_loyalty"

sale_price_info = get_sale_price(ACCESS_TOKEN, ITEM_ID, CHANNEL, LOYALTY_LEVEL)

if sale_price_info:
    price_id = sale_price_info.get("price_id", "N/A")
    amount = sale_price_info.get("amount", "N/A")
    regular_amount = sale_price_info.get("regular_amount", "N/A")
    currency_id = sale_price_info.get("currency_id", "N/A")
    reference_date = sale_price_info.get("reference_date", "N/A")
    metadata = sale_price_info.get("metadata", "N/A")
    promotion_id = sale_price_info.get("promotion_id", "N/A")
    promotion_type = sale_price_info.get("promotion_type", "N/A")
    
    print("Informações do Preço de Venda:")
    print(f"ID do Preço: {price_id}")
    print(f"Valor: {amount}")
    print(f"Valor Regular: {regular_amount}")
    print(f"Moeda: {currency_id}")
    print(f"Data de Referência: {reference_date}")
    print(f"Metadados: {metadata}")


# Obter preços dos produtos

def get_item_prices(access_token, item_id):
    url = f"https://api.mercadolibre.com/items/{item_id}/prices"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        pricesinfo = response.json()
        return pricesinfo
    else:
        print(f"Erro ao obter informações de preços do item {item_id}")
        return None


ACCESS_TOKEN = "seu_access_token"
ITEM_ID = "seu_item_id"

prices_info = get_item_prices(ACCESS_TOKEN, ITEM_ID)

if prices_info:
    for price_info in prices_info:
        price_id = price_info.get("id", "N/A")
        price_type = price_info.get("type", "N/A")
        amount = price_info.get("amount", "N/A")
        regular_amount = price_info.get("regular_amount", "N/A")
        currency_id = price_info.get("currency_id", "N/A")
        last_updated = price_info.get("last_updated", "N/A")

        print("Informações de Preços:")
        print(f"ID do Preço: {price_id}")
        print(f"Tipo de Preço: {price_type}")
        print(f"Valor: {amount}")
        print(f"Valor Regular: {regular_amount}")
        print(f"ID da Moeda: {currency_id}")
        print(f"Última Atualização: {last_updated}")
        print()
    