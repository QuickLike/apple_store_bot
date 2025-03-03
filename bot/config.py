from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()


class Config(BaseSettings):
    BOT_TOKEN: str
    GROUPS_IDS: str
    GROUPS_LINKS: str
    CHECK_SUBSCRIPTIONS_TEXT: str = 'Проверить подписки на каналы🔍'

    IS_SUBSCRIBER: bool = False

    @property
    def groups_ids(self) -> list[int]:
        return [int(id_) for id_ in self.GROUPS_IDS.split(',')]

    @property
    def groups_links(self) -> list[str]:
        return self.GROUPS_LINKS.split(',')


config = Config()
bot = Bot(config.BOT_TOKEN)
dp = Dispatcher()
