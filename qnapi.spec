#
# spec file for package qnapi
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

%global    debug_package %{nil}

Name:           qnapi
Version:        0.2.3
Release:        1
Summary:        A NapiProjekt client
Summary(pl):    Klient NapiProjekt
License:        GPLv2+
Group:          Networking/File transfer
Url:            http://qnapi.github.io/
Source0:        https://github.com/QNapi/qnapi/releases/download/%{version}/%{name}-%{version}.tar.gz
#BuildRequires:  fdupes
BuildRequires:  qmake5
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(libmediainfo) >= 18.03
Requires:       p7zip

%description
QNapi is similar app like NapiProjekt program (http://napiprojekt.pl)
written using Qt5. It's focused to be functional on GNU/Linux and other
Unix-like systems, for which NapiProjekt is not available.

%description -l pl
QNapi jest nieoficjalnym klonem programu NapiProjekt (http://napiprojekt.pl)
napisanym w bibliotece Qt5 z myślą o użytkownikach Linuksa oraz innych
systemów, pod które oryginalny NapiProjekt nie jest dostępny.

%prep
%setup -q
### Fix paths specific for openSUSE
#sed -i 's|doc.path = $${INSTALL_PREFIX}/share/doc/$${TARGET}|doc.path = $${INSTALL_PREFIX}/share/doc/packages/$${TARGET}|' qnapi.pro

%build
%{_qt5_qmake}
%make_build QMAKE=%{_qt5_qmake} PREFIX=%{_prefix}
#qmake5
#make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install %{?_smp_mflags}
# Add service menu
install -m 644 -D doc/qnapi-download.desktop %{buildroot}%{_datadir}/kde4/services/ServiceMenus/qnapi-download.desktop
install -m 644 -D doc/qnapi-scan.desktop %{buildroot}%{_datadir}/kde4/services/ServiceMenus/qnapi-scan.desktop

## Fix for "wrong-file-end-of-line-encoding" doc/ChangeLog file
sed -i 's/\r//' doc/ChangeLog

#fdupes %{buildroot}%{_prefix}
#suse_update_desktop_file -i -r -n %{name} AudioVideo AudioVideoEditing

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/icons/*
%{_datadir}/applications/%{name}.desktop
%attr(644,root,root) %{_mandir}/man1/*
%attr(644,root,root) %{_mandir}/*/man1/*
%dir %{_datadir}/kde4
%dir %{_datadir}/kde4/services
%dir %{_datadir}/kde4/services/ServiceMenus
%{_datadir}/kde4/services/ServiceMenus/qnapi-download.desktop
%{_datadir}/kde4/services/ServiceMenus/qnapi-scan.desktop
%{_docdir}/%{name}
