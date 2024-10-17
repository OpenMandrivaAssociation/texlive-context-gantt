Name:		texlive-context-gantt
Version:	47085
Release:	2
Summary:	GANTT module for ConTeXt
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/context/contrib/context-gantt
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-gantt.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-gantt.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context
Requires:	texlive-hatching

%description
Gantt is a module for drawing Gantt charts via metapost or
pgf/tikz.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/gantt
%doc %{_texmfdistdir}/doc/context/third/gantt

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
