from base64 import b64decode

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
import ast


class Decrypt:
    def decrypt_req(self):
        f = open('final_data.txt', 'r')
        req = ast.literal_eval(f.read())
        self.private_decrypt(req['data'], req['secret'])

    def private_decrypt(self, data, secret):
        private_key = RSA.import_key(open('private.pem', 'r').read())
        cipher = PKCS1_OAEP.new(key=private_key)
        dec_data = cipher.decrypt(b64decode(secret))
        dec_data = ast.literal_eval(dec_data.decode())
        key = dec_data['key']
        iv = dec_data['iv']
        self.aes_decrypt(AES.MODE_GCM, key, iv, data)

    def aes_decrypt(self, mode, key, iv, data):
        cipher = AES.new(key, mode, iv)
        decrypted = cipher.decrypt(b64decode(data))
        print(type(ast.literal_eval(decrypted.decode())))
        print('*='*30)
        print(decrypted.decode())


api = Decrypt()
api.decrypt_req()
