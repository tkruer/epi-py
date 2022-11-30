import os
import sys
import warnings

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='epi-py',
    version='0.0.2',
    packages=['epi-py'],
    install_requires=[

    ],
    test_suite='epi-py.test.all',
    url='https://github.com/tkruer/epi-py',
    license='MIT',
    author='Tyler Kruer',
    author_email='tylerkruer1@gmail.com',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    description='Epidemiology Package for Python',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)