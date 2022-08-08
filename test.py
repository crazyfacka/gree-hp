import base64
import json
import socket

from Crypto.Cipher import AES

HP_IP = '192.168.5.204'
HP_PORT = 7000

AES_KEY = 'a3K8Bx%2r8Y7#xDh'

FIND_MSG = {
    't': 'scan'
}

### Initialization ###
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', HP_PORT))
###

def parse_msg(msg):
    decoded_pack64 = base64.b64decode(msg['pack'])
    cipher = AES.new(AES_KEY.encode('utf-8'), AES.MODE_ECB)
    return cipher.decrypt(decoded_pack64)[:-2]

def send_msg(msg):
    b_msg = json.dumps(msg).encode('utf-8')
    sock.sendto(b_msg, (HP_IP, HP_PORT))

def receive_msg(sock):
    data, addr = sock.recvfrom(1024)
    decoded_data = json.loads(data)
    return decoded_data

send_msg(FIND_MSG)
pack = parse_msg(receive_msg(sock))
print(json.loads(pack))