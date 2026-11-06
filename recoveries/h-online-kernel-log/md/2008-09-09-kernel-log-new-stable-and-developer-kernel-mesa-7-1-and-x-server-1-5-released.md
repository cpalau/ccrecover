---
title: "Kernel-Log: New stable and developer kernel, Mesa 7.1 and X-Server 1.5 released."
date: 2008-09-09
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-New-stable-and-developer-kernel-Mesa-7-1-and-X-Server-1-5-released-737227.html
pages: 1
---

# Kernel-Log: New stable and developer kernel, Mesa 7.1 and X-Server 1.5 released.

**Dj Walker-Morgan**

The Linux stable series managers have released kernel versions [2.6.25.17](http://thread.gmane.org/gmane.linux.kernel/731054), [2.6.26.4](http://thread.gmane.org/gmane.linux.kernel/731055) and [2.6.26.5](http://thread.gmane.org/gmane.linux.kernel/731166), bringing numerous fixes and improvements from their preceding versions in the [2.6.25](../site/open/features/Improvements-throughout-what-s-new-in-Linux-2-6-25-746484.html "Improvements throughout – what's new in Linux 2.6.25 â 21 April 2008, 08:49") and [2.6.26](../site/open/features/Polish-and-add-ons-the-latest-updates-in-Linux-2-6-26-746492.html "Polish and add-ons; the latest updates in Linux 2.6.26 â 18 July 2008, 10:22") series. 2.6.26.5 was released to fix a problem only introduced in 2.6.26.4. Whether the new versions fix any security problems was not disclosed, but the releases did carry the note "Any users of the 2.6.25/2.6.26 kernel series should upgrade to this version.", addressing those who compile their own kernel, rather than those who receive their kernel from their Linux distributor.

Willy Tarreau has published 2.4.36.7, with minor fixes and improvements to the now quite old 2.4 series. In the email announcing the release, Tarreau happily gives more information that the 2.6 stable series manages, and refers to security fixes for [CVE-2008-2826](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2008-2826) and [CVE-2008-3525](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2008-3525). Tarreau also announced [2.4.37-rc1](http://thread.gmane.org/gmane.linux.kernel/730815), the start of development on 2.4.37. In the announcement of this preliminary version, Tarreau details the new features, including improved storage drivers, allowing the 2.4 kernel to work with PATA and SATA controllers in some newer chipsets.

The development of 2.6.27 moves forward; currently still at [2.6.27-rc5](http://thread.gmane.org/gmane.linux.kernel/727396), a sixth release candidate is expected soon. It has been suggested that 2.6.27 will be released in late September or early October, but Torvalds has not set a date; the [current list of issues introduced since 2.6.26](http://thread.gmane.org/gmane.linux.kernel.kernel-testers/1355) still includes 33 unresolved problems.

In the [middle of August](../site/news/item/Kernel-Log-New-stable-and-pre-release-kernels-Ubuntu-8-10-with-2-6-27-737021.html "Kernel Log: New stable and pre-release kernels, Ubuntu 8.10 with 2.6.27? â 25 August 2008, 11:32"), Torvalds had asked developers to concentrate on fixing bugs after the end of the merge window rather than sending in more patches for integration which could introduce more problems. Torvalds has highlighted this in recent weeks in his responses to other requests for patch integration ([1](http://thread.gmane.org/gmane.comp.video.dri.devel/31636/focus%3D31637),[2](http://thread.gmane.org/gmane.linux.network/104943/focus%3D104944),[3](http://thread.gmane.org/gmane.linux.network/104276/focus%3D730392)) and reprimanded the respective managers. Some kernel developers queried the existence of a new policy; Torvalds finally explaining that the current policy had been in place for some time but in practice had not been strictly implemented. Torvalds explained in different mails([1](http://thread.gmane.org/gmane.linux.network/104943/focus%3D104951),[2](http://thread.gmane.org/gmane.linux.network/104943/focus%3D104945)) what he thought the policy should be.

------------------------------------------------------------------------

After Mesa's developers published [Mesa 7.1](http://mesa3d.sourceforge.net/relnotes-7.1.html) at the end of August, X.org's developers were able to release [X-Server 1.5](http://lists.freedesktop.org/archives/xorg-announce/2008-September/000640.html); depending on your point of view, it's either six months or a year late. The new X server is a central part of X.org 7.4 which is expected in the next week.

X.org 7.4 drivers have also been updated by package administrators; the Intel driver is at [version 2.4.2](http://lists.freedesktop.org/archives/xorg-announce/2008-August/000645.html) and the X driver for VMWare guests is at [version 10.16.5](http://lists.freedesktop.org/archives/xorg-announce/2008-September/000647.html). [Version 2.1.11 of the open source Nvidia driver, nv](http://lists.freedesktop.org/archives/xorg-announce/2008-August/000635.html) added support for some new NVidia GPUs, but contained a bug which was then fixed in [version 2.1.12](http://lists.freedesktop.org/archives/xorg-announce/2008-August/000636.html). The proprietary AMD Catalyst drivers, known as fglrx, are not compatible with X-Server 1.5, along with drivers for older Nvidia graphics cards with version numbers 71.86.xx and 96.43.xx. This problem was noticed in May by users of Fedora 9, which uses a preliminary version of X-Server 1.5.

------------------------------------------------------------------------

Intel developer Keith Packard has taken on the role of release manager for X Server 1.6, after the long delays in completing X Server 1.5 was slowed by Mesa delays, and he is already planning to publish 1.6 in a few months. Present plans include the DRI2 infrastructure, RandR 1.3 and a revised input framework according to a report on [Phoronix](http://www.phoronix.com/) about the X Developer Summit 2008. X.org 7.5 would arrive after the next major X server revision.

**In Brief**

- Independently of X.org, Nvidia [released a beta version 177.70](http://www.nvnews.net/vbulletin/showthread.php?t=118602) of their proprietary Nvidia graphics driver for [x86-32](ftp://download.nvidia.com/XFree86/Linux-x86/177.70/) and [x86-64](ftp://download.nvidia.com/XFree86/Linux-x86_64/177.70/) systems.

<!-- -->

- Jeremy Fitzhardinge [presented patches for review](http://thread.gmane.org/gmane.linux.kernel/730867) to the Linux Kernel Mailing List that are the basis for Linux operating as a privileged Xen domain (Dom0).

<!-- -->

- 17 drivers for infrared devices from [Lirc](http://www.lirc.org/) that have lived outside the main kernel branch have [been submitted for inclusion in the main branch by Red Hat developer Jarod Wilson.\[/li](http://thread.gmane.org/gmane.linux.kernel/730867)

<!-- -->

- Dave Arlie [proposed a new model for the DRM development process](http://thread.gmane.org/gmane.comp.video.dri.devel/31693) to make the developers work easier and optimise the flow of patches between DRM development and the main development branch.

<!-- -->

- After [Git 1.6.0](http://thread.gmane.org/gmane.comp.version-control.git/92666) removed commands in the form of "git-foo" which upset some users, Git developers are holding a [user survey](http://thread.gmane.org/gmane.comp.version-control.git/94511) to obtain feedback.

<!-- -->

- Harold Welte published a [mini FAQ](http://laforge.gnumonks.org/weblog/2008/09/01/) on the [recently released](../site/news/item/VIA-open-source-Xorg-display-driver-released-737119.html "VIA open source Xorg display driver released â 01 September 2008, 10:31") open source VIA graphics drivers. It explains that VIA with to work with existing developer communities in incorporating this code and code from existing open source VIA drivers, Chrome and Unichrome, in future X.org releases.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: New stable and pre-release kernels, Ubuntu 8.10 with 2.6.27?](../site/news/item/Kernel-Log-New-stable-and-pre-release-kernels-Ubuntu-8-10-with-2-6-27-737021.html "Kernel Log: New stable and pre-release kernels, Ubuntu 8.10 with 2.6.27? â 25 August 2008, 11:32")
- [Kernel Log: New video drivers for AMD, Intel, Nvidia and VIA hardware](../site/news/item/Kernel-Log-New-video-drivers-for-AMD-Intel-Nvidia-and-VIA-hardware-736997.html "Kernel Log: New video drivers for AMD, Intel, Nvidia and VIA hardware â 22 August 2008, 11:59")
- [Kernel Log: Kernel development explained, new Synaptics driver, Linux 2.6.27-rc3 published](../site/news/item/Kernel-Log-Kernel-development-explained-new-Synaptics-driver-Linux-2-6-27-rc3-published-736911.html "Kernel Log: Kernel development explained, new Synaptics driver, Linux 2.6.27-rc3 published â 15 August 2008, 11:13")
- [Kernel Log: Ath9k driver for Atheros Wifi in 2.6.27; reading material and videos for Linux experts](../site/news/item/Kernel-Log-Ath9k-driver-for-Atheros-Wifi-in-2-6-27-reading-material-and-videos-for-Linux-experts-736829.html "Kernel Log: Ath9k driver for Atheros Wifi in 2.6.27; reading material and videos for Linux experts â 11 August 2008, 11:36")
- [Kernel Log: Btrfs 0.16 released, new stable kernels released, Wifi drivers for 2.6.27 merged](../site/news/item/Kernel-Log-Btrfs-0-16-released-new-stable-kernels-released-Wifi-drivers-for-2-6-27-merged-736815.html "Kernel Log: Btrfs 0.16 released, new stable kernels released, Wifi drivers for 2.6.27 merged â 08 August 2008, 14:32")
- [Kernel Log: New Stable kernel, DRI2 postponed, Xgl removed from X.org](../site/news/item/Kernel-Log-New-Stable-kernel-DRI2-postponed-Xgl-removed-from-X-org-736743.html "Kernel Log: New Stable kernel, DRI2 postponed, Xgl removed from X.org â 05 August 2008, 10:31")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
