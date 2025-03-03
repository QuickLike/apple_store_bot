from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import config

channels_links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        *[
            [InlineKeyboardButton(text=f'Канал {i}', url=group_link)]
            for i, group_link in enumerate(config.groups_links, 1)
        ],
        [InlineKeyboardButton(text=config.CHECK_SUBSCRIPTIONS_TEXT, callback_data="check_subscriptions")]
    ]
)
