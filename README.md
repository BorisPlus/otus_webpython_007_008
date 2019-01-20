# INDEX page

Проект сайта курсов дистанционного обучения (открытые уроки музыки)

## Описание

### Требования

Установите:

```bash
$ pip3 install -r requirements.txt
```

### Результаты ДЗ занятия 7 (прикручен бэкэнд) 

#### Dev

```bash
python3 ./manage.py makemigrations --settings=applicatura.settings.dev
python3 ./manage.py migrate --settings=applicatura.settings.dev
python3 ./manage.py init_test_data --settings=applicatura.settings.dev

python3 ./manage.py runserver --settings=applicatura.settings.dev
python3 ./manage.py createsuperuser --username=admin --email=admin@admin.admin  --settings=applicatura.settings.dev
```

#### Dev

```bash
python3 ./manage.py makemigrations --settings=applicatura.settings.prod
python3 ./manage.py migrate --settings=applicatura.settings.prod
python3 ./manage.py init_test_data --settings=applicatura.settings.prod

python3 ./manage.py collectstatic --settings=applicatura.settings.prod
python3 ./manage.py runserver --settings=applicatura.settings.prod
python3 ./manage.py createsuperuser --username=admin --email=admin@admin.admin  --settings=applicatura.settings.dev
```

Предупреждаю: цветопередача скринкаста просто жутчайшая. Но и я не "художник" )

#### Как этим управляет админ

![django_admin](https://raw.githubusercontent.com/BorisPlus/otus_webpython_007_008/master/README.files/images/screencasts/django_admin.gif "Title")

#### Как это видит пользователь

![django_user](https://raw.githubusercontent.com/BorisPlus/otus_webpython_007_008/master/README.files/images/screencasts/django_user.gif "Title")
  
#### Как это видит пользователь (доп список подписок)

![django_user](https://raw.githubusercontent.com/BorisPlus/otus_webpython_007_008/master/README.files/images/screencasts/django_user.gif "Title")
  

### Результаты ДЗ занятия 8 (прикручен REST API) 

Открытая часть:
* http://localhost:8000/rest_api/course/list - список курсов
* http://localhost:8000/rest_api/course/1 - курс подробно с уроками
* http://localhost:8000/rest_api/lesson/1 - урок подробно

Закрытая часть:
* http://localhost:8000/rest_api/subscriber/create - создание учетки подписчика
* http://localhost:8000/rest_api/subscriber/login - login подписчика
* http://localhost:8000/rest_api/subscriber/current - создание учетки подписчика
* http://localhost:8000/rest_api/subscriber/logout - оказывается это целая проблема JWT-logout, решают топорно, через введение UIID-поля токена пользователя
* http://localhost:8000/rest_api/subscriber/lesson/list - уроки подписчика

Только для админа :
http://localhost:8000/rest_api/subscription/list - (для админа только) подписки всех на все 

## Авторы

* **BorisPlus** - [https://github.com/BorisPlus/otus_webpython_013](https://github.com/BorisPlus/otus_webpython_013)

## Лицензия

Свободно

## Дополнительные сведения

Проект в рамках домашнего задания курса "Web-разработчик на Python" на https://otus.ru/learning
python3 manage.py createsuperuser --username=admin --email=admin@admin.admin
python3 manage.py createsuperuser --username=admin --email=admin@applicatura.ru --settings=applicatura.settings.prod
