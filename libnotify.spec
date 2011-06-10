#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	static_libs	# don't build static library
#
Summary:	Desktop notifications library
Summary(hu.UTF-8):	Desktop értesítő könyvtár
Summary(pl.UTF-8):	Biblioteka powiadomień dla pulpitu
Name:		libnotify
Version:	0.4.5
Release:	6
License:	LGPL v2.1+ (library), GPL v2+ (tools)
Group:		Libraries
Source0:	http://www.galago-project.org/files/releases/source/libnotify/%{name}-%{version}.tar.bz2
# Source0-md5:	6a8388f93309dbe336bbe5fc0677de6b
URL:		http://www.galago-project.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.12.1
BuildRequires:	gtk+2-devel >= 2:2.10.1
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.7}
BuildRequires:	gtk-doc-automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	dbus-glib >= 0.71
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library that sends desktop notifications to a notification daemon,
as defined in the Desktop Notifications spec. These notifications can
be used to inform the user about an event or display some form of
information without getting in the user's way.

%description  -l hu.UTF-8
Könyvtár, amely értesítéseket küld egy üzenetkezelő démonnak, ahogy a
Desktop Notifications szabványnak megfelel. Ezek az értesítések
tájékoztathatják a felhasználót eseményről vagy információt jeleníthet
meg.

%description -l pl.UTF-8
Biblioteka wysyłająca powiadomienia dla pulpitu do demona powiadomień
zgodnie ze specyfikacją Desktop Notifications. Powiadomienia te mogą
być używane do informowania użytkownika o zdarzeniu lub wyświetlania
jakiejś formy informacji bez wchodzenia użytkownikowi w drogę.

%package apidocs
Summary:	libnotify API documentation
Summary(hu.UTF-8):	libnotify API dokumentáció
Summary(pl.UTF-8):	Dokumentacja API biblioteki libnotify
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libnotify API documentation.

%description apidocs -l hu.UTF-8
libnotify API dokumentáció.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libnotify.

%package devel
Summary:	libnotify header files
Summary(hu.UTF-8):	libnotify fejléc fájlok
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libnotify
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib-devel >= 0.71
Requires:	glib2-devel >= 1:2.12.1
Requires:	gtk+2-devel >= 2:2.10.1

%description devel
Header files for libnotify-based programs development.

%description devel -l hu.UTF-8
Fejléc fájlok libnotify-t használó programok fejlesztéséhez.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia programów opartych o libnotify.

%package static
Summary:	Static libnotify library
Summary(hu.UTF-8):	Libnotify statikus könyvtár
Summary(pl.UTF-8):	Statyczna biblioteka libnotify
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnotify library.

%description static -l hu.UTF-8
Libnotify statikus könyvtár.

%description static -l pl.UTF-8
Statyczna biblioteka libnotify.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--%{?with_apidocs:en}%{!?with_apidocs:dis}able-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}/libnotify}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/lib*.so.1

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*
%{_includedir}/*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
