# Modificar Imagens

import json

import requests

# Defina o token de acesso
ACCESS_TOKEN = ''

# URL do endpoint
url = 'https://api.mercadolibre.com/items/MLA658778048'

# Cabeçalhos da requisição
headers = {
    'Authorization': 'Bearer ' + ACCESS_TOKEN,
    'Content-Type': 'application/json'
}

# Corpo da requisição
data = {
    "pictures": [
        {"source": "http://www.apertura.com/export/sites/revistaap/img/Tecnologia/Logo_ML_NUEVO.jpg_33442984.jpg"},
        {"source": "http://static.ellahoy.es/ellahoy/fotogallery/1200X0/371265/falda-plisada-rosa.jpg"},
        {"id": "553111-MLA20482692355_112015"},
        {"id": "629425-MLA25446587248_032017"}
    ],
    "variations": [
        {
            "id": 18200178910,
            "picture_ids": [
                "http://static.ellahoy.es/ellahoy/fotogallery/1200X0/371265/falda-plisada-rosa.jpg",
                "553111-MLA20482692355_112015"
            ]
        },
        {
            "id": 18200178913,
            "picture_ids": [
                "http://www.apertura.com/export/sites/revistaap/img/Tecnologia/Logo_ML_NUEVO.jpg_33442984.jpg",
                "629425-MLA25446587248_032017"
            ]
        }
    ]
}

# Convertendo o corpo da requisição para JSON
data_json = json.dumps(data)

# Fazendo a requisição PUT
response = requests.put(url, headers=headers, data=data_json)

# Imprimindo a resposta
print(response.json())
