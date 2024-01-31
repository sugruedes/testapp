##
# Portfolio is a django web app hosted on Parrot.
# It has two apps, 'pages' and 'project' and the
# associated database.
#
# create a directory to contain the project and cd into it.
# python3 -m venv venv
# source venv/biin/activate
# python3 -m pip install django
# pip install mod_wsgi
# pip freeze > requirements.txt OR pip -r requirements.txt
# django-admin startproject <project name> . (NB! Note the 'dot')
# <write code>
# python3 manage.py runserver
# python3 manage.py makemigrations <app name>
# python3 manage.py migrate <app name>
# python3 manage.py startapp pages
# mkdir -p pages/templates/pages  [keep templates tidy and app specific]
# touch pages/templates/pages/index.html
# touch urls.py
#
#python3 manage.py createsuperuser
#user: superuser
#password: Pa%%w0rd
#python3 

# Add ENVIRONMENT VARS SECRET_KEY, DEBUG, ALLOWED_HOSTS CSRF_TRUSTED_ORIGINS SECURE_SSL_REDIRECT 
# Also: SCM_BUILD.... to True
# Install env with pip install python-dotenv

#######################
## Postgres Specific ##
#######################
# To use Postgres instead of SQLite, first install the database adapter:
# pip install psycopg2-binary (add psycopg2-binary==2.9.5 to requirements.txt)
#
# Azure connection string:
# dbname=<db_name> host=<db_host> port=5432 user=<db_user> password=<db_password>
#
# split this into EVs, DBNAME, DBHOST, DBUSER, DBPASS
#
# And update DATABASE section of settings.py to:
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': os.environ.get('DBNAME'),
#        'HOST': os.environ.get('DBHOST'),
#        'USER': os.environ.get('DBUSER'),
#        'PASSWORD': os.environ.get('DBPASS'),
#        'OPTIONS': {'sslmode': 'require'},
#    }
#}
#
# Azure also requires 'sslmode', so set it.
# 'pip install gunicorn' to use production level WSGI server 
#
# Using WSGI
#
# Find path to VIRTUAL ENV to configure venv in mod_wsgi:
#  'python -c 'import sys; print(sys.prefix)'
#
# Serving static files in production:
# set STATIC_ROOT in settings - its shere 'collectstatic' will copy
# static files to. Run 'collectstatic'
# Edit apache2.conf to include following:
###############################################
## Django mod_wsgi configuration for testapp ##
###############################################
#
#WSGIScriptAlias / /var/www/apps/testapp/testapp/wsgi.py
#WSGIPythonHome /var/www/apps/testapp/venv
#WSGIPythonPath /var/www/apps/testapp
# Application Group is crucial - WAIT_CLOSE errors on each thread otherwise!
#WSGIApplicationGroup %{GLOBAL} or %{SERVER}
#
#<Directory /var/www/apps/testapp>
#<Files wsgi.py>
#Require all granted
#</Files>
#</Directory>
#
#Alias /robots.txt /var/www/testapp/static/robots.txt
#Alias /favicon.ico /path/to/mysite.com/static/favicon.ico
#
#Alias /media/ /var/www/testapp/media/
#Alias /static/ /var/www/testapp/static/
#
#<Directory /var/www/testapp/static>
#Require all granted
#</Directory>
#
#<Directory /var/www/testapp/media>
#Require all granted
#</Directory>
