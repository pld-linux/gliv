Summary:	Graphics file browser utility.
Summary(pl):	Narzêdzie do przegl±dania plików graficznych przy pomocy OpenGl  
Name:		gliv
Version:	1.5.1
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	%{name}-%{version}.tar.bz2
URL:		http://gliv.tuxfamily.org/
Vendor:		Guillaume Chazarain <booh@altern.org>
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	gtk+ >= 1.2
Requires:	gtkglarea

%description
+GLiv is an OpenGL image viewer, image loading is done through
Gdk-pixbuf (standalone or bundled with GTK+-2), rendering through
OpenGL and the graphical user interface uses GTK+ with the GtkGLArea
widget. If Gdk-pixbuf cannot load your image, it uses ImageMagick to
convert it to PNG. GLiv is very fast and smooth at rotating, panning
and zooming if you have an OpenGL accelerated board.

%description -l pl

+Gliv jest przegladarka na OpenGl'u obrazow, ladowanie obrazu odbywa 
sie poprzez Gdk-pixbuf (samodzielny lub zwiazany z GTK+-2), 
renderowanie poprzez OpenGL i interfejs graficzny uzytkownika uzywa 
GTK+ z GtkGLArea jesli Gtk-pixbuf nie moze zaladowac obrazka, wywoluje 
ImageMagick aby dokonac jego konwersji na format PNG.
GLiv jest bardzo szybki, plynnie wykonuje rotacje, przesuwaniu aktualnie 
wizualizowanego framgmentu w oknie, powiekszaniu i zmniejszaniu 
jesli posiadasz akcelerator.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT


%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README COPYING NEWS THANKS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%doc *.gz
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
