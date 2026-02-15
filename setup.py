from setuptools import setup,find_packages
from typing import List

def Requirements()->List[str]:
    with open('Requirements.txt') as f:
        return f.read().splitlines()

setup(
    name='Practice',
    version='0.1',
    packages=find_packages(),
    install_requires=Requirements(),
    author='Omkar',
    author_email="ok.@gmail.com"
)