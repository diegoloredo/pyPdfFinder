#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Based on nscms setup.py
"""
from distutils.core import setup
import os
import re
import sys

package = 'pdffinder'
install_requires = u"""
Pillow==2.5.3
PyPDF2==1.23
pyPdf==1.13
reportlab==3.1.8
""".strip().split("\n")


CLASSIFIERS = [
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks'
]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]
    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])

    return {package: filepaths}


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search(
        "^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)


if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    args = {'version': get_version(package)}
    sys.exit()


setup(name='pyPdfFinder',
      version=get_version(package),
      description=('A pdf api created to easy find and write words at a '
                   'pdf file'),
      author='Diego Loredo',
      author_email='dsloredo@gmail.com',
      url='https://github.com/diegoloredo/pyPdfFinder',
      packages=get_packages(package),
      packages_data=get_package_data(package),
      license='BSD',
      install_requires=install_requires,
      classifiers=CLASSIFIERS,
      )
