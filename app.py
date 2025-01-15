from flask import Flask, request
import telebot
import os

# Initialize Flask app
app = Flask(__name__)

# Bot configuration
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN provided!")

# Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

# Simple route
@app.route('/')
def home():
    return 'Bot is running'

# Webhook route
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return 'OK', 200
    return 'Bad Request', 400

# Handle /start command
@bot.message_handler(commands=['start'])
def start(message):
    response = """👋 Welcome to Guardian Angel Bot!

I can help you with:
• Guardian Angel Project Info
• NFT Collection Details
• $ANGEL Token Information
• Distribution System
• Official Channels"""
    bot.reply_to(message, response)

# Handle all messages
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    try:
        text = message.text.lower()
        if 'nft' in text:
            response = """🎨 Guardian Angel NFT Collection:
• Limited edition NFTs
• Exclusive holder benefits
• Part of ecosystem
• Special utilities"""
        elif 'token' in text:
            response = """💎 $ANGEL Token:
• Native token
• Built on SUI
• Governance & utilities
• Staking benefits"""
        else:
            response = "Ask me about NFTs or tokens!"
        bot.reply_to(message, response)
    except Exception as e:
        print(f"Error in message handler: {e}")
        bot.reply_to(message, "I'm processing your request...")

if __name__ == '__main__':
    # Start Flask app
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
