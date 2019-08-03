import logging
from telegram.ext import Updater, CommandHandler

from settings import *
# from database import *


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()


def logger_console(user, extra):
    logger.info("{} | {} | {} | {}".format(user.id, user.username, user.full_name, str(extra) ))


#def start_handler(update, context):
#    logger_console(update, "start")
#    update.message.reply_text("Hola! Soy CoHaEE, el bot de la Comunidad de Hacking Ético - Español");


def command_handler(update, context):
    if update.effective_user.username in ADMIN_LIST:
        logger_console(update.effective_user, ["command", "autorizado"])
        update.message.reply_text("Procesando comando, por favor espere.")


def error_handler(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


# inicializa el bot
def bot_start():
    logger.info("Iniciando COHAEE bot")
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler("command", command_handler))
    updater.dispatcher.add_error_handler(error_handler)

    updater.start_polling()
    updater.idle()
