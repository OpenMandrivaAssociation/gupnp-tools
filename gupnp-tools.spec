%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gupnp-tools
Version:	0.10.1
Release:	2
Summary:	A collection of dev tools utilizing GUPnP and GTK+
Group:		Development/Other
License:	GPLv2+
URL:		http://www.gupnp.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:   fix-build-str-fmt.patch
BuildRequires:  meson
BuildRequires:	pkgconfig(gssdp-1.2)
BuildRequires:	pkgconfig(gupnp-1.2)
BuildRequires:	pkgconfig(gupnp-av-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtksourceview-3.0)
BuildRequires:	pkgconfig(gnome-icon-theme)

%description
GUPnP is an object-oriented open source framework for creating UPnP 
devices and control points, written in C using GObject and libsoup. 
The GUPnP API is intended to be easy to use, efficient and flexible. 

GUPnP-tools is a collection of developer tools utilizing GUPnP and GTK+. 
It features a universal control point application as well as a sample 
DimmableLight v1.0 implementation. 

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README.md
%{_datadir}/%{name}
%{_bindir}/gssdp-discover
%{_bindir}/gupnp-network-light
%{_bindir}/gupnp-universal-cp
%{_bindir}/gupnp-av-cp
%{_bindir}/gupnp-upload
%{_datadir}/applications/gupnp-*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
