from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler,ContextTypes
import os

API_TOKEN = os.environ.get("API_TOKEN")

# print(API_TOKEN)
app = ApplicationBuilder().token(API_TOKEN).build()

async def startproj(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print('ok')



app.add_handler(CommandHandler("start", startproj))

app.run_polling()