import requests
import telebot
import config



bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=["start"])
def hello_func(message):
    bot.send_message(message.chat.id, 'Привет, бла-бла-бла')

 
@bot.message_handler(commands=['low'])
def low_info(message):
    low_api_info = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search'

    try:
        response = requests.get(low_api_info)
        bot.send_message(message.chat.id, f'Миниальное кол-во запросов: {response.headers.lower_items()}')

    except Exception as e:
        bot.send_message(message.chat.id, f'Произошла ошибка: {str(e)}')


bot.polling(none_stop=True)

