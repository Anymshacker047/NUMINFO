from telegram.ext import Updater, CommandHandler
import os
from dotenv import load_dotenv

from services.ip_lookup import ip_lookup
from services.phone_lookup import phone_lookup
from services.whois_lookup import whois_lookup

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def start(update, context):
    update.message.reply_text("OSINT Bot Ready 🔍")

def ip(update, context):
    result = ip_lookup(context.args[0])
    update.message.reply_text(result)

def phone(update, context):
    result = phone_lookup(context.args[0])
    update.message.reply_text(result)

def whois_cmd(update, context):
    result = whois_lookup(context.args[0])
    update.message.reply_text(result)

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("ip", ip))
dp.add_handler(CommandHandler("phone", phone))
dp.add_handler(CommandHandler("whois", whois_cmd))

updater.start_polling()
updater.idle()
