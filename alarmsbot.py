import telebot
from telebot import types
import logging


TOKEN = 'TOKEN_HERE'

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

@tb.message_handler(commands=['guardia'])

def command_guardia(m):
	cid = m.chat.id
	guardia1 = 'User1'
	guardia2 = 'User2'

	tb.send_message(cid, 'Esta semana de Guardia' + guardia1)


@tb.message_handler(commands=['status'])

def command_status(m):
	cid = m.chat.id
	import os
	hostname = "HostName" 
	response = os.system("ping -c 1 " + hostname)
	
	if response == 0:
		tb.send_message(cid, 'Servicios Arriba')
	else:
		tb.send_message(cid, 'Alerta en los servicios')


@tb.message_handler(commands=['help'])

def command_help(m):
	cid = m.chat.id

	text_help = 'La lista de comandos es \n/guardia: para saber quien esta de guardia. \
	\n/saludo: recibes un saludo del bot. \n/status: te da un estatus de la plataforma.\n \
	/jugar: Reto al Conocimiento.'

	tb.send_message(cid, text_help)

@tb.message_handler(commands=['jugar'])

def send_play(m):
	#unique_code = extract_unique_code(m.text)
	cid = m.chat.id
	markup = types.ReplyKeyboardMarkup(row_width=2)
	markup.add('JUGAR', 'SALIR')
	msg = tb.send_message(cid, "Selecciona una accion:", reply_markup=markup)
	tb.register_next_step_handler(msg, send_category)


def send_category(m):
	cid = m.chat.id

	markup = types.ReplyKeyboardMarkup(row_width=10)
	markup.add('Farandula', 'Cine', 'Deportes', 'Literatura', 'Ficcion', 'Ciencia')
	msg = tb.send_message(cid, "Escoge una Categoria:", reply_markup=markup)
	tb.register_next_step_handler(msg, process_next_step)


def process_next_step(m):

	try:
		cid = m.chat.id

		cat = m.text

		if (cat == u'Farandula') or (cat == u'Cine') or (cat == u'Deportes') or (cat == u'Literatura') or (cat == u'Ficcion') or (cat == u'Ciencia'):

			cat = cat

		else:

			raise Exception()

		msg = 'Excelente jugaremos en la Categoria: ' + cat

		tb.send_message(msg, process_category)

	except Exception as e:
		tb.reply_to(cid, 'ooooppssss')





tb.polling(none_stop=True)