# yamdb_final


![example workflow](https://github.com/ChukSerg/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

#### Описание
Программа для получения, хранения и предоставления отзывов пользователей на различные произведения (книги, фильмы, музыка и т.д.)
Программа собирается в контейнеры и разворачивается с помощью Docker compose
Автоматически проверяет тесты, обновляет образ на DockerHub, деплоит проект на боевой сервер при помощи Github Actions, отправляет 
сообщение на ваш телеграм-бот
#### Технологии
- Python 3.7
- Django 2.2.16
- Djangorestframework 3.12.4
#### Запуск проекта в dev-режиме
- Клонируйте репозиторий с помощью команды
````
git clone
````

- В папке infra создайте файл .env по следующему шаблону:
````
DB_ENGINE=django.db.backends.<ваша_база_данных> # указываем с какой базой работаем, например postgresql
DB_NAME=<имя_базы данных> # имя базы данных - измените на свое
POSTGRES_USER=<логин пользователя базы данных> # логин для подключения к базе данных - измените на свое
POSTGRES_PASSWORD=<уникальный пароль к базе данных> # пароль для подключения к БД (установите свой)
DB_HOST=<название контейнера> # название сервиса (контейнера)
DB_PORT=<номер порта> # порт для подключения к БД
```` 
В настройках Secrets репозитория создайте следующие переменные:
````
DOCKER_USERNAME - логин на DockerHub
DOCKER_PASSWORD - пароль на DockerHub
SSH_KEY - Скопируйте приватный ключ с компьютера, имеющего доступ к боевому серверу (cat ~/.ssh/id_rsa)
USER - сохраните имя пользователя для подключения к серверу
HOST - сохраните IP-адрес вашего сервера
PASSPHRASE - если при создании ssh-ключа вы использовали фразу-пароль
TELEGRAM_TO - сохраните ID своего телеграм-аккаунта. Узнать свой ID можно у бота @userinfobot
TELEGRAM_TOKEN - сохраните токен вашего бота. Получить этот токен можно у бота @BotFather
````
 - Перейдите в папку infra
- Соберите контейнеры с помощью команды:
````
docker-compose up -d --build
````
- Выполните последовательно следующие команды:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```

### Теперь проект доступен по адресу http://localhost/


#### Примеры запросов
###### Для неаутентифицированных пользователей:
- Регистрация пользователя: POST /api/v1/auth/signup/
- Получение JWT-токена: POST /api/v1/auth/token/
- Получение списка категорий: GET /api/v1/categories/
- Получение списка жанров: GET /api/v1/genres/
- Получение списка произведений: /api/v1/titles/
- Получение списка отзывов к произведению: /api/v1/titles/{title_id}/reviews/
- Получение списка комментариев к отзыву: /api/v1/titles/{title_id}/reviews/{review_id}/comments/
###### Только для аутентифицированных пользователей:
- Создание отзыва к произведению: POST /api/v1/titles/{title_id}/reviews/
- Создание комментария к отзыву: POST /api/v1/titles/{title_id}/reviews/{review_id}/comments/
###### Только для авторов публикации или комментария:
- Удаление отзыва: DELETE /api/v1/titles/{title_id}/reviews/{review_id}/
- Удаление комментария: DELETE /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
###### Подробная информация по запросам - /redoc/
### Авторы
Сергей Чукин
