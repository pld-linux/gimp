%include	/usr/lib/rpm/macros.perl
Summary:	The GNU Image Manipulation Program
Summary(de):	Das GNU-Bildbearbeitungs-Programm
Summary(es):	Programa de manipulaci�n de imagen GNU
Summary(fr):	Le programme de manipulation d'images de GNU
Summary(pl):	Program GNU do manipulacji formatami graficznymi (GIMP)
Summary(pt_BR):	Programa de manipula��o de imagem GNU
Summary(tr):	�izim, boyama ve g�r�nt� i�leme program�
Name:		gimp
Version:	1.2.3
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.gimp.org/pub/gimp/v1.2/v%{version}/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Patch0:		%{name}-perldep.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-croak.patch
URL:		http://www.gimp.org/
Icon:		gimp.gif
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.8-3
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-PDL-Graphics-TriD >= 1.9906
BuildRequires:	perl-PDL-Graphics-PGPLOT >= 1.9906
BuildRequires:	perl-gtk >= 0.6123
BuildRequires:	perl-Parse-RecDescent
BuildRequires:	perl-File-Slurp
BuildRequires:	libtiff-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libungif-devel
BuildRequires:	aalib-devel
BuildRequires:	mpeg_lib-devel
BuildRequires:	rpm-perlprov
Requires:	gtk+ >= 1.2.8-3
Requires:	mpeg_lib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gimp-data-min
Obsoletes:	gimp-libgimp

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

# need libmpeg.so from mpeg_lib (xmps has other libmpeg.so)
%define		_noautoreqdep	libmpeg.so
# workaround for find-perl-requires
%define		_noautoreq	"perl(of)"

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
GIMP es un programa de manejo de im�genes adecuado para retoque de
fotos, composici�n y editoraci�n de im�genes. Muchas personas lo
encuentran extremamente �til en la creaci�n de logos y otros gr�ficos
para p�ginas web. GIMP tiene muchas herramientas y filtros normalmente
encontrados en aplicaciones comerciales similares, adem�s de
caracter�sticas extras bien interesantes. GIMP ofrece una extensa caja
de herramientas de manejo de imagen, incluyendo camadas, efectos,
formaci�n de imagen subp�xel y antialiasing, conversiones, todos con
deshacer en varios niveles (multi-level undo).

%description -l fr
Le Programme de Manipulation d'Image de GNU permet de retoucher des
photos, de r�aliser des compositions. Beaucoup de gens l'appr�cient
pour la cr�ation de logos et de graphismes pour les pages web. GIMP
dispose d'un grand nombre de filtres et de plug-ins que l'on ne trouve
que dans les logiciels commerciaux haut de gamme ainsi que de
nombreuses fonctionnalit� in�dites.

GIMP fournit une boite � outil permettant de g�rer plusieurs calques,
de nombreux effets, l'anti-aliasing, les conversions de fichiers ainsi
qu'un grand nombre de niveaux d'annulation.

%description -l pt_BR
O GIMP � um programa de manipula��o de imagens adequado para retoque
de fotos, composi��o e editora��o de imagens. Muitas pessoas o acham
extremamente �til na cria��o de logos e outros gr�ficos para p�ginas
web. O GIMP tem muitas ferramentas e filtros normalmente encontrados
em aplica��es comerciais similares, al�m de caracter�sticas extras bem
interessantes.

O GIMP fornece uma extensa caixa de ferramentas de manipula��o de
imagem, incluindo camadas, efeitos, forma��o de imagem subp�xel e
anti-aliasing, convers�es, todos com desfazimento em v�rios n�veis
(multi-level undo).

%description -l pl
Program Gimp jest przeznaczony do obr�bki i tworzenia plik�w w r�nych
formatach graficznych. Dzi�ki niemu b�dziesz m�g� stworzy� grafik� dla
stron WWW, przerobi� zdj�cia, czy stworzy� w�asne logo.

%package devel
Summary:	GIMP plugin and extension development kit
Summary(de):	GIMP-Plugin und Extension Development Kit
Summary(es):	Kit de desarrollo de "plugins" extensiones para GIMP
Summary(fr):	Plugin GIMP et kit de d�veloppement d'extensions
Summary(pl):	Pliki do budowania modu��w i rozszerze� dla Gimp
Summary(pt_BR):	Kit de desenvolvimento de "plugins" extens�es para o GIMP
Summary(tr):	GIMP plugin ve uzant� geli�tirme ara�lar�
License:	LGPL
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtk+-devel >= 1.2.0

%description devel
Header files for writing GIMP plugins and extensions.

%description devel -l de
Header-Dateien zum Schreiben von GIMP-Plugins und -Erweiterungen.

%description devel -l es
Bibliotecas y archivos de inclusi�n para escribir extensiones y
plugins para Gimp.

%description devel -l pl
Pliki nag��wkowe dla GIMP.

%description devel -l pt_BR
Bibliotecas e arquivos de inclus�o para escrever extens�es e plugins
para o Gimp.

%description devel -l es
Bibliotecas y archivos de inclusi�n para escribir extensiones y
plugins para Gimp.

%package static
Summary:	GIMP static libraries
Summary(pl):	Biblioteki statyczne do GIMPa
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
GIMP static libraries.

%description static -l es
Bibliotecas est�ticas para escribir extensiones y plugins para Gimp.

%description static -l pl
Biblioteki statyczne do GIMPa.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento de plugins e extens�es do
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
Ce paquet contient le plugin d'art ASCII qui n�c�ssite la librairie
partag�e aalib.

%description aa -l pl
Ten pakiet zawiera wtyczk� do Gimpa ze wsparciem do ASCII Art.

%package mpeg
Summary:	MPEG plugin for Gimp
Summary(pl):	Wtyczka do MPEG Gimpa
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}

%description mpeg
This package contains the MPEG plugin.

%description mpeg -l pl
Ten pakiet zawiera wtyczk� do Gimpa ze wsparciem do MPEG.

%prep
%setup	-q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
CFLAGS="%{rpmcflags} -DPERL_POLLUTE"
%configure2_13 \
	--without-included-gettext \
	--enable-perl \
	--with-mp \
	--with-threads=posix
%{__make}
%{__make} -C plug-ins/perl/po update-gmo

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

gzip -9nf ChangeLog NEWS README README.i18n README.perl \
	TODO MAINTAINERS docs/*.txt

%find_lang %{name} --all-name

echo "%defattr(755,root,root,755)" >> %{name}.lang

ls -1 $RPM_BUILD_ROOT%{_libdir}/gimp/1.2/plug-ins/* | \
	egrep -w -v -e "aa|mpeg|print" | \
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
%doc {ChangeLog,NEWS,README,README.i18n,README.perl,MAINTAINERS}.gz
%doc docs/*.gz docs/*README
%doc docs/quick_reference.*

%attr(755,root,root) %{_bindir}/gimp
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
%lang(fr) %{_datadir}/gimp/1.2/tips/gimp_conseils.fr.txt
%lang(cs) %{_datadir}/gimp/1.2/tips/gimp_tips.cs.txt
%lang(de) %{_datadir}/gimp/1.2/tips/gimp_tips.de.txt
%lang(it) %{_datadir}/gimp/1.2/tips/gimp_tips.it.txt
%lang(ja) %{_datadir}/gimp/1.2/tips/gimp_tips.ja.txt
%lang(ko) %{_datadir}/gimp/1.2/tips/gimp_tips.ko.txt
%lang(pl) %{_datadir}/gimp/1.2/tips/gimp_tips.pl.txt
%lang(ru) %{_datadir}/gimp/1.2/tips/gimp_tips.ru.txt
%lang(uk) %{_datadir}/gimp/1.2/tips/gimp_tips.uk.txt

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
%attr(755,root,root) %{_bindir}/gimp-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/gimp/1.2/modules/*.la

%{_includedir}/gck
%{_includedir}/libgimp
%{_aclocaldir}/gimp.m4

%attr(755,root,root) %{_bindir}/embedxpm
%attr(755,root,root) %{_bindir}/gimpdoc
%attr(755,root,root) %{_bindir}/scm2perl
%attr(755,root,root) %{_bindir}/scm2scm
%attr(755,root,root) %{_bindir}/xcftopnm

%{_mandir}/man1/gimptool-1.2.1*
%{_mandir}/man1/embedxpm.1*
%{_mandir}/man1/escputil-1.2.1*
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

%files mpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gimp/1.2/plug-ins/mpeg
