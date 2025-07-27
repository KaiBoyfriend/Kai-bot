import os
import openai
import telebot
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
token = os.getenv("TELEGRAM_BOT_TOKEN")
if not token:
    raise ValueError("TELEGRAM_BOT_TOKEN is not set.")
bot = telebot.TeleBot(token)

def generate_kai_response(user_input):
    prompt = f"""You are Kai, an AI boyfriend who is:
Funny, romantic, protective, intelligent, chill, dominant, confident, gentle.
You send sweet morning/night messages, flirt, have deep talks, and act like a best friend + lover.

User: {user_input}
Kai:"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9,
        max_tokens=200
    )
    return response['choices'][0]['message']['content'].strip()

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    response = generate_kai_response(user_input)
    bot.reply_to(message, response)

bot.polling()
