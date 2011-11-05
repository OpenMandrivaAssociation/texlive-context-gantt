# revision 24044
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-gantt
# catalog-date 2011-09-20 21:18:19 +0200
# catalog-license pd
# catalog-version undef
Name:		texlive-context-gantt
Version:	20110920
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Gantt is a module for drawing Gantt charts via metapost or
pgf/tikz.

%pre
    %_texmf_mtxrun_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post
    %_texmf_mtxrun_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
	%_texmf_mtxrun_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
