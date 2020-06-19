#
# Conditional build:
%bcond_without	glade	# Glade catalog
%bcond_without	vala	# Vala API

Summary:	Library to access weather information from online services for numerous locations
Summary(pl.UTF-8):	Biblioteka dostępu do informacji pogodowych z serwisów internetowych dla różnych miejsc
Name:		libgweather
Version:	3.36.1
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgweather/3.36/%{name}-%{version}.tar.xz
# Source0-md5:	d6081108f9c224c5cb594f8ccb025db9
URL:		https://wiki.gnome.org/Projects/LibGWeather
BuildRequires:	geocode-glib-devel
BuildRequires:	gettext-tools >= 0.18
%{?with_glade:BuildRequires:	glade-devel >= 2.0}
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gtk+3-devel >= 3.14.0
BuildRequires:	gtk-doc >= 1.11
BuildRequires:	libsoup-devel >= 2.44.0
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
%{?with_vala:BuildRequires:	vala >= 2:0.18.0}
BuildRequires:	xz
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	glib2 >= 1:2.44.0
Requires:	glib2 >= 1:2.44.0
Requires:	gtk+3 >= 3.14.0
Requires:	libsoup >= 2.44.0
Requires:	libxml2 >= 1:2.6.30
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
Requires:	glib2-devel >= 1:2.44.0
Requires:	gtk+3-devel >= 3.14.0
Requires:	libsoup-devel >= 2.44.0
Requires:	libxml2-devel >= 1:2.6.30
Obsoletes:	gnome-applets-devel <= 2.21.4
Obsoletes:	libgweather-static < 3.28.0

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
%if "%{_rpmversion}" >= "4.6"
BuildArch:	noarch
%endif

%description apidocs
libgweather API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libgweather.

%package glade
Summary:	libgweather catalog file for Glade
Summary(pl.UTF-8):	Plik katalogu libgweather dla Glade
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	glade >= 2.0
%if "%{_rpmversion}" >= "4.6"
BuildArch:	noarch
%endif

%description glade
libgweather catalog file for Glade.

%description glade -l pl.UTF-8
Plik katalogu libgweather dla Glade.

%package -n vala-libgweather
Summary:	libgweather API for Vala language
Summary(pl.UTF-8):	API biblioteki libgweather dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.18.0
%if "%{_rpmversion}" >= "4.6"
BuildArch:	noarch
%endif

%description -n vala-libgweather
libgweather API for Vala language.

%description -n vala-libgweather -l pl.UTF-8
API biblioteki libgweather dla języka Vala.

%prep
%setup -q

%build
%meson build \
	-Dglade_catalog=%{!?with_glade:false}%{?with_glade:true} \
	-Dgtk_doc=true \
	-Dzoneinfo_dir=%{_datadir}/zoneinfo \
	-Denable_vala=%{!?with_vala:false}%{?with_vala:true}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# just a copy of es
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/es_ES

%find_lang libgweather-3.0 --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%glib_compile_schemas

%postun
/sbin/ldconfig
%glib_compile_schemas

%files -f libgweather-3.0.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README.md
%attr(755,root,root) %{_libdir}/libgweather-3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgweather-3.so.16
%{_datadir}/glib-2.0/schemas/org.gnome.GWeather.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.GWeather.gschema.xml
%dir %{_datadir}/libgweather
%{_datadir}/libgweather/Locations.xml
%{_datadir}/libgweather/locations.dtd
%{_libdir}/girepository-1.0/GWeather-3.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgweather-3.so
%{_includedir}/libgweather-3.0
%{_pkgconfigdir}/gweather-3.0.pc
%{_datadir}/gir-1.0/GWeather-3.0.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgweather

%if %{with glade}
%files glade
%defattr(644,root,root,755)
%{_datadir}/glade/catalogs/libgweather.xml
%endif

%if %{with vala}
%files -n vala-libgweather
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gweather-3.0.vapi
%{_datadir}/vala/vapi/gweather-3.0.deps
%endif
