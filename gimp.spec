
# http://bugzilla.gnome.org/show_bug.cgi?id=85249
%ifarch athlon
%define optflags -O2 -march=i386
%endif

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
Version:	1.3.8
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.gimp.org/pub/gimp/v1.3/v%{version}/%{name}-%{version}.tar.bz2
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
ftp-���� GIMP �������� ����� �������, ������� �� ������ ���������
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
������ ���� ������Φ � �����������. ftp-���� GIMP ͦ����� �����
����Ԧ�, ���Ҧ �� ������ ���������� �����Ԧ���, � ���� ������� �Ӧ
������, ����Ȧ�Φ ��� ������ �����Ҧ�� � �������� GIMP. ���˦ �
����Ԧ� ����� ������ ��������Φ ̦���ڦ�Φ �����; �Ӧ ̦���ڦ�
�������� � �������� �����. ����������
ftp://ftp.gimp.org/pub/gimp/fonts/freefonts-0.10.tar.gz ��
ftp://ftp.gimp.org/pub/gimp/fonts/sharefonts-0.10.tar.gz. ���� ������
��������� �����Ҧ� ��� �ͦ� ��� � ����Ҧ�� ����������Φ � ��� �
�����ͦ ������ ����� �������� �����Ҧ��.

%package devel
Summary:	GIMP plugin and extension development kit
Summary(de):	GIMP-Plugin und Extension Development Kit
Summary(es):	Kit de desarrollo de "plugins" extensiones para GIMP
Summary(fr):	Plugin GIMP et kit de d�veloppement d'extensions
Summary(pl):	Pliki do budowania modu��w i rozszerze� dla Gimp
Summary(pt_BR):	Kit de desenvolvimento de "plugins" extens�es para o GIMP
Summary(ru):	�������������� ��� ���������� �������� � ���������� GIMP
Summary(tr):	GIMP plugin ve uzant� geli�tirme ara�lar�
Summary(uk):	�����������Ҧ� ��� �������� ���ǦΦ� �� ��������� GIMP
Summary(zh_CN):	[����]gimp�Ŀ�����
Summary(zh_TW):	[�}�o]gimp���}�o�]
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

%prep
%setup	-q

%build
%configure \
	--without-included-gettext \
	--enable-mp

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Graphics}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

#install pixmaps/*.xpm plug-ins/*/*.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

cat $RPM_BUILD_ROOT%{_datadir}/gimp/1.3/misc/gimp.desktop | \
	sed 's@/usr/X11R6/share/gimp/1.3/images/@@' > \
	$RPM_BUILD_ROOT%{_applnkdir}/Graphics/gimp13.desktop
install data/images/wilber-icon.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --all-name

echo "%defattr(755,root,root,755)" >> %{name}.lang

\ls -1 $RPM_BUILD_ROOT%{_libdir}/gimp/1.3/plug-ins/* | \
	egrep -w -v -e "aa|something_else" | \
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
%doc AUTHORS ChangeLog MAINTAINERS NEWS PLUGIN_MAINTAINERS README TODO
%doc docs/{*.txt,quick_reference.*,Wilber*}

%attr(755,root,root) %{_bindir}/gimp-1.3
%attr(755,root,root) %{_bindir}/gimp-remote-1.3
%{_applnkdir}/Graphics/gimp13.desktop

%{_mandir}/man1/gimp-1.3.1*
%{_mandir}/man1/gimp-remote-1.3.1*
%{_mandir}/man5/gimprc-1.3.5*

%attr(755,root,root) %{_libdir}/lib*.so.*.*
# 1.2 own it
#%dir %{_libdir}/gimp
%dir %{_libdir}/gimp/1.3
%dir %{_libdir}/gimp/1.3/plug-ins
%dir %{_libdir}/gimp/1.3/modules
%attr(755,root,root) %{_libdir}/gimp/1.3/modules/*.so

%dir %{_datadir}/gimp/1.3
%{_datadir}/gimp/1.3/brushes
%{_datadir}/gimp/1.3/fractalexplorer
%{_datadir}/gimp/1.3/gfig
%{_datadir}/gimp/1.3/gflare
%{_datadir}/gimp/1.3/gimpressionist
%{_datadir}/gimp/1.3/gradients
%{_datadir}/gimp/1.3/images
%{_datadir}/gimp/1.3/palettes
%{_datadir}/gimp/1.3/patterns
%{_datadir}/gimp/1.3/scripts
%{_datadir}/gimp/1.3/themes
%{_datadir}/gimp/1.3/tips
%dir %{_datadir}/gimp/1.3/misc
%attr(755,root,root) %{_datadir}/gimp/1.3/misc/user_install

# 1.2 own it
#%dir %{_sysconfdir}/gimp
%dir %{_sysconfdir}/gimp/1.3
%config %verify(not md5 mtime) %{_sysconfdir}/gimp/1.3/gimprc*
%config %{_sysconfdir}/gimp/1.3/gtkrc*
%config %{_sysconfdir}/gimp/1.3/ps-menurc
%config %{_sysconfdir}/gimp/1.3/unitrc

%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%doc %{_datadir}/gtk-doc/html/*
%attr(755,root,root) %{_bindir}/gimptool-1.3
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/pkgconfig/*
%attr(755,root,root) %{_libdir}/gimp/1.3/modules/*.la

%{_includedir}/gimp-1.3
%{_aclocaldir}/gimp-1.4.m4

%{_mandir}/man1/gimptool-1.3.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files aa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gimp/1.3/plug-ins/aa
