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
    return response.get('CiphertextBlob')


def decrypt_ciphertext_blob(ciphertext_blob, encryption_context=None):
    encryption_context = encryption_context or {}
    response = client.decrypt(
        CiphertextBlob=ciphertext_blob,
        EncryptionContext=encryption_context,
        # GrantTokens=[
        #     'string',
        # ]
    )
    return response.get('Plaintext')
