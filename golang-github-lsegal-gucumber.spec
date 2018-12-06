# http://github.com/gucumber/gucumber
%global sec_goipath     github.com/gucumber/gucumber
%global goipath         github.com/lsegal/gucumber
%global commit          71608e2f6e76fd4da5b09a376aeec7a5c0b5edbc

%gometa -i

%global sec_name        %gorpmname %{sec_goipath}

Name:           golang-github-lsegal-gucumber
Version:        0
Release:        0.12%{?dist}
Summary:        An implementation of Cucumber BDD-style testing for Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/shiena/ansicolor)
BuildRequires: golang(github.com/stretchr/testify/assert)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%package -n %{sec_name}-devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/shiena/ansicolor)
BuildRequires: golang(github.com/stretchr/testify/assert)

%description -n %{sec_name}-devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup
chmod -x LICENSE.txt README.md

%install
%goinstall glide.lock glide.yaml
%goinstall glide.lock glide.yaml -i %{sec_goipath} -o sec-devel.file-list

pushd %{buildroot}/%{gopath}/src/%{sec_goipath}/
sed -i 's/"github\.com\/gucumber\/gucumber/"github\.com\/lsegal\/gucumber/g' \
        $(find . -name '*.go')
popd

%check
%gochecks -d .

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE.txt
%doc README.md

%files -n %{sec_name}-devel -f sec-devel.file-list
%license LICENSE.txt
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.11.git71608e2
- Upload glide files

* Thu Mar 01 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.20160715git71608e2
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git71608e2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git71608e2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git71608e2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git71608e2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.5.git71608e2
- Bump to upstream 71608e2f6e76fd4da5b09a376aeec7a5c0b5edbc
  resolves: #1415383

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.gite8116c9
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.gite8116c9
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gite8116c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gite8116c9
- First package for Fedora
  resolves: #1269799
