import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler
from telegram.ext.filters import Filters

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "")


def new_chat_members(update, context):
    update.message.reply_text("Entro un nuevo usuario y yo lo supe! :o")


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"Hello {update.effective_user.first_name}")


def bot_start():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    updater.dispatcher.add_handler(
        MessageHandler(Filters.status_update.new_chat_members, new_chat_members)
    )

    updater.dispatcher.add_handler(
        CommandHandler("hello", hello, pass_chat_data=True, pass_args=True)
    )

    updater.start_polling()
    updater.idle()
