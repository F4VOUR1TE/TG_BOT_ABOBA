from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Нихуёво тут в пижамах синих, ну че, лопнем мой пенис?")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"В очко™ себе свой: \"{update.message.text}\" засунь ♂")

def main() -> None:
    api_key = open("API key.txt", "r").read()
    aplication = Application.builder().token(api_key).build()
    
    aplication.add_handler(CommandHandler("start", start))
    
    aplication.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    aplication.run_polling(allowed_updates=Update.ALL_TYPES)

    
if __name__ == "__main__":
    main()
