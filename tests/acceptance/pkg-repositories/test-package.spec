Summary: CFEngine Test Package
Name: test-package
Version: 1.0
Release: 1
Source: dummy.txt
License: MIT
Group: Other
Url: http://example.com
BuildRoot: %{_topdir}/BUILD/%{name}-%{version}-%{release}-buildroot

AutoReqProv: no

%description
CFEngine Test Package

%prep
cp -f ${RPM_SOURCE_DIR}/dummy.txt .

%install
mkdir -p ${RPM_BUILD_ROOT}
cp -f ${RPM_BUILD_DIR}/dummy.txt ${RPM_BUILD_ROOT}/dummy.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir /
/dummy.txt
