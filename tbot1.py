from telegram.ext import Updater, CommandHandler
import wikipedia

TOKEN = '624357728:AAHsx_YCO7Z43kj3wY2IQsbYG7TAuMJXRVc'

def pong(update, context):
	update.message.reply_text(wikipedia.summary('ubuntu'))

def main():
	updater = Updater(TOKEN, use_context=True)
	dp = updater.dispatcher

	dp.add_handler(CommandHandler('ubuntu', pong))
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()
