%define upstream_name    Class-Inner
%define upstream_version 0.200001

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Class-Inner module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/Class-Inner/
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Class-Inner module for perl

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

# perl path hack
find . -type f | xargs perl -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Class/*
%{_mandir}/*/*

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.200.1-4mdv2012.0
+ Revision: 765086
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.200.1-3
+ Revision: 763530
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.200.1-2
+ Revision: 667043
- mass rebuild

* Sun Nov 22 2009 Jérôme Quelin <jquelin@mandriva.org> 0.200.1-1mdv2011.0
+ Revision: 468894
- update to 0.200001

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.1-7mdv2010.0
+ Revision: 430329
- rebuild

* Mon Sep 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1-6mdv2009.0
+ Revision: 289445
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.1-3mdv2008.1
+ Revision: 136683
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Mar 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1-3mdv2007.1
+ Revision: 138899
- use the %%mkrel macro

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Class-Inner

* Sun Jan 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1-2mdk
- rebuild

* Thu Dec 02 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.1-1mdk
- initial mandrake package

