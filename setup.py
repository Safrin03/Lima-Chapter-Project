from setuptools import setup, find_packages

setup(
    name='LimaChapterAnalysis',
    packages = find_packages(),
     install_requires=[
        'plotly',
        'openai',
        'geopandas',
       
    ],
)
