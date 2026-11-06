---
title: "Kernel Log: X server 1.7 delayed; Compiz runs on newer Radeon GPUs; DRBD in kernel soon"
date: 2009-08-05
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-X-server-1-7-delayed-Compiz-runs-on-newer-Radeon-GPUs-DRBD-in-kernel-soon-742829.html
pages: 1
---

# Kernel Log: X server 1.7 delayed; Compiz runs on newer Radeon GPUs; DRBD in kernel soon

**Dj Walker-Morgan**

![Kernel Log Penguin](../site/imgs/43/3/6/9/2/6/0/93e8ea3d0acdf147.jpg)

#### by Thorsten Leemhuis

**Although some X.org drivers have been updated for X server 1.7, development work is running behind schedule. New drivers from AMD, Intel and Nvidia and new Linux versions mean a number of corrections and enhancements in the graphics system. 3D support for newer Radeon GPUs is now adequate for Compiz. DRBD should make it into the main Linux kernel development tree in 2.6.32.**

It seems like many of the Northern hemisphere's finest open source developers must be away enjoying their summer holidays at the moment â€“ apart from the [release of Microsoft's Hyper-V driver for Linux](../site/news/item/Microsoft-GPLs-Linux-virtualisation-drivers-742565.html "Microsoft GPLs Linux virtualisation drivers â 20 July 2009, 17:22") under the GPL and [a disagreement between Linux gurus Alan Cox and Linus Torvalds](../site/news/item/Dispute-between-Linux-gurus-Alan-Cox-and-Linus-Torvalds-742717.html), things have been pretty quiet. Not that the open source community is in complete hibernation and there are plenty of newsworthy events for the Kernel Log to report.

**All about graphics hardware**

NVIDIA last week released version 185.18.29 of its proprietary Linux graphics drivers ([x86-32](http://www.nvidia.com/object/linux_display_ia32_185.18.29.html), [x86-64](http://www.nvidia.com/object/linux_display_amd64_185.18.29.html)). They contain a number of bug fixes and a few minor enhancements, in particular for the Video Decode and Presentation API for Unix (VDPAU), [released last November](../site/news/item/Linux-API-harnesses-GeForce-GPU-s-HD-video-capabilities-738137.html "Linux API harnesses GeForce GPU's HD video capabilities â 17 November 2008, 08:54"). The graphics chip vendor is now working on major changes and OpenGL 3.2 support in its 190 series drivers â€“ the current pre-release version number is [190.18.03](http://www.nvnews.net/vbulletin/showthread.php?t=136819).

AMD had previously released version 9.7 of its proprietary Catalyst, aka Fglrx, graphics driver for Linux. Like its predecessors, it is not compatible with the no-longer-quite-so-new Linux [2.6.29](../site/open/features/Steady-growth-What-s-new-in-Linux-2-6-29-746553.html) and [2.6.30](../site/open/features/Fine-tuning-What-s-new-in-Linux-2-6-30-746581.html) kernels, despite 2.6.29 being over more than four and a half months old. Both kernels also include a range of drivers and functions which are missing in earlier versions â€“ users wanting to use the proprietary AMD driver, but also requiring drivers for other hardware components found only in 2.6.29 or 2.6.30 find themselves in something of a bind.

The open source developers at X.org have also been keeping busy â€“ Intel developer Keith Packard, for example, has [released](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/701) version 1.6.3 of X.org's X server which should fix a number of bugs in the previous version. New versions of various X.org graphics drivers have also been released to ensure that they are compatible with the API and ABI for X server 1.7, which is currently under development. X server 1.7 was originally scheduled for a July release, but this has now been [put back to mid August](http://thread.gmane.org/gmane.comp.freedesktop.xorg/31957/focus%3D883). This deadline also looks likely to be missed, with the branching in the source code control system initially planned for 6thÂ July [still not having taken place](http://cgit.freedesktop.org/xorg/xserver/refs/heads), meaning that the development team is around a month behind the current, revised schedule.

Intel developers have now [released](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/688) version 2.8 of the company's graphics driver, which forms part of the [2009Q2 graphics driver package](http://thread.gmane.org/gmane.comp.freedesktop.xorg/39882). [As expected](../site/news/item/Kernel-Log-X-org-7-5-coming-in-summer-re-write-for-Intel-s-graphics-driver-741405.html "Kernel Log: X.org 7.5 coming in summer, re-write for Intel's graphics driver â 04 May 2009, 07:09"), it requires at least version 1.6 of X server, due to the removal of code providing support for DRI1, EXA, XXA and NoAccel in order to facilitate driver maintenance. The driver should work best with Linux version 2.6.31, scheduled for release in late August or early September, as it will contain a number of enhancements for GEM (Graphics Execution Manager) and kernel-based mode setting (KMS); use of the latter is recommended by the programming team in their release emails. Intel developer Eric Anholt gives a detailed overview of some of the changes in version 2.8 and background information on ongoing work on versionÂ 2.9 [on his blog](http://anholt.livejournal.com/41306.html).

Other news on Linux drivers for graphics hardware:

- Last weekend, Alex Deucher followed up his announcement that he has been making [good progress](../site/news/item/Kernel-Log-progress-with-free-graphics-drivers-three-new-stable-kernels-742411.html "Kernel Log: progress with free graphics drivers, three new stable kernels â 09 July 2009, 09:42") on 3D drivers for the R6xx and R7xx GPUs used on 2000, 3000 and 4000 series Radeon graphics cards by announcing [on his blog](http://www.botchco.com/agd5f/?p=47) that he has now also got Compiz running, albeit slowly. He is confident though that this will soon be fixed.

<!-- -->

- X developer Peter Hutterer has added parts [4](http://who-t.blogspot.com/2009/07/xi2-recipes-part-4.html), [5](http://who-t.blogspot.com/2009/07/xi2-recipes-part-5.html) and [6](http://who-t.blogspot.com/2009/07/xi2-recipes-part-6.html) of his 'XI2 recipes' series. He has also now [completed](http://lists.freedesktop.org/archives/xorg-devel/2009-July/001529.html) the main development phase of the XÂ InputÂ 2 subsystem planned for inclusion in X server 1.7.

<!-- -->

- A number of developers are once again toiling away on a 'VGA arbiter' for coordinating access to certain graphics hardware resources kernel-side to ensure that multiple X servers running in parallel don't trip over each other. One thing this should achieve is to make it easier to deploy multi-seat environments. Details can be found in blog entries by [Dave Airlie](http://airlied.livejournal.com/67628.html) and [Tiago Vignatti](http://vignatti.wordpress.com/2009/07/24/multiseat-with-multiple-x-servers-or-the-right-way/).

**Kernel status**

The Linux stable series maintainers released versions [2.6.27.29](http://thread.gmane.org/gmane.linux.kernel/871616) and [2.6.30.4](http://thread.gmane.org/gmane.linux.kernel/871613) in advance of the weekend. These fix a number of bugs and include minor enhancements. As usual, the stable series maintainers are recommending all users of earlier versions to switch to the new versions, without explicitly stating whether these updates fix security-related bugs.

Linux 2.6.31 development has reached the [fifth pre-release version](http://thread.gmane.org/gmane.linux.kernel/871932) stage. At the weekend the list of known bugs which were not present in 2.6.30 was down to [28Â unresolved problems](http://thread.gmane.org/gmane.linux.power-management.general/15319). The list of bugs known to have slipped in between 2.6.29 and 2.6.30 ran to [39Â items](http://thread.gmane.org/gmane.linux.power-management.general/15320).

The 2.4 series has not been forgotten â€“ maintainer Willy Tarreau recently released versions [2.4.37.3](http://thread.gmane.org/gmane.linux.kernel/866988) and [2.4.37.4](http://thread.gmane.org/gmane.linux.kernel/869530).

Some Real-Time tree developers have meanwhile ported the Real-Time patches to version 2.6.31-rc4. Thomas Gleixner provides some information on the changes and enhancements in his [2.6.31-rc4-rt1 release email](http://thread.gmane.org/gmane.linux.kernel/869530).

**In Brief**

- Andrew Morton has recently expressed [strong support](http://thread.gmane.org/gmane.linux.kernel/862072/focus%3D867540) for merging [DRBD](http://www.drbd.org/) (Distributed Replicated Block Device) on the LKML. As things stand at present, the replication solution, which is primarily used in high availability (HA) environments, will be merged into the main development tree in Linux 2.6.32. linux-next already contains DRBD.

<!-- -->

- Frederic Weisbecker continues to [work](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-File-systems-New-and-revamped-file-systems-741319.html "Kernel Log: What's coming in 2.6.30 - File systems: New and revamped file systems â 27 April 2009, 16:11") on [patches for ReiserFS](http://thread.gmane.org/gmane.comp.file-systems.reiserfs.general/22501) to reduce the use of the Big Kernel Lock. This has improved performance in some cases, but the developers [admit](http://thread.gmane.org/gmane.comp.file-systems.reiserfs.general/22501/focus%3D22503) that they have not yet carried out any major stress testing.

<!-- -->

- File system developer Valerie Aurora (formerly Henson) has summarised the history of Btrfs â€“ Linux' next generation file system-elect â€“ in the LWN.net article "[A short history of btrfs](http://lwn.net/Articles/342892/)". She goes into how it differs from ZFS, on which she also worked. The H has also recently taken a closer look at Btrfs in its article "[The Btrfs file system](../site/open/features/The-Btrfs-file-system-746597.html)".

<!-- -->

- Development work on the Tux3 file system has temporarily ground to a halt because the main programmer [has his hands full](http://article.gmane.org/gmane.comp.file-systems.tux3/840) with other work. Ext file system developer Theodore Tso weighed in with [some nuggets of advice](http://article.gmane.org/gmane.comp.file-systems.tux3/864) on how to take things forward but also wondered what Tux3 has to offer that Btrfs does not.

<!-- -->

- Mark Lord has been working on support for the ATA Trim command in hdparm. Details can be found in the release postings for hdparm [9.17](http://thread.gmane.org/gmane.linux.ide/42050), [9.18](http://thread.gmane.org/gmane.linux.ide/42065) and [9.20](http://thread.gmane.org/gmane.linux.ide/42084).

<!-- -->

- Kernel developer Matthew Garrett, who specialises in power management, attempted to clear up some of the myths surrounding power saving technologies in a presentation at the Gran Canaria Desktop Summit. The presentation is [available as a video](http://www.geeksoc.org/gcds/Matthew%20Garrett,%20Power%20management.ogv).

<!-- -->

- ACPI maintainer Len Brown has just [published](http://thread.gmane.org/gmane.linux.acpi.devel/39326/focus%3D40677) an outline summary of the issues discussed at the Power Management mini-summit held at the Montreal Linux Symposium.

<!-- -->

- Wi-Fi developer Johannes Berg has released the first version, [designated version 0.1](http://thread.gmane.org/gmane.linux.kernel.wireless.general/36285), of the [rfkill application](http://wireless.kernel.org/en/users/Documentation/rfkill). In combination with the Rfkill framework present in more recent kernel versions, this makes it possible to query and monitor slide switches or keyboard short cuts for switching Wi-Fi and Bluetooth on and off.

<!-- -->

- Novell developer Gregory Haskins has [announced](http://thread.gmane.org/gmane.linux.kernel/872604) the launch of the AlacrityVM project and AlacrityVM version 0.1. AlacrityVM is a KVM-based hypervisor specifically optimised for HPC (high performance computing) and real time environments.

<!-- -->

- Upstart developer Scott James Remnant has [released](http://thread.gmane.org/gmane.comp.sysutils.upstart.devel/924) version 0.6.3 of Upstart.

<!-- -->

- Greg Kroah-Hartman has announced on [his blog](http://www.kroah.com/log/linux/vme-drivers.html) and on [the LKML](http://thread.gmane.org/gmane.linux.kernel/872821) that Linux drivers for the [VME Bus](http://en.wikipedia.org/wiki/VMEbus) will be merged into the staging area. He also expressed his appreciation of the work done by Martyn Welch, who has brought together five different branches for supporting the VME bus, some of which are several years old, and has persuaded the copyright holders to agree to a release under the GPL.

<!-- -->

- The [Gutenprint development team](http://gutenprint.sourceforge.net/) has released [version 5.2.4](http://sourceforge.net/project/showfiles.php?group_id=1537) of their printer driver collection. It supports a number of printers which were not supported by the previous version.

<!-- -->

- In his "[XFS status update for July 2009](http://thread.gmane.org/gmane.comp.file-systems.xfs.general/29978)", Christoph Hellwig provides an overview of the latest developments relating to the XFS file system.

<!-- -->

- The Linux Foundation is continuing its "Kernel Newbie Corner" series, with the latest article ([the sixth in the series](http://cli.gs/WG6WYX)) entitled "[Kernel Symbols: What's Available to Your Module, What Isn't](http://ldn.linuxfoundation.org/article/kernel-symbols-whats-available-your-module-what-isnt)".

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the Kernel Log at The H Open Source:*

- [Kernel Log: progress with free graphics drivers, three new stable kernels](../site/news/item/Kernel-Log-progress-with-free-graphics-drivers-three-new-stable-kernels-742411.html "Kernel Log: progress with free graphics drivers, three new stable kernels â 09 July 2009, 09:42")
- [Kernel Log: Coming in 2.6.31 - Part 1: New Wi-Fi drivers and other network-related changes](../site/news/item/Kernel-Log-Coming-in-2-6-31-Part-1-New-Wi-Fi-drivers-and-other-network-related-changes-742309.html "Kernel Log - Coming in 2.6.31 - Part 1: New Wi-Fi drivers and other network-related changes â 02 July 2009, 12:44")
- [Kernel Log: Main development phase of Linux 2.6.31 completed](../site/news/item/Kernel-Log-Main-development-phase-of-Linux-2-6-31-completed-742199.html "Kernel Log: Main development phase of Linux 2.6.31 completed â 25 June 2009, 11:15")
- [Kernel Log: Winding down the IDE subsystem, LinuxTag Kernel presentations](../site/news/item/Kernel-Log-Winding-down-the-IDE-subsystem-LinuxTag-Kernel-presentations-742159.html "Kernel Log : Winding down the IDE subsystem, LinuxTag Kernel presentations â 23 June 2009, 17:04")
- [Fine Tuning - What's new in Linux 2.6.30](../site/open/features/Fine-tuning-What-s-new-in-Linux-2-6-30-746581.html)
- [Kernel Log: What's coming in 2.6.30 - Architecture and infrastructure](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-Architecture-and-infrastructure-741921.html "Kernel Log: What's coming in 2.6.30 - Architecture and infrastructure â 06 June 2009, 07:47")
- [Kernel Log: What's coming in 2.6.30 â€“ Drivers: New drivers for audio, video, USB hardware, netbooks and notebooks](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-Drivers-New-drivers-for-audio-video-USB-hardware-netbooks-and-notebooks-741837.html "Kernel Log: What's coming in 2.6.30 – Drivers: New drivers for audio, video, USB hardware, netbooks and notebooks â 01 June 2009, 18:52")

*Older Kernel Logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/).*

([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
