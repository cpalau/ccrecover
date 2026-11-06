---
title: "Kernel Log: Graphics drivers and Mesa3D updated, four new stable kernels"
date: 2010-04-07
author: "Thorsten Leemhuis"
source: http://www.h-online.com/open/features/Kernel-Log-Graphics-drivers-and-Mesa3D-updated-four-new-stable-kernels-971885.html
pages: 1
---

# Kernel Log: Graphics drivers and Mesa3D updated, four new stable kernels

**Thorsten Leemhuis**

**Almost simultaneously with the first series 1.8 X Server, the developers have also updated Mesa3D and various drivers. Four new stable kernels offer bug fixes and minor improvements.**

The X Server isn't the only component for which [a new version](../site/news/item/X-Server-1-8-with-new-configuration-mechanisms-970683.html "X Server 1.8 with new configuration mechanisms – 06 April 2010") has recently been released, as many other components that impact the graphics support in Linux distributions have also been updated in the past two weeks.

AMD employee Alex Deucher, for instance, has released versions [6.12.7](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/1032) and [6.13.0](http://thread.gmane.org/gmane.comp.freedesktop.xorg.drivers.ati/13926) of the xf86-video-ati driver package. While the former only fixes one minor bug, the latter offers numerous new features; among them are the support of many recent Radeon GPUs, KMS (Kernel-based Mode Setting) and various power saving features found in modern Radeon graphics chips; furthermore, the driver offers rudimentary support for the Evergreen GPUs on series 5000 Radeon HD cards.

Other advancements of version 6.13 include DRI2 support for all Radeon GPUs up to series r700, which are used, for instance, on series 4000 Radeon HD cards; in combination with current Mesa and DRM code, the driver offers 3D support for series r600 and r700 GPUs (Radeon HD series 2000, 3000 and 4000). However, these and various other new features can already be found in several Linux distributions, because the driver developers used code from the same development branch that has now produced version 6.13.

Just before the release of the new X Server, the Intel developers released version 2.11 of their X.org driver usually simply called "intel" [xf86-video-intel 2.11.0](http://thread.gmane.org/gmane.comp.freedesktop.xorg/43023). Its DRI2 support includes several functions which improve the coordination of new page impressions when changing pages ("page flipping"). With some older graphics cores such those in the 945 series, the driver is said to process large pixmaps considerably faster than before; furthermore, it already supports the graphics cores of Sandybridge processors, whose introduction Intel has been rumoured to plan for early next year. To simplify driver maintenance and development, the developers have removed further old code required for User Mode Setting (UMS), as the driver has already used KMS for several months.

[New versions](http://thread.gmane.org/gmane.comp.video.mesa3d.announce/95) of Mesa itself, which contains the 3D support and drivers, have also recently been released. However, [Mesa 7.7.1](http://www.mesa3d.org/relnotes-7.7.1.html) only differs from its predecessor by a few minor corrections. [Mesa 7.8](http://www.mesa3d.org/relnotes-7.8.html), on the other hand, which has been marked as a "development version", offers new features such as improved [EGL](http://www.mesa3d.org/egl.html), state trackers for [OpenGL ES 1.1 and 2.0](http://www.mesa3d.org/opengles.html), and documentation for Gallium; furthermore, the Gallium driver for Radeon's series r300 to r500 graphics chips has reportedly been improved considerably and is now reasonably stable, although still rather sluggish. On Easter Monday, [Mesa 7.8.1](http://thread.gmane.org/gmane.comp.video.mesa3d.devel/18611) was released as an "emergency release" to fix [a flaw](http://thread.gmane.org/gmane.comp.video.mesa3d.devel/18583) found in the previous version.

Jesse Barnes has also released [version 2.4.20 of the libdrm](http://thread.gmane.org/gmane.comp.video.dri.devel/44965), mostly adding minor corrections to this library which negotiates between Mesa and the kernel's graphics support. Other new releases in the past few days and weeks include [xf86-input-evdev 2.4.0](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/1034), [xf86-input-synaptics 1.2.2](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/1023) and [pixman 0.18.0](http://lists.freedesktop.org/archives/xorg-announce/2010-April/001288.html) – according to the latter's release email, this software offers significant performance improvements.

Meanwhile, the X.org developers have been discussing how to proceed with development. [Everything currently looks like](http://thread.gmane.org/gmane.comp.freedesktop.xorg.devel/6544/focus%3D6619) Peter Hutterer will take care of maintaining the recently released 1.8-series of the X Server. He plans to release minor version with bug fixes and small improvements every few weeks, just like he did while maintaining the 1.7 series. The development plans for version 1.9 are [currently being discussed](http://thread.gmane.org/gmane.comp.freedesktop.xorg.devel/6589/). Keith Packard, who led the 1.8 development, suggested to release new X Server every three months instead of every six; a merge of drivers or parts from them into the X Server is also under discussion.

At the end of March, AMD and NVIDIA also released new versions of their proprietary Linux drivers. Version 195.36.15 of the NVIDIA drivers fixes several flaws that caused the X Server to crash or performance to deteriorate in connection with KDE and non-antialiased text. The driver also supports the X Server 1.8 driver ABI as well as various recent graphics chips.

New additions listed in the [release notes](http://www2.ati.com/drivers/linux/catalyst_103_linux.pdf)![PDF](../site/icons/file-pdf.gif "PDF document") to version 10.3 of AMD's [Catalyst driver, which is also known as Fglrx](http://support.amd.com/us/Pages/drivers.aspx), include the "Early Look" support for the recently released [Red Hat Enterprise Linux 5.5](../site/open/features/What-s-new-in-Red-Hat-Enterprise-Linux-5-5-969097.html "What's new in Red Hat Enterprise Linux 5.5 – 01 April 2010"); the new version also offers various bug fixes. A day later, the vendor released an [experimental, 10.3-related driver version](http://support.amd.com/us/kbarticles/Pages/Catalyst-OpenGL-preview-driver.aspx) which already supports OpenGL 4.0.

### Linux version status

On Good Friday, the maintainers of the stable series released a total of four new kernel versions to introduce minor improvements and bug fixes: [2.6.27.46](http://thread.gmane.org/gmane.linux.kernel/969657), [2.6.31.13](http://thread.gmane.org/gmane.linux.kernel/969659), [2.6.32.11](http://thread.gmane.org/gmane.linux.kernel/969660) and [2.6.33.2](http://thread.gmane.org/gmane.linux.kernel/969663). The release email for the version 27 release emphatically recommends that users switch to the new version, while the emails for the version 32 and 33 releases only advise this with less urgency; as always, there is no mention of security issues. In his email to introduce the version 31 release, Greg Kroah-Hartman recommends that users switch to a version 32 or 33 kernel. It appears that he soon intends to stop maintaining the series 31 kernels altogether – although Kroah-Hartman had already announced this, he probably still released the thirteenth edition because he received some last corrections for this series.

At the end of March, Linus Torvalds already [released](http://thread.gmane.org/gmane.linux.kernel/968149) the third release candidate of 2.6.34. In his relatively long release email, Torvalds admits that the second RC didn't run very smoothly ("*Ok, so -rc2 was messy, no question about it.*"), and that the [shortened merge window](../site/open/features/Kernel-Log-Ceph-file-system-in-2-6-34-kernel-and-KVM-presentations-at-the-CLT2010-961429.html "Kernel Log: Ceph file system in 2.6.34, kernel and KVM presentations at the CLT2010 – 23 March 2010") didn't appear to have the desired effect this time. He also informed testers of some problems the two previous release candidates had with Ext3 and SELinux.

### In brief

*Kernel*

- In the past weeks and months, the maintainer of the RCU subsystem, Paul E. McKenney, has [posted a number of blog items](http://paulmck.livejournal.com/18755.html) which offer a detailed discussion of various "parallel programming" aspects. Parallel programming is crucial for the optimisation of multi-core systems.

*Graphics*

- In his two posts "Scrutinizing X Memory, [part 1: overview()](http://vignatti.wordpress.com/2010/03/25/scrutinizing-x-memory-part-1-overview/)" and "\[...\] [part 2: what's taking all that memory?](http://vignatti.wordpress.com/2010/03/25/scrutinizing-x-memory-part-2-whats-taking-all-that-memory/)", Tiago Vignatti explains some details in connection with the precise analysis of the memory consumption of X applications.

*Kernel environment ("plumbing layer"), userland drivers, developer tools, ...*

- Junio C Hamano has [released](http://thread.gmane.org/gmane.comp.version-control.git/142883) Git 1.7.0.3.
- [On their website](http://free-electrons.com/blog/elce-2009-videos/), the organisers of the Embedded Linux Conference Europe (ELCE) 2009 have posted video recordings of many of the conference presentations.
- Karel Zak has [released](http://thread.gmane.org/gmane.linux.kernel/964427) version 2.17.2 of the util-linux-ng tool collection used in many distributions.
- The [Systemtap developers](http://sourceware.org/systemtap/) have [released](http://thread.gmane.org/gmane.linux.systemtap/15416/focus%3D15430) version 1.2 of their tracing and debugging framework.
- The GCC developers have [released](http://gcc.gnu.org/ml/gcc/2010-04/msg00080.html) the first release candidate of GCC 4.5.0.

*Older Kernel Logs can be found in *[the archives](../site/open/news/archive/)* or by using *[the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log)* at *[The H Open Source](../site/open/)*. New editions of Kernel Logs are also mentioned on [Identi.ca](http://identi.ca/kernellog2) and [Twitter](http://twitter.com/kernellog2) via "@kernellog2". The Kernel Log author also posts updates about various topics on [Identi.ca](http://identi.ca/kernellogauthor) and [Twitter](http://twitter.com/kernellogauthor) via "@kernellogauthor".*

([thl](mailto:thl@ct.heise.de))
