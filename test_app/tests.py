from django.test import TestCase

from .models import MyModel


class MyModelTestCase(TestCase):
    def setUp(self):
        self.cmk = ''
        self.my_model_obj = MyModel.objects.create(my_secret_value="super secret value")

    def test_confirm_value_is_encrypted(self):
        self.assertTrue(isinstance(self.my_model_obj.my_secret_value, bytes))

    def test_decrypt_value(self):
        self.my_model_obj.my_secret_value.decrypt()
