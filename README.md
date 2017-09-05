Django Ancestry Relation
------------------------
Provides an abstract model class for heirarchical data to be stored in a database. 
Provides a manager to interface with the model.

Documentation is in the "docs" directory.

Requirements
------------
* Python 3.4 or higher
* Django 1.11

Quick start
-----------
1. Install via pip `pip install django-ancestry-relation`
2. Add "django_ancestry_relation" to your INSTALLED_APPS setting like this::
```
INSTALLED_APPS = [
    ...,
    'django_ancestry_relation'
]
```

Notes
-----
* Most efficient using Postgres as Django DB backend.
