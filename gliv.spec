Summary:	Graphics file browser utility
Summary(pl):	Narzêdzie do przegl±dania plików graficznych przy pomocy OpenGL
Name:		gliv
Version:	1.5.2
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Vendor:		Guillaume Chazarain <booh@altern.org>
Source0:	http://gliv.tuxfamily.org/%{name}-%{version}.tar.bz2
Patch0:		%{name}-AM_INIT_AUTOMAKE.patch
URL:		http://gliv.tuxfamily.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:	gtkglarea-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
GLiv is an OpenGL image viewer, image loading is done through
Gdk-pixbuf (standalone or bundled with GTK+-2), rendering through
OpenGL and the graphical user interface uses GTK+ with the GtkGLArea
widget. If Gdk-pixbuf cannot load your image, it uses ImageMagick to
convert it to PNG. GLiv is very fast and smooth at rotating, panning
and zooming if you have an OpenGL accelerated board.

%description -l pl
Gliv jest przegladark± obrazków u¿ywaj±c± OpenGL; ³adowanie obrazka
odbywa siê poprzez Gdk-pixbuf (samodzielny lub zwi±zany z GTK+-2),
renderowanie poprzez OpenGL, a interfejs graficzny u¿ytkownika u¿ywa
GTK+ z GtkGLArea. Je¶li Gtk-pixbuf nie mo¿e za³adowaæ obrazka,
wywo³uje ImageMagick aby dokonaæ jego konwersji na format PNG. GLiv
jest bardzo szybki, p³ynnie wykonuje rotacje, przesuwa aktualnie
wizualizowany framgment w oknie, powiêkszanie i zmniejszanie - je¶li
posiadasz akcelerator.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
gettextize --copy --force
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README NEWS THANKS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
