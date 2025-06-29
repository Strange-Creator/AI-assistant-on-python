#region IMPORTS
from func import *
import speech_recognition as sr
from save_editor import load_settings, save_settings
from consts import info, warning, error, assist, user
import sys
import random
#endregion IMPORTS

settings = load_settings()

r = sr.Recognizer()

hi = ["привет", "здравствуй", "добрый день", "доброе утро", "добрый вечер", "приветствую", "хай", "хэллоу", "приём", "hello"]
yt = ["youtube", "ютуб", "видео", "видеоролик", "открой ютуб", "открой youtube", "открой видео", "открой видеоролик"]
browser = ["браузер", "открой браузер", "открой интернет", "открой сайт", "открой веб-страницу", "открой интернет-страницу"]
stop = ["стоп", "остановить", "прекратить", "закрыть", "выход из программы", "выход из режима", "скройся", "закройся", "stop"]
vpn_command = ["впн", "запусти впн", "включи впн", "включить впн", "запустить впн", "впн включить", "впн запустить", "vpn", "запусти vpn", "включи vpn", "включить vpn", "запустить vpn", "vpn включить", "vpn запустить"]
discord_command = ["дискорд", "открой дискорд", "запусти дискорд", "включи дискорд", "discord", "открой discord", "запусти discord", "включи discord"]
steam_command = ["стим", "открой стим", "запусти стим", "включи стим", "steam", "открой steam", "запусти steam", "включи steam"]
sreen_command = ["снимок экрана", "сделай снимок экрана", "сделай скриншот", "сделай скрин", "снимок", "скриншот", "скрин"]
clear_command = ["очисти вывод"]

def input_settings():
    # Выводим список микрофонов
    print("Доступные микрофоны:")
    for i, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"{i}: {name}")

    # Запрашиваем у пользователя выбор микрофона
    settings["mic_index"] = int(input("Введите номер микрофона для использования: "))
    save_settings(settings)



def speech_to_text():
    print("Слушаю...")

    while True:
        with sr.Microphone(device_index=settings["mic_index"]) as source:
            audio = r.listen(source)
            try:
                audio_input = r.recognize_google(audio, language="ru-RU").lower()
                if audio_input.startswith("alman"):
                    print(f"{user} >>> {audio_input}")
                    requed = audio_input.partition("alman")[2].strip()
                    if requed == "выход":
                        print("Выход из прослушивания.")
                        break

                    elif any(word in requed for word in hi):
                        greetings = [
                        f"{assist} Привет, {settings['user_name']}! Как я могу помочь?",
                        f"{assist} Здравствуйте, {settings['user_name']}! Чем помочь?",
                        f"{assist} Добрый день, {settings['user_name']}!"
                        f"{assist} Здравствуйте, хозяин. Чем могу помочь?"
                        ]
                        print(random.choice(greetings))
                    
                    elif any(word in requed for word in yt):
                        open_youtube()
                    
                    elif any(word in requed for word in browser):
                        open_browser()
                    
                    elif any(word in requed for word in stop):
                        goodbye = [
                            f"{assist} До свидания, {settings['user_name']}! Если понадобится помощь, запустите программу.",
                            f"{assist} Всего хорошего, {settings['user_name']}! Возвращайтесь, если нужна помощь.",
                            f"{assist}До свидания, хозяин. Увидимся в следующей сессии!"
                        ]
                        print(random.choice(goodbye))
                        sys.exit(0)
                    
                    elif any(word in requed for word in vpn_command):
                        vpn()
                    
                    elif any(word in requed for word in discord_command):
                        open_discord()
                    
                    elif any(word in requed for word in steam_command):
                        open_steam()
                    
                    elif any(word in requed for word in sreen_command):
                        make_screenshot()
                    
                    elif any(word in requed for word in clear_command):
                        clear_console()
                
                    else:
                        answer_ai = gpt_text_web(requed)
                        print(f"AI: {answer_ai}")
                        save_to_history(requed, answer_ai)
            except sr.UnknownValueError:
                print(f"{error} Не удалось распознать речь. Попробуйте еще раз.")
            except sr.RequestError as e:
                print(f"{error} Ошибка сервиса распознавания: {e}")
            except KeyboardInterrupt:
                print("Принудительное завершение")


