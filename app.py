from flask import Flask, request,jsonify 
import json
import os 
os.environ['APP_ID'] =  '1119711'
os.environ['APP_WEBHOOK_SECERT'] = "hrithiwebhook"
os.environ['APP_CLIENT_ID'] = "Iv23li6xO8obaZANu92V"
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
   # github_webhooks_value = request.args.get('Github-webhooks')
    #if github_webhooks_value:
     #   print(github_webhooks_value)
    #else:
     #   return "Github-webhooks parameter not found", 400
    event = request.headers.get('X-Github-Event')
    # if not event:
    #     return "event not found"
    # else:
    #     return "event found"
    # github_hook_id = request.headers.get('X-Github-Hook-ID')
    # print(github_hook_id)
    # if not github_hook_id:
    #     return jsonify({'error':'Missing github ID'}),400
    try:
        payload = json.loads(request.get_data())
        print(payload)
    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid JSON payload'}), 400
    print('Webhook received successfully Sample!')
    return 'DEV'


if __name__ == '__main__':
    app.run(debug=True)
