from distutils.core import setup

setup(
    name='django_kmsfield',
    version='0.1.0',
    packages=['kms_field'],
    url='',
    license='',
    author='idritsas',
    author_email='dritsas@intelligems.eu',
    description='Adds KMSEncryptedField to django model fields',
    install_requires=[
        'aws-encryption-sdk',
        'kms_client'
    ],
    dependency_links=[
        'http://pypi.intelligems.eu/simple/kms-client/'
    ]
)