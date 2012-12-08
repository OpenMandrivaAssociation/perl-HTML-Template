%define upstream_name    HTML-Template
%define upstream_version 2.9

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Perl module to use HTML Templates from CGI scripts
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/S/SA/SAMTREGAR/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(CGI)

BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc ANNOUNCE ARTISTIC Changes FAQ README
%{perl_vendorlib}/HTML
%{_mandir}/*/*

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.900.0-4mdv2012.0
+ Revision: 765307
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.900.0-3
+ Revision: 763860
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.900.0-2
+ Revision: 667197
- mass rebuild

* Sun Feb 14 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.900.0-1mdv2010.1
+ Revision: 505767
- rebuild using %%perl_convert_version

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.9-4mdv2010.0
+ Revision: 426505
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.9-3mdv2009.0
+ Revision: 223791
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 2.9-2mdv2008.1
+ Revision: 180408
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 2.9-1mdv2008.0
+ Revision: 20175
- buildrequires
- 2.9


* Tue Dec 27 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.8-1mdk
- New release 2.8
- spec cleanup
- fix sources URL
- better summary and description
- %%mkrel

* Thu Jul 08 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.7-1mdk
- 2.7
- drop redundant requires

* Thu Aug 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.6-5mdk
- rebuild for new perl
- drop $RPM_OPT_FLAGS
- rm -rf /home/guillomovitch/rpm/tmp/perl-HTML-Template-2.8 in %%install, not %%build
- use %%makeinstall_std macro

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.6-4mdk
- rebuild for new auto{prov,req}

* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.6-3mdk
- rebuild

* Thu Oct 24 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.6-2mdk
- from Peter Chen <petechen@netilla.com> :
	- Minor fix in spec file and source permission to appease rpmlint.

* Wed Oct 23 2002 Peter Chen <petechen@netilla.com> 2.6-1mdk
- 2.6
- First packaging.

