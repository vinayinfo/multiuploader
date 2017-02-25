# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

for cmd in ('egg_info', 'develop'):
    import sys
    if cmd in sys.argv:
        from setuptools import setup

setup(
    name='django-multiuploader',
    version='0.2.9',
    author=u'Sinitsin Vladimir and Ivanov Vitaly',
    author_email='vs@llc.ac; vit@nlstar.com',
    packages=find_packages(),
    url='http://openite.com/ru/store/item/django-multiuploader.html',
    license='BSD licence, see LICENCE.txt',
    description='Adds jQuery dynamic form for uploading multiple files',
    long_description=open('README.rst').read(),
    include_package_data=True,
    install_requires=['django>=1.4', 'sorl-thumbnail>=11.12.1b', 'python-magic'],
    zip_safe=False,
)
