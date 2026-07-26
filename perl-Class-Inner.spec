%define upstream_name    Class-Inner
Summary:	Class-Inner module for perl 
Name:		perl-%{upstream_name}
Version:	0.200001
Release:	20
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Class-Inner
Source0:	https://cpan.metacpan.org/authors/id/A/AR/ARUNBEAR/Class-Inner-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
Class-Inner module for perl

%prep
%setup -qn %{upstream_name}-%{version} 

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

