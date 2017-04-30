%?mingw_package_header

Name:           mingw-zeromq
Version:        4.2.1
Release:        1%{?dist}
Summary:        MinGW port of ZeroMQ

License:        LGPL
URL:            http://zeromq.org
Source0:        https://github.com/zeromq/libzmq/releases/download/v%{version}/zeromq-%{version}.tar.gz

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-libsodium
BuildRequires:  mingw64-libsodium

BuildArch:      noarch

%description
MinGW Windows port of ZeroMQ.

# Win32
%package -n mingw32-zeromq
Summary:        32-bit version of ZeroMQ for Windows

%description -n mingw32-zeromq
%mingw32_description

# Win64
%package -n mingw64-zeromq
Summary:        64-bit version of ZeroMQ for Windows

%description -n mingw64-zeromq
%mingw64_description

%?mingw_debug_package

%prep
%setup -qn zeromq-%{version}

%build
%mingw_configure \
    --disable-static \
    --with-libsodium \
    --disable-silent-rules
%mingw_make %{?_smp_mflags}

%install
%mingw_make install DESTDIR=%{buildroot}
find %{buildroot} -name "*.la" -delete

# Win32
%files -n mingw32-zeromq
%{mingw32_bindir}/curve_keygen.exe
%{mingw32_bindir}/libzmq.dll
%{mingw32_includedir}/zmq.h
%{mingw32_includedir}/zmq_utils.h
%{mingw32_libdir}/libzmq.dll.a
%{mingw32_libdir}/pkgconfig/libzmq.pc

# Win64
%files -n mingw64-zeromq
%{mingw64_bindir}/curve_keygen.exe
%{mingw64_bindir}/libzmq.dll
%{mingw64_includedir}/zmq.h
%{mingw64_includedir}/zmq_utils.h
%{mingw64_libdir}/libzmq.dll.a
%{mingw64_libdir}/pkgconfig/libzmq.pc

%changelog
* Sun Apr 30 2017 Jajauma's Packages <jajauma@yandex.ru> - 4.2.1-1
- Initial release
