Summary:	OpenGL Easy Extension library
Name:		GLee
Version:	3.03
Release:	0.5
License:	BSD-like
Group:		X11/Libraries
Source0:	http://elf-stone.com/downloads/GLee/%{name}-%{version}-src.tar.gz
# Source0-md5:	84664f6545ed890ea87244c1ea5b2259
URL:		http://elf-stone.com/downloads.php
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The OpenGL Easy Extension library (GLee) makes life easier for OpenGL developers by automatically linking OpenGL extensions and core functions at initialisation time. This saves programmers the effort of manually linking every required extension, and effectively brings the OpenGL library up to date.

%prep
%setup -q -n glee

%build
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
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/GL/*
