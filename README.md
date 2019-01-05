# Django KMS Encrypted Fields

## Installation

- Connected to OpenVPN server

```Shell
pip install django_kmsfield \
   --extra-index-url http://pypi.intelligems.eu \
   --trusted-host pypi.intelligems.eu \
   --process-dependency-links
```

## Django Setup

- Add `kms_field` package to installed apps and
- Add below settings to base project `settings.py`

```Python
import os

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'kms_field',
    'your_app_name'
]

# ...

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
REGION_NAME = os.getenv('REGION_NAME')

CMK = os.getenv('CMK')
```