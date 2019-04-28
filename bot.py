import logging
import os
import sys

from telegram.ext import Updater, CommandHandler

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

TOKEN = os.getenv("TOKEN")
ADMINS = os.getenv("ADMINS")
print(ADMINS)


def run(updater):
    PORT = int(os.environ.get("PORT", "8443"))
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
    updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(HEROKU_APP_NAME, TOKEN))


def test_handler(bot, update):
    logger.info("Usuario id {} esta haciendo una prueba.".format(update.effective_user["id"]))
    update.message.reply_text("Hola! {}, esta es una prueba.".format(update.effective_user["username"])


if __name__ == '__main__':
    logger.info("Iniciando COHAEE bot")
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler("test", test_handler))

    run(updater)
