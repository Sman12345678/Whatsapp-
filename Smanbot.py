from flask import Flask, request
import requests

app = Flask(__name__)

VERIFY_TOKEN = 'EABo0otZAZCJe4BO3ASLTO7QYNDm7RWd2Tt1XX6Fzc4E58DIqQCo3MDGGNudP4hLKd6o13bh2P4vMqPhc9vY0u5iTCdRzwFN8XRgQtup4bVaVycuUZCBL1eWX4joIPDqae5yweuYjuunV9oHZBm6CcKcCYgCWOzPrOU9pWyj3GlZBSO98uRIlSiNZCw7kzjUifE1dIaA1CIl09Twmpesv4ZD'

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Verification request
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if mode and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return 'Verification token mismatch', 403

    elif request.method == 'POST':
        # Handle incoming messages
        incoming_message = request.form.get('Body')

        # Make a GET request to the API with the incoming message
        response = requests.get(f'https://widipe.com/Gemini?query={incoming_message}')
        
        # Send the API response back to the user
        return response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
