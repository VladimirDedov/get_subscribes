from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from config import API_HASH, API_ID, GROUP_ID

api_id = API_ID
api_hash = API_HASH
group_id = GROUP_ID

with TelegramClient('anon', api_id, api_hash) as client:
    try:
        entity = client.get_entity(group_id)

        participants = []
        offset = 0
        limit = 100

        while True:
            result = client(GetParticipantsRequest(
                channel=entity,
                filter=ChannelParticipantsSearch(''),
                offset=offset,
                limit=limit,
                hash=0
            ))

            if not result.users:
                break

            for user in result.users:
                user_data = {
                    'id': user.id,
                    'username': user.username or '',
                    'phone': user.phone or '',
                    'first_name': user.first_name or '',
                    'last_name': user.last_name or ''
                }
                participants.append(user_data)

            offset += len(result.users)

        # Сохраняем в файл
        with open("users.txt", "w", encoding="utf-8") as f:
            for p in participants:
                line = f"{p['id']} | @{p['username']} | {p['phone']} | {p['first_name']} {p['last_name']}\n"
                f.write(line)

        print(f"✅ Сохранено {len(participants)} пользователей в users.txt")

    except Exception as e:
        print("❌ Ошибка:", e)