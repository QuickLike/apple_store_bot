import asyncio
import logging
import sys

from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.methods import DeleteWebhook

from keyboards import channels_links_kb
from utils import check_channels_subscription
from config import bot, config, dp


@dp.message(CommandStart())
async def command_start(message: Message):
    await message.answer(
        'Для работы бота необходимо подписаться на каналы.',
        reply_markup=channels_links_kb
    )


@dp.callback_query(F.data == "check_subscriptions")
async def check_subscriptions(callback: CallbackQuery):
    user_id = callback.from_user.id
    await callback.answer('Проверяем подписки')
    await check_channels_subscription(user_id)
    logging.info(config.IS_SUBSCRIBER)
    if config.IS_SUBSCRIBER:
        await callback.message.answer('Вы подписаны')
    else:
        await callback.message.answer(
            'Проверьте подписки на каналы.',
            reply_markup=channels_links_kb
        )


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format=('%(asctime)s, '
                '%(levelname)s, '
                '%(funcName)s, '
                '%(message)s'
                ),
        encoding='UTF-8',
        handlers=[logging.FileHandler(__file__ + '.log'),
                  logging.StreamHandler(sys.stdout)]
    )
    asyncio.run(main())
