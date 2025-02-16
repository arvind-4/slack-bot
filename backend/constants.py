from decouple import config

POSTGRES_USER = config('POSTGRES_USER', cast=str)
POSTGRES_PASSWORD = config('POSTGRES_PASSWORD', cast=str)
POSTGRES_DB = config('POSTGRES_DB', cast=str)
POSTGRES_HOST = config('POSTGRES_HOST', cast=str)
POSTGRES_PORT = config('POSTGRES_PORT', cast=int)

SLACK_BOT_TOKEN = config('SLACK_BOT_TOKEN', cast=str)
SLACK_SIGNING_SECRET = config('SLACK_SIGNING_SECRET', cast=str)

SECRET_KEY = config('SECRET_KEY', cast=str)
DEBUG = config('DEBUG', cast=bool)

OPEN_ROUTER_API_KEY = config('OPEN_ROUTER_API_KEY', cast=str)
BASE_URL = 'https://openrouter.ai/api/v1/chat/completions'