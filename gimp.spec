Summary:	The GNU Image Manipulation Program
Summary(fr):	Le programme de manipulation d'images de GNU.
Summary(de):	Das GNU-Bildbearbeitungs-Programm
Summary(pl):	GNU program do manipulacji formatami graficznymi (GIMP)
Summary(tr):	Çizim, boyama ve görüntü iþleme programý
Name:		gimp
Version:	1.1.6
Release:	1
Copyright:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
#######		ftp://ftp.gimp.org/pub/gimp/unstable/v1.1.5/
Source:		%{name}-%{version}.tar.bz2
URL:		http://www.gimp.org/
Requires:	gtk+ >= 1.1.15
Requires:	glib >= 1.1.15
Requires:	perl >= 5.005
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	gimp-data-min
Obsoletes:	gimp-libgimp

%define	_prefix	/usr/X11R6

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

%package	devel
Summary:	GIMP plugin and extension development kit
Summary(fr):	Plugin GIMP et kit de développement d'extensions
Summary(de):	GIMP-Plugin und Extension Development Kit
Summary(pl):	Dodatkowe moduly i rozszerzenia dla Gimp
Summary(tr):	GIMP plugin ve uzantý geliþtirme araçlarý
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Copyright:	LGPL
Requires:	%{name} = %{version}
Requires:	gtk+-devel >= 1.1.15

%description devel
Header files for writing GIMP plugins and extensions.

%description -l de devel
Header-Dateien zum Schreiben von GIMP-Plugins und -Erweiterungen

%descriptions -l pl devel
Pliki nag³ówowe dla GIMP.

%package static
Summary:     GIMP static libraries
Summary(pl): Biblioteki statyczne do GIMPa
Group:       Libraries
Requires:    %{name}-devel = %{version}

%description static
GIMP static libraries

%description -l pl static
Biblioteki statyczne do GIMPa

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS -Wall" \
LDFLAGS="-s" \
./configure %{_target}\
	--prefix=%{_prefix} \
	--without-included-gettext \
	--without-xdelta 
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11
install -d $RPM_BUILD_ROOT/usr/share/aclocal
install -d $RPM_BUILD_ROOT/usr/X11R6/share/icons 
install -d $RPM_BUILD_ROOT/usr/lib/perl5/5.00502/$RPM_ARCH-linux-thread
install -d $RPM_BUILD_ROOT/usr/X11R6/lib/gimp/1.1/modules

make install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	INSTALLMAN1DIR=$RPM_BUILD_ROOT/usr/share/man/man1 \
	INSTALLMAN3DIR=$RPM_BUILD_ROOT/usr/share/man/man3 \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	INSTALLMAN5DIR=$RPM_BUILD_ROOT/usr/share/man/man5

mv $RPM_BUILD_ROOT%{_datadir}/aclocal/* $RPM_BUILD_ROOT/usr/share/aclocal

install pixmaps/*.xpm $RPM_BUILD_ROOT/usr/X11R6/share/icons/
install plug-ins/*/*.xpm $RPM_BUILD_ROOT/usr/X11R6/share/icons/

strip $RPM_BUILD_ROOT/usr/X11R6/{lib/lib*.so.*.*,bin/gimp,lib/gimp/*/plug-ins/*} ||:

mv $RPM_BUILD_ROOT/usr/share/aclocal/gimp* $RPM_BUILD_ROOT/%{_datadir}/aclocal

mv $RPM_BUILD_ROOT/usr/X11R6/lib/perl5/5.* $RPM_BUILD_ROOT/usr/lib/perl5/
install -d $RPM_BUILD_ROOT/usr/lib/perl5/site_perl/5.005
mv $RPM_BUILD_ROOT/usr/X11R6/lib/perl5/site_perl/5.005/* \
	$RPM_BUILD_ROOT/usr/lib/perl5/site_perl/5.005/

gzip -9 $RPM_BUILD_ROOT/usr/X11R6/man/man[135]/*
gzip -9 $RPM_BUILD_ROOT/usr/share/man/man[13]/*

bzip2 -9 ChangeLog NEWS README docs/*.txt

%find_lang	gimp
%find_lang	gimp-std-plugins

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f gimp.lang -f gimp-std-plugins
%defattr(644,root,root,755)
%doc ChangeLog.bz2 NEWS.bz2 README.bz2 docs/*.bz2 docs/*.eps

%attr(755,root,root) %{_bindir}/gimp 
%attr(755,root,root) %{_bindir}/gimpdoc 

%attr(644,root, man) %{_mandir}/man1/gimp.1* 

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

%config %verify(not md5 mtime) /usr/X11R6/share/gimp/gimprc*
%config /usr/X11R6/share/gimp/gtkrc*
%config /usr/X11R6/share/gimp/ps-menurc

##/usr/X11R6/share/gimp/gimp_tips.txt

%attr(755,root,root) /usr/X11R6/share/gimp/user_install

##/usr/X11R6/share/icons/*.xpm
%{_datadir}/icons/*.xpm 

%attr(-,root,root) /usr/lib/perl5/* 
#%attr(-,root,root) /usr/lib/perl5/*

%files devel
%defattr(644,root,root,755)

%attr(755,root,root) /usr/X11R6/lib/lib*.so 

%attr(644,root,root) %{_includedir}/gck/*.h 
%attr(644,root,root) %{_includedir}/libgimp/*.h
%attr(644,root,root)%{_datadir}/aclocal/gimp.m4

%attr(755,root,root) %{_bindir}/gimptool
%attr(755,root,root) %{_bindir}/scm2*

%attr(644,root, man) /usr/X11R6/man/man1/gimptool.1*
%attr(644,root, man) /usr/X11R6/man/man3/gpc.3*
%attr(644,root, man) /usr/X11R6/man/man5/gimprc.5*

%attr(644,root, man) /usr/share/man/man1/*
%attr(644,root, man) /usr/share/man/man3/*

%files static
%attr(644,root,root) %{_libdir}/lib*.a
%attr(644,root,root) %{_libdir}/lib*.la

%changelog
* Mon Jun 14 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
  [1.1.6-1]
- updated to version 1.1.6.

* Mon May 31 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
  [1.1.5-1]
- updated to 1.1.5,
- fixes file locations,
- based on gimp.spec from PLD-devel.
