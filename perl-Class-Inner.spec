%define upstream_name    Class-Inner
%define upstream_version 0.200001

Summary:	Class-Inner module for perl 
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	17
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/Class-Inner/
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
Class-Inner module for perl

%prep
%setup -qn %{upstream_name}-%{upstream_version} 

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
%{_mandir}/man3/*

