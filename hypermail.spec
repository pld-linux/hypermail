# TODO: use system pcre
Summary:	Mail(box) to HTML converter with threads and MIME support
Summary(pl.UTF-8):	Konwerter (skrzynek) poczty do HTML-a ze wsparciem dla MIME i wątków
Name:		hypermail
Version:	2.2.0
Release:	3
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/hypermail/%{name}-%{version}.tar.gz
# Source0-md5:	a064e36780ee41409c8c973f9c69927f
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

%description -l pl.UTF-8
Konwerter (skrzynek) poczty do HTML-a ze wsparciem MIME i wątków.

%prep
%setup -q
%patch0 -p1

%build
for i in . src/pcre src/fnv; do
	cp -f /usr/share/automake/config.sub $i
done;
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
