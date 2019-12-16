import logging
from telegram.ext import Updater, CommandHandler
from telegram import Chat
from settings import *

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()


def logger_console(user, extra):
    logger.info("{} | {} | {} | {}".format(user.id, user.username, user.full_name, str(extra) ))


def cmd_handler(update, context):
    if update.effective_user.username in ADMIN_LIST:
        update.message.reply_text("Procesando comando, por favor espere.")
        print(update)
        if len(update.message.text.split()) >= 2:
            comando = update.message.text.split()[1]

        if comando == 'scan':
            print(context.get_member(update.message.chat.id))

        logger_console(update.effective_user, ["command", "autorizado"])


def error_handler(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


# inicializa el bot
def bot_start():
    logger.info("Iniciando COHAEE bot")
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler("cmd", cmd_handler, pass_chat_data=True, pass_args=True))
    updater.dispatcher.add_error_handler(error_handler)

    print(updater.bot.get_chat(-1001297526243).get_member('%'))

    updater.start_polling()
    updater.idle()
