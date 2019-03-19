Name:             internal-ripgrep
Version:          0.10.0
Release:          1%{?dist}
Summary:          ripgrep recursively searches directories for a regex pattern 
License:          MIT
URL:              https://github.com/BurntSushi/ripgrep
Source0:          https://github.com/BurntSushi/ripgrep/releases/download/%{version}/ripgrep-%{version}-x86_64-unknown-linux-musl.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-buildroot
Requires(post):   /usr/sbin/update-alternatives
Requires(postun): /usr/sbin/update-alternatives

# sysroot's configuration
#------------------------
%define _prefix              /opt/internal/root
%define _exec_prefix         %{_prefix}
%define _bindir              %{_prefix}/bin
%define _syscompletiondir    /etc/bash_completion.d
%define _internalcompletiondir  %{_prefix}%{_syscompletiondir}
#------------------------

%description
ripgrep is a line-oriented search tool that recursively searches
your current directory for a regex pattern while respecting your
gitignore rules. ripgrep has first class support on Windows,
macOS and Linux, with binary downloads available for every
release. ripgrep is similar to other popular search tools like
The Silver Searcher, ack and grep.

%prep
%setup -qn ripgrep-%{version}-x86_64-unknown-linux-musl

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_internalcompletiondir}
# Copy the files in the targeted prefix
cp rg $RPM_BUILD_ROOT/%{_bindir}
cp complete/rg.bash $RPM_BUILD_ROOT/%{_internalcompletiondir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/update-alternatives --install /usr/bin/rg rg %{_bindir}/rg 0
if [ -d %{_syscompletiondir} ] ; then
  ln -s %{_internalcompletiondir}/rg.bash %{_syscompletiondir}/rg.bash
fi

%postun
if [ $1 -eq 0 ] ; then
  /usr/sbin/update-alternatives --remove rg %{_bindir}/rg
  if [ -L %{_syscompletiondir}/rg.bash ] ; then
    unlink %{_syscompletiondir}/rg.bash
  fi
fi

%files
%defattr (-,root,root)

# Files to include
%{_bindir}/rg
%{_internalcompletiondir}/rg.bash

%changelog
* Thu Feb 14 2019 Antoine Allard <antoine.allard@internal.com>
- Created the RPM

