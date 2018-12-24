import boto3

from django.db.models import TextField
from django.utils.translation import ugettext_lazy as _

aws_client = boto3.client('kms')


class KMSEncryptedField(TextField):
    description = _('Store string data encrypted/decrypted by KMS')

    def to_python(self, value):
        """
        Ensure we've got a string value typed in
        :param value: str value
        :return: value
        """

        if isinstance(value, str):
            return value
        raise value

    def get_db_prep_value(self, value, connection, prepared=False):
        """
        Store data inserted in KMS and return the ARN.
        :param value:
        :param connection:
        :param prepared:
        :return:
        """

        # todo
        return value

    def value_to_string(self, obj):
        """
        Using KMS via boto3, decrypt the value and return it to the user.
        :param obj:
        :return:
        """

        # todo
        return str(obj)
