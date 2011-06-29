# vim: expandtab textwidth=74
Name:           allegro
Version:        4.4.2
Release:        1%{?dist}
Summary:        A game programming library

Summary:        A game programming library
Summary(es):    Una libreria de programacion de juegos
Summary(fr):    Une librairie de programmation de jeux
Summary(it):    Una libreria per la programmazione di videogiochi
Summary(cs):    Knihovna pro programování her

Group:          System Environment/Libraries
License:        Giftware
URL:            http://alleg.sourceforge.net/
Source0:        http://downloads.sourceforge.net/alleg/allegro-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

%description -l es
Allegro es una librería multi-plataforma creada para ser usada en la
programación de juegos u otro tipo de programación multimedia.

%description -l fr
Allegro est une librairie multi-plateforme destinée à être utilisée
dans les jeux vidéo ou d'autres types de programmation multimédia.

%description -l it
Allegro è una libreria multipiattaforma dedicata all'uso nei
videogiochi ed in altri tipi di programmazione multimediale.

%description -l cs
Allegro je multiplatformní knihovna pro počítačové hry a jiné
typy multimediálního programování.

%package        devel
Summary:        A game programming library
Summary(es):    Una libreria de programacion de juegos
Summary(fr):    Une librairie de programmation de jeux
Summary(it):    Una libreria per la programmazione di videogiochi
Summary(cs):    Knihovna pro programování her
Group:          Development/Libraries
Provides:       %{name}-static = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}, xorg-x11-proto-devel
Requires:       libX11-devel, libXcursor-devel
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info

%description devel
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming. This package is needed to
build programs written with Allegro.

%description devel -l es
Allegro es una librería multi-plataforma creada para ser usada en la
programación de juegos u otro tipo de programación multimedia. Este
paquete es necesario para compilar los programas que usen Allegro.

%description devel -l fr
Allegro est une librairie multi-plateforme destinée à être utilisée
dans les jeux vidéo ou d'autres types de programmation multimédia. Ce
package est nécessaire pour compiler les programmes utilisant Allegro.

%description devel -l it
Allegro è una libreria multipiattaforma dedicata all'uso nei
videogiochi ed in altri tipi di programmazione multimediale. Questo
pacchetto è necessario per compilare programmi scritti con Allegro.

%description devel -l cs
Allegro je multiplatformní knihovna pro počítačové hry a jiné
typy multimediálního programování. Tento balíček je je potřebný
k sestavení programů napsaných v Allegru.

%package        tools
Summary:        Extra tools for the Allegro programming library
Summary(es):    Herramientas adicionales para la librería de programación Allegro
Summary(fr):    Outils supplémentaires pour la librairie de programmation Allegro
Summary(it):    Programmi di utilità aggiuntivi per la libreria Allegro
Summary(cs):    Přídavné nástroje pro programovou knihovnu Allegro
Group:          Development/Tools
Requires:       %{name} = %{version}-%{release}

%description tools
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming. This package contains extra
tools which are useful for developing Allegro programs.

%description tools -l es
Allegro es una librería multi-plataforma creada para ser usada en la
programación de juegos u otro tipo de programación multimedia. Este
paquete contiene herramientas adicionales que son útiles para
desarrollar programas que usen Allegro.

%description tools -l fr
Allegro est une librairie multi-plateforme destinée à être utilisée
dans les jeux vidéo ou d'autres types de programmation multimédia. Ce
package contient des outils supplémentaires qui sont utiles pour le
développement de programmes avec Allegro.

%description tools -l it
Allegro è una libreria multipiattaforma dedicata all'uso nei
videogiochi ed in altri tipi di programmazione multimediale. Questo
pacchetto contiene programmi di utilità aggiuntivi utili allo sviluppo
di programmi con Allegro.

%description tools -l cs
Allegro je multiplatformní knihovna pro počítačové hry a jiné
typy multimediálního programování. Tento balíček obsahuje přídavné nástroje,
které jsou užitečné pro vývoj Allegro programů.

%package        gl
Summary:        OpenGL support library for Allegro
Group:          System Environment/Libraries
Requires:		%{name} = %{version}-%{release}

%description    gl
AllegroGL is an Allegro add-on that allows you to use OpenGL alongside
Allegro.  You use OpenGL for your rendering to the screen, and Allegro for
miscellaneous tasks like gathering input, doing timers, getting
cross-platform portability, loading data, and drawing your textures. So
this library fills the same hole that things like glut do.

AllegroGL also automatically exposes most, if not all, OpenGL extensions
available to user programs. This means you no longer have to manually load
them; extension management is already done for you.

%package        gl-devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    gl-devel
The %{name}-gl-devel package contains libraries and header files
for developing applications that use %{name}-gl.

%prep
%setup -n %{name}-%{version} -q

%build
mkdir build
cd build
%cmake ..
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd build
make install DESTDIR=$RPM_BUILD_ROOT
mkdir %buildroot/%{_sysconfdir}

# Remove raw build system installed documentation.
rm %buildroot/usr/doc/allegro-%{version}/AUTHORS \
        %buildroot/usr/doc/allegro-%{version}/CHANGES \
        %buildroot/usr/doc/allegro-%{version}/THANKS \
        %buildroot/usr/doc/allegro-%{version}/*.txt \
        %buildroot/usr/info/allegro.info

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc build/docs/AUTHORS build/docs/CHANGES build/docs/THANKS
%doc build/docs/html/*.html
%doc build/docs/man/*.3
%doc build/docs/info/allegro.info
%doc build/docs/txt/*.txt
%{_libdir}/allegro/%{version}/modules.lst
%{_libdir}/allegro/%{version}/alleg-alsadigi.so
%{_libdir}/allegro/%{version}/alleg-alsamidi.so
%{_libdir}/allegro/%{version}/alleg-jack.so
%{_libdir}/liballeg.so
%{_libdir}/liballeg.so.4.4
%{_libdir}/liballeg.so.%{version}

%files devel
%{_bindir}/allegro-config
%{_includedir}/allegro.h
%{_includedir}/allegro/3d.h
%{_includedir}/allegro/3dmaths.h
%{_includedir}/allegro/alcompat.h
%{_includedir}/allegro/alinline.h
%{_includedir}/allegro/base.h
%{_includedir}/allegro/color.h
%{_includedir}/allegro/compiled.h
%{_includedir}/allegro/config.h
%{_includedir}/allegro/datafile.h
%{_includedir}/allegro/debug.h
%{_includedir}/allegro/digi.h
%{_includedir}/allegro/draw.h
%{_includedir}/allegro/file.h
%{_includedir}/allegro/fix.h
%{_includedir}/allegro/fixed.h
%{_includedir}/allegro/fli.h
%{_includedir}/allegro/fmaths.h
%{_includedir}/allegro/font.h
%{_includedir}/allegro/gfx.h
%{_includedir}/allegro/graphics.h
%{_includedir}/allegro/gui.h
%{_includedir}/allegro/inline/3dmaths.inl
%{_includedir}/allegro/inline/asm.inl
%{_includedir}/allegro/inline/color.inl
%{_includedir}/allegro/inline/draw.inl
%{_includedir}/allegro/inline/fix.inl
%{_includedir}/allegro/inline/fmaths.inl
%{_includedir}/allegro/inline/gfx.inl
%{_includedir}/allegro/inline/matrix.inl
%{_includedir}/allegro/inline/rle.inl
%{_includedir}/allegro/inline/system.inl
%{_includedir}/allegro/internal/aintern.h
%{_includedir}/allegro/internal/aintvga.h
%{_includedir}/allegro/internal/alconfig.h
%{_includedir}/allegro/joystick.h
%{_includedir}/allegro/keyboard.h
%{_includedir}/allegro/lzss.h
%{_includedir}/allegro/matrix.h
%{_includedir}/allegro/midi.h
%{_includedir}/allegro/mouse.h
%{_includedir}/allegro/palette.h
%{_includedir}/allegro/platform/aintbeos.h
%{_includedir}/allegro/platform/aintdos.h
%{_includedir}/allegro/platform/aintlnx.h
%{_includedir}/allegro/platform/aintmac.h
%{_includedir}/allegro/platform/aintosx.h
%{_includedir}/allegro/platform/aintpsp.h
%{_includedir}/allegro/platform/aintqnx.h
%{_includedir}/allegro/platform/aintunix.h
%{_includedir}/allegro/platform/aintwin.h
%{_includedir}/allegro/platform/al386gcc.h
%{_includedir}/allegro/platform/al386vc.h
%{_includedir}/allegro/platform/al386wat.h
%{_includedir}/allegro/platform/albcc32.h
%{_includedir}/allegro/platform/albecfg.h
%{_includedir}/allegro/platform/albeos.h
%{_includedir}/allegro/platform/aldjgpp.h
%{_includedir}/allegro/platform/aldmc.h
%{_includedir}/allegro/platform/aldos.h
%{_includedir}/allegro/platform/almac.h
%{_includedir}/allegro/platform/almaccfg.h
%{_includedir}/allegro/platform/almngw32.h
%{_includedir}/allegro/platform/almsvc.h
%{_includedir}/allegro/platform/alosx.h
%{_includedir}/allegro/platform/alosxcfg.h
%{_includedir}/allegro/platform/alplatf.h
%{_includedir}/allegro/platform/alpsp.h
%{_includedir}/allegro/platform/alpspcfg.h
%{_includedir}/allegro/platform/alqnx.h
%{_includedir}/allegro/platform/alqnxcfg.h
%{_includedir}/allegro/platform/alucfg.h
%{_includedir}/allegro/platform/alunix.h
%{_includedir}/allegro/platform/alunixac.h
%{_includedir}/allegro/platform/alwatcom.h
%{_includedir}/allegro/platform/alwin.h
%{_includedir}/allegro/platform/astdint.h
%{_includedir}/allegro/platform/macdef.h
%{_includedir}/allegro/quat.h
%{_includedir}/allegro/rle.h
%{_includedir}/allegro/sound.h
%{_includedir}/allegro/stream.h
%{_includedir}/allegro/system.h
%{_includedir}/allegro/text.h
%{_includedir}/allegro/timer.h
%{_includedir}/allegro/unicode.h
%{_includedir}/jpgalleg.h
%{_includedir}/loadpng.h
%{_includedir}/logg.h
%{_includedir}/xalleg.h
%{_libdir}/libjpgalleg.a
%{_libdir}/libloadpng.a
%{_libdir}/liblogg.a
%{_libdir}/pkgconfig/allegro.pc
%{_libdir}/pkgconfig/allegrogl.pc
%{_libdir}/pkgconfig/jpgalleg.pc
%{_libdir}/pkgconfig/loadpng.pc
%{_libdir}/pkgconfig/logg.pc

%files tools
%{_bindir}/colormap
%{_bindir}/dat
%{_bindir}/dat2c
%{_bindir}/dat2s
%{_bindir}/exedat
%{_bindir}/grabber
%{_bindir}/pack
%{_bindir}/pat2dat
%{_bindir}/rgbmap
%{_bindir}/textconv

%files gl

%files gl-devel
%{_includedir}/alleggl.h
%{_includedir}/allegrogl/GLext/gl_ext_alias.h
%{_includedir}/allegrogl/GLext/gl_ext_api.h
%{_includedir}/allegrogl/GLext/gl_ext_defs.h
%{_includedir}/allegrogl/GLext/gl_ext_list.h
%{_includedir}/allegrogl/GLext/glx_ext_alias.h
%{_includedir}/allegrogl/GLext/glx_ext_api.h
%{_includedir}/allegrogl/GLext/glx_ext_defs.h
%{_includedir}/allegrogl/GLext/glx_ext_list.h
%{_includedir}/allegrogl/GLext/wgl_ext_alias.h
%{_includedir}/allegrogl/GLext/wgl_ext_api.h
%{_includedir}/allegrogl/GLext/wgl_ext_defs.h
%{_includedir}/allegrogl/GLext/wgl_ext_list.h
%{_includedir}/allegrogl/alleggl_config.h
%{_includedir}/allegrogl/gl_ext.h
%{_includedir}/allegrogl/gl_header_detect.h
%{_libdir}/liballeggl.a

%changelog
* Thu Jun 23 2011 Brandon McCaig <bamccaig@gmail.com> 4.4.2-1
- Update to 4.4.2.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan  7 2011 Hans de Goede <hdegoede@redhat.com> 4.2.3-4
- Fix a format string bug in the pack utility reported on bugtraq
  (but without security implications)

* Thu Sep  9 2010 Hans de Goede <hdegoede@redhat.com> 4.2.3-3
- Fix FTBFS (#631099)

* Mon Jun 21 2010 Hans de Goede <hdegoede@redhat.com> 4.2.3-2
- Fix multilib conflict in -devel (#603836)

* Mon Oct  5 2009 Jindrich Novy <jnovy@redhat.com> 4.2.3-1
- update to 4.2.3

* Thu Sep 10 2009 Hans de Goede <hdegoede@redhat.com> 4.2.2-14
- Fix (workaround) viewport issues in fullscreen mode (#522116)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 25 2009 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.2-11
- Fix wrong file path in semanage call in scriptlets (#481407)

* Mon May  5 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.2-10
- Look for /etc/timidity.cfg instead of /usr/share/timidity/timidity.cfg,
  as the latter is no longer available now that Fedora has switched from
  timidity++-patches to PersonalCopy-Lite-patches

* Tue Apr  1 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.2-9
- Fix i386 asm code compilation with latest binutils
- Remove -fomit-frame-pointer from the compile flags of the default build, so
  that we get a usefull debuginfo even for the normal (non debug/profile) lib

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4.2.2-8
- Autorebuild for GCC 4.3

* Mon Jan 21 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.2-7
- Add makedoc utility to allegro-devel as allegro-makedoc (bz 429450)
- Fix sound when using pulseaudio
- Fix compilation of inline asm with gcc 4.3

* Sun Oct 14 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.2-6
- Require timidity++-patches instead of timidity++ itself so that we don't
  drag in arts and through arts, qt and boost
- Add BuildRequires: glib2-devel to workaround RH bug 331841

* Wed Aug 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.2-5
- Update to pristine upstream sources instead of using allegro.cc pre-release

* Tue Aug 21 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.2-4
- Rebuild for buildId

* Sun Aug 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.2-3
- Enable building of JACK (Jack Audio Connection Kit) sound output plugin
- Put non default sound output plugins in their own subpackage to avoid
  dragging in unwanted deps (allegro-esound-plugin, allegro-arts-plugin,
  allegro-jack-plugin) (bz 250736)
- Make man pages and info file UTF-8

* Tue Jul 24 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.2-2
- sync .libdir patch to 4.2.2 and use it again for multilib devel goodness
  (make allegro-devel i386 and x86_64 parallel installable again)

* Mon Jul 23 2007 Jindrich Novy <jnovy@redhat.com> 4.2.2-1
- update to 4.2.2
- drop .libdir patch
- sync .multilib patch

* Fri Jul  6 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.1-3
- Silence output of chcon command in %%post, because otherwise users get this:
  "chcon: can't apply partial context to unlabeled file" when installing with
  selinux disabled (bz 246820)

* Fri Dec 22 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.1-2
- Restore multilib devel goodness patch (make allegro-devel i386 and x86_64
  parallel installable)
- Restore execstack patch so that binaries linked against allegro do not
  require an execstack and thus work under selinux (without this
  liballeg_unshareable.a contains object files which require an executable
  stack which will end up in any app linked against allegro)
- Make alleg-dga2.so plugin 100% PIC so it can load with selinux enabled
- Mark alleg-vga.so plugin as textrel_shlib_t as it isn't 100% PIC and cannot
  be fixed (easily) to be 100% PIC

* Tue Nov 28 2006 Jindrich Novy <jnovy@redhat.com> 4.2.1-1
- update to 4.2.1

* Sun Oct 15 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.0-18
- Multilib devel goodness (make allegro-devel i386 and x86_64 parallel
  installable)

* Sat Sep  2 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.0-17
- FE6 Rebuild

* Fri Jul 14 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.0-16
- Don't package the main allegro lib in -devel as its already in the main
  package, iow only put the debug and profile versions -devel.

* Thu Jul  6 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.0-15
- Stop allegro from making applications linked against it claim that they
  need an executable stack (Patch11). Unfortunatly this requires a rebuild of
  all applications linked against allegro.

* Mon Jun 26 2006 Jindrich Novy <jnovy@redhat.com> 4.2.0-14
- compile alld and allp debuging/profiling libraries (#196616)
- fix typo in release caused by recent changes

* Sat Jun 10 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.0-13
- Add autoconf BR for missing autoheader with the new mock config.

* Tue Mar 21 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.0-12
- Sleep in xwindows vsync emulation, instead of busy waiting.
- Add %%{dist} to Release

* Mon Mar 13 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.0-11
- really, _really_ fix asm stretch code on i386 with NX processors, long
  story see bugzilla bug 185214 .

* Sat Mar 11 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.0-10
- really fix asm stretch code on i386 with NX processors, on OpenBSD mprotects
  first argument does not need to be page-aligned, but on Linux it does.
  Note that for this to work you may also need to disable selinux (rh 185214)

* Wed Mar  8 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.0-9
- fix fullscreen <-> window switching bug (bz 183645)
- fix asm stretch code on i386 with NX processors, thanks to openBSD.

* Mon Feb 27 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.0-8
- fix sound not working on PPC (bz 183112)
- fix allegro not finding and loading plugins/modules on x86_64 (bz 183113)

* Tue Feb  8 2006 Jindrich Novy <jnovy@redhat.com> 4.2.0-7
- set timidity++ as Requires instead of BuildRequires

* Tue Feb  7 2006 Jindrich Novy <jnovy@redhat.com> 4.2.0-6
- fix digmid loading of timidity midi patches (#180154)

* Wed Jan 25 2006 Jindrich Novy <jnovy@redhat.com> 4.2.0-5
- update default allegro configuration to use sound successfully,
  thanks to Hans de Goede (#178383)
- add timidity++ dependency

* Mon Jan 23 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.0-4
- add allegro-4.2.0-nostrip.patch, so that the main .so file
  doesn't get stripped and we actually get debuginfo for it in
  allegro-debuginfo

* Fri Jan 20 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 4.2.0-3
- update / fix BuildRequires for modular X (bz 178245)

* Fri Dec 16 2005 Jindrich Novy <jnovy@redhat.com> 4.2.0-2
- update dependencies for the new modular X
- disable _smp_mflags to workaround build failure caused
  by bad dependencies

* Wed May 25 2005 Jindrich Novy <jnovy@redhat.com> 4.2.0-1
- update to 4.2.0
- package dat2c, allegro.m4
- replace XFree86-devel Buildrequires with xorg-x11-devel
- drop mmaptest, novga, gcc4 patches

* Wed May 25 2005 Jindrich Novy <jnovy@redhat.com> 4.0.3-13
- fix compilation on x86_64 (#158648)

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 4.0.3-12
- rebuild on all arches

* Mon May  2 2005 Jindrich Novy <jnovy@redhat.com> 0:4.0.3-11
- fix build failures with gcc4 (#156224)
- don't use %%{name} in patch names
- add Czech translation to package description/summary

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Fri Mar  4 2005 Ville Skyttä <ville.skytta at iki.fi>
- Split context marked dependency syntax to work around #118773.

* Sun Feb 13 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:4.0.3-9
- Disable vga and vbeaf on all non-%%{ix86}.
- Fix lib paths in allegro-config for 64-bit archs.
- Use *nix commands in allegrorc's [grabber] section.

* Sun Feb 13 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:4.0.3-8
- Build without vga and vbeaf on non-x86-like archs.
- Apply upstream patch to fix build without vga.

* Fri Nov 12 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:4.0.3-7
- Explicitly disable svgalib for now.
- Let rpm take care of all stripping.
- Build with whatever the compiler supports, MMX and friends are detected
  at runtime.
- Minor specfile style improvements.

* Wed Nov 10 2004 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:4.0.3-6
- Fix build for FC3 via fixed mmap test in configure script.

* Mon Nov 10 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:4.0.3-0.fdr.5
- Use MMX/SSE where appropriate (bug 959).

* Mon May 26 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:4.0.3-0.fdr.4
- Include *.so.* symlink.
- Re-introduce ldconfigs.
- *grumble*

* Mon May 26 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:4.0.3-0.fdr.3
- -devel Requires XFree86-devel.

* Mon May 26 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:4.0.3-0.fdr.2
- Handle --excludedocs installs gracefully.
- BuildRequires arts-devel.
- Make *.so executable so RPM groks autodependencies.
- Update to accordance with current Fedora spec template.

* Sat Apr 26 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:4.0.3-0.fdr.1
- Update to 4.0.3.
- Make build honor optflags.
- Remove redundant ldconfigs.

* Sat Apr  5 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:4.0.3-0.fdr.0.1.rc3
- Update to 4.0.3RC3.

* Thu Mar 20 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:4.0.3-0.fdr.0.1.rc2
- Update to 4.0.3RC2, and to current Fedora guidelines.
- make -jX works again.
- Don't remove info files on -devel upgrade.

* Wed Feb 19 2003 Warren Togami <warren@togami.com> 4.0.3-0.beta2.fedora.2
- Disable smp make flags, Makefile needs fixing

* Wed Feb 12 2003 Ville Skyttä <ville.skytta at iki.fi> - 4.0.3-0.beta2.fedora.1
- First Fedora release, based on upstream source RPM.

* Fri Dec 07 2001 Angelo Mottola <lillo@users.sourceforge.net>  4.0.0-1
- added italian translation

* Tue Oct 02 2001 Peter Wang <tjaden@users.sourceforge.net>  3.9.39-1
- icon courtesy of Johan Peitz

* Mon Sep 24 2001 Peter Wang <tjaden@users.sourceforge.net>
- remaining translations by Eric Botcazou and Grzegorz Adam Hankiewicz

* Sun Sep 23 2001 Peter Wang <tjaden@users.sourceforge.net>
- translations by Eric Botcazou and Javier González
- language.dat and keyboard.dat moved to main package
- devel split into devel and tools packages
- makedoc added to tools package

* Wed Sep 16 2001 Peter Wang <tjaden@users.sourceforge.net>
- merged Osvaldo's spec file with gfoot's spec and some other changes

* Wed Sep 27 2000 Osvaldo Santana Neto <osvaldo@conectiva.com>
- updated to 3.9.33

