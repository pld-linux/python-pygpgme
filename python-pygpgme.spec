Summary:	A Python wrapper for the GPGME library
Name:		python-pygpgme
Version:	0.1
Release:	6
License:	MIT
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/p/pygpgme/pygpgme-%{version}.tar.gz
# Source0-md5:	0878d866b6ee8a98a9003a81934ecee3
URL:		https://launchpad.net/products/pygpgme
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	gpgme-devel
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyGPGME is a Python module that lets you sign, verify, encrypt and
decrypt messages using the OpenPGP format.

%prep
%setup -q -n pygpgme-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/gpgme/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/gpgme
%attr(755,root,root) %{py_sitedir}/gpgme/_gpgme.so
%{py_sitedir}/gpgme/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitedir}/pygpgme-%{version}-py*.egg-info
%endif
