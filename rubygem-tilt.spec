%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname tilt
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Name:		rubygem-%{gemname}
Summary: 	tilt
Version: 	1.4.1
Release: 	1%{?dist}
Group: 		Development/Languages
License: 	GPLv2+ or Ruby
URL:        http://%{gemname}.rubyforge.org/
Source0:    http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: 	rubygems
BuildRequires: 	rubygems
BuildArch: 	noarch
Provides: 	rubygem(%{gemname}) = %{version}

%description
tilt files

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

for file in `find %{buildroot}/%{geminstdir} -name "*.rb"`; do
    [ ! -z "`head -n 1 $file | grep \"^#!\"`" ] && chmod +x $file
done

# Remove zero-length file
rm -rf %{buildroot}/%{geminstdir}/%{gemname}-%{version}.gem

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/bin/tilt
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%changelog
* Tue Jun 4 2013 Sergey Mihailov <sergey.mihailov@gpm.int> - 1.4.1-1
- Initial package
