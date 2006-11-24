#
# TODO: Build requires libselinux-devel but it's not catched by dependencies
#
# Conditional build:
%bcond_without	aalib		# without aa plugin (which requires aalib)
%bcond_without	gnome		# don't build GNOME based features
%bcond_without	python		# without python plugins
%bcond_with	posix_shm	# with POSIX SHM (default is SysV SHM)
#
%define	mver	2.0
Summary:	The GNU Image Manipulation Program
Summary(de):	Das GNU-Bildbearbeitungs-Programm
Summary(es):	Programa de manipulaci�n de imagen GNU
Summary(fr):	Le programme de manipulation d'images de GNU
Summary(pl):	Program GNU do manipulacji formatami graficznymi (GIMP)
Summary(pt_BR):	Programa de manipula��o de imagem GNU
Summary(ru):	The GNU Image Manipulation Program
Summary(tr):	�izim, boyama ve g�r�nt� i�leme program�
Summary(uk):	The GNU Image Manipulation Program
Summary(zh_CN):	[ͼ��]GNUͼ��������
Summary(zh_TW):	[�Ϲ�]GNU�϶H�B�z�u��
Name:		gimp
Version:	2.3.13
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.gimp.org/pub/gimp/v2.3/%{name}-%{version}.tar.bz2
# Source0-md5:	b150a726e1380ee0a6af342a9c0ebe80
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-gcc4.patch
Patch3:		%{name}-nognome.patch
URL:		http://www.gimp.org/
%{?with_aalib:BuildRequires:	aalib-devel}
BuildRequires:	alsa-lib-devel >= 1.0.11
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	intltool >= 0.35.0
BuildRequires:	lcms-devel
BuildRequires:	libart_lgpl-devel
BuildRequires:	libexif-devel
BuildRequires:	libgtkhtml-devel >= 2.6.3
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel
BuildRequires:	libpng-devel >= 1.2.12
BuildRequires:	librsvg-devel >= 1:2.15.0
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	libwmf-devel >= 2:0.2.8
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.5.3
BuildRequires:	rpm-pythonprov
BuildRequires:	xorg-lib-libXpm-devel
%{?with_python:BuildRequires:	python-pygtk-devel >= 1:2.9.3}
%if %{with gnome}
BuildRequires:	gnome-keyring-devel >= 0.5.1
BuildRequires:	gnome-vfs2-devel >= 2.15.91
BuildRequires:	libgnomeui-devel >= 2.15.91
%endif
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires(post,postun):  gtk+2 >= 2:2.10.0
Requires:	hicolor-icon-theme
%{?with_python:Requires:	python-pygtk-gtk >= 1:2.9.3}
Obsoletes:	gimp-data-min
Obsoletes:	gimp-libgimp
Obsoletes:	gimp-print
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

%description -l pl
Program GIMP jest przeznaczony do obr�bki i tworzenia plik�w w r�nych
formatach graficznych. Przy jego u�yciu mo�na tworzy� grafik� dla
stron WWW, retuszowa� zdj�cia, czy stworzy� w�asne logo.

GIMP dostarcza du�y zestaw narz�dzi do obr�bki obraz�w, w tym do
operowania na kana�ach i warstwach, efekt�w, antyaliasingu oraz
konwersji, a to wszystko z wielopoziomowym cofaniem operacji.

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

%description -l ru
GIMP - ��� ��������� ��� �������� � ��������� �����������. �� �������
������������� �������� ��� �������� ��������� � ������ ������� ���
web-�������. GIMP ����� ��������� ������������ � ��������, �������
������ ���������� � ����������� ������������ ������, � ����� ���
������������, �������� ������ ��.

GIMP ������������� ������� ����� ������������ ��� ������ � ��������,
���������� �������� ��� ��������, ������, �������, sub-pixel imaging �
������������, ��������� ���������� � ��� ��� � �������������� �������.

GIMP �������� ��������� �������� ��������� (scripting facility),
������ ������ �� ������������ � ���������� ��������� ������������
������� �������, ������� �� ����� ���� �������� � �����������.
FTP-���� GIMP �������� ����� �������, ������� �� ������ ���������
��������������, ���������� ��� ������, ����������� ��� ������ ��������
� �������� ���������. ��������� �� ������� ����� ������ ���������
������������ ����������; ��� �������� �������� � ���������� �����.
�������� ftp://ftp.gimp.org/pub/gimp/fonts/freefonts-0.10.tar.gz �
ftp://ftp.gimp.org/pub/gimp/fonts/sharefonts-0.10.tar.gz, ���� ������
��������� �������� ��� ��������� ��� �������� �� ������, �������
����������� � ��� � �������, ����� �������� ���������.

%description -l uk
GIMP - �� �������� ��� ��������� �� ������� ���������. �� ��������
���� �������� ��� ��������� ������Ц� �� ���ϧ ���Ʀ�� ���
web-���Ҧ���. GIMP ��� ������ ���������Ԧ� �� Ʀ���Ҧ�, �˦ ��������
����������� � �����Ǧ�Φ �����æ�Φ ������, � ����� ��� �����������,
��������� ���� ��.

GIMP ����� ������� ��¦� ���������Ԧ� ��� ������ � ���Ʀ���, ��
������� �����æ� ��� ��������, ������ (layers), ������, sub-pixel
imaging � �����̦�����, Ҧ�����Φ�Φ ���������� � ��� �� �
������Ҧ������ צ������.

GIMP ��� Ц������� �����Ҧ�� (scripting facility), ����� ������ �
��������� �� �������� �����Ҧ�� ����������� ����Φ��� ����Ԧ�, �˦ ��
������ ���� ������Φ � �����������. FTP-���� GIMP ͦ����� �����
����Ԧ�, ���Ҧ �� ������ ���������� �����Ԧ���, � ���� ������� �Ӧ
������, ����Ȧ�Φ ��� ������ �����Ҧ�� � �������� GIMP. ���˦ �
����Ԧ� ����� ������ ��������Φ ̦���ڦ�Φ �����; �Ӧ ̦���ڦ�
�������� � �������� �����. ����������
ftp://ftp.gimp.org/pub/gimp/fonts/freefonts-0.10.tar.gz ��
ftp://ftp.gimp.org/pub/gimp/fonts/sharefonts-0.10.tar.gz. ���� ������
��������� �����Ҧ� ��� �ͦ� ��� � ����Ҧ�� ����������Φ � ��� �
�����ͦ ������ ����� �������� �����Ҧ��.

%package libs
Summary:	GIMP libraries
Summary(pl):	Biblioteki GIMPa
Group:		Libraries
Requires:	gtk+2 >= 2:2.10.0

%description libs
This package contains GIMP libraries.

%description libs -l pl
Pakiet zawiera biblioteki GIMPa.

%package devel
Summary:	GIMP plugin and extension development kit
Summary(de):	GIMP-Plugin und Extension Development Kit
Summary(es):	Kit de desarrollo de "plugins" extensiones para GIMP
Summary(fr):	Plugin GIMP et kit de d�veloppement d'extensions
Summary(pl):	Pliki do budowania modu��w i rozszerze� dla Gimpa
Summary(pt_BR):	Kit de desenvolvimento de "plugins" extens�es para o GIMP
Summary(ru):	�������������� ��� ���������� �������� � ���������� GIMP
Summary(tr):	GIMP plugin ve uzant� geli�tirme ara�lar�
Summary(uk):	�����������Ҧ� ��� �������� ���ǦΦ� �� ��������� GIMP
Summary(zh_CN):	[����]gimp�Ŀ�����
Summary(zh_TW):	[�}�o]gimp���}�o�]
License:	LGPL
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	gtk-doc-common
Requires:	gtk+2-devel >= 2:2.10.0

%description devel
Header files for writing GIMP plugins and extensions.

%description devel -l de
Header-Dateien zum Schreiben von GIMP-Plugins und -Erweiterungen.

%description devel -l es
Bibliotecas y archivos de inclusi�n para escribir extensiones y
plugins para Gimp.

%description devel -l pl
Pliki nag��wkowe do tworzenia wtyczek i rozszerze� dla Gimpa.

%description devel -l pt_BR
Bibliotecas e arquivos de inclus�o para escrever extens�es e plugins
para o Gimp.

%package static
Summary:	GIMP static libraries
Summary(pl):	Biblioteki statyczne Gimpa
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
GIMP static libraries.

%description static -l es
Bibliotecas est�ticas para escribir extensiones y plugins para Gimp.

%description static -l pl
Biblioteki statyczne Gimpa.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento de plugins e extens�es do
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
Ce paquet contient le plugin d'art ASCII qui n�c�ssite la librairie
partag�e aalib.

%description aa -l pl
Ten pakiet zawiera wtyczk� do Gimpa ze wsparciem do ASCII Art.

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
%patch2 -p1
%{!?with_gnome:%patch3 -p1}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-rpath \
	%{!?with_python: --disable-python} \
	--enable-mp \
	--with-html-dir=%{_gtkdocdir} \
	--enable-default-binary \
	--enable-static \
	--enable-gtk-doc \
	%{?with_posix_shm:--with-shm=posix}
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

################### end hack ############################

# Link gimptool to gimptool-2.0

ln -s gimptool-%{mver} $RPM_BUILD_ROOT%{_bindir}/gimptool
echo '.so gimptool-%{mver}' > $RPM_BUILD_ROOT%{_mandir}/man1/gimptool.1

# Remove obsolete files
rm -f $RPM_BUILD_ROOT%{_libdir}/gimp/%{mver}/modules/*.{a,la}
rm -f $RPM_BUILD_ROOT%{_libdir}/gimp/%{mver}/python/*.{a,la,py}
rm -r $RPM_BUILD_ROOT%{_datadir}/{application-registry,mime-info}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor

%postun
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%doc docs/Wilber*

%attr(755,root,root) %{_bindir}/gimp-2.3
%attr(755,root,root) %{_bindir}/gimp
%attr(755,root,root) %{_bindir}/gimp-console-2.3
%attr(755,root,root) %{_bindir}/gimp-remote-2.3
%attr(755,root,root) %{_bindir}/gimp-remote
%{_desktopdir}/gimp.desktop
%{_mandir}/man1/gimp-2*
%{_mandir}/man1/gimp-remote-2*
%{_mandir}/man5/gimprc-2*

%dir %{_libdir}/gimp
%dir %{_libdir}/gimp/%{mver}
%dir %{_libdir}/gimp/%{mver}/plug-ins
%{_libdir}/gimp/%{mver}/interpreters
%attr(755,root,root) %{_libdir}/gimp/%{mver}/plug-ins/*
%{?with_aalib:%exclude %{_libdir}/gimp/%{mver}/plug-ins/aa}
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

%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/%{mver}
%config %verify(not md5 mtime) %{_sysconfdir}/%{name}/%{mver}/gimprc*
%config(noreplace) %{_sysconfdir}/%{name}/%{mver}/templaterc
%config %{_sysconfdir}/%{name}/%{mver}/controllerrc
%config %{_sysconfdir}/%{name}/%{mver}/gtkrc*
%config %{_sysconfdir}/%{name}/%{mver}/menurc
%config %{_sysconfdir}/%{name}/%{mver}/ps-menurc
%config %{_sysconfdir}/%{name}/%{mver}/sessionrc
%config %{_sysconfdir}/%{name}/%{mver}/unitrc

%{_iconsdir}/hicolor/*/apps/gimp.*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

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

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%if %{with aalib}
%files aa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gimp/%{mver}/plug-ins/aa
%endif

%files svg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gimp/%{mver}/plug-ins/svg
