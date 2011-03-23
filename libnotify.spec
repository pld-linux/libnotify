#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	static_libs	# don't build static library
#
Summary:	Desktop notifications library
Summary(hu.UTF-8):	Desktop értesítő könyvtár
Summary(pl.UTF-8):	Biblioteka powiadomień dla pulpitu
Name:		libnotify
Version:	0.7.2
Release:	1
License:	LGPL v2.1+ (library), GPL v2+ (tools)
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libnotify/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	8577870326faed1b6a4e1a6043cbeffa
URL:		http://www.galago-project.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.10
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gobject-introspection-devel >= 0.9.12
BuildRequires:	gtk+3-devel >= 2.91.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.14}
BuildRequires:	gtk-doc-automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
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
Requires:	gdk-pixbuf2-devel
Requires:	glib2-devel >= 1:2.26.0

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
	--disable-silent-rules \
	--%{?with_apidocs:en}%{!?with_apidocs:dis}able-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{!?with_apidocs:%{__rm} -rf $RPM_BUILD_ROOT%{_gtkdocdir}/libnotify}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/notify-send
%attr(755,root,root) %{_libdir}/libnotify.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnotify.so.4
%{_libdir}/girepository-1.0/Notify-0.7.typelib

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnotify.so
%{_pkgconfigdir}/libnotify.pc
%{_includedir}/libnotify
%{_datadir}/gir-1.0/Notify-0.7.gir

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libnotify.a
%endif
