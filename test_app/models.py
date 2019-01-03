from django.db import models

from kms_field.fields import KMSEncryptedField
from kms_field.helpers import decrypt_ciphertext_blob


class MyModel(models.Model):
    my_secret_value = KMSEncryptedField()

    def decrypt(self):
        return decrypt_ciphertext_blob(self.my_secret_value)
