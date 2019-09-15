from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests

from urllib.request import urlopen
from bs4 import BeautifulSoup

from export.export_base import ExportBase
from imports.twitter_import import TwitterImport
from imports.youtube_import import YouTubeImport
from imports.facebook_import import FacebookImport
from imports.vk_import import VKImport

class TelegramExport(ExportBase):
    def __init__(self, username):
        self.username = username
    def get_key(self):
        return 'telegram'
        
    def get_news(bot, update):
        VKImport.get_elements(self, count)
        YouTubeImport.get_elements(self, count)
        FacebookImport.get_elements(self, count)
        TwitterImport.get_elements(self, count)

    def main():
        updater = Updater('942366907:AAG3-yvksu0jZn0DVNULD75XDT-fP7eU8OE') #http://t.me/BotForNews_bot ссылка на бота
        = updater.dispatcher
        dp.add_handler(CommandHandler('news',get_news))
        updater.start_polling()
        updater.idle()
if __name__ == '__telegram_export__':
    main()