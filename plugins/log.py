from pyrogram import Client
import pyrogram
import subprocess


@Client.on_message(pyrogram.filters.command("log"))
def get_logs(client, message):
    try:
        logs = subprocess.check_output(["journalctl", "-u", "my_bot.service"]).decode()
        message.reply_text(logs)
    except Exception as e:
        message.reply_text("Failed to get logs: {}".format(str(e)))
