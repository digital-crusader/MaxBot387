from maxapi.types import MessageCreated, BotStarted, Command, MessageCallback
from src.core.loader import Message

from maxapi.types.updates.message_callback import MessageForCallback
from maxapi.types.attachments.buttons.attachment_button import AttachmentButton

def setup(bot, dp):

    info_text = (
        'Доступные команды:'
        '\n/команды - список доступных команд'
        '\n/информация - информация для абитуриентов'


        '\n\nAvailable commands:'
        '\n/information - information for '
    )

    @dp.bot_started()
    async def bot_started(event: BotStarted):
        await bot.send_message(chat_id=event.chat_id, text=info_text)

    @dp.message_created(Command('команды'))
    async def info(event: MessageCreated):
        await event.message.answer(text=info_text)

    @dp.message_created(Command('информация'))
    async def start_ru(event: MessageCreated):
        message = Message("ру/информация")

        await event.message.answer(text=message.text, attachments=[message.builder.as_markup()])

    @dp.message_created(Command('information'))
    async def start_ru(event: MessageCreated):
        message = Message("англ/информация")

        await event.message.answer(text=message.text, attachments=[message.builder.as_markup()])

    @dp.message_callback()
    async def message_callback(event: MessageCallback):
        message_data = Message(event.callback.payload)

        builder = message_data.builder.as_markup()
        attachment_button = AttachmentButton.model_validate(builder.model_dump())

        message = MessageForCallback()
        message.text = message_data.text
        message.attachments = [attachment_button]

        await bot.send_callback(callback_id=event.callback.callback_id, message=message)