from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the incoming message from the user
    incoming_message = request.form.get('Body')

    # Make a GET request to the API with the incoming message
    response = requests.get(f'https://widipe.com/Gemini?query={incoming_message}')
    
    # Send the API response back to the user
    return response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
