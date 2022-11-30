import os
import sys
import warnings

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='epi-py',
    version='0.0.2',
    packages=find_packages("src"),
    install_requires=[],
    test_suite='tests.test.all',
    url='https://github.com/tkruer/epi-py',
    license='MIT',
    author='Tyler Kruer',
    author_email='tylerkruer1@gmail.com',
    long_description=long_description,
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
    ],
    package_dir={'':"src"},
    python_requires=">=3.9",
    entry_points={
        'console_scripts': [
            'hwpypcmd=hwpyp.mypy:sayHello',
        ]
    }
)