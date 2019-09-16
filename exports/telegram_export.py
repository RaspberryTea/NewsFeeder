from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests

from urllib.request import urlopen
from bs4 import BeautifulSoup

from storage.inmemory_storage import InmemoryStorage

storage = InmemoryStorage()

class TelegramExport(ExportBase):
    def __init__(self, username):
        self.username = username
    def get_key(self):
        return 'telegram'
        
    def get_news(bot, update):
      for s in storage:
        result = s.get_elements()

        for r in result:
            inspect_element(r)
            print()
            storage.find_elements(i.get_key(), r)

    def main():
        updater = Updater('942366907:AAG3-yvksu0jZn0DVNULD75XDT-fP7eU8OE') #http://t.me/BotForNews_bot ссылка на бота
        = updater.dispatcher
        dp.add_handler(CommandHandler('news',get_news))
        updater.start_polling()
        updater.idle()
if __name__ == '__telegram_export__':
    main()