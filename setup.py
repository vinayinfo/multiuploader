# -*- coding: utf-8 -*-

"""
`setup.py` for `multiuploader`.
For project information check out:
https://github.com/vinaypost/multiuploader
For `setup.py` information check out:
https://docs.python.org/2/distutils/setupscript.html
"""

from distutils.core import setup

from setuptools import find_packages

from multiuploader import __version__

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules',
]


for cmd in ('egg_info', 'develop'):
    import sys
    if cmd in sys.argv:
        from setuptools import setup

setup(
    name = 'multiuploader',
    version = __version__,
    author = 'Vinay Kumar',
    author_email = 'vk-sharma@outlook.com',
    packages = find_packages(),
    license = 'LICENSE.txt',
    description = 'Multiuploader - is an application which enable ability to upload multiple files in Django',
    long_description = open('README.md').read(),
    include_package_data = True,
    url = 'https://github.com/vinaypost/multiuploader',
    download_url = 'https://github.com/vinaypost/multiuploader/archive/0.1.01.tar.gz',
    keywords = ['multiupload', 'multiuploader', 'fileupload', 'mediaupload', 'imageupload'],
    platforms=['OS Independent'],
    classifiers = CLASSIFIERS,
    install_requires=['django>=1.10', 'sorl-thumbnail>=12.3', 'python-magic>=0.4.12'],
    zip_safe=False,
)
