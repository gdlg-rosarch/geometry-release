# Script generated with Bloom
pkgdesc="ROS - tf is a package that lets the user keep track of multiple coordinate frames over time. tf maintains the relationship between coordinate frames in a tree structure buffered in time, and lets the user transform points, vectors, etc between any two coordinate frames at any desired point in time. <p><b>Migration</b>: Since ROS Hydro, tf has been &quot;deprecated&quot; in favor of <a href="http://wiki.ros.org/tf2">tf2</a>. tf2 is an iteration on tf providing generally the same feature set more efficiently. As well as adding a few new features.<br/> As tf2 is a major change the tf API has been maintained in its current form. Since tf2 has a superset of the tf features with a subset of the dependencies the tf implementation has been removed and replaced with calls to tf2 under the hood. This will mean that all users will be compatible with tf2. It is recommended for new work to use tf2 directly as it has a cleaner interface. However tf will continue to be supported for through at least J Turtle. </p>"
url='http://www.ros.org/wiki/tf'

pkgname='ros-melodic-tf'
pkgver='1.11.9_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-melodic-angles'
'ros-melodic-catkin>=0.6.4'
'ros-melodic-geometry-msgs'
'ros-melodic-message-filters'
'ros-melodic-message-generation'
'ros-melodic-rosconsole'
'ros-melodic-roscpp'
'ros-melodic-rostest'
'ros-melodic-rostime'
'ros-melodic-rosunit'
'ros-melodic-sensor-msgs'
'ros-melodic-std-msgs'
'ros-melodic-tf2-ros>=0.5.16'
)

depends=('graphviz'
'ros-melodic-geometry-msgs'
'ros-melodic-message-filters>=1.11.1'
'ros-melodic-message-runtime'
'ros-melodic-rosconsole'
'ros-melodic-roscpp'
'ros-melodic-roswtf'
'ros-melodic-sensor-msgs'
'ros-melodic-std-msgs'
'ros-melodic-tf2-ros>=0.5.16'
)

conflicts=()
replaces=()

_dir=tf
source=()
md5sums=()

prepare() {
    cp -R $startdir/tf $srcdir/tf
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

