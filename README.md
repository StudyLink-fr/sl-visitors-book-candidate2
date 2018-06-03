# work-studylink

Quick start
-----------

How to start the app, following all steps.

----

1. virtualenv . -p /usr/bin/python

----

2. source bin/activate

----

3. pip install --upgrade pip

----

4. pip install Django

----

5. django-admin startproject 'enter the name you want'

----

6. Copy the polls directory in 'enter the name you want'

----

7. Add "polls" to your INSTALLED_APPS setting in settings.py like this::

    INSTALLED_APPS = [                                                          
        ...                                                                     
        'polls',                                                                
    ]                                                                           

----

8. Include the polls URLconf in your project urls.py like this::

    url(r'^polls/', include('polls.urls')),

and include : from django.conf.urls import include

----

9. Run `python manage.py migrate` to create the polls models.

----

10. Start the development server : python manage.py runserver

----

11. Visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

To create an admin account, see the doc "docs/admin_account.txt"

----

12. Visit http://127.0.0.1:8000/polls/ to participate in the poll.
