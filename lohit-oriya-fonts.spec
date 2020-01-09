%global fontname lohit-oriya
%global fontconf 66-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        2.4.3
Release:        5%{?dist}
Summary:        Free Oriya Font

Group:          User Interface/X
License:        GPLv2 with exceptions
URL:            https://fedorahosted.org/lohit/
Source0:        http://pravins.fedorapeople.org/lohit/oriya/%{fontname}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:      noarch
BuildRequires: fontforge >= 20080429
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem
Patch1: bug-549319-578037.patch
Patch2: bug-623995.patch
Patch3: bug-639977.patch
Obsoletes: lohit-fonts-common < %{version}-%{release}

%description
This package provides a free Oriya truetype/opentype font.


%prep
%setup -q -n %{fontname}-%{version} 
%patch1 -p1 -b .1-fix-font-conf
%patch2 -p1 -b .2-fix-for-qt
%patch3 -p1 -b .3-added-akhn-ligature-gsub

%build
./generate.pe *.sfd

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%clean
rm -fr %{buildroot}


%_font_pkg -f %{fontconf} *.ttf

%doc ChangeLog COPYRIGHT COPYING AUTHORS README ChangeLog.old


%changelog
* Mon Jan 24 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.3-5
- Resolves: bug 623990

* Tue May 04 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-4
- Resolves: bug 586864

* Tue Dec 29 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-3
- fixed bug 548686, license field
- Resolves: bug 551013

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.4.3-2.1
- Rebuilt for RHEL 6

* Fri Sep 25 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-2
- updated specs
	
* Fri Sep 11 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-1
- first release after lohit-fonts split in new tarball
