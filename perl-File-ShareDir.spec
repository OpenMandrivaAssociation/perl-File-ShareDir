%define modname	File-ShareDir
%define modver	1.03

Summary:	Locate per-dist and per-module shared files  
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	14
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Wx/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Class::Inspector)
BuildRequires:	perl-devel

%description
Locate per-dist and per-module shared files  

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

