%global debug_package %{nil}

Name:           broot
Version:        1.14.1
Release:        1%{?dist}
Summary:        A better way to navigate directories
Group:          Applications/System
License:        GPLv2
URL:            https://github.com/Canop/%{name}
BuildRequires:  cmake, cargo, rust
Source:         https://github.com/Canop/%{name}/archive/v%{version}.tar.gz

%description
Get an overview of a directory, even a big one
Find a directory then cd to it
Never lose track of file hierarchy while you search
Manipulate your files
Apply a standard or personal shortcut to a file
Replace ls (and its clones)
See what takes space

%prep
%setup -q -n %{name}-%{version}

%build
cargo build --release

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp target/release/broot %{buildroot}/usr/bin/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE* *.md
/usr/bin/broot

%changelog
* Thu Jul 7 2022 Jamie Curnow <jc@jc21.com> - 1.14.1-1
- https://github.com/Canop/broot/releases/tag/v1.14.1

* Sun May 29 2022 Jamie Curnow <jc@jc21.com> - 1.13.0-1
- https://github.com/Canop/broot/releases/tag/v1.13.0

* Mon Apr 4 2022 Jamie Curnow <jc@jc21.com> - 1.11.0-1
- https://github.com/Canop/broot/releases/tag/v1.11.0

* Tue Mar 15 2022 Jamie Curnow <jc@jc21.com> - 1.9.4-1
- https://github.com/Canop/broot/releases/tag/v1.9.4

* Wed Feb 16 2022 Jamie Curnow <jc@jc21.com> - 1.9.3-1
- https://github.com/Canop/broot/releases/tag/v1.9.3

* Sat Jan 8 2022 Jamie Curnow <jc@jc21.com> - 1.9.1-1
- https://github.com/Canop/broot/releases/tag/v1.9.1

* Sun Jan 2 2022 Jamie Curnow <jc@jc21.com> - 1.8.1-1
- https://github.com/Canop/broot/releases/tag/v1.8.1

* Fri Dec 3 2021 Jamie Curnow <jc@jc21.com> - 1.7.4-1
- https://github.com/Canop/broot/releases/tag/v1.7.4

* Mon Nov 1 2021 Jamie Curnow <jc@jc21.com> - 1.7.0-1
- https://github.com/Canop/broot/releases/tag/v1.7.0

* Mon Oct 24 2021 Jamie Curnow <jc@jc21.com> - 1.6.6-1
- https://github.com/Canop/broot/releases/tag/v1.6.6

* Thu Oct 21 2021 Jamie Curnow <jc@jc21.com> - 1.6.5-1
- https://github.com/Canop/broot/releases/tag/v1.6.5

* Tue Oct 5 2021 Jamie Curnow <jc@jc21.com> - 1.6.4-1
- https://github.com/Canop/broot/releases/tag/v1.6.4

* Tue Aug 3 2021 Jamie Curnow <jc@jc21.com> - 1.6.3-1
- https://github.com/Canop/broot/releases/tag/v1.6.3

* Fri Jun 25 2021 Jamie Curnow <jc@jc21.com> - 1.6.1-1
- https://github.com/Canop/broot/releases/tag/v1.6.1

* Fri Jun 4 2021 Jamie Curnow <jc@jc21.com> - 1.5.1-1
- https://github.com/Canop/broot/releases/tag/v1.5.1

* Mon May 17 2021 Jamie Curnow <jc@jc21.com> - 1.4.0-1
- https://github.com/Canop/broot/releases/tag/v1.4.0

* Tue May 4 2021 Jamie Curnow <jc@jc21.com> - 1.3.1-1
- https://github.com/Canop/broot/releases/tag/v1.3.1

* Thu Apr 29 2021 Jamie Curnow <jc@jc21.com> - 1.3.0-1
- https://github.com/Canop/broot/releases/tag/v1.3.0

* Fri Mar 19 2021 Jamie Curnow <jc@jc21.com> - 1.2.9-1
- https://github.com/Canop/broot/releases/tag/v1.2.9

* Mon Mar 12 2021 Jamie Curnow <jc@jc21.com> - 1.2.8-1
- https://github.com/Canop/broot/releases/tag/v1.2.8

* Mon Mar 1 2021 Jamie Curnow <jc@jc21.com> - 1.2.7-1
- https://github.com/Canop/broot/releases/tag/v1.2.7

* Fri Feb 26 2021 Jamie Curnow <jc@jc21.com> - 1.2.5-1
- https://github.com/Canop/broot/releases/tag/v1.2.5

* Mon Feb 15 2021 Jamie Curnow <jc@jc21.com> - 1.2.4-1
- https://github.com/Canop/broot/releases/tag/v1.2.4

* Mon Feb 8 2021 Jamie Curnow <jc@jc21.com> - 1.2.3-1
- https://github.com/Canop/broot/releases/tag/v1.2.3

* Thu Jan 28 2021 Jamie Curnow <jc@jc21.com> - 1.2.1-1
- https://github.com/Canop/broot/releases/tag/v1.2.1

* Fri Jan 15 2021 Jamie Curnow <jc@jc21.com> - 1.2.0-1
- https://github.com/Canop/broot/releases/tag/v1.2.0

* Mon Jan 11 2021 Jamie Curnow <jc@jc21.com> - 1.1.11-1
- https://github.com/Canop/broot/releases/tag/v1.1.11

* Sat Dec 26 2020 Jamie Curnow <jc@jc21.com> - 1.1.0-1
- https://github.com/Canop/broot/releases/tag/v1.1.0

* Mon Dec 21 2020 Jamie Curnow <jc@jc21.com> - 1.0.9-1
- https://github.com/Canop/broot/releases/tag/v1.0.9

* Sun Dec 6 2020 Jamie Curnow <jc@jc21.com> - 1.0.8-1
- https://github.com/Canop/broot/releases/tag/v1.0.8

* Sun Nov 29 2020 Jamie Curnow <jc@jc21.com> - 1.0.7-1
- https://github.com/Canop/broot/releases/tag/v1.0.7

* Mon Nov 23 2020 Jamie Curnow <jc@jc21.com> - 1.0.6-1
- https://github.com/Canop/broot/releases/tag/v1.0.6

* Fri Nov 6 2020 Jamie Curnow <jc@jc21.com> - 1.0.5-1
- https://github.com/Canop/broot/releases/tag/v1.0.5

* Mon Oct 26 2020 Jamie Curnow <jc@jc21.com> - 1.0.4-1
- https://github.com/Canop/broot/releases/tag/v1.0.4

* Fri Oct 9 2020 Jamie Curnow <jc@jc21.com> - 1.0.3-1
- https://github.com/Canop/broot/releases/tag/v1.0.3

* Thu Oct 1 2020 Jamie Curnow <jc@jc21.com> - 1.0.1-1
- https://github.com/Canop/broot/releases/tag/v1.0.1

* Mon Sep 7 2020 Jamie Curnow <jc@jc21.com> - 1.0.0-1
- https://github.com/Canop/broot/releases/tag/v1.0.0

* Thu Aug 25 2020 Jamie Curnow <jc@jc21.com> - 0.20.3-1
- https://github.com/Canop/broot/releases/tag/v0.20.3

* Thu Aug 20 2020 Jamie Curnow <jc@jc21.com> - 0.20.2-1
- https://github.com/Canop/broot/releases/tag/v0.20.2

* Mon Aug 17 2020 Jamie Curnow <jc@jc21.com> - 0.20.0-1
- https://github.com/Canop/broot/releases/tag/v0.20.0

* Mon Aug 3 2020 Jamie Curnow <jc@jc21.com> - 0.19.4-1
- https://github.com/Canop/broot/releases/tag/v0.19.4

* Tue Jul 28 2020 Jamie Curnow <jc@jc21.com> - 0.19.3-1
- https://github.com/Canop/broot/releases/tag/v0.19.3

* Fri Jul 24 2020 Jamie Curnow <jc@jc21.com> - 0.19.1-1
- https://github.com/Canop/broot/releases/tag/v0.19.1

* Mon Jul 13 2020 Jamie Curnow <jc@jc21.com> - 0.18.6-1
- https://github.com/Canop/broot/releases/tag/v0.18.6

* Mon Jul 6 2020 Jamie Curnow <jc@jc21.com> - 0.18.5-1
- https://github.com/Canop/broot/releases/tag/v0.18.5

* Thu Jul 2 2020 Jamie Curnow <jc@jc21.com> - 0.18.3-1
- https://github.com/Canop/broot/releases/tag/v0.18.3

* Tue Jun 30 2020 Jamie Curnow <jc@jc21.com> - 0.18.2-1
- https://github.com/Canop/broot/releases/tag/v0.18.2

* Mon Jun 29 2020 Jamie Curnow <jc@jc21.com> - 0.18.1-1
- https://github.com/Canop/broot/releases/tag/v0.18.1

* Wed Jun 24 2020 Jamie Curnow <jc@jc21.com> - 0.17.0-1
- https://github.com/Canop/broot/releases/tag/v0.17.0

* Mon Jun 22 2020 Jamie Curnow <jc@jc21.com> - 0.16.0-1
- https://github.com/Canop/broot/releases/tag/v0.16.0

* Mon Jun 15 2020 Jamie Curnow <jc@jc21.com> - 0.15.1-1
- https://github.com/Canop/broot/releases/tag/v0.15.1

* Tue Jun 2 2020 Jamie Curnow <jc@jc21.com> - 0.14.2-1
- https://github.com/Canop/broot/releases/tag/v0.14.2

* Mon Jun 1 2020 Jamie Curnow <jc@jc21.com> - 0.14.1-1
- https://github.com/Canop/broot/releases/tag/v0.14.1

* Thu Apr 9 2020 Jamie Curnow <jc@jc21.com> - 0.13.6-1
- https://github.com/Canop/broot/releases/tag/v0.13.6

* Mon Mar 30 2020 Jamie Curnow <jc@jc21.com> - 0.13.5-1
- https://github.com/Canop/broot/releases/tag/v0.13.5

* Mon Mar 16 2020 Jamie Curnow <jc@jc21.com> - 0.13.4-1
- https://github.com/Canop/broot/releases/tag/v0.13.4

* Mon Feb 17 2020 Jamie Curnow <jc@jc21.com> - 0.13.2-1
- https://github.com/Canop/broot/releases/tag/v0.13.2

* Mon Feb 10 2020 Jamie Curnow <jc@jc21.com> - 0.13.1-1
- https://github.com/Canop/broot/releases/tag/v0.13.1

* Fri Feb 7 2020 Jamie Curnow <jc@jc21.com> - 0.13.0-1
- https://github.com/Canop/broot/releases/tag/v0.13.0

* Thu Jan 30 2020 Jamie Curnow <jc@jc21.com> - 0.12.2-1
- https://github.com/Canop/broot/releases/tag/v0.12.2

* Sat Jan 25 2020 Jamie Curnow <jc@jc21.com> - 0.12.1-1
- https://github.com/Canop/broot/releases/tag/v0.12.1

* Mon Jan 20 2020 Jamie Curnow <jc@jc21.com> - 0.12.0-1
- https://github.com/Canop/broot/releases/tag/v0.12.0

* Thu Jan 16 2020 Jamie Curnow <jc@jc21.com> - 0.11.9-1
- https://github.com/Canop/broot/releases/tag/v0.11.9

* Mon Jan 13 2020 Jamie Curnow <jc@jc21.com> - 0.11.8-1
- Initial spec
