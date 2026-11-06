---
title: "Kernel Log - Improved USB 3. 0 support, X.org drivers to move back into X Server"
date: 2009-10-07
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-Improved-USB-3-0-support-X-org-drivers-to-move-back-into-X-Server-819872.html
pages: 1
---

# Kernel Log - Improved USB 3. 0 support, X.org drivers to move back into X Server

**Dj Walker-Morgan**

![Kernel Log Penguin](../site/imgs/43/4/1/8/1/4/4/93e8ea3d0acdf147.jpg)

#### by Thorsten Leemhuis

**Linux 2.6.31.2 not only offers minor bug fixes, but also selected major changes. The X.org hackers have adapted their development strategy and, in the long term, plan to merge several drivers back into the X Server code.**

### Linux version status

The maintainers of the Linux Stable Series have recently released their Linux versions [2.6.27.36](http://thread.gmane.org/gmane.linux.kernel/898045), [2.6.30.9](http://thread.gmane.org/gmane.linux.kernel/898043) and [2.6.31.2](http://thread.gmane.org/gmane.linux.kernel/898044) â€“ with the usual unspecific recommendation that the users of non-distribution kernels should make sure they upgrade to the new versions ("*All users of the 2.6.xx kernel series are very strongly encouraged to upgrade.*").

The new versions usually correct bugs and offer a number of minor improvements. However, Linux 2.6.31.2 also includes some changes that are uncommonly substantial for a stable kernel, as Greg Kroah-Hartmanand [points out](http://thread.gmane.org/gmane.linux.kernel/896829) in his review email. For instance, apparently only now has the USB 3.0 support that was introduced with 2.6.31 been made to run smoothly in 2.6.31.2; the developers also modified some of the Wi-Fi, KVM and Xen drivers to a greater extent than they usually do. The new version is said to allow better I/O throughput rates for large servers.

In his [2.6.30.9 release e-mail](http://thread.gmane.org/gmane.linux.kernel/898043), Kroah-Hartman explains that this will be the last version in the 2.6.30 series â€“ users are advised to switch to Linux 2.6.31. The kernel hackers still intend to maintain the 2.6.27 series for some time.

### Main development branch

Having closed the merge window for Linux 2.6.32 by releasing the [first release candidate](../site/news/item/Kernel-Log-Main-development-phase-of-Linux-2-6-32-completed-812328.html "Kernel Log - Main development phase of Linux 2.6.32 completed â 28 September 2009, 15:46") a week ago, Linus Torvalds recently [released](http://thread.gmane.org/gmane.linux.kernel/897768) the second RC. It is called Linux 2.6.32-rc3, because Torvalds [accidentally](http://thread.gmane.org/gmane.linux.kernel/895032/focus%3D895039) wrote rc2 into the [makefile](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git&a=commitdiff&h=17d857be649a21ca90008c6dc425d849fa83db5c), which caused the first release candidate to pretend it was the second RC â€“ to avoid further confusion, [Linus Torvalds has now called](http://thread.gmane.org/gmane.linux.kernel/897768) the actual second release candidate rc3. Torvalds hopes to avoid similar blunders in future, he said ("*And let's hope that I won't have that particular "senior moment" any more. Although I'm sure I can screw up releases some other way.*")

[As reported](../site/news/item/Kernel-Log-Main-development-phase-of-Linux-2-6-32-completed-812328.html "Kernel Log - Main development phase of Linux 2.6.32 completed â 28 September 2009, 15:46"), the DRBD (Distributed Replicated Block Device) replication solution missed the integration deadline for Linux 2.6.32 â€“ however, Torvalds is [willing](http://thread.gmane.org/gmane.linux.kernel/895997/focus%3D896598) to merge DRBD with 2.6.33.

### X status

Having discussed [reliable X.org releases](../site/news/item/Proposed-X-org-development-cycle-changes-812369.html "Proposed X.org development cycle changes â 30 September 2009, 12:49") in September, the X.org developers agreed an [actual procedure](http://thread.gmane.org/gmane.comp.freedesktop.xorg.devel/2150/) that is very close to the original proposal made at the recently held X Developers' Conference 2009 ([XDC2009](http://www.x.org/wiki/Events/XDC2009)). In addition, the developers agreed to merge some of the drivers they currently maintain separately back into the X Server code from about X Server version 1.10 ("*Around 1.10, we'd like to merge the drivers back into the core so we can start getting a coherent API (well, any API would be a start).*").

Find further notes about the topics discussed at the XDC2009 [in the X.org wiki](http://www.x.org/wiki/Events/XDC2009/Notes). According to the notes, the developers are preparing Linux to support AMD series R800 GPUs that are used, for example, in the recently introduced Radeon HD 5800 ("*support coming up"*).

### In brief

- The [program page](http://linuxplumbersconf.org/2009/program/) of the Linux Plumbers Conference held in Portland, Oregon, at the end of September, contains numerous documents with conference presentation materials. Many of them offer valuable background information â€“ [Introducing SELinux Sandbox](http://linuxplumbersconf.org/2009/slides/dan-walsh-selinux-sandbox.pdf)![PDF](../site/icons/file-pdf.gif "PDF document"), for instance, contains information about the recently presented [Sandbox framework for desktop applications](../site/news/item/Fedora-12-demonstrates-sandbox-for-desktop-applications-812242.html "Fedora 12 demonstrates sandbox for desktop applications â 23 September 2009, 09:39"); [USB 3.0 for Linux](http://linuxplumbersconf.org/2009/slides/Sarah-A-Sharp-lpc-usb3-pres.pdf)![PDF](../site/icons/file-pdf.gif "PDF document") provides background info about the kernel's USB 3.0 support introduced with [Linux 2.6.31](../site/open/features/The-Next-Round-The-new-features-of-Linux-2-6-31-746619.html "The Next Round – The new features of Linux 2.6.31 â 10 September 2009, 07:33") and in [Re-plugging the Modern Desktop](http://linuxplumbersconf.org/2009/slides/Kay-Sievers-David-Zeuthen-plugging-the-modern-desktop.pdf)![PDF](../site/icons/file-pdf.gif "PDF document"), Kay Sievers and David Zeuthen explain some of the current developments in the Udev and DeviceKit area.

<!-- -->

- Edward Shishkin has [released](http://thread.gmane.org/gmane.comp.file-systems.reiserfs.general/22617) a [Linux 2.6.31](../site/open/features/The-Next-Round-The-new-features-of-Linux-2-6-31-746619.html "The Next Round – The new features of Linux 2.6.31 â 10 September 2009, 07:33")-compatible version of the Reiser4 file system, which was much discussed several years ago.

<!-- -->

- Douglas Gilbert has released [sg3_utils 1.28](http://thread.gmane.org/gmane.linux.scsi/54892) and [sdparm 1.04](http://thread.gmane.org/gmane.linux.kernel/897472).

<!-- -->

- File system specialist Valerie Aurora has submitted [a new RFC](http://thread.gmane.org/gmane.linux.file-systems/35782) to further promote the development of a solution for union mounts (writeable file system overlays) that is suitable for integration into the main development branch.

<!-- -->

- A few days ago, a [Flash video](http://www.techcast.com/events/linuxcon/roundtable/) recording of the "Linux Kernel Roundtable" held at the Linuxcon conference was published on the web pages of techcast.com â€“ in the discussions, Torvalds [called](../site/news/item/Linux-Bloated-and-Huge-says-Linus-812222.html "Linux "Bloated and Huge" says Linus â 22 September 2009, 10:08") the Linux kernel "bloated."

<!-- -->

- Peter Hutterer has [announced](http://thread.gmane.org/gmane.comp.freedesktop.xorg.devel/2112/) the new xf86-input-wacom driver â€“ it is a fork of the [linuxwacom](http://linuxwacom.sourceforge.net) driver for Wacom tablets initiated by Ping Cheng, which in future, the X.org hackers intend to [develop and improve](http://thread.gmane.org/gmane.linux.drivers.wacom.devel/50) within X.org and Freedesktop.org.

<!-- -->

- The developers of the xf86-video-intel X.org graphics driver have released [version 2.9.0](http://thread.gmane.org/gmane.comp.freedesktop.xorg/40733) of the driver. It offers several improvements for Intel's old series 800 graphics chip-sets and supports the vendor's B43 chip-set. The driver is part of a "[Intel 2009Q3 release package](http://thread.gmane.org/gmane.comp.freedesktop.xorg/40735)" that became available on the same day and offers further driver software needed, among other things, for 3D support â€“ for instance the recently released [Mesa3D 7.6](http://www.mesa3d.org/relnotes-7.6.html). The Intel developers recommend to give preference to KMS (Kernel-based Mode Setting) with this driver collection ("*KMS (Kernel Mode Setting) is strongly recommended to use in this release.*").
- The Embedded Linux service provider [Pengutronix](http://www.pengutronix.de/) in Hildesheim has [recently](http://thread.gmane.org/gmane.linux.kernel/894797) started to maintain a repository with kernel packages precompiled for Debian that contain the real-time patches of the [development branch](http://rt.wiki.kernel.org:RT).

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the Kernel Log at The H Open Source:*

- [Kernel Log - Devtmpfs in 2.6.32, more discussion about DRBD, new stable kernels](../site/news/item/Kernel-Log-Devtmpfs-in-2-6-32-more-discussion-about-DRBD-new-stable-kernels-812212.html "Kernel Log - Devtmpfs in 2.6.32, more discussion about DRBD, new stable kernels â 21 September 2009, 12:36")
- [Kernel Log - Main development phase of Linux 2.6.32 completed](../site/news/item/Kernel-Log-Main-development-phase-of-Linux-2-6-32-completed-812328.html "Kernel Log - Main development phase of Linux 2.6.32 completed â 28 September 2009, 15:46")
- [The Next Round â€“ The new features of Linux 2.6.31](../site/open/features/The-Next-Round-The-new-features-of-Linux-2-6-31-746619.html "The Next Round – The new features of Linux 2.6.31 â 10 September 2009, 07:33")
- [Kernel Log â€“ Extra round for 2.6.31, X.org 7.5 on the horizon, staging area to be cleaned up](../site/news/item/Kernel-Log-Extra-round-for-2-6-31-X-org-7-5-on-the-horizon-staging-area-to-be-cleaned-up-743289.html "Kernel Log – Extra round for 2.6.31, X.org 7.5 on the horizon, staging area to be cleaned up â 08 September 2009, 10:06")
- [Kernel Log - Coming in 2.6.31 - Part 5: CUSE, USB 3.0, FireWire networking and the rest](../site/news/item/Kernel-Log-Coming-in-2-6-31-Part-5-CUSE-USB-3-0-FireWire-networking-and-the-rest-743173.html "Kernel Log: Coming in 2.6.31 - Part 5: CUSE, USB 3.0, FireWire networking and the rest â 31 August 2009, 08:02")
- [Kernel Log - Coming in 2.6.31 â€“ Part 4: Tracing, architecture, virtualisation](../site/news/item/Kernel-Log-Coming-in-2-6-31-Part-4-Tracing-architecture-virtualisation-743099.html "Kernel Log - Coming in 2.6.31 – Part 4: Tracing, architecture, virtualisation â 26 August 2009, 10:36")

*Older Kernel Logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
