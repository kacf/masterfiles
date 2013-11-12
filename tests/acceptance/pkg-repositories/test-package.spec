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

%package alpha
Summary: CFEngine Test Package Alpha
Group: Other
%description alpha
CFEngine Test Package Alpha

%package beta
Summary: CFEngine Test Package Beta
Group: Other
%description beta
CFEngine Test Package Beta

%prep
cp -f ${RPM_SOURCE_DIR}/dummy.txt .

%install
mkdir -p ${RPM_BUILD_ROOT}
cp -f ${RPM_BUILD_DIR}/dummy.txt ${RPM_BUILD_ROOT}/dummy.txt
cp -f ${RPM_BUILD_DIR}/dummy.txt ${RPM_BUILD_ROOT}/dummy-alpha.txt
cp -f ${RPM_BUILD_DIR}/dummy.txt ${RPM_BUILD_ROOT}/dummy-beta.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir /
/dummy.txt

%files alpha
%defattr(-,root,root)
%dir /
/dummy-alpha.txt

%files beta
%defattr(-,root,root)
%dir /
/dummy-beta.txt
