from maxapi.types import MessageCreated, BotStarted, Command, MessageCallback
from src.core.loader import Message

from maxapi.types.updates.message_callback import MessageForCallback
from maxapi.types.attachments.buttons.attachment_button import AttachmentButton

def setup(bot, dp):

    @dp.bot_started()
    async def bot_started(event: BotStarted):
        await bot.send_message(
            chat_id=event.chat_id,
            text='Доступные команды:\n'
                 '/info\n'
                 '/test'
        )

    @dp.message_created(Command('info'))
    async def info(event: MessageCreated):
        await event.message.answer(
            text='Доступные команды:\n'
                 '/info\n'
                 '/test'
        )

    @dp.message_created(Command('test'))
    async def test(event: MessageCreated):
        message = Message("start1")

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