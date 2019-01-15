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


#### Lyell Centre

Date | Informatics | Scientists | Notes
---- | ----------- | ---------- | -----
2018-08-28 | 5 | 1 | Overview of interest levels
2018-09-11 | 3 | 0 | Interactive plots with Plotly and Bokeh
2018-09-25 | 7 | 5 | Good split into multiple groups
2018-10-10 | 4 | 6 | Debugger and logging levels
2018-10-23 | 2 | 7 | [Easily convert coordinate systems with Pyproj](http://all-geo.org/volcan01010/2012/11/change-coordinates-with-pyproj/)
2018-11-07 | 4 | 4 | Exception handling
2018-11-20 | 5 | 4 | Virtual environments
2018-12-05 | 5 | 4 | Testing with pytest and downloading PDFs
2018-12-17 | 4 | 0 | Advent of Code dojo

## Notes

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
