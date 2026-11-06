---
title: "Kernel Log: New graphics drivers and Linux versions: Dom0 patches for 2.6.29?"
date: 2008-11-17
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-New-graphics-drivers-and-Linux-versions-Dom0-patches-for-2-6-29-738149.html
pages: 1
---

# Kernel Log: New graphics drivers and Linux versions: Dom0 patches for 2.6.29?

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/4/9/2/0/93e8ea3d0acdf147.jpg) AMD has released version 8.11 of its proprietary Linux graphics drivers, also known as fglrx or Catalyst, for [x86-32](http://ati.amd.com/support/drivers/linux/linux-radeon.html) and [x86-64](http://ati.amd.com/support/drivers/linux64/linux64-radeon.html). Under 'new features', the [release notes](http://www2.ati.com/drivers/linux/catalyst_811_linux.pdf)![PDF](../site/icons/file-pdf.gif "PDF document") list support for Red Hat Enterprise Linux (RHEL) 4.7, improved diagnostics for CrossFireX, and image scaling enhancements and adjustment for the (HD)TV formats 480i/p, 720p, 1080i and 1080p. AMD does not highlight what are certainly the most important new features in these drivers, support for X.org 7.4 and the ABI of the 1.5 series X server. Six months after the appearance of the [first distributions](../site/open/features/A-first-impression-of-Fedora-9-746490.html "A first impression of Fedora 9 – 27 May 2008, 11:01") of X Server  1.5 pre-release versions, AMD's proprietary graphics drivers can finally be used.

Nvidia was [much quicker](../site/news/item/Kernel-log-new-gfx-drivers-for-GeForce-Radeon-GPUs-Kernel-Track-at-LinuxTAG-735349.html "Kernel log: new gfx drivers for GeForce & Radeon GPUs; Kernel Track at LinuxTAG – 30 May 2008, 14:23") to implement compatibility with the 1.5 ABI on its main series of Linux graphics card drivers. Linux users with older graphics hardware supported only by Nvidia's 71xx and 96xx legacy drivers, who rely on being able to use features of the Nvidia drivers that the open source drivers do not offer, should stick with older X server distributions for the time being. A recently [released beta driver](http://www.nvnews.net/vbulletin/showthread.php?t=122139) offers some hope that Nvidia is planning at least a 96xx driver compatible with X Server 1.5. Together with the API, [announced separately](../site/news/item/Linux-API-harnesses-GeForce-GPU-s-HD-video-capabilities-738137.html "Linux API harnesses GeForce GPU's HD video capabilities – 17 November 2008, 08:54") in heise online, which makes use of the HD Video capabilities of GeForce GPUs under Unix-based systems such as Linux, Nvidia has now also released Linux beta drivers for its latest graphics cards. These have the version numbers 180.06, are available for [x86-32](http://www.nvidia.com/object/linux_display_ia32_180.06.html) and [x86-64](http://www.nvidia.com/object/linux_display_amd64_180.06.html) Linux and offer support for [CUDA](http://en.wikipedia.org/wiki/CUDA) 2.1. Nvidia has also updated its stable drivers with version 177.82 for [x86-32](http://www.nvidia.com/object/linux_display_ia32_177.82.html) and [x86-64](http://www.nvidia.com/object/linux_display_amd64_177.82.html) systems. Enhancements include a fix for a problem with Firefox and added support for a number of Quadro cards.

In the meantime, Intel developers have released versions [2.4.3](http://lists.freedesktop.org/archives/xorg-announce/2008-November/000686.html) and [2.5.1](http://lists.freedesktop.org/archives/xorg-announce/2008-November/000687.html) of the X.org graphic card driver xf86-video-intel. Both of these drivers, which are normally referred to simply as the "Intel" drivers, correct problems with the previous versions. According to the current roadmap, version 2.4.3 should be the last variant in the 2.4 series.

**New kernel versions**

The kernel hackers have released a host of new kernel versions in the past few days. Linux [2.6.25.20](http://thread.gmane.org/gmane.linux.kernel/755607) and [2.6.26.8](http://thread.gmane.org/gmane.linux.kernel/755610), for example, contain minor fixes for the 25 and 26 series. These are presumably the last versions of this kernel series, since the stable kernel team has announced its intention of discontinuing its maintenance support. In the release email, the kernel developers therefore recommend users of self-compiled kernels not supported by distributors to switch to the latest 2.6.27 version.

This is currently version [2.6.27.6](http://thread.gmane.org/gmane.linux.kernel/757074), which includes [a fix](http://git.kernel.org/?p=linux/kernel/git/stable/linux-2.6.27.y.git;a=commitdiff;h=3c050502c4166dc12009f35eb41fabe9c900cd43) for the [CVE-2008-5025](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2008-5025) security vulnerability in the HFS file system code. However, the stable team is already working on Linux [2.6.27.7](http://thread.gmane.org/gmane.linux.kernel/757722) – the kernel should in fact have been released today, but a few minor problems have meant that a second attempt will now be made to [issue the release](http://thread.gmane.org/gmane.linux.kernel/758296) on Wednesday.

Linus Torvalds has now released the [fifth pre-release version](http://thread.gmane.org/gmane.linux.kernel/757855) of Linux 2.6.28, which includes a number of small [structural updates and clean-ups](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=31c00fc15ebd35c1647775dbfc167a15d46657fd) to the documentation. A [recently updated list](http://thread.gmane.org/gmane.linux.kernel/757855) provides an overview of known problems in the main development tree found since 2.6.27.

**In Brief**

- Jeremy Fitzhardinge has published [a series of patches](http://thread.gmane.org/gmane.comp.emulators.xen.devel/57886) on LKLM for testing, which extends the Linux kernel by adding support for a Dom0 Xen domain. Elsewhere, Fitzhardinge has expressed his hope that an enhanced version of the code might possibly be incorporated in Linux 2.6.29.

<!-- -->

- Kernel hacker Matthew Garret, who specializes in ACPI and power-saving technologies, again reveals some interesting background information on Linux in his blog. In *[Adventures in PCI hotplug](http://mjg59.livejournal.com/100587.html)*, he looks into the PCIe hotplug technologies implemented in the Acer and Asus netbooks. Alternatively, in *[Hybrid Suspend](http://mjg59.livejournal.com/100643.html)* he examines some of the limitations of software suspend (hibernate) under Linux and explains why Linux will not be offering a hybrid suspend mode - as Microsoft has done in Windows Vista - for some time yet. Garrett has also been taking a *[closer look](http://mjg59.livejournal.com/100221.html)* at the Android kernel and has a few critical things to say about Google.

<!-- -->

- Perry Hung from MIT has [visualized](http://flickr.com/photos/45984696@N00/3023281511/) the Linux boot process. For fun, other bloggers have animated the same process [in Vista](http://www.junauza.com/2008/11/take-this-linux-windows-boot-sequence.html).

<!-- -->

- Peter Hutterer has [released version 1.0rc1 of the Synaptics touchpad driver](http://lists.freedesktop.org/archives/xorg-announce/2008-November/000688.html). Philip Langdale has released two new versions ([1](http://lists.freedesktop.org/archives/xorg-announce/2008-November/000689.html), [2](http://lists.freedesktop.org/archives/xorg-announce/2008-November/000690.html)) of the mouse driver for Linux guests running under VMWare.

<!-- -->

- The X developers are currently discussing [the schedule](http://thread.gmane.org/gmane.comp.freedesktop.xorg/33746/) for the completion of the [X Server 1.6 release](http://wiki.x.org/wiki/Server16Branch). According to the latest proposal from Intel release manager Keith Packard, the next X server generation should be ready in early January and will include DR12, RandR 1.3, input device properties and pointer acceleration – X Input 2 and Multi Pointer X (MPX) will not be ready in time.

<!-- -->

- Stephen Rothwell has summarized the linux-next rules and procedures [in an email](http://thread.gmane.org/gmane.linux.kernel.next/3836) to the kernel hackers.

<!-- -->

- Following the release of ALSA version 1.0.18, the developers have just made available [the bugfix release 1.0.18a](http://www.alsa-project.org/main/index.php/Changes_v1.0.18_v1.0.18a) of the [ALSA driver package](http://www.alsa-project.org/).

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: What's coming in 2.6.28 - Part 5: updates for netbooks and notebooks](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-5-updates-for-netbooks-and-notebooks-738121.html "Kernel Log: What's coming in 2.6.28 - Part 5: updates for netbooks and notebooks – 14 November 2008, 12:51")
- [Kernel Log: New kernels, open audio drivers for X-Fi](../site/news/item/Kernel-Log-New-kernels-open-audio-drivers-for-X-Fi-738061.html "Kernel Log: New kernels, open audio drivers for X-Fi – 11 November 2008, 10:03")
- [Kernel Log: Short video interviews with Torvalds, Kroah-Hartman and others](../site/news/item/Kernel-Log-Short-video-interviews-with-Torvalds-Kroah-Hartman-and-others-737833.html "Kernel Log: Short video interviews with Torvalds, Kroah-Hartman and others – 28 October 2008, 15:46")
- [Kernel Log: 2.6.28-rc1 released, new graphics and camera drivers](../site/news/item/Kernel-log-2-6-28-rc1-released-new-graphics-and-camera-drivers-737795.html "Kernel log: 2.6.28-rc1 released, new graphics and camera drivers – 27 October 2008, 09:10")
- [Kernel Log: What's coming in 2.6.28 - Part 4: Improved graphics support](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-4-Improved-graphics-support-737779.html "Kernel Log: What's coming in 2.6.28 - Part 4: Improved graphics support – 25 October 2008, 08:02")
- [Kernel Log: New Atheros WLAN drivers and stable kernels, radeon vs. radeonhd](../site/news/item/Kernel-Log-New-Atheros-WLAN-drivers-and-stable-kernels-radeon-vs-radeonhd-737773.html "Kernel Log: New Atheros WLAN drivers and stable kernels, radeon vs. radeonhd – 24 October 2008, 10:59")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
