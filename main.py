from telethon import TelegramClient
from config import API_HASH, API_ID

api_id = API_ID
api_hash = API_HASH


# The first parameter is the .session file name (absolute paths allowed)
with TelegramClient('anon', api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('@artur_suleimenov', 'Hello from autoBot!'))
    print("fff")
