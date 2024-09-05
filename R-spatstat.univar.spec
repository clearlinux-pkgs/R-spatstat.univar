#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v18
# autospec commit: f35655a
#
Name     : R-spatstat.univar
Version  : 3.0.1
Release  : 2
URL      : https://cran.r-project.org/src/contrib/spatstat.univar_3.0-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/spatstat.univar_3.0-1.tar.gz
Summary  : One-Dimensional Probability Distribution Support for the
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-spatstat.univar-lib = %{version}-%{release}
Requires: R-spatstat.utils
BuildRequires : R-spatstat.utils
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
including kernel density estimation, weighted empirical cumulative
	     distribution functions, Kaplan-Meier and reduced-sample estimators
	     for right-censored data, heat kernels, kernel properties,
	     quantiles and integration.

%package lib
Summary: lib components for the R-spatstat.univar package.
Group: Libraries

%description lib
lib components for the R-spatstat.univar package.


%prep
%setup -q -n spatstat.univar

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1725544759

%install
export SOURCE_DATE_EPOCH=1725544759
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/spatstat.univar/CITATION
/usr/lib64/R/library/spatstat.univar/DESCRIPTION
/usr/lib64/R/library/spatstat.univar/INDEX
/usr/lib64/R/library/spatstat.univar/Meta/Rd.rds
/usr/lib64/R/library/spatstat.univar/Meta/features.rds
/usr/lib64/R/library/spatstat.univar/Meta/hsearch.rds
/usr/lib64/R/library/spatstat.univar/Meta/links.rds
/usr/lib64/R/library/spatstat.univar/Meta/nsInfo.rds
/usr/lib64/R/library/spatstat.univar/Meta/package.rds
/usr/lib64/R/library/spatstat.univar/NAMESPACE
/usr/lib64/R/library/spatstat.univar/NEWS
/usr/lib64/R/library/spatstat.univar/R/spatstat.univar
/usr/lib64/R/library/spatstat.univar/R/spatstat.univar.rdb
/usr/lib64/R/library/spatstat.univar/R/spatstat.univar.rdx
/usr/lib64/R/library/spatstat.univar/doc/packagesizes.txt
/usr/lib64/R/library/spatstat.univar/help/AnIndex
/usr/lib64/R/library/spatstat.univar/help/aliases.rds
/usr/lib64/R/library/spatstat.univar/help/macros/defns.Rd
/usr/lib64/R/library/spatstat.univar/help/paths.rds
/usr/lib64/R/library/spatstat.univar/help/spatstat.univar.rdb
/usr/lib64/R/library/spatstat.univar/help/spatstat.univar.rdx
/usr/lib64/R/library/spatstat.univar/html/00Index.html
/usr/lib64/R/library/spatstat.univar/html/R.css
/usr/lib64/R/library/spatstat.univar/info/packagesizes.txt
/usr/lib64/R/library/spatstat.univar/tests/all.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/spatstat.univar/libs/spatstat.univar.so
