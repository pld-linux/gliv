Summary:	Graphics file browser utility
Summary(pl):	Narzêdzie do przegl±dania plików graficznych przy pomocy OpenGL
Name:		gliv
Version:	1.8
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Vendor:		Guillaume Chazarain <booh@altern.org>
Source0:	http://gliv.tuxfamily.org/%{name}-%{version}.tar.bz2
# Source0-md5:	75c516fc04426e88231b07fcd66d063e
URL:		http://gliv.tuxfamily.org/
BuildRequires:	gtk+2-devel >= 2.2.0
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
Gliv jest przegl±dark± obrazków u¿ywaj±c± OpenGL; ³adowanie obrazka
odbywa siê poprzez Gdk-pixbuf (samodzielny lub zwi±zany z GTK+-2),
renderowanie poprzez OpenGL, a interfejs graficzny u¿ytkownika u¿ywa
GTK+ z GtkGLArea. Je¶li Gtk-pixbuf nie mo¿e za³adowaæ obrazka,
wywo³uje ImageMagick aby dokonaæ jego konwersji na format PNG. GLiv
jest bardzo szybki, p³ynnie wykonuje rotacje, przesuwa aktualnie
wizualizowany fragment w oknie, powiêkszanie i zmniejszanie - je¶li
posiadasz akcelerator.

%prep
%setup -q

%build
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
