# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

for cmd in ('egg_info', 'develop'):
    import sys
    if cmd in sys.argv:
        from setuptools import setup

setup(
    name='multiuploader',
    version='0.1',
    author='Vinay Kumar',
    author_email='vk-sharma',
    packages=find_packages(),
    license='MIT License, see LICENCE.txt',
    description='Adds jQuery dynamic form for uploading multiple files',
    long_description=open('README.md').read(),
    include_package_data=True,
    install_requires=['django>=1.4', 'sorl-thumbnail>=11.12.1b', 'python-magic'],
    zip_safe=False,
)
