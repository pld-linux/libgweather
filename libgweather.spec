Summary:	libgweather is a library to access weather information from online services for numerous locations
Name:		libgweather
Version:	2.21.2
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgweather/2.21/%{name}-%{version}.tar.bz2
# Source0-md5:	715394c673895b52d1f807f874b66770
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.8.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.8
BuildRequires:	glib2-devel >= 2.13.0
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-vfs2-devel >= 2.15.4
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool >= 0.36.1
BuildRequires:	libtool
BuildRequires:	pkgconfig
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgweather is a library to access weather information from online
services for numerous locations.

%package devel
Summary:	Header files for libgweather
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.12.0

%description devel
Header files for libgweather.

%package static
Summary:	Static libgweather library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgweather library.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
%find_lang libgweather

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%gconf_schema_install gweather.schemas

%preun
%gconf_schema_uninstall gweather.schemas

%postun	-p /sbin/ldconfig

%files -f libgweather.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%{_sysconfdir}/gconf/schemas/gweather.schemas
%attr(755,root,root) %{_libdir}/libgweather.so.*.*.*
%{_datadir}/libgweather

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgweather.so
%{_libdir}/libgweather.la
%{_includedir}/libgweather
%{_pkgconfigdir}/gweather.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgweather.a
