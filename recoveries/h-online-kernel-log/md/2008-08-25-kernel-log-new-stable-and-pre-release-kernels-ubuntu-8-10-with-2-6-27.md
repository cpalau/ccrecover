---
title: "Kernel Log: New stable and pre-release kernels, Ubuntu 8.10 with 2.6.27?"
date: 2008-08-25
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-New-stable-and-pre-release-kernels-Ubuntu-8-10-with-2-6-27-737021.html
pages: 1
---

# Kernel Log: New stable and pre-release kernels, Ubuntu 8.10 with 2.6.27?

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/3/7/9/4/93e8ea3d0acdf147.jpg) The kernel developers have been busy in the last few days with several new Linux versions being released. Kernel versions [2.6.25.16](http://thread.gmane.org/gmane.linux.kernel/723993) and [2.6.26.3](http://thread.gmane.org/gmane.linux.kernel/723991) in the stable series have numerous fixes and minor improvements and some drivers [such as](http://git.kernel.org/?p=linux/kernel/git/stable/linux-2.6.26.y.git;a=commitdiff;h=cdc884a8da08b6007154b32a7878cd7fba1cf033) the Highpoint hpitop driver have expanded their supported devices list.

The release announcements for the new versions are a recommended update saying, "Any users of the 2.6.26 kernel series should upgrade to this version. For details on the fixes, see the changelog entries and the diffstat below." This is the standard text associated with the publication of stable series kernels and this makes it hard to say if any of the changes were related to vulnerabilities.

Linus Torvalds has published the fourth version of [2.6.27](http://thread.gmane.org/gmane.linux.kernel/724172), again with numerous bug fixes and also drivers for [the multitouch trackpad in recent MacBook Pro and MacBook Air notebooks](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f89bd95c5c946776f116ffeb997653d4193d6a35) and the [TUSB6010 USB controller](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=550a7375fe720924241f0eb76e4a5c1a3eb8c32f) from Texas Instruments.

Just before the release of 2.6.27-rc4, Linus Torvalds criticised the administrator of the network subsystem, David S. Miller, [specifically](http://thread.gmane.org/gmane.linux.network/103236/focus%3D103260) over the late and extensive updates he had submitted for inclusion into the main development branch. Miller and the other network developers should be in the second phase of the development cycle, focussing on bug fixes and deferring major changes to the next kernel version. In a [later mail](http://thread.gmane.org/gmane.linux.network/103236/focus%3D103371), Torvalds explained how he thought the subsystem administrators should handle this phase in the development cycle.

As part of the [lengthy discussion](http://thread.gmane.org/gmane.linux.network/103236/focus%3D103260), Miller [accepted](http://thread.gmane.org/gmane.linux.network/103236/focus%3D723540) Torvalds position. The current complaint is not new - Torvalds has had to stop and ask other developers to concentrate on bug fixing during the stabilisation phase over the past few months. If kernel hackers can more strongly adhere to the rules, then it could reduce the development time for new Linux versions – so far the stabilisation phase, planned to be six weeks long, has usually been nine weeks or more due to problems, such as large changes or new bugs, appearing during the merge window.

A shorter development time with 2.6.27 could become very important for Ubuntu after Ubuntu kernel developer Ben Collins proposed that version 8.10, Intrepid Ibex, could use the 2.6.27 kernel. The kernel currently used by the the Ubuntu developers is 2.6.26 which will need a number of improvements made to it, improvements that are already in 2.6.27. A fracture of the development tree has occurred with a new branch tracking 2.6.27, so that the Ubuntu developers can expedite a switch to 2.6.27 if it arrives before the target date for Ubuntu 8.10. Other distributions have used this strategy before without major problems.

------------------------------------------------------------------------

NTT Developer Ryusuke Konisho [published patches for review](http://thread.gmane.org/gmane.linux.file-systems/25660/) to the Linux Kernel Mailing list, to support NILFS2 (New Implementation of a Log-structured File System). The log-structured file system (LFS) supports "continuous snapshotting" and is designed for the needs of solid state drives, SSDs. A detailed description of the file system's functions is given on the [NILFS.org home page](http://www.nilfs.org/en/). At the 2008 [Linux & Storage File System Workshop](http://www.usenix.org/event/lsf08/) in February, a [presentation](http://www.usenix.org/event/lsf08/tech/shin_SSD.pdf) was given which compared NILFS2 with btrfs, ext2, ext3, ext4, reiserfs and XFS, and their behaviour and performance when operating with SSDs.

Another recently [published-for-review patch](http://thread.gmane.org/gmane.linux.kernel.embedded/835/) extended Linux support for AXFS, the Advanced XIP File System. XIP, eXecute-In-Place, allows code to be run from the file system rather than loading it into RAM first, and is especially useful in the embedded space where RAM is at a premium. The [AXFS home page](http://axfs.sourceforge.net/) contains details of XIP and how it functions. At the Ottawa Linux Symposium, one [presentation](http://ols.fedoraproject.org/OLS/Reprints-2008/hulbert-reprint.pdf) compared the advantages and disadvantages of AXFS with other embedded file systems such as CRAMFS, JFFS2, SQUASHFS,YAFFS2, LOGFS and UBIFS. Some well-known kernel developers were impressed with AXFS and are hoping to get it into Linux kernel 2.6.28.

**In Brief**

- Junio C Hamano released [GIT version 1.60](http://thread.gmane.org/gmane.comp.version-control.git/92666), the source code management system started by Linus Torvalds and used for Linux kernel development. Many GIT programs now can only be reached with commands like `git foo`, and not with the out dated form `git-foo`.
- Matthew Garrett released a [Dell laptop driver](http://thread.gmane.org/gmane.linux.kernel/722047) which can adjust brightness of the display and report the status of the Wifi switch.
- David Vrabel [presented](http://thread.gmane.org/gmane.linux.kernel/724481) a new set of drivers and patches for Linux support of Ultra Wideband radio, Wireless USB and WiMedia LLC Protocol.
- A [patch to the documentation](http://thread.gmane.org/gmane.linux.kernel/723878/) covers how Completely Fair Scheduling (CFS), which appeared in Linux 2.6.23, works in detail.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: New video drivers for AMD, Intel, Nvidia and VIA hardware](../site/news/item/Kernel-Log-New-video-drivers-for-AMD-Intel-Nvidia-and-VIA-hardware-736997.html "Kernel Log: New video drivers for AMD, Intel, Nvidia and VIA hardware – 22 August 2008, 11:59")
- [Kernel Log: Kernel development explained, new Synaptics driver, Linux 2.6.27-rc3 published](../site/news/item/Kernel-Log-Kernel-development-explained-new-Synaptics-driver-Linux-2-6-27-rc3-published-736911.html "Kernel Log: Kernel development explained, new Synaptics driver, Linux 2.6.27-rc3 published – 15 August 2008, 11:13")
- [Kernel Log: Ath9k driver for Atheros Wifi in 2.6.27; reading material and videos for Linux experts](../site/news/item/Kernel-Log-Ath9k-driver-for-Atheros-Wifi-in-2-6-27-reading-material-and-videos-for-Linux-experts-736829.html "Kernel Log: Ath9k driver for Atheros Wifi in 2.6.27; reading material and videos for Linux experts – 11 August 2008, 11:36")
- [Kernel Log: Btrfs 0.16 released, new stable kernels released, Wifi drivers for 2.6.27 merged](../site/news/item/Kernel-Log-Btrfs-0-16-released-new-stable-kernels-released-Wifi-drivers-for-2-6-27-merged-736815.html "Kernel Log: Btrfs 0.16 released, new stable kernels released, Wifi drivers for 2.6.27 merged – 08 August 2008, 14:32")
- [Kernel Log: New Stable kernel, DRI2 postponed, Xgl removed from X.org](../site/news/item/Kernel-Log-New-Stable-kernel-DRI2-postponed-Xgl-removed-from-X-org-736743.html "Kernel Log: New Stable kernel, DRI2 postponed, Xgl removed from X.org – 05 August 2008, 10:31")
- [Kernel Log: New Nvidia drivers are still slow, Linux 2.6.26.1 soon](../site/news/item/Kernel-Log-New-Nvidia-drivers-are-still-slow-Linux-2-6-26-1-soon-736723.html "Kernel Log: New Nvidia drivers are still slow, Linux 2.6.26.1 soon – 04 August 2008, 09:07")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
