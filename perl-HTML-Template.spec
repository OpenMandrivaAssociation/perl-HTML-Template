%define module  HTML-Template
%define	name	perl-%{module}
%define version 2.9
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Perl module to use HTML Templates from CGI scripts
License: 	GPL or Artistic
Group: 		Development/Perl
Source: 	http://search.cpan.org/CPAN/authors/id/S/SA/SAMTREGAR/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(CGI)
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
This module attempts make using HTML templates simple and natural. It
extends standard HTML with a few new HTML-esque tags - <TMPL_VAR>,
<TMPL_LOOP>, <TMPL_INCLUDE>, <TMPL_IF> and <TMPL_ELSE>. The file
written with HTML and these new tags is called a template. It is
usually saved separate from your script - possibly even created by
someone else!  Using this module you fill in the values for the
variables, loops and branches declared in the template. This allows
you to separate design - the HTML - from the data, which you generate
in the Perl script.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ANNOUNCE ARTISTIC Changes FAQ README
%{perl_vendorlib}/HTML
%{_mandir}/*/*

