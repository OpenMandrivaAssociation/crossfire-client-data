%define	version	1.50.0
%define	release %mkrel 1

Name:		crossfire-client-data
Version:	%{version}
Release:	%{release}
Summary:	Data files for Crossfire game clients
Group:		Games/Adventure
License:	GPL
URL:		http://crossfire.real-time.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch

Source0:	http://prdownloads.sourceforge.net/crossfire/crossfire-client-sounds-%{version}.tar.gz
Source1:	http://prdownloads.sourceforge.net/crossfire/crossfire-client-images-%{version}.tar.gz

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
rm -rf %{buildroot}

# extract cache images to buildroot
mkdir -p %{buildroot}%{_gamesdatadir}/crossfire-client/
tar -xvf %{SOURCE0} -C %{buildroot}%{_gamesdatadir}/crossfire-client/
tar -xvf %{SOURCE1} -C %{buildroot}%{_gamesdatadir}/crossfire-client/

#remove debian files
rm -rf %{buildroot}%{_gamesdatadir}/crossfire-client/sounds/debian

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%{_gamesdatadir}/crossfire-client/*
