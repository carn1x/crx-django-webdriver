# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='crx-django-webdriver',
    version='0.0.1',
    author='carn1x',
    author_email='github.com/carn1x',
    packages=['crx_django_webdriver'],
    install_requires=[
        'selenium==2.53.6',
        'django>=1.8',
    ],
    url='https://github.com/carn1x/crx-django-webdriver',
    license='GNU GENERAL PUBLIC LICENSE Version 3, see LICENCE',
    description='Helper methods and examples for defining pages within a Django application to simplify test writing.',
    long_description=open('README.md').read(),
    zip_safe=False,
)