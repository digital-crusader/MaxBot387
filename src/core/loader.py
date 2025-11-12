import os
import json
import logging
from maxapi.types import MessageCreated, BotStarted, Command, CallbackButton, MessageCallback
from maxapi.utils.inline_keyboard import InlineKeyboardBuilder

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
    def __init__(self, message_id):
        data = self.load_message(message_id)

        self.text = data["text"]

        self.builder = InlineKeyboardBuilder()

        for row, buttons in data["buttons"].items():
            button_objs = [Button(button_id) for button_id in buttons]
            callback_buttons = [CallbackButton(text=b.title, payload=b.message) for b in button_objs]

            self.builder.row(*callback_buttons)


    def load_message(self, message_id):
        path = 'data/messages'
        path = os.path.join(path, f'{message_id}.json')
        return load_file(path)


class Button:
    def __init__(self, button_id):
        data = self.load_button(button_id)
        self.title = data["title"]
        self.message = data["message"]

    def load_button(self, button_id):
        path = 'data/buttons'
        path = os.path.join(path, f'{button_id}.json')
        return load_file(path)