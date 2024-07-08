Name:		texlive-ctie
Version:	70015
Release:	1
Summary:	C version of tie (merging Web change files)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/web/c_cpp/ctie
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctie.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctie.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-kpathsea
Requires:	texlive-ctie.bin

%description
This is a version of tie converted for use with cweb.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/ctie.1*
%doc %{_texmfdistdir}/doc/man/man1/ctie.man1.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
