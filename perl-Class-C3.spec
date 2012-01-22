%define upstream_name	 Class-C3
%define upstream_version 0.23

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 5

Summary:	A pragma to use the C3 method resolution order algortihm
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Algorithm::C3) >= 0.05
BuildRequires:	perl(Scalar::Util) >= 1.10
BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:	perl(Test::Exception) >= 0.15
BuildRequires:	perl(Class::C3::XS) >= 0.07
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
Requires:	    perl(Algorithm::C3)

%description
This is pragma to change Perl 5's standard method resolution order
from depth-first left-to-right (a.k.a - pre-order) to the more
sophisticated C3 method resolution order.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_mandir}/man*/*
%{perl_vendorlib}/Class
