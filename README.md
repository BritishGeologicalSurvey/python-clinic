# Python Clinic

Resources linked to the Lyell Centre and Keyworth Python clinics

## Handy links

#### Python distributions

+ [Anaconda](https://www.anaconda.com/download/)

#### Tutorials

+ [The Python Tutorial](https://docs.python.org/3/tutorial/): Sections
  1 - 5 are essential for getting started. Sections 10 and 11 are always worth
revisiting even by experienced developers.
+ [Scipy Lecture Notes](https://www.scipy-lectures.org/): Section 1 is an
  excellent start for using Python for data. Download as PDF and work away
online.

#### Demos

+ [GeoPandas Demo](https://github.com/BritishGeologicalSurvey/geopandas-demo):
  Demonstrates Jupyter notebook, Pandas data frames and automation of GIS
analysis.

#### Misc

+ [BGS Teams: Discuss Python ](https://teams.microsoft.com/l/channel/19%3a4cab3e4fd4ab4c0e86f35e5bc75bb528%40thread.skype/Discuss%2520Python?groupId=986a7d3d-501a-4b2c-b8f5-5be979296946&tenantId=b311db95-32ad-438f-a101-7ba061712a4e)
+ [Feather](https://blog.rstudio.com/2016/03/29/feather/) is a data file format
  that allows rapid access to large datasets within R. Pandas has functions
e.g.
[to_feather](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_feather.html)
that can read/write Feather files.

## Useful libraries

#### Standard library


+ datetime - Tools for dealing with date and time data
+ logging - Log what's going on within your code
+ [pathlib](https://realpython.com/python-pathlib/) - Object-oriented utilities to deal the files and directories
+ traceback - Utilities for handling error message stack traces
+ [subprocess](https://docs.python.org/3/library/subprocess.html) - amongst other things, allows access to command line utilities

#### Science

+ [Numpy](http://www.numpy.org/) - Adds arrays for numerical work (turns Python into Matlab)
+ [Pandas](https://pandas.pydata.org/) - Adds dataframes for tabular data and time series (turns Python into
  R)
+ [Matplotlib](https://matplotlib.org/) - Make publication-quality plots

#### Spatial

+ [GeoPandas](http://geopandas.org/) - Adds geodataframes for GIS-style work
+ pyproj - coordinate system transformations (wrapper to Proj4)
+ fiona - read / write GIS vector data (wrapper to OGR)
+ shapely - geometric operations for GIS vector data (wrapper to GEOS)
+ cartopy - plot spatial data in different map projections (similar to GMT)
+ iris - read / write / plot 4D gridded data (NetCDF, GRIB etc)
+ [arcpy](http://pro.arcgis.com/en/pro-app/arcpy/get-started/what-is-arcpy-.htm) - ESRI specific functions to handle and take advantage of ESRI constructs

#### Databases

+ SQLAlchemy - Deal with databases as Python objects in backend-agnostic way
+ [sqlacodegen](https://github.com/agronholm/sqlacodegen) - Automatically generate models from existing database
+ [eralchemy](https://github.com/Alexis-benoist/eralchemy) - Automatically generate entity-relation diagrams from existing database

#### Machine learning / Artificial intelligence

+ [scikit-learn](https://scikit-learn.org/stable/) - various algorithms for implementing a range of ML/AI techniques

#### Image processing

+ [scikit-image](https://scikit-image.org/) - various algorithms for image processing

#### Web services

+ falcon - lightweight web framework for creating HTTP APIs

## Past meetings

#### Keyworth

Date | Attendance | Notes
---- | ----------- | -----
2018-12-04 | 20+ | Overview of interest levels
2019-01-15 | 12  | [Anaconda](./keyworth_materials/anaconda_intro.pdf)
2019-01-29 | 10  | [Pandas (Python notebook provided)](./keyworth_materials)


#### Lyell Centre

Date | Informatics | Scientists | Heriot Watt | Notes
---- | ----------- | ---------- | ----------- | -----
2018-08-28 | 5 | 1 | 0 | Overview of interest levels
2018-09-11 | 3 | 0 | 0 | Interactive plots with Plotly and Bokeh
2018-09-25 | 7 | 5 | 0 | Good split into multiple groups
2018-10-10 | 4 | 6 | 0 | Debugger and logging levels
2018-10-23 | 2 | 7 | 0 | [Easily convert coordinate systems with Pyproj](http://all-geo.org/volcan01010/2012/11/change-coordinates-with-pyproj/)
2018-11-07 | 4 | 4 | 0 | Exception handling
2018-11-20 | 5 | 4 | 0 | Virtual environments
2018-12-05 | 5 | 4 | 0 | Testing with pytest and downloading PDFs
2018-12-17 | 4 | 0 | 0 | Advent of Code dojo
2019-01-15 | 5 | 0 | 2 | Datetime, __file__ variable, installation
2019-02-13 | ? | ? | ? | 
2019-02-26 | 4 | 0 | 1 | String methods, find replace and regular expressions
2019-03-13 | 3 | 1 | 2 | Looping [Notebook provided](./edinburgh_materials)
2019-03-26 | 5 | 1 | 2 | Splitting time series files [hawaii_co2](./edinburgh_materials/hawaii_co2.md)
2019-04-10 | 2 | 1 | 1 | Chatted with Romesh about weathering in borehole records, decided it may be a ML problem. Advised HW person about GNU Octave as a post-student MATLAB alternative
2019-04-30 | 5 | 0 | 1 | Reproducing official plot in
[hawaii_co2](./edinburgh_materials/hawaii_co2.md)
2019-05-28 | 5 | 1 | 0 | flake8, pylint and git pre-commit hooks
2019-06-12 | 2 | 2 | 1 | pytesting console input, geopandas to generate fracture heatmaps

## Notes

#### Working with Jupyter notebooks

A walk through using Anaconda is provided [here](./keyworth_materials/open_a_jupyter_notebook.pdf)

#### 2018-10-23 Pyproj code

Cleaned up IPython code history from coordinate conversion problem:

```python
import pyproj

def to_alaska5(x, y):
    """
    Takes input in Alaska 4 (values in FEET!!!) and converts to Alaska 5.
    """
    FEET_TO_METRES = 0.3048006
    alaska4 = pyproj.Proj('+init=EPSG:26734')
    alaska5 = pyproj.Proj('+init=EPSG:26705')
    return pyproj.transform(alaska4, alaska5, x*FEET_TO_METRES, y*FEET_TO_METRES)

to_alaska5(209844.16, 2233473.9)
```

#### 2018-11-07 Exception handling

Cleaned up code to demonstrate catching and handling of exceptions.

```python
import logging
from traceback import TracebackException

# Custom exceptions can have helpful names and may perform extra
# tasks such as logging or raising an error dialog in a GUI application.
class HelpfulZeroException(Exception):
    """A custom exception that writes a log entry when called."""
    logging.exception('Helpful Zero exception raised')

# This code demonstrates an error when you have a file open
try:
    f = open('test.txt', 'w')
    f.write('hello again\n')
    1/0  # BOOM!!!
    f.write('and again')  # this line will never be called
    
except ZeroDivisionError as err:
    # Catch the error and extract useful stack trace information
    tb_exception = TracebackException.from_exception(err)
    bad_line = tb_exception.stack[-1].lineno
    
    # Create a new error with more helpful information
    # The program will terminate here
    msg = f"Tried to divide by zero on line {bad_line}"
    raise HelpfulZeroException(msg) from err

finally:
    # This line is always called, whether an error was raised or not
    # In this case it makes sure that the file is always closed.
    f.close()

logging.debug('Successfully wrote lines to file')
```

Note that this a contrived example and that it is best to use [context managers](https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/) to make sure that files are closed when you are finished with them.


#### 2018-12-18 Advent of code

The results of the first puzzle (as written tests-first) is in the
[advent_of_code](advent_of_code) directory.


#### 2019-01-15 Datetime overview

The following code was used as a demo of modules, classes and `timedelta`.


```python
import datetime as dt

def my_function():
    print('hello from my function in {}'.format(__file__))
    
class MyClass(object):
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = dt.datetime.strptime(date_of_birth, '%Y-%m-%d')
    
    def show_info(self):
        print('{} was born on {}'.format(self.name, self.date_of_birth))
    
    def show_age(self):
        age = dt.datetime.now() - self.date_of_birth
        age_years = age.days / 365
        print('{} is {:.1f} years old'.format(self.name, age_years))
```

### 2019-02-26 String methods, find replace and regular expressions

All string objects have useful methods built-in.

```python
message = "Hello world"
type(message)
dir(message)
message.upper()
message.lower()
message_caps = message.upper()
message.split()
message.startswith('H')
message.lower().startswith('h')
```

Simple find and replace:

```python
message.find('World')
message.replace('world', 'Charlie')
```

Regular expressions can match text patterns, but can be tricky to use.
Pythex website helps test them.
Regular expressions can also do search and replace.

Links:

+ https://xkcd.com/1171/
+ https://pythex.org/
+ https://docs.python.org/3/library/re.html

Contact data example:

```python
contacts = """A Geologist, 0131 650 0260, ageol@bgs.ac.uk, EH14 4AP
S Developer, 0131 650 5432, sdev@bgs.ac.uk, M1 1AA
T ypoMess, 01316506666, T.Mess@bgs.ac.uk, sw1x 4qq"""
print(contacts)
```

Try to match phone numbers, email addresses and postcodes.

Pythex examples:

+ [Match postcodes](https://pythex.org/?regex=(%5Ba-zA-Z%5D%7B1%2C2%7D%5Cd%7B1%2C2%7D%5Ba-zA-Z%5D%3F%20%5Cd%7B1%2C2%7D%5Ba-zA-Z%5D%7B2%7D)&test_string=A%20Geologist%2C%200131%20650%200260%2C%20ageol%40bgs.ac.uk%2C%20EH14%204AP%0AS%20Developer%2C%200131%20650%205432%2C%20sdev%40bgs.ac.uk%2C%20M1%201AA%0AT%20ypoMess%2C%2001316506666%2C%20T.Mess%40bgs.ac.uk%2C%20sw1x%204qq&ignorecase=0&multiline=0&dotall=0&verbose=0)
+ [Named groups](https://pythex.org/?regex=(%3FP%3Cphone%3E%5Cd%7B4%7D%20%3F%5Cd%7B3%7D%20%3F%5Cd%7B4%7D).*(%3FP%3Cpostcode%3E%5Ba-zA-Z%5D%7B1%2C2%7D%5Cd%7B1%2C2%7D%5Ba-zA-Z%5D%3F%20%5Cd%7B1%2C2%7D%5Ba-zA-Z%5D%7B2%7D)&test_string=A%20Geologist%2C%200131%20650%200260%2C%20ageol%40bgs.ac.uk%2C%20EH14%204AP%0AS%20Developer%2C%200131%20650%205432%2C%20sdev%40bgs.ac.uk%2C%20M1%201AA%0AT%20ypoMess%2C%2001316506666%2C%20T.Mess%40bgs.ac.uk%2C%20sw1x%204qq&ignorecase=0&multiline=0&dotall=0&verbose=0)

Python returns matched data as groups:

```python
import re
match = re.search(r'(\d{4} ?\d{3} ?\d{4})')
match.groups()
```

Regular expressions can be used for find and replace, e.g. replace all phone
numbers with the switchboard.

```python
re.sub(r'\d{4} ?\d{3} ?\d{4}', '0131 650 1000', contacts)
```

### 2019-04-03: Hawaii plotting

Attempt to reproduce official Hawaii CO2 plot with Pandas and Matplotlib.  See
partial solution at [./edinburgh_materials/hawaii-plot.py](./edinburgh_materials/hawaii-plot.py).
