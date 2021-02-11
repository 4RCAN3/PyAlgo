from setuptools import *
from os import path

directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding = 'utf-8') as f:
    long_description = f.read()

setup( 
        name ='pyalgo-lib',
        version = '0.0.1',
        author ='Devansh Singh',
        author_email ='devanshamity@gmail.com',
        url ='https://github.com/Devansh3712/PyAlgo',
        description ='Library for algorithm implementations in python',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license = 'MIT',
        packages = ["pyalgo"],
        include_package_data = True,
        classifiers =[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
)