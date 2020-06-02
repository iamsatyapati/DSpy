# DSPy
Scrapy website scrapper

though it is a required package, still using in a virtual environment is recommended. 

## Using pip virtual environment
- to install pip virtual environment : pip install pipenv
- to create a virtual environment : virtualenv .
- activate your virtual environment : ./bin/activate

Installing scrapy - pip install scrapy
starting a scrapy project - scrapy startproject projname

Your project lies in projname folder.

Directory structures

1. Spider : Your spider file should be created inside this directory.
2. settins.py : Holds all the setting for your project. Bot name is your spider name.
3. pipeline.py : Move your data, like from programs to database.
4. middleware.py : Adding middle wares in our requests like proxies.

To use scrapy shell : scrapy shell url
