from telegram.ext import Updater, InlineQueryHandler
from decouple import config
import logging
from bot.modules import *

BOT_TOKEN = config('BOT_TOKEN')

updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

inline_ket_handler = InlineQueryHandler(inline_ket)

dispatcher.add_handler(inline_ket_handler)
