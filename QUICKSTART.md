
## Centos 7

Comes with 2.7 by default and does not distribute 3.6 in core packages so you need EPEL.

  * sudo yum install python3
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

If you get an error about not finding the kernel-headers package, make sure you have a recent-ish kernel, run

  * sudo yum update



