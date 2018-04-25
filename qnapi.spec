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
%setup -qn %{name}-%{version}

%build
export QTDIR=%{_libdir}/qt5
export CFLAGS=-I%{_libdir}/qt5/include
export CXXFLAGS=${CFLAGS}
%qmake_qt5
%make_build

%install
%qmakeinstall_std
%__install -Dm644 doc/qnapi-download.desktop %{buildroot}%{_kf5_services}/ServiceMenus/qnapi-download.desktop
%__install -m644 doc/qnapi-scan.desktop %{buildroot}%{_kf5_services}/ServiceMenus/qnapi-scan.desktop
%__rm -rf %{buildroot}%{_docdir}/%{name}

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="AudioVideo" \
  --remove-category="Player" \
  --add-category="X-MandrivaLinux-Multimedia-Video" \
  --dir %{buildroot}%{_desktopdir} %{buildroot}%{_desktopdir}/qnapi.desktop

%files
%defattr(-,root,root)
%doc README.md doc/{ChangeLog,COPYRIGHT,LICENSE,LICENSE-pl}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%dir %{_kf5_services}/ServiceMenus
%{_kf5_services}/ServiceMenus/qnapi-*.desktop
%{_mandir}/*
