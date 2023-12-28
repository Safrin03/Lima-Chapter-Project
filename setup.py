from setuptools import setup, find_packages

setup(
    name='Home',
    py_modules=['Home'],
    packages=find_packages(),
    install_requires=[
        'geopandas',
        'openai',
    ],
)
