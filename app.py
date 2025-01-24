from flask import Flask, request,jsonify 

import hashlib
import json



app = Flask(__name__)
APP_KEY = b"webhookhrithi"
@app.route('/webhook', methods=['POST'])
def handle_webhook():
    github_hook_id = request.headers.get('X-Github-Hook-ID')
    if not github_hook_id:
        return jsonify({'error':'Missing github ID'}),400
    try:
        payload = json.loads(request.get_data())
    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid JSON payload'}), 400
    print('Webhook received successfully Sample!')
    return 'Webhook'

if __name__ == '__main__':
    app.run(debug=True)