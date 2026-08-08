from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8863585835:AAGFBFQLUJhvcqBrBL8zgoY_QNxipBSWwvA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 🌹\n\n"
        "به مرکز تخصصی نگارش خوش آمدید.\n\n"
        "📚 نگارش مقاله\n"
        "📋 نگارش پروپوزال\n"
        "🎓 نگارش پایان‌نامه و مونوگراف\n"
        "🌐 ترجمه فارسی، دری و انگلیسی\n\n"
        "برای ثبت سفارش با ما در ارتباط باشید."
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("ربات فعال شد...")

app.run_polling()