import logging


logging.basicConfig(
    filename='app.log',          # имя лог-файла
    level=logging.INFO,          # минимальный уровень логов
    format='%(asctime)s - %(levelname)s - %(message)s'  # формат вывода
)

logging.info("Программа запущена")
logging.warning("Что-то пошло не так")
logging.error("Произошла ошибка")