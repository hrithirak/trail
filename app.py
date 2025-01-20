from flask import Flask, request

app = Flask(__name__)

@app.route('/github/webhook', methods=['POST'])
def handle_webhook():
    
    return 'Webhook received successfully!'

if __name__ == '__main__':
    app.run(debug=True)