# -*- coding: utf-8 -*-
from distutils.core import setup

from setuptools import find_packages

for cmd in ('egg_info', 'develop'):
    import sys
    if cmd in sys.argv:
        from setuptools import setup

setup(
    name='multiuploader',
    version='0.1.02',
    author='Vinay Kumar',
    author_email='vk-sharma@outlook.com',
    packages=find_packages(),
    license='MIT License, see LICENCE.txt',
    description='Adds jQuery dynamic form for uploading multiple files',
    long_description=open('README.md').read(),
    include_package_data=True,
    url = 'https://github.com/SharmaVinayKumar/multiuploader', # use the URL to the github repo
    download_url = 'https://github.com/SharmaVinayKumar/multiuploader/tarball/0.1', # I'll explain this in a second
    keywords = ['multipleupload', 'fileupload', 'mediaupload', 'imageupload'], # arbitrary keywords
    install_requires=['django>=1.10', 'sorl-thumbnail>=12.3', 'python-magic>=0.4.12'],
    zip_safe=False,
)
