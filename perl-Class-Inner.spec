Summary:	Class-Inner module for perl 
Name:		perl-Class-Inner
Version:	0.1
Release:	%mkrel 7
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://www.cpan.org
Source0:	Class-Inner-%{version}.tar.bz2
Patch0:		Class-Inner-test_fix.diff
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Class-Inner module for perl

%prep

%setup -q -n Class-Inner-%{version} 
%patch0 -p0

# perl path hack
find . -type f | xargs perl -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor

%make OPTIMIZE="%{optflags}"

make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class/*
%{_mandir}/*/*
