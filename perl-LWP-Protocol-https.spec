#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	LWP
%define		pnam	Protocol-https
Summary:	LWP::Protocol::https - Provide https support for LWP::UserAgent
Summary(pl.UTF-8):	LWP::Protocol::https - obsługa https dla LWP::UserAgent
Name:		perl-LWP-Protocol-https
Version:	6.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/LWP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cf64e4bc57a9266ac4343cdf0808c5c8
URL:		http://search.cpan.org/dist/LWP-Protocol-https/
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-IO-Socket-SSL >= 1:1.54
BuildRequires:	perl-Mozilla-CA >= 20180117
BuildRequires:	perl-Net-HTTP >= 6
BuildRequires:	perl-Test-RequiresInternet
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-libwww >= 6.06
%endif
BuildRequires:	perl-Mozilla-CA >= 20180117
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The LWP::Protocol::https module provide support for using https
schemed URLs with LWP. This module is a plug-in to the LWP protocol
handling, so you don't use it directly. Once the module is installed
LWP is able to access sites using HTTP over SSL/TLS.

%description -l pl.UTF-8
Moduł LWP::Protocol::https zapewnia obsługę URL-i ze schematu https w
LWP. Ten moduł jest wtyczką do obsługi protokołu w LWP, więc nie używa
się go bezpośrednio. Po zainstalowaniu modułu LWP potrafi łączyć się z
serwisami przy użyciu HTTP po SSL/TLS.

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
%doc CONTRIBUTING.md Changes Install
%{perl_vendorlib}/LWP/Protocol/https.pm
%{_mandir}/man3/LWP::Protocol::https.3pm*
