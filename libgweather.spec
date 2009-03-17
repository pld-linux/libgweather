Summary:	Library to access weather information from online services for numerous locations
Summary(pl.UTF-8):	Biblioteka dostępu do informacji pogodowych z serwisów internetowych dla różnych miejsc
Name:		libgweather
Version:	2.26.0
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgweather/2.26/%{name}-%{version}.tar.bz2
# Source0-md5:	b96016d7b35c66cf251189e9851ee252
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.25.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gtk+2-devel >= 2:2.15.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libsoup-gnome-devel >= 2.25.90
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	pkgconfig >= 1:0.19
Requires(post,preun):	GConf2
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgweather is a library to access weather information from online
services for numerous locations.

%description -l pl.UTF-8
libgweather to biblioteka pozwalająca na dostęp do informacji
pogodowych z serwisów internetowych dla różnych miejsc.

%package devel
Summary:	Header files for libgweather
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgweather
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	GConf2-devel >= 2.25.0
Requires:	gtk+2-devel >= 2:2.15.0
Requires:	libsoup-devel >= 2.25.90
Requires:	libxml2-devel >= 1:2.6.30
Obsoletes:	gnome-applets-devel <= 2.21.4

%description devel
Header files for libgweather.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgweather.

%package static
Summary:	Static libgweather library
Summary(pl.UTF-8):	Statyczna biblioteka libgweather
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgweather library.

%description static -l pl.UTF-8
Statyczna biblioteka libgweather.

%package apidocs
Summary:	libgweather API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libgweather
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libgweather API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libgweather.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-zoneinfo-dir=%{_datadir}/zoneinfo \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make} -j1 -C data
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/es_ES

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
%attr(755,root,root) %{_libdir}/libgweather.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgweather.so.1
%{_sysconfdir}/gconf/schemas/gweather.schemas
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

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgweather
