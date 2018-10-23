# Python Clinic

Resources linked to the Lyell Centre Python clinics

## Handy links

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


## Past meetings

Date | Informatics | Scientists | Notes
---- | ----------- | ---------- | -----
2018-08-28 | 5 | 1 | Overview of interest levels
2018-09-11 | 3 | 0 | Interactive plots with Plotly and Bokeh
2018-09-25 | 7 | 5 | Good split into multiple groups
2018-10-10 | 4 | 6 | Debugger and logging levels
2018-10-23 | 2 | 7 | [Easily convert coordinate systems with Pyproj](http://all-geo.org/volcan01010/2012/11/change-coordinates-with-pyproj/)

## Notes

#### 2018-10-23 Pyproj code

Cleaned up IPython code history from coordinate conversion problem:

```python
import pyproj
alaska4 = pyproj.Proj('+init=EPSG:26734')
alaska5 = pyproj.Proj('+init=EPSG:26705')

def to_alaska5(x, y):
    """
    Takes input in Alaska 4 (values in FEET!!!) and converts to Alaska 5.
    """
    FEET_TO_METRES = 0.3048006
    return pyproj.transform(alaska4, alaska5, x*FEET_TO_METRES, y*FEET_TO_METRES)

to_alaska5(209844.16, 2233473.9)
```
