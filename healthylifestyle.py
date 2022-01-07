from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler
from telegram.ext import messagequeue as mq
from telegram.utils.request import Request
from telegram.error import Unauthorized
import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.error import (TelegramError, Unauthorized, BadRequest, 
                            TimedOut, ChatMigrated, NetworkError)
import logging
import datetime
import time
import os
from dotenv import load_dotenv
load_dotenv()
import re

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv('TOKEN')


def start(update, context):
    update.message.reply_text('Hii')


def main():
    # Create the Updater and pass in bot's token.
    updater = Updater(TOKEN)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    # Create command handlers
    dp.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()

