Cookiecutter Django - First
===========================

Cookiecutter Django First is a 2 minutes Django project. No big dependencies and simple ready to use project
Powered by Cookiecutter_
Based on Cookiecutter-django_

Why
---

Sometimes all we need is start a fresh and functional project in 2 minutes rather than spend hours setting a complete environment

Features
---------

* FRONTEND: Default and very basic frontend files (CSS, Javascript)
* FRONTEND: Default landing page (index.html)
* FRONTEND: Default base.html template
* FRONTEND: CSS style using MaterializeCSS_ (light and mobile friendly)
* STRUCTURE: Default initial app
* STRUCTURE: Multiple environments (ready for development and production)
* STRUCTURE: Initial SQLite for quick prototyping
* STRUCTURE: Change settings using environment variables (django-environ_)


Requirements
-----------

First, get Cookiecutter. Trust me, it's awesome::

    $ pip install "cookiecutter>=1.4.0"


Get Started
-----------

Let's pretend you want to create your new product landing page. Rather than using `startproject` + `startapp`
and then editing the settings and much more...
get cookiecutter_ to do all the work.

Now run it against this repo::

    $ cookiecutter https://github.com/huogerac/cookiecutter-django-first

You'll be prompted for some values. Provide them, then a Django project will be created for you.

Answer the prompts with your own desired options_. For example::

    Cloning into 'cookiecutter-django-first'...
    remote: Counting objects: 550, done.
    project_name [Project Name]: My First Site
    project_slug [my_first_site]: myfirstsite
    first_app_name [core]: myapp
    author_name [Roger]: Roger
    email [you@example.com]: myemail@mydomain.com
    description [A short description of the project.]: Getting a django project in 2 minutes time.
    version [0.1.0]: 0.0.1

Then enter the project and run it::

    $ cd myfirstsite/
    $ pip install -r requirements/development.pip
    $ ./manage.py migrate
    $ ./manage.py runserver
    Go to http://localhost:8000


Notes
-----

* As other python projects, it is a good practice to use a Virtualenv_ instead of `pip install` directly into your global environment.


Community
-----------

* Have questions?
* Have suggestions?
* Get in touch or create an Issue_
* Contributions and Ideas are more than welcome!

.. _Issue: https://github.com/huogerac/cookiecutter-django-first/issues


Not Exactly What You Want?
---------------------------

Check the Cookiecutter-django_ repo


Credits
-------

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Cookiecutter-django: https://github.com/pydanny/cookiecutter-django
.. _MaterializeCSS: http://materializecss.com/
.. _django-environ: https://github.com/joke2k/django-environ
.. _Virtualenv: https://virtualenv.pypa.io/en/stable/
