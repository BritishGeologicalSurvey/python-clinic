# Get Started Python 

## TL;DR

  * Use version 3.6 or higher where possible
  * Anaconda makes life easier
  * `pip install -r requirements.txt`

## Python Versions

_Short version: Python 2.x is legacy, Python 3.x is the present and future of the language_

  * Use at least 3.6 for all new development
  * Some projects (ArcPy, ansible) still require 2.7

### Virtual Environment

Easy way to manage python installation and dependencies by using `a virtual environment, a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.`

  * Standard python: [venv](https://docs.python.org/3/tutorial/venv.html)
  * `python -m venv env; . ./env/bin/activate`

  * Anaconda has its own [conda env](https://conda.io/docs/user-guide/tasks/manage-environments.html)
  * `conda create --name env; . activate myenv`

## Dependencies

  * `requirements.txt` lists third-party dependencies for a project with minimum versions

With pip:

  * `pip install -r requirements.txt`

With conda:
  * `conda install -f requirements.txt`

### C / C++ dependencies

Some python packages depend on having C/C++ sources to link to at build time. Often they will distribute "binary wheels" with the dependencies pre-compiled.   


# Platform-specific installation hints

## Windows

Anaconda is recommended. The Windows download provides the Spyder IDE.

  * https://www.anaconda.com/download/

### GIS Dependencies

#### Shapely / pyproj

If you use Anaconda you should get a binary wheel and not need the C libraries.

If installing with a system python you need OSGeo4W libraries in your PATH at installation time. 

(The shapely docs point you at GEOS_LIBRARY_PATH at install time but in practise you also need PATH set at run time.

  * Install OSGeo4W - download from here, do full Desktop install https://trac.osgeo.org/osgeo4w/

  * $Env:PATH="$Env:PATH;C:\OSGeo4W64\bin\"

  * C:\Python36\Scripts\pip.exe install shapely

  
## Centos 7

Comes with 2.7 by default and does not distribute 3.6 in core packages so you need EPEL.

  * sudo yum install python36 python36-devel
  * /usr/bin/python36 -m venv env

Then add the following to .bashrc or .zshrc
  * source ~/env/bin/activate

Be aware there is an RH graphical installer package also called anaconda

### Build tools 

(For C/C++ based dependencies)

Centos has no moral equivalent of debian/Ubuntu build-essential package but this is recommended:

  * sudo yum groupinstall 'Development Tools'

If you get an error about kernel-headers then

  * sudo yum install kernel-headers

If you get an error about not finding the kernel-headers package, worth checking the last line of `/etc/yum.conf` to make sure that `kernel*` packages are not being excluded, and also

  * sudo yum update



