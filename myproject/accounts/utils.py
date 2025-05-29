import requests

def send_telegram_message(chat_id, message):
    token = '7597704596:AAFBPE1gZn48lD3p-VCvv7rKfAN5rok5XRw'
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}
    requests.post(url, data=data)