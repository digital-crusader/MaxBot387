import os
import json
import logging
from maxapi.types import MessageCreated, BotStarted, Command, CallbackButton, MessageCallback
from maxapi.utils.inline_keyboard import InlineKeyboardBuilder

from data.custom_data import custom_data

logger = logging.getLogger(__name__)


def load_file(path):
    path = os.path.join(path)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logger.warning(f'Ошибка при загрузке {path}: {e}')
        return None

class Message:
    def __init__(self, message_path):
        data = self.load_message(message_path)
        if not data:
            raise FileNotFoundError(f'Файл сообщения {message_path}.json не найден.')

        self.text = data["text"]
        self.builder = InlineKeyboardBuilder()

        for row, buttons in data.get("buttons", {}).items():
            callback_buttons = [CallbackButton(text=btn[0], payload=btn[1]) for btn in buttons]
            if callback_buttons:
                self.builder.row(*callback_buttons)

    def load_message(self, message_path):
        path = 'data/messages'
        path = os.path.join(path, f'{message_path}.json')
        data = custom_data(message_path)
        if not data: data = load_file(path)

        return data