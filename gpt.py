# https://github.com/Spidy20/ChatGPT_Whatsapp_Bot/blob/master/BOT_API.py


from flask import Flask, request
import openai
# from twilio.twiml.messaging_response import MessagingResponse
import os
import requests


# Init the Flask App
app = Flask(__name__)

# Initialize the OpenAI API key
# export OPENAI_API_KEY=YOUR API KEY
# openai.api_key = os.environ.get("OPENAI_API_KEY")
openai.api_key  = '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'


# Define a function to generate answers using GPT-3
def generate_answer(question):

    print(question)
    model_engine = "text-davinci-002"
    prompt = (f"Q: {question}\n"
              "A:")
    
    print(prompt)

    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    answer = response.choices[0].text.strip()
    return answer


def make_request(sender_id,sender_name,message_text):
      
    message = 'Hi '+sender_name+'\n'+'\n'+'Thanks for messaging : '+message_text
    # print(message)
    url = "https://api.openai.com/v1/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai.api_key}",
    }

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": f"Say this is a test!{message}"}],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        print("Generated Text:")
        print(data["choices"][0]["message"]["content"])
    else:
        print("Request failed with status code:", response.status_code)
        print("Response content:", response.text)


# ------------



# Define a route to handle incoming requests
@app.route('/receive_msg',  methods=['POST','GET'])
def chatgpt():

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
           
            
            data = raw_json['entry'][0]['changes'][0]['value']
            sender_id = data['messages'][0]['from'] 
            sender_name = data['contacts'][0]['profile']['name']
            message_text = data['messages'][0]['text']['body']


            print(sender_id,sender_name,message_text)
            print(openai.api_key)
            # make_request(sender_id,sender_name,message_text)

            # Generate the answer using GPT-3
            # answer = generate_answer(message_text)
            # print("BOT Answer: ", answer)
            # bot_resp = MessagingResponse()
            # msg = bot_resp.message()
            # msg.body(answer)
            
        except:
            print('except')
            pass

        # raw_json = request.get_json()
        # message_text = raw_json['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
        # # print("Question: ", message_text)
        # # Generate the answer using GPT-3

        answer = generate_answer(message_text)
        # make_request(sender_id,sender_name,message_text)
        
        print("BOT Answer: ", answer)
        bot_resp = MessagingResponse()
        msg = bot_resp.message()
        msg.body(answer)
        return str(bot_resp)
        return 'gpt code'

    return '200 - Working OK HTTPS.'



# Run the Flask app
if __name__ == '__main__':

    # app.run(host='0.0.0.0', debug=False, port=8000)
    app.run(port=8000,debug=True)