Name:           ros-jade-tf-conversions
Version:        1.11.7
Release:        0%{?dist}
Summary:        ROS tf_conversions package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/tf_conversions
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-kdl-conversions
Requires:       ros-jade-orocos-kdl
Requires:       ros-jade-python-orocos-kdl
Requires:       ros-jade-tf
BuildRequires:  eigen3-devel
BuildRequires:  ros-jade-catkin >= 0.5.68
BuildRequires:  ros-jade-cmake-modules
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-kdl-conversions
BuildRequires:  ros-jade-orocos-kdl
BuildRequires:  ros-jade-tf

%description
This package contains a set of conversion functions to convert common tf
datatypes (point, vector, pose, etc) into semantically identical datatypes used
by other libraries. The conversion functions make it easier for users of the
transform library (tf) to work with the datatype of their choice. Currently this
package has support for the Kinematics and Dynamics Library (KDL) and the Eigen
matrix library. This package is stable, and will get integrated into tf in the
next major release cycle (see roadmap).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Apr 21 2015 Tully Foote <tfoote@osrfoundation.org> - 1.11.7-0
- Autogenerated by Bloom

* Wed Mar 25 2015 Tully Foote <tfoote@osrfoundation.org> - 1.11.6-0
- Autogenerated by Bloom

* Tue Mar 17 2015 Tully Foote <tfoote@osrfoundation.org> - 1.11.5-0
- Autogenerated by Bloom

* Tue Jan 13 2015 Tully Foote <tfoote@osrfoundation.org> - 1.11.4-0
- Autogenerated by Bloom
