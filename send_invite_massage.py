import time
import random
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.tl.functions.contacts import ImportContactsRequest, DeleteContactsRequest
from telethon.tl.types import InputPhoneContact
from config import API_HASH, API_ID

api_id = API_ID
api_hash = API_HASH

invite_link = "https://t.me/kazah_news_channal"
usernames = ["vldedov"]  # получатели

phone = '+77075001271'
message = f"Приглашаю тебя в наш канал: {invite_link}"


def send_message_user_id():
    user_ids = [355575739]  # список user_id
    message_templates = [
        f"Привет! Загляни сюда: {invite_link}",
        f"Приглашаю тебя в наш канал: {invite_link}",
        f"Вот ссылка, если интересно: {invite_link}"
    ]

    def random_message():
        return random.choice(message_templates)

    with TelegramClient('anon', api_id, api_hash) as client:
        for user_id in user_ids:
            try:
                entity = client.get_entity(user_id)  # Получаем TLObject (User)
                client.send_message(entity, random_message())
                print(f"✅ Сообщение отправлено: user_id = {user_id}")
                time.sleep(random.uniform(4, 8))  # Задержка между сообщениями
            except Exception as e:
                print(f"❌ Ошибка при отправке user_id = {user_id}: {e}")


def send_phone_number_message():
    with TelegramClient('anon', api_id, api_hash) as client:
        try:
            # Импортируем временный контакт
            result = client(ImportContactsRequest([InputPhoneContact(
                client_id=0,
                phone=phone,
                first_name='Temp',
                last_name=''
            )]))

            if result.users:
                user = result.users[0]  # Это TLObject (User)
                client.send_message(user, message)
                print(f"✅ Сообщение отправлено на номер {phone}")

                # удалить контакт после отправки
                client(DeleteContactsRequest([user]))
            else:
                print(f"⚠️ Пользователь с номером {phone} не найден в Telegram")

        except Exception as e:
            print(f"❌ Ошибка с телефоном {phone}: {e}")

if __name__ == '__main__':

    send_message_user_id()
#   send_phone_number_message()
