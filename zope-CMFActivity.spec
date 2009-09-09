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
URL:        http://www.erp5.org
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
