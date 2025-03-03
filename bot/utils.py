from config import config, bot


async def check_channels_subscription(user_id):
    for group_id in config.groups_ids:
        user_channel_status = await bot.get_chat_member(chat_id=group_id, user_id=user_id)
        if user_channel_status.status != 'member':
            config.IS_SUBSCRIBER = False
            break
    else:
        config.IS_SUBSCRIBER = True
