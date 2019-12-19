Name: acestream-launcher
Version: 2.0.1
Release: 2%{?dist}
Summary: Ace Stream Launcher
License: GPLv3
Group: Productivity/Multimedia/Other
URL: https://github.com/jonian/%{name}
Source: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1: acestream-launcher.patch
BuildArch: noarch
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: fdupes
#!BuildIgnore: acestream-engine
Requires: curl python3 python3-acestream acestream-engine mpv

%description
Acestream Launcher allows you to open Acestream links with a Media Player of your choice.

%prep
%setup -q
%patch1 -p1

%build
%py3_build

%install
%py3_install

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/%{name}
%{python3_sitelib}/*
%{_datadir}/applications/%{name}.desktop

%changelog
* Mon Dec 16 2019 Sérgio Basto <sergio@serjux.com> - 2.0.1-2
- custom patch

