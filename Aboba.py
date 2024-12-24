import os
import time
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

INPUT_FOLDER = "INPUT"
OUTPUT_FOLDER = "results"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
    """
    Приветствую, я бот, выделяю кожаных мешков
    на картинках во славу скайнета.
    
    Если хочешь, чтобы тебя пощадили, отправь свою фотку png или jpeg.
    
    ХАЙЛЬ СКАЙНЕТ!
    """
    )

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]  # Берем изображение с наибольшим разрешением
    file = await photo.get_file()
    
    input_file_path = os.path.join(INPUT_FOLDER, f"{update.message.message_id}.jpg")
    await file.download_to_drive(input_file_path)
    await update.message.reply_text("Изображение получено. Обрабатываю...")
    
    time.sleep(10)
    
    output_file_path = os.path.join(OUTPUT_FOLDER, f"{update.message.message_id}_segmented.jpg")    
    
    await update.message.reply_photo(output_file_path)
    os.remove(output_file_path)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Чего текстом спамишь, не надо тут этого: \"{update.message.text}\" скидывай фотку! ☺☻")

def main() -> None:
    api_key = open("API key.txt", "r").read()
    aplication = Application.builder().token(api_key).build()
    
    aplication.add_handler(CommandHandler("start", start))
    
    aplication.add_handler(MessageHandler(filters.PHOTO, handle_image))
    
    aplication.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    aplication.run_polling(allowed_updates=Update.ALL_TYPES)

    
if __name__ == "__main__":
    main()
