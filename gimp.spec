Summary:	The GNU Image Manipulation Program
Summary(fr):	Le programme de manipulation d'images de GNU.
Summary(de):	Das GNU-Bildbearbeitungs-Programm
Summary(pl):	GNU program do manipulacji formatami graficznymi (GIMP)
Summary(tr):	Çizim, boyama ve görüntü iþleme programý
Name:		gimp
Version:	1.1.6
Release:	2
Copyright:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source:		ftp://ftp.gimp.org/pub/gimp/unstable/v%{version}/%{name}-%{version}.tar.bz2
URL:		http://www.gimp.org/
BuildPrereq:	gtk+-devel >= 1.2.0
BuildPrereq:	glib-devel >= 1.2.0
BuildPrereq:	perl
BuildPrereq:	XFree86-devel
BuildPrereq:	libtiff-devel
BuildPrereq:	libjpeg-devel
BuildPrereq:	libpng-devel
BuildPrereq:	libungif-devel
BuildPrereq:	xpm-devel
BuildPrereq:	zlib-devel
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	gimp-data-min
Obsoletes:	gimp-libgimp

%define	_prefix	/usr/X11R6
%define	_mandir	%{_prefix}/man

%description
The GIMP is an image manipulation program suitable for photo retouching,
image composition and image authoring.  Many people find it extremely useful
in creating logos and other graphics for web pages.  The GIMP has many of the
tools and filters you would expect to find in similar commercial offerings,
and some interesting extras as well.

The GIMP provides a large image manipulation toolbox, including channel
operations and layers, effects, sub-pixel imaging and anti-aliasing,
and conversions, all with multi-level undo.

This version of The GIMP includes a scripting facility, but many of the
included scripts rely on fonts that we cannot distribute.  The GIMP ftp
site has a package of fonts that you can install by yourself, which
includes all the fonts needed to run the included scripts.  Some of the
fonts have unusual licensing requirements; all the licenses are documented
in the package. Get ftp://ftp.gimp.org/pub/gimp/fonts/freefonts-0.10.tar.gz
and ftp://ftp.gimp.org/pub/gimp/fonts/sharefonts-0.10.tar.gz if you are so
inclined. Alternatively, choose fonts which exist on your system before
running the scripts.

%description -l pl
Program Gimp jest przeznaczony do obróbki i tworzenia plików w ró¿nych
formatach graficznych. Dziêki niemu bêdziesz móg³ stworzyæ grafikê dla 
stron WWW, przerobiæ zdjêcia, czy stworzyæ w³asne logo.

%package devel
Summary:	GIMP plugin and extension development kit
Summary(fr):	Plugin GIMP et kit de développement d'extensions
Summary(de):	GIMP-Plugin und Extension Development Kit
Summary(pl):	Dodatkowe moduly i rozszerzenia dla Gimp
Summary(tr):	GIMP plugin ve uzantý geliþtirme araçlarý
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Copyright:	LGPL
Requires:	%{name} = %{version}
Requires:	gtk+-devel >= 1.2.0

%description devel
Header files for writing GIMP plugins and extensions.

%description -l de devel
Header-Dateien zum Schreiben von GIMP-Plugins und -Erweiterungen

%descriptions -l pl devel
Pliki nag³ówkowe dla GIMP.

%package static
Summary:	GIMP static libraries
Summary(pl):	Biblioteki statyczne do GIMPa
Group:		Libraries
Requires:	%{name}-devel = %{version}

%description static
GIMP static libraries.

%description -l pl static
Biblioteki statyczne do GIMPa.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS -Wall" \
LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--without-included-gettext \
	--without-xdelta 
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11,usr/share/aclocal} \
	$RPM_BUILD_ROOT%{_datadir}/icons \
	$RPM_BUILD_ROOT%{perl_sitearch} \
	$RPM_BUILD_ROOT%{_libdir}/gimp/1.1/{modules,plug-ins}

make install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	INSTALLMAN1DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	INSTALLMAN3DIR=$RPM_BUILD_ROOT/usr/share/man/man3 \
	PREFIX=$RPM_BUILD_ROOT/usr \
	INSTALLMAN5DIR=$RPM_BUILD_ROOT%{_mandir}/man5

mv $RPM_BUILD_ROOT%{_datadir}/aclocal/* $RPM_BUILD_ROOT/usr/share/aclocal
mv $RPM_BUILD_ROOT/usr/bin/* $RPM_BUILD_ROOT%{_bindir}

install pixmaps/*.xpm $RPM_BUILD_ROOT%{_datadir}/icons/
install plug-ins/*/*.xpm $RPM_BUILD_ROOT%{_datadir}/icons/

strip $RPM_BUILD_ROOT{%{_bindir}/gimp,%{_libdir}/gimp/*/plug-ins/*} ||: 
strip --strip-unneeded \
	$RPM_BUILD_ROOT%{_libdir}/lib*.so.*.* \
	$RPM_BUILD_ROOT%{perl_sitearch}/auto/Gimp/*.so \
	$RPM_BUILD_ROOT%{perl_sitearch}/auto/Gimp/{Lib,Net}/*.so

gzip -9nf $RPM_BUILD_ROOT/usr/share/man/man3/* \
	$RPM_BUILD_ROOT%{_mandir}/man[135]/* \
	ChangeLog NEWS README README.i18n README.perl \
	TODO MAINTAINERS docs/*.txt

%find_lang %{name}
%find_lang %{name}-std-plugins

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang -f %{name}-std-plugins.lang
%defattr(644,root,root,755)
%doc {ChangeLog,NEWS,README,README.i18n,README.perl,MAINTAINERS}.gz
%doc docs/*.gz docs/*README docs/*.eps docs/script-fu.tex 
%doc docs/white-paper/gimp-white-paper.tex docs/quick_reference.*

%attr(755,root,root) %{_bindir}/gimp 
%attr(755,root,root) %{_bindir}/gimpdoc 

%{_mandir}/man1/gimp.1* 
%{_mandir}/man5/gimprc.5*

%attr(755,root,root) %{_libdir}/lib*.so.* 
%attr(755,root,root) %{_libdir}/gimp 

%dir %{_datadir}/gimp
%{_datadir}/gimp/brushes
%{_datadir}/gimp/gfig
%{_datadir}/gimp/gradients
%{_datadir}/gimp/palettes
%{_datadir}/gimp/patterns
%{_datadir}/gimp/scripts
%{_datadir}/gimp/*.ppm

%dir %{_datadir}/gimp/tips
%{_datadir}/gimp/tips/gimp_tips.txt
%lang(fr) %{_datadir}/gimp/tips/gimp_conseils.fr.txt
%lang(de) %{_datadir}/gimp/tips/gimp_tips.de.txt

%config %verify(not md5 mtime) %{_datadir}/gimp/gimprc*
%config %{_datadir}/gimp/gtkrc*
%config %{_datadir}/gimp/ps-menurc

%attr(755,root,root) %{_datadir}/gimp/user_install

%{_datadir}/icons/*.xpm 

## perl stuff
%{perl_sitearch}/Gimp
%dir %{perl_sitearch}/auto/Gimp
%dir %{perl_sitearch}/auto/Gimp/Lib
%dir %{perl_sitearch}/auto/Gimp/Net
%{perl_sitearch}/auto/Gimp/Gimp.bs
%{perl_sitearch}/auto/Gimp/Lib/Lib.bs
%{perl_sitearch}/auto/Gimp/Net/Net.bs
%attr(755,root,root) %{perl_sitearch}/auto/Gimp/Lib/Lib.so
%attr(755,root,root) %{perl_sitearch}/auto/Gimp/Net/Net.so
%attr(755,root,root) %{perl_sitearch}/auto/Gimp/Gimp.so
/usr/share/man/man3/Gimp*

%files devel
%defattr(644,root,root,755)

%attr(755,root,root) %{_libdir}/lib*.so 
%{_libdir}/lib*.la

%{_includedir}/gck/*.h 
%{_includedir}/libgimp/*.h
/usr/share/aclocal/gimp.m4

%attr(755,root,root) %{_bindir}/gimptool
%attr(755,root,root) %{_bindir}/scm2*

%{_mandir}/man1/gimptool.1*
%{_mandir}/man1/scm2*.1*
%{_mandir}/man3/gpc.3*

%files static
%attr(644,root,root) %{_libdir}/lib*.a

%changelog
* Tue Jun 15 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
  [1.1.6-2]
- fixed documentation.

* Mon Jun 14 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
  [1.1.6-1]
- updated to version 1.1.6.

* Mon May 31 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
  [1.1.5-1]
- updated to 1.1.5,
- fixes file locations,
- based on gimp.spec from PLD-devel.
