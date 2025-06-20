from telethon.sync import TelegramClient
from telethon.tl.types import Channel, Chat
from config import API_HASH, API_ID

api_id = API_ID
api_hash = API_HASH


with TelegramClient('anon', api_id, api_hash) as client:
    dialogs = client.get_dialogs()

    print("📋 Все группы и каналы:\n")

    for dialog in dialogs:
        entity = dialog.entity

        # Только группы и каналы (исключаем личные чаты)
        if isinstance(entity, (Channel, Chat)):
            title = getattr(entity, 'title', '')
            entity_id = entity.id
            username = getattr(entity, 'username', None)

            # Формируем ссылку: либо по username, либо t.me/c/<chat_id>
            if username:
                link = f"https://t.me/{username}"
            elif isinstance(entity, Channel) and entity.megagroup:
                # Приватная супергруппа без username
                link = f"https://t.me/c/{str(entity_id)[4:]}" if str(entity_id).startswith("-100") else None
            else:
                link = None

            print(f"Название: {title}")
            print(f"ID: {entity_id}")
            print(f"Username: {username}")
            print(f"Ссылка: {link}")
            print("-" * 40)

