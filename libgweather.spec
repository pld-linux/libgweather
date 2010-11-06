Summary:	Library to access weather information from online services for numerous locations
Summary(pl.UTF-8):	Biblioteka dostępu do informacji pogodowych z serwisów internetowych dla różnych miejsc
Name:		libgweather
Version:	2.91.0
Release:	0.1
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgweather/2.91/%{name}-%{version}.tar.bz2
# Source0-md5:	caca489d500e7a8e3cd5ad3b38b78273
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.26.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gtk+2-devel >= 2:2.16.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.40.3
BuildRequires:	libsoup-gnome-devel >= 2.26.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	pkgconfig >= 1:0.19
Requires(post,postun):	gnome-icon-theme
Requires(post,postun):	gtk+2
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
Requires:	GConf2-devel >= 2.26.0
Requires:	gtk+2-devel >= 2:2.16.0
Requires:	libsoup-devel >= 2.26.0
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
sed -i s#^en@shaw## po/LINGUAS
rm po/en@shaw.po

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-zoneinfo-dir=%{_datadir}/zoneinfo \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--disable-silent-rules
%{__make} -j1 -C data
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/es_ES

%find_lang libgweather-3.0

find $RPM_BUILD_ROOT -name "Locations.*.xml" | sed 's:'"$RPM_BUILD_ROOT"'::
s:\(.*\)/Locations\.\([^.]*\)\.xml:%lang(\2) \1/Locations.\2.xml:' >> libgweather.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_icon_cache gnome
%gconf_schema_install gweather.schemas

%preun
%gconf_schema_uninstall gweather.schemas

%postun
/sbin/ldconfig
%update_icon_cache gnome

%files -f libgweather-3.0.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/libgweather-3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgweather-3.so.0
%{_sysconfdir}/gconf/schemas/gweather.schemas
%dir %{_datadir}/libgweather
%{_datadir}/libgweather/Locations.xml
%{_datadir}/libgweather/locations.dtd
%{_iconsdir}/gnome/*/status/*.png
# XXX: gnome-icon-theme doesn't provide this directory
%{_iconsdir}/gnome/scalable
%{_libdir}/girepository-1.0/GWeather-3.0.typelib
%lang(ang) %{_datadir}/libgweather/Locations.ang.xml
%lang(ar) %{_datadir}/libgweather/Locations.ar.xml
%lang(as) %{_datadir}/libgweather/Locations.as.xml
%lang(ast) %{_datadir}/libgweather/Locations.ast.xml
%lang(az) %{_datadir}/libgweather/Locations.az.xml
%lang(be) %{_datadir}/libgweather/Locations.be.xml
%lang(be) %{_datadir}/libgweather/Locations.be@latin.xml
%lang(bg) %{_datadir}/libgweather/Locations.bg.xml
%lang(bn) %{_datadir}/libgweather/Locations.bn.xml
%lang(bn_IN) %{_datadir}/libgweather/Locations.bn_IN.xml
%lang(br) %{_datadir}/libgweather/Locations.br.xml
%lang(bs) %{_datadir}/libgweather/Locations.bs.xml
%lang(ca) %{_datadir}/libgweather/Locations.ca.xml
%lang(ca) %{_datadir}/libgweather/Locations.ca@valencia.xml
%lang(crh) %{_datadir}/libgweather/Locations.crh.xml
%lang(cs) %{_datadir}/libgweather/Locations.cs.xml
%lang(cy) %{_datadir}/libgweather/Locations.cy.xml
%lang(da) %{_datadir}/libgweather/Locations.da.xml
%lang(de) %{_datadir}/libgweather/Locations.de.xml
%lang(dz) %{_datadir}/libgweather/Locations.dz.xml
%lang(el) %{_datadir}/libgweather/Locations.el.xml
%lang(en@shaw) %{_datadir}/libgweather/Locations.en@shaw.xml
%lang(en_CA) %{_datadir}/libgweather/Locations.en_CA.xml
%lang(en_GB) %{_datadir}/libgweather/Locations.en_GB.xml
%lang(eo) %{_datadir}/libgweather/Locations.eo.xml
%lang(es) %{_datadir}/libgweather/Locations.es.xml
%lang(et) %{_datadir}/libgweather/Locations.et.xml
%lang(eu) %{_datadir}/libgweather/Locations.eu.xml
%lang(fa) %{_datadir}/libgweather/Locations.fa.xml
%lang(fi) %{_datadir}/libgweather/Locations.fi.xml
%lang(fr) %{_datadir}/libgweather/Locations.fr.xml
%lang(ga) %{_datadir}/libgweather/Locations.ga.xml
%lang(gl) %{_datadir}/libgweather/Locations.gl.xml
%lang(gu) %{_datadir}/libgweather/Locations.gu.xml
%lang(he) %{_datadir}/libgweather/Locations.he.xml
%lang(hi) %{_datadir}/libgweather/Locations.hi.xml
%lang(hr) %{_datadir}/libgweather/Locations.hr.xml
%lang(hu) %{_datadir}/libgweather/Locations.hu.xml
%lang(id) %{_datadir}/libgweather/Locations.id.xml
%lang(it) %{_datadir}/libgweather/Locations.it.xml
%lang(ja) %{_datadir}/libgweather/Locations.ja.xml
%lang(ka) %{_datadir}/libgweather/Locations.ka.xml
%lang(kn) %{_datadir}/libgweather/Locations.kn.xml
%lang(ko) %{_datadir}/libgweather/Locations.ko.xml
%lang(ku) %{_datadir}/libgweather/Locations.ku.xml
%lang(ky) %{_datadir}/libgweather/Locations.ky.xml
%lang(lt) %{_datadir}/libgweather/Locations.lt.xml
%lang(lv) %{_datadir}/libgweather/Locations.lv.xml
%lang(mai) %{_datadir}/libgweather/Locations.mai.xml
%lang(mg) %{_datadir}/libgweather/Locations.mg.xml
%lang(mk) %{_datadir}/libgweather/Locations.mk.xml
%lang(ml) %{_datadir}/libgweather/Locations.ml.xml
%lang(mn) %{_datadir}/libgweather/Locations.mn.xml
%lang(mr) %{_datadir}/libgweather/Locations.mr.xml
%lang(ms) %{_datadir}/libgweather/Locations.ms.xml
%lang(nb) %{_datadir}/libgweather/Locations.nb.xml
%lang(nds) %{_datadir}/libgweather/Locations.nds.xml
%lang(ne) %{_datadir}/libgweather/Locations.ne.xml
%lang(nl) %{_datadir}/libgweather/Locations.nl.xml
%lang(nn) %{_datadir}/libgweather/Locations.nn.xml
%lang(oc) %{_datadir}/libgweather/Locations.oc.xml
%lang(or) %{_datadir}/libgweather/Locations.or.xml
%lang(pa) %{_datadir}/libgweather/Locations.pa.xml
%lang(pl) %{_datadir}/libgweather/Locations.pl.xml
%lang(pt) %{_datadir}/libgweather/Locations.pt.xml
%lang(pt_BR) %{_datadir}/libgweather/Locations.pt_BR.xml
%lang(ro) %{_datadir}/libgweather/Locations.ro.xml
%lang(ru) %{_datadir}/libgweather/Locations.ru.xml
%lang(rw) %{_datadir}/libgweather/Locations.rw.xml
%lang(si) %{_datadir}/libgweather/Locations.si.xml
%lang(sk) %{_datadir}/libgweather/Locations.sk.xml
%lang(sl) %{_datadir}/libgweather/Locations.sl.xml
%lang(sq) %{_datadir}/libgweather/Locations.sq.xml
%lang(sr) %{_datadir}/libgweather/Locations.sr.xml
%lang(sr) %{_datadir}/libgweather/Locations.sr@latin.xml
%lang(sv) %{_datadir}/libgweather/Locations.sv.xml
%lang(ta) %{_datadir}/libgweather/Locations.ta.xml
%lang(te) %{_datadir}/libgweather/Locations.te.xml
%lang(th) %{_datadir}/libgweather/Locations.th.xml
%lang(tr) %{_datadir}/libgweather/Locations.tr.xml
%lang(ug) %{_datadir}/libgweather/Locations.ug.xml
%lang(uk) %{_datadir}/libgweather/Locations.uk.xml
%lang(vi) %{_datadir}/libgweather/Locations.vi.xml
%lang(zh_CN) %{_datadir}/libgweather/Locations.zh_CN.xml
%lang(zh_HK) %{_datadir}/libgweather/Locations.zh_HK.xml
%lang(zh_TW) %{_datadir}/libgweather/Locations.zh_TW.xml

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgweather-3.so
%{_libdir}/libgweather-3.la
%{_includedir}/libgweather-3.0
%{_pkgconfigdir}/gweather-3.0.pc
%{_datadir}/gir-1.0/GWeather-3.0.gir


%files static
%defattr(644,root,root,755)
%{_libdir}/libgweather-3.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgweather-3.0
