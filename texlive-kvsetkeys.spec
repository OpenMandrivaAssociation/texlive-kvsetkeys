Name:		texlive-kvsetkeys
Version:	64632
Release:	1
Summary:	Key value parser with default handler support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/kvsetkeys
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kvsetkeys.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kvsetkeys.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kvsetkeys.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides \kvsetkeys, a variant of package keyval's
\setkeys. It allows the user to specify a handler that deals
with unknown options. Active commas and equal signs may be used
(e.g. see babel's shorthands) and only one level of curly
braces are removed from the values.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/kvsetkeys
%{_texmfdistdir}/tex/latex/kvsetkeys
%doc %{_texmfdistdir}/doc/latex/kvsetkeys

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
