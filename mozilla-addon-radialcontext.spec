%define		_realname	radialcontext
Summary:	A radial context menu for Mozilla
Summary(pl.UTF-8):	Menu kontekstowe dla mozilli
Name:		mozilla-addon-%{_realname}
Version:	1.0
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.radialthinking.de/radialcontext/RadialContext.xpi
# Source0-md5:	9727c912580f062106f5b60de04c4331
Source1:	%{_realname}-installed-chrome.txt
URL:		http://www.radialthinking.de/radialcontext/
BuildRequires:	unzip
BuildRequires:	zip
Requires(post,postun):	mozilla >= 5:1.7.3-3
Requires(post,postun):	textutils
Requires:	mozilla >= 2:1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
The RadialContext menu is a hierarchical, context-sensitive pie menu
for Mozilla. It offers an alternative to both the normal context menu
and mouse gestures. The feeling is very similar to mouse gestures. But
there also is a GUI so you don't have to look up what options are
available in the given context.

%description -l pl.UTF-8
RadialContext stanowi hierarchiczne, zależne od kontekstu okrągłe menu
dla mozilli. Stanowi alternatywę zarówno dla zwykłego menu
kontekstowego, jak i dla ruchów myszki. Odczucia są bardzo podobne do
ruchów myszki. Ale jest jeszcze interfejs graficzny (GUI), więc nie ma
potrzeby sprawdzania, które opcję są dostępne w danym kontekście.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

cd %{_realname}
mv about.txt ..
zip -r -9 -m ../%{_realname}.jar ./
cd -
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}
install %{_realname}.jar $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
	%{_sbindir}/mozilla-chrome+xpcom-generate
fi

%postun
[ ! -x %{_sbindir}/mozilla-chrome+xpcom-generate ] || %{_sbindir}/mozilla-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%doc about.txt
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
