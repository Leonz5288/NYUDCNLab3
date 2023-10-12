import json, socket

UDP_IP = '127.0.0.1'
UDP_PORT = 53533

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    print('Start to host UPD listener')
    while True:
        data, addr = sock.recvfrom(1024)
        print('received message: %s' % data)
