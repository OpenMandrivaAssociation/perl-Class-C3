%define upstream_name	 Class-C3
%define upstream_version 0.34

Summary:	A pragma to use the C3 method resolution order algortihm
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
License:	Artistic/GPLv2
Group:		Development/Perl
Url:		http://metacpan.org/pod/Class::C3
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Algorithm::C3) >= 0.05
BuildRequires:	perl(Scalar::Util) >= 1.10
BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:	perl(Test::Exception) >= 0.15
BuildRequires:	perl(Class::C3::XS) >= 0.07
Requires:	perl(Algorithm::C3)

%description
This is pragma to change Perl 5's standard method resolution order
from depth-first left-to-right (a.k.a - pre-order) to the more
sophisticated C3 method resolution order.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc  README
%{perl_vendorlib}/Class
%{_mandir}/man3/*
