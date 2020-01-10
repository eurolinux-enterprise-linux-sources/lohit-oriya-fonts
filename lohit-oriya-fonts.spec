%global fontname lohit-oriya
%global fontconf 65-0-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        2.5.4.1
Release:        3%{?dist}
Summary:        Free Odia Font

Group:          User Interface/X
License:        OFL
URL:            https://fedorahosted.org/lohit/
Source0:        https://fedorahosted.org/releases/l/o/lohit/%{fontname}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:      noarch
BuildRequires: fontforge >= 20080429
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem


%description
This package provides a free Odia truetype/opentype font.


%prep
%setup -q -n %{fontname}-%{version} 
mv 66-%{fontname}.conf 65-0-lohit-oriya.conf


%build
make ttf

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%_font_pkg -f %{fontconf} *.ttf

%doc ChangeLog COPYRIGHT OFL.txt AUTHORS README


%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.5.4.1-3
- Mass rebuild 2013-12-27

* Thu Dec 26 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.4.1-2
- Resolves: rhbz#1046263 :- Replaced Oriya with Odia

* Wed Jun 19 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.4.1-1
- Upstream release 2.5.4.1

* Wed May 29 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.4-1
- Upstream release 2.5.4

* Fri Apr 26 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-3
- Resolved #923215: UTRRS 123 GSub combination and other ligature

* Fri Apr 12 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-2
- Resolved #950520

* Thu Jan 31 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-1
- Upstream release 2.5.3

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-1
- Upstream new release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 10 2011 Pravin Satpute <psatpute@redhat.com> - 2.5.0-1
- Upstream new release with relicensing to OFL

* Wed Apr 13 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.3-9
- Resolved bug 692364

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 08 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.3-7
- resolved bug 673417, added rupee sign

* Mon Oct 25 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-6
- fixed bug 639977, resolved problem of ligature rendering with gedit and oowriter

* Wed Aug 25 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-5
- fixed bug 623995, problem with kwrite/qt

* Fri Apr 16 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-4
- fixed bug 578037, conf file

* Sun Dec 13 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-3
- fixed bug 548686, license field
- corrected source url

* Fri Sep 25 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-2
- updated specs
	
* Fri Sep 11 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-1
- first release after lohit-fonts split in new tarball
