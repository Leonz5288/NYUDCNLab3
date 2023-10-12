import json, socket

UDP_IP = '127.0.0.1'
UDP_PORT = 53533

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    print('Start to host UDP listener')
    while True:
        data, addr = sock.recvfrom(1024)
        print('received message: %s' % data)
        dl = data.decode('utf-8').split('\n')
        data_dict = {}
        for x in dl:
            xl = x.split('=')
            data_dict[xl[0]] = xl[1]
        if data_dict.get('VALUE') is None: # Receiving a DNS request.
            with open('dns_table.json', 'r') as openfile:
                json_obj = json.load(openfile)
                if json_obj['NAME'] == data_dict['NAME']: # Record found
                    msg = 'TYPE='+json_obj['TYPE']+'\nNAME='+json_obj['NAME']+'\nVALUE='+json_obj['VALUE']+'\nTTL='+json_obj['TTL']
                    sock.sendto(bytes(msg, 'utf-8'), (addr[0], addr[1]))
        else: # Receiving a registration request.
            # Saving record to DNS table.
            with open('dns_table.json', 'w') as outfile:
                outfile.write(json.dumps(data_dict, indent=4))
            msg = 'OK'
            sock.sendto(bytes(msg, 'utf-8'), (addr[0], addr[1]))
