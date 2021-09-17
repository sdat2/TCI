from setuptools import setup, find_packages

setup(
    name='tci',
    version='1.0.0',
    url='https://github.com/wy2136/TCI.git',
    author='Wenchang Yang',
    author_email='wenchang@princeton.edu',
    description='Calculate TC indices',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)
