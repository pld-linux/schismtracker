Summary:	Impulse Tracker clone
Summary(pl.UTF-8):	Klon Impulse Trackera
Name:		schism
Version:	0.2a
Release:	1
Epoch:		1	
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://rigelseven.com/schism/dl/%{name}-%{version}.tar.bz2
# Source0-md5:	2b07f1f7657ab82ad6f0a737dda623eb
Source1:	%{name}.desktop
URL:		http://rigelseven.com/schism/
BuildRequires:	SDL-devel >= 1.1.8
Requires:	SDL >= 1.1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Impulse Tracker clone with support of almost all module types.

%description -l pl.UTF-8
Klon Impulse Trackera z obsługą niemal wszystkich typów modułów.

%prep
%setup -q 

%build
%configure \
	--enable-alsa-mixer
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
