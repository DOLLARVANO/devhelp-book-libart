Summary:	DevHelp book: libart
Summary(pl):	Ksi±¿ka do DevHelp'a o libart
Name:		devhelp-book-libart
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/libart.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about libart

%description -l pl
Ksi±¿ka do DevHelp o libart

%prep
%setup -q -c libart -n libart

%build
mv -f book libart
mv -f book.devhelp libart.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/libart
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install libart.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install libart/* $RPM_BUILD_ROOT%{_prefix}/books/libart

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs
