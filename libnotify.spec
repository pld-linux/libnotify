# TODO: actually run tests (broken after switching to meson)
#
# Conditional build:
%bcond_without	apidocs		# gi-docgen API documentation
%bcond_without	static_libs	# static library
%bcond_without	tests		# tests build

Summary:	Desktop notifications library
Summary(hu.UTF-8):	Desktop értesítő könyvtár
Summary(pl.UTF-8):	Biblioteka powiadomień dla pulpitu
Name:		libnotify
Version:	0.8.6
Release:	1
License:	LGPL v2.1+ (library), GPL v2+ (tools)
Group:		Libraries
Source0:	https://download.gnome.org/sources/libnotify/0.8/%{name}-%{version}.tar.xz
# Source0-md5:	09bce743badbe1c180ce14d92539afb9
URL:		http://developer.gnome.org/notification-spec/
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl-nons
BuildRequires:	gdk-pixbuf2-devel >= 2.0
%{?with_apidocs:BuildRequires:	gi-docgen >= 2021.7}
BuildRequires:	glib2-devel >= 1:2.62.0
BuildRequires:	gobject-introspection-devel >= 0.9.12
%{?with_tests:BuildRequires:	gtk+3-devel >= 3.0.0}
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xmlto
BuildRequires:	xz
Requires:	glib2 >= 1:2.62.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library that sends desktop notifications to a notification daemon,
as defined in the Desktop Notifications spec. These notifications can
be used to inform the user about an event or display some form of
information without getting in the user's way.

%description -l hu.UTF-8
Könyvtár, amely értesítéseket küld egy üzenetkezelő démonnak, ahogy a
Desktop Notifications szabványnak megfelel. Ezek az értesítések
tájékoztathatják a felhasználót eseményről vagy információt jeleníthet
meg.

%description -l pl.UTF-8
Biblioteka wysyłająca powiadomienia dla pulpitu do demona powiadomień
zgodnie ze specyfikacją Desktop Notifications. Powiadomienia te mogą
być używane do informowania użytkownika o zdarzeniu lub wyświetlania
jakiejś formy informacji bez wchodzenia użytkownikowi w drogę.

%package devel
Summary:	libnotify header files
Summary(hu.UTF-8):	libnotify fejléc fájlok
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libnotify
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gdk-pixbuf2-devel >= 2.0
Requires:	glib2-devel >= 1:2.62.0

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

%package apidocs
Summary:	libnotify API documentation
Summary(hu.UTF-8):	libnotify API dokumentáció
Summary(pl.UTF-8):	Dokumentacja API biblioteki libnotify
Group:		Documentation
BuildArch:	noarch

%description apidocs
libnotify API documentation.

%description apidocs -l hu.UTF-8
libnotify API dokumentáció.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libnotify.

%prep
%setup -q

%if %{with static_libs}
%{__sed} -i -e '/libnotify_lib/ s/shared_library/library/' libnotify/meson.build
%endif

%build
%meson \
	%{!?with_apidocs:-Dgtk_doc=false} \
	%{!?with_tests:-Dtests=false}

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libnotify/spec

%if %{with apidocs}
install -d $RPM_BUILD_ROOT%{_gidocdir}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/libnotify-0 $RPM_BUILD_ROOT%{_gidocdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS build/docs/notification-spec.html
%attr(755,root,root) %{_bindir}/notify-send
%attr(755,root,root) %{_libdir}/libnotify.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnotify.so.4
%{_libdir}/girepository-1.0/Notify-0.7.typelib
%{_mandir}/man1/notify-send.1*

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

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gidocdir}/libnotify-0
%endif
