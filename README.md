WeatherBot

WeatherBot — это бот для Telegram, который предоставляет актуальную информацию о погоде. Бот позволяет пользователю быстро узнать погоду в популярных городах России или ввести название своего города, чтобы получить прогноз.

Функции:

Приветственное сообщение: бот приветствует пользователя и предлагает узнать погоду, нажав кнопку «Показать погоду».

Показ популярных городов: бот отображает список популярных городов для быстрого выбора.

Выбор города вручную: возможность ввода названия любого города для получения прогноза.

Информация о погоде: отображает температуру, ощущаемую температуру, влажность и краткое описание погодных условий.

Установка:

Клонируйте репозиторий и перейдите в директорию проекта:

git clone https://github.com/zoloto0o/practik
cd practik

Установите необходимые библиотеки:
pip install python-telegram-bot

Отредактируйте файл config.py в корне проекта и добавьте следующие переменные:

TELEGRAM_API_KEY = "ВАШ_ТЕЛЕГРАМ_API_KEY"
WEATHER_API_KEY = "ВАШ_WEATHER_API_KEY"

Запустите бота:

python main.py

Описание основных модулей:

main.py: основной файл, запускающий бота и настраивающий диспетчер команд.

bot_handlers.py: содержит обработчики команд и сообщений бота.

show_city_options: отображает кнопки для выбора популярного города или ввода собственного.

handle_city_selection: обрабатывает выбор города.

handle_custom_city_input: обрабатывает ввод города от пользователя.

weather_api.py: модуль, взаимодействующий с OpenWeatherMap API для получения данных о погоде.

Использование:
Запуск: отправьте команду /start, чтобы начать взаимодействие с ботом.

Выбор города:

Нажмите на кнопку "Показать погоду".

Выберите один из популярных городов или воспользуйтесь опцией «Ввести свой город».

Получение прогноза: после выбора города бот отправит актуальную информацию о погоде.