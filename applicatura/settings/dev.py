from . import base
import os


class Dev(base.BaseDev):
    SECRET_KEY = 'u8cq6*nc&p9jby)28&xg3f6v8_ppr6by@i4_z7v@ux#k=z!2#7'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(base.BaseDev.BASE_DIR, 'db.dev.sqlite3'),
        }
    }
