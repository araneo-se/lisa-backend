from __future__ import print_function
from setuptools import setup, find_packages
import io
import codecs
import os
import sys

import backend

# Find where we are...
here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
	encoding = kwargs.get('encoding', 'utf-8')
	sep = kwargs.get('sep', '\n')
	buf = []
	for filename in filenames:
		with io.open(filename, encoding=encoding) as f:
			buf.append(f.read())
	return sep.join(buf)

long_description = read('README.txt', 'CHANGES.txt')

setup(
    name='backend',
    version=backend.__version__,
    url='http://github.com/johanwet/lisabackend/',
    license='Apache Software License',
    author='Johan Wettergren',
    install_requires=['Flask>=0.10.1',
							'phonenumbers>=7.0.2'
                      ],
    author_email='johan@araneo.se',
    description='Proof-of-Concept backend for CA LISA tests',
    long_description=long_description,
    packages=['backend'],
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
)
