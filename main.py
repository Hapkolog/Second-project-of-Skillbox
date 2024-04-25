import requests
import telebot
import config
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)

bot = telebot.TeleBot(config.TOKEN)

def api_request(method_endswith,  
                params, 
                method_type  
                ):
    
    url = f"https://hotels4.p.rapidapi.com/{method_endswith}"

    if method_type == 'GET':
        return get_request(
            url=url,
            params=params
        )
    else:
        return post_request(
            url=url,
            params=params
        )

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
