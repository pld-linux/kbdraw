Name:		kbdraw
Summary:	GTK+ widget that draws Xkb keyboards.
Version:	0.1.0
Release:	1
License:	GPL
Group:		Development/Libraries
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


%package devel
Summary:	Libraries, includes, etc to develop kbdraw applications
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Libraries, include files, etc you can use to develop kbdraw
applications.

%package static
Summary:	Static version of kbdraw library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of kbdraw library.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README 
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
