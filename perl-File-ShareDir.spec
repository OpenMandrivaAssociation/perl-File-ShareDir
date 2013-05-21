%define upstream_name    File-ShareDir
%define upstream_version 1.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Locate per-dist and per-module shared files  
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Wx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Class::Inspector)
BuildRequires:	perl-devel

BuildArch:	noarch

%description
Locate per-dist and per-module shared files  

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.30.0-4mdv2012.0
+ Revision: 765249
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.30.0-3
+ Revision: 763763
- rebuilt for perl-5.14.x

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.30.0-2
+ Revision: 654329
- rebuild for updated spec-helper

* Wed Feb 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.30.0-1
+ Revision: 635186
- update to new version 1.03

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.20.0-2mdv2011.0
+ Revision: 607088
- rebuild

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2010.1
+ Revision: 526440
- update to 1.02

* Tue Nov 24 2009 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-1mdv2010.1
+ Revision: 469430
- update to 1.01

* Mon Aug 31 2009 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-2mdv2010.0
+ Revision: 422794
- force rebuild

* Sat Aug 30 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.00-1mdv2009.0
+ Revision: 277666
- import perl-File-ShareDir


