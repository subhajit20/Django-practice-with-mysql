Django with mysql integrations

step 1 ------ pip install pymysql
step 2 ------- create model in the model file 
step 3 ------- after creating model go to cmd and type python manage.py appname makemigrations

step 4 ------- After that type python manage.py appname migrate 
step 5 -------  At last we have to type python manage.py makemigartions 

This migrate all the changes in our project folder as well as in the app folder .....

****** Important *****
Declare this in the setting folder in the project folder .....

import pymysql
pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db',
        'USER':'root',
        'PASSWORD':'12345',
        'HOST':'localhost',
        'PORT':'3306'
    }
}
