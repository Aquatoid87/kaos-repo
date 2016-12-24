################################################################################

%global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(0)")

################################################################################

%define _posixroot        /
%define _root             /root
%define _bin              /bin
%define _sbin             /sbin
%define _srv              /srv
%define _home             /home
%define _lib32            %{_posixroot}lib
%define _lib64            %{_posixroot}lib64
%define _libdir32         %{_prefix}%{_lib32}
%define _libdir64         %{_prefix}%{_lib64}
%define _logdir           %{_localstatedir}/log
%define _rundir           %{_localstatedir}/run
%define _lockdir          %{_localstatedir}/lock/subsys
%define _cachedir         %{_localstatedir}/cache
%define _spooldir         %{_localstatedir}/spool
%define _crondir          %{_sysconfdir}/cron.d
%define _loc_prefix       %{_prefix}/local
%define _loc_exec_prefix  %{_loc_prefix}
%define _loc_bindir       %{_loc_exec_prefix}/bin
%define _loc_libdir       %{_loc_exec_prefix}/%{_lib}
%define _loc_libdir32     %{_loc_exec_prefix}/%{_lib32}
%define _loc_libdir64     %{_loc_exec_prefix}/%{_lib64}
%define _loc_libexecdir   %{_loc_exec_prefix}/libexec
%define _loc_sbindir      %{_loc_exec_prefix}/sbin
%define _loc_bindir       %{_loc_exec_prefix}/bin
%define _loc_datarootdir  %{_loc_prefix}/share
%define _loc_includedir   %{_loc_prefix}/include
%define _loc_mandir       %{_loc_datarootdir}/man
%define _rpmstatedir      %{_sharedstatedir}/rpm-state
%define _pkgconfigdir     %{_libdir}/pkgconfig

################################################################################

%global pkgname           enchant
%define pypi_subpath      73/73/49f95fe636ab3deed0ef1e3b9087902413bcdf74ec00298c3059e660cfbb

################################################################################

Summary:            Python bindings for Enchant spellchecking library
Name:               python-%{pkgname}
Version:            1.6.8
Release:            0%{?dist}
License:            LGPLv2+
Group:              Development/Languages
URL:                http://packages.python.org/pyenchant/

Source0:            https://pypi.python.org/packages/%{pypi_subpath}/py%{pkgname}-%{version}.tar.gz

BuildRoot:          %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:          noarch

BuildRequires:      python-setuptools python-devel enchant-devel

Provides:           PyEnchant = %{version}-%{release}

################################################################################

%description
PyEnchant is a spellchecking library for Python, based on the Enchant
library by Dom Lachowicz.

################################################################################

%prep
%setup -qn pyenchant-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf %{buildroot}

%{__python} setup.py install -O1 --skip-build --root %{buildroot} --single-version-externally-managed

%clean
rm -rf %{buildroot}

################################################################################

%files
%defattr(-,root,root,-)
%doc LICENSE.txt README.txt TODO.txt
%{python_sitelib}/*

################################################################################

%changelog
* Tue Dec 13 2016 Anton Novojilov <andy@essentialkaos.com> - 1.6.8-0
- Initial build for kaos repo