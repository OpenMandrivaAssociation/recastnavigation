%define sonum 1
%define libname %mklibname recastnavigation
%define devname %mklibname -d recastnavigation

Name:           recastnavigation
Version:        1.6.0
Release:        1
Summary:        Recast & Detour
License:        Zlib
URL:            https://github.com/recastnavigation/recastnavigation
Source:         %{url}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig(glu)

%description
Recast is state of the art navigation mesh construction toolset for games.
Recast is accompanied with Detour, path-finding and spatial reasoning toolkit.
You can use any navigation mesh with Detour, but of course the data generated
with Recast fits perfectly.

%package -n %{libname}
Summary:        Shared library for %{name}
Provides:    recastnavigation-lib = %{EVRD}

%description -n %{libname}
This package contains the shared library files.

%package -n %{devname}
Summary:        Development files for %{name}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
This package contains development files for %{name}.

%prep
%autosetup -p1

%build
%cmake \
    -DRECASTNAVIGATION_DEMO=OFF \
    -DRECASTNAVIGATION_EXAMPLES=OFF \
    -DRECASTNAVIGATION_TESTS=OFF
%make_build

%install
%make_install -C build

%files -n %{devname}
%license License.txt
%doc README.md
%{_libdir}/libDebugUtils.so
%{_libdir}/libDetour.so
%{_libdir}/libDetourCrowd.so
%{_libdir}/libDetourTileCache.so
%{_libdir}/libRecast.so
%{_includedir}/recastnavigation
%{_libdir}/pkgconfig/recastnavigation.pc
%{_libdir}/cmake/%{name}

%files -n %{libname}
%{_libdir}/libDebugUtils.so.*
%{_libdir}/libDetour.so.*
%{_libdir}/libDetourCrowd.so.*
%{_libdir}/libDetourTileCache.so.*
%{_libdir}/libRecast.so.*
