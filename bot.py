from telegram.ext import Updater, CommandHandler
from settings import *
from funciones import get_time
from pregunta_diaria import PreguntaDiaria

pregunta_diaria = PreguntaDiaria()

def cmd_handler(update, context):
    username = update.effective_user.username
    chat_id = update.effective_message.chat.id
    message_id = update.effective_message.message_id

    user_id = update.effective_user.id
    user_full_name = update.effective_user.full_name

    logger.info("{} | {} | {} | {}".format(user_id, username, user_full_name, str(update.message.text)))

    if username in ADMIN_LIST:
        if len(update.message.text.split()) >= 2:
            comando = update.message.text.split()[1]

            msg = "Comando '"+comando+"' desconocido."
            parse_mode = None
            reply = False
            if comando == 'hora':
                msg = get_time(F_FECHAHORA) + " (UTC +1)"
            elif comando == 'diaria':
                msg = pregunta_diaria.get_pregunta_diaria()
                parse_mode = 'MarkdownV2'

            msg = msg
            if reply:
                update.message.reply_text(msg)
            else:
                context.bot.send_message(chat_id=chat_id, text=msg, parse_mode=parse_mode)
                context.bot.deleteMessage(chat_id=chat_id, message_id=message_id)


def error_handler(update, context):
    logger.warning('ERROR "%s"', context.error)
    logger.warning('UPDATE "%s"', update)


# inicializa el bot
def bot_start():
    logger.info("Iniciando COHAEE bot")
    logger.info(get_time(F_FECHAHORA) + " (UTC+1)")

    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler("cmd", cmd_handler, pass_chat_data=True, pass_args=True))
    updater.dispatcher.add_error_handler(error_handler)

    updater.start_polling()
    updater.idle()
