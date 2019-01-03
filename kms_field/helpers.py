import base64
import boto3

client = boto3.client('kms')


def generate_cmk(description='KMSField CMK'):
    response = client.create_key(
        # Policy='string',
        Description=description,
        KeyUsage='ENCRYPT_DECRYPT',
        Origin='AWS_KMS',
        BypassPolicyLockoutSafetyCheck=True,
    )
    return response


def encrypt_value(value, cmk, encryption_context=None):
    encryption_context = encryption_context or {}
    response = client.encrypt(
        KeyId=cmk,
        Plaintext=value,
        EncryptionContext=encryption_context,
        # GrantTokens=[
        #     'string',
        # ]
    )
    cipher = response.get('CiphertextBlob')
    return base64.b64encode(cipher).decode('utf-8')


def decrypt_ciphertext_blob(cipher, encryption_context=None):
    ciphertext_blob = base64.b64decode(cipher)
    encryption_context = encryption_context or {}
    response = client.decrypt(
        CiphertextBlob=ciphertext_blob,
        EncryptionContext=encryption_context,
        # GrantTokens=[
        #     'string',
        # ]
    )
    plaintext = response.get('Plaintext')
    if plaintext is not None:
        return plaintext.decode('utf-8')
    return None


def decrypt_cipher_client(client, cipher, encryption_context=None):
    ciphertext_blob = base64.b64decode(cipher)
    encryption_context = encryption_context or {}
    response = client.decrypt(
        CiphertextBlob=ciphertext_blob,
        EncryptionContext=encryption_context,
        # GrantTokens=[
        #     'string',
        # ]
    )
    plaintext = response.get('Plaintext')
    if plaintext is not None:
        return plaintext.decode('utf-8')
    return None