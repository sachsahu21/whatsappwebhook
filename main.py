from flask import Flask, request
import requests
 
app = Flask(__name__)
 
@app.route('/')

def index():
   return "Hello ATF"
 
def send_msg(sender_id,sender_name,message_text):
   
    message = 'Hi '+sender_name+'\n'+'\n'+'Thanks for messaging : '+message_text
    print(message)
    headers = {
        'Authorization': 'Bearer EAAN6DGKldRABAEAY2RP12Byy1BXNZCIduMS53gMXX6NSFiUINRSI7GlQFuaoiSda5lvj70XobNB1LUDYclYYQvgvx4pOzUZCQuraaFjpwoFzweChgOlzErH42Ii9DDXZCZAARyAi1ZC5NLCwxaCceNuXXAeVLJF4l30iFlO73U1ZC4bHD1t5hNzZA8oPN58AUqDIi0NlDVnYgZDZD',
    }
    json_data = {
        'messaging_product': 'whatsapp',
        'to': sender_id,
        'type': 'text',
        "text": {
            "body": message
        }
    }
    response = requests.post('https://graph.facebook.com/v17.0/108427882323095/messages', headers=headers, json=json_data)
    print(response.text)
 
 
# @app.route('/receive_msg', methods=['POST','GET'])
@app.route('/receive_msg', methods=['POST','GET'])


def webhook():
   
    # print('Request : ',request)
    # res = request.get_json()
    # raw_json = request.json
    # print('res : ',res)

    # try:
    #     if res['entry'][0]['changes'][0]['value']['messages'][0]['id']:
    #         send_msg("Thank you for the response.")
    # except:
    #     pass


    raw_json = request.get_json()
    # print('raw_json : ',raw_json)
    # print(raw_json['entry'][0]['changes'][0]['value']['messages'][0]['text']['body'])

    try:
        if raw_json['entry'][0]['changes'][0]['value']['messages'][0]['text']['body'] : 
            data = raw_json['entry'][0]['changes'][0]['value']
            sender_id = data['messages'][0]['from'] 
            sender_name = data['contacts'][0]['profile']['name']
            message_text = data['messages'][0]['text']['body']
            print(sender_id,sender_name,message_text)
            send_msg(sender_id,sender_name,message_text)
        
    except:
        print('except')
        pass

    return '200 OK HTTPS.'

# ---- the below code is to validate once 

    # if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
    #     if not request.args.get("hub.verify_token")== "123":
    #         return "Verification token missmatch", 403
    #     return request.args['hub.challenge'], 200
    # return "Hello world", 200
  


if __name__ == "__main__":
   app.run(port=8000,debug=True)