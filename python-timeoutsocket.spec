%include	/usr/lib/rpm/macros.python

%define		module timeoutsocket

Summary:	Timeout Socket Python module
Summary(pl):	Modu³ Pythona Timeout Socket
Name:		python-%{module}
Version:	1.23
Release:	2
License:	distributable
Group:		Development/Languages/Python
Source0:	http://www.timo-tasi.org/python/timeoutsocket.py
# Source0-md5:	137f1e1fe6e250896f01a589c25b44eb
URL:		http://www.timo-tasi.org/python/
%pyrequires_eq	python
BuildRequires:	rpm-pythonprov
BuildRequires:	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module enables a timeout mechanism on all TCP connections. It
does this by inserting a shim into the socket module. After this
module has been imported, all socket creation goes through this shim.
As a result, every TCP connection will support a timeout.

%description -l pl
Ten modu³ dodaje mechanizm limitu czasowego dla wszystkich po³±czeñ
TCP. Modu³ robi to poprzez do³o¿enie wk³adki do modu³u socket. Po
zaimportowaniu tego modu³u, ka¿de tworzenie gniazd przechodzi przez tê
wk³adkê. W efekcie ka¿de po³±czenie TCP obs³uguje limit czasowy.

%prep
python <<EOF
import sys
d={}
execfile("%{SOURCE0}",d,d)
if d["__version__"].split()[1]!="%{version}":
	print >>sys.stderr,"Source version mismatch!"
	sys.exit(1)
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

install %{SOURCE0} $RPM_BUILD_ROOT%{py_sitescriptdir}

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}

rm $RPM_BUILD_ROOT%{py_sitescriptdir}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.py?
