from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import InlineQuery,InlineQueryResultArticle,InputTextMessageContent
import logging
import random

happy = ["ʘ‿ʘ","┬─┬⃰͡ (ᵔᵕᵔ͜ )","(｡◕‿◕｡)","ʕᵔᴥᵔʔ","ヽ(´▽`)/","（ ^_^）o自自o（^_^ ）","ಠ‿ಠ",":D"]
misc = ["◔_◔","♥‿♥","( ˘ ³˘)♥","♪♪ ヽ(ˇ∀ˇ )ゞ","(•̀ᴗ•́)و ̑̑","(☞ﾟヮﾟ)☞","(´･_･`)","¯\_(⊙︿⊙)_/¯","ᕙ(⇀‸↼‶)ᕗ","( ͡° ͜ʖ ͡°)","¯\(°_o)/¯","щ（ﾟДﾟщ）"]
sad = ["ಥ﹏ಥ","(⊙.☉)7","(ಥ⌣ಥ)"]
angry = ["( ಠ ʖ̯ ಠ)","( ͡ಠ ʖ̯ ͡ಠ) ","♨_♨","(Ծ‸ Ծ)","눈_눈","(ノಠ ∩ಠ)ノ彡( \\o°o)\\","t(-_-t)","(╬ ಠ益ಠ)","┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻"]
	
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
	"""Send a message when the command /start is issued."""
	update.message.reply_text('Hi!')


def help(bot, update):
	"""Send a message when the command /help is issued."""
	update.message.reply_text('''
	 \(^.^) 
	I reply with ASCII faces for the mood!
	/start - Reply with Hi!
	/help -  Options and How to Use
	/sendface - Send a random Ascii Face
	Currently supported moods:
	1. Happy
	2. Sad
	3. Angry
	4. Misc
	How to use:
	Just type in your mood and receive a random ASCII Face for that mood!
	If that mood isn't available, I'll echo your text.
	''')


def echo(bot, update):
	"""Echo the user message."""
	if update.message.text.lower() == "happy":
		update.message.reply_text(random.choice(happy))
	elif update.message.text.lower() == "sad":
		update.message.reply_text(random.choice(sad))
	elif update.message.text.lower() == "angry":
		update.message.reply_text(random.choice(angry))
	elif update.message.text.lower() == "misc":
		update.message.reply_text(random.choice(misc))
	else:
		update.message.reply_text(update.message.text)


def inline_echo(bot, update):
	result = []
	if update.inline_query.query.lower() == "happy":
		for id,faces in enumerate(happy):
			result.append(InlineQueryResultArticle(id,faces,InputTextMessageContent(faces)))
		update.inline_query.answer(result)
	if update.inline_query.query.lower() == "sad":
		for id,faces in enumerate(sad):
			result.append(InlineQueryResultArticle(id,faces,InputTextMessageContent(faces)))
		update.inline_query.answer(result)
	if update.inline_query.query.lower() == "misc":
		for id,faces in enumerate(misc):
			result.append(InlineQueryResultArticle(id,faces,InputTextMessageContent(faces)))
		update.inline_query.answer(result)
	if update.inline_query.query.lower() == "angry":
		for id,faces in enumerate(angry):
			result.append(InlineQueryResultArticle(id,faces,InputTextMessageContent(faces)))
		update.inline_query.answer(result)
	else:
		for id, faces in enumerate(happy+sad+angry+misc):
			result.append(InlineQueryResultArticle(id, faces, InputTextMessageContent(faces)))
		update.inline_query.answer(result)

def error(bot, update, error):
	"""Log Errors caused by Updates."""
	logger.warning('Update "%s" caused error "%s"', update, error)

def sendface(bot, update):
	"""Send in a default face"""
	update.message.reply_text(random.choice(happy+sad+angry+misc))

def main():
	"""Start the bot."""
	
	# Create the EventHandler and pass it your bot's token.
	updater = Updater("503635874:AAF1FRp2bpe-XDw7UL-lcCBlHNLVUFMDGbo")

	# Get the dispatcher to register handlers
	dp = updater.dispatcher

	# on different commands - answer in Telegram
	dp.add_handler(CommandHandler("start", help))
	dp.add_handler(CommandHandler("help", help))
	dp.add_handler(CommandHandler("sendface", sendface))
	dp.add_handler(InlineQueryHandler(inline_echo))
	
	
	# on noncommand i.e message - echo the message on Telegram
	dp.add_handler(MessageHandler(Filters.text, echo))

	# log all errors
	dp.add_error_handler(error)

	# Start the Bot
	updater.start_polling()

	# Run the bot until you press Ctrl-C or the process receives SIGINT,
	# SIGTERM or SIGABRT. This should be used most of the time, since
	# start_polling() is non-blocking and will stop the bot gracefully.
	updater.idle()


if __name__ == '__main__':
	main()