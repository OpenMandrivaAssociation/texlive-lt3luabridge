Name:		texlive-lt3luabridge
Version:	64801
Release:	2
Summary:	Execute Lua code in any TeX engine that exposes the shell
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lt3luabridge
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lt3luabridge.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lt3luabridge.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lt3luabridge.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is an expl3(-generic) package for plain TeX, LaTeX, and
ConTeXt that allows you to execute Lua code in LuaTeX or any
other TeX engine that exposes the shell.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/lt3luabridge
%{_texmfdistdir}/tex/generic/lt3luabridge
%doc %{_texmfdistdir}/doc/generic/lt3luabridge

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
