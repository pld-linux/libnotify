Summary:	Desktop notifications library
Summary(pl):	Biblioteka powiadomieñ dla pulpitu
Name:		libnotify
Version:	0.4.0
Release:	2
License:	LGPL v2.1+ (library), GPL v2+ (tools)
Group:		Applications/System
Source0:	http://www.galago-project.org/files/releases/source/libnotify/%{name}-%{version}.tar.gz
# Source0-md5:	c9b5b51578742908bb1d3201a2da8f00
URL:		http://www.galago-project.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	glib2-devel >= 2.2.2
BuildRequires:	gtk+2-devel >= 1:2.2.2
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	dbus-glib >= 0.60
BuildRoot:	%{_tmppath}/%{name}-%{version}-root-%(id -u -n)

%description
A library that sends desktop notifications to a notification daemon,
as defined in the Desktop Notifications spec. These notifications can
be used to inform the user about an event or display some form of
information without getting in the user's way.

%description -l pl
Biblioteka wysy³aj±ca powiadomienia dla pulpitu do demona powiadomieñ
zgodnie ze specyfikacj± Desktop Notifications. Powiadomienia te mog±
byæ u¿ywane do informowania u¿ytkownika o zdarzeniu lub wy¶wietlania
jakiej¶ formy informacji bez wchodzenia u¿ytkownikowi w drogê.

%package devel
Summary:	libnotify header files
Summary(pl):	Pliki nag³ówkowe biblioteki libnotify
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib-devel >= 0.36
Requires:	glib2-devel >= 2.2.2
Requires:	gtk+2-devel >= 1:2.2.2

%description devel
Header files for libnotify-based programs development.

%description devel -l pl
Pliki nag³ówkowe do tworzenia programów opartych o libnotify.

%package static
Summary:	Static libnotify library
Summary(pl):	Statyczna biblioteka libnotify
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnotify library.

%description static -l pl
Statyczna biblioteka libnotify.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
