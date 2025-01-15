from flask import Flask, request
import telebot
import os

# Initialize Flask app
app = Flask(__name__)

# Bot configuration
BOT_TOKEN = "7934553609:AAE_FN9vh0zoEfuY2U5evy74SPHy4S3HnPk"
bot = telebot.TeleBot(BOT_TOKEN)

# Webhook route
@app.route('/' + BOT_TOKEN, methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'OK'

# Handle /start command
@bot.message_handler(commands=['start'])
def start(message):
    response = """👋 Welcome to Guardian Angel Bot!

I can help you with:
• Guardian Angel Project Info
• NFT Collection Details
• $ANGEL Token Information
• Distribution System
• Official Channels

What would you like to know about?"""
    bot.reply_to(message, response)

# Handle specific keywords
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()
    
    if 'nft' in text:
        response = """🎨 Guardian Angel NFT Collection:
• Limited edition NFTs
• Exclusive holder benefits
• Part of Guardian Angel ecosystem
• Special utilities for holders"""
    
    elif 'token' in text or 'angel' in text:
        response = """💎 $ANGEL Token:
• Native token of Guardian Angel
• Built on SUI blockchain
• Used for governance and utilities
• Staking benefits available"""
    
    elif 'distribution' in text:
        response = """📊 Token Distribution:
• Fair launch mechanism
• Community-focused allocation
• Staking rewards
• NFT holder benefits"""
    
    else:
        response = """I can tell you about:
• NFT Collection
• $ANGEL Token
• Distribution
• Official Channels

Just ask about any of these topics!"""
    
    bot.reply_to(message, response)

# Health check route
@app.route('/')
def health():
    return 'Guardian Angel Bot is running!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
