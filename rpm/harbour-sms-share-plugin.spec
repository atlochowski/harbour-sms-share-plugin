# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       harbour-sms-share-plugin

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    SMS sharing plugin
Version:    1.0
Release:    1
Group:      Qt/Qt
License:    MIT
URL:        https://github.com/martonmiklos/harbour-sms-share-plugin
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-sms-share-plugin.yaml
Requires:   libnemotransferengine-qt5 >= 0.3.1
Requires:   declarative-transferengine-qt5 >= 0.0.44
Requires:   vcardserializer >= 1.0
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(nemotransferengine-qt5)
BuildRequires:  pkgconfig(Qt5DBus)

%description
Nem transferengine plugin for sharing contact data via SMS


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_libdir}/nemo-transferengine/plugins/*shareplugin.so
%{_datadir}/nemo-transferengine/plugins/SmsShare.qml
%{_datadir}/translations/nemotransferengine/*.qm
# >> files
# << files
