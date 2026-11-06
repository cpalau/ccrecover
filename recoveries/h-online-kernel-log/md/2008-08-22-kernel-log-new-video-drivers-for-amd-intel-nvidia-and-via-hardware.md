---
title: "Kernel Log: New video drivers for AMD, Intel, Nvidia and VIA hardware"
date: 2008-08-22
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-New-video-drivers-for-AMD-Intel-Nvidia-and-VIA-hardware-736997.html
pages: 1
---

# Kernel Log: New video drivers for AMD, Intel, Nvidia and VIA hardware

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/3/7/7/0/93e8ea3d0acdf147.jpg) The monthly release of AMD's Catalyst Linux drivers reaches [Version 8.8](http://www2.ati.com/drivers/linux/catalyst_88_linux.html) and, after previous versions had hardly anything new, there's now [an abundance of new features](http://www2.ati.com/drivers/linux/catalyst_88_linux.html#194695) in the 8.52 fglrx driver. The new driver supports the [CrossFireX](http://www2.ati.com/drivers/linux/catalyst_88_linux.html#207896) configurations on the ATI Radeon 4800, and overclockers can now make use of [Overdrive](http://www2.ati.com/drivers/linux/catalyst_88_linux.html#212442) for extracting more power out of their graphics hardware. [Adaptive Anti-aliasing](http://www2.ati.com/drivers/linux/catalyst_88_linux.html#207899) support has been enabled to improve image quality and [ATI Multiview](http://www2.ati.com/drivers/linux/catalyst_88_linux.html#212709) has been incorporated to support multiple displays on systems with a range of FireGL cards.

[Fedora 9](../site/open/features/A-first-impression-of-Fedora-9-746490.html "A first impression of Fedora 9 – 27 May 2008, 11:01") and beta versions of some distributions including X.org 7.4, X Server 1.5 and AMD's proprietary driver are not compatible with them, but there are two ready alternatives in the open source [radeon](http://wiki.x.org/wiki/radeon) and [radeonhd](http://wiki.x.org/wiki/radeonhd) drivers. Although some of the fglrx driver functions are not supported, these open source drivers should satisfy some users.

Nvidia released beta versions of their proprietary Linux driver for GeForce cards, version [177.67](http://us.download.nvidia.com/XFree86/Linux-x86_64/177.67/README/index.html) for [x86-32](http://www.nvidia.com/object/linux_display_ia32_177.67.html) and [x86-64](http://www.nvidia.com/object/linux_display_amd64_177.67.html). Shortly after this, a [177.68](ftp://download.nvidia.com/XFree86/Linux-x86/177.68/README/index.html) driver for [x86-32](ftp://download.nvidia.com/XFree86/Linux-x86/177.68/) and [x86-64](ftp://download.nvidia.com/XFree86/Linux-x86_64/177.68/) appeared on the Nvidia FTP site. In the semi-official NVzone forum, an Nvidia employee [said](http://www.nvnews.net/vbulletin/showthread.php?t=118073#12) that the 177.67 driver should address 2D performance problems, which have been especially noticeable when using Firefox 3 and KDE 4, but added that some of the improvements depended on new/experimental features which were not enabled by default and pointed interested users at a [tweaking guide](http://www.nvnews.net/vbulletin/showthread.php?t=118088) for those features.

The X.org project developers published some new graphics drivers. [Version 2.4.1](http://lists.freedesktop.org/archives/xorg-announce/2008-August/000631.html) of the graphics driver for Intel chipsets provides minor bug fixes and improvements. Parallel to this, the developers of the next generation driver for Intel chipsets reported [some progress](http://anholt.livejournal.com/38717.html). Other news came from the [open chrome project](http://www.openchrome.org/) whose developer published [version 0.2.903 of the driver](http://lists.freedesktop.org/archives/xorg/2008-August/038122.html) with support for newer VIA graphic chipsets, while the developers of drivers for the graphics core of the AMD Geode [released a new version](http://lists.freedesktop.org/archives/xorg-announce/2008-August/000633.html).

The Mesa developers published [Mesa 7.0.4](http://marc.info/?l=mesa3d-announce&m=121890604311356&w=2) and [Mesa 7.1rc4](http://marc.info/?l=mesa3d-announce&m=121890362108753&w=2). In the announcement, Brian Paul said he hopes to have 7.1 published soon. X developers are waiting on this release as parts of X.org 7.4 are already dependant on the new Mesa 7.1, which is why the next X.org version will only be released after Mesa 7.1.

**In Brief**

- The Alsa developers published [version 1.0.18rc1](http://www.alsa-project.org/main/index.php/Main_Page) of their kernel sound driver. The [changelog](http://www.alsa-project.org/main/index.php/Changes_v1.0.17a_v1.0.18rc1) lists all the updates. The kernel developers usually revise audio drivers at the start of the next development cycle in the main developement branch, so this driver should eventually appear in Kernel version 2.6.28.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: Kernel development explained, new Synaptics driver, Linux 2.6.27-rc3 published](../site/news/item/Kernel-Log-Kernel-development-explained-new-Synaptics-driver-Linux-2-6-27-rc3-published-736911.html "Kernel Log: Kernel development explained, new Synaptics driver, Linux 2.6.27-rc3 published – 15 August 2008, 11:13")
- [Kernel Log: Ath9k driver for Atheros Wifi in 2.6.27; reading material and videos for Linux experts](../site/news/item/Kernel-Log-Ath9k-driver-for-Atheros-Wifi-in-2-6-27-reading-material-and-videos-for-Linux-experts-736829.html "Kernel Log: Ath9k driver for Atheros Wifi in 2.6.27; reading material and videos for Linux experts – 11 August 2008, 11:36")
- [Kernel Log: Btrfs 0.16 released, new stable kernels released, Wifi drivers for 2.6.27 merged](../site/news/item/Kernel-Log-Btrfs-0-16-released-new-stable-kernels-released-Wifi-drivers-for-2-6-27-merged-736815.html "Kernel Log: Btrfs 0.16 released, new stable kernels released, Wifi drivers for 2.6.27 merged – 08 August 2008, 14:32")
- [Kernel Log: New Stable kernel, DRI2 postponed, Xgl removed from X.org](../site/news/item/Kernel-Log-New-Stable-kernel-DRI2-postponed-Xgl-removed-from-X-org-736743.html "Kernel Log: New Stable kernel, DRI2 postponed, Xgl removed from X.org – 05 August 2008, 10:31")
- [Kernel Log: New Nvidia drivers are still slow, Linux 2.6.26.1 soon](../site/news/item/Kernel-Log-New-Nvidia-drivers-are-still-slow-Linux-2-6-26-1-soon-736723.html "Kernel Log: New Nvidia drivers are still slow, Linux 2.6.26.1 soon – 04 August 2008, 09:07")
- [Kernel Log: Tux3 file system announced, X.org updates](../site/news/item/Kernel-Log-Tux3-file-system-announced-X-org-updates-736707.html "Kernel Log : Tux3 file system announced, X.org updates – 01 August 2008, 09:17")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
