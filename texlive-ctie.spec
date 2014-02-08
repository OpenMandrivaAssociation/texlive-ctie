# revision 23089
# category TLCore
# catalog-ctan /web/c_cpp/ctie
# catalog-date 2011-04-16 11:10:37 +0200
# catalog-license gpl
# catalog-version 1.1
Name:		texlive-ctie
Version:	1.1
Release:	3
Summary:	C version of tie (merging Web change files)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/web/c_cpp/ctie
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctie.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctie.doc.tar.xz
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 750686
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 718183
- texlive-ctie
- texlive-ctie
- texlive-ctie
- texlive-ctie

