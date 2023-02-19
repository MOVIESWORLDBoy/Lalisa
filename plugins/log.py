import logging
import os
import sys
from pyrogram import Client
import pyrogram

# Create a logger for your bot
logger = logging.getLogger(__name__)

# Configure the logger to write logs to standard output
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)


# Define a command handler for the "/log" command
@Client.on_message(pyrogram.filters.command("log"))
def get_logs(client, message):
    try:
        # Read the contents of the log file
        with open("/app/logs/bot.log", "r") as f:
            logs = f.read()
        # Send the log file contents as a text message to the user
        message.reply_text(logs)
    except Exception as e:
        logger.exception("Failed to get logs")
        message.reply_text("Failed to get logs: {}".format(str(e)))
        
# Start the bot
