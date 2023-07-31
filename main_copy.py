# Refer the below Website
# https://www.pragnakalp.com/automate-messages-using-whatsapp-business-api-flask-part-1/

from flask import Flask, request,jsonify
import requests
 
app = Flask(__name__)
 
@app.route('/')

def index():
   return "Hello ATF"
 
def send_msg(sender_id,sender_name,message_text):
   
    message = 'Hi '+sender_name+'\n'+'\n'+'Thanks for messaging : '+message_text
    # print(message)
    url = "https://graph.facebook.com/v17.0/108427882323095/messages"
    access_token = 'EAAN6DGKldRABO6rRYbf9ih6Q9d0HEQ1tZAcgZC6uT2eAsb9BiHxyksfz7NfeMGKFQ7P2CAOY9oOPEDulEHqf7TUi0wFylJaagI9oxfLyvTGKsuwZALZCgT5swGB8bGwQUe3ggTWYEoUOzH3qtXZC2CqGl5VRlMvhThEFEaREjzysvrRfZCVoBLYt2xIVZCRTGXSuhwOy1SktlZB50Hp7Q5ay'

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    json_data = {
        'messaging_product': 'whatsapp',
        'to': sender_id,
        'type': 'text',
        "text": {
            "body": message
        }
    }

    response = requests.post(url, headers=headers, json=json_data)
    print('send_msg response text',response.text)
 
@app.route('/receive_msg', methods=['POST','GET'])


def webhook():
    if request.method == 'GET':
        # Webhook verification
        if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
            if not request.args.get("hub.verify_token")== "123":
                return "Verification token missmatch", 403
            return request.args['hub.challenge'], 200
        return "Hello world", 200

    elif request.method == 'POST':
        raw_json = request.get_json()
        try:
            # if raw_json['entry'][0]['changes'][0]['value']['messages'][0]['text']['body'] : 
            data = raw_json['entry'][0]['changes'][0]['value']
            sender_id = data['messages'][0]['from'] 
            sender_name = data['contacts'][0]['profile']['name']
            message_text = data['messages'][0]['text']['body']
            # print(sender_id,sender_name,message_text)
            send_msg(sender_id,sender_name,message_text)
            return "Worked"
            
        except:
            # print('except')
            pass

    return '200 OK HTTPS.'


if __name__ == "__main__":
   app.run(port=8000,debug=True)