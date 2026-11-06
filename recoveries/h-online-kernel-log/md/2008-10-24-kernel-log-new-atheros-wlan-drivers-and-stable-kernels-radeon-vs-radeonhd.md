---
title: "Kernel Log: New Atheros WLAN drivers and stable kernels, radeon vs. radeonhd"
date: 2008-10-24
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-New-Atheros-WLAN-drivers-and-stable-kernels-radeon-vs-radeonhd-737773.html
pages: 1
---

# Kernel Log: New Atheros WLAN drivers and stable kernels, radeon vs. radeonhd

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/4/5/4/4/93e8ea3d0acdf147.jpg) Linux Wi-Fi specialist and developer LuisÂ R. Rodriguez, who has worked for Atheros for several months now, has announced [the release of the Otus driver](http://thread.gmane.org/gmane.linux.kernel/747372) under the [ISC](http://www.opensource.org/licenses/isc-license.txt) open source licence. This driver for Atheros UB81, UB82 and UB83 802.11n USB Wi-Fi chips has been released to have it integrated into the main development branch of Linux as soon as possible. That this approach can work very well was already demonstrated by [ath9k](../site/news/item/Kernel-Log-Ath9k-driver-for-Atheros-Wifi-in-2-6-27-reading-material-and-videos-for-Linux-experts-736829.html "Kernel Log: Ath9k driver for Atheros Wifi in 2.6.27; reading material and videos for Linux experts â 11 August 2008, 11:36"). The kernel hackers integrated it into the main development branch that recently produced [Linux 2.6.27](../site/open/features/Kernel-Log-Linux-2-6-27-Released-746496.html "Kernel Log: Linux 2.6.27 Released â 10 October 2008, 08:38") only a few weeks after its release in July. As the next versions of Fedora, OpenSuse and Ubuntu will come with this kernel version, all three will also include ath9k.

Greg Kroah-Hartman has already [announced](http://thread.gmane.org/gmane.linux.kernel/747372/focus%3D22601) that he will incorporate the driver into the [linux-staging tree](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-3-Dodgy-drivers-737747.html "Kernel Log: What's coming in 2.6.28 - Part 3: Dodgy drivers â 22 October 2008, 09:29"). Before it becomes a regular Linux feature, the driver will need to undergo quite a bit of modification. For example, the driver contains code for supporting previous kernel versions, something the kernel hackers don't like to see in drivers that have been integrated into Linux.

Rodriguez is also busying himself in other areas: Only recently, he started [a discussion about a process for improving the support of system power saving techniques](http://thread.gmane.org/gmane.linux.kernel.wireless.general/22377) and sleep states in the Linux Wi-Fi stack. The [Wi-Fi developers' todo-list](http://wireless.kernel.org/en/developers/todo-list#powersaving) already contains several items concerning these topics; Wi-Fi subsystem maintainer JohnÂ W. Linville already pointed out in his [OLS presentation](../site/open/features/In-depth-insights-Linux-information-from-the-OLS-746494.html "In-depth insights – Linux information from the OLS â 31 July 2008, 12:43") this summer that the use of power saving mechanisms is the biggest problem in Linux Wi-Fi support.

**New 2.6.27 varieties**

While last week's [Linux 2.6.27.1 disabled the code which probably caused the e1000e problem](../site/news/item/Kernel-Log-new-Catalyst-drivers-2-6-27-1-resolves-cause-of-e1000e-problem-737701.html "Kernel Log: new Catalyst drivers, 2.6.27.1 resolves cause of e1000e problem â 18 October 2008, 08:02"), [version 2.6.27.2](http://thread.gmane.org/gmane.linux.kernel/746190), which was published two days later, includes numerous further corrections for [kernel version 2.6.27](../site/open/features/Kernel-Log-Linux-2-6-27-Released-746496.html "Kernel Log: Linux 2.6.27 Released â 10 October 2008, 08:38") which was released two weeks ago.

But that is not all â€“ the preparatory phase for versions [2.6.25.19](http://thread.gmane.org/gmane.linux.kernel/746236), [2.6.26.7](http://thread.gmane.org/gmane.linux.kernel/746211) and [2.6.27.3](http://thread.gmane.org/gmane.linux.kernel/746191) of Linux began straight after the release of 2.6.27.2. The maintainers of the stable kernel series gave other kernel developers a few days to comment on the proposed changes; the three new kernels should be released shortly. Those who use self-compiled kernels on systems with recent Intel graphics chipset (G33 and newer) are strongly advised to update to these versions as they contain [a correction](http://thread.gmane.org/gmane.linux.kernel/746250) that fixes the [CVE-2008-3831](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2008-3831) security hole which affects these mainboard chipsets. Some of the Linux distributors have already released new kernels in which this problem has also been solved.

The users of series 2.4 kernels should also consider updating: [Linux version 2.4.36.8](http://www.uwsg.indiana.edu/hypermail/linux/kernel/0810.2/1476.html) corrects various flaws and three "medium local security issues".

**Next round: radeon vs. radeonhd**

X.org developer [Daniel Stone recently removed the radeonhd driver](http://thread.gmane.org/gmane.comp.freedesktop.xorg.cvs/10962/) from the list of official X.org modules, saying "Drop radeonhd \[...\] We already have a Radeon driver." The driver he refers to is part of the ati driver package ([radeon](http://wiki.x.org/wiki/radeon)). Like the radeonhd driver, it supports a large variety of the current Radeon graphics cards and offers a similar range of features, although the two drivers did take turns to be the first to support a new function or graphics card in the past. In addition, both drivers contain fragments of each other's code, and the developers of the two drivers actively co-operated to integrate [Mesa 3D](http://www.mesa3d.org/), which is required for 3D support; however, only the older radeon driver supports seasoned Radeon graphics cards.

Novell employee and radeonhd developer [Luc Verhaegen criticised Stone's decision](http://thread.gmane.org/gmane.comp.freedesktop.xorg.cvs/10962/focus%3D33044). This has triggered a discussion in which several well-known Linux and X.org developers have defended the removal of the driver, pointing out the disadvantages caused by simultaneously developing several drivers for the same hardware.

Whether the removal is final remains to be seen. Also unknown are the long term consequences for users, distributors and radeonhd programmers. If things remain as they are, however, radeon stands a slightly better chance to become the standard driver for Radeon graphics cards.

**In brief**

- The organisers of the [Linux Kongress 2008](../site/open/features/Linux-Kongress-2008-746416.html "Linux Kongress 2008 â 17 October 2008, 11:08") have recently made many presentation slides of this convention which attracts many well-known kernel hackers as visitors or presenters [available](http://www.linux-kongress.org/2008/program.html#2008/10/09) on their home page. Some of the presentations were already discussed in our coverage; Since then, Lars Ellenberg of [Linbit](http://www.linbit.com) has also released [text versions](http://www.drbd.org/fileadmin/drbd/publications/drbd9.linux-kongress.2008.pdf)![PDF](../site/icons/file-pdf.gif "PDF document") of his presentation titled "DRBD 9 & Device-Mapper â€“ Linux Block Level Storage Replication".

<!-- -->

- Ingo Molnar has [started](http://thread.gmane.org/gmane.linux.kernel/745892) a new development branch called "fix all build warnings, on all configs". He intends use the branch for collecting patches which remove the compiler warnings during kernel compilation and for preparing these patches for integration into the kernel.

<!-- -->

- The Git developers have [released](http://thread.gmane.org/gmane.comp.version-control.git/98828) version 1.6.0.3 of the Git source code management software which is used for kernel development among other things.

<!-- -->

- Having developed the [squashfs](http://squashfs.sourceforge.net/) filesystem, used in the live media of many distributions, to maturity independent of the official kernel, the filesystem's developers are now [actively promoting its integration](http://thread.gmane.org/gmane.linux.kernel.embedded/1178/) into the official Linux kernel.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: What's coming in 2.6.28 - Part 3: Dodgy drivers](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-3-Dodgy-drivers-737747.html "Kernel Log: What's coming in 2.6.28 - Part 3: Dodgy drivers â 22 October 2008, 09:29")
- [Kernel Log: More than 10 million lines of Linux source files](../site/news/item/Kernel-Log-More-than-10-million-lines-of-Linux-source-files-737731.html "Kernel Log: More than 10 million lines of Linux source files â 21 October 2008, 14:50")
- [Kernel Log: Coming in 2.6.28 - Part 2: network infrastructure and network drivers](../site/news/item/Kernel-Log-Coming-in-2-6-28-Part-2-network-infrastructure-and-network-drivers-737711.html "Kernel Log: Coming in 2.6.28 - Part 2: network infrastructure and network drivers â 20 October 2008, 09:39")
- [Kernel Log: Coming in 2.6.28 - Part 1: ATA support and block layer](../site/news/item/Kernel-Log-Coming-in-2-6-28-Part-1-ATA-support-and-block-layer-737699.html "Kernel Log: Coming in 2.6.28 - Part 1: ATA support and block layer â 19 October 2008, 08:02")
- [Kernel Log: new Catalyst drivers, 2.6.27.1 resolves cause of e1000e problem](../site/news/item/Kernel-Log-new-Catalyst-drivers-2-6-27-1-resolves-cause-of-e1000e-problem-737701.html "Kernel Log: new Catalyst drivers, 2.6.27.1 resolves cause of e1000e problem â 18 October 2008, 08:02")
- [Kernel Log: Ext4 completes development phase as interim step to btrfs](../site/news/item/Kernel-Log-Ext4-completes-development-phase-as-interim-step-to-btrfs-737697.html "Kernel Log: Ext4 completes development phase as interim step to btrfs â 17 October 2008, 09:52")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
