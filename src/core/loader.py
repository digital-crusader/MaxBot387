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
    def __init__(self, message_path):
        data, message_id = self.load_message(message_path)
        if not data: raise FileNotFoundError(f'Файл сообщения {message_path}.json не найден.')

        if data["text"] != "custom":
            self.text = data["text"]
        else:
            from data.custom_messages import load_custom_message
            self.text = load_custom_message(message_id)

        self.builder = InlineKeyboardBuilder()

        for row, buttons in data.get("buttons", {}).items():
            button_objs = []
            for button_id in buttons:
                button_objs.append(Button(button_id))

            if not button_objs:
                continue

            callback_buttons = [CallbackButton(text=b.title, payload=b.message) for b in button_objs]

            self.builder.row(*callback_buttons)


    def load_message(self, message_path):
        path = 'data/messages'
        path = os.path.join(path, f'{message_path}.json')
        return load_file(path), os.path.basename(path)


class Button:
    def __init__(self, button_path):
        data = self.load_button(button_path)
        if not data: raise FileNotFoundError(f'Файл кнопки {button_path}.json не найден')

        self.title = data["title"]
        self.message = data["message"]

    def load_button(self, button_path):
        path = 'data/buttons'
        path = os.path.join(path, f'{button_path}.json')
        return load_file(path)