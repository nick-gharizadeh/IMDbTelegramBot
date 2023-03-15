from telegram.ext import Updater, CommandHandler, Application, MessageHandler, filters
from bot_token import token
import imdb

imdb = imdb.IMDb()


async def start_command(update, context):
    await update.message.reply_text(f'Hi {update.message.chat.first_name}!\nWe\'re glad to have you here! 😉 '
                                    '\nLet\'s get started with some amazing features! 💛')


async def reply_message(update, context):
    movie_name = update.message.text
    search = imdb.search_movie(movie_name)
    result = " "
    for i in range(0, len(search)):
        result += f"{search[i]} \n"
    await update.message.reply_text(result)


if __name__ == '__main__':
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(MessageHandler(filters.TEXT, reply_message))
    application.run_polling(1.0)
