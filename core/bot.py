from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler,ContextTypes
import os

API_TOKEN = os.environ.get("API_TOKEN")

async def startproj(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    await context.bot.send_message(chat_id=update.effective_chat.id,text=update.message)
    # get data of message


def main():
    # print(API_TOKEN)
    app = ApplicationBuilder().token(API_TOKEN).build()

    app.add_handler(CommandHandler("start", startproj))

    app.run_polling()



if __name__ == "__main__":
    main()