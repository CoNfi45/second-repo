import telebot
import random
import os
from random import choice
from os import listdir

bot = telebot.TeleBot('7824109192:AAHllh0EPy0dZfDO6-n3ObmlMsDd7nxd0KQ')


#советы
tips = ['не вырубать деревья🎄',
        ' не мусторить на дорогах🚯',
        'убирать за собой мусор на природе🗑',
        'экономьте воду💦',
        'выключайте свет, когда не дома⚡',
        'Сортируй мусор — это просто!',
        'Чини, а не выбрасывай.',
        'Сажай деревья — дыши чище.'
        ]

@bot.message_handler(commands=['start'])
def start_command(message):
    chat_id = message.chat.id
    text = ('привет,! я бот, который помогает сохранять окружающую среду и любить природу!')

@bot.message_handler(commands=['tips'])
def send_random_tip(message):
    tip = random.choice(tips)
    bot.reply_to(message, f"🌱 Экосовет:\n\n{tip}")  
    
@bot.message_handler(commands=['pic'])
def send_mem(message):
    random_mem = choice(listdir('pic'))
    with open(f'pic/{random_mem}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

eco_challenges = [
    "🌱 Сегодня откажись от одноразового пластика (стаканы, пакеты, трубочки)",
    "🚲 Передвигайся только на велосипеде/самокате/пешком целый день",
    "💡 Выключай все электроприборы из розеток на ночь",
    "♻️ Сдай в переработку 5 пластиковых бутылок",
    "🛒 Купи продукты только без упаковки (на развес)",
    "🚿 Сократи время душа на 5 минут",
    "📱 Не заряжай телефон до 100% (оптимально 80%)",
    "🌳 Посади комнатное растение или дерево на улице",
    "🍎 Устрой веганский день (без мяса и молочных продуктов)",
    "📚 Прочитай статью об экологии и поделись с другом"
]

@bot.message_handler(commands=['challenge'])
def send_challenge(message):
    challenge = random.choice(eco_challenges)
    response = f"🌍 Эко-челлендж дня:\n\n{challenge}\n\nПрисылай фотоотчет! 📸"
    bot.send_message(message.chat.id, response)

bot.infinity_polling()
