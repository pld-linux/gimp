Summary:	The GNU Image Manipulation Program
Summary(fr):	Le programme de manipulation d'images de GNU
Summary(de):	Das GNU-Bildbearbeitungs-Programm
Summary(pl):	GNU program do manipulacji formatami graficznymi (GIMP)
Summary(tr):	Çizim, boyama ve görüntü iþleme programý
Name:		gimp
Version:	1.1.10
Release:	1
Copyright:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source0:	ftp://ftp.gimp.org/pub/gimp/unstable/v%{version}/%{name}-%{version}.tar.bz2
Source1:	gimp.desktop
Patch0:		gimp-perlinst.patch
Patch1:		gimp-noWIN.patch
URL:		http://www.gimp.org/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	perl
BuildRequires:	perl-PDL >= 1.9906
BuildRequires:	perl-gtk >= 0.5120
BuildRequires:	perl-Parse-RecDescent
BuildRequires:	XFree86-devel
BuildRequires:	libtiff-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libungif-devel
BuildRequires:	xpm-devel
BuildRequires:	zlib-devel
BuildRequires:	aalib-devel
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-Parse-RecDescent
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	gimp-data-min
Obsoletes:	gimp-libgimp

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The GIMP is an image manipulation program suitable for photo retouching,
image composition and image authoring. Many people find it extremely useful
in creating logos and other graphics for web pages. The GIMP has many of the
tools and filters you would expect to find in similar commercial offerings,
and some interesting extras as well.

The GIMP provides a large image manipulation toolbox, including channel
operations and layers, effects, sub-pixel imaging and anti-aliasing,
and conversions, all with multi-level undo.

This version of The GIMP includes a scripting facility, but many of the
included scripts rely on fonts that we cannot distribute. The GIMP ftp
site has a package of fonts that you can install by yourself, which
includes all the fonts needed to run the included scripts.

%description -l fr
Le Programme de Manipulation d'Image de GNU permet de retoucher des photos,
de réaliser des compositions.  Beaucoup de gens l'apprécient pour la
création de logos et de graphismes pour les pages web.  GIMP dispose d'un
grand nombre de filtres et de plug-ins que l'on ne trouve que dans les
logiciels commerciaux haut de gamme ainsi que de nombreuses fonctionnalité
inédites.

GIMP fournit une boite à outil permettant de gérer plusieurs calques, de
nombreux effets, l'anti-aliasing, les conversions de fichiers ainsi qu'un
grand nombre de niveaux d'annulation.

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
%setup  -q
%patch0 -p0
%patch1 -p1

%build
LDFLAGS="-s"; export LDFLAGS
CFLAGS="$RPM_OPT_FLAGS -DPERL_POLLUTE"; export CFLAGS
%configure \
	--without-included-gettext \
	--without-xdelta \
	--enable-perl \
	--enable-python \
	--with-mp \
	--with-threads=posix 
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/icons \
	$RPM_BUILD_ROOT%{_datadir}/applnk/Graphics

make install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	gimpplugindir=$RPM_BUILD_ROOT%{_libdir}/gimp/1.1 \
	gimpdatadir=$RPM_BUILD_ROOT%{_datadir}/gimp \
	m4datadir=$RPM_BUILD_ROOT/usr/share/aclocal \
	PREFIX=$RPM_BUILD_ROOT/usr \
	INSTALLMAN1DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	INSTALLMAN3DIR=$RPM_BUILD_ROOT/usr/share/man/man3

install pixmaps/*.xpm $RPM_BUILD_ROOT%{_datadir}/icons/
install plug-ins/*/*.xpm $RPM_BUILD_ROOT%{_datadir}/icons/

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applnk/Graphics
mv $RPM_BUILD_ROOT/usr/bin/* $RPM_BUILD_ROOT%{_bindir}

strip --strip-unneeded \
	$RPM_BUILD_ROOT%{_libdir}/lib*.so.*.* \
	$RPM_BUILD_ROOT%{_libdir}/gimp/1.1/modules/lib*.so \
	$RPM_BUILD_ROOT%{perl_sitearch}/auto/Gimp/*.so \
	$RPM_BUILD_ROOT%{perl_sitearch}/auto/Gimp/{Lib,Net}/*.so

gzip -9nf $RPM_BUILD_ROOT/usr/share/man/man3/* \
	$RPM_BUILD_ROOT%{_mandir}/man[135]/* \
	ChangeLog NEWS README README.i18n README.perl \
	TODO MAINTAINERS docs/*.txt

%find_lang %{name}
%find_lang %{name}-std-plugins

cat %{name}-std-plugins.lang >> %{name}.lang

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {ChangeLog,NEWS,README,README.i18n,README.perl,MAINTAINERS}.gz
%doc docs/*.gz docs/*README docs/*.eps docs/script-fu.tex 
%doc docs/white-paper/gimp-white-paper.tex docs/quick_reference.*

%attr(755,root,root) %{_bindir}/gimp 
%{_datadir}/applnk/Graphics/gimp.desktop

%{_mandir}/man1/gimp.1* 
%{_mandir}/man5/gimprc.5*

%attr(755,root,root) %{_libdir}/lib*.so.* 
%dir %{_libdir}/gimp
%dir %{_libdir}/gimp/1.1
%dir %{_libdir}/gimp/1.1/plug-ins
%attr(755,root,root) %{_libdir}/gimp/1.1/plug-ins/*
%dir %{_libdir}/gimp/1.1/modules
%attr(755,root,root) %{_libdir}/gimp/1.1/modules/*la
%attr(755,root,root) %{_libdir}/gimp/1.1/modules/*so

%dir %{_datadir}/gimp
%{_datadir}/gimp/brushes
%{_datadir}/gimp/fractalexplorer
%{_datadir}/gimp/gfig
%{_datadir}/gimp/gflare
%{_datadir}/gimp/gimpressionist
%{_datadir}/gimp/gradients
%{_datadir}/gimp/help
%{_datadir}/gimp/palettes
%{_datadir}/gimp/patterns
%{_datadir}/gimp/scripts
%{_datadir}/gimp/*.ppm

%dir %{_datadir}/gimp/tips
%{_datadir}/gimp/tips/gimp_tips.txt
%lang(fr) %{_datadir}/gimp/tips/gimp_conseils.fr.txt
%lang(de) %{_datadir}/gimp/tips/gimp_tips.de.txt
%lang(ja) %{_datadir}/gimp/tips/gimp_tips.ja.txt
%lang(ru) %{_datadir}/gimp/tips/gimp_tips.ru.txt

%config %verify(not md5 mtime) %{_datadir}/gimp/gimprc*
%config %{_datadir}/gimp/gtkrc*
%config %{_datadir}/gimp/ps-menurc
%config %{_datadir}/gimp/unitrc

%attr(755,root,root) %{_datadir}/gimp/user_install

%{_datadir}/icons/*.xpm 

## perl stuff
%{perl_sitearch}/Gimp
%{perl_sitearch}/Gimp.pm
%dir %{perl_sitearch}/auto/Gimp
%dir %{perl_sitearch}/auto/Gimp/Lib
%dir %{perl_sitearch}/auto/Gimp/Net
%{perl_sitearch}/auto/Gimp/Gimp.bs
%{perl_sitearch}/auto/Gimp/Lib/Lib.bs
%{perl_sitearch}/auto/Gimp/Net/Net.bs
%attr(755,root,root) %{perl_sitearch}/auto/Gimp/Lib/Lib.so
%attr(755,root,root) %{perl_sitearch}/auto/Gimp/Net/Net.so
%attr(755,root,root) %{perl_sitearch}/auto/Gimp/Gimp.so

%files devel
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/gimptool
%attr(755,root,root) %{_libdir}/lib*.so 
%{_libdir}/lib*.la

%{_includedir}/gck/*.h 
%{_includedir}/libgimp/*.h
/usr/share/aclocal/gimp.m4

%attr(755,root,root) %{_bindir}/embedxpm
%attr(755,root,root) %{_bindir}/gimpdoc
%attr(755,root,root) %{_bindir}/scm2perl
%attr(755,root,root) %{_bindir}/scm2scm
%attr(755,root,root) %{_bindir}/xcftopnm

%{_mandir}/man1/gimptool.1*
%{_mandir}/man1/scm2*.1*
%{_mandir}/man3/*
/usr/share/man/man3/*

%files static
%attr(644,root,root) %{_libdir}/lib*.a
