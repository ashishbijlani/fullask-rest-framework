#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = [ ]

setup(
    author="fullask_rest_framework",
    author_email='twicegoddessana1229@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A fully-supported flask extension to build REST API.",
    entry_points={
        'console_scripts': [
            'fullask_rest_framework=fullask_rest_framework.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='fullask_rest_framework',
    name='fullask_rest_framework',
    packages=find_packages(include=['fullask_rest_framework', 'fullask_rest_framework.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/tgoddessana/fullask_rest_framework',
    version='0.1.0',
    zip_safe=False,
)
