import os
import boto3
from django.test import TestCase

from .models import MyModel
from kms_field.helpers import encrypt_value, decrypt_ciphertext_blob, decrypt_cipher_client


class EncryptTestCase(TestCase):
    def setUp(self):
        self.cmk = os.getenv('CMK')
        self.plaintext = 'secret_value'
        self.client2 = boto3.client('kms')
        self.cipher = encrypt_value(value=self.plaintext, cmk=self.cmk)
        self.decrypted = decrypt_ciphertext_blob(cipher=self.cipher)
        self.decrypted2 = decrypt_cipher_client(
            client=self.client2,
            cipher=self.cipher
        )

    def test_encrypt_success(self):
        self.assertIsInstance(self.cipher, str)
        self.assertNotEqual(self.cipher, self.plaintext)

    def test_decrypt_success(self):
        print(self.decrypted2)
        self.assertEqual(self.decrypted, self.plaintext)


class MyModelTestCase(TestCase):
    def setUp(self):
        self.my_model_obj = MyModel.objects.create(my_secret_value="super secret value")

    def test_confirm_value_is_encrypted(self):
        print(self.my_model_obj.my_secret_value)

        retrieve = MyModel.objects.first()
        print(retrieve.my_secret_value)
        print(retrieve.decrypt())
        self.assertTrue(isinstance(self.my_model_obj.my_secret_value, str))

    # def test_decrypt_value(self):
    #     self.my_model_obj.my_secret_value.decrypt()
