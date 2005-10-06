Summary:	Desktop notifications library
Name:		libnotify
Version:	0.2.2
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://www.galago-project.org/files/releases/source/libnotify/%{name}-%{version}.tar.gz
# Source0-md5:	cbf2ff0a8a62eb1f310367a0a174a273
URL:		http://www.galago-project.org/
BuildRequires:	dbus-devel >= 0.30
Requires:	dbus >= 0.30
BuildRoot:	%{_tmppath}/%{name}-%{version}-root-%(id -u -n)

%description
A library that sends desktop notifications to a notification daemon, as
defined in the Desktop Notifications spec. These notifications can be
used to inform the user about an event or display some form of
information without getting in the user's way.

%package devel
Summary:	libnotify header files
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for libnotify-based programs development.

%prep
%setup -q

%build
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
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/pkgconfig/*
%{_includedir}/*
