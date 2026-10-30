py -m venv .venv

py -m pip install django

django-admin --version

source .venv/Scripts/activate

django-admin startproject config .

pip install django djangorestframework                       `'rest_framework'`(add in installed apps)
