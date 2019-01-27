%define with_eds	0

%define api		3.0
%define major		8
%define libname		%mklibname %{name} %{api} %{major}
%define devname		%mklibname %{name} -d

%define bmajor		0
%define blibname	%mklibname glbarcode %{api} %{bmajor}
%define bdevname	%mklibname glbarcode -d

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	GNOME program to create labels and business cards
Name:		glabels
Version:	3.4.1
Release:	1
License:	GPLv2+
Group:		Office/Utilities
Source:		https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
URL:		http://glabels.sourceforge.net/
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)

%if %{with_eds}
BuildRequires:	pkgconfig(libebook-1.2)
%endif

BuildRequires:	pkgconfig(libiec16022)
BuildRequires:	pkgconfig(libqrencode)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pythonegg(six)
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk-doc
BuildRequires:	zint-devel
BuildRequires:	gettext-devel
BuildRequires:	itstool

%description
Glabels is stand-alone program for creating labels and business cards
for GNOME.

%package -n %{libname}
Summary:	Shared libraries for %{name}
Group:		System/Libraries

%description -n %{libname}
This package provides the shared libraries for %{name}.

%package -n %{blibname}
Summary:	Barcode support libraries for %{name}
Group:		System/Libraries

%description -n %{blibname}
This package contains the shared libraries for barcode support for %{name}.

%package -n %{devname}
Summary:	Development files and headers for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Recommends:	%{name}-docs = %{version}-%{release}

%description -n %{devname}
This package contains the development files and headers for %{name}.

%package -n %{bdevname}
Summary:	Development files and headers for %{name} barcodes
Group:		Development/Other
Requires:	%{blibname} = %{version}-%{release}
Provides:	glbarcode-devel = %{version}-%{release}
Recommends:	%{name}-docs = %{version}-%{release}

%description -n %{bdevname}
This package contains the development files and headers for %{name} barcodes.

%package docs
Summary:	Development documentation for %{name}
Group:		Documentation
BuildArch:	noarch

%description docs
This package contains the development documentation for %{name}.

%prep
%setup -q

%build
%configure2_5x \
%if %{with_eds}
	--with-libebook \
%else
	--without-libebook \
%endif
	--disable-static \
	--disable-schemas-compile

%make_build

%install
%make_install

perl -p -i -e 's/%{name}-%{api}.png/%{name}-%{api}/g' \
	%{buildroot}%{_datadir}/applications/*.desktop

%find_lang %{name}-%{api} --with-gnome

#we don't want these
find %{buildroot} -name "*.la" -delete

%files -f %{name}-%{api}.lang
%doc README AUTHORS
%{_bindir}/*
%{_datadir}/%{name}-%{api}
%{_datadir}/lib%{name}-%{api}
%{_datadir}/applications/*
%{_datadir}/mime/packages/*
%{_mandir}/man1/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/glib-2.0/schemas/org.gnome.glabels-3.gschema.xml
%{_datadir}/appdata/glabels-3.appdata.xml

%files docs
%{_datadir}/gtk-doc/html/libglabels-%{api}
%{_datadir}/gtk-doc/html/libglbarcode-%{api}

%files -n %{libname}
%{_libdir}/libglabels-%{api}.so.%{major}{,.*}

%files -n %{blibname}
%{_libdir}/libglbarcode-%{api}.so.%{bmajor}{,.*}

%files -n %{devname}
%{_libdir}/libglabels-%{api}.so
%{_includedir}/libglabels-%{api}
%{_libdir}/pkgconfig/libglabels-%{api}.pc

%files -n %{bdevname}
%{_libdir}/libglbarcode-%{api}.so
%{_includedir}/libglbarcode-%{api}
%{_libdir}/pkgconfig/libglbarcode-%{api}.pc
