# Script generated with Bloom
pkgdesc="ROS - This package contains a set of conversion functions to convert common tf datatypes (point, vector, pose, etc) into semantically identical datatypes used by other libraries. The conversion functions make it easier for users of the transform library (tf) to work with the datatype of their choice. Currently this package has support for the Kinematics and Dynamics Library (KDL) and the Eigen matrix library. This package is stable, and will get integrated into tf in the next major release cycle (see roadmap)."
url='http://www.ros.org/wiki/tf_conversions'

pkgname='ros-melodic-tf-conversions'
pkgver='1.11.9_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('eigen3'
'ros-melodic-catkin>=0.5.68'
'ros-melodic-cmake-modules'
'ros-melodic-geometry-msgs'
'ros-melodic-kdl-conversions'
'ros-melodic-orocos-kdl'
'ros-melodic-tf'
)

depends=('eigen3'
'ros-melodic-geometry-msgs'
'ros-melodic-kdl-conversions'
'ros-melodic-orocos-kdl'
'ros-melodic-python-orocos-kdl'
'ros-melodic-tf'
)

conflicts=()
replaces=()

_dir=tf_conversions
source=()
md5sums=()

prepare() {
    cp -R $startdir/tf_conversions $srcdir/tf_conversions
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/melodic/setup.bash ] && source /opt/ros/melodic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/melodic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

