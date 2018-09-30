# INDEX page

Проект приветственной страницы сайта курсов дистанционного обучения

## Описание

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
* коричневый на коричневом — только в заголовке и только лого, но с черной обводкой. мне так нравится
 
## Вопросы

* правильно ли _div.footer_ в style организован? может можно что погибче, <footer> я не осилил.
* если браузер не раскрывать на весь экран, то меню НЕ идет со скролом до самого конца вниз? то есть, есть период, когда меню перестает идти вниз и начинает скрываться наверху. .wrapper-а нет больше, а поведение меню осталось

## Cкриншоты

### Демонстрация подсветки меню:

![index](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/README.files/images/screenshots/index.png "Title")


### Демонстрация привязки меню к прокрутке:

![index_slider](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/README.files/images/screenshots/index_scrolled_with_menu.png "Title")


### Низ страницы всегда снизу:

![index_bottom](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/README.files/images/screenshots/empty.png "Title")

### Переопределение при узком экране:

![narrow_monitor](https://raw.githubusercontent.com/BorisPlus/otus_webpython_013/master/README.files/images/screenshots/narrow_monitor.png "Title")


## Авторы

* **BorisPlus** - [https://github.com/BorisPlus/otus_webpython_013](https://github.com/BorisPlus/otus_webpython_013)

## Лицензия

Свободно

## Дополнительные сведения

Проект в рамках домашнего задания курса "Web-разработчик на Python" на https://otus.ru/learning
