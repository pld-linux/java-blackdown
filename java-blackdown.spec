Summary:	Blackdown Java - JDK (Java Development Kit) for Linux
Summary(pl):	Blackdown Java - JDK (¶rodowisko programistyczne Javy) dla Linuksa
Name:		java-blackdown
%ifarch %{ix86} sparc sparc64
%define	mainversion	1.4.1
Version:	1.4.1_01
Release:	2
%else
%define mainversion 1.3.1
Version:	1.3.1
Release:	1
%endif
License:	restricted, non-distributable
Group:		Development/Languages/Java
%ifarch	%{ix86}
Source0:	ftp://metalab.unc.edu/pub/linux/devel/lang/java/blackdown.org/JDK-1.4.1/i386/01/j2sdk-1.4.1-01-linux-i586-gcc3.2.bin
# NoSource0-md5:	a0c7838233603fccb30641998195e8bc
NoSource:	0
%endif
%ifarch ppc
Source1:	ftp://metalab.unc.edu/pub/linux/devel/lang/java/blackdown.org/JDK-%{version}/ppc/FCS-02b/j2sdk-%{version}-02b-FCS-linux-ppc.bin
NoSource:	1
%endif
%ifarch sparc sparc64
Source2:	ftp://metalab.unc.edu/pub/linux/devel/lang/java/blackdown.org/JDK-1.4.1/sparc/01/j2sdk-1.4.1-01-linux-sparc-gcc3.2.bin
NoSource:	2
%endif
URL:		http://www.blackdown.org/
Provides:	jdk = %{version}
Requires:	%{name}-jre = %{version}
Obsoletes:	blackdown-java-sdk
Obsoletes:	ibm-java
Obsoletes:	java-sun
Obsoletes:	jdk
Obsoletes:	kaffe
ExclusiveArch:	%{ix86} ppc sparc sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		javadir		%{_libdir}/java
%define		jredir		%{_libdir}/java/jre
%define		classdir	%{_datadir}/java
%define		netscape4dir	/usr/lib/netscape
%if %{?_with_ra:1}%{!?_with_ra:0}
%define		mozilladir	/usr/X11R6/lib/mozilla
%else
%define		mozilladir	/usr/lib/mozilla
%endif

# prevent wrong requires when building with another JRE
%define		_noautoreqdep	libawt.so libjava.so libjvm.so libmlib_image.so libverify.so libnet.so
# ??? unixODBC-devel? no package provides it
%define		_noautoreq	libodbcinst.so libodbc.so

%ifarch %{ix86}
%define		archd	i386
%endif
%ifarch ppc
%define		archd	ppc
%endif
%ifarch sparc sparc64
%define		archd	sparc
%endif

%description
Blackdown Java implementation (based on Sun Java). This package
contains JDK (Java Development Kit).

%description -l pl
Implementacja Javy z Blackdown (bazuj±ca na wersji Suna). Ten pakiet
zawiera JDK (¶rodowisko programistyczne Javy).

%package jre
Summary:	Blackdown Java - JRE (Java Runtime Environment) for Linux
Summary(pl):	Blackdown Java - JRE (¶rodowisko uruchomieniowe Javy) dla Linuksa
Group:		Development/Languages/Java
Requires:	XFree86-libs
%if %{?_with_ra:0}%{!?_with_ra:1}
Requires:	libgcc >= 3.2.0
Requires:	libstdc++ >= 3.2.0
%endif
Provides:	jre = %{version}
#Provides:	jar
Provides:	java
Obsoletes:	jre
Obsoletes:	java-sun-jre

%description jre
Blackdown Java implementation (based on Sun Java). This package
contains JRE (Java Runtime Environment).

%description jre -l pl
Implementacja Javy z Blackdown (bazuj±ca na wersji Suna). Ten pakiet
zawiera JRE (¶rodowisko uruchomieniowe Javy).

%package demos
Summary:	JDK demonstration programs
Summary(pl):	Programy demonstracyjne do JDK
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}
Obsoletes:	java-sun-demos
Obsoletes:	jdk-demos

%description demos
JDK demonstration programs.

%description demos -l pl
Programy demonstracyjne do JDK.

%ifarch %{ix86}
%package -n netscape4-plugin-%{name}
Summary:	Netscape 4.x Java plugin
Summary(pl):	Wtyczka Javy do Netscape 4.x
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}
Requires:	netscape-common >= 4.0
Obsoletes:	blackdown-java-sdk-netscape4-plugin
Obsoletes:	java-sun-nn4-plugin
Obsoletes:	jre-netscape4-plugin
Obsoletes:	netscape4-plugin-java-sun

%description -n netscape4-plugin-%{name}
Java plugin for Netscape 4.x.

%description -n netscape4-plugin-%{name} -l pl
Wtyczka z obs³ug± Javy dla Netscape 4.x.
%endif

%package tools
Summary:	Shared java tools
Summary(pl):	Wspó³dzielone narzêdzia javy
Group:		Development/Languages/Java
Provides:	jar
Provides:	java-shared
Obsoletes:	java-shared
Obsoletes:	jar
Obsoletes:	fastjar

%description tools
This package contains tools that are common for every Java(tm) implementation,
such as rmic or jar.

%description tools -l pl
Pakiet ten zawiera narzêdzia wspólne dla ka¿dej implementacji Javy(tm), takie
jak rmic czy jar.


%package -n mozilla-plugin-%{name}
Summary:	Mozilla Java plugin
Summary(pl):	Wtyczka Javy do Mozilli
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}
PreReq:		mozilla-embedded
Obsoletes:	blackdown-java-sdk-mozilla-plugin
Obsoletes:	java-sun-moz-plugin
Obsoletes:	jre-mozilla-plugin
Obsoletes:	mozilla-plugin-blackdown-java-sdk
Obsoletes:	mozilla-plugin-java-sun

%description -n mozilla-plugin-%{name}
Java plugin for Mozilla.

%description -n mozilla-plugin-%{name} -l pl
Wtyczka z obs³ug± Javy dla Mozilli.

%prep
%setup -qcT -n j2sdk%{mainversion}
%ifarch %{ix86}
tail -n +522 %{SOURCE0} | bzip2 -dc - | tar xf - -C ..
%endif
%ifarch ppc
tail -n +400 %{SOURCE1} | bzip2 -dc - | tar xf - -C ..
%endif
%ifarch sparc sparc64
tail -n +522 %{SOURCE2} | bzip2 -dc - | tar xf - -C ..
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{jredir},%{classdir},%{_bindir},%{_includedir}} \
	$RPM_BUILD_ROOT%{_mandir}/{,ja/}man1

cp -rf bin demo include lib $RPM_BUILD_ROOT%{javadir}
install man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
install man/ja/man1/* $RPM_BUILD_ROOT%{_mandir}/ja/man1

# not needed now?
#ln -sf %{jredir} $RPM_BUILD_ROOT/usr/lib/jre
#ln -sf %{javadir}/include $RPM_BUILD_ROOT%{_includedir}/java

%ifarch ppc
ln -sf .java_wrapper jre/bin/java_vm
rm -rf jre/bin/realpath
ln -s ppc/realpath jre/bin/realpath
%endif 

%ifnarch ppc
mv -f jre/lib/%{archd}/client/Xusage.txt jre/Xusage.client
mv -f jre/lib/%{archd}/server/Xusage.txt jre/Xusage.server
mv jre/lib/font.properties{,.orig}
mv jre/lib/font.properties{.Redhat6.1,}
%endif

mv -f jre/lib/*.txt jre

cp -rf jre/{bin,lib} $RPM_BUILD_ROOT%{jredir}

# conflict with heimdal
for i in kinit klist ; do
        ln -sf %{jredir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/j$i
done

for i in JavaPluginControlPanel java java_vm keytool ktab orbd policytool \
	rmid rmiregistry servertool tnameserv ; do
	ln -sf %{jredir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done

for i in HtmlConverter appletviewer extcheck idlj jar jarsigner java-rmi.cgi \
         javac javadoc javah javap jdb native2ascii rmic serialver ; do
	ln -sf %{javadir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done

%ifarch ppc
ln -sf %{javadir}/bin/j2sdk-config $RPM_BUILD_ROOT%{_bindir}/j2sdk-config
%endif 

rm -f $RPM_BUILD_ROOT%{javadir}/bin/java
ln -sf %{jredir}/bin/java $RPM_BUILD_ROOT%{javadir}/bin/java

%ifarch %{ix86}
install -d $RPM_BUILD_ROOT%{netscape4dir}/{plugins,java/classes}
install jre/plugin/%{archd}/netscape4/javaplugin.so $RPM_BUILD_ROOT%{netscape4dir}/plugins
for i in javaplugin rt sunrsasign ; do
	ln -sf %{jredir}/lib/$i.jar $RPM_BUILD_ROOT%{netscape4dir}/java/classes
done
%endif

install -d $RPM_BUILD_ROOT{%{mozilladir}/plugins,%{jredir}/plugin/%{archd}/mozilla}
install jre/plugin/%{archd}/mozilla/javaplugin_oji.so \
	$RPM_BUILD_ROOT%{jredir}/plugin/%{archd}/mozilla
ln -sf %{jredir}/plugin/%{archd}/mozilla/javaplugin_oji.so \
	$RPM_BUILD_ROOT%{mozilladir}/plugins

# these binaries are in %{jredir}/bin - not needed in %{javadir}/bin?
rm -f $RPM_BUILD_ROOT%{javadir}/bin/{JavaPluginControlPanel,keytool,kinit,klist,ktab,orbd,policytool,rmid,rmiregistry,servertool,tnameserv}

%clean
rm -rf $RPM_BUILD_ROOT

%pre jre
if [ -L %{jredir} ]; then
	rm -f %{jredir}
fi
if [ -L %{javadir} ]; then
	rm -f %{javadir}
fi

%files
%defattr(644,root,root,755)
%doc COPYRIGHT LICENSE README README.html
%attr(755,root,root) %{_bindir}/HtmlConverter
%attr(755,root,root) %{_bindir}/appletviewer
%attr(755,root,root) %{_bindir}/extcheck
%attr(755,root,root) %{_bindir}/idlj
%attr(755,root,root) %{_bindir}/jarsigner
%attr(755,root,root) %{_bindir}/java-rmi.cgi
%attr(755,root,root) %{_bindir}/javac
%attr(755,root,root) %{_bindir}/javadoc
%attr(755,root,root) %{_bindir}/javah
%attr(755,root,root) %{_bindir}/javap
%attr(755,root,root) %{_bindir}/jdb
%attr(755,root,root) %{_bindir}/native2ascii
%attr(755,root,root) %{_bindir}/serialver
%ifarch ppc
%attr(755,root,root) %{_bindir}/j2sdk-config
%endif
%attr(755,root,root) %{javadir}/bin/HtmlConverter
%attr(755,root,root) %{javadir}/bin/appletviewer
%attr(755,root,root) %{javadir}/bin/extcheck
%attr(755,root,root) %{javadir}/bin/idlj
%attr(755,root,root) %{javadir}/bin/jar
%attr(755,root,root) %{javadir}/bin/jarsigner
%attr(755,root,root) %{javadir}/bin/java-rmi.cgi
%attr(755,root,root) %{javadir}/bin/javac
%attr(755,root,root) %{javadir}/bin/javadoc
%attr(755,root,root) %{javadir}/bin/javah
%attr(755,root,root) %{javadir}/bin/javap
%attr(755,root,root) %{javadir}/bin/jdb
%attr(755,root,root) %{javadir}/bin/native2ascii
%attr(755,root,root) %{javadir}/bin/serialver
%ifarch ppc
%attr(755,root,root) %{javadir}/bin/.java_wrapper
%attr(755,root,root) %{javadir}/bin/awt_robot
%attr(755,root,root) %{javadir}/bin/j2sdk-config
%attr(755,root,root) %{javadir}/bin/%{archd}
%endif
%{javadir}/include
#%%{_includedir}/jdk
%dir %{javadir}/lib
%{javadir}/lib/*.jar
%{javadir}/lib/*.idl
%ifarch ppc
%{javadir}/lib/%{archd}/*.so
%endif
%{_mandir}/man1/appletviewer.1*
%{_mandir}/man1/extcheck.1*
%ifnarch ppc
%{_mandir}/man1/idlj.1*
%endif
%{_mandir}/man1/jarsigner.1*
%{_mandir}/man1/javac.1*
%{_mandir}/man1/javadoc.1*
%{_mandir}/man1/javah.1*
%{_mandir}/man1/javap.1*
%{_mandir}/man1/jdb.1*
%{_mandir}/man1/native2ascii.1*
%{_mandir}/man1/serialver.1*
%lang(ja) %{_mandir}/ja/man1/appletviewer.1*
%lang(ja) %{_mandir}/ja/man1/extcheck.1*
%ifnarch ppc
%lang(ja) %{_mandir}/ja/man1/idlj.1*
%endif
%lang(ja) %{_mandir}/ja/man1/jarsigner.1*
%lang(ja) %{_mandir}/ja/man1/javac.1*
%lang(ja) %{_mandir}/ja/man1/javadoc.1*
%lang(ja) %{_mandir}/ja/man1/javah.1*
%lang(ja) %{_mandir}/ja/man1/javap.1*
%lang(ja) %{_mandir}/ja/man1/jdb.1*
%lang(ja) %{_mandir}/ja/man1/native2ascii.1*
%lang(ja) %{_mandir}/ja/man1/serialver.1*

%files jre
%defattr(644,root,root,755)
%doc jre/JavaPluginControlPanel.html
%ifnarch ppc
%doc jre/Welcome.html jre/Xusage*
%doc jre/{CHANGES,COPYRIGHT,LICENSE,README,*.txt}
%endif
%attr(755,root,root) %{_bindir}/JavaPluginControlPanel
%attr(755,root,root) %{_bindir}/java
%attr(755,root,root) %{_bindir}/java_vm
%attr(755,root,root) %{_bindir}/keytool
%attr(755,root,root) %{_bindir}/policytool
%ifnarch ppc
%attr(755,root,root) %{_bindir}/jkinit
%attr(755,root,root) %{_bindir}/jklist
%attr(755,root,root) %{_bindir}/ktab
%attr(755,root,root) %{_bindir}/orbd
%attr(755,root,root) %{_bindir}/servertool
%endif
%attr(755,root,root) %{_bindir}/rmid
%attr(755,root,root) %{_bindir}/tnameserv
%dir %{javadir}
%dir %{javadir}/bin
%attr(755,root,root) %{javadir}/bin/java
%dir %{jredir}
%dir %{jredir}/bin
%attr(755,root,root) %{jredir}/bin/JavaPluginControlPanel
%attr(755,root,root) %{jredir}/bin/java
%attr(755,root,root) %{jredir}/bin/java_vm
%attr(755,root,root) %{jredir}/bin/keytool
%ifnarch ppc
%attr(755,root,root) %{jredir}/bin/kinit
%attr(755,root,root) %{jredir}/bin/klist
%attr(755,root,root) %{jredir}/bin/ktab
%attr(755,root,root) %{jredir}/bin/orbd
%attr(755,root,root) %{jredir}/bin/servertool
%endif
%attr(755,root,root) %{jredir}/bin/policytool
%attr(755,root,root) %{jredir}/bin/rmid
%attr(755,root,root) %{jredir}/bin/tnameserv
%ifarch ppc
%attr(755,root,root) %{jredir}/bin/.java_wrapper
%attr(755,root,root) %{jredir}/bin/realpath
%attr(755,root,root) %{jredir}/bin/awt_robot
%attr(755,root,root) %{jredir}/bin/j2sdk-config
%attr(755,root,root) %{jredir}/bin/%{archd}
%endif
%dir %{jredir}/lib
%attr(755,root,root) %{jredir}/lib/%{archd}
%ifarch ppc
%{jredir}/lib/jvm.cfg
%{jredir}/lib/tzmappings
%endif
%{jredir}/lib/applet
%{jredir}/lib/audio
%{jredir}/lib/cmm
%{jredir}/lib/ext
%{jredir}/lib/fonts
%ifnarch ppc
%{jredir}/lib/im
%{jredir}/lib/zi
%endif
%{jredir}/lib/images
%dir %{jredir}/lib/security
%{jredir}/lib/security/*.*
%verify(not md5 size mtime) %config(noreplace) %{jredir}/lib/security/cacerts
%{jredir}/lib/*.jar
%{jredir}/lib/*.properties
#%%{jredir}/lib/*.cfg
#%%{jredir}/lib/tzmappings
%lang(ja) %{jredir}/lib/*.properties.ja
#%lang(zh) %{jredir}/lib/*.properties.zh
%dir %{jredir}/plugin
%dir %{jredir}/plugin/%{archd}
%dir %{classdir}
%{_mandir}/man1/java.1*
%{_mandir}/man1/keytool.1*
%ifnarch ppc
%{_mandir}/man1/orbd.1*
%{_mandir}/man1/policytool.1*
%{_mandir}/man1/servertool.1*
%endif
%{_mandir}/man1/rmid.1*
%{_mandir}/man1/tnameserv.1*
%lang(ja) %{_mandir}/ja/man1/java.1*
%lang(ja) %{_mandir}/ja/man1/keytool.1*
%ifnarch ppc
%lang(ja) %{_mandir}/ja/man1/orbd.1*
%lang(ja) %{_mandir}/ja/man1/policytool.1*
%lang(ja) %{_mandir}/ja/man1/servertool.1*
%endif
%lang(ja) %{_mandir}/ja/man1/rmid.1*
%lang(ja) %{_mandir}/ja/man1/tnameserv.1*

%files demos
%defattr(644,root,root,755)
%{javadir}/demo

%ifarch %{ix86}
%files -n netscape4-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{netscape4dir}/plugins/javaplugin.so
%{netscape4dir}/java/classes/*
%dir %{jredir}/lib/locale
%lang(de) %{jredir}/lib/locale/de
%lang(es) %{jredir}/lib/locale/es
%lang(fr) %{jredir}/lib/locale/fr
%lang(it) %{jredir}/lib/locale/it
%lang(ja) %{jredir}/lib/locale/ja
%lang(ko) %{jredir}/lib/locale/ko
%lang(ko) %{jredir}/lib/locale/ko.UTF-8
%lang(sv) %{jredir}/lib/locale/sv
%lang(zh_CN) %{jredir}/lib/locale/zh
%lang(zh_CN) %{jredir}/lib/locale/zh.GBK
%lang(zh_TW) %{jredir}/lib/locale/zh_TW
%lang(zh_TW) %{jredir}/lib/locale/zh_TW.BIG5
%endif

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jar
%attr(755,root,root) %{_bindir}/rmic
%attr(755,root,root) %{_bindir}/rmiregistry
%attr(755,root,root) %{jredir}/bin/rmiregistry
%attr(755,root,root) %{javadir}/bin/rmic
%{_mandir}/man1/jar.1*
%lang(ja) %{_mandir}/ja/man1/jar.1*
%{_mandir}/man1/rmiregistry.1*
%{_mandir}/man1/rmic.1*
%lang(ja) %{_mandir}/ja/man1/rmiregistry.1*
%lang(ja) %{_mandir}/ja/man1/rmic.1*

%files -n mozilla-plugin-%{name}
%defattr(644,root,root,755)
%dir %{jredir}/plugin/%{archd}/mozilla
%attr(755,root,root) %{jredir}/plugin/%{archd}/mozilla/javaplugin_oji.so
%attr(755,root,root) %{mozilladir}/plugins/javaplugin_oji.so
