from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import config


BUTTONS = {
    config.CHECK_SUBSCRIPTIONS_DATA: InlineKeyboardButton(
        text=config.CHECK_SUBSCRIPTIONS_TEXT,
        callback_data=config.CHECK_SUBSCRIPTIONS_DATA
    ),
    config.CATALOG_DATA: InlineKeyboardButton(
        text=config.CATALOG_TEXT,
        callback_data=config.CATALOG_DATA
    ),
    config.SHOPPING_CART_DATA: InlineKeyboardButton(
        text=config.SHOPPING_CART_TEXT,
        callback_data=config.SHOPPING_CART_DATA
    ),
    config.FAQ_DATA: InlineKeyboardButton(
        text=config.FAQ_TEXT,
        callback_data=config.FAQ_DATA
    ),
    config.BACK_DATA: InlineKeyboardButton(
        text=config.BACK_TEXT,
        callback_data=config.BACK_DATA
    )

}

channels_links = InlineKeyboardMarkup(
    inline_keyboard=[
        *[
            [InlineKeyboardButton(text=f'Канал {i}', url=group_link)]
            for i, group_link in enumerate(config.groups_links, 1)
        ],
        [BUTTONS[config.CHECK_SUBSCRIPTIONS_DATA]]
    ]
)

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [BUTTONS[config.CATALOG_DATA]],
        [BUTTONS[config.SHOPPING_CART_DATA]],
        [BUTTONS[config.FAQ_DATA]],
    ]
)

back = InlineKeyboardMarkup(
    inline_keyboard=[
        [BUTTONS[config.BACK_DATA]]
    ]
)
