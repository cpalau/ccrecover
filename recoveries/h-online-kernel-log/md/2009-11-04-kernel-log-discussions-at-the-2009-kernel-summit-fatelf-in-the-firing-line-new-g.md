---
title: "Kernel Log - Discussions at the 2009 Kernel Summit, FatELF in the firing line, new graphics drivers"
date: 2009-11-04
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-Discussions-at-the-2009-Kernel-Summit-FatELF-in-the-firing-line-new-graphics-drivers-850044.html
pages: 1
---

# Kernel Log - Discussions at the 2009 Kernel Summit, FatELF in the firing line, new graphics drivers

**Dj Walker-Morgan**

#### ![](../site/imgs/43/4/3/6/3/3/2/kernellogpenguin.jpg-03be1eada51fb8bf.jpeg) by Thorsten Leemhuis

**This year's Kernel Summit saw Linux developers, led by Linus Torvalds, discussing the development process and gaining an insight into how Google uses the Linux kernel in-house. Ulrich Drepper and Alan Cox think universal binaries in Linux are a step in the wrong direction. Various graphics drivers have recently been updated to add new functionality.**

### Developers get-together

This year's Kernel Summit was held in mid October in Tokyo. The kernel developers invited to the event discussed a broad range of Linux kernel-related issues and kernel development. Linux Weekly News has, as usual, published a [detailed summary](http://lwn.net/Articles/KernelSummit2009/) of the topics discussed at the meeting, which is now also available to non-subscribers.

As ever, one of the main topics of discussion was the development process. According to [the LWN.net report](http://lwn.net/Articles/357805/), kernel developers are broadly happy with linux-stable and linux-next, but there was criticism of the fact that a significant number of patches are not finding their way into linux-next before being merged into the main development tree. The kernel hackers are also considering in future moving occasional obsolete kernel drivers to the staging area for immature drivers which don't meet kernel development quality standards. If they do not get picked up from there, they will then be removed from the kernel source completely a few months later. Other points were also discussed, but, as the report stresses, in contrast to previous developer meetings, Linus Torvalds now appears to be broadly satisfied with the overall development process.

The article "[How Google uses Linux](http://lwn.net/Articles/357658/)" takes a detailed look at a Kernel Summit presentation given by a Google staff member on the search engine behemoth's use of Linux. To date, Google has been using older kernels, which it rarely updates and which have been extensively patched to optimise them for Google's purposes. Much of this work does not get submitted for integration into the main development tree, but efforts are under way to work more closely with kernel developers in future.

Not for the first time, the kernel developers discussed the best procedure for [preventing regressions](http://lwn.net/Articles/357480/) â€“ problems fixed in previous versions which re-emerge in later releases. Following Linus Torvalds attention-grabbing statement that the kernel is "[bloated and huge](../site/news/item/Linux-Bloated-and-Huge-says-Linus-812222.html "Linux "Bloated and Huge" says Linus â 22 September 2009, 10:08")", there was also discussion of [performance regressions](http://lwn.net/Articles/357795/).

The Kernel Summit also saw elections for five members of the Linux Foundation's Technical Advisory Board ([TAB](http://www.linuxfoundation.org/en/Technical_Advisory_Board_%28TAB%29)). Jonathan Corbet from LWN.net, Greg Kroah-Hartman from Novell, Alan Cox from Intel, Thomas Gleixner from Linutronix and Theodore Y. Ts'o, seconded to the Linux Foundation from IBM, were all [elected](http://thread.gmane.org/gmane.linux.kernel/904349/focus%3D904554). The kernel developers also clearly had some fun at the summit, at least it certainly looks that way in Chris SchlÃ¤ger's [photo](http://picasaweb.google.com/cschlaeger/JapanLinuxSymposium#5395400000458161906) of Linus Torvalds posing in front of a WindowsÂ 7 sales stand. A [group photo of the participants at the summit](http://lwn.net/Articles/357651/) can be found on LWN.net.

### Bloated

Ryan Gordon's recent presentation of the FatELF concept, which makes possible universal binaries under Linux, has attracted a great deal of attention. Glibc maintainer Ulrich Drepper was less than enthusiastic in a posting to a Fedora mailing list, "It is a 'solution' which adds costs in many, many places for a problem that doesn't exist. I don't see why people even spend a second thinking about this."

Gordon has since submitted a number of FatELF kernel patches to LKML for evaluation. Alan Cox has spoken out [robustly against](http://thread.gmane.org/gmane.linux.kernel/904188/focus%3D907811) the adoption of one of these patches in one posting on LMKL. [In another](http://thread.gmane.org/gmane.linux.kernel/907751/focus%3D908229), the Linux grandee has taken a closer look at the supposed benefits offered by FatELF, explaining in some detail why he sees it as an irrelevance, with package managers having solved the problem back in the '90s.

There was also a question mark over whether FatELF, in its current form, may infringe certain patents â€“ Gordon had [asked for help](http://thread.gmane.org/gmane.linux.kernel/907751/focus%3D907852) in clarifying this issue, but has now [decided to abandon](http://icculus.org/cgi-bin/finger/finger.pl?user=icculus&date=2009-11-03&time=19-56-22) his attempt to get FatELF adopted and has archived the project.

### In Brief: The Kernel

### 

- One developer [recently proposed](http://thread.gmane.org/gmane.linux.ide/43131/) designating the IDE subsystem, taken under the wing of David Miller several months ago, as deprecated, in order to encourage people to switch to more modern drivers in the Libata subsystem. There are strong signs that this proposal is likely to be adopted, but the issue of when is still under discussion.
- The Android drivers added to the staging area of Linux 2.6.29 may be given the boot because Google developers [are no longer maintaining them](http://thread.gmane.org/gmane.linux.kernel/905490/focus%3D907367). A Google employee has, however, [announced](http://thread.gmane.org/gmane.linux.kernel/905490/focus%3D907382) that in the longer term they are hoping to increase their contribution to the main Linux development branch.
- The GRUB development team has recently released [version 1.97](http://thread.gmane.org/gmane.comp.boot-loaders.grub.devel/13738) of the GRUB2 boot loader. It is now able to load kernels for various BSD derivatives, supports x86-64 EFI and offers enhancements for GPT. Storage devices can also now be addressed using UUID.
- The latest stable kernel versions, [2.6.27.38](http://thread.gmane.org/gmane.linux.kernel/905319/) and [2.6.31.5](http://thread.gmane.org/gmane.linux.kernel/905318), were released on 23Â October.
- Kernel developer Rusty Russell will in future be doing [more work on Samba](http://ozlabs.org/~rusty/index.cgi/2009/10/24#2009-10-23), but will also continue to maintain the Virtio drivers
- Following a lengthy lull in the process of merging the Lirc drivers (used in many remote controls) into the main Linux development tree, Jarod Wilson is taking [a second shot](http://thread.gmane.org/gmane.linux.kernel.input/9227) at it.
- Neil Brown, MD kernel code maintainer, has released mdadm versions [3.0.3](http://thread.gmane.org/gmane.linux.raid/24899) and [3.1.0](http://thread.gmane.org/gmane.linux.raid/24902). While the former contains minor enhancements and bug fixes, the latter includes numerous new options for setting up and modifying software RAID arrays. It now allows RAIDÂ 1 to be converted to RAIDÂ 5 and from there to RAIDÂ 6 and back again, and can be used to shrink RAID levels 4, 5 and 6. Some of this functionality requires very new, or as yet unreleased, kernel versions. Users should therefore only use version 3.1.0 if they require the new functionality or wish to test the new version. Brown has since found the odd bug, which he plans to remedy by releasing version 3.1.1. He expects the latter to be suitable for general use.

### Driving Graphics

NVIDIA late last week released version 190.42 of its proprietary graphics driver for [x86-32](http://www.nvidia.com/object/linux_display_ia32_190.42.html) and [x86-64](http://www.nvidia.com/object/linux_display_amd64_190.42.html) Linux. New features include support for OpenGL 3.2, X-Server 1.7.0Â RC1 and many new graphics cards. There were also enhancements in the Video Decode and Presentation API for Unix (VDPAU). The driver can now also be used to control fan and energy-saving behaviour ("GPU PowerMizer Mode").

A few days earlier, AMD released a new version of its [proprietary Linux](http://ati.amd.com/support/drivers/linux/linux-radeon.html) graphics driver, which it has designated as version 9.10. New features include 'early look support' for Ubuntu 9.10, which uses Linux kernel 2.6.31. The [release notes](http://www2.ati.com/drivers/linux/catalyst_910_linux.pdf)![PDF](../site/icons/file-pdf.gif "PDF document") list various bugs which should no longer occur with the latest driver.

Intel developers have recently [released](http://thread.gmane.org/gmane.comp.freedesktop.xorg/41151) version 2.9.1 of Intel's open source driver for Intel graphics chip sets, which is primarily a bug fix release. The radeonhd driver development team released [version 1.3.0](http://thread.gmane.org/gmane.comp.freedesktop.xorg.drivers.radeonhd/8500) shortly after the last [Kernel Log](../site/news/item/Kernel-Log-Improved-USB-3-0-support-X-org-drivers-to-move-back-into-X-Server-819872.html "Kernel Log - Improved USB 3. 0 support, X.org drivers to move back into X Server â 07 October 2009, 16:18"). Driver developer Matthias Hopf has published a [blog entry](http://emmes.livejournal.com/6258.html) listing the major changes, including support for newer Radeon models, HDMI audio and some of the power-saving functions offered by Radeon graphics hardware. Ben Skeggs has meanwhile summarised the changes and enhancements to the Nouveau driver over the last six months [on his blog](http://skeggsb.livejournal.com/568.html).

### In Brief: Graphics

### 

- Peter Hutterer has once again summarised the major changes in the recently released X11R7.5 (Xorg 7.5) [on his blog](http://who-t.blogspot.com/2009/10/x11r75-released-but-what-is-it.html). They include [version 1.7.1](http://thread.gmane.org/gmane.comp.freedesktop.xorg/41121) of X server which fixes numerous bugs from [version 1.7.0](../site/news/item/X-org-Server-1-7-0-released-812407.html "X.org Server 1.7.0 released â 02 October 2009, 10:31"), released in early October.
- With kernel-based mode setting having already delivered a largely flicker-free boot experience, systems with a cooperative BIOS and various patches [submitted](http://thread.gmane.org/gmane.comp.video.dri.devel/39639) by Jesse Barnes should now be able to go completely flicker-free.
- In recent days, various developers have been making big changes to the X.org Wiki's [table](http://www.x.org/wiki/RadeonFeature) of X driver functionality for Radeon hardware. The column for the radeonhd driver has been removed and a new column added for the Evergreen GPUs used in the Radeon HD 5000 series.
- An NVIDIA programmer working on the company's proprietary Linux graphics drivers recently gave an [interview with Phoronix](http://www.phoronix.com/scan.php?page=article&amp&item=nvidia_qa_linux&amp&num=1), in which he offers some insights into the drivers, driver development and the significance of these drivers for the company.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the Kernel Log at The H Open Source:*

- [Kernel Log - Improved USB 3. 0 support, X.org drivers to move back into X Server](../site/news/item/Kernel-Log-Improved-USB-3-0-support-X-org-drivers-to-move-back-into-X-Server-819872.html "Kernel Log - Improved USB 3. 0 support, X.org drivers to move back into X Server â 07 October 2009, 16:18")
- [Kernel Log - Devtmpfs in 2.6.32, more discussion about DRBD, new stable kernels](../site/news/item/Kernel-Log-Devtmpfs-in-2-6-32-more-discussion-about-DRBD-new-stable-kernels-812212.html "Kernel Log - Devtmpfs in 2.6.32, more discussion about DRBD, new stable kernels â 21 September 2009, 12:36")
- [Kernel Log - Main development phase of Linux 2.6.32 completed](../site/news/item/Kernel-Log-Main-development-phase-of-Linux-2-6-32-completed-812328.html "Kernel Log - Main development phase of Linux 2.6.32 completed â 28 September 2009, 15:46")
- [The Next Round â€“ The new features of Linux 2.6.31](../site/open/features/The-Next-Round-The-new-features-of-Linux-2-6-31-746619.html "The Next Round – The new features of Linux 2.6.31 â 10 September 2009, 07:33")
- [Kernel Log â€“ Extra round for 2.6.31, X.org 7.5 on the horizon, staging area to be cleaned up](../site/news/item/Kernel-Log-Extra-round-for-2-6-31-X-org-7-5-on-the-horizon-staging-area-to-be-cleaned-up-743289.html "Kernel Log – Extra round for 2.6.31, X.org 7.5 on the horizon, staging area to be cleaned up â 08 September 2009, 10:06")
- [Kernel Log - Coming in 2.6.31 - Part 5: CUSE, USB 3.0, FireWire networking and the rest](../site/news/item/Kernel-Log-Coming-in-2-6-31-Part-5-CUSE-USB-3-0-FireWire-networking-and-the-rest-743173.html "Kernel Log: Coming in 2.6.31 - Part 5: CUSE, USB 3.0, FireWire networking and the rest â 31 August 2009, 08:02")

*Older Kernel Logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/).* ([thl](mailto:thl@ct.heise.de) /c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
