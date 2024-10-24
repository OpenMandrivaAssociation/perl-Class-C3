%define upstream_name	 Class-C3

Summary:	A pragma to use the C3 method resolution order algortihm
Name:		perl-%{upstream_name}
Version:	0.35
Release:	1
License:	Artistic/GPLv2
Group:		Development/Perl
Url:		https://metacpan.org/pod/Class::C3
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Algorithm::C3)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Class::C3::XS)
Requires:	perl(Algorithm::C3)

%description
This is pragma to change Perl 5's standard method resolution order
from depth-first left-to-right (a.k.a - pre-order) to the more
sophisticated C3 method resolution order.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make test

%install
%make_install

%files
%doc  README
%{perl_vendorlib}/Class
%{_mandir}/man3/*
