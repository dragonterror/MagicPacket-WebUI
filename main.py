from flask import Flask, render_template, request
from wakeonlan import send_magic_packet

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    mac_address = request.form['mac_address']
    send_magic_packet(mac_address)
    return "Magic packet sent!"

if __name__ == '__main__':
    app.run()