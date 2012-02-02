#
# Conditional build:
%bcond_without	aalib		# without aa plugin (which requires aalib)
%bcond_without	gnomevfs	# without GNOME VFS support
%bcond_without	gnome		# convenient alias for gnomevfs
%bcond_without	python		# without python plugins
%bcond_without	webkit		# without webkit-based help browser
%bcond_with	posix_shm	# with POSIX SHM (default is SysV SHM)
#
%if %{without gnome}
%undefine	with_gnomevfs
%endif
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
Version:	2.6.12
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.gimp.org/pub/gimp/v2.6/%{name}-%{version}.tar.bz2
# Source0-md5:	9f876ee63a0c4a4c83f50f32fb3bbe63
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-gcc4.patch
Patch3:		%{name}-udev.patch
URL:		http://www.gimp.org/
%{?with_aalib:BuildRequires:	aalib-devel}
BuildRequires:	alsa-lib-devel >= 1.0.11
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	babl-devel >= 0.0.22
BuildRequires:	curl-devel >= 7.15.1
BuildRequires:	cairo-devel >= 1.4.10
BuildRequires:	dbus-glib-devel >= 0.70
BuildRequires:	docbook-dtd412-xml
BuildRequires:	fontconfig-devel >= 1:2.2.0
BuildRequires:	gegl-devel >= 0.0.18
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
BuildRequires:	glib2-devel >= 1:2.16.1
BuildRequires:	gtk+2-devel >= 2:2.12.5
BuildRequires:	gtk-doc >= 1.6
%{?with_webkit:BuildRequires:	gtk-webkit-devel >= 1.1.0}
BuildRequires:	intltool >= 0.36.3
BuildRequires:	iso-codes
BuildRequires:	lcms-devel >= 1.16
BuildRequires:	libart_lgpl-devel
BuildRequires:	libexif-devel >= 0.6.15
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel
BuildRequires:	libpng-devel >= 1.2.12
BuildRequires:	librsvg-devel >= 1:2.15.0
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	libwmf-devel >= 2:0.2.8
BuildRequires:	pango-devel >= 1:1.18.0
BuildRequires:	pkgconfig >= 1:0.16
BuildRequires:	poppler-devel >= 0.17
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	udev-glib-devel >= 1:167
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	zlib-devel
%if %{with gnomevfs}
BuildRequires:	gnome-vfs2-devel >= 2.15.91
BuildRequires:	libgnome-keyring-devel >= 0.5.1
BuildRequires:	libgnomeui-devel >= 2.15.91
%endif
%if %{with python}
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-pygtk-devel >= 2:2.10.4
%endif
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	curl >= 7.15.1
Requires:	dbus-glib >= 0.70
Requires:	hicolor-icon-theme
Requires:	lcms >= 1.16
Requires:	libexif >= 0.6.15
%{?with_python:Requires:	python-pygtk-gtk >= 1:2.10.4}
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

%package libs
Summary:	GIMP libraries
Summary(pl.UTF-8):	Biblioteki GIMP-a
License:	LGPL v2+
Group:		Libraries
Requires:	glib2 >= 1:2.16.1
Requires:	gtk+2 >= 2:2.12.5
Requires:	pango >= 1:1.18.0

%description libs
This package contains GIMP libraries.

%description libs -l pl.UTF-8
Pakiet zawiera biblioteki GIMP-a.

%package devel
Summary:	GIMP plugin and extension development kit
Summary(de.UTF-8):	GIMP-Plugin und Extension Development Kit
Summary(es.UTF-8):	Kit de desarrollo de "plugins" extensiones para GIMP
Summary(fr.UTF-8):	Plugin GIMP et kit de développement d'extensions
Summary(pl.UTF-8):	Pliki do budowania modułów i rozszerzeń dla GIMPa
Summary(pt_BR.UTF-8):	Kit de desenvolvimento de "plugins" extensões para o GIMP
Summary(ru.UTF-8):	Инструментарий для разработки плагинов и расширений GIMP
Summary(tr.UTF-8):	GIMP plugin ve uzantı geliştirme araçları
Summary(uk.UTF-8):	Інструментарій для розробки плагінів та розширень GIMP
Summary(zh_CN.UTF-8):	[开发]gimp的开发包
Summary(zh_TW.UTF-8):	[開發]gimp的開發包
License:	LGPL v2+
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	glib2-devel >= 1:2.16.1
Requires:	gtk+2-devel >= 2:2.12.5

%description devel
Header files for writing GIMP plugins and extensions.

%description devel -l de.UTF-8
Header-Dateien zum Schreiben von GIMP-Plugins und -Erweiterungen.

%description devel -l es.UTF-8
Bibliotecas y archivos de inclusión para escribir extensiones y
plugins para GIMP.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia wtyczek i rozszerzeń dla GIMPa.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão para escrever extensões e plugins
para o GIMP.

%package static
Summary:	GIMP static libraries
Summary(pl.UTF-8):	Biblioteki statyczne GIMPa
License:	LGPL v2+
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
GIMP static libraries.

%description static -l es.UTF-8
Bibliotecas estáticas para escribir extensiones y plugins para GIMP.

%description static -l pl.UTF-8
Biblioteki statyczne GIMPa.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento de plugins e extensões do
GIMP.

%package apidocs
Summary:	GIMP API documentation
Summary(pl.UTF-8):	Dokumentacja API GIMPa
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GIMP API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API GIMPa.

%package aa
Summary:	ASCII Art plugin for GIMP
Summary(fr.UTF-8):	Plugin d'art ASCII pour GIMP
Summary(pl.UTF-8):	Wtyczka do ASCII Art do GIMPa
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description aa
This package contains the ASCII Art plugin which requires the aalib
shared library.

%description aa -l fr.UTF-8
Ce paquet contient le plugin d'art ASCII qui nécéssite la librairie
partagée aalib.

%description aa -l pl.UTF-8
Ten pakiet zawiera wtyczkę do GIMPa ze wsparciem do ASCII Art.

%package svg
Summary:	SVG plugin for GIMP
Summary(pl.UTF-8):	Wtyczka SVG dla GIMPa
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	librsvg >= 2.15.0

%description svg
SVG plugin for GIMP.

%description svg -l pl.UTF-8
Wtyczka SVG dla GIMPa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

mv modules/gimpinputdevicestore-hal.c modules/gimpinputdevicestore-gudev.c

%build
rm acinclude.m4 m4macros/gtk-doc.m4
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I m4macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_gnomevfs:--disable-gnomevfs} \
	%{!?with_python:--disable-python} \
	--enable-default-binary \
	--enable-gimp-remote \
	--enable-gtk-doc \
	--enable-static \
	--with-html-dir=%{_gtkdocdir} \
	%{?with_posix_shm:--with-shm=posix} \
	%{!?with_webkit:--without-webkit}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Link gimptool to gimptool-2.0.1
ln -s gimptool-2.0 $RPM_BUILD_ROOT%{_bindir}/gimptool
echo '.so gimptool-2.0.1' > $RPM_BUILD_ROOT%{_mandir}/man1/gimptool.1

# remove unneeded files
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gimp/%{mver}/modules/*.{a,la}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gimp/%{mver}/python/*.{a,la,py}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:
%update_icon_cache hicolor

%postun
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE NEWS README
%doc docs/Wilber*

%attr(755,root,root) %{_bindir}/gimp-2.6
%attr(755,root,root) %{_bindir}/gimp
%attr(755,root,root) %{_bindir}/gimp-console-2.6
%attr(755,root,root) %{_bindir}/gimp-console
%attr(755,root,root) %{_bindir}/gimp-remote-2.6
%attr(755,root,root) %{_bindir}/gimp-remote
%{_desktopdir}/gimp.desktop
%{_mandir}/man1/gimp-2.6.1*
%{_mandir}/man1/gimp.1*
%{_mandir}/man1/gimp-console-2.6.1*
%{_mandir}/man1/gimp-console.1*
%{_mandir}/man1/gimp-remote-2.6.1*
%{_mandir}/man1/gimp-remote.1*
%{_mandir}/man5/gimprc-2.6.5*
%{_mandir}/man5/gimprc.5*

%dir %{_libdir}/gimp
%dir %{_libdir}/gimp/%{mver}
%dir %{_libdir}/gimp/%{mver}/plug-ins
%{_libdir}/gimp/%{mver}/interpreters
%attr(755,root,root) %{_libdir}/gimp/%{mver}/plug-ins/*
%{?with_aalib:%exclude %{_libdir}/gimp/%{mver}/plug-ins/file-aa}
%exclude %{_libdir}/gimp/%{mver}/plug-ins/file-svg

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
%attr(755,root,root) %{_libdir}/libgimp-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgimp-2.0.so.0
%attr(755,root,root) %{_libdir}/libgimpbase-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgimpbase-2.0.so.0
%attr(755,root,root) %{_libdir}/libgimpcolor-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgimpcolor-2.0.so.0
%attr(755,root,root) %{_libdir}/libgimpconfig-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgimpconfig-2.0.so.0
%attr(755,root,root) %{_libdir}/libgimpmath-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgimpmath-2.0.so.0
%attr(755,root,root) %{_libdir}/libgimpmodule-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgimpmodule-2.0.so.0
%attr(755,root,root) %{_libdir}/libgimpthumb-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgimpthumb-2.0.so.0
%attr(755,root,root) %{_libdir}/libgimpui-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgimpui-2.0.so.0
%attr(755,root,root) %{_libdir}/libgimpwidgets-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgimpwidgets-2.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gimptool-%{mver}
%attr(755,root,root) %{_bindir}/gimptool
%attr(755,root,root) %{_libdir}/libgimp-2.0.so
%attr(755,root,root) %{_libdir}/libgimpbase-2.0.so
%attr(755,root,root) %{_libdir}/libgimpcolor-2.0.so
%attr(755,root,root) %{_libdir}/libgimpconfig-2.0.so
%attr(755,root,root) %{_libdir}/libgimpmath-2.0.so
%attr(755,root,root) %{_libdir}/libgimpmodule-2.0.so
%attr(755,root,root) %{_libdir}/libgimpthumb-2.0.so
%attr(755,root,root) %{_libdir}/libgimpui-2.0.so
%attr(755,root,root) %{_libdir}/libgimpwidgets-2.0.so
%{_libdir}/libgimp-2.0.la
%{_libdir}/libgimpbase-2.0.la
%{_libdir}/libgimpcolor-2.0.la
%{_libdir}/libgimpconfig-2.0.la
%{_libdir}/libgimpmath-2.0.la
%{_libdir}/libgimpmodule-2.0.la
%{_libdir}/libgimpthumb-2.0.la
%{_libdir}/libgimpui-2.0.la
%{_libdir}/libgimpwidgets-2.0.la
%{_pkgconfigdir}/gimp-2.0.pc
%{_pkgconfigdir}/gimpthumb-2.0.pc
%{_pkgconfigdir}/gimpui-2.0.pc
%{_includedir}/gimp-2.0
%{_aclocaldir}/gimp-2.0.m4
%{_mandir}/man1/gimptool-%{mver}.1*
%{_mandir}/man1/gimptool.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgimp-2.0.a
%{_libdir}/libgimpbase-2.0.a
%{_libdir}/libgimpcolor-2.0.a
%{_libdir}/libgimpconfig-2.0.a
%{_libdir}/libgimpmath-2.0.a
%{_libdir}/libgimpmodule-2.0.a
%{_libdir}/libgimpthumb-2.0.a
%{_libdir}/libgimpui-2.0.a
%{_libdir}/libgimpwidgets-2.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgimp
%{_gtkdocdir}/libgimpbase
%{_gtkdocdir}/libgimpcolor
%{_gtkdocdir}/libgimpconfig
%{_gtkdocdir}/libgimpmath
%{_gtkdocdir}/libgimpmodule
%{_gtkdocdir}/libgimpthumb
%{_gtkdocdir}/libgimpwidgets

%if %{with aalib}
%files aa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gimp/%{mver}/plug-ins/file-aa
%endif

%files svg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gimp/%{mver}/plug-ins/file-svg
