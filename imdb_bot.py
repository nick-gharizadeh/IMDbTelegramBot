from telegram.ext import Updater, CommandHandler, Application
from bot_token import token


async def start_command(update, context):
    await update.message.reply_text(f'Hi {update.message.chat.first_name}!\nWe\'re glad to have you here! 😉 '
                                    '\nLet\'s get started with some amazing features! 💛')


if __name__ == '__main__':
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler('start', start_command))
    application.run_polling(1.0)
