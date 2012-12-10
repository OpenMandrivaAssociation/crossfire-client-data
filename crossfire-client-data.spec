%define	version	1.70.0
%define	release %mkrel 2

Name:		crossfire-client-data
Version:	%{version}
Release:	%{release}
Summary:	Data files for Crossfire game clients
Group:		Games/Adventure
License:	GPL
URL:		http://crossfire.real-time.com/
BuildArch:	noarch

Source0:	http://downloads.sourceforge.net/project/crossfire/crossfire-%{version}/crossfire-client-sounds-%{version}.tar.gz
Source1:	http://downloads.sourceforge.net/project/crossfire/crossfire-%{version}/crossfire-client-images-%{version}.tar.gz

%description
Crossfire is a highly graphical role-playing adventure game with
characteristics reminiscent of rogue, nethack, omega, and gauntlet. 
It has multiplayer capability and presently runs under X11.

This package contains data files for Crossfire game clients.
It includes sound files and image cache.

%prep
%setup -q -c -T

%build

%install
# extract cache images to buildroot
mkdir -p %{buildroot}%{_gamesdatadir}/crossfire-client/
tar -xvf %{SOURCE0} -C %{buildroot}%{_gamesdatadir}/crossfire-client/
tar -xvf %{SOURCE1} -C %{buildroot}%{_gamesdatadir}/crossfire-client/

#remove debian files
rm -rf %{buildroot}%{_gamesdatadir}/crossfire-client/sounds/debian

%files
%defattr(0644,root,root,0755)
%{_gamesdatadir}/crossfire-client/*
