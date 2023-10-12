from flask import Flask, request
import json, socket

app = Flask('fibonacci_server')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

@app.route('/register', methods=['PUT'])
def register():
    payload = request.get_json()
    hostname = payload['hostname']
    ip = payload['ip']
    as_ip = payload['as_ip']
    as_port = payload['as_port']
    msg = 'TYPE=A\nNAME='+hostname+'\nVALUE='+ip+'\nTTL=10'
    sock.sendto(bytes(msg, 'utf-8'), (as_ip, int(as_port)))
    data, addr = sock.recvfrom(1024)
    if data.decode('utf-8') == 'OK':
        return 'Success', 201
    return 'Failure', 400

@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    number = request.args.get('number')
    if number is None:
        return 'Lack of Parameter', 400
    try:
        number = int(number)
    except ValueError:
        return 'Bad Format', 400
    return str(fib_helper(number)), 200

def fib_helper(x):
    if x == 0:
        return 0
    if x == 1 or x == 2:
        return 1
    return fib_helper(x-1) + fib_helper(x-2)

if __name__ == '__main__':
    sock.bind(('127.0.0.1', 0))
    app.run(port=9090)
