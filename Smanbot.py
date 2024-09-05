from flask import Flask, request
import requests

app = Flask(__name__)

commands = {}

def execute_command(command_code):
    try:
        exec_globals = {}
        exec(command_code, exec_globals)
        return exec_globals.get('output', 'No output returned.')
    except Exception as e:
        return f"Error executing command: {str(e)}"

@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_message = request.form.get('Body')
    sender = request.form.get('From')

    if incoming_message.startswith('cmd install '):
        command_code = incoming_message[len('cmd install '):]
        commands[sender] = command_code
        return "New command installed successfully!"

    elif sender in commands:
        response = execute_command(commands[sender])
        return response

    else:
        response = requests.get('https://widipe.com/Gemini')
        return response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
