#region IMPORTS
from g4f.client import Client
from consts import warning, info, error, assist
import webbrowser
from save_editor import *
import subprocess
import multiprocessing as mp
import pyautogui
import datetime
#endregion IMPORTS

history = []

sys_prompt = f"Ты - умный помощник, который отвечает на вопросы пользователей. Твоя задача - давать точные и полезные ответы на вопросы. Если ты не знаешь ответа, просто скажи об этом. Будь вежлив. Сообщи, если ответ может быть не точен.Обращайся к пользователю по имени {settings["user_name"]}. Тебя зовут Алман/Алмон(Alman/Almon)"

def save_to_history(prompt, answer_ai):
    history.append({"role": "user", "content": prompt})
    history.append({"role": "assistant", "content": answer_ai})

#region AI


def gpt_text_no(message: str):
    client = Client(showless=True, browserless=True)

    response = client.chat.completions.create(
        model=settings["text_model_name"],
        messages=[{"role": "system", "content": sys_prompt},
                  {"role": "user", "content": message}],
        web_search=False,
    )
    return response.choices[0].message.content


def gpt_text_web(message: str):

    client = Client(showless=True, browserless=True)

    response = client.chat.completions.create(
        model=settings["text_model_name"],
        messages=[{"role": "system", "content": sys_prompt},
                  #*history,
                  {"role": "user", "content": message}],
        web_search=True,
    )
    return response.choices[0].message.content


def gpt_img(message: str):

    client = Client()

    response = client.images.generate(
        model=settings["graphic_model_name"],
        prompt=message,
        response_format="url"
    )
    return response.data[0].url

#endregion AI



#region USER_COMMANDS
def open_browser():
    print(f"{assist} Открываю браузер...")
    webbrowser.open("https://ya.ru/")


def open_url(url):
    print(f"{assist} Открываю URL: {url}")
    webbrowser.open(url)


def open_youtube():
    print(f"{assist} Открываю YouTube...")
    webbrowser.open("https://www.youtube.com/")


def vpn():
    print(f"{assist} Запускаю VPN...")
    subprocess.Popen("C:\\Program Files\\Proton\\VPN\\ProtonVPN.Launcher.exe")


def open_discord():
    print(f"{assist} Открываю Discord...")
    user_login = os.getlogin()
    subprocess.Popen(f"C:\\Users\\{user_login}\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe")


def open_steam():
    print(f"{assist} Открываю Steam...")
    subprocess.Popen("G:\\GameCenter\\Steam\\steam.exe")


def make_screenshot():
    if not os.path.exists("images"):
        os.makedirs("images")
    filename = f"images/screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    print(f"{assist} Скриншот сохранен как {filename}")


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#endregion USERCOMMANDS