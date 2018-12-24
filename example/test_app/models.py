from django.db import models

from kms_field.fields import KMSEncryptedField


class MyModel(models.Model):
    my_secret_value = KMSEncryptedField()

    def __str__(self):
        return self.my_secret_value
