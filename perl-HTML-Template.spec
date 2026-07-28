%define modname	HTML-Template
%define modver	2.97

Summary:	Perl module to use HTML Templates from CGI scripts
Name:		perl-%{modname}
Version:	%{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://github.com/mpeters/html-template
Source0:	https://cpan.metacpan.org/authors/id/S/SA/SAMTREGAR/HTML-Template-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildRequires:	perl(CGI)

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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/HTML
%{_mandir}/man3/*

