# Django.-Homework-1_1-Introduction

----

# 1.1. Знакомство с Django. Подготовка и запуск проекта.

----

1. Создал проект "Django_Homework1_Introduction"
2. Создал приложение "app_homework1_1"
3. Зарегистрировал вновь созданное приложение "app_homework1_1" в файле settings.py в списке INSTALLED_APPS
4. В проекте "Django_Homework1_Introduction" в файле urls.py подключил метод include и 
добавил путь path('', include('app_homework1_1.urls'))
5. Отслеживаю url адреса, а именно переход на главную страницу и делегирую эти полномочия приложению "app_homework1_1".
6. Создал файл urls.py в приложении "app_homework1_1".
7. В файле Views импортирую HttpResponse из django.http. Создаю функцию homepage, которая выводит текст "Список доступных страниц"
8. Возвращаюсь в файл app_homework1_1/urls.py импортирую файл Views и обращаюсь к функции homepage
9. Проверяю результат. Запускаю команду python manage.py runserver. Работает, барузер отобразил текст "Список доступных страниц"
10. Добавляю страницы в приложение "app_homework1_1":
    current_time/ - показывает текущее время в любом удобном вам формате;
    workdir/ – выводит содержимое рабочей директории.
11. B файле Views импортирую модули datetime и os
12. Создаю страницы current_time и workdir на которых реализую показ текущего времени и отображение содержимого рабочей директории
13. На страницы current_time и workdir добавляю навигационные кнопки возврат "На главную"
14. Создал файл requirements.txt посредством команды pip freeze > requirements.txt. так как команда pip install -r requirements.txt
выдала ошибку  ERROR: Could not open requirements file: [Errno 2] Нет такого файла или каталога: 'requirements.txt'




