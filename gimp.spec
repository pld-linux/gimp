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
Version:	1.3.8
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.gimp.org/pub/gimp/v1.3/v%{version}/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
URL:		http://www.gimp.org/
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gimp-print-devel
BuildRequires:	libart_lgpl-devel
BuildRequires:	pkgconfig
BuildRequires:	libtiff-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libungif-devel
BuildRequires:	aalib-devel
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

%description -l pl
Program Gimp jest przeznaczony do obróbki i tworzenia plików w ró¿nych
formatach graficznych. Dziêki niemu bêdziesz móg³ stworzyæ grafikê dla
stron WWW, przerobiæ zdjêcia, czy stworzyæ w³asne logo.

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
ftp-ÓÁÊÔ GIMP ÓÏÄÅÒÖÉÔ ÐÁËÅÔ ÛÒÉÆÔÏ×, ËÏÔÏÒÙÅ ×Ù ÍÏÖÅÔÅ ÐÏÓÔÁ×ÉÔØ
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
ÍÏÖÕÔØ ÂÕÔÉ ×ËÌÀÞÅÎ¦ × ÄÉÓÔÒÉÂÕÔÉ×. ftp-ÓÁÊÔ GIMP Í¦ÓÔÉÔØ ÐÁËÅÔ
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
Summary(pl):	Pliki do budowania modu³ów i rozszerzeñ dla Gimp
Summary(pt_BR):	Kit de desenvolvimento de "plugins" extensões para o GIMP
Summary(ru):	éÎÓÔÒÕÍÅÎÔÁÒÉÊ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÌÁÇÉÎÏ× É ÒÁÓÛÉÒÅÎÉÊ GIMP
Summary(tr):	GIMP plugin ve uzantý geliþtirme araçlarý
Summary(uk):	¶ÎÓÔÒÕÍÅÎÔÁÒ¦Ê ÄÌÑ ÒÏÚÒÏÂËÉ ÐÌÁÇ¦Î¦× ÔÁ ÒÏÚÛÉÒÅÎØ GIMP
Summary(zh_CN):	[¿ª·¢]gimpµÄ¿ª·¢°ü
Summary(zh_TW):	[¶}µo]gimpªº¶}µo¥]
License:	LGPL
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtk+-devel >= 1.2.0

%description devel
Header files for writing GIMP plugins and extensions.

%description devel -l de
Header-Dateien zum Schreiben von GIMP-Plugins und -Erweiterungen.

%description devel -l es
Bibliotecas y archivos de inclusión para escribir extensiones y
plugins para Gimp.

%description devel -l pl
Pliki nag³ówkowe dla GIMP.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusão para escrever extensões e plugins
para o Gimp.

%description devel -l es
Bibliotecas y archivos de inclusión para escribir extensiones y
plugins para Gimp.

%package static
Summary:	GIMP static libraries
Summary(pl):	Biblioteki statyczne do GIMPa
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
GIMP static libraries.

%description static -l es
Bibliotecas estáticas para escribir extensiones y plugins para Gimp.

%description static -l pl
Biblioteki statyczne do GIMPa.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento de plugins e extensões do
GIMP.

%package aa
Summary:	ASCII Art plugin for Gimp
Summary(fr):	Plugin d'art ASCII pour Gimp
Summary(pl):	Wtyczka do ASCII Art do Gimpa
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}

%description aa
This package contains the ASCII Art plugin which requires the aalib
shared library.

%description aa -l fr
Ce paquet contient le plugin d'art ASCII qui nécéssite la librairie
partagée aalib.

%description aa -l pl
Ten pakiet zawiera wtyczkê do Gimpa ze wsparciem do ASCII Art.

%prep
%setup	-q

%build
%configure \
	--without-included-gettext \
	--enable-mp

%{__make}

exit 1
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir} \
	$RPM_BUILD_ROOT%{_applnkdir}/Graphics

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

install pixmaps/*.xpm plug-ins/*/*.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics
mv -f $RPM_BUILD_ROOT/usr/bin/* $RPM_BUILD_ROOT%{_bindir}
mv -f $RPM_BUILD_ROOT/usr/share/man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1

%find_lang %{name} --all-name

echo "%defattr(755,root,root,755)" >> %{name}.lang

ls -1 $RPM_BUILD_ROOT%{_libdir}/gimp/1.2/plug-ins/* | \
	egrep -w -v -e "aa|gap_decode_mpeg|mpeg|print" | \
	sed -e s#^`echo $RPM_BUILD_ROOT`## >> %{name}.lang

echo "%defattr(644,root,root,755)" >> %{name}.lang

rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/yes.xpm
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/no.xpm

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README README.i18n README.perl MAINTAINERS
%doc docs/*.txt docs/*README
%doc docs/quick_reference.*

%attr(755,root,root) %{_bindir}/gimp-1.2
%attr(755,root,root) %{_bindir}/gimp
%attr(755,root,root) %{_bindir}/gimp-remote-1.2
%attr(755,root,root) %{_bindir}/gimp-remote
%attr(755,root,root) %{_bindir}/gimpdoc
%{_applnkdir}/Graphics/gimp.desktop

%{_mandir}/man1/gimp-1.2.1*
%{_mandir}/man1/gimp-remote-1.2.1*
%{_mandir}/man5/gimprc-1.2.5*

%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/gimp
%dir %{_libdir}/gimp/1.2
%dir %{_libdir}/gimp/1.2/plug-ins
%dir %{_libdir}/gimp/1.2/modules
%attr(755,root,root) %{_libdir}/gimp/1.2/modules/*.so

%dir %{_datadir}/gimp
%dir %{_datadir}/gimp/1.2
%{_datadir}/gimp/1.2/brushes
%{_datadir}/gimp/1.2/fractalexplorer
%{_datadir}/gimp/1.2/gfig
%{_datadir}/gimp/1.2/gflare
%{_datadir}/gimp/1.2/gimpressionist
%{_datadir}/gimp/1.2/gradients
%{_datadir}/gimp/1.2/help
%{_datadir}/gimp/1.2/palettes
%{_datadir}/gimp/1.2/patterns
%{_datadir}/gimp/1.2/scripts
%{_datadir}/gimp/1.2/*.ppm

%dir %{_datadir}/gimp/1.2/tips
%{_datadir}/gimp/1.2/tips/gimp_tips.txt
%lang(cs) %{_datadir}/gimp/1.2/tips/gimp_tips.cs.txt
%lang(da) %{_datadir}/gimp/1.2/tips/gimp_tips.da.txt
%lang(de) %{_datadir}/gimp/1.2/tips/gimp_tips.de.txt
%lang(es) %{_datadir}/gimp/1.2/tips/gimp_tips.es.txt
%lang(fr) %{_datadir}/gimp/1.2/tips/gimp_conseils.fr.txt
%lang(hu) %{_datadir}/gimp/1.2/tips/gimp_tips.hu.txt
%lang(it) %{_datadir}/gimp/1.2/tips/gimp_tips.it.txt
%lang(ja) %{_datadir}/gimp/1.2/tips/gimp_tips.ja.txt
%lang(ko) %{_datadir}/gimp/1.2/tips/gimp_tips.ko.txt
%lang(lt) %{_datadir}/gimp/1.2/tips/gimp_tips.lt.txt
%lang(pl) %{_datadir}/gimp/1.2/tips/gimp_tips.pl.txt
%lang(ru) %{_datadir}/gimp/1.2/tips/gimp_tips.ru.txt
%lang(tr) %{_datadir}/gimp/1.2/tips/gimp_tips.tr.txt
%lang(uk) %{_datadir}/gimp/1.2/tips/gimp_tips.uk.txt
%lang(zh_CN) %{_datadir}/gimp/1.2/tips/gimp_tips.zh_CN.txt
%lang(zh_TW) %{_datadir}/gimp/1.2/tips/gimp_tips.zh_TW.txt

%dir %{_sysconfdir}/gimp
%dir %{_sysconfdir}/gimp/1.2
%config %verify(not md5 mtime) %{_sysconfdir}/gimp/1.2/gimprc*
%config %{_sysconfdir}/gimp/1.2/gtkrc*
%config %{_sysconfdir}/gimp/1.2/ps-menurc
%config %{_sysconfdir}/gimp/1.2/unitrc

%attr(755,root,root) %{_datadir}/gimp/1.2/user_install

%{_pixmapsdir}/*.xpm

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
%attr(755,root,root) %{_bindir}/gimptool-1.2
%attr(755,root,root) %{_bindir}/gimp-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/gimp/1.2/modules/*.la

%{_includedir}/gck
%{_includedir}/libgimp
%{_aclocaldir}/gimp.m4

%attr(755,root,root) %{_bindir}/embedxpm
%attr(755,root,root) %{_bindir}/scm2perl
%attr(755,root,root) %{_bindir}/scm2scm
%attr(755,root,root) %{_bindir}/xcftopnm

%{_mandir}/man1/gimptool-1.2.1*
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
%attr(755,root,root) %{_libdir}/gimp/1.2/plug-ins/aa
