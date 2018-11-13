
## Centos 7

Comes with 2.7 by default and does not distribute 3.6 in core packages so you need EPEL.

  * sudo yum install python36 python36-devel
  * /usr/bin/python36 -m venv env

Then add the following to .bashrc or .zshrc
  * source ./env/bin/activate

Be aware there is an RH graphical installer package also called anaconda

### Build tools 

(For C/C++ based dependencies)

Centos has no moral equivalent of debian/Ubuntu build-essential package but this is recommended:

  * sudo yum groupinstall 'Development Tools'

If you get an error about kernel-headers then

  * sudo yum install kernel-headers

If you get an error about not finding the kernel-headers package, worth checking the last line of `/etc/yum.conf` to make sure that `kernel*` packages are not being excluded, and also

  * sudo yum update



