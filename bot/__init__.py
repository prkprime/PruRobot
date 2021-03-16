from telegram.ext import Updater, InlineQueryHandler
from decouple import config
import logging
from bot.modules import *

BOT_TOKEN = config('BOT_TOKEN')

updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

inline_master_handler = InlineQueryHandler(inline_master)

dispatcher.add_handler(inline_master_handler)
