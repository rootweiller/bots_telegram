import telebot
from telebot import types
import logging


TOKEN = '359259033:AAFgJHiPsJ9nvZEW1ILl__kyFbqLlPiRvto'

# Enable Logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)


tb = telebot.TeleBot(TOKEN)
updates = tb.get_updates(1234,100,20)

last_chat_id = 0

user_dict = {}


class User:
    def __init__(self, name):
        self.cat = None


def any_message(bot, update):
    """ Print to console """

    # Save last chat_id to use in reply handler
    global last_chat_id
    last_chat_id = update.message.chat_id

    logger.info("New message\nFrom: %s\nchat_id: %d\nText: %s" %
                (update.message.from_user,
                 update.message.chat_id,
                 update.message.text))

@tb.message_handler(commands=['saludo'])

def command_saludo(m):
	cid = m.chat.id
	message = 'Hola, soy Deep Thought o Pensamiento Profundo como tu quieras llamarme \
	y deseo ayudarte, ejecuta /help para conocer lo que puedo hacer'
	tb.send_message(cid, message)


@tb.message_handler(commands=['help'])

def command_help(m):
	cid = m.chat.id

	text_help = 'La lista de comandos es \n/conversar: para saber quien esta de guardia. \
	\n/saludo: recibes un saludo del bot. \n/historial: te da un estatus de la plataforma.\n \
	/recordatorio: Reto al Conocimiento.'

	tb.send_message(cid, text_help)

@tb.message_handler(commands=['conversar'])
def command_conversar(m):
	cid = m.chat.id

	text_help = 'Me gusta conversar, pero debo conocerte antes. como te llamas'

	tb.send_message(cid, text_help)



tb.polling(none_stop=True)