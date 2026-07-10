%global tl_name ctie
%global tl_revision 77830

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	C version of tie (merging Web change files)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/web/c_cpp/ctie
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ctie.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ctie.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(ctie.bin)
Requires:	texlive(kpathsea)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a version of tie converted for use with cweb.

