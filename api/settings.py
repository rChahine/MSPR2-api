from starlette.config import Config
from starlette.datastructures import URL, Secret

env = Config(".env")

DATABASE_URL: URL = env("DATABASE_URL", cast=URL)
SECRET_KEY: Secret = env("SECRET_KEY", cast=Secret)
