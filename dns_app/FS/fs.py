from flask import Flask, request
import json, socket

app = Flask('fibonacci_server')

@app.route('/register', methods=['PUT'])
def register():
    payload = request.get_json()
    hostname = payload['hostname']
    ip = payload['ip']
    as_ip = payload['as_ip']
    as_port = payload['as_port']
    msg = 'TYPE=A\nNAME='+hostname+'\nVALUE='+ip+'\nTTL=10'
    sock = socket.socket(socket.AFINET, socket.SOCK_DGRAM)
    sock.sendto(bytes(msg, 'utf-8'), (as_ip, as_port))
    return str(number), 201

@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    number = request.args.get('number')
    if number is None:
        return 'Lack of Parameter', 400
    if type(number) is not int:
        return 'Bad Format', 400
    return number, 200

if __name__ == '__main__':
    app.run(port=9090)
