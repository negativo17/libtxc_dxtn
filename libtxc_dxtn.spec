%define         commit ef072983

Name:           libtxc_dxtn
Version:        1.0.1
Release:        1.git%{commit}%{?dist}
Epoch:          1
Summary:        Free implementation of the s3tc texture compression algorithm

License:        BSD
URL:            http://cgit.freedesktop.org/~mareko/%{name}/
Source0:        %{name}-%{version}-git%{commit}.tar.bz2
Source10:       %{name}-git-checkout.sh

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  mesa-libGL-devel       

%description
Free implementation of the s3tc texture compression algorithm.

%prep
%setup -q -n %{name}
sed -i -e 's|pixerrorcolorbest\[3\]|pixerrorcolorbest[3]={0,0,0}|g' txc_compress_dxtn.c
sed -i -e 's|GLshort alphatest\[2\]|GLshort alphatest[2]={0,0}|g' txc_compress_dxtn.c

%build
autoreconf -vif
%configure --disable-static

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
# Do not install header, but use it as license
sed -n '5,22{s|^ \* \?||;p}' txc_dxtn.h > LICENSE
rm -fr %{buildroot}/%{_includedir}

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_libdir}/*.so

%changelog
* Fri Apr 24 2015 Simone Caronni <negativo17@gmail.com> - 1:1.0.1-1.gitef072983
- Update to 1.0.1 git; switch to autotools build.
- SPEC file cleanup.
- Add license file.

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1:1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 1:1.0.0-3
- Mass rebuilt for Fedora 19 Features

* Wed Jan 25 2012 Nicolas Chauvet <kwizart@gmail.com> - 1:1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Mar 22 2011 Hicham HAOUARI <hicham.haouari@gmail.com> - 1:1.0.0-1
- Update to 1.0.0 from Marek's branch

* Tue Oct 26 2010 Hicham HAOUARI <hicham.haouari@gmail.com> - 070518-1
- Initial package for Fedora.
