%include	/usr/lib/rpm/macros.perl
%define		__find_requires	%{_builddir}/gimp-%{version}/find-perl-requires
Summary:	The GNU Image Manipulation Program
Summary(fr):	Le programme de manipulation d'images de GNU
Summary(de):	Das GNU-Bildbearbeitungs-Programm
Summary(pl):	GNU program do manipulacji formatami graficznymi (GIMP)
Summary(tr):	Çizim, boyama ve görüntü iþleme programý
Name:		gimp
Version:	1.1.32
Release: 	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Graphics
Group(fr):	X11/Applications/Graphismes
Group(pl):	X11/Aplikacje/Grafika
Source0:	ftp://ftp.gimp.org/pub/gimp/unstable/v%{version}/%{name}-%{version}.tar.bz2
Source1:	gimp.desktop
Patch0:		gimp-perldep.patch
Patch1:		gimp-DESTDIR.patch
Patch2:		gimp-croak.patch
Patch3:		gimp-i18n.patch
URL:		http://www.gimp.org/
Icon:		gimp.gif
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.8-3
BuildRequires:	perl >= 1:5.6
BuildRequires:	perl-PDL >= 1.9906
BuildRequires:	perl-gtk >= 0.6123
BuildRequires:	perl-Parse-RecDescent
BuildRequires:	perl-File-Slurp
BuildRequires:	libtiff-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libungif-devel
BuildRequires:	zlib-devel
BuildRequires:	aalib-devel
BuildRequires:	rpm-perlprov
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	gtk+ >= 1.2.8-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gimp-data-min
Obsoletes:	gimp-libgimp

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The GIMP is an image manipulation program suitable for photo
retouching, image composition and image authoring. Many people find it
extremely useful in creating logos and other graphics for web pages.
The GIMP has many of the tools and filters you would expect to find in
similar commercial offerings, and some interesting extras as well.

The GIMP provides a large image manipulation toolbox, including
channel operations and layers, effects, sub-pixel imaging and
anti-aliasing, and conversions, all with multi-level undo.

This version of The GIMP includes a scripting facility, but many of
the included scripts rely on fonts that we cannot distribute. The GIMP
ftp site has a package of fonts that you can install by yourself,
which includes all the fonts needed to run the included scripts.

%description -l fr
Le Programme de Manipulation d'Image de GNU permet de retoucher des
photos, de réaliser des compositions. Beaucoup de gens l'apprécient
pour la création de logos et de graphismes pour les pages web. GIMP
dispose d'un grand nombre de filtres et de plug-ins que l'on ne trouve
que dans les logiciels commerciaux haut de gamme ainsi que de
nombreuses fonctionnalité inédites.

GIMP fournit une boite à outil permettant de gérer plusieurs calques,
de nombreux effets, l'anti-aliasing, les conversions de fichiers ainsi
qu'un grand nombre de niveaux d'annulation.

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
License:	LGPL
Requires:	%{name} = %{version}
Requires:	gtk+-devel >= 1.2.0

%description devel
Header files for writing GIMP plugins and extensions.

%description -l de devel
Header-Dateien zum Schreiben von GIMP-Plugins und -Erweiterungen.

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

%package aa
Summary:	ASCII Art plugin for Gimp
Summary(fr):	Plugin d'art ASCII pour Gimp
Group:		X11/Applications/Graphics
Group(fr):	X11/Applications/Graphismes
Group(pl):	X11/Aplikacje/Grafika
Requires:	%{name} = %{version}

%description aa
This package contains the ASCII Art plugin which requires the aalib
shared library.

%description aa -l fr
Ce paquet contient le plugin d'art ASCII qui nécéssite la librairie
partagée aalib.

%package xd
Summary:	Xdelta plugin for GIMP
Summary(fr):	Plugin Xdelta pour GIMP
Group:		X11/Applications/Graphics
Group(fr):	X11/Applications/Graphismes
Group(pl):	X11/Aplikacje/Grafika
Requires:	%{name} = %{version}

%description xd
This package contains the Xdelta plugin which requires the xdelta
shared library.

%description -l fr xd
Ce paquet contient le plugin Xdelta qui nécéssite la librairie
partagée xdelta.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

chmod +x find-perl-requires

%build
CFLAGS="$RPM_OPT_FLAGS -DPERL_POLLUTE"; export CFLAGS
%configure \
	--without-included-gettext \
	--without-xdelta \
	--enable-perl \
	--enable-python \
	--with-mp \
	--with-threads=posix 
%{__make}
%{__make} -C plug-ins/perl/po update-gmo

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/icons \
	$RPM_BUILD_ROOT%{_applnkdir}/Graphics

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

install pixmaps/*.xpm $RPM_BUILD_ROOT%{_datadir}/icons/
install plug-ins/*/*.xpm $RPM_BUILD_ROOT%{_datadir}/icons/

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics
mv $RPM_BUILD_ROOT/usr/bin/* $RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT/usr/share/man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf ChangeLog NEWS README README.i18n README.perl \
	TODO MAINTAINERS docs/*.txt

%find_lang %{name} --all-name

echo "%defattr(755,root,root,755)" >> %{name}.lang

ls -1 $RPM_BUILD_ROOT%{_libdir}/gimp/1.1/plug-ins/* | \
	egrep -w -v -e "aa|xd" | \
	sed -e s#^`echo $RPM_BUILD_ROOT`## >> %{name}.lang
	
echo "%defattr(644,root,root,755)" >> %{name}.lang

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {ChangeLog,NEWS,README,README.i18n,README.perl,MAINTAINERS}.gz
%doc docs/*.gz docs/*README
%doc docs/quick_reference.*

%attr(755,root,root) %{_bindir}/gimp* 
%{_applnkdir}/Graphics/gimp.desktop

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
%dir %{_datadir}/gimp/1.1
%{_datadir}/gimp/1.1/brushes
%{_datadir}/gimp/1.1/fractalexplorer
%{_datadir}/gimp/1.1/gfig
%{_datadir}/gimp/1.1/gflare
%{_datadir}/gimp/1.1/gimpressionist
%{_datadir}/gimp/1.1/gradients
%{_datadir}/gimp/1.1/help
%{_datadir}/gimp/1.1/palettes
%{_datadir}/gimp/1.1/patterns
%{_datadir}/gimp/1.1/scripts
%{_datadir}/gimp/1.1/*.ppm

%dir %{_datadir}/gimp/1.1/tips
%{_datadir}/gimp/1.1/tips/gimp_tips.txt
%lang(fr) %{_datadir}/gimp/1.1/tips/gimp_conseils.fr.txt
%lang(cs) %{_datadir}/gimp/1.1/tips/gimp_tips.cs.txt
%lang(de) %{_datadir}/gimp/1.1/tips/gimp_tips.de.txt
%lang(it) %{_datadir}/gimp/1.1/tips/gimp_tips.it.txt
%lang(ja) %{_datadir}/gimp/1.1/tips/gimp_tips.ja.txt
%lang(ko) %{_datadir}/gimp/1.1/tips/gimp_tips.ko.txt
%lang(pl) %{_datadir}/gimp/1.1/tips/gimp_tips.pl.txt
%lang(ru) %{_datadir}/gimp/1.1/tips/gimp_tips.ru.txt

%config %verify(not md5 mtime) %{_sysconfdir}/gimp/1.1/gimprc*
%config %{_sysconfdir}/gimp/1.1/gtkrc*
%config %{_sysconfdir}/gimp/1.1/ps-menurc
%config %{_sysconfdir}/gimp/1.1/unitrc

%attr(755,root,root) %{_datadir}/gimp/1.1/user_install

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
%{_aclocaldir}/gimp.m4

%attr(755,root,root) %{_bindir}/embedxpm
%attr(755,root,root) %{_bindir}/gimpdoc
%attr(755,root,root) %{_bindir}/scm2perl
%attr(755,root,root) %{_bindir}/scm2scm
%attr(755,root,root) %{_bindir}/xcftopnm

%{_mandir}/man1/gimptool.1*
%{_mandir}/man1/embedxpm.1*
%{_mandir}/man1/scm2perl.1*
%{_mandir}/man1/scm2scm.1*
%{_mandir}/man1/xcftopnm.1*
/usr/share/man/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files aa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gimp/1.1/plug-ins/aa

#%files xd
#%attr(755,root,root) %{_libdir}/gimp/1.1/plug-ins/xd
