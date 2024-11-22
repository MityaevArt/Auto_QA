﻿# Проект автоматизации тестирования API Яндекс Самокат

Проект направлен на автоматизацию проверки API для создания и отслеживания заказов.

## Необходимые условия
- Python 3.6+
- Установленные пакеты: pytest, requests

## Структура проекта
- configuration.py: URL и пути для тестового стенда.
- data.py: Данные для создания заказа.
- sender_stand_request.py: Функции и описания тестов.

## Шаги автотеста
1. Отправить запрос на создание заказа.
2. Сохранить трек-номер заказа.
3. Получить заказ по трек-номеру.
4. Проверить, что код ответа равен 200.

## Установка и запуск

### Установка

1. Клонируйте репозиторий:
   
2. Создайте и активируйте виртуальную среду:

   python -m venv venv

На Windows:
   .\venv\Scripts\activate

На macOS/Linux:
   source venv/bin/activate
   

3. Установите зависимости:

   pip install pytest requests
     
### Запуск тестов

Запустите тесты командой:

pytest -s

Опция -s покажет все выводы в терминале.
