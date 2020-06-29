Name: acestream-launcher
Version: 2.0.1
Release: 4%{?dist}
Summary: Ace Stream Launcher
License: GPLv3
Group: Productivity/Multimedia/Other
URL: https://github.com/jonian/%{name}
Source: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: v2.0.1...ce1c637c0bae7687b84a4f11a5cfc696766df394.diff
Patch1: acestream-launcher.patch
BuildArch: noarch
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python3-rpm-macros
BuildRequires: fdupes
#!BuildIgnore: acestream-engine
Requires: curl python3 python3-acestream acestream-engine mpv

%description
Acestream Launcher allows you to open Acestream links with a Media Player of your choice.

%prep
%autosetup -p1

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
* Mon Jun 29 2020 Sérgio Basto <sergio@serjux.com> - 2.0.1-4
- Add support for file:// .acelive and .torrent urls

* Sat Jun 06 2020 Sérgio Basto <sergio@serjux.com> - 2.0.1-3
- acestreamengine --client-gtk doesn't work anymore because we don't have
  python2-appindicator, moving to default

* Mon Dec 16 2019 Sérgio Basto <sergio@serjux.com> - 2.0.1-2
- custom patch

