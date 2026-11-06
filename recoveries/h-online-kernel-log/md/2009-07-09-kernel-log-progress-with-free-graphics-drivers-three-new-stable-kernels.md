---
title: "Kernel Log: progress with free graphics drivers, three new stable kernels"
date: 2009-07-09
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-progress-with-free-graphics-drivers-three-new-stable-kernels-742411.html
pages: 1
---

# Kernel Log: progress with free graphics drivers, three new stable kernels

**Dj Walker-Morgan**

![Kernel Log Penguin](../site/imgs/43/3/6/8/8/4/2/93e8ea3d0acdf147.jpg)

**A new version of the nv driver supports later NVIDIA GPUs. Drivers giving 3D support for later Radeon GPUs are making progress, and so is code for running the X server without root rights. The kernel developers have now issued new stable kernel versions and no longer support the 2.6.29 series.**

Not much has been heard in recent months about the open-source graphics driver for NVIDIA GPUs, properly known as "xf86-video-nv" but usually shortened to just "nv". Recently, however, NVIDIA man Aaron Plattner released [version 2.1.14](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/667). Although innovations are few, some of the changes mean that the driver now handles a great many later graphic chips that were previously only supported by the Nouveau driver or the proprietary NVIDIA driver. These [include](http://cgit.freedesktop.org/xorg/driver/xf86-video-nv/commit/?id=c8d6f7aa7c99a1b71289f8e8e07becc10f61f379) various GeForce 7950 cards, the GeForce models 285 and 295, and many other graphics cards in the 9000 series.

[A week ago](http://jbridgman.livejournal.com/945.html), in his blog AMD's John Bridgman announced some progress with work on the open source driver code to give 3D support to the R6xx and R7xx GPU series used with Radeon graphics hardware in the 2000, 3000 and 4000 series. He said it seemed to be behaving properly on 14 of 63Â tests, drawing incorrectly on 24 and either not drawing or crashing, on the remaining 25. Apart from there still being some work to do to fix these bugs the driver performance is also reported to be (*"mind-bogglingly slow"*).

Meanwhile the developers have released X server [version 1.6.2](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/672), which is reported to fix various bugs in its 1.6-series predecessors â€“ though the driver API and ABI should be compatible its two predecessors.

Intel developer Jesse Barnes and other X developers have been [discussing](http://thread.gmane.org/gmane.comp.freedesktop.xorg.devel/1158) the introduction of interfaces to let the X server run without root rights, as planned for Moblin. The kernel-based mode setting (KMS) introduced in 2.6.29 and improved in 2.6.30 is a step in this direction, but some details obviously still have to be worked out.

**Kernel status**

At the end of last week, the minders of the Linux Stable Series released versions [2.6.27.26](http://thread.gmane.org/gmane.linux.kernel/860990), [2.6.29.6](http://thread.gmane.org/gmane.linux.kernel/860991) and [2.6.30.1](http://thread.gmane.org/gmane.linux.kernel/860993), as usual advising users of previous versions to update, but without stating explicitly whether these new versions eliminate security bugs.

The updated kernels in the 27 and 29 series differ from their predecessors with 30 to 40 patches. Greg Kroah-Hartman emphasises in his email on 2.6.29.6 that this is to be the last version in the 29 series. In the [2.6.30-stable review email](http://thread.gmane.org/gmane.linux.kernel/859669), he apologises for the late appearance of the first stable version for [Linux version 2.6.30](../site/open/features/Fine-tuning-What-s-new-in-Linux-2-6-30-746581.html "Fine tuning – What's new in Linux 2.6.30 â 10 June 2009, 09:34"), which was released four weeks ago. With more than a hundred changes, 2.6.30.1 is quite comprehensive. Among other things, it improves the handling of Suspend and Resume for Intel GPUs, and makes a number of changes to the ath5k and ath9k drivers that handle Atheros WLAN chips.

The development of 2.6.31 has now reached its [second pre-release version](http://thread.gmane.org/gmane.linux.kernel/861659). It's now said to be a bit too large for Torvalds, making him somewhat less willing to accept changes.

**In Brief**

- Hans de Goede explains [in his blog](http://hansdegoede.livejournal.com/7932.html) that intentionally, some hardware monitoring drivers are no longer loaded under Linux 2.6.30, in order to prevent them clashing with the ACPI code.

<!-- -->

- The developers of the [HPLIP project](http://hplipopensource.com/) have released version 3.9.6b of the HPLIP drivers for HP printers and multi-function devices to eliminate some bugs in the still young version 3.9.6.

<!-- -->

- A [recent article](http://www.linux.com/news/software/linux-kernel/23685-the-kernel-newbie-corner-your-first-loadable-kernel-module) on Linux.com for beginners explains how to develop a small kernel module, containing few if any functions.

<!-- -->

- Christoph Hellwig has recently published the [XFS status update for June 2009](http://thread.gmane.org/gmane.comp.file-systems.xfs.general/29640).

<!-- -->

- In their Wiki, the wireless developers have [collected](http://wireless.kernel.org/en/developers/Summits/Berlin-2009) some papers that were presented at LinuxTag, the small wireless summit recently co-located with the FUDCon Fedora conference. A PDF version of the [presentation](http://www.kernel.org/pub/linux/kernel/people/linville/fudcon_berlin_2009/fudcon_berlin_2009.pdf)![PDF](../site/icons/file-pdf.gif "PDF document") given at FUDCon by the wireless subsystem maintainer John W. Linville is also online.

<!-- -->

- In his blog posting, [SELinux for Humans](http://james-morris.livejournal.com/42865.html), security subsystem maintainer James Morris mentions two slide decks that give some background information and give practical examples of SELinux. Earlier, in [another blog entry](http://james-morris.livejournal.com/42541.html), Morris summarised the main changes of Linux 2.6.30 in the realm of security.

<!-- -->

- The developers of the [ndsiwrapper](http://ndiswrapper.sourceforge.net/) have published version 1.55.

<!-- -->

- The [Ksplice developers](http://www.ksplice.com/) have [announced](http://thread.gmane.org/gmane.linux.kernel/857212) a [package depot](http://www.ksplice.com/uptrack/) that supplies Ksplice updates to users of Ubuntu 9.04 (Jaunty Jackalope) to correct security vulnerabilities in the Jaunty Jackalope kernel without requiring a reboot.

<!-- -->

- Till Kamppeter, OpenPrinting manager at the Linux Foundation, has released [version 4.0.2 of Foomatic](http://forums.linux-foundation.org/read.php?21,9708,9708#msg-9708).

<!-- -->

- In his blog, kernel developer Matthew Garrett [criticises](http://mjg59.livejournal.com/111853.html) Intel for the problematic situation with graphics drivers for the Poulsbo chip-set (US15W). He explains in [another blog entry](http://mjg59.livejournal.com/111995.html) what he's been doing to promote the use of USB auto-suspend in order to reduce power consumption.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the Kernel Log at The H Open Source:*

- [Kernel Log - Coming in 2.6.31 - Part 1: New Wi-Fi drivers and other network-related changes](../site/news/item/Kernel-Log-Coming-in-2-6-31-Part-1-New-Wi-Fi-drivers-and-other-network-related-changes-742309.html "Kernel Log - Coming in 2.6.31 - Part 1: New Wi-Fi drivers and other network-related changes â 02 July 2009, 12:44")
- [Kernel Log: Main development phase of Linux 2.6.31 completed](../site/news/item/Kernel-Log-Main-development-phase-of-Linux-2-6-31-completed-742199.html "Kernel Log: Main development phase of Linux 2.6.31 completed â 25 June 2009, 11:15")
- [Kernel Log : Winding down the IDE subsystem, LinuxTag Kernel presentations](../site/news/item/Kernel-Log-Winding-down-the-IDE-subsystem-LinuxTag-Kernel-presentations-742159.html "Kernel Log : Winding down the IDE subsystem, LinuxTag Kernel presentations â 23 June 2009, 17:04")
- [Fine Tuning - What's new in Linux 2.6.30](../site/open/features/Fine-tuning-What-s-new-in-Linux-2-6-30-746581.html "Fine tuning – What's new in Linux 2.6.30 â 10 June 2009, 09:34")
- [Kernel Log: What's coming in 2.6.30 - Architecture and infrastructure](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-Architecture-and-infrastructure-741921.html "Kernel Log: What's coming in 2.6.30 - Architecture and infrastructure â 06 June 2009, 07:47")
- [Kernel Log: What's coming in 2.6.30 â€“ Drivers: New drivers for audio, video, USB hardware, netbooks and notebooks](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-Drivers-New-drivers-for-audio-video-USB-hardware-netbooks-and-notebooks-741837.html "Kernel Log: What's coming in 2.6.30 – Drivers: New drivers for audio, video, USB hardware, netbooks and notebooks â 01 June 2009, 18:52")

*Older Kernel Logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/).*

([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
