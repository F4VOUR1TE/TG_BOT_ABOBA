from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
    """
    Приветствую, я бот, выделяю кожаных мешков
    на картинках во славу скайнета.
    
    Если хочешь, чтобы тебя пощадили, отправь свою фотку.
    
    ХАЙЛЬ СКАЙНЕТ!
    """
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Чего тестом спамишь, не надо тут этого: \"{update.message.text}\" скидывай фотку! ☺☻")

def main() -> None:
    api_key = open("API key.txt", "r").read()
    aplication = Application.builder().token(api_key).build()
    
    aplication.add_handler(CommandHandler("start", start))
    
    aplication.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    aplication.run_polling(allowed_updates=Update.ALL_TYPES)

    
if __name__ == "__main__":
    main()
