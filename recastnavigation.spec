%define sonum 1

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

%package devel
Summary:        Include Files for Recastnavigation Libraries
Requires:       libDebugUtils%{sonum} = %{version}
Requires:       libDetour%{sonum} = %{version}
Requires:       libDetourCrowd%{sonum} = %{version}
Requires:       libDetourTileCache%{sonum} = %{version}
Requires:       libRecast%{sonum} = %{version}

%description devel
This package contains files and libraries needed for develeopment with
recastnavigation libraries.

%package -n libDebugUtils%{sonum}
Summary:        Debug Utils Library for Recastnavigation

%description -n libDebugUtils%{sonum}
This package contains the debug utilities library for the recastnavigation.

%package -n libDetour%{sonum}
Summary:        Detour Library for Recastnatnaviagtion

%description -n libDetour%{sonum}
This package contains the detour library part of Recastnatnaviagtion.

%package -n libDetourCrowd%{sonum}
Summary:        Detour Crowd Library for Recastnatnaviagtion

%description -n libDetourCrowd%{sonum}
This package contains the detour crowd library part of Recastnatnaviagtion.

%package -n libDetourTileCache%{sonum}
Summary:        Detour Tile Cache Library for Recastnatnaviagtion

%description -n libDetourTileCache%{sonum}
This package contains the detour tile cache library part of Recastnatnaviagtion.

%package -n libRecast%{sonum}
Summary:        Recast Library for Recastnatnaviagtion

%description -n libRecast%{sonum}
This package contains the recast library of Recastnatnaviagtion.

%prep
%setup -q

%build
%cmake \
    -DRECASTNAVIGATION_DEMO=OFF \
    -DRECASTNAVIGATION_EXAMPLES=OFF \
    -DRECASTNAVIGATION_TESTS=OFF
%make_build

%install
%make_install -C build

%files devel
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

%files -n libDebugUtils%{sonum}
%{_libdir}/libDebugUtils.so.*

%files -n libDetour%{sonum}
%{_libdir}/libDetour.so.*

%files -n libDetourCrowd%{sonum}
%{_libdir}/libDetourCrowd.so.*

%files -n libDetourTileCache%{sonum}
%{_libdir}/libDetourTileCache.so.*

%files -n libRecast%{sonum}
%{_libdir}/libRecast.so.*
