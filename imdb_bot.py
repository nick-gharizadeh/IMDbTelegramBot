from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, Application, MessageHandler, filters
from bot_token import token
import imdb

imdb = imdb.IMDb()
buttons = []


async def start_command(update, context):
    await update.message.reply_text(f'Hi {update.message.chat.first_name}!\nWe\'re glad to have you here! 😉 '
                                    '\nLet\'s get started with some amazing features! 💛')


async def reply_message(update, context):
    movie_name = update.message.text
    global buttons
    if len(buttons) != 0 and is_movie_exist_on_keyboard(movie_name):
        await show_movie_details(update, context)
    else:
        buttons.clear()
        search = imdb.search_movie(movie_name)
        for i in range(0, len(search)):
            buttons.append([KeyboardButton(f"🎬 {search[i]}")])
        await update.message.reply_text("Now, select one of these results to show the details:",
                                        reply_markup=ReplyKeyboardMarkup(buttons))


async def show_movie_details(update, context):
    await update.message.reply_text(update.message.text)


def is_movie_exist_on_keyboard(movie_name):
    """
    This function searches for a button in the buttons list to determine if the user has selected a button or not.
    Each button in the buttons list has its own properties.We want to compare the user's input(movie_name) with text
    property of keyboard button.
    :param movie_name:
    :return bool: Exists or not
    """
    for button in buttons:
        for button_items in button:
            if button_items.text == movie_name:
                return True
    return False


if __name__ == '__main__':
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(MessageHandler(filters.TEXT, reply_message))
    application.run_polling(1.0)
