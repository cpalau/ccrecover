---
title: "Kernel Log: Kernel development explained, new Synaptics driver, Linux 2.6.27-rc3 published"
date: 2008-08-15
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-Kernel-development-explained-new-Synaptics-driver-Linux-2-6-27-rc3-published-736911.html
pages: 1
---

# Kernel Log: Kernel development explained, new Synaptics driver, Linux 2.6.27-rc3 published

**Dj Walker-Morgan**

As mentioned [earlier in the week](../site/news/item/Guide-to-participating-in-Linux-Kernel-Community-published-736881.html "Guide to participating in Linux Kernel Community published â 13 August 2008, 14:47"), the [Linux Foundation](http://www.linuxfoundation.org/) has published *[How to Participate in the Linux Community](http://ldn.linuxfoundation.org/book/how-participate-linux-community)* by Jon Corbet. Corbet explains the background to the kernel development process and has many tips on how to get into kernel development, avoid common errors in submitted code and how to cooperate with the kernel developers. The book should be very useful, not only for hobby developers, but for enterprises and hardware companies who are not familiar with how the Linux kernel is developed. The publication seems more than overdue; in the past, hardware manufacturers releasing driver code, for example, have had trouble interacting with the open source development process.

Attentive Kernel Log readers will recall the book was actually released [at the end of July](../site/news/item/Kernel-Log-New-Stable-kernel-DRI2-postponed-Xgl-removed-from-X-org-736743.html "Kernel Log: New Stable kernel, DRI2 postponed, Xgl removed from X.org â 05 August 2008, 10:31") by Jon Corbet, its author and director of LWN.net, as a patch to the Linux Kernel Mailing List, LKML, so that other kernel developers could read it and submit suggestions for improvements. Corbet and the Linux Foundation are not alone in dealing with this topic; Andi Kleen presented *[On submitting kernel patches](http://ols.fedoraproject.org/OLS/Reprints-2008/kleen-reprint.pdf)* as one of the many presentations at the [Ottawa Linux Symposium 2008](../site/open/features/In-depth-insights-Linux-information-from-the-OLS-746494.html "In-depth insights – Linux information from the OLS â 31 July 2008, 12:43").

------------------------------------------------------------------------

Many notebooks use the X-input driver for the [synaptics and ALPS](http://web.telia.com/~u89404340/touchpad/) trackpads but the driver has not been [updated since 2006](http://web.telia.com/~u89404340/touchpad/files/changes.txt). Now Christopher Brill is managing the driver and has released [version 0.15.0](http://lists.freedesktop.org/archives/xorg-announce/2008-August/000629.html). This brings with it [numerous changes and bug fixes](http://lists.freedesktop.org/archives/xorg-announce/2008-August/000629.html). It is also the first version of the driver to be released under the MIT licence, the licence used by the [X.org project](http://www.x.org/wiki/); previous versions of the driver were GPL licensed.

------------------------------------------------------------------------

The constant flood of patches in the main development branch leading to the 2.6.27 kernel over the past few days seems to have come to a rest. Linus Torvalds has released [Linux 2.6.27-rc3](http://thread.gmane.org/gmane.linux.kernel/720448) and expressed the hope that many of the regressions from 2.6.26 have been resolved. Some minor changes were made though, such as the [removal](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=88d987d6db2a14b191f4eb21cc623dae31e28e9d) of the long-broken ISDN auerswald USB driver from the kernel whose duties are now managed by a libusb user space driver.

As well as the [previously mentioned](../site/news/item/Kernel-Log-Ath9k-driver-for-Atheros-Wifi-in-2-6-27-reading-material-and-videos-for-Linux-experts-736829.html "Kernel Log: Ath9k driver for Atheros Wifi in 2.6.27; reading material and videos for Linux experts â 11 August 2008, 11:36") ath9k driver for the Atheros Draft-n wifi chipsets, the [Ridiculous Count 3](http://article.gmane.org/gmane.linux.kernel/247735/match%3Dridiculous%2Bcount) release of 2.6.27 already has support of Intel's Ibex Peak I/O chip, expected to appear, in the third quarter of next year, as part of Intel's 'Nehalem' architure processors, currently codenamed Lynnfield and Havendale. Torvalds, writing on the Linux Kernel Mailing List, [suggested](http://thread.gmane.org/gmane.linux.kernel/718141/focus%3D721224) that the handling of page faults on the 'Nehalem' architecture was signifigantly improved over the Pentium 4 and catching up with AMD's handling.

------------------------------------------------------------------------

After the code to support the Centrino-2 Wifi chips in Intel's "Wireless Wifi Link 5000AGN" was [recently](../site/news/item/Kernel-Log-Btrfs-0-16-released-new-stable-kernels-released-Wifi-drivers-for-2-6-27-merged-736815.html "Kernel Log: Btrfs 0.16 released, new stable kernels released, Wifi drivers for 2.6.27 merged â 08 August 2008, 14:32") included in the main development branch, Intel has [officially announced](http://thread.gmane.org/gmane.linux.kernel.wireless.general/19436/) Linux support for the chips. It also plans to back-port the driver, named iwlagn, to older releases of the kernel. The driver does not work with the WIMAX features available in some of the chips. Intel developers are working with the [linuxwimax.org project](http://linuxwimax.org) which recently released a [1.2.5 version of the WIMAX stack](http://thread.gmane.org/gmane.linux.kernel.wireless.general/19443).

**In Brief**

- HP Developer Rick Jones has [announced](http://thread.gmane.org/gmane.linux.kernel/721240) [pcitop](http://pcitop.berlios.de/), a PCI bus utilisation analyser. Currently it only works with HP Integrity systems.
- Stefan Judge, responsible for managing the Firewire code of Linux, has [announced a new Wiki for Firewire](http://thread.gmane.org/gmane.linux.kernel.firewire.user/3409). The [new Wiki](http://ieee1394.wiki.kernel.org/) replaces [wiki.linux1394.org](http://wiki.linux1394.org/) which has been recently vandalised by spammers, and moves it under the kernel.org domain.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: Ath9k driver for Atheros Wifi in 2.6.27; reading material and videos for Linux experts](../site/news/item/Kernel-Log-Ath9k-driver-for-Atheros-Wifi-in-2-6-27-reading-material-and-videos-for-Linux-experts-736829.html "Kernel Log: Ath9k driver for Atheros Wifi in 2.6.27; reading material and videos for Linux experts â 11 August 2008, 11:36")
- [Kernel Log: Btrfs 0.16 released, new stable kernels released, Wifi drivers for 2.6.27 merged](../site/news/item/Kernel-Log-Btrfs-0-16-released-new-stable-kernels-released-Wifi-drivers-for-2-6-27-merged-736815.html "Kernel Log: Btrfs 0.16 released, new stable kernels released, Wifi drivers for 2.6.27 merged â 08 August 2008, 14:32")
- [Kernel Log: New Stable kernel, DRI2 postponed, Xgl removed from X.org](../site/news/item/Kernel-Log-New-Stable-kernel-DRI2-postponed-Xgl-removed-from-X-org-736743.html "Kernel Log: New Stable kernel, DRI2 postponed, Xgl removed from X.org â 05 August 2008, 10:31")
- [Kernel Log: New Nvidia drivers are still slow, Linux 2.6.26.1 soon](../site/news/item/Kernel-Log-New-Nvidia-drivers-are-still-slow-Linux-2-6-26-1-soon-736723.html "Kernel Log: New Nvidia drivers are still slow, Linux 2.6.26.1 soon â 04 August 2008, 09:07")
- [Kernel Log : Tux3 file system announced, X.org updates](../site/news/item/Kernel-Log-Tux3-file-system-announced-X-org-updates-736707.html "Kernel Log : Tux3 file system announced, X.org updates â 01 August 2008, 09:17")
- [Kernel Log: 2.6.25.13 corrects a vulnerability, problems with ACPI](../site/news/item/Kernel-log-2-6-25-13-corrects-a-vulnerability-problems-with-ACPI-736703.html "Kernel log: 2.6.25.13 corrects a vulnerability, problems with ACPI â 31 July 2008, 14:42")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
