Summary:	Software synthesizer based on ZynAddSubFX
Name:		yoshimi
Version:	1.2.5
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/yoshimi/%{name}-%{version}.tar.bz2
# Source0-md5:	068e32213a17047330d1594218de1e48
BuildRequires:	alsa-lib-devel
BuildRequires:	boost-devel
BuildRequires:	cairo-devel
BuildRequires:	cmake
BuildRequires:	fftw3-devel
BuildRequires:	fltk-devel
BuildRequires:	fltk-gl-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	mxml-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A software synthesizer for Linux, based on ZynAddSubFX.
Yoshimi delivers the same synthesizer capabilities along with very
good Jack and Alsa midi/audio functionality on Linux.

%prep
%setup -q

%build
install -d build
cd build
%cmake ../src \
	-DBuildOptionsBasic:STRING="%{rpmcflags} -O3"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

cat > $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop <<EOF
[Desktop Entry]
Type=Application
Exec=yoshimi
Icon=yoshimi
Terminal=false
Name=Yoshimi
Comment=Software synthesizer
StartupNotify=true
Categories=AudioVideo;Audio;Midi;
EOF

install desktop/yoshimi.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png

