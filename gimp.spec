%include	/usr/lib/rpm/macros.perl
%define		__find_requires	%{_builddir}/gimp-%{version}/find-perl-requires
Summary:	The GNU Image Manipulation Program
Summary(fr):	Le programme de manipulation d'images de GNU
Summary(de):	Das GNU-Bildbearbeitungs-Programm
Summary(pl):	GNU program do manipulacji formatami graficznymi (GIMP)
Summary(tr):	�izim, boyama ve g�r�nt� i�leme program�
Name:		gimp
Version:	1.1.18
Release:	1
Copyright:	GPL
Group:		X11/Applications/Graphics
Group(fr):	X11/Applications/Graphismes
Group(pl):	X11/Aplikacje/Grafika
Source0:	ftp://ftp.gimp.org/pub/gimp/unstable/v%{version}/%{name}-%{version}.tar.bz2
Source1:	gimp.desktop
Patch0:		gimp-perldep.patch
Patch1:		gimp-DESTDIR.patch
URL:		http://www.gimp.org/
Icon:		gimp.gif
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	perl
BuildRequires:	perl-PDL >= 1.9906
BuildRequires:	perl-gtk >= 0.6123
BuildRequires:	perl-Parse-RecDescent
BuildRequires:	perl-File-Slurp
BuildRequires:	XFree86-devel
BuildRequires:	libtiff-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libungif-devel
BuildRequires:	xpm-devel
BuildRequires:	zlib-devel
BuildRequires:	aalib-devel
BuildRequires:	rpm-perlprov
%requires_eq	perl
Requires:	%{perl_sitearch}
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
de r�aliser des compositions.  Beaucoup de gens l'appr�cient pour la
cr�ation de logos et de graphismes pour les pages web.  GIMP dispose d'un
grand nombre de filtres et de plug-ins que l'on ne trouve que dans les
logiciels commerciaux haut de gamme ainsi que de nombreuses fonctionnalit�
in�dites.

GIMP fournit une boite � outil permettant de g�rer plusieurs calques, de
nombreux effets, l'anti-aliasing, les conversions de fichiers ainsi qu'un
grand nombre de niveaux d'annulation.

%description -l pl
Program Gimp jest przeznaczony do obr�bki i tworzenia plik�w w r�nych
formatach graficznych. Dzi�ki niemu b�dziesz m�g� stworzy� grafik� dla 
stron WWW, przerobi� zdj�cia, czy stworzy� w�asne logo.

%package devel
Summary:	GIMP plugin and extension development kit
Summary(fr):	Plugin GIMP et kit de d�veloppement d'extensions
Summary(de):	GIMP-Plugin und Extension Development Kit
Summary(pl):	Dodatkowe moduly i rozszerzenia dla Gimp
Summary(tr):	GIMP plugin ve uzant� geli�tirme ara�lar�
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
Pliki nag��wkowe dla GIMP.

%package static
Summary:	GIMP static libraries
Summary(pl):	Biblioteki statyczne do GIMPa
Group:		Libraries
Requires:	%{name}-devel = %{version}

%description static
GIMP static libraries.

%description -l pl static
Biblioteki statyczne do GIMPa.

%package aa
Summary:	ASCII Art plugin for Gimp
Summary(fr):	Plugin d'art ASCII pour Gimp
Group:		X11/Applications/Graphics
Group(fr):	X11/Applications/Graphismes
Group(pl):	X11/Aplikacje/Grafika
Requires:	%{name} = %{version}

%description aa
This package contains the ASCII Art plugin which requires the aalib shared
library.

%description aa -l fr
Ce paquet contient le plugin d'art ASCII qui n�c�ssite la librairie partag�e
aalib.

#%package xd
#Summary:	Xdelta plugin for GIMP
#Summary(fr):	Plugin Xdelta pour GIMP
#Group:		X11/Applications/Graphics
#Group(fr):	X11/Applications/Graphismes
#Group(pl):	X11/Aplikacje/Grafika
#Requires:	%{name} = %{version}

#%description xd
#This package contains the Xdelta plugin which requires the xdelta shared
#library.

#%description xd -l fr
#Ce paquet contient le plugin Xdelta qui n�c�ssite la librairie partag�e
#xdelta.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

chmod +x find-perl-requires

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
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=/usr/share/aclocal

install pixmaps/*.xpm $RPM_BUILD_ROOT%{_datadir}/icons/
install plug-ins/*/*.xpm $RPM_BUILD_ROOT%{_datadir}/icons/

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applnk/Graphics
mv $RPM_BUILD_ROOT/usr/bin/* $RPM_BUILD_ROOT%{_bindir}

strip --strip-unneeded \
	$RPM_BUILD_ROOT%{_libdir}/lib*.so.*.* \
	$RPM_BUILD_ROOT%{_libdir}/gimp/1.1/modules/lib*.so \
	$RPM_BUILD_ROOT%{perl_sitearch}/auto/Gimp/*.so \
	$RPM_BUILD_ROOT%{perl_sitearch}/auto/Gimp/*/*.so

gzip -9nf $RPM_BUILD_ROOT/usr/share/man/man[13]/* \
	$RPM_BUILD_ROOT%{_mandir}/man[15]/* \
	ChangeLog NEWS README README.i18n README.perl \
	TODO MAINTAINERS docs/*.txt

%find_lang %{name}
%find_lang %{name}-perl
%find_lang %{name}-script-fu
%find_lang %{name}-std-plugins
cat %{name}.lang %{name}-perl.lang %{name}-script-fu.lang \
	%{name}-std-plugins.lang > %{name}.list

echo "%defattr(755,root,root,755)" >> %{name}.list

ls -1 $RPM_BUILD_ROOT%{_libdir}/gimp/1.1/plug-ins/* | \
	egrep -w -v -e "aa|xd" | \
	sed -e s#^`echo $RPM_BUILD_ROOT`## >> %{name}.list
	
echo "%defattr(644,root,root,755)" >> %{name}.list

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.list
%defattr(644,root,root,755)
%doc {ChangeLog,NEWS,README,README.i18n,README.perl,MAINTAINERS}.gz
%doc docs/*.gz docs/*README docs/*.eps docs/script-fu.tex 
%doc docs/white-paper/gimp-white-paper.tex docs/quick_reference.*

%attr(755,root,root) %{_bindir}/gimp* 
%{_datadir}/applnk/Graphics/gimp.desktop

%{_mandir}/man1/gimp.1* 
%{_mandir}/man5/gimprc.5*

%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/gimp
%dir %{_libdir}/gimp/1.1
%dir %{_libdir}/gimp/1.1/plug-ins
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
%lang(cs) %{_datadir}/gimp/tips/gimp_tips.cs.txt
%lang(de) %{_datadir}/gimp/tips/gimp_tips.de.txt
%lang(it) %{_datadir}/gimp/tips/gimp_tips.it.txt
%lang(ja) %{_datadir}/gimp/tips/gimp_tips.ja.txt
%lang(ko) %{_datadir}/gimp/tips/gimp_tips.ko.txt
%lang(pl) %{_datadir}/gimp/tips/gimp_tips.pl.txt
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
%dir %{perl_sitearch}/auto/Gimp/UI
%{perl_sitearch}/auto/Gimp/Gimp.bs
%{perl_sitearch}/auto/Gimp/Lib/Lib.bs
%{perl_sitearch}/auto/Gimp/Net/Net.bs
%{perl_sitearch}/auto/Gimp/UI/UI.bs
%attr(755,root,root) %{perl_sitearch}/auto/Gimp/Lib/Lib.so
%attr(755,root,root) %{perl_sitearch}/auto/Gimp/Net/Net.so
%attr(755,root,root) %{perl_sitearch}/auto/Gimp/UI/UI.so
%attr(755,root,root) %{perl_sitearch}/auto/Gimp/Gimp.so

%files devel
%defattr(644,root,root,755)
%doc devel-docs/libgimp/html/*
%attr(755,root,root) %{_bindir}/gimptool
%attr(755,root,root) %{_libdir}/lib*.so 
%{_libdir}/lib*.la

%{_includedir}/gck 
%{_includedir}/libgimp
/usr/share/aclocal/gimp.m4

%attr(755,root,root) %{_bindir}/embedxpm
%attr(755,root,root) %{_bindir}/gimpdoc
%attr(755,root,root) %{_bindir}/scm2perl
%attr(755,root,root) %{_bindir}/scm2scm
%attr(755,root,root) %{_bindir}/xcftopnm

%{_mandir}/man1/gimptool.1*
/usr/share/man/man1/*
/usr/share/man/man3/*

%files static
%attr(644,root,root) %{_libdir}/lib*.a

%files aa
%attr(755,root,root) %{_libdir}/gimp/1.1/plug-ins/aa

#%files xd
#%attr(755,root,root) %{_libdir}/gimp/1.1/plug-ins/xd
