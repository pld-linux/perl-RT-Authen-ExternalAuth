#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	RT
%define	pnam	Authen-ExternalAuth
Summary:	RT::Authen::ExternalAuth - RT Authentication using External Sources
Name:		perl-RT-Authen-ExternalAuth
Version:	0.08
Release:	1
License:	GPL version 2
Group:		Development/Languages/Perl
URL:		http://search.cpan.org/dist/RT-Authen-ExternalAuth/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rt >= 3.8.0
Source0:	http://www.cpan.org/modules/by-module/RT/%{pdir}-%{pnam}-%{version}.tar.gz	
# Source0-md5:	ba591003a2ca39ac2965b548e158a34f
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A complete package for adding external authentication mechanisms to
RT. It currently supports LDAP via Net::LDAP and External Database
authentication for any database with an installed DBI driver.

It also allows for authenticating cookie information against an
external database through the use of the RT-Authen-CookieAuth
extension.

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
%doc ChangeLog README
%{perl_vendorlib}/RT/*.pm
%dir %{perl_vendorlib}/RT/Authen
%{perl_vendorlib}/RT/Authen/*.pm
%dir %{perl_vendorlib}/RT/Authen/ExternalAuth
%{perl_vendorlib}/RT/Authen/ExternalAuth/*.pm
%dir %{perl_vendorlib}/RT/Authen/ExternalAuth/DBI/
%{perl_vendorlib}/RT/Authen/ExternalAuth/DBI/*.pm
%{_mandir}/man3/*
