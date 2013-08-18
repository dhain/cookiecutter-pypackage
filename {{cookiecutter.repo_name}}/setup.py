#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


_dir = os.path.dirname(__file__)
readme = open(os.path.join(_dir, 'README.rst')).read()
history = open(os.path.join(_dir, 'HISTORY.rst')).read().replace(
    '.. :changelog:', '')


setup_args = dict(
    name='{{ cookiecutter.repo_name }}',
    version='{{ cookiecutter.version }}',

    description='{{ cookiecutter.project_short_description }}',
    long_description=readme + '\n\n' + history,

    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    keywords='{{ cookiecutter.repo_name }}',

    packages=[
        '{{ cookiecutter.repo_name }}',
        '{{ cookiecutter.repo_name }}.test',
    ],
    include_package_data=True,
    zip_safe=False,

    install_requires=[
    ],

    test_suite='{{ cookiecutter.repo_name }}.test',
    tests_require=[
    ],
)


if __name__ == '__main__':
    setup(**setup_args)
