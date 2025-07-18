from telegram import Update , InlineKeyboardButton, InlineKeyboardMarkup ,ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler,ContextTypes , CallbackQueryHandler, MessageHandler, filters
import os

API_TOKEN = os.environ.get("API_TOKEN")
if not API_TOKEN:
    raise ValueError("توکن ربات پیدا نشد! لطفاً متغیر API_TOKEN را تنظیم کنید.")

async def startproj(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard= InlineKeyboardMarkup([
        [InlineKeyboardButton('کلید های شورتکات' , callback_data='show_shortcuts')],
        [InlineKeyboardButton('مشاهده وبسایت', url='https://amirimohsen.ir')],
        [InlineKeyboardButton('پروفایل' , callback_data='user_profile')],
    ])

    await update.message.reply_text( f"سلام {update.effective_user.first_name} 👋\nبه ربات خوش اومدی!\nیکی از گزینه‌ها رو انتخاب کن:", reply_markup=keyboard)

async def handel_btn(update:Update, context:ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data =='show_shortcuts':
        keyboard = ReplyKeyboardMarkup(keyboard=[['/help', '/start'],["❌ حذف شورتکات"]], resize_keyboard=True,one_time_keyboard=False)
        await query.message.reply_text('شورکات مورد نظر را انتخاب کنید' , reply_markup = keyboard) 

    elif query.data == 'user_profile':
        await query.message.reply_text("✏️ این بخش به‌زودی فعال می‌شود...")

async def remove_shortcut_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "❌ حذف شورتکات":
        await update.message.reply_text(
            "✅ شورتکات‌ها حذف شدن.",
            reply_markup=ReplyKeyboardRemove()
        )


def main():
    # print(API_TOKEN)
    app = ApplicationBuilder().token(API_TOKEN).build()

    app.add_handler(CommandHandler("start", startproj))
    app.add_handler(CallbackQueryHandler(handel_btn))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), remove_shortcut_keyboard))

    app.run_polling()



if __name__ == "__main__":
    main()