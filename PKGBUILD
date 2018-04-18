# Script generated with Bloom
pkgdesc="ROS - Conversion functions between: - Eigen and KDL - Eigen and geometry_msgs."
url='http://ros.org/wiki/eigen_conversions'

pkgname='ros-lunar-eigen-conversions'
pkgver='1.11.9_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('eigen3'
'ros-lunar-catkin'
'ros-lunar-cmake-modules'
'ros-lunar-geometry-msgs'
'ros-lunar-orocos-kdl'
'ros-lunar-std-msgs'
)

depends=('eigen3'
'ros-lunar-geometry-msgs'
'ros-lunar-orocos-kdl'
'ros-lunar-std-msgs'
)

conflicts=()
replaces=()

_dir=eigen_conversions
source=()
md5sums=()

prepare() {
    cp -R $startdir/eigen_conversions $srcdir/eigen_conversions
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
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

