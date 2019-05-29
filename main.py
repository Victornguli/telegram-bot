from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

def get_dog_url():
	contents = requests.get('https://random.dog/woof.json').json()
	url = contents['url']
	return url

def get_cat_url():
	contents = requests.get("http://aws.random.cat/meow").json()
	url = contents["file"]
	return url

def get_image_url():
	allowed_extension = ['jpg','jpeg','png']
	file_extension = ''
	while file_extension not in allowed_extension:
		url = get_dog_url()
		file_extension = re.search("([^.]*)$",url).group(1).lower()
	return url

def bop(bot, update):
	url = get_image_url()
	chat_id = update.message.chat_id
	bot.send_photo(chat_id=chat_id, photo=url)
	print(chat_id)

def cat(bot, update):
	url = get_cat_url()
	chat_id = update.message.chat_id
	bot.send_photo(chat_id=chat_id, photo=url)
	

def main():
	updater = Updater('526631934:AAGBaf8bGl0jgV8xqCA0rixnjvKssxABlVA') #Telegram API Token
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('start',bop))
	dp.add_handler(CommandHandler('dog',bop))
	dp.add_handler(CommandHandler("bop",bop))
	dp.add_handler(CommandHandler('cat',cat))
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()
