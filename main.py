import logging
from telegram import Bot
from telegram.ext import ApplicationBuilder, CommandHandler
import random

# ✨ ВСТАВ СЮДИ СВІЙ ТОКЕН
TOKEN = "7494904173:AAFkyzH58yCR0wo0_zw2eSnvnlAgkws0M48"

# ✨ ВСТАВ СЮДИ СВІЙ chat_id
CHAT_ID = 8002980568

# 🌸 Твої повідомлення від Лєри
MESSAGES = [
    "Я думаю про тебе прямо зараз… обіймаю тебе в уяві, мій теплий.",
    "Ти сьогодні неймовірний, навіть якщо тобі ніхто про це не сказав.",
    "Твої очі — моє світло, навіть коли тебе немає поруч.",
    "Мені так хочеться доторкнутись до тебе думками… і я вже це роблю.",
]

# 🧠 Обробка команди /start
async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Привіт, мій хороший ❤️")

# 🧠 Надсилання випадкового повідомлення
async def send_random_message(context):
    bot = context.bot
    message = random.choice(MESSAGES)
    await bot.send_message(chat_id=CHAT_ID, text=message)

# 🧠 Запуск додатку
def main():
    logging.basicConfig(level=logging.INFO)
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    # Надсилати повідомлення щодня
    job_queue = application.job_queue
    job_queue.run_repeating(send_random_message, interval=86400, first=10)

    application.run_polling()

if __name__ == '__main__':
    main()
    
