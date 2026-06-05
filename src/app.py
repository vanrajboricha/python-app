from flask import Flask, jsonify
from datetime import datetime
import socket
app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    #return "<h1>Hello, Flask!</h1>"
    now = datetime.now()

    return jsonify({
        "current_date": now.strftime("%Y-%m-%d"),
        "current_time": now.strftime("%H:%M:%S"),
        "timestamp": now.isoformat(),
        'hostname': socket.gethostname(),
        'message': 'you are doing great, Vanraj!!!'
    })

@app.route('/api/v1/healthz')
def health():
    return jsonify({
        'status': 'up'
    }), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0")
#'/api/v1/details'
#'/api/v1/healthz'