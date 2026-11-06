---
title: "Kernel Log: Ath9k driver for Atheros Wifi in 2.6.27; reading material and videos for Linux experts"
date: 2008-08-11
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-Ath9k-driver-for-Atheros-Wifi-in-2-6-27-reading-material-and-videos-for-Linux-experts-736829.html
pages: 1
---

# Kernel Log: Ath9k driver for Atheros Wifi in 2.6.27; reading material and videos for Linux experts

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/3/6/0/2/93e8ea3d0acdf147.jpg) How quickly time can pass; three weeks after Atheros developer Luis "mcgrof" Rodriguez publically presented the [ath9k](http://wireless.kernel.org/en/users/Drivers/ath9k) Wifi driver for the [first](http://thread.gmane.org/gmane.linux.kernel.wireless.general/18019) [time](../site/news/item/Kernel-log-ath9k-driver-for-new-Atheros-WLAN-chips-discussions-of-Nvidia-drivers-736563.html "Kernel log: ath9k driver for new Atheros WLAN chips, discussions of Nvidia drivers â 22 July 2008, 15:48"), the driver for the Atheros draft-N supporting chips has [been included](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f078f209704849c86bd43c0beccfc1f410ed1c66) in the main development branch of the Linux kernel. Linux 2.6.27, due around the end of September or early October, will support the Atheros Wifi chips, AR5418+AR5133, AR5416+AR5133, AR5316+AR2133, AR9160, AR9280 and AR9821 as standard.

These chipsets are found in newer notebooks and are used to make PCI/PCIe cards and PC-Cards found in products from Belkin, Linksys, NEC and Netgear according to the [drivers web page](http://wireless.kernel.org/en/users/Drivers/ath9k#ProductsintheretailmarketcontainingAtherosAR5008-basedsolutions). So far the ath9k driver only works in client mode (STA/station mode) but the [ToDo list](http://wireless.kernel.org/en/users/Drivers/ath9k#TODO) shows the developers already at work on mesh and AP support. Constant definitions and comments in the source code suggest that to help debugging, in the long term, support for Wireshark is planned.

------------------------------------------------------------------------

There has been a lot of background material to read for interested Linuxers with the [papers from the Ottawa Linux Symposium 2008](../site/open/features/In-depth-insights-Linux-information-from-the-OLS-746494.html "In-depth insights – Linux information from the OLS â 31 July 2008, 12:43") and now there is even more to read. The ACM Special Interest Group on Operating Systems, [SIGOPS](http://www.sigops.org/), [announced](http://thread.gmane.org/gmane.linux.kernel/718152) on the Linux Kernel Mailing List, LKML, that their [Operating Systems Review](http://www.sigops.org/osr.html) contains a [dozen](http://portal.acm.org/toc.cfm?id=1400097) articles on various Linux issues.

The article *[Towards achieving fairness in the Linux scheduler](http://portal.acm.org/citation.cfm?id=1400097.1400102)* describes the internals of Linux 2.6.23, where the Completely Fair Scheduler was introduced, and how it allocates CPU time to running processes and threads. *[On the design of a new Linux readahead framework](http://portal.acm.org/citation.cfm?id=1400097.1400106)* looks at the techniques used in the preliminary reading of disks within the kernel. Rusty Russell, in *[virtio: towards a de-facto standard for virtual I/O devices](http://portal.acm.org/citation.cfm?id=1400097.1400108)*, looks at virtio's method of unifying and handling the different drivers of the eight virtualisation solutions available for Linux. In *[Extending futex for kernel to user notification](http://portal.acm.org/citation.cfm?id=1400097.1400100)*, University of Frieberg employees describe their work in creating user level notification, while in *[I/O resource management through system call scheduling](http://portal.acm.org/citation.cfm?id=1400097.1400103)*, University of Salzburg researchers look at new ways of managing I/O resources.

[Free Electrons'](http://lwn.net/Articles/293318/) Michael Opdenacker and Thomas Peazzoni have made available, under a Creative Commons license, [thirty videos](http://free-electrons.com/news/news-2008-08-08) of the lectures at the Ottowa Linux Symposium. The videos, encoded in Theora and OGG Vorbis format, are available at the [Free Electrons' conference site](http://free-electrons.com/community/videos/conferences/). Among them are some presentations for "normal" Linux users such as *Tux on the Air: State of Linux Wireless Networking* with Red Hat developer John W. Linville, *Suspend to RAM in Linux: State of the Union* with Intels Len Brown and Rafael Wysocki, and the keynote *The Kernel: 10 Years in Review*, with Intels Matthew Wilcox.

**In Brief**

- Rafael J. Wysocki has put together a [list of reported regressions](http://thread.gmane.org/gmane.linux.kernel.kernel-testers/645) from Linux 2.6.26 that occur in 2.6.27-rc1.
- Jesse Barnes, published a [report in his blog](http://virtuousgeek.org/blog/index.php/2008/08/09/xf86_video_intel_2_5_merge_status) on the development of the X.org Intel graphics driver. The main development branch of Mesa already contains the infrastructure for the next version of GEM and the developers are looking to have 2.5 included as part of Linux 2.6.28.
- Ext file system developer Theodore Ts'o talks [in his blog](http://tytso.livejournal.com/57711.html) about how fsck in ext4 is faster than ext3, even though developers had not explicitly worked on the issue.
- RadeonHD developer Matthais Hopf has [reported on his progress](http://emmes.livejournal.com/1783.html) in enabling 3D support for the R600 GPUs as used in the Radeon series 2000 and 3000 cards.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: Btrfs 0.16 released, new stable kernels released, Wifi drivers for 2.6.27 merged](../site/news/item/Kernel-Log-Btrfs-0-16-released-new-stable-kernels-released-Wifi-drivers-for-2-6-27-merged-736815.html "Kernel Log: Btrfs 0.16 released, new stable kernels released, Wifi drivers for 2.6.27 merged â 08 August 2008, 14:32")
- [Kernel Log: New Stable kernel, DRI2 postponed, Xgl removed from X.org](../site/news/item/Kernel-Log-New-Stable-kernel-DRI2-postponed-Xgl-removed-from-X-org-736743.html "Kernel Log: New Stable kernel, DRI2 postponed, Xgl removed from X.org â 05 August 2008, 10:31")
- [Kernel Log: New Nvidia drivers are still slow, Linux 2.6.26.1 soon](../site/news/item/Kernel-Log-New-Nvidia-drivers-are-still-slow-Linux-2-6-26-1-soon-736723.html "Kernel Log: New Nvidia drivers are still slow, Linux 2.6.26.1 soon â 04 August 2008, 09:07")
- [Kernel Log : Tux3 file system announced, X.org updates](../site/news/item/Kernel-Log-Tux3-file-system-announced-X-org-updates-736707.html "Kernel Log : Tux3 file system announced, X.org updates â 01 August 2008, 09:17")
- [Kernel Log: 2.6.25.13 corrects a vulnerability, problems with ACPI](../site/news/item/Kernel-log-2-6-25-13-corrects-a-vulnerability-problems-with-ACPI-736703.html "Kernel log: 2.6.25.13 corrects a vulnerability, problems with ACPI â 31 July 2008, 14:42")
- [Kernel Log: First release candidate concludes the hot development phase of 2.6.27](../site/news/item/Kernel-Log-First-release-candidate-concludes-the-hot-development-phase-of-2-6-27-736695.html "Kernel Log: First release candidate concludes the hot development phase of 2.6.27 â 31 July 2008, 12:23")
- Kernel Log: Practical Practices - Ottawa Linux Symposium Notes

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
