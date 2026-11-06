---
title: "Kernel Log: New kernels, open audio drivers for X-Fi"
date: 2008-11-11
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-New-kernels-open-audio-drivers-for-X-Fi-738061.html
pages: 1
---

# Kernel Log: New kernels, open audio drivers for X-Fi

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/4/8/3/2/93e8ea3d0acdf147.jpg) Creative Labs has recently started to offer the source code of a GPLv2 licensed Linux driver for X-Fi sound hardware on its [download page](http://support.creative.com/Downloads/welcome.aspx). According to the driver's documentation and a posting [on the forum](http://forums.creative.com/creativelabs/board/message?board.id=soundblaster&thread.id=132288) by a Creative employee, the driver is only intended for advanced users and certainly not for production systems; "*We recommend that only experienced users install this driver. Do not install this driver on a system used to perform critical tasks.*". A list of the X-Fi models supported by the driver and the driver's complete range of features can be found in the same posting; while recording and playback are said to work via Alsa, the driver doesn't currently support external sound card I/O modules.

This seems to put an end to the driver chaos around X-Fi, following the release of two beta versions of Creative's rough and only partially ready proprietary beta driver more than a year ago and a [rudimentary open source driver](../site/news/item/Creative-Labs-opens-up-driver-development-734163.html "Creative Labs opens up driver development – 09 February 2008, 13:08") based on Open Sound Systems (OSS) which has become largely irrelevant for Linux environments. Whether the Creative driver will be widely accepted remains to be seen. Alsa and kernel developer Takashi Iwai has also been working on a driver for X-Fi hardware within the [Alsa project](http://www.alsa-project.org/main/index.php/Main_Page). However, [version 1.0.18](http://www.alsa-project.org/main/index.php/Changes_v1.0.17_v1.0.18) of the Alsa components, which was released at the end of October, didn't include this driver.

### New kernel versions

In the past few days, the kernel hackers have released several new Linux versions for users who like to compile their own kernels rather than obtain them from a distributor. [Kernel 2.6.27.5](http://thread.gmane.org/gmane.linux.kernel/754801) adds several corrections and some minor improvements to the 2.6.27 series – it contains a change to the TCP stack said to solve a router related [network connectivity problem](http://lwn.net/Articles/304791/). In the new version's release email, Greg Kroah-Hartman suggests with considerably more emphasis than usual that users update to the new version, but he didn't explicitly point out any security related corrections.

With the release of [2.6.25.20](http://thread.gmane.org/gmane.linux.kernel/754791) and [2.6.26.8](http://thread.gmane.org/gmane.linux.kernel/754761), two further new stable kernels are now available. These versions could be the last in the 2.6.25 and 2.6.26 series, as the maintainers of the stable kernel series have announced that they will soon stop supporting them. This could well be one of the reasons for the emphatic invitation to update to 2.6.27.5.

For users of 2.4 kernels, Willy Tarreau has released version [2.4.36.9](http://thread.gmane.org/gmane.linux.kernel/755286) which includes several minor corrections including one to fix a DoS vulnerability. Only an hour later, the maintainer of the 2.4 series released [2.6.37-rc2](http://thread.gmane.org/gmane.linux.kernel/755295). The second release candidate of 2.6.37 offers many of the corrections included in 2.4.36.9 as well as several new or improved drivers – find [details](http://thread.gmane.org/gmane.linux.kernel/755295) in the release announcement email.

Meanwhile, the development of 2.6.28 continued to progress with the release of [2.6.28-rc3](http://thread.gmane.org/gmane.linux.kernel/752356) and [2.6.28-rc4](http://thread.gmane.org/gmane.linux.kernel/755303).

### In Brief

- The X.org developers have released [version 1.5.3 of the X-Server](http://lists.freedesktop.org/archives/xorg-announce/2008-November/000681.html) to add some corrections. This X-Server is part of X.org 7.4. The developers also released version [2.4.1 of libdrm](http://lists.freedesktop.org/archives/xorg-announce/2008-October/000678.html).

<!-- -->

- Nvidia has [released the beta version 96.43.09 of the 96xx legacy drivers](http://www.nvnews.net/vbulletin/showthread.php?t=122139) for early Nvidia cards. It is said to work with series 1.5 X-Servers, which are, for example, included in Fedora 9 and Ubuntu 8.10.

<!-- -->

- Matthias Hopf reports about the development progress of the DRI support for R6xx GPUs (Radeon 2xxx/3xxx) [in his blog](http://emmes.livejournal.com/2155.html).

<!-- -->

- After several futile attempts to remove eepro100 – a derivative of the e100 driver for early Intel network cards – from the kernel sources, the kernel developers are [now planning to make another attempt in Linux 2.6.29](http://thread.gmane.org/gmane.linux.network/109993).

<!-- -->

- [Terratec](http://www.terratec.net/en/index.html) has set up a [web page](http://linux.terratec.de/) offering a Linux driver as well as links to various open source drivers that support Terratec hardware; there is, though, no overview of which Linux version is supported by the drivers and which audio and video hardware is supported by the drivers.

<!-- -->

- Mark Lord has released versions [9.2](http://thread.gmane.org/gmane.linux.ide/35807) and [9.3](http://thread.gmane.org/gmane.linux.ide/35807/focus%3D35847) of [hdparm](http://sourceforge.net/projects/hdparm/) to download. They now support Device Configuration Overlay (DCO), firmware download and IDLE_IMMEDIATE.

<!-- -->

- The [hplip project](http://hplipopensource.com/) developers have released [version 2.8.10 of the hplip drivers](http://hplipopensource.com/hplip-web/release_notes.html) for HP printers and multifunction devices. This version offers a plug-in to support the scanners of various LaserJet models and can address 46 devices not supported by previous hplip versions.

<!-- -->

- The article "[Get to know GCC 4 - What's new in the GNU Compiler Collection release series](http://www.ibm.com/developerworks/linux/library/l-gcc4/index.html)" at IBM's developerworks portal describes some new features of the latest GCC version.

<!-- -->

- The Madwifi project can now on be found at the [madwifi-project.org](http://madwifi-project.org/) domain – according to the [removal announcement](http://madwifi-project.org/wiki/news/20081106/new-primary-project-domain) there were ongoing DNS problems with the previous server.

<!-- -->

- The development branch of the [btrfs](http://btrfs.wiki.kernel.org/) filesystem has recently started to support [data compression](http://thread.gmane.org/gmane.comp.file-systems.btrfs/1500). The developers once again had to change the on-disk format to implement this feature.

<!-- -->

- [Version 3.12](http://linux-man-pages.blogspot.com/2008/10/man-pages-312-is-released.html) of the man-pages now also documents the syscalls around the file descriptors [which were added to Linux 2.6.27](http://lwn.net/Articles/281965/).

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: Short video interviews with Torvalds, Kroah-Hartman and others](../site/news/item/Kernel-Log-Short-video-interviews-with-Torvalds-Kroah-Hartman-and-others-737833.html "Kernel Log: Short video interviews with Torvalds, Kroah-Hartman and others – 28 October 2008, 15:46")
- [Kernel Log: 2.6.28-rc1 released, new graphics and camera drivers](../site/news/item/Kernel-log-2-6-28-rc1-released-new-graphics-and-camera-drivers-737795.html "Kernel log: 2.6.28-rc1 released, new graphics and camera drivers – 27 October 2008, 09:10")
- [Kernel Log: What's coming in 2.6.28 - Part 4: Improved graphics support](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-4-Improved-graphics-support-737779.html "Kernel Log: What's coming in 2.6.28 - Part 4: Improved graphics support – 25 October 2008, 08:02")
- [Kernel Log: New Atheros WLAN drivers and stable kernels, radeon vs. radeonhd](../site/news/item/Kernel-Log-New-Atheros-WLAN-drivers-and-stable-kernels-radeon-vs-radeonhd-737773.html "Kernel Log: New Atheros WLAN drivers and stable kernels, radeon vs. radeonhd – 24 October 2008, 10:59")
- [Kernel Log: What's coming in 2.6.28 - Part 3: Dodgy drivers](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-3-Dodgy-drivers-737747.html "Kernel Log: What's coming in 2.6.28 - Part 3: Dodgy drivers – 22 October 2008, 09:29")
- [Kernel Log: More than 10 million lines of Linux source files](../site/news/item/Kernel-Log-More-than-10-million-lines-of-Linux-source-files-737731.html "Kernel Log: More than 10 million lines of Linux source files – 21 October 2008, 14:50")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
