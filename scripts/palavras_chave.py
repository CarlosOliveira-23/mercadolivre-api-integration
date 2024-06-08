import requests

access_Token = ""
url = "https://api.mercadolibre.com/shipments/keyword_validation?access_token={accessToken}"
params = {
    "keyword": str,
    "method": ["online", "offline"],
    "driver_id": float, 
    "shipments_ids": float,
}

response = requests.post(url)
if response.status_code == 200:
    print("Entrada da palavra chave válida!")
    print("Resposta:")
    print(response.json())
else:
    print("Palvra chave invalida:", response.text)
    print("Código de status:", response.status_code)
