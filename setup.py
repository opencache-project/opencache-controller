#!/usr/bin/env python2.7

from setuptools import setup, find_packages

conf = dict(
    name='opencache-controller',
    version='0.1.0',
    description='Controller for a number of connected OpenCache Nodes.',
    long_description='For more details and the README, please see our `GitHub page <https://github.com/opencache-project/opencache-controller>`_.',
    author='Matthew Broadbent',
    author_email='matt@matthewbroadbent.net',
    scripts=['scripts/opencache-controller'],
    install_requires=['pymongo', 'pyzmq', 'configparser', 'opencache-lib'],
    url='https://github.com/opencache-project/opencache-controller',
    download_url = 'https://github.com/opencache-project/opencache-controller/tarball/0.1.0',
    license='Apache License, Version 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: DFSG approved',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: System :: Networking',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Logging',
        'Topic :: System :: Monitoring'
        ],
    keywords = ['content', 'caching', 'distribution', 'software defined networking'],
    packages=find_packages(),
    namespace_packages=['opencache']
)

setup(**conf)
