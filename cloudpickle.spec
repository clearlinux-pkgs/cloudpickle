#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cloudpickle
Version  : 1.6.0
Release  : 42
URL      : https://github.com/cloudpipe/cloudpickle/archive/v1.6.0/cloudpickle-1.6.0.tar.gz
Source0  : https://github.com/cloudpipe/cloudpickle/archive/v1.6.0/cloudpickle-1.6.0.tar.gz
Summary  : Extended pickling support for Python objects
Group    : Development/Tools
License  : BSD-3-Clause
Requires: cloudpickle-license = %{version}-%{release}
Requires: cloudpickle-python = %{version}-%{release}
Requires: cloudpickle-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
# cloudpickle
[![Automated Tests](https://github.com/cloudpipe/cloudpickle/workflows/Automated%20Tests/badge.svg?branch=master&event=push)](https://github.com/cloudpipe/cloudpickle/actions)
[![codecov.io](https://codecov.io/github/cloudpipe/cloudpickle/coverage.svg?branch=master)](https://codecov.io/github/cloudpipe/cloudpickle?branch=master)

%package license
Summary: license components for the cloudpickle package.
Group: Default

%description license
license components for the cloudpickle package.


%package python
Summary: python components for the cloudpickle package.
Group: Default
Requires: cloudpickle-python3 = %{version}-%{release}

%description python
python components for the cloudpickle package.


%package python3
Summary: python3 components for the cloudpickle package.
Group: Default
Requires: python3-core
Provides: pypi(cloudpickle)

%description python3
python3 components for the cloudpickle package.


%prep
%setup -q -n cloudpickle-1.6.0
cd %{_builddir}/cloudpickle-1.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1598634870
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cloudpickle
cp %{_builddir}/cloudpickle-1.6.0/LICENSE %{buildroot}/usr/share/package-licenses/cloudpickle/1714ccb2a2ccbaa4fdd69680f0406848451a7f41
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cloudpickle/1714ccb2a2ccbaa4fdd69680f0406848451a7f41

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
