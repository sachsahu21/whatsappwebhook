from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Process the incoming data here (e.g., send a reply to WhatsApp)
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(debug=True)
