%bcond_with bootstrap
%global packname  gWidgets
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}

Name:             R-%{packname}
Version:          0.0.52
Release:          2
Summary:          gWidgets API for building toolkit-independent, interactive GUIs
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/gWidgets_0.0-52.tar.gz
Requires:         R-methods R-utils R-cairoDevice
%if %{without bootstrap}
Requires:         R-gWidgetsRGtk2 R-gWidgetstcltk
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods
BuildRequires:    R-utils R-cairoDevice
%if %{without bootstrap}
BuildRequires:    R-gWidgetsRGtk2 R-cairoDevice R-gWidgetstcltk
%endif
BuildRequires:    x11-server-xvfb

%description
gWidgets provides a toolkit-independent API for building interactive GUIs.
Atleast one of the gWidgetsXXX packages, such as gWidgetstcltk, needs to
be installed. Some icons are on loan from the scigraphica project

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
xvfb-run %{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/images
%{rlibdir}/%{packname}/install
%{rlibdir}/%{packname}/tests
