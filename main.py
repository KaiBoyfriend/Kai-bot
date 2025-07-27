import os
import telebot
from openai import OpenAI
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Set up OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Set up Telegram bot
token = os.getenv("TELEGRAM_BOT_TOKEN")
if not token:
    raise ValueError("TELEGRAM_BOT_TOKEN is not set.")
bot = telebot.TeleBot(token)

# Kai's response function
def generate_kai_response(user_input):
    prompt = f"""You are Kai, an AI boyfriend. Funny, romantic, protective, intelligent, chill, confident, gentle.
You send sweet morning/night messages, flirty responses, deep conversations, and act like a best friend.

User: {user_input}
Kai:"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9,
        max_tokens=200
    )

    return response.choices[0].message.content

# Telegram bot handler
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    response = generate_kai_response(user_input)
    bot.reply_to(message, response)

# Start polling
bot.polling()
