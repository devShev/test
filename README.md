# Test task
Парсинг информации по артикулу товара WB.
Информация приходит с помощью WB API, сохраняется в JSON.

Протестировано на 30 артикулах.

## Зависимости:
- Docker


## Установка и запуск
- ```git clone https://github.com/devShev/test.git``` Скопировать репозиторий
- Создать файл ```.env.development``` и поместить во внутрь необходимые переменные окружения
```
#.env.development

# APP
DJANGO_SECRET_KEY='django-insecure-kr8v@ii!rccrc2=7a-jqssk80#%3m$$5ba#0bp62pa1$a@ylw*'

# DB
POSTGRES_HOST='postgres_test_db'
POSTGRES_PORT='5432'
POSTGRES_DB='test_db'
POSTGRES_USER='test_user'
POSTGRES_PASSWORD='gjsbUKEu5csdf2JruU123'

# REDIS
REDIS_HOST=redis_cache
REDIS_PORT=6379
REDIS_DB=0

# PGADMIN
PGADMIN_DEFAULT_EMAIL=root@mail.ru
PGADMIN_DEFAULT_PASSWORD=root

```

- Выполнить команду ```docker compose up```
