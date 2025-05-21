
import os
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
from sniper import snipe_token
from checker import run_risk_analysis
from config import load_config, update_config
from utils import log_transaction

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

def start(update, context):
    update.message.reply_text("Welcome to GMGN Solana Sniper Bot!")

def snipe(update, context):
    token_address = context.args[0]
    result = run_risk_analysis(token_address)
    if "High Risk" in result:
        update.message.reply_text(f"Risk check failed: {result}")
    else:
        tx = snipe_token(token_address)
        log_transaction(token_address, tx)
        update.message.reply_text(f"Sniped token {token_address}. Transaction ID: {tx}")

def check(update, context):
    token_address = context.args[0]
    result = run_risk_analysis(token_address)
    update.message.reply_text(f"Risk Check:\n{result}")

def profit(update, context):
    new_profit = float(context.args[0])
    update_config("profit_target", new_profit)
    update.message.reply_text(f"Profit target set to {new_profit * 100}%")

def stoploss(update, context):
    new_stop = float(context.args[0])
    update_config("stop_loss", new_stop)
    update.message.reply_text(f"Stop loss set to {new_stop * 100}%")

def main():
    updater = Updater(TELEGRAM_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("snipe", snipe))
    dp.add_handler(CommandHandler("check", check))
    dp.add_handler(CommandHandler("profit", profit))
    dp.add_handler(CommandHandler("stoploss", stoploss))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
