#
# Conditional build:
%bcond_without	aalib		# aa plugin (which requires aalib)
%bcond_without	libunwind	# detailed backtraces using libunwind
%bcond_without	static_libs	# static libraries
%bcond_with	posix_shm	# with POSIX SHM (default is SysV SHM)

%define	babl_ver	0.1.112
%define	gegl_ver	0.4.58

%define		mver	3.0
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
Version:	3.0.2
Release:	1
Epoch:		1
License:	GPL v3+
Group:		X11/Applications/Graphics
Source0:	https://download.gimp.org/pub/gimp/v3.0/%{name}-%{version}.tar.xz
# Source0-md5:	e08392371ac08ce55c01dc824f734a35
Patch0:		%{name}-home_etc.patch
URL:		https://www.gimp.org/
BuildRequires:	OpenEXR-devel >= 1.6.1
%{?with_aalib:BuildRequires:	aalib-devel}
BuildRequires:	alsa-lib-devel >= 1.0.11
BuildRequires:	appstream-glib-devel >= 0.7.7
BuildRequires:	atk-devel >= 1:2.4.0
BuildRequires:	babl-devel >= %{babl_ver}
BuildRequires:	bzip2-devel
BuildRequires:	cairo-devel >= 1.14.0
BuildRequires:	cfitsio-devel
BuildRequires:	exiv2-devel >= 0.27.4
BuildRequires:	fontconfig-devel >= 2.12.4
BuildRequires:	fonts-TTF-DejaVu
BuildRequires:	freetype-devel >= 2.1.7
BuildRequires:	gdk-pixbuf2-devel >= 2.30.8
BuildRequires:	gegl-devel >= %{gegl_ver}
BuildRequires:	gettext-tools >= 0.19
BuildRequires:	gexiv2-devel >= 0.14.0
BuildRequires:	ghostscript-devel
BuildRequires:	gi-docgen
BuildRequires:	gjs-devel
BuildRequires:	glib-networking
BuildRequires:	glib2-devel >= 1:2.70.0
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel >= 3.24.0
BuildRequires:	harfbuzz-devel >= 2.8.2
BuildRequires:	iso-codes
BuildRequires:	json-glib-devel >= 1.2.6
BuildRequires:	lcms2-devel >= 2.8
BuildRequires:	libarchive-devel
BuildRequires:	libbacktrace-devel
BuildRequires:	libgomp-devel
BuildRequires:	libheif-devel >= 1.15.1
BuildRequires:	libjpeg-devel
BuildRequires:	libjxl-devel >= 0.7.0
BuildRequires:	libmng-devel
BuildRequires:	libmypaint-devel >= 1.4.0
BuildRequires:	libpng-devel >= 2:1.6.25
BuildRequires:	librsvg-devel >= 1:2.40.6
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	libtiff-devel >= 4.0.0
%{?with_libunwind:BuildRequires:	libunwind-devel >= 1.1.0}
BuildRequires:	libwebp-devel >= 0.6.0
BuildRequires:	libwmf-devel >= 2:0.2.8
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.61.0
BuildRequires:	mypaint-brushes-1-devel >= 1.0
BuildRequires:	ninja
BuildRequires:	openjpeg2-devel >= 2.1.0
BuildRequires:	pango-devel >= 1:1.50.0
BuildRequires:	perl-base >= 1:5.10.0
BuildRequires:	pkgconfig >= 1:0.16
BuildRequires:	poppler-data >= 0.4.9
BuildRequires:	poppler-glib-devel >= 0.69.0
BuildRequires:	python3 >= 1:3.6
BuildRequires:	python3-pygobject3
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	sed >= 4.0
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-glib-devel >= 1:167
BuildRequires:	vala
BuildRequires:	vala-babl
BuildRequires:	vala-gegl
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xz
BuildRequires:	xz-devel >= 1:5.0.0
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2 >= 2:2.24.32
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	OpenEXR >= 1.6.1
Requires:	alsa-lib >= 1.0.11
Requires:	appstream-glib >= 0.7.7
Requires:	atk >= 1:2.4.0
Requires:	babl >= %{babl_ver}
Requires:	cairo >= 1.14.0
Requires:	fontconfig-libs >= 2.12.4
Requires:	freetype >= 1:2.1.7
Requires:	gdk-pixbuf2 >= 2.30.8
Requires:	gegl >= %{gegl_ver}
Requires:	gexiv2 >= 0.14.0
Requires:	glib2 >= 1:2.70.0
Requires:	gtk+3 >= 3.24.0
Requires:	harfbuzz >= 2.8.2
Requires:	hicolor-icon-theme
Requires:	iso-codes
Requires:	json-glib >= 1.2.6
Requires:	lcms2 >= 2.8
Requires:	libheif >= 1.15.1
Requires:	libjxl >= 0.7.0
Requires:	libmypaint >= 1.4.0
Requires:	libpng >= 2:1.6.25
Requires:	libtiff >= 4.0.0
Requires:	libwebp >= 0.6.0
Requires:	libwmf-libs >= 2:0.2.8
Requires:	mypaint-brushes-1 >= 1.0
Requires:	openjpeg2 >= 2.1.0
Requires:	pango >= 1:1.50.0
Requires:	poppler-data >= 0.4.9
Requires:	poppler-glib >= 0.69.0
Requires:	udev-glib >= 1:167
Requires:	xz-libs >= 1:5.0.0
# for https
Suggests:	glib-networking
Obsoletes:	gimp-data-min < 1.1.1
Obsoletes:	gimp-libgimp < 1.1.1
Obsoletes:	gimp-print < 1:2.4
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
можуть бути включені в дистрибутив.

%package libs
Summary:	GIMP libraries
Summary(pl.UTF-8):	Biblioteki GIMP-a
License:	LGPL v2+
Group:		X11/Libraries
Requires:	babl >= %{babl_ver}
Requires:	cairo >= 1.14.0
Requires:	fontconfig-libs >= 2.12.4
Requires:	gdk-pixbuf2 >= 2.30.8
Requires:	gegl >= %{gegl_ver}
Requires:	glib2 >= 1:2.70.0
Requires:	gtk+3 >= 3.24.0
Requires:	lcms2 >= 2.8
Requires:	pango >= 1:1.50.0

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
Requires:	cairo-devel >= 1.14.0
Requires:	gdk-pixbuf2-devel >= 2.30.8
Requires:	gegl-devel >= %{gegl_ver}
Requires:	glib2-devel >= 1:2.70.0
Requires:	gtk+3-devel >= 3.24.0
Requires:	pango-devel >= 1:1.50.0

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
BuildArch:	noarch

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
Requires:	librsvg >= 1:2.40.6

%description svg
SVG plugin for GIMP.

%description svg -l pl.UTF-8
Wtyczka SVG dla GIMPa.

%package -n vala-gimp
Summary:	Vala API for gimp
Summary(pl.UTF-8):	API języka Vala dla gimpa
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
BuildArch:	noarch

%description -n vala-gimp
Vala API for gimp.

%description -n vala-gimp -l pl.UTF-8
API języka Vala dla gimpa.

%prep
%setup -q
%patch -P 0 -p1

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+gjs(\s|$),#!/usr/bin/gjs\1,' \
	extensions/goat-exercises/goat-exercise-gjs.js

%build
%meson \
	-Dbug-report-url="https://www.pld-linux.org/" \
	-Dappdata-test=disabled \
	-Dwith-sendmail=/usr/lib/sendmail \
	-Dgi-docgen=enabled \
	-Dlibunwind=%{__true_false libunwind} \
	%{?with_posix_shm:-Dshmem-type=posix}

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

# Fix mn page symlinks
for m in gimp gimp-console gimptool ; do
	%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/${m}{,-3}.1
	echo ".so ${m}-3.0.1" > $RPM_BUILD_ROOT%{_mandir}/man1/${m}-3.1
	echo ".so ${m}-3.0.1" > $RPM_BUILD_ROOT%{_mandir}/man1/${m}.1
done

%{__rm} $RPM_BUILD_ROOT%{_mandir}/man5/gimprc{,-3}.5
echo ".so gimprc-3.0.5" > $RPM_BUILD_ROOT%{_mandir}/man5/gimprc-3.5
echo ".so gimprc-3.0.5" > $RPM_BUILD_ROOT%{_mandir}/man5/gimprc.5

#%{?with_static_libs:%{__rm} $RPM_BUILD_ROOT%{_libdir}/gimp/%{mver}/modules/*.a}

# don't hide python/python3 behind /usr/bin/env
%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+python3(\s|$),#!%{__python3}\1,' \
	$RPM_BUILD_ROOT%{_libdir}/gimp/%{mver}/plug-ins/*/*.py \
	$RPM_BUILD_ROOT%{_libdir}/gimp/%{mver}/extensions/*/*.py

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+gimp-script-fu-interpreter-3.0(\s|$),#!%{_bindir}/gimp-script-fu-interpreter-3.0\1,' \
	$RPM_BUILD_ROOT%{_libdir}/gimp/%{mver}/plug-ins/test-sphere-v3/test-sphere-v3.scm

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS LICENSE NEWS README
%doc docs/Wilber*

%attr(755,root,root) %{_bindir}/gimp-3.0
%attr(755,root,root) %{_bindir}/gimp-3
%attr(755,root,root) %{_bindir}/gimp
%attr(755,root,root) %{_bindir}/gimp-console-3.0
%attr(755,root,root) %{_bindir}/gimp-console-3
%attr(755,root,root) %{_bindir}/gimp-console
%attr(755,root,root) %{_bindir}/gimp-script-fu-interpreter-3.0
%attr(755,root,root) %{_bindir}/gimp-test-clipboard-3.0
%attr(755,root,root) %{_bindir}/gimp-test-clipboard-3
%attr(755,root,root) %{_bindir}/gimp-test-clipboard
%attr(755,root,root) %{_libexecdir}/gimp-debug-tool-3.0
%attr(755,root,root) %{_libexecdir}/gimp-debug-tool-3
%attr(755,root,root) %{_libexecdir}/gimp-debug-tool
%{_datadir}/metainfo/org.gimp.GIMP.appdata.xml
%{_desktopdir}/gimp.desktop
%{_iconsdir}/hicolor/*x*/apps/gimp.png
%{_iconsdir}/hicolor/scalable/apps/gimp.svg
%{_mandir}/man1/gimp*.1*
%{_mandir}/man5/gimprc*.5*

%dir %{_libdir}/gimp
%dir %{_libdir}/gimp/%{mver}
%dir %{_libdir}/gimp/%{mver}/plug-ins
%{_libdir}/gimp/%{mver}/interpreters
%attr(755,root,root) %{_libdir}/gimp/%{mver}/plug-ins/*
%{?with_aalib:%exclude %{_libdir}/gimp/%{mver}/plug-ins/file-aa}
%exclude %{_libdir}/gimp/%{mver}/plug-ins/file-svg
%dir %{_libdir}/gimp/%{mver}/extensions
%dir %{_libdir}/gimp/%{mver}/extensions/org.gimp.extension.goat-exercises
%{_libdir}/gimp/%{mver}/extensions/org.gimp.extension.goat-exercises/goat-exercise*
%{_libdir}/gimp/%{mver}/extensions/org.gimp.extension.goat-exercises/org.gimp.extension.goat-exercises.metainfo.xml

%dir %{_libdir}/gimp/%{mver}/modules
%attr(755,root,root) %{_libdir}/gimp/%{mver}/modules/*.so
%{_libdir}/gimp/%{mver}/environ

%{_libdir}/girepository-1.0/Gimp-3.0.typelib
%{_libdir}/girepository-1.0/GimpUi-3.0.typelib

%dir %{_datadir}/gimp
%dir %{_datadir}/gimp/%{mver}
%{_datadir}/gimp/%{mver}/gimp-release
%{_datadir}/gimp/%{mver}/brushes
%{_datadir}/gimp/%{mver}/dynamics
%{_datadir}/gimp/%{mver}/file-raw
%{_datadir}/gimp/%{mver}/fractalexplorer
%{_datadir}/gimp/%{mver}/gfig
%{_datadir}/gimp/%{mver}/gflare
%{_datadir}/gimp/%{mver}/gimpressionist
%{_datadir}/gimp/%{mver}/gradients
%{_datadir}/gimp/%{mver}/icons
%{_datadir}/gimp/%{mver}/images
%{_datadir}/gimp/%{mver}/menus
%{_datadir}/gimp/%{mver}/palettes
%{_datadir}/gimp/%{mver}/patterns
%{_datadir}/gimp/%{mver}/scripts
%{_datadir}/gimp/%{mver}/tags
%{_datadir}/gimp/%{mver}/themes
%{_datadir}/gimp/%{mver}/tips
%{_datadir}/gimp/%{mver}/tool-presets

%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/%{mver}
%config %verify(not md5 mtime size) %{_sysconfdir}/%{name}/%{mver}/gimprc*
%config(noreplace) %{_sysconfdir}/%{name}/%{mver}/templaterc
%config %{_sysconfdir}/%{name}/%{mver}/gimp.css
%config %{_sysconfdir}/%{name}/%{mver}/controllerrc
%config %{_sysconfdir}/%{name}/%{mver}/sessionrc
%config %{_sysconfdir}/%{name}/%{mver}/toolrc
%config %{_sysconfdir}/%{name}/%{mver}/unitrc

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgimp-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgimp-3.0.so.0
%attr(755,root,root) %{_libdir}/libgimp-scriptfu-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgimp-scriptfu-3.0.so.0
%attr(755,root,root) %{_libdir}/libgimpbase-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgimpbase-3.0.so.0
%attr(755,root,root) %{_libdir}/libgimpcolor-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgimpcolor-3.0.so.0
%attr(755,root,root) %{_libdir}/libgimpconfig-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgimpconfig-3.0.so.0
%attr(755,root,root) %{_libdir}/libgimpmath-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgimpmath-3.0.so.0
%attr(755,root,root) %{_libdir}/libgimpmodule-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgimpmodule-3.0.so.0
%attr(755,root,root) %{_libdir}/libgimpthumb-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgimpthumb-3.0.so.0
%attr(755,root,root) %{_libdir}/libgimpui-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgimpui-3.0.so.0
%attr(755,root,root) %{_libdir}/libgimpwidgets-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgimpwidgets-3.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gimptool-3.0
%attr(755,root,root) %{_bindir}/gimptool-3
%attr(755,root,root) %{_bindir}/gimptool
%attr(755,root,root) %{_libdir}/libgimp-3.0.so
%attr(755,root,root) %{_libdir}/libgimp-scriptfu-3.0.so
%attr(755,root,root) %{_libdir}/libgimpbase-3.0.so
%attr(755,root,root) %{_libdir}/libgimpcolor-3.0.so
%attr(755,root,root) %{_libdir}/libgimpconfig-3.0.so
%attr(755,root,root) %{_libdir}/libgimpmath-3.0.so
%attr(755,root,root) %{_libdir}/libgimpmodule-3.0.so
%attr(755,root,root) %{_libdir}/libgimpthumb-3.0.so
%attr(755,root,root) %{_libdir}/libgimpui-3.0.so
%attr(755,root,root) %{_libdir}/libgimpwidgets-3.0.so
%{_pkgconfigdir}/gimp-3.0.pc
%{_pkgconfigdir}/gimpthumb-3.0.pc
%{_pkgconfigdir}/gimpui-3.0.pc
%{_includedir}/gimp-3.0
%{_datadir}/gir-1.0/Gimp-3.0.gir
%{_datadir}/gir-1.0/GimpUi-3.0.gir
%{_mandir}/man1/gimptool*.1*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgimp-3.0.a
%{_libdir}/libgimp-scriptfu-3.0.a
%{_libdir}/libgimpbase-3.0.a
%{_libdir}/libgimpcolor-3.0.a
%{_libdir}/libgimpconfig-3.0.a
%{_libdir}/libgimpmath-3.0.a
%{_libdir}/libgimpmodule-3.0.a
%{_libdir}/libgimpthumb-3.0.a
%{_libdir}/libgimpui-3.0.a
%{_libdir}/libgimpwidgets-3.0.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/gimp-3.0

%if %{with aalib}
%files aa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gimp/%{mver}/plug-ins/file-aa
%endif

%files svg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gimp/%{mver}/plug-ins/file-svg

%files -n vala-gimp
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gimp-3.0.deps
%{_datadir}/vala/vapi/gimp-3.0.vapi
%{_datadir}/vala/vapi/gimp-ui-3.0.deps
%{_datadir}/vala/vapi/gimp-ui-3.0.vapi
