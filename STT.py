#region IMPORTS
from func import *
import speech_recognition as sr
from save_editor import commands, settings, check_commands, check_settings
from consts import info, warning, error, assist, user
import sys
import random
#endregion IMPORTS


r = sr.Recognizer()

def input_settings():
    global settings
    # Выводим список микрофонов
    print("Доступные микрофоны:")
    for i, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"{i}: {name}")

    # Запрашиваем у пользователя выбор микрофона
    settings["mic_index"] = int(input("Введите номер микрофона для использования: "))
    save_settings(settings)


def speech_to_text():
    global commands, settings
    print("Слушаю...")

    while True:
        with sr.Microphone(device_index=settings["mic_index"]) as source:
            audio = r.listen(source)
            try:
                audio_input = r.recognize_google(audio, language="ru-RU").lower()
                if audio_input.startswith("alman"):
                    print(f"{user} >>> {audio_input}")
                    requed = audio_input.partition("alman")[2].strip()

                    cmd = get_command(requed, commands)

                    if requed == "выход":
                        print("Выход из прослушивания.")
                        break

                    elif cmd == "hi":
                        greetings = [
                        f"{assist} Привет, {settings['user_name']}! Как я могу помочь?",
                        f"{assist} Здравствуйте, {settings['user_name']}! Чем помочь?",
                        f"{assist} Добрый день, {settings['user_name']}!"
                        f"{assist} Здравствуйте, хозяин. Чем могу помочь?"
                        ]
                        print(random.choice(greetings))
                    
                    elif cmd == "yt":
                        open_youtube()
                    
                    elif cmd == "browser":
                        open_browser()
                    
                    elif cmd == "stop":
                        goodbye = [
                            f"{assist} До свидания, {settings['user_name']}! Если понадобится помощь, запустите программу.",
                            f"{assist} Всего хорошего, {settings['user_name']}! Возвращайтесь, если нужна помощь.",
                            f"{assist} До свидания, хозяин. Увидимся в следующей сессии!"
                        ]
                        print(random.choice(goodbye))
                        sys.exit(0)
                    
                    elif cmd == "vpn":
                        vpn()
                    
                    elif cmd == "discord":
                        open_discord()
                    
                    elif cmd == "steam":
                        open_steam()
                    
                    elif cmd == "screenshot":
                        make_screenshot()
                    
                    elif cmd == "clear":
                        clear_console()
                    elif cmd == "update_request":
                        commands = check_commands()
                        settings = check_settings()
                        print(f"Debug: {info} Завистимости обновлены!")

                
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

def get_command(requed, commands):
    for cmd, keywords in commands.items():
        if any(word in requed for word in keywords):
            return cmd
    return None