import json
from consts import warning, info, error
import os

#region Settings
CONFIG_PATH = "configs"
COMMANDS_FILE = os.path.join(CONFIG_PATH, "commands.json")
SETTINGS_FILE = os.path.join(CONFIG_PATH, "settings.json")


def save_settings(settings):
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(CONFIG_PATH)
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, ensure_ascii=False, indent=4)




def load_settings():
    try:
        print(f"Debug: {info} Файл настроек найден. Загрузка параметров...")
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            settings = json.load(f)
            print(f"Debug: {info} Параметры загружены!")
            return settings
    except FileNotFoundError:
        return check_settings()

def check_settings():
    if not os.path.exists(SETTINGS_FILE):
        print(f"Debug: {warning} Файл с настройками не найден. Создание нового файла настроек со значениями по умолчанию.")
        default_settings = {
            "version": "0.1.4-alpha",
            "text_model_name": "gpt-4o-mini",
            "graphic_model_name": "Stable Diffusion",
            "mic_index": None,
            "user_name": "Пользователь",
            "first_start": False
        }
        if not os.path.exists(CONFIG_PATH):
            os.makedirs(CONFIG_PATH)
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(default_settings, f, ensure_ascii=False, indent=4)
        print(f"Debug: {info} Файл с настройками создан. Используются значения по умолчанию.")
        return default_settings
    else:
        return load_settings()  # Загружаем настройки из файла
    

#endregion Settings

#region Commands_settings
def load_commands():
    try:
        with open(COMMANDS_FILE, "r", encoding="utf-8") as g:
            commands = json.load(g)
            return commands
    except FileNotFoundError:
        return check_commands()


def save_commands(commands):
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(CONFIG_PATH)
    with open(COMMANDS_FILE, "w", encoding="utf-8") as g:
        json.dump(commands, g, ensure_ascii=False, indent=4)
    print(f"Debug: {info} Команды сохранены!")


def check_commands():
    if not os.path.exists(COMMANDS_FILE):
        print(f"Debug: {warning} Файл с командами не найден. Будет создан со значениями по умолчанию")
        default_commands = {
            "hi": [
                "привет", "здравствуй", "добрый день", "доброе утро", "добрый вечер",
                "приветствую", "хай", "хэллоу", "приём", "hello"
            ],
            "yt": [
                "youtube", "ютуб", "видео", "видеоролик", "открой ютуб", "открой youtube",
                "открой видео", "открой видеоролик"
            ],
            "browser": [
                "браузер", "открой браузер", "открой интернет", "открой сайт",
                "открой веб-страницу", "открой интернет-страницу"
            ],
            "stop": [
                "стоп", "остановить", "прекратить", "закрыть", "выход из программы",
                "выход из режима", "скройся", "закройся", "stop"
            ],
            "vpn": [
                "впн", "запусти впн", "включи впн", "включить впн", "запустить впн",
                "впн включить", "впн запустить", "vpn", "запусти vpn", "включи vpn",
                "включить vpn", "запустить vpn", "vpn включить", "vpn запустить"
            ],
            "discord": [
                "дискорд", "открой дискорд", "запусти дискорд", "включи дискорд",
                "discord", "открой discord", "запусти discord", "включи discord"
            ],
            "steam": [
                "стим", "открой стим", "запусти стим", "включи стим",
                "steam", "открой steam", "запусти steam", "включи steam"
            ],
            "screenshot": [
                "снимок экрана", "сделай снимок экрана", "сделай скриншот", "сделай скрин",
                "снимок", "скриншот", "скрин"
            ],
            "clear": [
                "очисти вывод"
            ],
            "update_request": [
                "обнови завистимости", 
                "обновись", 
                "обнови"
            ]
        }

        if not os.path.exists(CONFIG_PATH):
            os.makedirs(CONFIG_PATH)
        with open(COMMANDS_FILE, "w", encoding="utf-8") as g:
            json.dump(default_commands, g, ensure_ascii=False, indent=4)
        print(f"Debug: {info} Файл создан")
        return default_commands
    else:
        return load_commands()
#endregion Commands_settings


settings = check_settings()
commands = check_commands()