from distutils.core import setup

setup(
    name='django_kmsfield',
    version='0.3.2',
    packages=['kms_field', 'kms_field.management', 'kms_field.management.commands'],
    url='',
    license='',
    author='idritsas',
    author_email='dritsas@intelligems.eu',
    description='Adds KMSEncryptedField to django model fields',
    install_requires=[
        'aws-encryption-sdk',
        'kms_client',
        'Django'
    ],
    dependency_links=[
        'http://pypi.intelligems.eu/simple/kms-client/'
    ]
)
