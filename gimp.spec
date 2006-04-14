#
# Conditional build:
%bcond_without	aalib		# without aa plugin (which requires aalib)
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	print		# without print plugin (which requires gimp-print 4.2.x)
%bcond_without	python		# without python plugins
%bcond_with	posix_shm	# with POSIX SHM (default is SysV SHM)
%bcond_without	static_libs	# do not build static libraries
#
%define	mver	2.0
Summary:	The GNU Image Manipulation Program
Summary(de):	Das GNU-Bildbearbeitungs-Programm
Summary(es):	Programa de manipulación de imagen GNU
Summary(fr):	Le programme de manipulation d'images de GNU
Summary(pl):	Program GNU do manipulacji formatami graficznymi (GIMP)
Summary(pt_BR):	Programa de manipulação de imagem GNU
Summary(ru):	The GNU Image Manipulation Program
Summary(tr):	Çizim, boyama ve görüntü iþleme programý
Summary(uk):	The GNU Image Manipulation Program
Summary(zh_CN):	[Í¼Ïñ]GNUÍ¼Ïó´¦Àí¹¤¾ß
Summary(zh_TW):	[¹Ï¹³]GNU¹Ï¶H³B²z¤u¨ã
Name:		gimp
Version:	2.2.11
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.gimp.org/pub/gimp/v2.2/%{name}-%{version}.tar.bz2
# Source0-md5:	0403e9b4e0415c99cd27b137b9839212
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.gimp.org/
%{?with_aalib:BuildRequires:	aalib-devel}
BuildRequires:	alsa-lib-devel >= 1.0.0
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	gettext-devel
%{?with_print:BuildRequires:	gimp-print-devel < 4.3.0}
%{?with_print:BuildRequires:	gimp-print-devel >= 4.2.6}
BuildRequires:	gtk+2-devel >= 2:2.4.4
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.0}
BuildRequires:	intltool
BuildRequires:	lcms-devel
BuildRequires:	libart_lgpl-devel
BuildRequires:	libexif-devel
BuildRequires:	libgtkhtml-devel >= 2.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	librsvg-devel >= 2.2.0
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	libungif-devel
BuildRequires:	libwmf-devel >= 2:0.2.8
BuildRequires:	pkgconfig
%{?with_python:BuildRequires:	python-pygtk-devel >= 1.99.15}
%{?with_python:BuildRequires:	rpm-pythonprov}
Requires:	gtk+2 >= 2:2.4.4
%{?with_python:Requires:	python-pygtk-gtk >= 1.99.15}
Obsoletes:	gimp-data-min
Obsoletes:	gimp-libgimp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
FTP site has a package of fonts that you can install by yourself,
which includes all the fonts needed to run the included scripts.

%description -l es
GIMP es un programa de manejo de imágenes adecuado para retoque de
fotos, composición y editoración de imágenes. Muchas personas lo
encuentran extremamente útil en la creación de logos y otros gráficos
para páginas web. GIMP tiene muchas herramientas y filtros normalmente
encontrados en aplicaciones comerciales similares, además de
características extras bien interesantes. GIMP ofrece una extensa caja
de herramientas de manejo de imagen, incluyendo camadas, efectos,
formación de imagen subpíxel y antialiasing, conversiones, todos con
deshacer en varios niveles (multi-level undo).

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
Program GIMP jest przeznaczony do obróbki i tworzenia plików w ró¿nych
formatach graficznych. Przy jego u¿yciu mo¿na tworzyæ grafikê dla
stron WWW, retuszowaæ zdjêcia, czy stworzyæ w³asne logo.

GIMP dostarcza du¿y zestaw narzêdzi do obróbki obrazów, w tym do
operowania na kana³ach i warstwach, efektów, antyaliasingu oraz
konwersji, a to wszystko z wielopoziomowym cofaniem operacji.

%description -l pt_BR
O GIMP é um programa de manipulação de imagens adequado para retoque
de fotos, composição e editoração de imagens. Muitas pessoas o acham
extremamente útil na criação de logos e outros gráficos para páginas
web. O GIMP tem muitas ferramentas e filtros normalmente encontrados
em aplicações comerciais similares, além de características extras bem
interessantes.

O GIMP fornece uma extensa caixa de ferramentas de manipulação de
imagem, incluindo camadas, efeitos, formação de imagem subpíxel e
anti-aliasing, conversões, todos com desfazimento em vários níveis
(multi-level undo).

%description -l ru
GIMP - ÜÔÏ ÐÒÏÇÒÁÍÍÁ ÄÌÑ ÓÏÚÄÁÎÉÑ É ÏÂÒÁÂÏÔËÉ ÉÚÏÂÒÁÖÅÎÉÊ. åÅ ÓÞÉÔÁÀÔ
ÉÓËÌÀÞÉÔÅÌØÎÏ ÐÏÌÅÚÎÏÊ ÄÌÑ ÓÏÚÄÁÎÉÑ ÌÏÇÏÔÉÐÏ× É ÄÒÕÇÏÊ ÇÒÁÆÉËÉ ÄÌÑ
web-ÓÔÒÁÎÉÃ. GIMP ÉÍÅÅÔ ÍÎÏÖÅÓÔ×Ï ÉÎÓÔÒÕÍÅÎÔÏ× É ÆÉÌØÔÒÏ×, ËÏÔÏÒÙÅ
ÏÂÙÞÎÏ ×ËÌÀÞÁÀÔÓÑ × ÁÎÁÌÏÇÉÞÎÙÅ ËÏÍÍÅÒÞÅÓËÉÅ ÐÁËÅÔÙ, Á ÔÁËÖÅ ÒÑÄ
×ÏÚÍÏÖÎÏÓÔÅÊ, ÐÒÉÓÕÝÉÈ ÔÏÌØËÏ ÅÊ.

GIMP ÐÒÅÄÏÓÔÁ×ÌÑÅÔ ÂÏÌØÛÏÊ ÎÁÂÏÒ ÉÎÓÔÒÕÍÅÎÔÏ× ÄÌÑ ÒÁÂÏÔÙ Ó ÇÒÁÆÉËÏÊ,
×ËÌÀÞÁÀÝÉÊ ÏÐÅÒÁÃÉÉ ÎÁÄ ËÁÎÁÌÁÍÉ, ÓÌÏÑÍÉ, ÜÆÆÅËÔÙ, sub-pixel imaging É
ÁÎÔÉÁÌÉÁÓÉÎÇ, ×ÓÑÞÅÓËÉÅ ËÏÎ×ÅÒÔÏÒÙ É ×ÓÅ ÜÔÏ Ó ÍÎÏÇÏÕÒÏ×ÎÅ×ÙÍ ÏÔËÁÔÏÍ.

GIMP ×ËÌÀÞÁÅÔ ÐÏÄÄÅÒÖËÕ ÓÏÚÄÁÎÉÑ ÓÃÅÎÁÒÉÅ× (scripting facility),
ÏÄÎÁËÏ ÍÎÏÇÉÅ ÉÚ ÐÏÓÔÁ×ÌÑÅÍÙÈ Ó ÐÒÏÇÒÁÍÍÏÊ ÓÃÅÎÁÒÉÅ× ÐÒÅÄÐÏÌÁÇÁÀÔ
ÎÁÌÉÞÉÅ ÛÒÉÆÔÏ×, ËÏÔÏÒÙÅ ÎÅ ÍÏÇÕÔ ÂÙÔØ ×ËÌÀÞÅÎÙ × ÄÉÓÔÒÉÂÕÔÉ×.
FTP-ÓÁÊÔ GIMP ÓÏÄÅÒÖÉÔ ÐÁËÅÔ ÛÒÉÆÔÏ×, ËÏÔÏÒÙÅ ×Ù ÍÏÖÅÔÅ ÐÏÓÔÁ×ÉÔØ
ÓÁÍÏÓÔÏÑÔÅÌØÎÏ, ×ËÌÀÞÁÀÝÉÊ ×ÓÅ ÛÒÉÆÔÙ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÒÁÂÏÔÙ ×ÈÏÄÑÝÉÈ
× ËÏÍÐÌÅËÔ ÓÃÅÎÁÒÉÅ×. îÅËÏÔÏÒÙÅ ÉÚ ÛÒÉÆÔÏ× ÉÍÅÀÔ ×ÅÓØÍÁ ÎÅÏÂÙÞÎÙÅ
ÌÉÃÅÎÚÉÏÎÎÙÅ ÔÒÅÂÏ×ÁÎÉÑ; ×ÓÅ ÌÉÃÅÎÚÉÉ ×ËÌÀÞÅÎÙ × ÕÐÏÍÑÎÕÔÙÊ ÐÁËÅÔ.
óËÁÞÁÊÔÅ ftp://ftp.gimp.org/pub/gimp/fonts/freefonts-0.10.tar.gz É
ftp://ftp.gimp.org/pub/gimp/fonts/sharefonts-0.10.tar.gz, ÅÓÌÉ ÈÏÔÉÔÅ
ÚÁÐÕÓËÁÔØ ÓÃÅÎÁÒÉÉ ÂÅÚ ÉÚÍÅÎÅÎÉÊ ÉÌÉ ×ÙÂÅÒÉÔÅ ÔÅ ÛÒÉÆÔÙ, ËÏÔÏÒÙÅ
ÕÓÔÁÎÏ×ÌÅÎÙ Õ ×ÁÓ × ÓÉÓÔÅÍÅ, ÐÅÒÅÄ ÚÁÐÕÓËÏÍ ÓÃÅÎÁÒÉÅ×.

%description -l uk
GIMP - ÃÅ ÐÒÏÇÒÁÍÁ ÄÌÑ ÓÔ×ÏÒÅÎÎÑ ÔÁ ÏÂÒÏÂËÉ ÚÏÂÒÁÖÅÎØ. ·§ ××ÁÖÁÀÔØ
ÄÕÖÅ ËÏÒÉÓÎÏÀ ÄÌÑ ÓÔ×ÏÒÅÎÎÑ ÌÏÇÏÔÉÐ¦× ÔÁ ¦ÎÛÏ§ ÇÒÁÆ¦ËÉ ÄÌÑ
web-ÓÔÏÒ¦ÎÏË. GIMP ÍÁ¤ ÂÁÇÁÔÏ ¦ÎÓÔÒÕÍÅÎÔ¦× ÔÁ Æ¦ÌØÔÒ¦×, ÑË¦ Ú×ÉÞÁÊÎÏ
×ËÌÀÞÁÀÔØÓÑ × ÁÎÁÌÏÇ¦ÞÎ¦ ËÏÍÅÒÃ¦ÊÎ¦ ÐÁËÅÔÉ, Á ÔÁËÏÖ ÒÑÄ ÍÏÖÌÉ×ÏÓÔÅÊ,
×ÌÁÓÔÉ×ÉÈ ÓÁÍÅ §Ê.

GIMP ÎÁÄÁ¤ ×ÅÌÉËÉÊ ÎÁÂ¦Ò ¦ÎÓÔÒÕÍÅÎÔ¦× ÄÌÑ ÒÏÂÏÔÉ Ú ÇÒÁÆ¦ËÏÀ, ÝÏ
×ËÌÀÞÁ¤ ÏÐÅÒÁÃ¦§ ÎÁÄ ËÁÎÁÌÁÍÉ, ÛÁÒÁÍÉ (layers), ÅÆÅËÔÉ, sub-pixel
imaging ¦ ÁÎÔÉÁÌ¦ÁÓÉÎÇ, Ò¦ÚÎÏÍÁÎ¦ÔÎ¦ ËÏÎ×ÅÒÔÏÒÉ ¦ ×ÓÅ ÃÅ Ú
ÂÁÇÁÔÏÒ¦×ÎÅ×ÉÍ ×¦ÄËÁÔÏÍ.

GIMP ÍÁ¤ Ð¦ÄÔÒÉÍËÕ ÓÃÅÎÁÒ¦§× (scripting facility), ÐÒÏÔÅ ÂÁÇÁÔÏ Ú
×ËÌÀÞÅÎÉÈ ÄÏ ÐÏÓÔÁ×ËÉ ÓÃÅÎÁÒ¦§× ÐÒÉÐÕÓËÁÀÔØ ÎÁÑ×Î¦ÓÔØ ÛÒÉÆÔ¦×, ÑË¦ ÎÅ
ÍÏÖÕÔØ ÂÕÔÉ ×ËÌÀÞÅÎ¦ × ÄÉÓÔÒÉÂÕÔÉ×. FTP-ÓÁÊÔ GIMP Í¦ÓÔÉÔØ ÐÁËÅÔ
ÛÒÉÆÔ¦×, ËÏÔÒ¦ ×É ÍÏÖÅÔÅ ×ÓÔÁÎÏ×ÉÔÉ ÓÁÍÏÓÔ¦ÊÎÏ, × ÑËÉÊ ×ÈÏÄÑÔØ ×Ó¦
ÛÒÉÆÔÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÒÏÂÏÔÉ ÓÃÅÎÁÒ¦§× Ú ÐÏÓÔÁ×ËÉ GIMP. äÅÑË¦ Ú
ÛÒÉÆÔ¦× ÍÁÀÔØ ×ÅÌØÍÉ ÎÅÚ×ÉÞÁÊÎ¦ Ì¦ÃÅÎÚ¦ÊÎ¦ ÕÍÏ×É; ×Ó¦ Ì¦ÃÅÎÚ¦§
×ËÌÀÞÅÎÏ × ÚÇÁÄÁÎÉÊ ÐÁËÅÔ. úÁ×ÁÎÔÁÖÔÅ
ftp://ftp.gimp.org/pub/gimp/fonts/freefonts-0.10.tar.gz ÔÁ
ftp://ftp.gimp.org/pub/gimp/fonts/sharefonts-0.10.tar.gz. ÑËÝÏ ÈÏÞÅÔÅ
ÚÁÐÕÓËÁÔÉ ÓÃÅÎÁÒ¦§ ÂÅÚ ÚÍ¦Î ÁÂÏ Ö ×ÉÂÅÒ¦ÔØ ×ÓÔÁÎÏ×ÁÌÅÎ¦ Õ ×ÁÓ ×
ÓÉÓÔÅÍ¦ ÛÒÉÆÔÉ ÐÅÒÅÄ ÚÁÐÕÓËÏÍ ÓÃÅÎÁÒ¦§×.

%package devel
Summary:	GIMP plugin and extension development kit
Summary(de):	GIMP-Plugin und Extension Development Kit
Summary(es):	Kit de desarrollo de "plugins" extensiones para GIMP
Summary(fr):	Plugin GIMP et kit de développement d'extensions
Summary(pl):	Pliki do budowania modu³ów i rozszerzeñ dla Gimpa
Summary(pt_BR):	Kit de desenvolvimento de "plugins" extensões para o GIMP
Summary(ru):	éÎÓÔÒÕÍÅÎÔÁÒÉÊ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÌÁÇÉÎÏ× É ÒÁÓÛÉÒÅÎÉÊ GIMP
Summary(tr):	GIMP plugin ve uzantý geliþtirme araçlarý
Summary(uk):	¶ÎÓÔÒÕÍÅÎÔÁÒ¦Ê ÄÌÑ ÒÏÚÒÏÂËÉ ÐÌÁÇ¦Î¦× ÔÁ ÒÏÚÛÉÒÅÎØ GIMP
Summary(zh_CN):	[¿ª·¢]gimpµÄ¿ª·¢°ü
Summary(zh_TW):	[¶}µo]gimpªº¶}µo¥]
License:	LGPL
Group:		X11/Development/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gtk+2-devel >= 2:2.4.4
Requires:	gtk-doc-common

%description devel
Header files for writing GIMP plugins and extensions.

%description devel -l de
Header-Dateien zum Schreiben von GIMP-Plugins und -Erweiterungen.

%description devel -l es
Bibliotecas y archivos de inclusión para escribir extensiones y
plugins para Gimp.

%description devel -l pl
Pliki nag³ówkowe do tworzenia wtyczek i rozszerzeñ dla Gimpa.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusão para escrever extensões e plugins
para o Gimp.

%package static
Summary:	GIMP static libraries
Summary(pl):	Biblioteki statyczne Gimpa
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
GIMP static libraries.

%description static -l es
Bibliotecas estáticas para escribir extensiones y plugins para Gimp.

%description static -l pl
Biblioteki statyczne Gimpa.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento de plugins e extensões do
GIMP.

%package aa
Summary:	ASCII Art plugin for Gimp
Summary(fr):	Plugin d'art ASCII pour Gimp
Summary(pl):	Wtyczka do ASCII Art do Gimpa
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description aa
This package contains the ASCII Art plugin which requires the aalib
shared library.

%description aa -l fr
Ce paquet contient le plugin d'art ASCII qui nécéssite la librairie
partagée aalib.

%description aa -l pl
Ten pakiet zawiera wtyczkê do Gimpa ze wsparciem do ASCII Art.

%package print
Summary:	Print plugin for Gimp
Summary(pl):	Wtyczka do drukowania dla Gimpa
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gimp-print-lib >= 4.2.6

%description print
Print plugin for Gimp.

%description print -l pl
Wtyczka do drukowania dla Gimpa.

%package svg
Summary:	SVG plugin for Gimp
Summary(pl):	Wtyczka SVG dla Gimpa
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	librsvg >= 2.2.0

%description svg
SVG plugin for Gimp.

%description svg -l pl
Wtyczka SVG dla Gimpa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

#cp /usr/share/automake/py-compile plug-ins/pygimp

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	%{!?with_print: --disable-print} \
	--disable-rpath \
	--enable-default-binary \
	%{?with_apidocs:--enable-gtk-doc} \
	--enable-mp \
	%{?with_python: --enable-python} \
	%{?with_static_libs:--enable-static} \
	--with-html-dir=%{_gtkdocdir} \
	%{?with_posix_shm:--with-shm=posix}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#########################################################
# This is hack indeed, but it was supposed to disappear #
# when version 2.0 will arrive but it doesn't :(        #
#########################################################

cat $RPM_BUILD_ROOT%{_datadir}/gimp/%{mver}/misc/gimp.desktop | \
	sed 's@/usr/share/gimp/%{mver}/images/@@' > \
	$RPM_BUILD_ROOT%{_desktopdir}/gimp.desktop
install data/images/wilber-icon.png $RPM_BUILD_ROOT%{_pixmapsdir}

################### end hack ############################

# Link gimptool to gimptool-2.0

ln -s gimptool-%{mver} $RPM_BUILD_ROOT%{_bindir}/gimptool
echo '.so gimptool-%{mver}' > $RPM_BUILD_ROOT%{_mandir}/man1/gimptool.1

# Remove obsolete files
rm -f $RPM_BUILD_ROOT%{_libdir}/gimp/%{mver}/modules/*.{a,la}
rm -f $RPM_BUILD_ROOT%{_libdir}/gimp/%{mver}/python/*.{a,la,py}
rm -f $RPM_BUILD_ROOT%{_datadir}/gimp/%{mver}/misc/gimp.{applications,desktop,keys}
rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
/sbin/ldconfig
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
umask 022
/sbin/ldconfig
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%doc docs/{*.txt,quick_reference.*,Wilber*}

%attr(755,root,root) %{_bindir}/gimp-2.2
%attr(755,root,root) %{_bindir}/gimp
%attr(755,root,root) %{_bindir}/gimp-remote-2.2
%attr(755,root,root) %{_bindir}/gimp-remote
%{_desktopdir}/gimp.desktop
%{_mandir}/man1/gimp-2*
%{_mandir}/man1/gimp-remote-2*
%{_mandir}/man5/gimprc-2*

%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/gimp
%dir %{_libdir}/gimp/%{mver}
%dir %{_libdir}/gimp/%{mver}/plug-ins
%attr(755,root,root) %{_libdir}/gimp/%{mver}/plug-ins/*
%{?with_aalib:%exclude %{_libdir}/gimp/%{mver}/plug-ins/aa}
%{?with_print:%exclude %{_libdir}/gimp/%{mver}/plug-ins/print}
%exclude %{_libdir}/gimp/%{mver}/plug-ins/svg

%dir %{_libdir}/gimp/%{mver}/modules
%attr(755,root,root) %{_libdir}/gimp/%{mver}/modules/*.so
%{_libdir}/gimp/%{mver}/environ

%if %{with python}
%dir %{_libdir}/gimp/%{mver}/python
%{_libdir}/gimp/%{mver}/python/*.py[co]
%{_libdir}/gimp/%{mver}/python/*.png
%attr(755,root,root) %{_libdir}/gimp/%{mver}/python/*.so
%endif

%dir %{_datadir}/gimp
%dir %{_datadir}/gimp/%{mver}
%{_datadir}/gimp/%{mver}/brushes
%{_datadir}/gimp/%{mver}/fractalexplorer
%{_datadir}/gimp/%{mver}/gfig
%{_datadir}/gimp/%{mver}/gflare
%{_datadir}/gimp/%{mver}/gimpressionist
%{_datadir}/gimp/%{mver}/gradients
%{_datadir}/gimp/%{mver}/images
%{_datadir}/gimp/%{mver}/menus
%{_datadir}/gimp/%{mver}/palettes
%{_datadir}/gimp/%{mver}/patterns
%{_datadir}/gimp/%{mver}/scripts
%{_datadir}/gimp/%{mver}/themes
%{_datadir}/gimp/%{mver}/tips
%dir %{_datadir}/gimp/%{mver}/misc

%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/%{mver}
%config %verify(not md5 mtime) %{_sysconfdir}/%{name}/%{mver}/gimprc*
%config(noreplace) %{_sysconfdir}/%{name}/%{mver}/templaterc
%config %{_sysconfdir}/%{name}/%{mver}/gtkrc*
%config %{_sysconfdir}/%{name}/%{mver}/ps-menurc
%config %{_sysconfdir}/%{name}/%{mver}/sessionrc
%config %{_sysconfdir}/%{name}/%{mver}/unitrc
%config %{_sysconfdir}/%{name}/%{mver}/controllerrc

%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gimptool-%{mver}
%attr(755,root,root) %{_bindir}/gimptool
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*
%{_gtkdocdir}/*

%{_includedir}/gimp-2.0
%{_aclocaldir}/gimp-2.0.m4

%{_mandir}/man1/gimptool-%{mver}*
%{_mandir}/man1/gimptool.1*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif

%if %{with aalib}
%files aa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gimp/%{mver}/plug-ins/aa
%endif

%if %{with print}
%files print
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gimp/%{mver}/plug-ins/print
%endif

%files svg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gimp/%{mver}/plug-ins/svg
