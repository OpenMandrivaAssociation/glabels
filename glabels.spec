%define name glabels
%define version 2.2.0
%define release %mkrel 2

%define major 5
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name}  -d


Summary:	GNOME program to create labels and business cards
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		Office

Source:		http://easynews.dl.sourceforge.net/sourceforge/glabels/%name-%version.tar.gz

URL:		http://snaught.com/glabels/
Buildrequires:  libgnomeprintui-devel
BuildRequires:  evolution-data-server-devel
BuildRequires:  libglade2.0-devel
BuildRequires:  libgnomeui2-devel
BuildRequires:  perl-XML-Parser
BuildRequires:  scrollkeeper
BuildRequires:  desktop-file-utils
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

%configure2_5x
#perl -p -i -e 's/%{name}.png/%{name}/g' data/desktop/%{name}.desktop
%make

%install
rm -fr %buildroot %name.lang

%makeinstall UPDATE_MIME_DATABASE=true UPDATE_DESKTOP_DATABASE=true

rm -rf $RPM_BUILD_ROOT/var

perl -p -i -e 's/%{name}.png/%{name}/g' %{buildroot}/%{_datadir}/applications/%{name}.desktop

desktop-file-install --vendor="" \
  --remove-category='Application' \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%find_lang %name --with-gnome

%post
%update_menus
%update_mime_database
%update_scrollkeeper

%postun
%clean_menus
%clean_mime_database
%clean_scrollkeeper

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-, root, root)
%doc README AUTHORS
%_bindir/*
%_datadir/%name
%_datadir/application-registry/*
%_datadir/applications/*
%_datadir/mime-info/*
%_datadir/mime/packages/*
%dir %_datadir/omf/%name
%_datadir/omf/%name/%name-C.omf
%_datadir/pixmaps/*
%_mandir/man1/*
%_datadir/gtk-doc/html/libglabels/*

%files -n %libname
%defattr(-, root, root)
%_libdir/*.so.%{major}*

%files -n %libnamedev
%defattr(-, root, root)
%_libdir/*.so
%_libdir/*.*a
%dir %_includedir/libglabels
%_includedir/libglabels/*
%_libdir/pkgconfig/libglabels.pc


