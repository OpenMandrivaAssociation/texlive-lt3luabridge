%global tl_name lt3luabridge
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2.2
Release:	%{tl_revision}.1
Summary:	Execute Lua code in any TeX engine that exposes the shell
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/lt3luabridge
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lt3luabridge.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lt3luabridge.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lt3luabridge.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is an expl3(-generic) package for plain TeX, LaTeX, and ConTeXt
that allows you to execute Lua code in LuaTeX or any other TeX engine
that exposes the shell.

