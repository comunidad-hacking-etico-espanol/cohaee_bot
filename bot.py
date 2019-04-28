import logging
import os
import sys

from telegram.ext import Updater, CommandHandler

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

TOKEN = os.getenv("TOKEN")
ADMINS = os.getenv("ADMINS")

def run(updater):
    PORT = int(os.environ.get("PORT", "8443"))
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
    updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(HEROKU_APP_NAME, TOKEN))

def logger_console(update, accion):
    logger.info("{} | {} | {} | {}".format(update.effective_user["id"], update.effective_user["username"], update.effective_user.full_name, accion))

def start_handler(bot, update):
    logger_console(update, "start")
    update.message.reply_text("Hola! Soy CoHaEE, el bot de la Comunidad de Hacking Ético - Español");


def test_handler(bot, update):
    logger_console(update, "test")
    update.message.reply_text("{} está haciendo pruebas conmigo...".format(update.effective_user.full_name))


if __name__ == '__main__':
    logger.info("Iniciando COHAEE bot")
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler("test", test_handler))
    updater.dispatcher.add_handler(CommandHandler("start", start_handler))

    run(updater)
