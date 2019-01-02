import os

from django.db.models import BinaryField
from django.utils.translation import ugettext_lazy as _

from .helpers import decrypt_ciphertext_blob, encrypt_value


class KMSEncryptedField(BinaryField):
    description = _('Store byte data encrypted with KMS')

    def save_form_data(self, instance, data):
        cmk = os.getenv('CMK')
        byte_data = encrypt_value(data, cmk)
        setattr(instance, self.name, byte_data)

    def decrypt(self, cmk):
        return decrypt_ciphertext_blob(self)
