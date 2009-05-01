%define module	Class-C3
%define	modprefix Class
%define version	0.21
%define release	%mkrel 1

Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
Summary:	A pragma to use the C3 method resolution order algortihm
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source0:	http://www.cpan.org/modules/by-module/Class/%{module}-%{version}.tar.gz
BuildRequires:	perl(Algorithm::C3) >= 0.05
BuildRequires:	perl(Scalar::Util) >= 1.10
BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:	perl(Test::Exception) >= 0.15
BuildRequires:	perl(Class::C3::XS) >= 0.07
Requires:	    perl(Algorithm::C3)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is pragma to change Perl 5's standard method resolution order
from depth-first left-to-right (a.k.a - pre-order) to the more
sophisticated C3 method resolution order.


%prep
%setup -q -n %{module}-%{version}

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
%{perl_vendorlib}/%{modprefix}

