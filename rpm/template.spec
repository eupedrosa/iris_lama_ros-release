%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-iris-lama-ros
Version:        1.1.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS iris_lama_ros package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-iris-lama
Requires:       ros-noetic-message-filters
Requires:       ros-noetic-nav-msgs
Requires:       ros-noetic-rosbag
Requires:       ros-noetic-rosbag-storage
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-std-srvs
Requires:       ros-noetic-tf
Requires:       ros-noetic-tf-conversions
Requires:       ros-noetic-visualization-msgs
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-iris-lama
BuildRequires:  ros-noetic-message-filters
BuildRequires:  ros-noetic-nav-msgs
BuildRequires:  ros-noetic-rosbag
BuildRequires:  ros-noetic-rosbag-storage
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-std-srvs
BuildRequires:  ros-noetic-tf
BuildRequires:  ros-noetic-tf-conversions
BuildRequires:  ros-noetic-visualization-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
ROS package of IRIS Localization and Mapping (LaMa).

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Wed Dec 16 2020 Eurico Pedrosa <efp@ua.pt> - 1.1.0-1
- Autogenerated by Bloom

