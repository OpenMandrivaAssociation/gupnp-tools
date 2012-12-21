%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gupnp-tools
Version:	0.8.5
Release:	1
Summary:	A collection of dev tools utilizing GUPnP and GTK+
Group:		Development/Other
License:	GPLv2+
URL:		http://www.gupnp.org/
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gssdp-1.0) >= 0.10
BuildRequires:	pkgconfig(gupnp-1.0) >= 0.13
BuildRequires:	pkgconfig(gupnp-av-1.0) >= 0.5.5
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:	pkgconfig(gtksourceview-3.0)
BuildRequires:	pkgconfig(gnome-icon-theme) >= 2.20

%description
GUPnP is an object-oriented open source framework for creating UPnP 
devices and control points, written in C using GObject and libsoup. 
The GUPnP API is intended to be easy to use, efficient and flexible. 

GUPnP-tools is a collection of developer tools utilizing GUPnP and GTK+. 
It features a universal control point application as well as a sample 
DimmableLight v1.0 implementation. 

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files
%doc AUTHORS README
%{_datadir}/%{name}
%{_bindir}/gssdp-discover
%{_bindir}/gupnp-network-light
%{_bindir}/gupnp-universal-cp
%{_bindir}/gupnp-av-cp
%{_bindir}/gupnp-upload
%{_datadir}/applications/gupnp-*.desktop

