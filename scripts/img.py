# Imagens nos anuncios

# Validar e carregar uma imagem

import subprocess

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

# Defina seu ACCESS_TOKEN e o caminho do arquivo que você deseja fazer upload
ACCESS_TOKEN = 'seu_token_de_acesso'
file_path = '/caminho/para/seu/arquivo.extensao'

# URL da API
url = 'https://api.mercadolibre.com/pictures/items/upload'

# Cabeçalhos da requisição
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'multipart/form-data'
}

# Configuração do multipart encoder
multipart_data = MultipartEncoder(
    fields={
        'file': (file_path, open(file_path, 'rb'), 'image/jpeg')  # Substitua 'image/jpeg' pelo tipo MIME correto do
        # seu arquivo
    }
)

# Cabeçalhos da requisição
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': multipart_data.content_type  # Define o tipo de conteúdo como multipart
}

# Fazendo a requisição POST
response = requests.post(url, headers=headers, data=multipart_data)

# Verifica se a requisição foi bem-sucedida (código 200)
if response.status_code == 200:
    response_data = response.json()
    print(response_data)  # Exibe os dados retornados pela API
else:
    print(f"Erro ao fazer a requisição: {response.status_code}")

# Vincular uma imagem ao produto

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

data = {
    "id": "MLA430387888_032012"
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    response_data = response.json()
    print(response_data)
else:
    print(f"Erro ao fazer a requisição: {response.status_code}")

# Substituir imagens

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

data = {
    "pictures": [
        {"source": "http://www.apertura.com/export/sites/revistaap/img/Tecnologia/Logo_ML_NUEVO.jpg_33442984.jpg"},
        {"source": "http://appsuser.net/www/wp-content/uploads/2012/10/logo-mercadolibre.jpg"}
    ]
}

response = requests.put(url, headers, json=data)

if response.status_code == 200:
    response_data = response.json()
    print(response_data)
else:
    print(f"Erro ao fazer a requisição: {response.status_code}")

# Revisar possiveis erros

url = 'https://api.mercadolibre.com/pictures/$PICTURE_ID/errors'

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    response_data = response.json()
    print(response_data)
else:
    print(f"Erro ao fazer a requisição: {response.status_code}")


# Formato da Imagem

def download_image(url):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open('image.jpg', 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
        else:
            print('Failed to download image:', response.status_code)
    except Exception as e:
        print('Exception occurred:', str(e))


def main():
    image_url = 'link da imagem'
    download_image(image_url)

    try:
        subprocess.run(['echo', 'link da imagem'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print('Exception occurred during subprocess:', str(e))

    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}

    response = requests.get(url, headers=headers)
    print(response.content)

    # Baixar imagem diretamente pela API

    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Abre o arquivo para escrita binária ('wb')
        with open('146.111111.jpg', 'wb') as f:
            # Escreve o conteúdo da resposta no arquivo
            f.write(response.content)
        print("Download concluído.")
    else:
        print(f"Erro ao baixar: {response.status_code}")


if __name__ == "__main__":
    main()
