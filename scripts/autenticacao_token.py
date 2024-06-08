import secrets

import requests

url = 'https://api.mercadolibre.com/oauth/token'

# Parâmetros da solicitação
payload = {
    'grant_type': 'authorization_code',
    'client_id': '',
    'client_secret': '',
    'code': '',
    'redirect_uri': 'https://127.0.0.1:8000/'
}

headers = {
    'accept': 'application/json',
    'content-type': 'application/x-www-form-urlencoded'
}

response = requests.post(url, data=payload, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("Token de acesso:", data['access_token'])
else:
    print("Erro:", response.status_code, response.text)

# Gerar um número aleatório seguro
random_number = secrets.randbelow(100)

print(random_number)

#################################################################


token = '4581772277609371'

headers = {
    'Authorization': f'Bearer {token}'
}

#
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Solicitação bem-sucedida!")
    print("Conteúdo da resposta:", response.json())
else:
    print("Erro:", response.status_code, response.text)
