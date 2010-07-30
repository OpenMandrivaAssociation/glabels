%define name glabels
%define version 2.3.0
%define release %mkrel 1

%define api 3.0
%define major 7
%define libname %mklibname %{name} %api %major
%define libnamedev %mklibname %{name}  -d


Summary:	GNOME program to create labels and business cards
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		Office
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
URL:		http://glabels.sourceforge.net/
BuildRequires:  evolution-data-server-devel
BuildRequires:  gtk+2-devel
BuildRequires:  scrollkeeper
BuildRequires:  desktop-file-utils
BuildRequires:	intltool
BuildRequires:	gnome-doc-utils >= 0.3.2
Requires(post): scrollkeeper
Requires(postun): scrollkeeper

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
for omf in %buildroot%_datadir/omf/*/*-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name-%api.lang
done

%clean
rm -rf $RPM_BUILD_ROOT

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


