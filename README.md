# Магазин техники Apple.

## Как развернуть локально
1. Клонируйте репозиторий 
```
git clone https://github.com/QuickLike/apple_store_bot
```
2. Перейдите в директорию
```
cd apple
```
3. Создайте файл .env и добавьте в него необходимые переменные окружения без фигурных скобок
```
SECRET_KEY={secret key django}
DEBUG={debug mode true or false}
ALLOWED_HOSTS={hosts separated with comma}

POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
DB_HOST=postgres
DB_PORT=5432

BOT_TOKEN={токен бота}
GROUPS_IDS={id групп на которые необходимо подписаться, разделенные запятыми}
GROUPS_LINKS={ссылки на группы для подписки, разделенные запятыми}

DJANGO_SUPERUSER_USERNAME={username суперпользователя}
DJANGO_SUPERUSER_EMAIL={email суперпользователя}
DJANGO_SUPERUSER_PASSWORD={password суперпользователя}
```
4. Запустите локальный сервер
```
docker-compose up --build
```


## Стек

Python

Django

Aiogram

Docker

Docker compose

[Власов Эдуард Витальевич](https://github.com/QuickLike)
