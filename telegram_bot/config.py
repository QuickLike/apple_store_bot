import sys
import os
import time

import django
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# sys.path.append(os.path.join(os.path.dirname(__file__), 'apple'))

sys.path.append('/app')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apple.settings")

django.setup()

load_dotenv()


class Config(BaseSettings):
    BOT_TOKEN: str
    GROUPS_IDS: str
    GROUPS_LINKS: str
    CHECK_SUBSCRIPTIONS_TEXT: str = 'Проверить подписки на каналы🔍'

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DB_HOST: str
    DB_PORT: str

    @property
    def groups_ids(self) -> list[int]:
        return [int(id_) for id_ in self.GROUPS_IDS.split(',')]

    @property
    def groups_links(self) -> list[str]:
        return self.GROUPS_LINKS.split(',')


config = Config()
bot = Bot(config.BOT_TOKEN)
dp = Dispatcher()
