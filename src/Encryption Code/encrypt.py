import json
from base64 import b64encode

from Crypto import Random
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
import ast

from rsa import PrivateKey


class Encrypt:

    def encrypt_data(self):
        # open the file containing the credentials
        f = open('credentials.json', encoding='utf-8')
        credentials = ast.literal_eval(f.read())
        
        key, iv = Random.new().read(32), Random.new().read(16)
        credentials = self.aes_encrypt(AES.MODE_GCM, credentials, key, iv)
        secret = {"key": key, "iv": iv}
        secret = str(secret).encode('utf-8')
        secrets = self.public_encrypt(secret)

        final_data = {'data': credentials.decode('utf-8'), 'secret': secrets.decode('utf-8')}
        final_data_json = json.dumps(final_data, indent=4)
        print(final_data)

        f = open('final_data.txt', 'w')
        f.write(str(final_data))
        with open('final_data.json', 'w') as outfile:
            outfile.write(final_data_json)
        f.close()

    def public_encrypt(self, data):
        keys = RSA.generate(2048)
        public_key = keys.publickey().export_key()
        private_key = keys.export_key()

        f = open('public.pem','wb')
        f.write(public_key)
        f.close()

        f = open('private.pem','wb')
        f.write(private_key)
        f.close()
        #public_key = RSA.import_key(open('public.pem', 'r').read())
        

        if type(data) == str:
            data = data.encode('utf-8')
        elif type(data) == dict:
            data = str(json.dumps(data)).encode('utf-8')
        if type(data) == bytes:
            cipher = PKCS1_OAEP.new(key=keys)
            return b64encode(cipher.encrypt(data))
        raise TypeError('can only encrypt the following types str, dict, bytes')

    def aes_encrypt(self, mode, message, key, iv):
        if type(message) == str:
            message = message.encode('utf-8')
        elif type(message) == dict:
            message = str(json.dumps(message)).encode('utf-8')
        if type(message) == bytes:
            cipher = AES.new(key, mode, iv)
            return b64encode(cipher.encrypt(message))
        raise TypeError('can only encrypt the following types str, dict, bytes')

api = Encrypt()
api.encrypt_data()