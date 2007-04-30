%define module	Class-C3
%define	modprefix Class

%define version	0.15_05
%define release	%mkrel 1

Summary:	A pragma to use the C3 method resolution order algortihm
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildRoot:	%{_tmppath}/%{name}-buildroot
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Algorithm::C3) >= 0.05
BuildRequires:	perl(Scalar::Util) >= 1.10
BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:	perl(Test::Exception) >= 0.15
BuildArch:	noarch

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
%defattr(644,root,root,755)
%doc ChangeLog README
%{_mandir}/man*/*
%{perl_vendorlib}/%{modprefix}

