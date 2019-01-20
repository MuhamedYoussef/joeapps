from .base import *
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = True
ADMINS = (
    ('Mohamed Youssef', 'mu7med.youssef@gmail.com'),
)
ALLOWED_HOSTS = ['shimasu-progress.herokuapp.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd81mt03ukhmtf6',
        'HOST': 'ec2-54-75-245-94.eu-west-1.compute.amazonaws.com',
        'USER': 'ihyqfibforfslm',
        'PASSWORD': '73d2b66759068ec0e8e3b4f41e43dd1293798ed9fe9e2ea9225e8ee2e125c201',
    }
}
