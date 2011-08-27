#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	LWP
%define		pnam	Protocol-https
%include	/usr/lib/rpm/macros.perl
Summary:	LWP::Protocol::https - Provide https support for LWP::UserAgent
#Summary(pl.UTF-8):	
Name:		perl-LWP-Protocol-https
Version:	6.02
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/LWP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a37185492b15ad5ac13da4aef48bd388
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/LWP-Protocol-https/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Mozilla::CA) >= 20110101
BuildRequires:	perl-IO-Socket-SSL >= 1:1.38
BuildRequires:	perl-libwww >= 6.02
BuildRequires:	perl-Net-HTTP >= 6
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The LWP::Protocol::https module provide support for using https schemed
URLs with LWP.  This module is a plug-in to the LWP protocol handling, so
you don't use it directly.  Once the module is installed LWP is able
to access sites using HTTP over SSL/TLS.

If hostname verification is requested by LWP::UserAgent's ssl_opts, and
neither SSL_ca_file nor SSL_ca_path is set, then SSL_ca_file is
implied to be the one provided by Mozilla::CA.  If the Mozilla::CA module
isn't available SSL requests will fail.  Either install this module, set up an
alternative SSL_ca_file or disable hostname verification.

This module used to be bundled with the libwww-perl, but it was unbundled in
v6.02 in order to be able to declare its dependencies properly for the CPAN
tool-chain.  Applications that need https support can just declare their
dependency on LWP::Protocol::https and will no longer need to know what
underlying modules to install.



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/LWP/Protocol/*.pm
%{_mandir}/man3/*
