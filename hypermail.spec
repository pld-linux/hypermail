Summary:	Mail(box) to HTML converter with threads and MIME support
Summary(pl):	Konwerter (skrzynek) poczty do HTML-a ze wsparciem dla MIME i w±tków
Name:		hypermail
Version:	2.1.8
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.hypermail.org/dist/%{name}-%{version}.tar.gz
# Source0-md5:	bacd95589f2f3ca426631461fd9237dd
Patch0:		%{name}-pcre.patch
URL:		http://www.hypermail.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	gdbm-devel
BuildRequires:	pcre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		httpdir		/home/services/httpd
%define		htmldir		/home/services/httpd/html

%description
Mail(box) to HTML converter with threads and MIME support.

%description -l pl
Konwerter (skrzynek) poczty do HTML-a ze wsparciem MIME i w±tków.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure \
	--with-httpddir=%{httpdir} \
	--with-htmldir=%{htmldir} \
	--with-domainaddr=localhost \
	--with-gdbm

%{__make} all

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall} \
	httpddir=$RPM_BUILD_ROOT%{httpdir} \
	htmldir=$RPM_BUILD_ROOT%{htmldir} \
	imagedir=$RPM_BUILD_ROOT%{htmldir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc KNOWN_BUGS README TODO UPGRADE docs/*.txt docs/*.html docs/*.png
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
