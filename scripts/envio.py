import json
import requests


def main():
    # Autorização Online
    url = 'http://example.com/shipments/shipment_id/authorization'
    payload = {'key1': 'value1', 'key2': 'value2'}
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Solicitação de Autorização Online bem sucedida!")
        print("Resposta do servidor:", response.text)
    else:
        print("Erro ao enviar solicitação de Autorização Online. Código de status:", response.status_code)

    # Autorização Offline
    url = 'https://carrier-host-name/trackingnumbers'
    payload = {'tracking_number': '1234567890'}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("\nSolicitação de Autorização Offline bem sucedida!")
        print("Resposta do servidor:", response.text)
    else:
        print("Erro ao enviar solicitação de Autorização Offline. Código de status:", response.status_code)

    # CD API Offline
    url = 'https://carrier-host-name/shipping/authorization/custom_data'
    payload = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("\nSolicitação da CD API Offline bem sucedida!")
        print("Resposta do servidor:", response.text)
    else:
        print("Erro ao enviar solicitação da CD API Offline. Código de status:", response.status_code)

    # Palavra chave
    url = 'https://api.mercadolibre.com/shipments/keyword_validation?access_token={accessToken}'
    payload = {'palavra chave'}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("\nSolicitação da Palavra chave bem sucedida!")
        print("Resposta do servidor:", response.text)
    else:
        print("Erro ao enviar solicitação da Palavra chave. Código de status:", response.status_code)

    # Cancelamento de Envio. ML fará um PUT para url de autorização
    url = 'service_url/shipments/{shipment_id}/authorization'
    response = requests.put(url, data=json.dumps)

    if response.status_code == 200:
        print("\nSolicitação de cacelamento realizado com sucesso")
        print("Resposta do servidor:", response.text)
    else:
        print("Erro ao enviar Cancelamento de Envio. Código de Status:", response.status_code)

    # Notificações das Agencias

    url = 'service_url/agencies'
    payload = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("\nSolicitação de Notificações das Agencias bem sucedida!")
        print("Resposta do servidor:", response.text)
    else:
        print("Erro ao receber notificação da Agecia. Código de Status:", response.text)

    # Notificação de Push

    country_id = 'BR'
    agency_id = 'agency_id'  # Substitua pelo agency_id correto
    access_token = 'accessToken'  # Substitua pelo access_token 
    url = f'service_url/agencies/{country_id}/{agency_id}/push?access_token={access_token}'
    payload = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("\nSolicitação de Notificação de Push bem sucedida!")
        print("Resposta do servidor:", response.text)
    else:
        print("Erro ao receber notificação de Push. Código de Status:", response.text)

    # Notificações Pull

    produto_id = ''
    tracking_number = ''
    url = f'https://hostname/produto/{produto_id}/tracking/{tracking_number}'
    response = requests.post(url, data=json.dumps)

    if response.status_code == 200:
        print("\nNotificação envidada com sucesso")
        print("resposta do Servidor:", response.text)
    else:
        print("Erro ao enviar Notificação. Código de Status:", response.text)

    # Rastreamento de Containers

    id = ''
    access_token = ''
    url = f'https://api.mercadolibre.com/tracking/{id}/notifications?access_token={access_token}'

    if response.status_code == 200:
        print("\nRastreamento de Containers realizado com sucesso")
        print("Resposta do servidor:", response.text)
    else:
        print("Erro ao enviar Rastreamento de Containers. Código de Status:", response.text)

    # Handling Unit (HU) Obtenção

    handling_unit = ''
    access_token = ''
    url = f'https://api.mercadolibre.com/handling_units/{handling_unit}?access_token={access_token}'

    response = requests.get(url)
    if response.status_code == 200:
        print("\nObtenção realizada com sucesso")
        print("Resposta do Servidor", response.text)
    else:
        print("Erro na Obtenção, Código de Status:", response.text)

    # Notificações de Eventos e Novidades (HU)

    shiment_id = ''
    url = f'https://hostname//shipments/steps/{shiment_id}/authorization?caller.scopes=admin'

    reponse = requests.post(url, data=json.dumps())
    if reponse.status_code == 200:
        print("\nNotificação enviada com sucesso")
        print("Resposta do Servidor", reponse.text)
    else:
        print("Erro ao enviar notificação. Código de Status", response.text)


if __name__ == "__main__":
    main()
