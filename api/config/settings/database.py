from .env import IntEnv, StrEnv

__all__ = [
    "DATABASES",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': StrEnv("DB_NAME"),
        'USER': StrEnv("DB_USER"),
        'PASSWORD': StrEnv("DB_PASS"),
        'HOST': StrEnv("DB_HOST"),
        'PORT': IntEnv("DB_PORT"),
    }
}
