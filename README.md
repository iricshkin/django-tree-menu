## Django app древовидное меню

Django приложение реализовывающее древовидное меню через templatetag. Добавление новых меню и его элементов в бд просходит через админку Django. Нарисовать на любой нужной странице меню по его slug c помощью тега {% draw_menu 'main_menu' %}, где 'main_menu' - slug нужного меню.

### Стек технологий

![Django-app workflow](https://github.com/iricshkin/django-tree-menu/actions/workflows/app-testing.yml/badge.svg)

[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)

- Python 3.10
- Django 4.1.7

### Установка и запуск

1. Cклонировать репозиторий `git@github.com:iricshkin/django-tree-menu.git`

2. Создать и заполнить .env файл по аналогии с .env.example

3. Установить зависимости `poetry install`

4. Для запуска сервера разработки, находясь в директории проекта выполнить команды:

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

5. Заполнить БД. Создайть меню с именем "main_menu" и заполнить несколько полей модели Item

### Об авторе

Ирина Фок [iricshkin](https://github.com/iricshkin/)
