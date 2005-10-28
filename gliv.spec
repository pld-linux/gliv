Summary:	Graphics file browser utility
Summary(pl):	Narz�dzie do przegl�dania plik�w graficznych przy pomocy OpenGL
Name:		gliv
Version:	1.9.3
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Vendor:		Guillaume Chazarain <booh@altern.org>
Source0:	http://guichaz.free.fr/gliv/%{name}-%{version}.tar.bz2
# Source0-md5:	3840a547cdc679c5a592d30040b9f6b5
URL:		http://guichaz.free.fr/gliv/
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	gtkglext-devel >= 1.0.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
GLiv is an OpenGL image viewer, image loading is done through
Gdk-pixbuf (standalone or bundled with GTK+-2), rendering through
OpenGL and the graphical user interface uses GTK+ with the GtkGLArea
widget. If Gdk-pixbuf cannot load your image, it uses ImageMagick to
convert it to PNG. GLiv is very fast and smooth at rotating, panning
and zooming if you have an OpenGL accelerated board.

%description -l pl
Gliv jest przegl�dark� obrazk�w u�ywaj�c� OpenGL; �adowanie obrazka
odbywa si� poprzez Gdk-pixbuf (samodzielny lub zwi�zany z GTK+-2),
renderowanie poprzez OpenGL, a interfejs graficzny u�ytkownika u�ywa
GTK+ z GtkGLArea. Je�li Gtk-pixbuf nie mo�e za�adowa� obrazka,
wywo�uje ImageMagick aby dokona� jego konwersji na format PNG. GLiv
jest bardzo szybki, p�ynnie wykonuje rotacje, przesuwa aktualnie
wizualizowany fragment w oknie, powi�kszanie i zmniejszanie - je�li
posiadasz akcelerator.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README NEWS THANKS
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(ru) %{_mandir}/ru/man1/*
