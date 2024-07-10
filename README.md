# Данный проект реализцуется для учета продукции

Этот проект реализуется для учета продукции в магазине пока что отсутсвует frontend и авторизация в будушем будет добавленно

>Требование
 
    • Git
    • Python 3.12.3
    • PostgreSQL

>Клонируем репозиторий куда удобно

    git clone https://github.com/sultangame/counting_on_fastapi.git
>Установка нужных зависемостей для проекта

    pip install -r requirement.txt
> Создаем таблицы в бд командой в терминале alembic upgrade head

> И в конце настраивоте по примеру example.env  свой app.env

>Запуск проекта
 
    python3 main.py

> Переходим на http://localhost:8000/docs
