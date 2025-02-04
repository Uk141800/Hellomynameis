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
git copy https://github.com/Uk141800/hellomynameis.git
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
![chrome_i7FxlSmWtz.gif](..%2F..%2F..%2FDownloads%2FShareX-17.0.0-portable%2FShareX%2FScreenshots%2F2025-02%2Fchrome_i7FxlSmWtz.gif)
## Лицензия

Этот проект распространяется под лицензией **GNU General Public License v3.0**.  
Подробности можно найти в файле [LICENSE](LICENSE).