---
title: "Kernel Log: New Nvidia drivers are still slow, Linux 2.6.26.1 soon"
date: 2008-08-04
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-New-Nvidia-drivers-are-still-slow-Linux-2-6-26-1-soon-736723.html
pages: 1
---

# Kernel Log: New Nvidia drivers are still slow, Linux 2.6.26.1 soon

*In Brief*

**Dj Walker-Morgan**

Nvidia has released new proprietary GeForce drivers; Version 173.14.12 of the drivers for [x86-32](http://www.nvidia.com/object/linux_display_ia32_173.14.12.html) and [x96-64](http://www.nvidia.com/object/linux_display_amd64_173.14.12.html) now support the GeForce 8600 GS while fixing bugs in OpenGL, SDL support and the configuration tool.

2D performance problems with the newer GeForce graphics cards, discussed in [many](http://www.nvnews.net/vbulletin/showthread.php?t=115916) [forums](http://www.phoronix.com/forums/showthread.php?t=11044) and [blogs](http://www.larsen-b.com/Article/290.html) are not addressed with this update. Some applications which use Cairo or newer QT versions can feel like they are running on a several year old PC, even when it is actually on a quick system. This is especially apparent when rendering complex web pages with Firefox 3 or using Compiz and KDE 4.

KDE 4 is so slow with Nvidia drivers that the desktop is not really suitabled for production use. The KDE Project notes the performance problems with Nvida cards in the [KDE 4.1 announcement](http://www.kde.org/announcements/4.1/). From reports of users and heise online readers, the weak desktop performance is noticable with the lower end of the GeForce series, the 8000 and 9000, bit is mitigated with higher end graphics cards in the GeForce range like the 8800 and 9800, due to their immense computing power.

A Nvidia employee [acknowledged](http://www.nvnews.net/vbulletin/showpost.php?p=1642162&postcount=42) the problem back in April on the semi-official Nvidia Linux forum. Until Nvida fix the problem, there are some ([1](http://www.nvnews.net/vbulletin/showpost.php?p=1704073&postcount=1),[2](http://techbase.kde.org/User%3ALemma/KDE4-NVIDIA)) tricks that can help performance. As an alternative, users could run the X.org VESA server or Nvidia's 177 beta drivers.

Greg Kroah-Hartman [will soon](http://thread.gmane.org/gmane.linux.kernel/714296) release Linux version 2.6.26.1. A large number of the 62 patches fix bugs in the two and a half week old [Linux 2.2.26 kernel](../site/news/item/AMD-45-nm-Opterons-to-function-on-current-server-boards-738019.html "AMD: 45 nm Opterons to function on current server boards – 07 November 2008, 06:55"). Some do add hardware support though – a [patch](http://thread.gmane.org/gmane.linux.kernel/714346) adds support to the kernel for the webcam in the Medion Akoya mini E1210 netbook.

## In Brief

- Jeremy Fitzhardinge [reports on the status of Xen integration in the Linux kernel](http://thread.gmane.org/gmane.comp.emulators.xen.devel/54274), saying amongst other things, that he hopes to have Dom0 support merged into the mainline 2.6.28.
- The Open Source Automation Development Lab ([OSADL](http://www.osadl.org/)) has [declared their real-time kernel based on Linux 2.6.24 as their "Latest Stable" release](http://www.osadl.org/Single-View.111+M59309c3c8d7.0.html). It uses the framework of the [RT Development branch](http://rt.wiki.kernel.org/) to give Linux real-time characteristics.
- Constantine Shulyupin is [updating the "Kernel Map"](http://groups.google.com/group/fa.linux.kernel/browse_thread/thread/9c847e20929d82e9/6efa2921feea7421?show_docid=6efa2921feea7421) ([interactive](http://www.makelinux.net/kernel_map),[png](http://www.makelinux.info/kernel_map.d/LKM63_2048.png) and is looking for comments.
- After the [problems surrounding ACPI](../site/news/item/OpenDS-Directory-Server-1-0-released-736517.html "OpenDS Directory Server 1.0 released – 18 July 2008, 09:30"), Matthew Garrett [gives more background on ACPI and Linux](http://mjg59.livejournal.com/96129.html) and explains why ACPI implementations might want to distinguish between a Windows and a Linux operating system.
- Jesse Barnes [is already planning xf86-video-intel 2.5](http://lists.freedesktop.org/archives/xorg/2008-July/037672.html) following the release of [2.4.0](../site/news/item/OpenDS-Directory-Server-1-0-released-736517.html "OpenDS Directory Server 1.0 released – 18 July 2008, 09:30"), aiming to release with usable EXA support and cooperation with GEM if it is loaded in the kernel.
- [The HPLIP project](http://hplip.sourceforge.net/) have released version 2.8.87 of the Hplip drivers for HP printers and multifunction devices. Newly supported are the Deskjet f735 and d730 and the PhotoSmart a532, a536, a538 and c5500.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log : Tux3 file system announced, X.org updates](../site/news/item/Kernel-Log-Tux3-file-system-announced-X-org-updates-736707.html "Kernel Log : Tux3 file system announced, X.org updates – 01 August 2008, 09:17")
- [Kernel Log: 2.6.25.13 corrects a vulnerability, problems with ACPI](../site/news/item/Kernel-log-2-6-25-13-corrects-a-vulnerability-problems-with-ACPI-736703.html "Kernel log: 2.6.25.13 corrects a vulnerability, problems with ACPI – 31 July 2008, 14:42")
- [Kernel Log: First release candidate concludes the hot development phase of 2.6.27](../site/news/item/Kernel-Log-First-release-candidate-concludes-the-hot-development-phase-of-2-6-27-736695.html "Kernel Log: First release candidate concludes the hot development phase of 2.6.27 – 31 July 2008, 12:23")
- Kernel Log: Practical Practices - Ottawa Linux Symposium Notes
- [Kernel Log: Centrino 2 WLAN driver iwl 5000 and webcam driver gscpa in Linux 2.6.27](../site/news/item/Kernel-Log-Centrino-2-WiFi-driver-iwl-5000-and-webcam-driver-gscpa-in-Linux-2-6-27-736569.html "Kernel Log: Centrino 2 WiFi driver iwl 5000 and webcam driver gscpa in Linux 2.6.27 – 23 July 2008, 16:46")
- [Kernel Log: ath9k driver for new Atheros WLAN chips, discussions of Nvidia drivers](../site/news/item/Kernel-log-ath9k-driver-for-new-Atheros-WLAN-chips-discussions-of-Nvidia-drivers-736563.html "Kernel log: ath9k driver for new Atheros WLAN chips, discussions of Nvidia drivers – 22 July 2008, 15:48")
- [Kernel Log: No unstable series; Linux 2008.7, dealing with security fixes](../site/news/item/Kernel-Log-No-unstable-series-Linux-2008-7-dealing-with-security-fixes-736557.html "Kernel Log: No unstable series; Linux 2008.7; dealing with security fixes – 22 July 2008, 01:47")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
