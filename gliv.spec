Summary:	Graphics file browser utility.
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

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
rm -rf

%{__make} install prefix=$RPM_BUILD_ROOT

%clean
rm -rf

%files
%defattr(644,root,root,755)

%doc README COPYING NEWS THANKS
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
