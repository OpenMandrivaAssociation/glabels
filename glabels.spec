%define api 3.0
%define major 7
%define libname %mklibname %{name} %api %major
%define libnamedev %mklibname %{name}  -d


Summary:	GNOME program to create labels and business cards
Name:		glabels
Version:	2.3.0
Release:	5
License:	GPLv2+
Group:		Office
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
URL:		https://glabels.sourceforge.net/
BuildRequires:  evolution-data-server-devel
BuildRequires:  gtk+2-devel
BuildRequires:  scrollkeeper
BuildRequires:  desktop-file-utils
BuildRequires:	intltool
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:  qrencode-devel
BuildRequires:  iec16022-devel
BuildRequires:  zint-devel
BuildRequires:  barcode-devel
Requires(post): scrollkeeper
Requires(postun): scrollkeeper

%description
Glabels is stand-alone program for creating labels and business cards
for GNOME.

%package -n %libname
Summary: GNOME program to create labels and business cards
Group: System/Libraries

%description -n %libname
Glabels is stand-alone program for creating labels and business cards
for GNOME. Libraries.

%package -n %libnamedev
Summary: Glabels devel files
Group: Development/Other
Requires: %libname = %version
Provides: libglabels-devel
Obsoletes: %mklibname -d glabels 4

%description -n %libnamedev
Glabels is stand-alone program for creating labels and business cards
for GNOME. Devel files.

%prep
%setup -q

%build
export LDFLAGS="-lgobject-2.0"
%configure2_5x --disable-update-mimedb --disable-update-desktopdb
%make

%install
rm -fr %buildroot *.lang
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/var

perl -p -i -e 's/%{name}.png/%{name}/g' %{buildroot}/%{_datadir}/applications/%{name}.desktop

desktop-file-install --vendor="" \
  --remove-category='Application' \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%find_lang %name-%api --with-gnome
#for omf in %buildroot%_datadir/omf/*/*-??*.omf;do 
#echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name-%api.lang
#done

%files -f %name-%api.lang
%defattr(-, root, root)
%doc README AUTHORS
%_bindir/*
%_datadir/%name-%api
%_datadir/lib%name-%api
%_datadir/applications/*
%_datadir/mime/packages/*
%_datadir/icons/hicolor/*/mimetypes/*glabels*
#%dir %_datadir/omf/%name
#%_datadir/omf/%name/%name-C.omf
%_datadir/pixmaps/*
%_mandir/man1/*
%_datadir/gtk-doc/html/lib%name-%api/

%files -n %libname
%defattr(-, root, root)
%_libdir/libglabels-%api.so.%{major}*

%files -n %libnamedev
%defattr(-, root, root)
%_libdir/libglabels-%api.so
%_libdir/libglabels-%api.*a
%dir %_includedir/libglabels-%api
%_includedir/libglabels-%api/*
%_libdir/pkgconfig/libglabels-%api.pc




%changelog
* Thu Mar 17 2011 Jani VÃ¤limaa <wally@mandriva.org> 2.3.0-3mdv2011.0
+ Revision: 646255
- enable optional barcode backends

* Mon Aug 09 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.3.0-2mdv2011.0
+ Revision: 568226
- rebuild for new e-d-s

* Fri Jul 30 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.3.0-1mdv2011.0
+ Revision: 563390
- new version
- drop patch
- new major
- new source URL
- update build deps
- update file list

* Tue Apr 20 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.2.8-1mdv2010.1
+ Revision: 536931
- update to new version 2.2.8

* Wed Mar 03 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.2.7-1mdv2010.1
+ Revision: 513800
- new version
- add omf files

* Thu Nov 12 2009 Funda Wang <fwang@mandriva.org> 2.2.6-1mdv2010.1
+ Revision: 465134
- BR gnome-doc-utils
- new version 2.2.6

* Sat May 02 2009 Funda Wang <fwang@mandriva.org> 2.2.5-1mdv2010.0
+ Revision: 370441
- New version 2.2.5

* Tue Dec 23 2008 Funda Wang <fwang@mandriva.org> 2.2.4-1mdv2009.1
+ Revision: 317773
- fix str fmt
- new version 2.2.4

* Wed Aug 20 2008 Funda Wang <fwang@mandriva.org> 2.2.3-1mdv2009.0
+ Revision: 274124
- New version 2.2.3
- drop merged patch

* Sun Aug 10 2008 Frederik Himpe <fhimpe@mandriva.org> 2.2.2-2mdv2009.0
+ Revision: 270431
- Add Fedora patch to fix a segfault

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 2.2.2-1mdv2009.0
+ Revision: 218423
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
- do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Feb 24 2008 Frederik Himpe <fhimpe@mandriva.org> 2.2.2-1mdv2008.1
+ Revision: 174116
- New upstream release

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 2.2.0-2mdv2008.1
+ Revision: 170863
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Sun Dec 30 2007 Funda Wang <fwang@mandriva.org> 2.2.0-1mdv2008.1
+ Revision: 139526
- New major
- New version 2.2.0

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 21 2007 JÃ©rÃ´me Soyer <saispo@mandriva.org> 2.1.4-1mdv2008.1
+ Revision: 110924
- Fix Bug #35569
- Fix Bug #35569

  + Thierry Vignaud <tv@mandriva.org>
    - replace %%_datadir/man by %%_mandir!


* Fri Dec 29 2006 Frederic Crozat <fcrozat@mandriva.com> 2.1.3-5mdv2007.0
+ Revision: 102561
- Rebuild with latest eds

* Thu Nov 30 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.1.3-4mdv2007.1
+ Revision: 88942
- fix buildrequires
- fix buildrequires
- handle scrollkeeper
- spec fixes
- Import glabels

* Thu Nov 30 2006 Götz Waschk <waschk@mandriva.org> 2.1.3-3mdv2007.1
- fix buildrequires

* Fri Aug 04 2006 Frederic Crozat <fcrozat@mandriva.com> 2.1.3-2mdv2007.0
- xdg menu
- rebuild with latest dbus

* Wed May 31 2006 Lenny Cartier <lenny@mandriva.com> 2.1.3-1mdv2007.0
- 2.1.3

* Thu May 11 2006 Frederic Crozat <fcrozat@mandriva.com> 2.1.2-3mdk
- Fix buildrequires

* Tue Apr 25 2006 Frederic Crozat <fcrozat@mandriva.com> 2.1.2-2mdk
- Rebuild with latest e-d-s

* Thu Apr 06 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.1.2-1mdk
- New release 2.1.2

* Mon Dec 26 2005 Lenny Cartier <lenny@mandriva.com> 2.0.4-1mdk
- 2.0.4

* Fri Oct 28 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.0.3-3mdk
- Fix BuildRequires

* Fri Oct 28 2005 Lenny Cartier <lenny@mandriva.com> 2.0.3-2mdk
- rebuild for dependencies

* Fri Jul 22 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.0.3-1mdk
- New release 2.0.3

* Mon Jan 24 2005 Lenny Cartier <lenny@mandrakesoft.com> 2.0.2-1mdk
- 2.0.2

* Thu Jan 06 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0.1-6mdk 
- Rebuild with latest howl

* Fri Nov 12 2004 Götz Waschk <waschk@linux-mandrake.com> 2.0.1-5mdk
- fix installation
- spec fixes
- fix buildrequires

* Fri Nov 12 2004 Götz Waschk <waschk@linux-mandrake.com> 2.0.1-4mdk
- spec fixes
- remove generated files from /usr/share/mime/

* Mon Aug 30 2004 Jerome Soyer <saispo@mandrake.org> 2.0.1-3mdk
- Another BuildRequires

* Wed Aug 18 2004 Jerome Soyer <saispo@mandrake.org> 2.0.1-2mdk
- Fix BuildRequires

* Tue Aug 17 2004 Jerome Soyer <saispo@mandrake.org> 2.0.1-1mdk
- 2.0.1

* Thu Aug 12 2004 Jerome Soyer <saispo@mandrake.org> 2.0.0-1mdk
- 2.0.0

* Thu Jun 03 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.93.3-1mdk
- 1.93.3

