from kms_client import generate_client
from django.conf import settings

client = generate_client(
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.REGION_NAME
)


def generate_cmk(description='KMSField CMK'):
    return client.generate_masterkey(
        description=description
    )


def encrypt_value(value, cmk, encryption_context=None, isfile=False):
    return client.encrypt(
        value=value,
        cmk=cmk or settings.CMK,
        encryption_context=encryption_context,
        isfile=isfile
    )


def decrypt_cipher(cipher, encryption_context=None, filename=None, isfile=False):
    return client.decrypt(
        cipher=cipher,
        encryption_context=encryption_context,
        filename=filename,
        isfile=isfile
    )
