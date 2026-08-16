Name:          oberon-governor
Version:       0.1
Release:       2
Summary:       GPU governor for the AMD BC-250
URL:           https://gitlab.com/mothenjoyer69/oberon-governor.git
License:       GPLv3

BuildRequires: cmake
BuildRequires: libdrm-devel
BuildRequires: cmake(yaml-cpp)
BuildSystem:   cmake

Source0: https://gitlab.com/mothenjoyer69/oberon-governor/-/archive/0.1/oberon-governor-0.1.tar.gz
Patch0:  system-yaml-cpp.patch

%description
A GPU governor that automatically manages
memory and core clocks on the AMD BC-250

%files
%license LICENSE
%{_bindir}/%{name}
%{_sysconfdir}/oberon-config.yaml
%{_unitdir}/%{name}.service
