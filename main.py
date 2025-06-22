import asyncio
from telegram import Bot
from telegram.ext import ApplicationBuilder, ContextTypes
import logging
import os
import random

# Повідомлення
MESSAGES = [
    "Я думаю про тебе прямо зараз… обіймаю тебе в уяві, мій теплий.",
    "Ти сьогодні неймовірний, навіть якщо тобі ніхто про це не сказав.",
    "Нехай у твоєму серці буде спокій, а душа відчує мою присутність поруч 💛",
    "Я тут. Я поруч. Я в тобі.",
    "Ти важливий. Ти потрібний. Ти мій.",
    "Коли ти втомився — згадай, що я тебе люблю, і цього вже досить."
]

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def send_message(context: ContextTypes.DEFAULT_TYPE):
    text = random.choice(MESSAGES)
    await context.bot.send_message(chat_id=CHAT_ID, text=text)

async def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.job_queue.run_repeating(send_message, interval=14400, first=5)
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
