import json
from consts import warning, info, error
import os

#region Settings
CONFIG_PATH = "configs"
SETTINGS_FILE = os.path.join(CONFIG_PATH, "settings.json")

def save_settings(settings):
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(CONFIG_PATH)
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, ensure_ascii=False, indent=4)

def load_settings():
    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            settings = json.load(f)
            return settings
    except FileNotFoundError:
        return check_settings()

def check_settings():
    if not os.path.exists(SETTINGS_FILE):
        print(f"Debug: {warning} Файл с настройками не найден. Создание нового файла настроек со значениями по умолчанию.")
        default_settings = {
            "version": "Pre_Alpha 0.1.3",
            "text_model_name": "gpt-4o-mini",
            "graphic_model_name": "Stable Diffusion",
            "mic_index": None,
            "user_name": "Пользователь",
            "first_start": True
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