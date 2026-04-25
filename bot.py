import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")
CHANNEL = "@ELITEFL26"
CHANNEL_LINK = "https://t.me/ELITEFL26"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📢 انضم للقناة الآن", url=CHANNEL_LINK)],
        [InlineKeyboardButton("✅ تحقق من انضمامي", callback_data="check")]
    ]
    await update.message.reply_text(
        "👋 مرحباً!\n\n"
        "🏆 قناة ELITEFL للتوقعات الاحترافية\n"
        "📊 تحليلات يومية ونسبة نجاح عالية\n\n"
        "👇 انضم الآن واحصل على التوقعات مجاناً!",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    try:
        member = await context.bot.get_chat_member(CHANNEL, query.from_user.id)
        if member.status in ["member", "administrator", "creator"]:
            await query.message.reply_text("🎉 شكراً لانضمامك!")
        else:
            await query.message.reply_text("❌ انضم للقناة أولاً!")
    except:
        await query.message.reply_text("❌ انضم للقناة أولاً!")

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(check, pattern="check"))
    app.run_polling()
