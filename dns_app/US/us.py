from flask import Flask, request

app = Flask('user_server')

@app.route('/fibonacci')
def ask_for_num():
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')
    return str(hostname) + str(as_ip)

if __name__ == '__main__':
    app.run(port=8080)
