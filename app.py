from flask import Flask, request
import telebot
import os

# Initialize Flask app
app = Flask(__name__)

# Bot configuration
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@app.route('/')
def home():
    return 'Bot is running'

@app.route('/' + BOT_TOKEN, methods=['POST'])
def webhook():
    try:
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return 'OK', 200
    except Exception as e:
        print(f"Webhook error: {e}")
        return 'Error', 500

@bot.message_handler(commands=['start'])
def start(message):
    try:
        bot.reply_to(message, "👋 Hello! I'm working now!")
    except Exception as e:
        print(f"Start error: {e}")

@bot.message_handler(func=lambda message: True)
def echo(message):
    try:
        bot.reply_to(message, f"You said: {message.text}")
    except Exception as e:
        print(f"Echo error: {e}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
