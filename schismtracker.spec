Summary:	Impulse Tracker clone
Summary(pl.UTF-8):	Klon Impulse Trackera
Name:		schismtracker
Version:	20120105
Release:	1
Epoch:		1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://schismtracker.org/dl/%{name}-%{version}.tar.bz2
# Source0-md5:	c85ee0750b2890cbd123ff6f9cb827b9
Source1:	%{name}.desktop
Source2:	itf.desktop
URL:		http://www.schismtracker.org/
BuildRequires:	SDL-devel >= 1.1.8
Requires:	SDL >= 1.1.8
Obsoletes:	schism
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Impulse Tracker clone with support of almost all module types.

%description -l pl.UTF-8
Klon Impulse Trackera z obsługą niemal wszystkich typów modułów.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/{16x16,22x22,24x24,32x32,36x36,48x48,64x64,72x72,96x96,128x128,scalable}/apps

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install icons/schism-icon-16.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/schismtracker.png
install icons/schism-icon-22.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/22x22/apps/schismtracker.png
install icons/schism-icon-24.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/24x24/apps/schismtracker.png
install icons/schism-icon-32.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/schismtracker.png
install icons/schism-icon-36.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/36x36/apps/schismtracker.png
install icons/schism-icon-48.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/schismtracker.png
install icons/schism-icon-64.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/64x64/apps/schismtracker.png
install icons/schism-icon-72.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/72x72/apps/schismtracker.png
install icons/schism-icon-96.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/96x96/apps/schismtracker.png
install icons/schism-icon-128.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/128x128/apps/schismtracker.png
install icons/schism-icon.svg $RPM_BUILD_ROOT%{_iconsdir}/hicolor/scalable/apps/schismtracker.svg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/schismtracker.1*
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*
