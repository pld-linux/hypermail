Summary:	Mail(box) to HTML converter with threads and MIME support
Summary(pl):	Konwerter (skrzynek) poczty do HTML ze wsparciem MIME i w±tków
Name:		hypermail
Version:	2.1.3
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.hypermail.org/dist/%{name}-%{version}.tar.gz
Patch0:		%{name}-pcre.patch
URL:		http://www.hypermail.org/
BuildRequires:	gdbm-devel
BuildRequires:	pcre-devel
BuildRequires:	autoconf
BuildRequires:	bison
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail(box) to HTML converter with threads and MIME support.

%description -l pl
Konwerter (skrzynek) poczty do HTML ze wsparciem MIME i w±tków.

%prep
%setup -q
%patch0 -p1

%build
aclocal
autoconf
%configure \
	--with-httpddir=/home/httpd \
	--with-htmldir=/home/httpd/html \
	--with-domainaddr=localhost \
	--with-gdbm	

%{__make} all

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall} \
	httpddir=$RPM_BUILD_ROOT/home/httpd \
	htmldir=$RPM_BUILD_ROOT/home/httpd/html

gzip -9nf KNOWN_BUGS README TODO UPGRADE docs/*.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz docs/*.gz docs/*.html docs/*.gif
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
