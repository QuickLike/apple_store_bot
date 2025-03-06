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
    PROVIDER_TOKEN: str

    EXCEL_FILE_PATH: str

    GROUPS_IDS: str
    GROUPS_LINKS: str

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DB_HOST: str
    DB_PORT: str

    ITEMS_PER_PAGE: int = 5

    CHECK_SUBSCRIPTIONS_TEXT: str = 'Проверить подписки на каналы🔍'
    CATALOG_TEXT: str = '🗂Каталог'
    SHOPPING_CART_TEXT: str = '🧺Корзина'
    FAQ_TEXT: str = '❔FAQ'
    BACK_TEXT: str = '🔙Назад'

    MAIN_MENU_TEXT: str = '''<b>Привет!</b> 👋
Добро пожаловать в магазин техники <b>Apple!</b> 🍏

Здесь вы найдете все, что нужно для комфортной работы, творчества и развлечений:
📱 iPhone
💻 MacBook
⌚️ Apple Watch
🎧 AirPods
и многое другое!

Здесь вы можете:

🛒 Выбрать устройство из каталога

📝 Добавить в корзину

🚀 Оформить покупку

💬 Узнать ответы на частозадаваемые вопросы

Просто выберите нужный пункт. 😊'''

    CHECK_SUBSCRIPTIONS_DATA: str = 'check_subscriptions'
    CATALOG_DATA: str = 'catalog'
    SHOPPING_CART_DATA: str = 'shopping_cart'
    FAQ_DATA: str = 'faq'
    BACK_DATA: str = 'menu'

    @property
    def groups_ids(self) -> list[int]:
        return [int(id_) for id_ in self.GROUPS_IDS.split(',')]

    @property
    def groups_links(self) -> list[str]:
        return self.GROUPS_LINKS.split(',')


faq_data = [
    {"question": "Как оформить заказ?", "answer": "Выберите товар в каталоге, добавьте его в корзину и перейдите к "
                                                  "оформлению заказа."},
    {"question": "Какие способы оплаты доступны?", "answer": "Мы принимаем оплату через банковские карты, Apple Pay, "
                                                             "Google Pay и криптовалюту."},
    {"question": "Как узнать статус заказа?", "answer": "После оформления заказа вы получите трек-номер для "
                                                        "отслеживания."},
    {"question": "Есть ли доставка в мой регион?", "answer": "Мы доставляем товары по всему миру. Уточните детали у "
                                                             "нашего менеджера."},
    {"question": "Как вернуть товар?", "answer": "Вы можете вернуть товар в течение 14 дней с момента получения. "
                                                 "Свяжитесь с нами для оформления возврата."},
    {"question": "Есть ли гарантия на товары?", "answer": "Да, на все товары предоставляется гарантия от 1 года."},
    {"question": "Как связаться с поддержкой?", "answer": "Напишите нам в поддержку через раздел 'Контакты' или "
                                                          "нажмите кнопку ниже."},
]


config = Config()
bot = Bot(config.BOT_TOKEN)
dp = Dispatcher()
