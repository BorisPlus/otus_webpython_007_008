# INDEX page

Проект приветственной страницы сайта курсов дистанционного обучения

## Описание

### Требования

Данный проект использует:
* Django 2

Установите:

```bash
$ pip3 install 'django>=2.1'
```

или

```bash
$ pip3 install -r requirements.txt
```

### Старт

```bash
python3 ./manage.py runserver --settings=applicatura.settings.dev
```

### Результаты ДЗ занятия 13 (HTML, верстка)

* Страница имеет меню, разделенное на общее (слева) и клиентское (справа).
* Меню движется с прокруткой
* Низ страницы снизу
* черный текст на светло коричневом
* шрифт кастомный через api google
* иконки у списка
* максимально отвязал классы от тегов в div content
* селектор на потомков содержит класс потомка
* строки в главной области укоротил за счет 24px шрифта, узкая область мне не нравится
* сделал переопределение для узкого экрана
* черный на коричневом
 
### Результаты ДЗ занятия 15 (элементы JavaScript)

Режим BugReport на JavaScript. 

Механизм формирования сообщения BugReport и как будто отправляются:
* адрес страницы
* выделенный пользователем текст
* дополнительный комментарий пользователя
* CameCase
* ООП
* кнопка, универсально

### Результаты ДЗ занятия 17 (Расписание JavaScript)

Режим просмотра дополнительных данных карточек музыкальных инструментов. Если навести, то увеличится карточка. 
Если щелкнуть, то поверх всего нарисуется область (пока полупустая).
Если на область щелкнуть, то закроется.

Чего нет: 
* щелкание другого инструмента не приводит к закрытию допинформации по предыдущему, доп инфа как бы наслаивается.
Это можно переделать, но времени нет.
* можно навесить на щелкание вне области доп.информации закрытие всех доп.информаций

## Cкриншоты

### Результаты ДЗ занятия 13

#### Демонстрация подсветки меню:

![index](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/README.files/images/screenshots/index.png "Title")


#### Демонстрация привязки меню к прокрутке до самого низа страницы:

![index_slider](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/README.files/images/screenshots/index_scrolled_with_menu.png "Title")


#### Низ страницы всегда снизу даже при пустой странице:

![empty](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/README.files/images/screenshots/empty.png "Title")

#### Переопределение при узком экране:

![narrow_monitor](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/README.files/images/screenshots/narrow_monitor.png "Title")


### Результаты ДЗ занятия 15

#### Сообщение о работе BugReport:

см. "Если нашли ошибку, выделите текст и нажмите на кнопку."

![bag_report_narrow_monitor](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/README.files/images/screenshots/js_015/bag_report_normal_monitor.png "Title")

![narrow_monitor](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/README.files/images/screenshots/js_015/bag_report_narrow_monitor.png "Title")


#### Выделите мышкой:

![mark](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/README.files/images/screenshots/js_015/mark_normal_monitor.png "Title")

![mark_narrow_monitor](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/README.files/images/screenshots/js_015/mark_narrow_monitor.png "Title")

#### Нажмите кнопку и заполните форму по желанию:

![promt](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/README.files/images/screenshots/js_015/promt_normal_monitor.png "Title")

![promt_narrow_monitor](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/README.files/images/screenshots/js_015/promt_narrow_monitor.png "Title")

#### Благодарность:

![thanks_message](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/README.files/images/screenshots/js_015/thanks_normal_monitor.png "Title")

![thanks_message](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/README.files/images/screenshots/js_015/thanks_narrow_monitor.png "Title")

через 3 секунды все вернется обратно, а выделение останется.

### Результаты ДЗ занятия 17

Карточки курсов заменил на карточки инструментов

![cards](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/project/cards.html "Title")

#### Список инструментов

![instruments](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/README.files/images/screenshots/js_017/instruments.png "Title")

![instruments_narrow](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/README.files/images/screenshots/js_017/instruments_narrow.png "Title")

#### Навели на инструмент

![instrument_hover](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/README.files/images/screenshots/js_017/instrument_hover.png "Title")

![instrument_hover_narrow](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/README.files/images/screenshots/js_017/instrument_hover_narrow.png "Title")

#### Щелкнули на инструмент

Появившаяся область закроется, если в любом месте щелкнуть на эту облать доп. информации

![instrument_clicked](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/README.files/images/screenshots/js_017/instrument_clicked.png "Title")

![instrument_clicked_narrow](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/README.files/images/screenshots/js_017/instrument_clicked_narrow.png "Title")



### Результаты ДЗ занятия 7 (прикручен бэкэнд) 

Вышло немного не хронологически ))))

```bash
python3 ./manage.py runserver --settings=applicatura.settings.dev
```

#### Как этим управляет админ

![django_admin](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/README.files/images/screenshots/js_017/django_admin.png "Title")

#### Как это видит пользователь

![django_user](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/README.files/images/screenshots/js_017/django_user.png "Title")

## Авторы

* **BorisPlus** - [https://github.com/BorisPlus/otus_webpython_013](https://github.com/BorisPlus/otus_webpython_013)

## Лицензия

Свободно

## Дополнительные сведения

Проект в рамках домашнего задания курса "Web-разработчик на Python" на https://otus.ru/learning
