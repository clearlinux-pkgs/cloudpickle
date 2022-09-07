#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cloudpickle
Version  : 2.2.0
Release  : 57
URL      : https://github.com/cloudpipe/cloudpickle/archive/v2.2.0/cloudpickle-2.2.0.tar.gz
Source0  : https://github.com/cloudpipe/cloudpickle/archive/v2.2.0/cloudpickle-2.2.0.tar.gz
Summary  : Extended pickling support for Python objects
Group    : Development/Tools
License  : BSD-3-Clause
Requires: cloudpickle-license = %{version}-%{release}
Requires: cloudpickle-python = %{version}-%{release}
Requires: cloudpickle-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

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
%setup -q -n cloudpickle-2.2.0
cd %{_builddir}/cloudpickle-2.2.0
pushd ..
cp -a cloudpickle-2.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1662595015
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cloudpickle
cp %{_builddir}/cloudpickle-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/cloudpickle/1714ccb2a2ccbaa4fdd69680f0406848451a7f41 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
