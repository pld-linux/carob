%define	_ver	%(echo %{version} |tr . _)
Summary:	Carob library
Summary(pl):	Biblioteka carob
Name:		carob
Version:	0.6.2
Release:	0.2
License:	Apache License v2.0
Group:		Libraries
Source0:	https://forge.continuent.org/frs/download.php/182/%{name}-r%{_ver}.tar.gz
# Source0-md5:	6969f74fa9f4c19c434b68d29590eb3a
URL:		http://carob.continuent.org/HomePage
BuildRequires:	gmp-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bringing Sequoia technology to the C/C++ world.

Carob's base is a C++ port of the JDBC driver code. It offers to
developpers the same access as in Java. Connections, Requests,
ResultSets and all necessary C++ classes can be used transparently and
directly in any C++ enabled application.

%package devel
Summary:	Header files for carob library
Summary(pl):	Pliki nag³ówkowe biblioteki carob
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for carob library.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki carob.

%package static
Summary:	Static carob library
Summary(pl):	Statyczna biblioteka carob
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static carob library.

%description static -l pl
Statyczna biblioteka carob.

%prep
%setup -q -n %{name}-r%{_ver}

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -fPIC" \
	LDFLAGS="%{rpmldflags} -lpthread"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_includedir}/carob,%{_libdir}}
install libcarob.so.1 $RPM_BUILD_ROOT%{_libdir}
install libcarob.a $RPM_BUILD_ROOT%{_libdir}
install include/*.hpp $RPM_BUILD_ROOT%{_includedir}/carob
ln -s libcarob.so.1 $RPM_BUILD_ROOT%{_libdir}/libcarob.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libcarob.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcarob.so
%{_includedir}/carob

%files static
%defattr(644,root,root,755)
%{_libdir}/libcarob.a
