import requests

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Extract incoming message details
    sender = data['messages'][0]['from']
    message = data['messages'][0]['text']

    # Process the message (you can implement your custom logic here)
    response_text = f"Received message '{message}' from {sender}."

    # Send a reply to the user
    send_whatsapp_message(sender, response_text)

    return jsonify({'status': 'success'})

def send_whatsapp_message(receiver = '6581317616', message):
    # Replace 'YOUR_ACCESS_TOKEN' with the actual access token from your WhatsApp Business API account
    access_token = 'EAAN6DGKldRABAPJFnESuoLSXXWCFTVFvVMAfwFXDmrPGrlEcIBXZCk9kebotQi8XzGuAxQKTjTIUBY71QSOjbptFJ3wHv9ZAK9qP6cYg11ZB56SZCv0BNrc1VNNvAY0STxhwMP5ChNSTBAZBlPmNNxE3whlXM0yu83wIipJ0TMZB4eG9VWuuu5ABsZBgw8yQs1HtMdRu6ZADBgZDZD'
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}'}
    payload = {'phone': receiver, 'message': message}

    # Send the message using WhatsApp Business API
    response = requests.post('https://graph.facebook.com/v17.0/108427882323095/messages', json=payload, headers=headers)

    return response.json()
