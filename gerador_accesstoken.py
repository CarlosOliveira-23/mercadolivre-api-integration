import requests


def refresh_access_token():
    refresh_token = 'INSIRA SEU TG AQUI'
    client_id = 'Insira seu client_id'
    client_secret = 'Insira seu client_secret'
    url = "https://api.mercadolibre.com/oauth/token"

    payload = (f'grant_type=refresh_token&client_id={client_id}&client_secret={client_secret}&refresh_token='
               f'{refresh_token}')
    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        token_data = response.json()
        new_access_token = token_data['access_token']
        print(f'Novo Access Token: {new_access_token}')
    else:
        print('Erro ao atualizar o Access Token')


# while True:
#     refresh_access_token()
#     time.sleep(60 * 60 * 6)
