import requests


def main():
    # Substitua 12345678 pelo ID da rota e accessToken pelo seu token de acesso real
    route_id = '12345678'
    access_token = 'seu_access_token'
    offset = 0
    limit = 3

    url = (f'https://api.mercadolibre.com/routes/{route_id}/fiscal-info?offset={offset}&limit={limit}'
           f'&access_token={access_token}')

    response = requests.get(url)

    if response.status_code == 200:
        print("Solicitação bem sucedida!")
        print("Resposta do servidor:", response.json())
    else:
        print("Erro ao enviar solicitação. Código de status:", response.status_code)

    # Consulta de Informações Fiscais para MWH 

    hug_id = '0'
    offset = '0'
    token = ''
    url = f'https://api.mercadolibre.com/dispatches/{hug_id}/fiscal-info?access_token={token}&offset={offset}'
    response = requests.get(url)
    if response.status_code == 200:
        print("Consulta realizada com suceso!")
        print("Resposta do Servidor:", response.json())
    else:
        print("Erro na Consulta, Código de Status:", response.status_code)

    # Consulta da CTE de MWH

    chave_cte = '123456789'
    url = f'https://api.mercadolibre.com/shipments/cte/{chave_cte}?access_token={token}&doctype=xml'
    response = requests.get(url)
    if response.status_code == 200:
        print("Consulta CTE realizada com Sucesso")
        print("Reposta do Servidor:", response.status_code)
    else:
        print("Erro ao Realizar consulta CTE, Código de Status:", response.status_code)

    # Consulta de CT-e

    shipment_id = ''
    url = f'https://api.mercadolibre.com/shipments/{shipment_id}/cte?doctype=xml&access_token=<accessToken>'
    response = requests.get(url)
    if response.status_code == 200:
        print("Consulta CT-e realizada com Sucesso")
        print("Reposta do Servidor:", response.status_code)
    else:
        print("Erro ao consultar CTE", response.text)

    # Obtenção de dados fiscais de envio

    shipmentid = ''
    url = f'https://api.mercadolibre.com/dispatches/{shipmentid}/fiscal-info?access_token={token}'
    response = requests.get(url)
    if response.status_code == 200:
        print("Dados Obtidos com sucesso!")
        print("Resposta do Servidor:", response.status_code)
    else:
        print("Erro ao Obter dados Fiscais", response.text)

    # Após a requisição acima fazer a consulta dados de invoice, ele devera percorrer
    #  download do cml utlizando a url contida em fiscal_data.tax.document.href (lembrando que é necessário adicionar
    #  o token de segurança na requisição).

    cte_key = ''
    access_token = ''
    url = f'https://api.mercadolibre.com/shipments/cte/{cte_key}?doctype=xml&access_token={access_token}'
    response = requests.get(url)
    if response.status_code == 200:
        print("Dados Obtidos e download realizado com sucesso!")
        print("Resposta do Servidor:", response.status_code)
    else:
        print("Erro ao obter dados e realizar download do XML", response.text)

    # Consulta de informações Fiscais para Shipment

    shipmentid = ''
    url = f'https://api.mercadolibre.com/shipments/{shipmentid}/fiscal-info?access_token={token}'
    response = requests.get(url)
    if response.status_code == 200:
        print("Consulta de Informações via Shipment realizada com sucesso!")
        print("Resposta do Servidor:", response.status_code)
    else:
        print("Erro ao realizar consulta de Informações via Shipment", response.text)

    # Consulta de Informarções Fiscais para Logstics

    url = f'https://api.mercadolibre.com/routes/12345678/fiscal-info?offset=0&limit=3&access_token=accessToken'
    response = requests.get(url)
    if response.status_code == 200:
        print("Consulta de Informações Fiscais para Logstics realizada com sucesso!")
        print("Resposta do Servidor:", response.status_code)
    else:
        print("Falha ao realizar consulta de Informações Fiscais para Logstics", response.text)

    # Consulta de Listagem de rotas para CT-e de Redespacho

    url = 'https://api.mercadolibre.com/MLB/routes/redispatch'
    response = requests.get(url)
    if response.status_code == 200:
        print("Consulta de Listagem para CT-e de redespacho realizada com Sucesso")
        print("Resposta do Servidor:", response.status_code)
    else:
        print("Falha ao realizar consulta de listagem para CTE de redespacho", response.text)

    # Consulta de listagem de CT-e para Redespacho

    route_id = '123'
    token = ''
    page = '1'
    limit = '100'
    url = (f'https://api.mercadolibre.com/MLB/routes/{route_id}/redispatch/fiscal-info?access_token={token}&page={page}'
           f'&limit={limit}')
    response = requests.get(url)
    if response.status_code == 200:
        print("Consulta CT-e para Redespacho realizada com sucesso")
        print("Reposta do Servidor:", response.status_code)
    else:
        print("Falha ao consultar CT-e para Redespacho", response.text)

    # Download de CT-e de redespacho

    route_id = '123'
    shipment_id = ''
    cte_key = ''
    token = ''
    url = (f'https://api.mercadolibre.com/MLB/routes/{route_id}/shipments/{shipment_id}/cte/{cte_key}?doctype=xml'
           f'&access_token={token}')
    response = requests.get(url)
    if response.status_code == 200:
        print("Download da CT-e para Redespacho realizado com sucesso!")
        print("Resposta do Servidor:", response.status_code)
    else:
        print("Falha ao realizar download da CT-e para redespacho", response.text)


if __name__ == "__main__":
    main()
