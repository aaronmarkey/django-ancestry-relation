import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-ancestry-relation',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License ',
    description='A Django app that makes an abstract Node model available for flat stacking hierarchical data in a database.',
    long_description=README,
    url='https://github.com/aaronmarkey',
    author='Aaron Markey',
    author_email='markeyaaron@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
    ],
)