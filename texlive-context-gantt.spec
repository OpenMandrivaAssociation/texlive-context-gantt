# revision 27472
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-gantt
# catalog-date 2012-03-20 08:48:23 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-context-gantt
Version:	20120320
Release:	4
Summary:	GANTT module for ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-gantt
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-gantt.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-gantt.doc.tar.xz
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
%{_texmfdistdir}/tex/context/third/gantt/gantt-s-mp.tex
%{_texmfdistdir}/tex/context/third/gantt/gantt-s-tikz.tex
%{_texmfdistdir}/tex/context/third/gantt/t-gantt.tex
%doc %{_texmfdistdir}/doc/context/third/gantt/README
%doc %{_texmfdistdir}/doc/context/third/gantt/examples/gantt-1.tex
%doc %{_texmfdistdir}/doc/context/third/gantt/examples/gantt-2.tex
%doc %{_texmfdistdir}/doc/context/third/gantt/examples/gantt-3.tex
%doc %{_texmfdistdir}/doc/context/third/gantt/examples/gantt-4.tex
%doc %{_texmfdistdir}/doc/context/third/gantt/examples/gantt-5.tex
%doc %{_texmfdistdir}/doc/context/third/gantt/gantt.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
