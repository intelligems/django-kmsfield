import os

from django.conf import settings
from django.db.models import CharField
from django.utils.translation import ugettext_lazy as _

from .helpers import encrypt_value


class KMSEncryptedField(CharField):
    description = _('Store byte data base64 representation encrypted with KMS')

    def __init__(self, *args, max_length=250, **kwargs):
        super().__init__(*args, max_length=max_length, **kwargs)

    def get_db_prep_save(self, value, connection):
        cmk = settings.CMK
        return super().get_db_prep_save(
            value=encrypt_value(value, cmk),
            connection=connection
        )

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        if kwargs.get("max_length") == 250:
            del kwargs['max_length']
        return name, path, args, kwargs
