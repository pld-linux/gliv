Summary:	Graphics file browser utility
Summary(pl.UTF-8):	Narzędzie do przeglądania plików graficznych przy pomocy OpenGL
Name:		gliv
Version:	1.9.7
Release:	1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://guichaz.free.fr/gliv/files/%{name}-%{version}.tar.bz2
# Source0-md5:	5f0fafaf41651da8882e88b3df062d02
Patch0:		%{name}-link.patch
URL:		http://guichaz.free.fr/gliv/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	gtkglext-devel >= 1.0.0
BuildRequires:	pkgconfig
Requires:	gtk+2 >= 2:2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
GLiv is an OpenGL image viewer, image loading is done through
Gdk-pixbuf (standalone or bundled with GTK+-2), rendering through
OpenGL and the graphical user interface uses GTK+ with the GtkGLArea
widget. If Gdk-pixbuf cannot load your image, it uses ImageMagick to
convert it to PNG. GLiv is very fast and smooth at rotating, panning
and zooming if you have an OpenGL accelerated board.

%description -l pl.UTF-8
Gliv jest przeglądarką obrazków używającą OpenGL; ładowanie obrazka
odbywa się poprzez Gdk-pixbuf (samodzielny lub związany z GTK+-2),
renderowanie poprzez OpenGL, a interfejs graficzny użytkownika używa
GTK+ z GtkGLArea. Jeśli Gtk-pixbuf nie może załadować obrazka,
wywołuje ImageMagick aby dokonać jego konwersji na format PNG. GLiv
jest bardzo szybki, płynnie wykonuje rotacje, przesuwa aktualnie
wizualizowany fragment w oknie, powiększanie i zmniejszanie - jeśli
posiadasz akcelerator.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%doc NEWS README THANKS
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/gliv.1*
%lang(cs) %{_mandir}/cs/man1/gliv.1*
%lang(de) %{_mandir}/de/man1/gliv.1*
%lang(fr) %{_mandir}/fr/man1/gliv.1*
%lang(ru) %{_mandir}/ru/man1/gliv.1*
