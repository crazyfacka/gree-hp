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

def parse_msg(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        decoded_data = json.loads(str(data, 'utf-8'))
        decoded_pack64 = base64.b64decode(decoded_data['pack'])

        cipher = AES.new(bytes(AES_KEY, 'utf-8'), AES.MODE_ECB)
        print(cipher.decrypt(decoded_pack64))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('0.0.0.0', HP_PORT))

b_find_msg = json.dumps(FIND_MSG).encode('utf-8')
sock.sendto(b_find_msg, (HP_IP, HP_PORT))

parse_msg(sock)