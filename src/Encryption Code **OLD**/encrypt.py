import json
from base64 import b64encode

from Crypto import Random
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
import ast
from google.cloud import kms
from rsa import PrivateKey
# Import the client library.
from google.cloud import kms
from google.protobuf import duration_pb2
import datetime
    
project_id = 'silken-period-357815'
location_id = 'nam3'
key_ring_id = 'PorcupassRing'
key_id = 'Test5'
version_id = '1'
# Create the client.
client = kms.KeyManagementServiceClient()


class Encrypt():

    def crc32c(data):
        """
        Calculates the CRC32C checksum of the provided data.
        Args:
            data: the bytes over which the checksum should be calculated.
        Returns:
            An int representing the CRC32C checksum of the provided bytes.
        """
        import crcmod
        import six
        crc32c_fun = crcmod.predefined.mkPredefinedCrcFun('crc-32c')
        return crc32c_fun(six.ensure_binary(data))

    def create_key_asymmetric_sign(project_id, location_id, key_ring_id, key_id):
        """
        Creates a new asymmetric signing key in Cloud KMS.

        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            key_id (string): ID of the key to create (e.g. 'my-asymmetric-signing-key').

        Returns:
            CryptoKey: Cloud KMS key.

        """

        
        # Call the API.
        # Build the parent key ring name.
        key_ring_name = client.key_ring_path(project_id, location_id, key_ring_id)


        # Build the key.
        purpose = kms.CryptoKey.CryptoKeyPurpose.ASYMMETRIC_SIGN
        algorithm = kms.CryptoKeyVersion.CryptoKeyVersionAlgorithm.RSA_SIGN_PKCS1_2048_SHA256
        key = {
            'purpose': purpose,
            'version_template': {
                'algorithm': algorithm,
            },

            # Optional: customize how long key versions should be kept before
            # destroying.
            'destroy_scheduled_duration': duration_pb2.Duration().FromTimedelta(datetime.timedelta(days=1))
        }

        # Call the API.
        created_key = client.create_crypto_key(
            request={'parent': key_ring_name, 'crypto_key_id': key_id, 'crypto_key': key})
        print('Created asymmetric signing key: {}'.format(created_key.name))
        return created_key

    key = create_key_asymmetric_sign(project_id, location_id, key_ring_id, key_id) 

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
        
        '''
        keys = RSA.generate(2048)
        public_key = keys.publickey().export_key()
        private_key = keys.export_key()

        f = open('public.pem','wb')
        f.write(public_key)
        f.close()

        f = open('private.pem','wb')
        f.write(private_key)
        f.close()'''


        # Build the key version name.
        key_version_name = client.crypto_key_version_path(project_id, location_id, key_ring_id, key_id, version_id)

        public_key = client.get_public_key(request={'name': key_version_name})

        # Optional, but recommended: perform integrity verification on public_key.
        # For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit:
        # https://cloud.google.com/kms/docs/data-integrity-guidelines
        if not public_key.name == key_version_name:
            raise Exception('The request sent to the server was corrupted in-transit.')
        # See crc32c() function defined below.
        if not public_key.pem_crc32c == crc32c(public_key.pem):
            raise Exception('The response received from the server was corrupted in-transit.')
        # End integrity verification


        if type(data) == str:
            data = data.encode('utf-8')
        elif type(data) == dict:
            data = str(json.dumps(data)).encode('utf-8')
        if type(data) == bytes:
            cipher = PKCS1_OAEP.new(key=public_key)
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

