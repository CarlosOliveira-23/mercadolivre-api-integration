import requests


def book_pickup(bookingid, serviceurl):
    url = f"{serviceurl}/book_pickup/{bookingid}"
    response = requests.post(url)

    if response.status_code == 200:
        print("Coleta realizada com sucesso")
        print("Resposta do servidor:", response.status_code)
    else:
        print("Erro ao realizar coleta", response.text)


booking_id = "12345"
service_url = "https://carrierA/book_pickup/MzM3OTczMTM5fDIwMTgtMDctMjZ8MTc1MDA1NDA"

book_pickup(booking_id, service_url)


# Notificações de Eventos e Novidades

def send_notification(shipmentid, notificationdata, baseurl):
    url = f"{baseurl}/shipments/{shipmentid}/notification"
    response = requests.post(url, json=notificationdata)

    if response.status_code == 200:
        print("Notificação enviada com Sucesso!")
    else:
        print(f"Falha ao enviar Notificação. Status code: {response.status_code}")


shipment_id = "123"
notification_data = {"message": "Sua encomenda está a caminho!"}
base_url = "http://example.com/api"

send_notification(shipment_id, notification_data, base_url)


def main():
    pass


if __name__ == "__main__":
    main()
