%define Product CMFActivity
%define product cmfactivity
%define name    zope-%{Product}
%define version 0.8
%define release %mkrel 7

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Activity Tool for zope
License:    GPL
Group:      System/Servers
URL:        https://www.erp5.org
Source:     %{Product}-%{version}.tar.bz2
Requires:   zope
Obsoletes:  %{Product}
Buildarch:  noarch
BuildRoot:  %{_tmppath}/%{name}

%description
This tools allows to implement activities for zope objects. 

%prep
%setup -q -n %{Product}-%{version}

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_libdir}/zope/lib/python/Products/%{Product}
cp -pr * %{buildroot}%{_libdir}/zope/lib/python/Products/%{Product}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc VERSION.txt
%{_libdir}/zope/lib/python/Products/%{Product}


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.8-7mdv2010.0
+ Revision: 435474
- rebuild
- rebuild

* Mon Aug 04 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.8-5mdv2009.0
+ Revision: 263094
- rebuild
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.8-2mdv2008.1
+ Revision: 136633
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.8-2mdv2008.0
+ Revision: 91825
- spec cleanup
  package renaming
- package renaming
- import CMFActivity

