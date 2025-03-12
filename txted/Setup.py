from setuptools import setup, find_packages
from os import path
working_directory = path.abspath(path.dirname(__file__))

with open(path.join(working_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='txted', # name of packe which will be package dir below project
    version='0.0.1',
    author='Bobiptus',
    author_email='al24760228@ite.edu.mx',
    description='Libreria para manipulacion de archivos de texto',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[],
)