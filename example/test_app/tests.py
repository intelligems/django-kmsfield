from django.test import TestCase

from .models import MyModel


class MyModelTestCase(TestCase):
    def setUp(self):
        self.my_model_obj = MyModel.objects.create(my_secret_value="super secret value")
