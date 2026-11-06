---
title: "Kernel Log: main development phase for 2.6.29 ends, new X.org drivers"
date: 2009-01-12
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-main-development-phase-for-2-6-29-ends-new-X-org-drivers-739633.html
pages: 1
---

# Kernel Log: main development phase for 2.6.29 ends, new X.org drivers

**Dj Walker-Morgan**

With the release [of 2.6.29-rc1](http://thread.gmane.org/gmane.linux.kernel/778565) on Saturday night, Linus Torvalds has closed the 2.6.29 merge window and brought to a close the development phase, during which the major new features for the next version of Linux are adopted. All significant changes in 2.6.29 should now be in the Linux source code management system, including new features previously discussed on heise open such as [WiMAX](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-2-WiMAX-739621.html "Kernel Log: What's new in 2.6.29 - Part 2: WiMAX – 12 January 2009, 10:19"), [access point](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-1-Dodgy-Wifi-drivers-and-AP-support-739619.html "Kernel Log: What's new in 2.6.29 - Part 1: Dodgy Wifi drivers and AP support – 11 January 2009, 16:08") support and the [Btrfs and Squashfs](../site/news/item/Btrfs-and-Squashfs-merged-into-Linux-kernel-739613.html "Btrfs and Squashfs merged into Linux kernel – 10 January 2009, 15:44") file systems.

These changes are just some of the more conspicuous changes adopted by the kernel hackers for 2.6.29. Support has been added for kernel-based mode setting on Intel graphics hardware and improvements have been made to the Graphics Execution Manager (GEM), which was integrated [with 2.6.28](../site/open/features/Kernel-Log-Higher-and-Further-The-innovations-of-Linux-2-6-28-746519.html "Kernel Log: Higher and Further, The innovations of Linux 2.6.28 – 23 December 2008, 15:55"). The SCSI subsystem now supports Fibre Channel over Ethernet (FCoE) and there are fixes to, and new functions in, the eCryptfs, Ext4, OCFS2 and XFS file systems. There are also numerous new and revised drivers, including new or revised audio drivers from the Alsa project and over 600 changes to the V4L/DVB drivers. These are now joined by various, in some cases very large, staging drivers, such as the [Comedi](http://www.comedi.org/) framework, or support for Google's Android. heise open's Kernel Log will carry detailed reports on these and other changes over the next few weeks as part of our "What's coming in 2.6.29" series.

The realtime defragmenter (*online ext4 defragmentation*) has not made it into 2.6.29 – Theodore Tso [explains why](http://thread.gmane.org/gmane.linux.kernel/778756/focus%3D778944) on LKML. Also left out, for the time being, are support for operation as a primary Xen domain (Dom0) and [compression of the kernel image with bzip2/lzma](http://thread.gmane.org/gmane.linux.kernel/778572). It [looks like it could also be a while](http://airlied.livejournal.com/64271.html) before support for kernel-based mode setting with AMD hardware meets the kernel development team's quality standards.

**All about X.org**

AMD developer Alex Deucher has released [version 6.10](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/517) of the xf86-video-ati driver package, usually known simply as ati or radeon. It includes support for the RV710 (Radeon HD 4300/HD 4500) and RV730 (Radeon HD 4600) Radeon chips. The new version also [reduces](http://www.botchco.com/agd5f/?p=33) tearing during video playback and supports Bicubic Xv scaling on r3xx/r4xx/r5xx/rs690 Radeon chips. The developer discusses further changes [on his blog](http://www.botchco.com/agd5f/?p=34). Matthias Hopf has now released the AtomBIOS disassembler previously used for programming the alternative Radeon graphics driver radeonhd. He describes some of the background to the tool [on his blog](http://emmes.livejournal.com/3678.html).

The X.org developers have also [released](http://article.gmane.org/gmane.comp.freedesktop.xorg.announce/520) version 1.4.0 of the xf86-input-mouse mouse driver. This driver deals with many of the tasks previously dealt with by X server, and the code responsible for this has been removed from X server – with the result that in X server 1.6, currently under development, users will, unless their systems use Evdev, need at least version 1.4.0 of xf86-input-mouse.

**In Brief:**

- Following LWN.net's occasional publication of analysis of which kernel developers have, for instance, introduced the most or the largest changes into a kernel version (e.g. [1](http://lwn.net/Articles/312074/), [2](http://lwn.net/Articles/306690/), [3](http://lwn.net/Articles/302061/)), [Wang Chen](http://thread.gmane.org/gmane.linux.kernel/775581/) has been trying his hand at a similar set of [online](http://www.remword.com/kps_result/) statistics.

<!-- -->

- SELinux hacker James Morris has announced the creation of the [Kernel Security Wiki](http://security.wiki.kernel.org/index.php/Main_Page) on [his blog](http://james-morris.livejournal.com/37748.html), where he has also recently [summarised](http://james-morris.livejournal.com/37583.html) all the most significant security-related changes in Linux 2.6.28.

<!-- -->

- [As part of the discussion on the adoption of Squashfs](http://thread.gmane.org/gmane.linux.file-systems/28733/focus%3D28958), Greg Kroah-Hartman has declared that he will in future accept file systems into the staging directory, as long as they do not require changes in other parts of the kernel.

<!-- -->

- Daniel Phillips is continuing to work on Tux3 and is keeping the developer community updated on new features or internal matters in his "Tux3 Report" – a [recent e-mail](http://thread.gmane.org/gmane.comp.file-systems.tux3/52/focus%3D590) to LKML, for example, elucidates the current structure of the file system.

<!-- -->

- The kernel development team are planning to hold a "[Linux Storage and Filesystem Summit 2009](http://thread.gmane.org/gmane.linux.ide/37194)" in San Francisco in early April.

<!-- -->

- A group of developers are working on [open source firmware](http://thread.gmane.org/gmane.linux.kernel.wireless.general/26670) for some of the Broadcom WLAN chips supported under Linux by the b43 driver; this firmware does not, however, appear to work for all testers. Marvell has made WLAN firmware for the GSPI-88W8686 [available to download](http://thread.gmane.org/gmane.linux.kernel.wireless.general/26469/), but has not released the source code.

<!-- -->

- As [reported elsewhere](../site/news/item/New-Nvidia-driver-for-Linux-739609.html "New Nvidia driver for Linux – 09 January 2009, 16:09"), Nvidia has released version 180.22 of its proprietary graphics driver for [x86-32](http://www.nvidia.com/object/linux_display_ia32_180.22.html) and [x86-64](http://www.nvidia.com/object/linux_display_amd64_180.22.html) Linux.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: What's new in 2.6.29 - Part 2: WiMax](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-2-WiMAX-739621.html "Kernel Log: What's new in 2.6.29 - Part 2: WiMAX – 12 January 2009, 10:19")
- [Kernel Log: What's new in 2.6.29 - Part 1: Dodgy Wifi drivers and AP support](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-1-Dodgy-Wifi-drivers-and-AP-support-739619.html "Kernel Log: What's new in 2.6.29 - Part 1: Dodgy Wifi drivers and AP support – 11 January 2009, 16:08")
- [Kernel Log: 2.6.29 development kicks off, improved 3D support](../site/news/item/Kernel-Log-2-6-29-development-kicks-off-improved-3D-support-739551.html "Kernel Log: 2.6.29 development kicks off, improved 3D support – 05 January 2009, 17:29")
- [Kernel Log: Higher and Further, The innovations of Linux 2.6.28](../site/open/features/Kernel-Log-Higher-and-Further-The-innovations-of-Linux-2-6-28-746519.html "Kernel Log: Higher and Further, The innovations of Linux 2.6.28 – 23 December 2008, 15:55")
- [Kernel Log: What's coming in 2.6.28 - Part 9: Fastboot and other remainders](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-9-Fastboot-and-other-remainders-739431.html "Kernel Log: What's coming in 2.6.28 - Part 9: Fastboot and other remainders – 19 December 2008, 12:45")
- [Kernel Log: What's coming in 2.6.28 - Part 8: Video4Linux/DVB, (Wireless) USB, hardware monitoring, and input devices](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-8-Video4Linux-DVB-Wireless-USB-hardware-monitoring-and-input-devices-739405.html "Kernel Log: What's coming in 2.6.28 - Part 8: Video4Linux/DVB, (Wireless) USB, hardware monitoring, and input devices – 18 December 2008, 08:16")
- [Kernel Log: What's coming in 2.6.28 - Part 7: architecture support, memory subsystem and virtualisation](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-7-architecture-support-memory-subsystem-and-virtualisation-739397.html "Kernel Log: What's coming in 2.6.28 - Part 7: architecture support, memory subsystem and virtualisation – 17 December 2008, 10:35")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
