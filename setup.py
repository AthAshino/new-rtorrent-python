from setuptools import setup, find_namespace_packages
import os, sys

# version = __import__('rtorrent').__version__

classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Communications :: File Sharing",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

setup(
    name="new-rtorrent-python",
    version='1.0.0-alpha',
    url='https://github.com/sickchill/rtorrent-python',
    author='Chris Lucas',
    author_email='miigotu@gmail.com',
    maintainer='Dustyn Gibson',
    maintainer_email='miigotu@gmail.com',
    description='A simple rTorrent interface written in Python',
    keywords="rtorrent p2p",
    license="MIT",
    packages=find_namespace_packages(),
    scripts=[],
    install_requires=[
        'bencodepy',
        'requests'
    ],
    tests_require=[
        'nose'
    ],
    test_suite='nose.collector',
    classifiers=classifiers,
    include_package_data=True,
)
