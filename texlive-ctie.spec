Name:		texlive-ctie
Version:	1.1
Release:	1
Summary:	C version of tie (merging Web change files)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/web/c_cpp/ctie
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctie.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctie.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-kpathsea
Requires:	texlive-ctie.bin
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is a version of tie converted for use with cweb.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/ctie.1*
%doc %{_texmfdir}/doc/man/man1/ctie.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
