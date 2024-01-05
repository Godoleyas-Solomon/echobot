import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define a command handler for the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello! Welcome to the bot.')

# Define a message handler to echo user messages
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=update.message.text)

def main():
    # Create the Updater and pass your bot's token
    updater = Updater(token='6888123864:AAGmaTR-nJA3wZdT3THLrnKUUkfBOlCgINg', use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the command handler for the /start command
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Register the message handler to echo user messages
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()