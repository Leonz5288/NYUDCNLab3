from flask import Flask, request
import socket, requests

app = Flask('user_server')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

@app.route('/fibonacci', methods=['GET'])
def ask_for_num():
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')
    if hostname is None or fs_port is None or number is None or as_ip is None or as_port is None:
        return 'Lack of Parameters', 400
    print('Finding ip')
    msg = 'TYPE=A\nNAME='+hostname
    sock.sendto(bytes(msg, 'utf-8'), ('127.0.0.1', 53533))
    data, addr = sock.recvfrom(1024)
    dl = data.decode('utf-8').split('\n')
    print('Got id')
    print(dl)
    ip = dl[2].split('=')[1]
    url = 'http://'+ip+':9090/fibonacci?number='+number
    r = requests.get(url)
    return r.text, 200

if __name__ == '__main__':
    sock.bind(('127.0.0.1', 0))
    app.run(port=8080)
