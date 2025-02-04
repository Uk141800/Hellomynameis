# Hello, my name is...

## Что это
Web-based инструмент для создания QR кода с vCard.

Вводим данные о себе, получаем QR код, при сканировании которого будет создаваться контакт в телефоне.
## Как запустить в первый раз?
Запускаем командную строку любимым образом.

Переходим в папку командой
```commandline
cd path\to\folder
```
Копируем себе сервер из репозитория 
```commandline
git copy https://github.com/Uk141800/Hellomynameis.git
```
Создаем и активируем виртуальное окружение
```commandline
python -m venv venv
venv\Scripts\activate
```
Устанавливаем библиотеки
```commandline
pip install -r requirements.txt
```
Запускаем сервер:
```commandline
python app.py
```

В браузере открываем http://127.0.0.1:8050

...

PROFIT
## Как запустить во второй раз?
```commandline
cd path\to\folder
venv\Scripts\activate
python app.py
```
## Демонстрация
![chrome_i7FxlSmWtz](https://github.com/user-attachments/assets/34683d61-a4e5-422f-b715-6f882418d5be)
## Лицензия

Этот проект распространяется под лицензией **GNU General Public License v3.0**.  
Подробности можно найти в файле [LICENSE](LICENSE).
