Name: acestream-launcher
Version: 2.1.0
Release: 1%{?dist}
Summary: Ace Stream Launcher
License: GPLv3
Group: Productivity/Multimedia/Other
URL: https://github.com/jonian/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: acelive.xml
Patch1: acestream-launcher.patch
BuildArch: noarch
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python3-rpm-macros
#!BuildIgnore: acestream-engine
Requires: curl
Requires: python3
Requires: python3-acestream
Requires: acestream-engine
Requires: mpv

%description
Acestream Launcher allows you to open Acestream links with a Media Player of your choice.

%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install

install -d %{buildroot}%{_datadir}/mime/packages
install -p -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/mime/packages/

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/%{name}
%{python3_sitelib}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/acelive.xml

%changelog
* Tue Aug 10 2021 Sérgio Basto <sergio@serjux.com> - 2.1.0-1
- Update to 2.1.0

* Tue Feb 16 2021 Sérgio Basto <sergio@serjux.com> - 2.0.3-1
- Update to 2.0.3


* Fri Aug 07 2020 Alessandro Astone <ales.astone AT gmail DOT com> - 2.0.1-6
- Don't hard code gnome-terminal

* Thu Jul 02 2020 Sérgio Basto <sergio@serjux.com> - 2.0.1-5
- Register mime type for .acelive files

* Mon Jun 29 2020 Sérgio Basto <sergio@serjux.com> - 2.0.1-4
- Add support for file:// .acelive and .torrent urls

* Sat Jun 06 2020 Sérgio Basto <sergio@serjux.com> - 2.0.1-3
- acestreamengine --client-gtk doesn't work anymore because we don't have
  python2-appindicator, moving to default

* Mon Dec 16 2019 Sérgio Basto <sergio@serjux.com> - 2.0.1-2
- custom patch

