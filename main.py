#region IMPORTS
from g4f.client import Client
import func
import os
import platform
from consts import warning, info, error
from save_editor import *
from STT import speech_to_text, input_settings
#endregion IMPORTS

if settings["first_start"]:
    print(f"Debug: {info} Первоначальный запуск программы. Желаете первоначально настроить программу?...")
    first_setup = input("Да/Нет (y/n)\n>>> ").lower()
    if first_setup in("y", "да"):
        print("Отлично!\nКак вас зовут?")
        settings["user_name"] = input(">>> ")
        print("Модель ИИ для текста? (Доступны GPT-4 и GPT-4o-mini)")
        gpt_model_setup = input("Какую модель хотите?(введите 0 для модели по умолчанию)\n>>> ").lower()
        if gpt_model_setup in("gpt-4", "gpt-4o-mini"):
            settings["text_model_name"] = gpt_model_setup
        elif int(gpt_model_setup) == 0:
            print("включена модель по умолчанию")
        print("Модель ИИ для изображений?(Доступны flux и Stable Duffusion)")
        image_model_setup = input("Какую модель хотите?(введите 0 для модели по умолчанию)")
        if image_model_setup in("flux", "Stable Diffusion"):
            settings["graphic_model_name"] = image_model_setup
        elif int(image_model_setup) == 0:
            print("Включена модель по умолчанию")
    else:
        print("Первоначальная настройка отменена. Вы сможете настроить программу позже в настройках")

    settings["first_start"] = False
    save_settings(settings)

#region MAIN_MENU
while True:
    print("Выберите режим работы:\n1 - без веб-поиска\n2 - с веб-поиском\n3 - генерация изображений\n4 - Голосовой ввод(еще разрабатывается)\n5 - Настройки\nexit - выход из программы и режимов")
    mode = input("Режим: ")
    #region 1_MODE(gpt no web)
    if mode == "1":
        while True:
            user_input = input("Запрос: ")
            if user_input.lower() == "exit":
                break
            else:
                print("Ответ от GPT:", func.gpt_text_no(user_input))
    #endregion 1_MODE(gpt no web)

    #region 2_MODE(gpt with web)
    elif mode == "2":
        while True:
            web_search = input("Запрос: ")
            if web_search.lower() == "exit":
                break
            else:
                print("Ответ от GPT:", func.gpt_text_web(web_search))
    #endregion 2_MODE(gpt with web)

    #region 3_MODE(image generate)
    elif mode == "3":
        while True:
            img_prompt = input("Запрос для генерации изображения: ")
            if img_prompt.lower() == "exit":
                break
            else:
                print("Сгенерированное изображение:", func.gpt_img(img_prompt))
    #endregion 3_MODE(image generate)

    elif mode == "exit":
        print("Выход из программы.")
        break

    #region SPEECH-TO-TEXT
    elif mode == "4":
        print("Голосовой ввод (экспериментальный режим). Скажите 'выход' для завершения.")
        speech_to_text()  # Функция для голосового ввода, определенная в STT.py
    #endregion SPEECH-TO-TEXT

    #region SETTINGS_MENU
    elif mode == "5":
        while True:
            print("Настройки:\n1 - Модель\n2 - Ввод и вывод\n3 - Информация о вас\n4 - Назад")
            settings_choice = input("Выберите настройку: ")

            if settings_choice == "1":
                print("Настройка текстовой модели. Доступные модели: gpt-4, gpt-4o-mini(Вводить строго по регистру!). Введите название модели:")

                #настройки текстовой модели
                settings["text_model_name"] = input("Модель: ")
                print(f"Выбранная модель {settings["text_model_name"]} сохранена!")
                print("Настройка графической модели. Доступные модели: flux, Stable Diffusion(Вводить строго по регистру!). Введите название модели:")

                #настройки графической модели
                settings["graphic_model_name"] = input("Модель: ")

                save_settings(settings)  # Сохраняем настройки в файл
                print(f"Выбранная модель {settings["graphic_model_name"]} сохранена!")

                

            elif settings_choice == "2":
                
                print(f"Debug: {info} Настройка ввода и вывода:")
                #вызываем функцию для ввода настроек микрофона)
                settings["mic_index"] = input_settings()

                save_settings(settings)  # Сохраняем настройки в файл
                print(f"Выбранный микрофон с индексом {settings["mic_index"]} сохранен!")
                
            
            elif settings_choice == "3":
                print("Настройка информации о вас. Введите ваше имя:")

                # Настройка информации о пользователе
                settings["user_name"] = input("Имя: ")
                print(f"Ваше имя '{settings["user_name"]}' сохранено!")

                save_settings(settings)  # Сохраняем настройки в файл

            elif settings_choice == "4":
                print("Возврат в главное меню.")
                break
    #endregion SETTINGS_MENU

    #region DEVELOP
    elif mode == "dbg.info":
        print(f"Debug: {info} Версия программы: {settings["version"]}")
        print(f"Debug: {info} Используемая текстовая модель: {settings["text_model_name"]}")
        print(f"Debug: {info} Используемая графическая модель: {settings["graphic_model_name"]}")
        print(f"Debug: {info} Индекс микрофона: {settings["mic_index"]}")
        print(f"Debug: {info} Имя пользователя: {settings["user_name"]}")
    elif mode == "dbg.root":
        root = int(input("Введите код доступа:\n>>> "))
        if root == 9597:
            print(f"Debug: {info} Вы вошли в режим отладки.")
            while True:
                debug_command = input("Введите команду отладки (или 'exit' для выхода): ")
                if debug_command.lower() == "exit":
                    break
                elif debug_command == "dbg.info":
                    print(f"Debug: {info} Информация о программе:")
                    print(f"Debug: {info} Версия программы: {settings["version"]}")
                    print(f"Debug: {info} Используемая текстовая модель: {settings["text_model_name"]}")
                    print(f"Debug: {info} Используемая графическая модель: {settings["graphic_model_name"]}")
                    print(f"Debug: {info} Индекс микрофона: {settings["mic_index"]}")
                    print(f"Debug: {info} Имя пользователя: {settings["user_name"]}")

                    print(f"Debug: {info} Системная информация:")
                    print(f"Debug: {info} ОС: {platform.system()} {platform.release()}")
                    print(f"Debug: {info} Архитектура: {platform.machine()}")
                    print(f"Debug: {info} Процессор: {platform.processor()}")
                    for line in os.popen("wmic path win32_VideoController get name"):
                        if line.strip() and "Name" not in line:
                            print(f"Debug: {info} Видеокарта: {line.strip()}")
                    print(f"Debug: {info} Имя пользователя: {os.getlogin()}")
                    print(f"Debug: {info} Версия Python: {platform.python_version()}")
                else:
                    print("Неверная команда отладки.")
        else:
            print(f"Debug: {error} В доступе отказано. Возврат в главное меню")
    else:
        print("Неверный режим. Пожалуйста, выберите 1-5.")
    #endregion DEVELOP