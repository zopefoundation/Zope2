import os
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))


def _read_file(filename):
    with open(os.path.join(HERE, filename)) as f:
        return f.read()


README = _read_file('README.rst')
CHANGES = _read_file('CHANGES.rst')


version = '4.0b1'

setup(
    name='Zope2',
    version=version,
    url='https://zope.readthedocs.io/en/latest/',
    license='ZPL 2.1',
    description='Zope application server / web framework',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    long_description="\n\n".join([README, CHANGES]),
    keywords="zope application server WSGI meta",
    classifiers=[
        'Development Status :: 6 - Mature',
        "Environment :: Web Environment",
        "Framework :: Zope2",
        "License :: OSI Approved :: Zope Public License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    zip_safe=False,
    install_requires=[
        'Zope >= 4.0b1',
    ],
)
