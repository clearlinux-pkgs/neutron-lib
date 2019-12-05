#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : neutron-lib
Version  : 1.29.1
Release  : 32
URL      : https://files.pythonhosted.org/packages/b9/04/4ff9f6ea20af12c65e53ab5ad39124647d7194b6e96817c051732f8ee9dc/neutron-lib-1.29.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/b9/04/4ff9f6ea20af12c65e53ab5ad39124647d7194b6e96817c051732f8ee9dc/neutron-lib-1.29.1.tar.gz
Summary  : Neutron shared routines and utilities
Group    : Development/Tools
License  : Apache-2.0
Requires: neutron-lib-license = %{version}-%{release}
Requires: neutron-lib-python = %{version}-%{release}
Requires: neutron-lib-python3 = %{version}-%{release}
Requires: SQLAlchemy
Requires: WebOb
Requires: keystoneauth1
Requires: netaddr
Requires: os-ken
Requires: os-traits
Requires: oslo.concurrency
Requires: oslo.config
Requires: oslo.context
Requires: oslo.db
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.messaging
Requires: oslo.policy
Requires: oslo.serialization
Requires: oslo.service
Requires: oslo.utils
Requires: oslo.versionedobjects
Requires: osprofiler
Requires: pbr
Requires: pecan
Requires: setproctitle
Requires: six
Requires: stevedore
Requires: weakrefmethod
BuildRequires : SQLAlchemy
BuildRequires : WebOb
BuildRequires : buildreq-distutils3
BuildRequires : keystoneauth1
BuildRequires : netaddr
BuildRequires : os-ken
BuildRequires : os-traits
BuildRequires : oslo.concurrency
BuildRequires : oslo.config
BuildRequires : oslo.context
BuildRequires : oslo.db
BuildRequires : oslo.i18n
BuildRequires : oslo.log
BuildRequires : oslo.messaging
BuildRequires : oslo.policy
BuildRequires : oslo.serialization
BuildRequires : oslo.service
BuildRequires : oslo.utils
BuildRequires : oslo.versionedobjects
BuildRequires : osprofiler
BuildRequires : pbr
BuildRequires : pecan
BuildRequires : setproctitle
BuildRequires : six
BuildRequires : stevedore
BuildRequires : weakrefmethod

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/neutron-lib.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

%package license
Summary: license components for the neutron-lib package.
Group: Default

%description license
license components for the neutron-lib package.


%package python
Summary: python components for the neutron-lib package.
Group: Default
Requires: neutron-lib-python3 = %{version}-%{release}

%description python
python components for the neutron-lib package.


%package python3
Summary: python3 components for the neutron-lib package.
Group: Default
Requires: python3-core

%description python3
python3 components for the neutron-lib package.


%prep
%setup -q -n neutron-lib-1.29.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567783232
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/neutron-lib
cp LICENSE %{buildroot}/usr/share/package-licenses/neutron-lib/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/neutron-lib/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
