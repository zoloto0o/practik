# bot_handlers.py

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from weather_api import get_weather

# Определяем популярные города России для быстрого выбора
popular_cities = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Нижний Новгород"]

# Постоянная клавиатура с кнопкой "Показать погоду"
keyboard = [["Показать погоду"]]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def start(update: Update, context: CallbackContext) -> None:
    """Приветственное сообщение с клавиатурой 'Показать погоду'."""
    update.message.reply_text(
        "Привет! Я бот для получения информации о погоде.\n"
        "Нажми на кнопку 'Показать погоду' ниже, чтобы узнать погоду в популярных городах "
        "или ввести свой город.",
        reply_markup=reply_markup
    )

def show_city_options(update: Update, context: CallbackContext) -> None:
    """Отправляет инлайн-кнопки с популярными городами и кнопкой для ввода своего города."""
    # Создаем вертикальные кнопки для каждого города
    keyboard = [[InlineKeyboardButton(city, callback_data=city)] for city in popular_cities]
    keyboard.append([InlineKeyboardButton("Ввести свой город", callback_data="custom_city")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text("Выберите один из популярных городов или введите свой:", reply_markup=reply_markup)

def handle_city_selection(update: Update, context: CallbackContext) -> None:
    """Обрабатывает нажатие на инлайн-кнопки с выбором города."""
    query = update.callback_query
    query.answer()

    city = query.data
    if city == "custom_city":
        # Просим пользователя ввести название своего города
        query.edit_message_text("Введите название города, чтобы узнать погоду:")
    else:
        # Получаем погоду для выбранного города и отправляем ответ
        weather_info = get_weather(city)
        query.edit_message_text(weather_info)

def handle_custom_city_input(update: Update, context: CallbackContext) -> None:
    """Обрабатывает ввод города пользователем после выбора 'Ввести свой город'."""
    city = update.message.text
    weather_info = get_weather(city)
    update.message.reply_text(weather_info, reply_markup=reply_markup)

# Функция для регистрации обработчиков в основном файле
def setup_dispatcher(dispatcher):
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.regex("Показать погоду"), show_city_options))
    dispatcher.add_handler(CallbackQueryHandler(handle_city_selection))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_custom_city_input))
