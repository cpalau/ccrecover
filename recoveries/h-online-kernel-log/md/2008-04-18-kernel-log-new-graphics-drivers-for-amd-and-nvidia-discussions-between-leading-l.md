---
title: "Kernel Log: New graphics drivers for AMD and Nvidia; discussions between leading Linux developers"
date: 2008-04-18
author: "Jonathan Bennett"
source: http://www.h-online.com/open/news/item/Kernel-Log-New-graphics-drivers-for-AMD-and-Nvidia-discussions-between-leading-Linux-developers-734923.html
pages: 1
---

# Kernel Log: New graphics drivers for AMD and Nvidia; discussions between leading Linux developers

**Jonathan Bennett**

![Kernel Log logo](../site/imgs/43/3/6/1/6/9/8/a345f5e7c547062f.jpg) New versions of various Linux graphics card drivers have been introduced in the past few days. The open source [radeonhd](http://wiki.x.org/wiki/radeonhd) driver, suitable for newer Radeon graphics cards has had the most updates. Version 1.2 of the driver adds support for the GPUs used in Radeon HD models 34xx and 36xx and accelerates the output of 2D graphics in R5xx GPUs in the Radeon X1000 series. [Version 1.2.1](http://lists.opensuse.org/radeonhd/2008-04/msg00186.html), released on the heels of the driver, remedies some errors in radeonhd 1.2. [According to one developer](http://egbert-e.livejournal.com/1428.html), additional improvements, such as support for TV output and the 780G chipset, are on the way.

Nvidia has also released beta version 173.08 ([x86-32](http://www.nvidia.com/object/linux_display_ia32_173.08.html), [x86-64](http://www.nvidia.com/object/linux_display_amd64_173.08.html)) of its proprietary graphics driver for Linux. The new version works with the soon to be released Linux kernel 2.6.25 and provides [rudimentary support](http://www.nvnews.net/vbulletin/showthread.php?t=111460) for the X server in X.org 7.4, expected to be released in late April; Pre-release versions of the latter are already included in the developer branches and beta versions of some distributions. Developers of the Intel graphics driver have also released a new [beta version](http://lists.freedesktop.org/archives/xorg/2008-April/034668.html).

Two debates on the Linux Kernel Mailing List (LKML) turned into something of a scrap. One of the discussions was triggered when Mark Lord found [an error](http://thread.gmane.org/gmane.linux.kernel/663422) in 2.6.25 rc8 and did not quite know how to track down its cause. That set off a long and sometimes harsh debate about how much effort the parties involved – kernel developers and the developers and users that report bugs – should expend to find the cause of errors not present in previous kernel versions.

Some of the participants in the discussion were of the opinion that those who report the problems cannot be expected to use *[git bisect](http://www.kernel.org/pub/software/scm/git/docs/git-bisect.html)* to search for the commit at fault, with the compilation and testing of various stages of development that go along with it; and that searching for potential causes ought to be the responsibility of the subsystem maintainers and other developers. On the other hand, other developers argued that many errors are dependent upon the environment (hardware, distribution, configuration, etc.) and therefore the person making the report had to help narrow down the cause of the bug.

The discussion about this problem – which has since been solved – will not yield any substantial results, since there are still no detailed rules that hackers follow when someone reports a bug. In fact, different developers and subsystem administrators often proceed differently when tracking down errors. How they proceed is greatly influenced by the knowledge level and attitude of the person reporting the bug, as well as the type of error.

The second [discussion](http://thread.gmane.org/gmane.linux.file-systems/22558) among prominent hackers revolved around the integration of the OMFS file system, used by Rio Karma, ReplayTV and others. Andrew Morton and others spoke out against including the OMFS code in the kernel – there was only a small number of OMFS users, making a FUSE ([Filesystem in Userspace](http://fuse.sourceforge.net/)) based variant a better choice. Well known kernel developers on the other hand, like Christoph Hellwig, Alan Cox and David Woodhouse were of a different opinion, calling explicitly for the inclusion of OMFS.

### Kernel Log in brief

- With the release of 2.6.25-rc9 [last Friday](http://thread.gmane.org/gmane.linux.kernel/664509) and a few changes made in the past few hours, the release of 2.6.25 could happen at [any time](http://thread.gmane.org/gmane.linux.kernel/664225/focus%3D666304).
- VIA recently announced that it wants to increase cooperation with open source developers. For that purpose, a new [website](http://linux.via.com.tw/) will be set up. VIA has made similar announcements in the past, but tangible results have not materialised.
- First generation Sandisk MP3 players in the Sansa e200 series can now be driven by Linux. To do this, [SansaLinux](http://www.sansalinux.org/) developers used [iPodLinux](http://ipodlinux.org/).
- An Intel developer [explained](http://thread.gmane.org/gmane.linux.kernel.wireless.general/13107) on the LKML that the proprietary WiMAX Supplicant for the [recently released WIMAX stack for Linux](../site/news/item/Kernel-log-developer-statistics-on-Linux-2-6-25-status-report-of-Linux-Driver-Project-734843.html "Kernel log: developer statistics on Linux 2.6.25, status report of Linux Driver Project – 11 April 2008, 09:56") is only a temporary solution and that an open source variant was in the works.
- The [Open Graphics Project](http://www.opengraphics.org/) is now taking [pre-orders](http://www.opengraphics.org/) for a trial version of the open source hardware developed within the project; the offer is primarily directed at hardware and graphics chip hackers for test purposes.
- The X Developers' Conference ([XDC2008](http://xorg.freedesktop.org/wiki/Events/XDC2008)) begins today in Mountain View, California, where numerous X developers will present their work and discuss the future of X.org.

([jbe](mailto: "Jonathan Bennett"))
