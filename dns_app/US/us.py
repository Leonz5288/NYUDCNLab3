from flask import Flask, request

app = Flask('user_server')

@app.route('/fibonacci', methods=['GET'])
def ask_for_num():
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')
    if hostname is None or fs_port is None or number is None or as_ip is None or as_port is None:
        return 'Lack of Parameters', 400
    return str(number), 200

if __name__ == '__main__':
    app.run(port=8080)
