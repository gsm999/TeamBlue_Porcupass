import base64

def decrypt_symmetric(project_id, location_id, key_ring_id, key_id, ciphertext):
    """
    Decrypt the ciphertext using the symmetric key

    Args:
        project_id (string): Google Cloud project ID (e.g. 'my-project').
        location_id (string): Cloud KMS location (e.g. 'us-east1').
        key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
        key_id (string): ID of the key to use (e.g. 'my-key').
        ciphertext (bytes): Encrypted bytes to decrypt.

    Returns:
        DecryptResponse: Response including plaintext.

    """

    # Import the client library.
    from google.cloud import kms

    # Create the client.
    client = kms.KeyManagementServiceClient()

    # Build the key name.
    key_name = client.crypto_key_path(project_id, location_id, key_ring_id, key_id)

    # Optional, but recommended: compute ciphertext's CRC32C.
    # See crc32c() function defined below.
    ciphertext_crc32c = crc32c(ciphertext)

    # Call the API.
    decrypt_response = client.decrypt(
        request={'name': key_name, 'ciphertext': ciphertext, 'ciphertext_crc32c': ciphertext_crc32c})

    # Optional, but recommended: perform integrity verification on decrypt_response.
    # For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit:
    # https://cloud.google.com/kms/docs/data-integrity-guidelines
    if not decrypt_response.plaintext_crc32c == crc32c(decrypt_response.plaintext):
        raise Exception('The response received from the server was corrupted in-transit.')
    # End integrity verification

    print('Plaintext: {}'.format(decrypt_response.plaintext))
    return decrypt_response


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




project_id = 'silken-period-357815'
location_id = 'nam3'
key_ring_id = 'PorcupassRing'
key_id = 'sym1'



ciphertext = b'\n$\x00\xda<Eh_\x1e\xb5\xbe\x8d\xdc\x830\xce-<\xb4\xbe?\xd1m\xc6\xc6\x8e\x8f\xe245\xbd\xf0d\x82\xc7O^\x87\x12.\x00\xae\x9c\xfa\x0c\xbco,\xcdN\xa9\xa6\xa2\x00>[\x82\xc4\xfe#\x96k\x91\x8fmO\xe0;\xaa-\xbd4\xd6\xa2\xc2>\xd7\xf36\xe2/\x1d*\xece\xd6'
decrypt_symmetric(project_id, location_id, key_ring_id, key_id, ciphertext)
