#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v12
# autospec commit: f9eab48
#
Name     : qt6translations
Version  : 6.7.2
Release  : 15
URL      : https://download.qt.io/official_releases/qt/6.7/6.7.2/submodules/qttranslations-everywhere-src-6.7.2.zip
Source0  : https://download.qt.io/official_releases/qt/6.7/6.7.2/submodules/qttranslations-everywhere-src-6.7.2.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-3.0
Requires: qt6translations-data = %{version}-%{release}
Requires: qt6translations-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : qt6base-dev
BuildRequires : qt6tools-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
All translations are contributed by the Qt community.
They are provided without guarantees, will often be stale, and may even
disappear entirely from future Qt releases.

%package data
Summary: data components for the qt6translations package.
Group: Data

%description data
data components for the qt6translations package.


%package license
Summary: license components for the qt6translations package.
Group: Default

%description license
license components for the qt6translations package.


%prep
%setup -q -n qttranslations-everywhere-src-6.7.2
cd %{_builddir}/qttranslations-everywhere-src-6.7.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1718936590
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1718936590
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6translations
cp %{_builddir}/qttranslations-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6translations/79453f55fa8ee32d7b95581473edcbfd043e088f || :
cp %{_builddir}/qttranslations-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6translations/7713a1753ce88f2c7e6b054ecc8e4c786df76300 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qt6/translations/assistant_ar.qm
/usr/share/qt6/translations/assistant_bg.qm
/usr/share/qt6/translations/assistant_cs.qm
/usr/share/qt6/translations/assistant_da.qm
/usr/share/qt6/translations/assistant_de.qm
/usr/share/qt6/translations/assistant_en.qm
/usr/share/qt6/translations/assistant_es.qm
/usr/share/qt6/translations/assistant_fr.qm
/usr/share/qt6/translations/assistant_hr.qm
/usr/share/qt6/translations/assistant_hu.qm
/usr/share/qt6/translations/assistant_ja.qm
/usr/share/qt6/translations/assistant_ka.qm
/usr/share/qt6/translations/assistant_ko.qm
/usr/share/qt6/translations/assistant_nl.qm
/usr/share/qt6/translations/assistant_pl.qm
/usr/share/qt6/translations/assistant_pt_BR.qm
/usr/share/qt6/translations/assistant_ru.qm
/usr/share/qt6/translations/assistant_sk.qm
/usr/share/qt6/translations/assistant_sl.qm
/usr/share/qt6/translations/assistant_tr.qm
/usr/share/qt6/translations/assistant_uk.qm
/usr/share/qt6/translations/assistant_zh_CN.qm
/usr/share/qt6/translations/assistant_zh_TW.qm
/usr/share/qt6/translations/catalogs.json
/usr/share/qt6/translations/designer_ar.qm
/usr/share/qt6/translations/designer_bg.qm
/usr/share/qt6/translations/designer_cs.qm
/usr/share/qt6/translations/designer_da.qm
/usr/share/qt6/translations/designer_de.qm
/usr/share/qt6/translations/designer_en.qm
/usr/share/qt6/translations/designer_es.qm
/usr/share/qt6/translations/designer_fr.qm
/usr/share/qt6/translations/designer_hr.qm
/usr/share/qt6/translations/designer_hu.qm
/usr/share/qt6/translations/designer_ja.qm
/usr/share/qt6/translations/designer_ka.qm
/usr/share/qt6/translations/designer_ko.qm
/usr/share/qt6/translations/designer_nl.qm
/usr/share/qt6/translations/designer_pl.qm
/usr/share/qt6/translations/designer_ru.qm
/usr/share/qt6/translations/designer_sk.qm
/usr/share/qt6/translations/designer_sl.qm
/usr/share/qt6/translations/designer_tr.qm
/usr/share/qt6/translations/designer_uk.qm
/usr/share/qt6/translations/designer_zh_CN.qm
/usr/share/qt6/translations/designer_zh_TW.qm
/usr/share/qt6/translations/linguist_ar.qm
/usr/share/qt6/translations/linguist_bg.qm
/usr/share/qt6/translations/linguist_cs.qm
/usr/share/qt6/translations/linguist_da.qm
/usr/share/qt6/translations/linguist_de.qm
/usr/share/qt6/translations/linguist_en.qm
/usr/share/qt6/translations/linguist_es.qm
/usr/share/qt6/translations/linguist_fr.qm
/usr/share/qt6/translations/linguist_hr.qm
/usr/share/qt6/translations/linguist_hu.qm
/usr/share/qt6/translations/linguist_it.qm
/usr/share/qt6/translations/linguist_ja.qm
/usr/share/qt6/translations/linguist_ka.qm
/usr/share/qt6/translations/linguist_ko.qm
/usr/share/qt6/translations/linguist_nl.qm
/usr/share/qt6/translations/linguist_pl.qm
/usr/share/qt6/translations/linguist_ru.qm
/usr/share/qt6/translations/linguist_sk.qm
/usr/share/qt6/translations/linguist_sl.qm
/usr/share/qt6/translations/linguist_sv.qm
/usr/share/qt6/translations/linguist_tr.qm
/usr/share/qt6/translations/linguist_uk.qm
/usr/share/qt6/translations/linguist_zh_CN.qm
/usr/share/qt6/translations/linguist_zh_TW.qm
/usr/share/qt6/translations/qt_ar.qm
/usr/share/qt6/translations/qt_bg.qm
/usr/share/qt6/translations/qt_ca.qm
/usr/share/qt6/translations/qt_cs.qm
/usr/share/qt6/translations/qt_da.qm
/usr/share/qt6/translations/qt_de.qm
/usr/share/qt6/translations/qt_en.qm
/usr/share/qt6/translations/qt_es.qm
/usr/share/qt6/translations/qt_fa.qm
/usr/share/qt6/translations/qt_fi.qm
/usr/share/qt6/translations/qt_fr.qm
/usr/share/qt6/translations/qt_gd.qm
/usr/share/qt6/translations/qt_gl.qm
/usr/share/qt6/translations/qt_he.qm
/usr/share/qt6/translations/qt_help_ar.qm
/usr/share/qt6/translations/qt_help_bg.qm
/usr/share/qt6/translations/qt_help_ca.qm
/usr/share/qt6/translations/qt_help_cs.qm
/usr/share/qt6/translations/qt_help_da.qm
/usr/share/qt6/translations/qt_help_de.qm
/usr/share/qt6/translations/qt_help_en.qm
/usr/share/qt6/translations/qt_help_es.qm
/usr/share/qt6/translations/qt_help_fr.qm
/usr/share/qt6/translations/qt_help_gl.qm
/usr/share/qt6/translations/qt_help_hr.qm
/usr/share/qt6/translations/qt_help_hu.qm
/usr/share/qt6/translations/qt_help_it.qm
/usr/share/qt6/translations/qt_help_ja.qm
/usr/share/qt6/translations/qt_help_ka.qm
/usr/share/qt6/translations/qt_help_ko.qm
/usr/share/qt6/translations/qt_help_nl.qm
/usr/share/qt6/translations/qt_help_nn.qm
/usr/share/qt6/translations/qt_help_pl.qm
/usr/share/qt6/translations/qt_help_pt_BR.qm
/usr/share/qt6/translations/qt_help_ru.qm
/usr/share/qt6/translations/qt_help_sk.qm
/usr/share/qt6/translations/qt_help_sl.qm
/usr/share/qt6/translations/qt_help_tr.qm
/usr/share/qt6/translations/qt_help_uk.qm
/usr/share/qt6/translations/qt_help_zh_CN.qm
/usr/share/qt6/translations/qt_help_zh_TW.qm
/usr/share/qt6/translations/qt_hr.qm
/usr/share/qt6/translations/qt_hu.qm
/usr/share/qt6/translations/qt_it.qm
/usr/share/qt6/translations/qt_ja.qm
/usr/share/qt6/translations/qt_ka.qm
/usr/share/qt6/translations/qt_ko.qm
/usr/share/qt6/translations/qt_lt.qm
/usr/share/qt6/translations/qt_lv.qm
/usr/share/qt6/translations/qt_nl.qm
/usr/share/qt6/translations/qt_nn.qm
/usr/share/qt6/translations/qt_pl.qm
/usr/share/qt6/translations/qt_pt_BR.qm
/usr/share/qt6/translations/qt_pt_PT.qm
/usr/share/qt6/translations/qt_ru.qm
/usr/share/qt6/translations/qt_sk.qm
/usr/share/qt6/translations/qt_sl.qm
/usr/share/qt6/translations/qt_sv.qm
/usr/share/qt6/translations/qt_tr.qm
/usr/share/qt6/translations/qt_uk.qm
/usr/share/qt6/translations/qt_zh_CN.qm
/usr/share/qt6/translations/qt_zh_TW.qm
/usr/share/qt6/translations/qtbase_ar.qm
/usr/share/qt6/translations/qtbase_bg.qm
/usr/share/qt6/translations/qtbase_ca.qm
/usr/share/qt6/translations/qtbase_cs.qm
/usr/share/qt6/translations/qtbase_da.qm
/usr/share/qt6/translations/qtbase_de.qm
/usr/share/qt6/translations/qtbase_en.qm
/usr/share/qt6/translations/qtbase_es.qm
/usr/share/qt6/translations/qtbase_fa.qm
/usr/share/qt6/translations/qtbase_fi.qm
/usr/share/qt6/translations/qtbase_fr.qm
/usr/share/qt6/translations/qtbase_gd.qm
/usr/share/qt6/translations/qtbase_he.qm
/usr/share/qt6/translations/qtbase_hr.qm
/usr/share/qt6/translations/qtbase_hu.qm
/usr/share/qt6/translations/qtbase_it.qm
/usr/share/qt6/translations/qtbase_ja.qm
/usr/share/qt6/translations/qtbase_ka.qm
/usr/share/qt6/translations/qtbase_ko.qm
/usr/share/qt6/translations/qtbase_lv.qm
/usr/share/qt6/translations/qtbase_nl.qm
/usr/share/qt6/translations/qtbase_nn.qm
/usr/share/qt6/translations/qtbase_pl.qm
/usr/share/qt6/translations/qtbase_pt_BR.qm
/usr/share/qt6/translations/qtbase_ru.qm
/usr/share/qt6/translations/qtbase_sk.qm
/usr/share/qt6/translations/qtbase_tr.qm
/usr/share/qt6/translations/qtbase_uk.qm
/usr/share/qt6/translations/qtbase_zh_CN.qm
/usr/share/qt6/translations/qtbase_zh_TW.qm
/usr/share/qt6/translations/qtconnectivity_bg.qm
/usr/share/qt6/translations/qtconnectivity_ca.qm
/usr/share/qt6/translations/qtconnectivity_da.qm
/usr/share/qt6/translations/qtconnectivity_de.qm
/usr/share/qt6/translations/qtconnectivity_en.qm
/usr/share/qt6/translations/qtconnectivity_es.qm
/usr/share/qt6/translations/qtconnectivity_hr.qm
/usr/share/qt6/translations/qtconnectivity_hu.qm
/usr/share/qt6/translations/qtconnectivity_ka.qm
/usr/share/qt6/translations/qtconnectivity_ko.qm
/usr/share/qt6/translations/qtconnectivity_nl.qm
/usr/share/qt6/translations/qtconnectivity_pl.qm
/usr/share/qt6/translations/qtconnectivity_pt_BR.qm
/usr/share/qt6/translations/qtconnectivity_ru.qm
/usr/share/qt6/translations/qtconnectivity_tr.qm
/usr/share/qt6/translations/qtconnectivity_uk.qm
/usr/share/qt6/translations/qtconnectivity_zh_CN.qm
/usr/share/qt6/translations/qtdeclarative_ar.qm
/usr/share/qt6/translations/qtdeclarative_bg.qm
/usr/share/qt6/translations/qtdeclarative_ca.qm
/usr/share/qt6/translations/qtdeclarative_da.qm
/usr/share/qt6/translations/qtdeclarative_de.qm
/usr/share/qt6/translations/qtdeclarative_en.qm
/usr/share/qt6/translations/qtdeclarative_es.qm
/usr/share/qt6/translations/qtdeclarative_fa.qm
/usr/share/qt6/translations/qtdeclarative_fi.qm
/usr/share/qt6/translations/qtdeclarative_fr.qm
/usr/share/qt6/translations/qtdeclarative_hr.qm
/usr/share/qt6/translations/qtdeclarative_hu.qm
/usr/share/qt6/translations/qtdeclarative_ja.qm
/usr/share/qt6/translations/qtdeclarative_ka.qm
/usr/share/qt6/translations/qtdeclarative_ko.qm
/usr/share/qt6/translations/qtdeclarative_lv.qm
/usr/share/qt6/translations/qtdeclarative_nl.qm
/usr/share/qt6/translations/qtdeclarative_nn.qm
/usr/share/qt6/translations/qtdeclarative_pl.qm
/usr/share/qt6/translations/qtdeclarative_pt_BR.qm
/usr/share/qt6/translations/qtdeclarative_ru.qm
/usr/share/qt6/translations/qtdeclarative_sk.qm
/usr/share/qt6/translations/qtdeclarative_tr.qm
/usr/share/qt6/translations/qtdeclarative_uk.qm
/usr/share/qt6/translations/qtdeclarative_zh_CN.qm
/usr/share/qt6/translations/qtdeclarative_zh_TW.qm
/usr/share/qt6/translations/qtlocation_bg.qm
/usr/share/qt6/translations/qtlocation_ca.qm
/usr/share/qt6/translations/qtlocation_da.qm
/usr/share/qt6/translations/qtlocation_de.qm
/usr/share/qt6/translations/qtlocation_en.qm
/usr/share/qt6/translations/qtlocation_es.qm
/usr/share/qt6/translations/qtlocation_fi.qm
/usr/share/qt6/translations/qtlocation_fr.qm
/usr/share/qt6/translations/qtlocation_hr.qm
/usr/share/qt6/translations/qtlocation_hu.qm
/usr/share/qt6/translations/qtlocation_ka.qm
/usr/share/qt6/translations/qtlocation_ko.qm
/usr/share/qt6/translations/qtlocation_nl.qm
/usr/share/qt6/translations/qtlocation_pl.qm
/usr/share/qt6/translations/qtlocation_pt_BR.qm
/usr/share/qt6/translations/qtlocation_ru.qm
/usr/share/qt6/translations/qtlocation_tr.qm
/usr/share/qt6/translations/qtlocation_uk.qm
/usr/share/qt6/translations/qtlocation_zh_CN.qm
/usr/share/qt6/translations/qtmultimedia_ar.qm
/usr/share/qt6/translations/qtmultimedia_bg.qm
/usr/share/qt6/translations/qtmultimedia_ca.qm
/usr/share/qt6/translations/qtmultimedia_cs.qm
/usr/share/qt6/translations/qtmultimedia_da.qm
/usr/share/qt6/translations/qtmultimedia_de.qm
/usr/share/qt6/translations/qtmultimedia_en.qm
/usr/share/qt6/translations/qtmultimedia_es.qm
/usr/share/qt6/translations/qtmultimedia_fa.qm
/usr/share/qt6/translations/qtmultimedia_fi.qm
/usr/share/qt6/translations/qtmultimedia_fr.qm
/usr/share/qt6/translations/qtmultimedia_hr.qm
/usr/share/qt6/translations/qtmultimedia_hu.qm
/usr/share/qt6/translations/qtmultimedia_it.qm
/usr/share/qt6/translations/qtmultimedia_ja.qm
/usr/share/qt6/translations/qtmultimedia_ka.qm
/usr/share/qt6/translations/qtmultimedia_ko.qm
/usr/share/qt6/translations/qtmultimedia_nl.qm
/usr/share/qt6/translations/qtmultimedia_nn.qm
/usr/share/qt6/translations/qtmultimedia_pl.qm
/usr/share/qt6/translations/qtmultimedia_pt_BR.qm
/usr/share/qt6/translations/qtmultimedia_ru.qm
/usr/share/qt6/translations/qtmultimedia_sk.qm
/usr/share/qt6/translations/qtmultimedia_tr.qm
/usr/share/qt6/translations/qtmultimedia_uk.qm
/usr/share/qt6/translations/qtmultimedia_zh_CN.qm
/usr/share/qt6/translations/qtmultimedia_zh_TW.qm
/usr/share/qt6/translations/qtserialport_de.qm
/usr/share/qt6/translations/qtserialport_en.qm
/usr/share/qt6/translations/qtserialport_es.qm
/usr/share/qt6/translations/qtserialport_ja.qm
/usr/share/qt6/translations/qtserialport_ka.qm
/usr/share/qt6/translations/qtserialport_ko.qm
/usr/share/qt6/translations/qtserialport_pl.qm
/usr/share/qt6/translations/qtserialport_ru.qm
/usr/share/qt6/translations/qtserialport_uk.qm
/usr/share/qt6/translations/qtserialport_zh_CN.qm
/usr/share/qt6/translations/qtwebengine_ca.qm
/usr/share/qt6/translations/qtwebengine_de.qm
/usr/share/qt6/translations/qtwebengine_en.qm
/usr/share/qt6/translations/qtwebengine_es.qm
/usr/share/qt6/translations/qtwebengine_ka.qm
/usr/share/qt6/translations/qtwebengine_ko.qm
/usr/share/qt6/translations/qtwebengine_pl.qm
/usr/share/qt6/translations/qtwebengine_ru.qm
/usr/share/qt6/translations/qtwebengine_uk.qm
/usr/share/qt6/translations/qtwebengine_zh_CN.qm
/usr/share/qt6/translations/qtwebsockets_ca.qm
/usr/share/qt6/translations/qtwebsockets_de.qm
/usr/share/qt6/translations/qtwebsockets_en.qm
/usr/share/qt6/translations/qtwebsockets_es.qm
/usr/share/qt6/translations/qtwebsockets_fr.qm
/usr/share/qt6/translations/qtwebsockets_ja.qm
/usr/share/qt6/translations/qtwebsockets_ka.qm
/usr/share/qt6/translations/qtwebsockets_ko.qm
/usr/share/qt6/translations/qtwebsockets_pl.qm
/usr/share/qt6/translations/qtwebsockets_ru.qm
/usr/share/qt6/translations/qtwebsockets_uk.qm
/usr/share/qt6/translations/qtwebsockets_zh_CN.qm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6translations/7713a1753ce88f2c7e6b054ecc8e4c786df76300
/usr/share/package-licenses/qt6translations/79453f55fa8ee32d7b95581473edcbfd043e088f
