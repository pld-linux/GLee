Summary:	OpenGL Easy Extension library
Summary(pl.UTF-8):	Biblioteka OpenGL Easy Extension
Name:		GLee
Version:	5.03
%define		_ver	%(echo %{version} | tr . _)
Release:	1
License:	BSD-like
Group:		X11/Libraries
Source0:	http://elf-stone.com/downloads/GLee/%{name}%{_ver}.zip
# Source0-md5:	92a3f9282af73b8a9966ad5a0e2eaf8d
Source1:	http://elf-stone.com/downloads/GLee/%{name}-3.03-src.tar.gz
# Source1-md5:	84664f6545ed890ea87244c1ea5b2259
URL:		http://elf-stone.com/downloads.php
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.167
BuildRequires:	unzip
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The OpenGL Easy Extension library (GLee) makes life easier for OpenGL
developers by automatically linking OpenGL extensions and core
functions at initialisation time. This saves programmers the effort of
manually linking every required extension, and effectively brings the
OpenGL library up to date.

%description -l pl.UTF-8
Biblioteka OpenGL Easy Extension (GLee) ułatwia życie programistom
używającym OpenGL poprzez automatyczne linkowanie rozszerzeń OpenGL i
głównych funkcji w czasie inicjalizacji. Oszczędza to programistom
trudów ręcznego linkowania każdego wymaganego rozszerzenia i
efektywnie czyni bibliotekę OpenGL aktualną.

%package devel
Summary:	Header file for GLee library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki GLee
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-devel

%description devel
Header file for GLee library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki GLee.

%prep
%setup -q -a1 -c
cp glee/{configure,config.h.in,install-sh,Makefile.in} .

%build
CXXFLAGS="%{rpmcxxflags} -fPIC"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir}/GL,%{_libdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INCLUDEDIR=$RPM_BUILD_ROOT%{_includedir} \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	DATADIR=$RPM_BUILD_ROOT%{_datadir} \
	LDCONFIG=/bin/true

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc extensionList.txt readme.txt
%attr(755,root,root) %{_libdir}/libGLee.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/GL/GLee.h
