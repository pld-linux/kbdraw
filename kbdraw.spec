Summary:	GTK+ widget that draws Xkb keyboards
Summary(pl):	Widget GTK+ rysuj±cy klawiatury Xkb
Name:		kbdraw
Version:	0.1.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/kbdraw/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	6e7d260a959dce8447967d11a3850fd7
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	popt-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kbdraw is a GTK+ widget and test program that draws Xkb keyboards. It
gets the keyboard geometry and keysyms from X. It can draw any
keyboard configuration. By default it draws the current one for the
display.

%description -l pl
Kbdraw to widget GTK+ rysuj±cy klawiatury Xkb oraz program testowy dla
niego. Pobiera geometriê klawiatury oraz keysymy z X. Mo¿e narysowaæ
dowoln± konfiguracjê klawiatury. Domy¶lnie rysuje bie¿±c± dla ekranu.

%package devel
Summary:	Header files to develop kbdraw applications
Summary(pl):	Pliki nag³ówkowe do tworzenia aplikacji kbdraw
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files to develop kbdraw applications.

%description devel -l pl
Pliki nag³ówkowe do tworzenia aplikacji korzystaj±cych z kbdraw.

%package static
Summary:	Static version of kbdraw library
Summary(pl):	Statyczna wersja biblioteki kbdraw
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of kbdraw library.

%description static -l pl
Statyczna wersja biblioteki kbdraw.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README 
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
