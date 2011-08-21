Summary:	A Python wrapper for the GPGME library
Summary(pl.UTF-8):	Pythonowy interfejs do biblioteki GPGME
Name:		python-pygpgme
Version:	0.2
Release:	1
License:	LGPL v2.1+
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/p/pygpgme/pygpgme-%{version}.tar.gz
# Source0-md5:	674e3f5374efa2aaac7ab420810c91e6
URL:		https://launchpad.net/products/pygpgme
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	gpgme-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyGPGME is a Python module that lets you sign, verify, encrypt and
decrypt messages using the OpenPGP format.

%description -l pl.UTF-8
PyGPGME to moduł Pythona pozwalający podpisywać, weryfikować,
szyfrować i odszyfrowywać wiadomości w formacie OpenPGP.

%prep
%setup -q -n pygpgme-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/gpgme/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{py_sitedir}/gpgme
%attr(755,root,root) %{py_sitedir}/gpgme/_gpgme.so
%{py_sitedir}/gpgme/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitedir}/pygpgme-%{version}-py*.egg-info
%endif
