%define		plugin	w3-total-cache
Summary:	W3 Total Cache
Name:		wordpress-plugin-%{plugin}
Version:	0.9.1.3
Release:	0.3
License:	GPL
Group:		Applications/WWW
Source0:	http://downloads.wordpress.org/plugin/w3-total-cache.%{version}.zip
# Source0-md5:	f6449b43ab5162abf071424eb76341d3
URL:		http://wordpress.org/extend/plugins/w3-total-cache/
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	webapps
Requires:	webserver(php)
Requires:	wordpress >= 2.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		wp_root		%{_datadir}/wordpress
%define		wp_content	%{wp_root}/wp-content
%define		pluginsdir	%{wp_content}/plugins
%define		plugindir	%{pluginsdir}/%{plugin}

%description
Easily optimize the speed and user experience of your site with
caching: browser, page, object, database, minify and content delivery
network support.

%prep
%setup -qn %{plugin}
%undos -f php,txt,phtml

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm $RPM_BUILD_ROOT%{plugindir}/readme.txt
rm -f $RPM_BUILD_ROOT%{plugindir}/debug*.list

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%dir %{plugindir}
%{plugindir}/w3-total-cache.php
%dir %{plugindir}/wp-content
%{plugindir}/wp-content/advanced-cache.php
%{plugindir}/wp-content/db.php
%{plugindir}/wp-content/object-cache.php
%{plugindir}/wp-content/w3tc
%{plugindir}/inc
%{plugindir}/ini
%{plugindir}/lib
