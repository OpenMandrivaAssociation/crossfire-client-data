%define	version	1.11.0
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

Source0:	http://prdownloads.sourceforge.net/crossfire/crossfire-client-sounds-%{version}.tar.bz2
Source1:	http://prdownloads.sourceforge.net/crossfire/crossfire-client-images-%{version}.tar.bz2

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
bzip2 -dc %{SOURCE0} | tar -x -C %{buildroot}%{_gamesdatadir}/crossfire-client/
bzip2 -dc %{SOURCE1} | tar -x -C %{buildroot}%{_gamesdatadir}/crossfire-client/
find %{buildroot}%{_gamesdatadir}/crossfire-client -type f -print0 | xargs -r -0 chmod 0644

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_gamesdatadir}/crossfire-client

