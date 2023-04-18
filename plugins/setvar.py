import heroku3
from info import ADMINS
from pyrogram import Client, filters

HRK_API = "eb088c41-a226-4d55-ba70-d8f4370f8780"
HRK_APP_NAME = "publicautofilter"

heroku_conn = heroku3.from_key(HRK_API)

app = heroku_conn.apps()[HRK_APP_NAME]

@Client.on_message(filters.command("setvar") & filters.user(ADMINS))
async def setvarrrz(bot, message):
    data = message.text        
    command, varname, value = data.split(" ")
    config = app.config()
    config[f'{varname}'] = f'{value}'
