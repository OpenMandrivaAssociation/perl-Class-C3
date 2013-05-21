%define upstream_name	 Class-C3
%define upstream_version 0.23

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

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
BuildRequires:	perl-devel
BuildArch:	noarch
Requires:		perl(Algorithm::C3)

%description
This is pragma to change Perl 5's standard method resolution order
from depth-first left-to-right (a.k.a - pre-order) to the more
sophisticated C3 method resolution order.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{_mandir}/man*/*
%{perl_vendorlib}/Class

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.230.0-5mdv2012.0
+ Revision: 765082
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.230.0-4
+ Revision: 763525
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.230.0-3
+ Revision: 676880
- rebuild
- mass rebuild

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.230.0-1mdv2011.0
+ Revision: 553071
- update to 0.23

* Fri Jan 29 2010 Jérôme Quelin <jquelin@mandriva.org> 0.220.0-1mdv2010.1
+ Revision: 497908
- update to 0.22

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.210.0-1mdv2010.0
+ Revision: 406315
- rebuild using %%perl_convert_version

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.21-1mdv2010.0
+ Revision: 370018
- update to new version 0.21

* Fri Dec 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-1mdv2009.1
+ Revision: 313586
- new release

* Wed Oct 01 2008 Oden Eriksson <oeriksson@mandriva.com> 0.19-5mdv2009.0
+ Revision: 290361
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Jul 05 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.19-2mdv2008.0
+ Revision: 48599
- fix dependencies

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.19-1mdv2008.0
+ Revision: 47924
- fix build dependencies
- update to new version 0.19

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 0.15_05-1mdv2008.0
+ Revision: 19778
- 0.15_05


* Sun Aug 27 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-27 12:49:44 (58210)
- Version 0.13

* Fri Aug 04 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-04 23:01:57 (53121)
Version 0.12

* Fri Aug 04 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-04 22:56:48 (53119)
import perl-Class-C3-0.11-1mdk

* Mon May 22 2006 Scott Karns <scottk@mandriva.org> 0.11-1mdk
- Initial MDV release

