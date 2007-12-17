Summary:	Class-Inner module for perl 
Name:		perl-Class-Inner
Version:	0.1
Release:	%mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
Source0:	Class-Inner-%{version}.tar.bz2
URL:		http://www.cpan.org
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Class-Inner module for perl

%prep

%setup -q -n Class-Inner-%{version} 

# perl path hack
find . -type f | xargs perl -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor

%make OPTIMIZE="%{optflags}"

make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std


%clean 
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class/*
%{_mandir}/*/*


