Summary:	The GNU Image Manipulation Program
Summary(fr):	Le programme de manipulation d'images de GNU.
Summary(de):	Das GNU-Bildbearbeitungs-Programm
Summary(pl):	GNU program do manipulacji formatami graficznymi (GIMP)
Summary(tr):	Çizim, boyama ve görüntü iþleme programý
Name:		gimp
Version:	1.1.4
Release:	1
Copyright:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source0:	ftp://ftp.gimp.org/pub/gimp/unstable/v1.1/%{name}-%{version}.tar.bz2
Source1:	gimp.wmconfig
Patch0:		gimp-perl.patch
Patch1:		gimp-DESTDIR.patch
URL:		http://www.gimp.org/
Icon:		gimp.xpm
Requires:	gtk+ = 1.2.1
Requires:	glib = 1.2.1
Requires:	perl >= 5.005
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	gimp-data-min
Obsoletes:	gimp-libgimp

%description
The GIMP is an image manipulation program suitable for photo retouching,
image composition and image authoring.  Many people find it extremely useful
in creating logos and other graphics for web pages.  The GIMP has many of the
tools and filters you would expect to find in similar commercial offerings,
and some interesting extras as well.

The GIMP provides a large image manipulation toolbox, including channel
operations and layers, effects, sub-pixel imaging and anti-aliasing,
and conversions, all with multi-level undo.

This version of The GIMP includes a scripting facility, but many of the
included scripts rely on fonts that we cannot distribute.  The GIMP ftp
site has a package of fonts that you can install by yourself, which
includes all the fonts needed to run the included scripts.  Some of the
fonts have unusual licensing requirements; all the licenses are documented
in the package. Get ftp://ftp.gimp.org/pub/gimp/fonts/freefonts-0.10.tar.gz
and ftp://ftp.gimp.org/pub/gimp/fonts/sharefonts-0.10.tar.gz if you are so
inclined. Alternatively, choose fonts which exist on your system before
running the scripts.

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
Group:		X11/Developmet/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Copyright:	LGPL
Requires:	%{name} = %{version}
Requires:	gtk+-devel = 1.2.1

%description devel
Header files for writing GIMP plugins and extensions.

%description -l de devel
Header-Dateien zum Schreiben von GIMP-Plugins und -Erweiterungen

%descriptions -l pl devel
Pliki nag³ówowe dla GIMP.

%package static
Summary:	GIMP static libraries
Summary(pl):	Biblioteki statyczne do GIMPa
Group:		X11/Developmet/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
GIMP static libraries

%description -l pl static
Biblioteki statyczne do GIMPa

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr/X11R6 \
	--without-included-gettext \
	--disable-perl \
	--with-xdelta
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/share/aclocal} \
	$RPM_BUILD_ROOT/usr/X11R6/share/icons \
	$RPM_BUILD_ROOT/usr/lib/perl5/5.00502/$RPM_ARCH-linux-thread

make install \
	prefix=$RPM_BUILD_ROOT/usr/X11R6 \
	INSTALLMAN3DIR=/tmp/gimp-1.1.4-root%{_mandir}/man3 \
	INSTALLMAN1DIR=/tmp/gimp-1.1.4-root%{_mandir}/man1 \
	PREFIX=/tmp/gimp-1.1.4-root/usr \
	m4datadir=$RPM_BUILD_ROOT/usr/share/aclocal

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/gimp

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/man/man*/* \
	ChangeLog NEWS README docs/{*.txt,*.eps} \
#	$RPM_BUILD_ROOT%{_mandir}/man*/*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,NEWS,README,docs/*,docs/*.eps}.gz

/etc/X11/wmconfig/gimp

%attr(755,root,root) /usr/X11R6/bin/gimp
#%attr(755,root,root) /usr/bin/*

/usr/X11R6/man/man1/gimp.1*
/usr/X11R6/man/man5/gimprc.5*
#%{_mandir}/man1/*

%attr(755,root,root) /usr/X11R6/lib/lib*.so.*

%attr(755,root,root,755) /usr/X11R6/lib/gimp

%dir /usr/X11R6/share/gimp
/usr/X11R6/share/gimp/brushes
/usr/X11R6/share/gimp/gfig
/usr/X11R6/share/gimp/gradients
/usr/X11R6/share/gimp/palettes
/usr/X11R6/share/gimp/patterns
/usr/X11R6/share/gimp/scripts
/usr/X11R6/share/gimp/*.ppm

%config %verify(not md5 mtime) /usr/X11R6/share/gimp/gimprc*
%config /usr/X11R6/share/gimp/gtkrc*
%config /usr/X11R6/share/gimp/ps-menurc

/usr/X11R6/share/gimp/gimp_tips.txt

%attr(755,root,root) /usr/X11R6/share/gimp/user_install

#%attr(-,root,root,755) /usr/lib/perl5/site_perl/*

%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/gimp.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/gimp.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/gimp.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/gimp.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/gimp.mo
%lang(ja) /usr/X11R6/share/locale/ja/LC_MESSAGES/gimp.mo
%lang(ko) /usr/X11R6/share/locale/ko/LC_MESSAGES/gimp.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/gimp.mo

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/lib/lib*.so
%attr(755,root,root) /usr/X11R6/bin/gimptool

/usr/X11R6/include/*
/usr/share/aclocal/*

/usr/X11R6/man/man1/gimptool.1.*
/usr/X11R6/man/man3/*
#%{_mandir}/man3/*

%files static
%attr(644,root,root) /usr/X11R6/lib/lib*.a

%changelog
* Mon Mar 29 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.3-1]
- removed man group from man pages,
- gzipping %doc,

* Fri Feb 05 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.1.2-1d]
- updated to 1.1.2,
- compresed man documentation,
- hashed /etc/X11/* .

* Wed Oct 14 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [981216-1d]
- build against Tornado,
- build against gtk+-1.1.7+
- fixed files permissions,
- fixed shared libraries permissions,
- translation modified for pl,
- minor modifications of the spec file.

* Sun Sep 27 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.0-0.980921]
- many siplifications an updates in %install and %files
- updates Requires lists,
- added more Requires rules to devel and static subpackages,
- changed prefix to /usr/X11R6.

* Sat Aug 22 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0.0-2]
- added static subpackage,
- "Prereq: /sbin/install-info" moved to devel.
- added fr, fr, tr translation from RH spec.
- recompiled gimp against gtk+ 1.1.1 and latest libjpeg, libpng and xdelta.

* Sun Jun  7 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0.0-1]
- removed libgimp subpackage,
- added icons,
- added missing patterns to main package,
- added gimptool script with man page to devel,
- added man3 pages to devel.

* Mon May 11 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.99.29-2]
- added moving $RPM_BUILD_ROOT/usr/lib/gimp/0.99/plug-ins/lib*.a to
  $RPM_BUILD_ROOT/usr/lib (moved to devel subpackage) because files lib*.a
  are not plugins.

* Wed May  5 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.99.29-1]
- changed Requires for gimp, now gimp require gtk+ >= 1.0.1,
- added using %{SOURCE#} nacros in %install,
- %%{version} macro instead %%{PACKAGE_VERSION},
- added using %%{name} macro in Buildroot, in Requires in gimplib and in
  Source fields,
- added -q parameter (quiet) for %setup macro.

* Wed Apr 28 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>                   
  [0.99.28-2]
- added removing libmegawidget.a from plugins directory (this not plugin but
  static library required on compile time fuse plugin from unstable plugins
  wihtch curenly not compile),

* Wed Mar 24 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.99.28-1]
- Source is now in bz2 format,
- Buildroot changed to /tmp/gimp-%%{PACKAGE_VERSION}-root,
- replaced "mkdir -p" with "install -d" in %install,
- added gimp-ATEXIT.diff patch wit dirty fix not finding ATEXIT macro from
  gtk+ (is it gtk+ bug ?),
- removed INSTALL from %doc,
- removed COPYING from %doc (copyright info in package herader),
- added "Requires: libgimp = %%{PACKAGE_VERSION}" for main and devel packages,
- changed main package Copyright to GPL and to LGPL in libgimp and devel,
- added %config files (in future with using rpm 2.5.x modifing on install
  %time in post gimprc allow install gimp package as relocatable),
- /usr/lib/lib*.so moved from libgimp to devel,
- added striping plug-ins and shared libs,
- added %defattr, %attr macros in %files (allows building package from
  non-root account and determine real permission); %defattr requires rpm
  >= 2.4.99.

* Sat Mar 21 1998 Trond Eivind Glomsrød <teg@pvv.ntnu.no>
- No longer requires xdelta, that was a bug on my part
- spec cleanup, changed libgimp copyright, can now be
  built by non-root users, removed some lines in the description

* Fri Mar 20 1998 Trond Eivind Glomsrød <teg@pvv.ntnu.no>
- upgraded to 0.99.22

* Sun Mar 15 1998 Trond Eivind Glomsrød <teg@pvv.ntnu.no>
- upgraded to 0.99.21

* Thu Mar 12 1998 Trond Eivind Glomsrød <teg@pvv.ntnu.no>
- Upgraded to 0.99.20

* Mon Mar 09 1998 Trond Eivind Glomsrød <teg@pvv.ntnu.no>
- Recompiled with gtk+ 0.99.5
- Now requires gtk+ >= 0.99.5 instead of gtk+ 0.99.4

* Mon Mar 02 1998 Trond Eivind Glomsrød <teg@pvv.ntnu.no>
- Upgraded to 0.99.19
- gave up requiring gtk+ >= a specific version.
  = is better suited to the totally unstable API of gtk+.
- Obsoleted gimp-data-min, as it is now part of gimp.
- Removed some old changelog entries

* Tue Jan 27 1998 Trond Eivind Glomsrød <teg@pvv.ntnu.no>
- It doesn't seem to work with glibc 2.0.5. So I added
  a requirement for glibc 2.0.6 or higher. This is an
  errata item for RH5, and so should be installed anyway.

* Mon Jan 26 1998 Trond Eivind Glomsrød <teg@pvv.ntnu.no>
- Upgraded to 0.99.18
- removed the hacks necesarry for compiling 0.99.17

* Wed Jan 07 1998 Trond Eivind Glomsrød <teg@pvv.ntnu.no>
- Updated to 0.99.17
- use an old aclocal.m4, since the new one breaks building
  libs

* Mon Dec 15 1997 Trond Eivind Glomsrød <teg@pvv.ntnu.no>
- Updated to 0.99.16

* Sat Nov 29 1997 Trond Eivind Glomsrød <teg@pvv.ntnu.no>
- Updated to 0.99.15
- Now uses RPM_OPT_FLAGS

* Thu Oct 30 1997 Michael K. Johnson <johnsonm@redhat.com>
- fixed wmconfig
