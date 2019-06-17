#
# Conditional build:
%bcond_without	aalib		# aa plugin (which requires aalib)
%bcond_without	python		# python plugins
%bcond_without	libunwind	# detailed backtraces using libunwind
%bcond_without	webkit		# webkit-based help browser
%bcond_with	posix_shm	# with POSIX SHM (default is SysV SHM)

%define	babl_ver	0.1.62
%define	gegl_ver	0.4.14

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
Version:	2.10.10
Release:	3
Epoch:		1
License:	GPL v3+
Group:		X11/Applications/Graphics
Source0:	http://ftp.gimp.org/pub/gimp/v2.10/%{name}-%{version}.tar.bz2
# Source0-md5:	0b837ea2bbf801da7f5306df4c99fa18
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-gcc4.patch
Patch3:		%{name}-no-checks-for-runtime-deps.patch
URL:		http://www.gimp.org/
BuildRequires:	OpenEXR-devel >= 1.6.1
%{?with_aalib:BuildRequires:	aalib-devel}
BuildRequires:	alsa-lib-devel >= 1.0.11
BuildRequires:	atk-devel >= 1:2.2.0
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	babl-devel >= %{babl_ver}
BuildRequires:	bzip2-devel
BuildRequires:	cairo-devel >= 1.12.2
BuildRequires:	docbook-dtd412-xml
BuildRequires:	fontconfig-devel >= 2.12.4
BuildRequires:	freetype-devel >= 1:2.1.7
BuildRequires:	gdk-pixbuf2-devel >= 2.30.8
BuildRequires:	gegl-devel >= %{gegl_ver}
BuildRequires:	gettext-tools >= 0.19
BuildRequires:	gexiv2-devel >= 0.10.6
BuildRequires:	ghostscript-devel
BuildRequires:	giflib-devel
BuildRequires:	glib2-devel >= 1:2.54.2
BuildRequires:	glib-networking
BuildRequires:	gtk+2-devel >= 2:2.24.32
BuildRequires:	gtk-update-icon-cache >= 2.24.32
BuildRequires:	gtk-doc >= 1.6
%{?with_webkit:BuildRequires:	gtk-webkit-devel >= 1.6.1}
BuildRequires:	harfbuzz-devel >= 0.9.19
BuildRequires:	intltool >= 0.40.1
BuildRequires:	iso-codes
BuildRequires:	lcms2-devel >= 2.8
BuildRequires:	libheif-devel >= 1.1.0
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel
BuildRequires:	libmypaint-devel >= 1.3.0
BuildRequires:	libpng-devel >= 2:1.6.25
BuildRequires:	librsvg-devel >= 1:2.40.6
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:2.2
%{?with_libunwind:BuildRequires:	libunwind-devel >= 1.1.0}
BuildRequires:	libwebp-devel >= 0.6.0
BuildRequires:	libwmf-devel >= 2:0.2.8
BuildRequires:	mypaint-brushes-devel >= 1.0
BuildRequires:	mypaint-brushes-devel < 2
BuildRequires:	openjpeg2-devel >= 2.1.0
BuildRequires:	pango-devel >= 1:1.29.4
BuildRequires:	perl-base >= 1:5.10.0
BuildRequires:	pkgconfig >= 1:0.16
BuildRequires:	poppler-glib-devel >= 0.50.0
%{?with_python:BuildRequires:	python >= 1:2.5.0}
%{?with_python:BuildRequires:	python-pycairo-devel >= 1.12.2}
%{?with_python:BuildRequires:	python-pygtk-devel >= 1:2.10.4}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	udev-glib-devel >= 1:167
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
Requires(post,postun):	gtk+2 >= 2:2.24.32
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	OpenEXR >= 1.6.1
Requires:	alsa-lib >= 1.0.11
Requires:	atk >= 1:2.2.0
Requires:	fontconfig-libs >= 2.12.4
Requires:	freetype >= 1:2.1.7
Requires:	harfbuzz >= 0.9.19
Requires:	hicolor-icon-theme
Requires:	iso-codes
Requires:	libheif >= 1.1.0
Requires:	libmypaint >= 1.3.0
Requires:	libpng >= 2:1.6.25
Requires:	libwebp >= 0.6.0
Requires:	libwmf-libs >= 2:0.2.8
Requires:	mypaint-brushes >= 1.0
Requires:	mypaint-brushes < 2
Requires:	openjpeg2 >= 2.1.0
Requires:	poppler-data >= 0.4.7
Requires:	poppler-glib >= 0.50.0
%{?with_python:Requires:	python-pygtk-gtk >= 1:2.10.4}
Requires:	udev-glib >= 1:167
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
Requires:	cairo >= 1.12.2
Requires:	gdk-pixbuf2 >= 2.30.8
Requires:	gegl >= %{gegl_ver}
Requires:	gexiv2 >= 0.10.6
Requires:	glib2 >= 1:2.54.2
Requires:	gtk+2 >= 2:2.24.32
Requires:	lcms2 >= 2.8
Requires:	pango >= 1:1.29.4

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
Requires:	cairo-devel >= 1.12.2
Requires:	gdk-pixbuf2-devel >= 2.30.8
Requires:	gegl-devel >= %{gegl_ver}
Requires:	glib2-devel >= 1:2.54.2
Requires:	gtk+2-devel >= 2:2.24.32
Requires:	pango-devel >= 1:1.29.4

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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

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

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__rm} acinclude.m4
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I m4macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_python:--disable-python} \
	--disable-silent-rules \
	--enable-default-binary \
	--enable-gtk-doc \
	--enable-static \
	--without-appdata-test \
	--with-bug-report-url="https://www.pld-linux.org/" \
	--with-html-dir=%{_gtkdocdir} \
	--with-lcms=2 \
	%{!?with_libunwind:--without-libunwind} \
	--with-sendmail=/usr/lib/sendmail \
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

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgimp*.la
# dynamic modules loaded via gmodule
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gimp/%{mver}/modules/*.{a,la}
%if %{with python}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gimp/%{mver}/python/*.{a,la,py}
%endif

# don't hide {python,python2,python3} behind /usr/bin/env
%{__sed} -i -e '1s,/usr/bin/env python,/usr/bin/python,' $RPM_BUILD_ROOT%{_libdir}/gimp/%{mver}/plug-ins/*/*.py

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
[ ! -x %{_bindir}/update-desktop-database ] || %{_bindir}/update-desktop-database >/dev/null 2>&1 ||:
%update_icon_cache hicolor

%postun
umask 022
[ ! -x %{_bindir}/update-desktop-database ] || %{_bindir}/update-desktop-database >/dev/null 2>&1
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE NEWS README
%doc docs/Wilber*

%attr(755,root,root) %{_bindir}/gimp-2.10
%attr(755,root,root) %{_bindir}/gimp
%attr(755,root,root) %{_bindir}/gimp-console-2.10
%attr(755,root,root) %{_bindir}/gimp-console
%attr(755,root,root) %{_bindir}/gimp-test-clipboard-2.0
%attr(755,root,root) %{_libexecdir}/gimp-debug-tool-2.0
%{_datadir}/metainfo/gimp-data-extras.metainfo.xml
%{_datadir}/metainfo/org.gimp.GIMP.appdata.xml
%{_desktopdir}/gimp.desktop
%{_iconsdir}/hicolor/*x*/apps/gimp.png
%{_mandir}/man1/gimp-2.10.1*
%{_mandir}/man1/gimp.1*
%{_mandir}/man1/gimp-console-2.10.1*
%{_mandir}/man1/gimp-console.1*
%{_mandir}/man5/gimprc-2.10.5*
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
%{_datadir}/gimp/%{mver}/ui

%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/%{mver}
%config %verify(not md5 mtime) %{_sysconfdir}/%{name}/%{mver}/gimprc*
%config(noreplace) %{_sysconfdir}/%{name}/%{mver}/templaterc
%config %{_sysconfdir}/%{name}/%{mver}/controllerrc
%config %{_sysconfdir}/%{name}/%{mver}/gtkrc*
%config %{_sysconfdir}/%{name}/%{mver}/menurc
%config %{_sysconfdir}/%{name}/%{mver}/sessionrc
%config %{_sysconfdir}/%{name}/%{mver}/unitrc

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
