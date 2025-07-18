from telegram import Update , InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler,ContextTypes , CallbackQueryHandler
import os

API_TOKEN = os.environ.get("API_TOKEN")

async def startproj(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard= InlineKeyboardMarkup([
        [InlineKeyboardButton('کلید های شورتکات' , callback_data='show_shortcuts')],
        [InlineKeyboardButton('مشاهده وبسایت', url='https://amirimohsen.ir')],
        [InlineKeyboardButton('پروفایل' , callback_data='user_profile')],
    ])

    await update.message.reply_text(f'سلام {update.effective_user.first_name} . خوش آمدی ', reply_markup=keyboard)


def main():
    # print(API_TOKEN)
    app = ApplicationBuilder().token(API_TOKEN).build()

    app.add_handler(CommandHandler("start", startproj))

    app.run_polling()



if __name__ == "__main__":
    main()