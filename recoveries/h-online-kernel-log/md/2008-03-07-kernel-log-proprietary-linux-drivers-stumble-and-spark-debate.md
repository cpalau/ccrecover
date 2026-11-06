---
title: "Kernel log: Proprietary Linux drivers stumble and spark debate"
date: 2008-03-07
author: "Terry Relph-Knight"
source: http://www.h-online.com/open/news/item/Kernel-log-Proprietary-Linux-drivers-stumble-and-spark-debate-734409.html
pages: 1
---

# Kernel log: Proprietary Linux drivers stumble and spark debate

**Terry Relph-Knight**

![](../site/imgs/43/3/6/1/1/8/4/93e8ea3d0acdf147.jpg) Linux kernel 2.6.25 testers have encountered various problems with proprietary drivers. The kernel modules of the Nvidia graphics driver, for example, were temporarily unavailable because kernel developers [no longer exported](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3abf024d2abb79614d8c4cb25a70d5596f77d0ad) the `init_mm` interface. When asked whether this [decision could be reversed](http://thread.gmane.org/gmane.linux.kernel/646638), one developer showed [little inclination to co-operate](http://thread.gmane.org/gmane.linux.kernel/646638/focus%3D647170). He later even added another message [clearly criticising Nvidia](http://thread.gmane.org/gmane.linux.kernel/646638/focus%3D647961). The changes were [subsequently reversed in the development branch](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=757265b8c57bb8fd91785d3d1a87fb483c86c9c2) regardless. But this is only a temporary measure, as `init_mm` is set to disappear again with Linux 2.6.26 in a few weeks' time; this arrangement is designed to give the developers of external kernel modules – VirtualBox was mentioned – time to adjust their code.

Ndiswrapper currently also struggles with the test versions of 2.6.25, because the kernel marks itself as tainted when loading Ndiswrapper, which prevents Ndiswrapper from accessing interfaces exclusive to GPL2 compatible drivers. At the time of the test version release it seemed as if developers would quickly reverse this change.

However, this didn't happen. When the [respective patch](http://thread.gmane.org/gmane.linux.kernel/647537) was sent to the Linux Kernel Mailing List (LKML) at the end of last week, [Linus Torvalds severely criticised the patch](http://thread.gmane.org/gmane.linux.kernel/647537/focus%3D647567). "*I'm not seeing why ndiswrapper should be treated separately. If it loads non-GPL modules, it shouldn't be able to use `GPLONLY` symbols.*". He later added that Ndiswrapper itself, wasn't GPL compatible. In the course of the [lengthy discussion](http://thread.gmane.org/gmane.linux.kernel/647537) he explained these and other arguments against the change, in more detail.

The discussion also mentioned the change to the USB API proposed for 2.6.25. With this change, USB developers tried to clarify that only USB drivers under GPL2, or a compatible licence, are allowed to use the central functionality of the kernel's internal USB driver API. However, Ndiswrapper is said to bypass this rule by claiming to be GPL compatible, but subsequently loading incompatible code - the NDIS drivers written for Windows. This code, it was discussed, then indirectly uses the USB interfaces enabled via `EXPORT_SYMBOL_GPL`.

Whether this is legal would probably cause controversy even among lawyers familiar with software licensing, and could only be clarified in court. Things don't usually go this far, which leaves the focus on what kernel developers will do. If every thing stays the way it is, Ndiswrapper is denied access to interfaces enabled via `EXPORT_SYMBOL_GPL` - as this includes the central USB interfaces in 2.6.25, Ndiswrapper will not function properly at least with USB networking hardware under the "official" Linux 2.6.25.

### Kernel log in brief

:

- [Current plans](http://thread.gmane.org/gmane.comp.freedesktop.xorg/26419) schedule the release of X.org 7.4 together with Fedora 9 for the end of April.
- Linux developers [are discussing](http://thread.gmane.org/gmane.linux.kernel.wireless.general/11908) the Central Regulatory Domain Agent (CRDA), a userspace program intended to adjust WiFi hardware to comply with the respective regional operating guidelines and legislation.
- The developers of [BadRAM](http://rick.vanrein.org/linux/badram/) are trying to [convince kernel hackers to integrate](http://thread.gmane.org/gmane.linux.kernel/648458) these long established Linux extension into the official kernel. BadRAM can be used to instruct the kernel not to use faulty areas in memory modules – for example in order to continue using a notebook which has faulty memory soldered to its mainboard.
- The Hdparm program is now available in versions 8.5 and 8.6 which fix several critical security holes in the previous 8.x versions.
- Kernel developer Oliver Pinter, who has not made a big appearance so far, plans to maintain Linux version 2.6.22 within the ["op" kernel series](http://thread.gmane.org/gmane.linux.kernel/646261). This is following the recent and probably last release (2.6.22.19) by the admins of the stable kernel series 2.6.22.

([trk](mailto:trk@h-online.com "Terry Relph-Knight"))
