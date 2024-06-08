import requests


def main():
    accesstoken = ""
    shipmentid = ""
    url = f"https://api.mercadolibre.com/shipments/{shipmentid}/documents/cbt_invoice?access_token={accesstoken}"

    response = requests.get(url)
    if response.status_code == 200:
        print("Pedido Entregue com sucesso!")
        print("Resposta do Servidor", response.status_code)
    else:
        print("Erro ao Obter documento!", response.text)


# Label

def get_label(shipment_id, access_token, response_type):
    url = f'https://api.mercadolibre.com/shipments/{shipment_id}/documents/cbt_label'
    params = {
        "access_token": access_token,
        "response_type": response_type
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        print("Documento Baixado com Sucesso!")
    else:
        print(f"Erro ao Baixar documento. Status code: {response.status_code}")


shipment_id = "12345"
access_token = "seu_access_token"
response_type = "seu_tipo_de_resposta"

get_label(shipment_id, access_token, response_type)

if __name__ == "__main__":
    main()
