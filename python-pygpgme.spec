#
# conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
#
Summary:	A Python 2 wrapper for the GPGME library
Summary(pl.UTF-8):	Interfejs Pythona 2 do biblioteki GPGME
Name:		python-pygpgme
Version:	0.3
Release:	8
License:	LGPL v2.1+
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/p/pygpgme/pygpgme-%{version}.tar.gz
# Source0-md5:	d38355af73f0352cde3d410b25f34fd0
URL:		https://launchpad.net/products/pygpgme
BuildRequires:	gpgme-devel
%if %{with python2}
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-modules >= 1:2.4
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyGPGME is a Python module that lets you sign, verify, encrypt and
decrypt messages using the OpenPGP format.

This package contains Python 2 module.

%description -l pl.UTF-8
PyGPGME to moduł Pythona pozwalający podpisywać, weryfikować,
szyfrować i odszyfrowywać wiadomości w formacie OpenPGP.

Ten pakiet zawiera moduł Pythona 2.

%package -n python3-pygpgme
Summary:	A Python 3 wrapper for the GPGME library
Summary(pl.UTF-8):	Interfejs Pythona 3 do biblioteki GPGME
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-pygpgme
PyGPGME is a Python module that lets you sign, verify, encrypt and
decrypt messages using the OpenPGP format.

This package contains Python 3 module.

%description -n python3-pygpgme -l pl.UTF-8
PyGPGME to moduł Pythona pozwalający podpisywać, weryfikować,
szyfrować i odszyfrowywać wiadomości w formacie OpenPGP.

Ten pakiet zawiera moduł Pythona 3.

%prep
%setup -q -n pygpgme-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc NEWS README
%dir %{py_sitedir}/gpgme
%attr(755,root,root) %{py_sitedir}/gpgme/_gpgme.so
%{py_sitedir}/gpgme/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitedir}/pygpgme-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-pygpgme
%defattr(644,root,root,755)
%doc NEWS README
%dir %{py3_sitedir}/gpgme
%attr(755,root,root) %{py3_sitedir}/gpgme/_gpgme.cpython-*.so
%{py3_sitedir}/gpgme/*.py
%{py3_sitedir}/gpgme/__pycache__
%{py3_sitedir}/pygpgme-%{version}-py*.egg-info
%endif
