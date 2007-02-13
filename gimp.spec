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
Summary(de.UTF-8):	Das GNU-Bildbearbeitungs-Programm
Summary(es.UTF-8):	Programa de manipulación de imagen GNU
Summary(fr.UTF-8):	Le programme de manipulation d'images de GNU
Summary(pl.UTF-8):	Program GNU do manipulacji formatami graficznymi (GIMP)
Summary(pt_BR.UTF-8):	Programa de manipulação de imagem GNU
Summary(ru.UTF-8):	The GNU Image Manipulation Program
Summary(tr.UTF-8):	Çizim, boyama ve görüntü işleme programı
Summary(uk.UTF-8):	The GNU Image Manipulation Program
Summary(zh_CN.UTF-8):	[图像]GNU图象处理工具
Summary(zh_TW.UTF-8):	[圖像]GNU圖象處理工具
Name:		gimp
Version:	2.2.13
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.gimp.org/pub/gimp/v2.2/%{name}-%{version}.tar.bz2
# Source0-md5:	d84a4a476a0c4fae24602db67f6fe49a
Patch0:		%{name}-home_etc.patch
URL:		http://www.gimp.org/
%{?with_aalib:BuildRequires:	aalib-devel}
BuildRequires:	alsa-lib-devel >= 1.0.0
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
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

%description -l es.UTF-8
GIMP es un programa de manejo de imágenes adecuado para retoque de
fotos, composición y editoración de imágenes. Muchas personas lo
encuentran extremamente útil en la creación de logos y otros gráficos
para páginas web. GIMP tiene muchas herramientas y filtros normalmente
encontrados en aplicaciones comerciales similares, además de
características extras bien interesantes. GIMP ofrece una extensa caja
de herramientas de manejo de imagen, incluyendo camadas, efectos,
formación de imagen subpíxel y antialiasing, conversiones, todos con
deshacer en varios niveles (multi-level undo).

%description -l fr.UTF-8
Le Programme de Manipulation d'Image de GNU permet de retoucher des
photos, de réaliser des compositions. Beaucoup de gens l'apprécient
pour la création de logos et de graphismes pour les pages web. GIMP
dispose d'un grand nombre de filtres et de plug-ins que l'on ne trouve
que dans les logiciels commerciaux haut de gamme ainsi que de
nombreuses fonctionnalité inédites.

GIMP fournit une boite à outil permettant de gérer plusieurs calques,
de nombreux effets, l'anti-aliasing, les conversions de fichiers ainsi
qu'un grand nombre de niveaux d'annulation.

%description -l pl.UTF-8
Program GIMP jest przeznaczony do obróbki i tworzenia plików w różnych
formatach graficznych. Przy jego użyciu można tworzyć grafikę dla
stron WWW, retuszować zdjęcia, czy stworzyć własne logo.

GIMP dostarcza duży zestaw narzędzi do obróbki obrazów, w tym do
operowania na kanałach i warstwach, efektów, antyaliasingu oraz
konwersji, a to wszystko z wielopoziomowym cofaniem operacji.

%description -l pt_BR.UTF-8
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

%description -l ru.UTF-8
GIMP - это программа для создания и обработки изображений. Ее считают
исключительно полезной для создания логотипов и другой графики для
web-страниц. GIMP имеет множество инструментов и фильтров, которые
обычно включаются в аналогичные коммерческие пакеты, а также ряд
возможностей, присущих только ей.

GIMP предоставляет большой набор инструментов для работы с графикой,
включающий операции над каналами, слоями, эффекты, sub-pixel imaging и
антиалиасинг, всяческие конверторы и все это с многоуровневым откатом.

GIMP включает поддержку создания сценариев (scripting facility),
однако многие из поставляемых с программой сценариев предполагают
наличие шрифтов, которые не могут быть включены в дистрибутив.
FTP-сайт GIMP содержит пакет шрифтов, которые вы можете поставить
самостоятельно, включающий все шрифты, необходимые для работы входящих
в комплект сценариев. Некоторые из шрифтов имеют весьма необычные
лицензионные требования; все лицензии включены в упомянутый пакет.
Скачайте ftp://ftp.gimp.org/pub/gimp/fonts/freefonts-0.10.tar.gz и
ftp://ftp.gimp.org/pub/gimp/fonts/sharefonts-0.10.tar.gz, если хотите
запускать сценарии без изменений или выберите те шрифты, которые
установлены у вас в системе, перед запуском сценариев.

%description -l uk.UTF-8
GIMP - це програма для створення та обробки зображень. Її вважають
дуже корисною для створення логотипів та іншої графіки для
web-сторінок. GIMP має багато інструментів та фільтрів, які звичайно
включаються в аналогічні комерційні пакети, а також ряд можливостей,
властивих саме їй.

GIMP надає великий набір інструментів для роботи з графікою, що
включає операції над каналами, шарами (layers), ефекти, sub-pixel
imaging і антиаліасинг, різноманітні конвертори і все це з
багаторівневим відкатом.

GIMP має підтримку сценаріїв (scripting facility), проте багато з
включених до поставки сценаріїв припускають наявність шрифтів, які не
можуть бути включені в дистрибутив. FTP-сайт GIMP містить пакет
шрифтів, котрі ви можете встановити самостійно, в який входять всі
шрифти, необхідні для роботи сценаріїв з поставки GIMP. Деякі з
шрифтів мають вельми незвичайні ліцензійні умови; всі ліцензії
включено в згаданий пакет. Завантажте
ftp://ftp.gimp.org/pub/gimp/fonts/freefonts-0.10.tar.gz та
ftp://ftp.gimp.org/pub/gimp/fonts/sharefonts-0.10.tar.gz. якщо хочете
запускати сценарії без змін або ж виберіть встановалені у вас в
системі шрифти перед запуском сценаріїв.

%package devel
Summary:	GIMP plugin and extension development kit
Summary(de.UTF-8):	GIMP-Plugin und Extension Development Kit
Summary(es.UTF-8):	Kit de desarrollo de "plugins" extensiones para GIMP
Summary(fr.UTF-8):	Plugin GIMP et kit de développement d'extensions
Summary(pl.UTF-8):	Pliki do budowania modułów i rozszerzeń dla Gimpa
Summary(pt_BR.UTF-8):	Kit de desenvolvimento de "plugins" extensões para o GIMP
Summary(ru.UTF-8):	Инструментарий для разработки плагинов и расширений GIMP
Summary(tr.UTF-8):	GIMP plugin ve uzantı geliştirme araçları
Summary(uk.UTF-8):	Інструментарій для розробки плагінів та розширень GIMP
Summary(zh_CN.UTF-8):	[开发]gimp的开发包
Summary(zh_TW.UTF-8):	[開發]gimp的開發包
License:	LGPL
Group:		X11/Development/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gtk+2-devel >= 2:2.4.4
Requires:	gtk-doc-common

%description devel
Header files for writing GIMP plugins and extensions.

%description devel -l de.UTF-8
Header-Dateien zum Schreiben von GIMP-Plugins und -Erweiterungen.

%description devel -l es.UTF-8
Bibliotecas y archivos de inclusión para escribir extensiones y
plugins para Gimp.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia wtyczek i rozszerzeń dla Gimpa.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão para escrever extensões e plugins
para o Gimp.

%package static
Summary:	GIMP static libraries
Summary(pl.UTF-8):	Biblioteki statyczne Gimpa
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
GIMP static libraries.

%description static -l es.UTF-8
Bibliotecas estáticas para escribir extensiones y plugins para Gimp.

%description static -l pl.UTF-8
Biblioteki statyczne Gimpa.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento de plugins e extensões do
GIMP.

%package aa
Summary:	ASCII Art plugin for Gimp
Summary(fr.UTF-8):	Plugin d'art ASCII pour Gimp
Summary(pl.UTF-8):	Wtyczka do ASCII Art do Gimpa
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description aa
This package contains the ASCII Art plugin which requires the aalib
shared library.

%description aa -l fr.UTF-8
Ce paquet contient le plugin d'art ASCII qui nécéssite la librairie
partagée aalib.

%description aa -l pl.UTF-8
Ten pakiet zawiera wtyczkę do Gimpa ze wsparciem do ASCII Art.

%package print
Summary:	Print plugin for Gimp
Summary(pl.UTF-8):	Wtyczka do drukowania dla Gimpa
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gimp-print-lib >= 4.2.6

%description print
Print plugin for Gimp.

%description print -l pl.UTF-8
Wtyczka do drukowania dla Gimpa.

%package svg
Summary:	SVG plugin for Gimp
Summary(pl.UTF-8):	Wtyczka SVG dla Gimpa
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	librsvg >= 2.2.0

%description svg
SVG plugin for Gimp.

%description svg -l pl.UTF-8
Wtyczka SVG dla Gimpa.

%prep
%setup -q
%patch0 -p1

cp /usr/share/automake/py-compile plug-ins/pygimp

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

%if %{with posix_shm}
%verifyscript
if ! grep -q -s '^[^ ]* /dev/shm tmpfs ' /proc/mounts ; then
	echo "/dev/shm is not mounted, but GIMP was compiled to use POSIX SHM"
fi
%endif

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
