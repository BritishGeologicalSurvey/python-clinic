# Windows

Anaconda recommended

GIS Dependencies

### Shapely / pyproj

If you use Anaconda you should get a binary wheel and not need the C libraries.

If installing with a system python you need OSGeo4W libraries in your PATH at installation time. 

(The shapely docs point you at GEOS_LIBRARY_PATH but it's not enough by itself.

  * Install OSGeo4W - download from here, do full Desktop install https://trac.osgeo.org/osgeo4w/

  * $Env:PATH="$Env:PATH;C:\OSGeo4W64\bin\"

  * C:\Python36\Scripts\pip.exe install shapely


# Centos 7

Comes with 2.7 by default and does not distribute 3.6 in core packages so you need EPEL.

  * sudo yum install python36 python36-devel
  * /usr/bin/python36 -m venv env

Then add the following to .bashrc or .zshrc
  * source ./env/bin/activate

Be aware there is an RH graphical installer package also called anaconda

## Build tools 

(For C/C++ based dependencies)

Centos has no moral equivalent of debian/Ubuntu build-essential package but this is recommended:

  * sudo yum groupinstall 'Development Tools'

If you get an error about kernel-headers then

  * sudo yum install kernel-headers

If you get an error about not finding the kernel-headers package, worth checking the last line of `/etc/yum.conf` to make sure that `kernel*` packages are not being excluded, and also

  * sudo yum update

## GIS dependencies

  * TBC
