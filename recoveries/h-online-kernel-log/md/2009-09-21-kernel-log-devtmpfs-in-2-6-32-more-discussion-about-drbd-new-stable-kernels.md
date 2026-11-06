---
title: "Kernel Log - Devtmpfs in 2.6.32, more discussion about DRBD, new stable kernels"
date: 2009-09-21
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-Devtmpfs-in-2-6-32-more-discussion-about-DRBD-new-stable-kernels-812212.html
pages: 1
---

# Kernel Log - Devtmpfs in 2.6.32, more discussion about DRBD, new stable kernels

**Dj Walker-Morgan**

![Kernel Log Penguin](../site/imgs/43/4/1/3/5/9/5/93e8ea3d0acdf147.jpg)

#### by Thorsten Leemhuis

**The development of Linux 2.6.32 is in full swing â€“ although the integration of devtmpfs into the main development branch has caused considerable friction. The integration of DRBD, which already seemed certain, is also being debated again. X Server 7.5 is making progress as the developers release the first RC and several new drivers.**

### 2.6.32 in the making

Linus Torvalds has integrated just under 5,500 commits into the main development branch since the release of [Linux 2.6.31](../site/open/features/The-Next-Round-The-new-features-of-Linux-2-6-31-746619.html "The Next Round – The new features of Linux 2.6.31 â 10 September 2009, 07:33"). The commits already include some of the major new additions to Linux version 2.6.32, which is expected to be released in about ten to twelve weeks â€“ for example a [redeveloped](http://thread.gmane.org/gmane.linux.kernel/888279) writeback infrastructure designed to improve the throughput in SMP systems and the support of Intel's Trusted Execution Technology ([TXT](http://www.intel.com/technology/security/)), which used to be known as LaGrande Technology.

New additions include many mISDN drivers for chips by various vendors as well as several fresh Wi-Fi drivers for the staging area. As expected, the staging area is now also home to [Microsoft's Hyper-V drivers](../site/news/item/Microsoft-GPLs-Linux-virtualisation-drivers-742565.html "Microsoft GPLs Linux virtualisation drivers â 20 July 2009, 17:22"). That they could soon be removed again, as [threatened](../site/open/The-Next-Round-The-new-features-of-Linux-2-6-31--/features/114132/5) by one of the staging branch maintainers, has become less likely: Microsoft's developers [are now active again](http://thread.gmane.org/gmane.linux.kernel/887970), and Sam Ramji [emphasised](../site/news/item/Microsoft-says-We-are-working-on-our-Linux-drivers-770066.html "Microsoft says "We are working on our Linux drivers" â 15 September 2009, 08:48") in a recent interview that Microsoft is putting a lot of work into the drivers.

Con Kolivas' [recently released](../site/news/item/Kernel-Log-Extra-round-for-2-6-31-X-org-7-5-on-the-horizon-staging-area-to-be-cleaned-up-743289.html "Kernel Log – Extra round for 2.6.31, X.org 7.5 on the horizon, staging area to be cleaned up â 08 September 2009, 10:06") BFS (Brain Fuck Scheduler) which was developed independently from the kernel, has had some minor effects on the development of Linux 2.6.32: When running comparison benchmarks, several testers found a problem in a relatively recent section of code in the current kernel scheduler, which prompted the developers to [temporarily deactivate the section](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3f2aa307c4d26b4ed6509d0a79e8254c9e07e921). Numerous further changes have been made to improve the current scheduler's performance ([1](http://thread.gmane.org/gmane.linux.kernel/888423), [2](http://thread.gmane.org/gmane.linux.kernel/891182)).

The"perf sched" [program recently introduced](http://thread.gmane.org/gmane.linux.kernel/891157) by Ingo Molnar is designed to simplify and improve the evaluation of the scheduler's behaviour in future. On a slightly larger scale, Timechart, the graphical analysis program Arjan van de Ven recently [introduced](http://blog.fenrus.org/?p=5), was developed to track down general performance bottlenecks within a Linux system â€“ however, the full set of Timechart features requires [several patches](http://thread.gmane.org/gmane.linux.kernel/891137) which have now been [released upstream](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=10274989fd595db455874fc2c83272fb33f6b27b) and will be included in 2.6.32.

Linus Torvalds has incorporated the devtmpfs feature also known as "Devfs 2.0" into Linux version 2.6.32. Devtmpfs allows the kernel itself to create the device file system usually found at /dev, which reduces the demands on Udev during system start up â€“ and reportedly results in a faster system start, although this is said to be only one of the advantages offered by devtmpfs. Several developers who had previously criticised devtmpfs months ago have now [renewed](http://thread.gmane.org/gmane.linux.kernel/889864/focus%3D890291) their criticism or even [demanded its removal](http://thread.gmane.org/gmane.linux.kernel/890849). Torvalds didn't really comment on the criticised details â€“ but two of his contributions indicate that he doesn't seem to dislike devtmpfs ([1](http://thread.gmane.org/gmane.linux.kernel/890849/focus%3D891147), [2](http://thread.gmane.org/gmane.linux.kernel/890849/focus%3D891239)).

The developers are also arguing about the [expected integration](../site/open/The-Next-Round-The-new-features-of-Linux-2-6-31--/features/114132/5) of [DRBD](http://www.drbd.org/) (Distributed Replicated Block Device), because one of the devtmpfs critics is also [against integrating](http://thread.gmane.org/gmane.linux.network.drbd.devel/953/focus%3D889988) DRBD. However, several of the SUSE developers like [Neil Brown](http://thread.gmane.org/gmane.linux.network.drbd.devel/953/focus%3D891286), who is responsible for the kernel's MD code and the related mdadm tool, have strongly advocated integrating DRBD. Whether the feature will make it into 2.6.32 should become apparent in the next few days, as the merge window, during which Linus Torvalds integrates the majority of changes for the forthcoming version into the main development branch, should close within the week.

### Linux version status

The maintainers of the Linux stable series have recently released versions [2.6.27.34](http://thread.gmane.org/gmane.linux.kernel/889861) and [2.6.30.7](http://thread.gmane.org/gmane.linux.kernel/889869) â€“ with the usual unspecific recommendation that the users of non-distribution kernels should make sure they upgrade to the new versions ("*All users of the 2.6.xx kernel series are very strongly encouraged to upgrade.*").

As usual, the two new versions correct several bugs and offer numerous, mostly minor, improvements. However, they are soon to be obsolete, because their two successors and version 2.6.31.1 are already in progress ([1](http://thread.gmane.org/gmane.linux.kernel/890589), [2](http://thread.gmane.org/gmane.linux.kernel/890602), [3](http://thread.gmane.org/gmane.linux.kernel/890629)). As the comment window closed on Saturday morning, the new versions are expected to be released soon. Greg Kroah-Hartman has indicated that the maintenance of the 2.6.30 series [will soon be discontinued](http://thread.gmane.org/gmane.linux.kernel/877196/focus%3D890353).

Willy Tarreau, who maintains the 2.4 series, has also been far from idle and [released Linux version 2.4.37.6](http://thread.gmane.org/gmane.linux.kernel/888770) to close several security holes. Thomas Gleixner has [released](http://thread.gmane.org/gmane.linux.rt.user/3911/focus%3D5089) version 2.6.31-rt10 â€“ the first [Linux 2.6.31](../site/open/features/The-Next-Round-The-new-features-of-Linux-2-6-31-746619.html "The Next Round – The new features of Linux 2.6.31 â 10 September 2009, 07:33")-based kernel to include the real-time patches from the [RT tree](http://rt.wiki.kernel.org).

### X status

Peter Hutterer has [released](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/779) the first RC of X Server 1.7, which is scheduled to be part of X.org 7.5. He has also [released](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/776) a new version of the "nv" driver for NVIDIA hardware that is suitable for the new X Server. Dave Airlie has provided two new versions of the xf86-video-ati open source driver for Radeon hardware ([1](http://lists.freedesktop.org/archives/xorg-announce/2009-September/001026.html), [2](http://lists.freedesktop.org/archives/xorg-announce/2009-September/001033.html)). The first of them offers a range of [improvements](http://lists.freedesktop.org/archives/xorg-announce/2009-September/001026.html) and supports, for example, recent Radeon models, such as the HDÂ 4770.

AMD has also been active and recently released [version 9.9](http://support.amd.com/us/gpudownload/linux/Pages/radeon_linux.aspx?type=2.4.1&product=2.4.1.3.36%E2%8C%A9=English) of the proprietary Linux graphics drivers. According to the [release notes](http://www2.ati.com/drivers/linux/catalyst_99_linux.pdf)![PDF](../site/icons/file-pdf.gif "PDF document"), new features include full openSUSE 11.1 support and some first support ("*Early Look*") of SLED/SLESÂ 10Â SP3. However, the driver isn't suitable for [Linux version 2.6.31](../site/open/features/The-Next-Round-The-new-features-of-Linux-2-6-31-746619.html "The Next Round – The new features of Linux 2.6.31 â 10 September 2009, 07:33") â€“ this version will apparently become available with version 9.10 of the driver, which is scheduled for release next month.

### In Brief

- The article called "[Reduce Linux power consumption, Part 1: The CPUfreq subsystem](http://www.ibm.com/developerworks/linux/library/l-cpufreq-1/index.html)" at IBM developerWorks provides some background information on how the kernel utilises the power saving techniques offered by modern CPUs.

<!-- -->

- [In his blog](http://anholt.livejournal.com/41522.html), Intel developer Eric Anholt gives a overview of the most recent improvements to the code of the Intel graphics drivers for Linux.

<!-- -->

- NVIDIA developer Aaron Plattner has released the [vdpauinfo 0.0.6](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/781) and [libvdpau 0.2](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/780) open source programs. The latter is a software library which used to be shipped together with the proprietary graphics driver. It works with the Video Decode and Presentation API for Unix (VDPAU) introduced [at the end of last year](../site/news/item/Linux-API-harnesses-GeForce-GPU-s-HD-video-capabilities-738137.html "Linux API harnesses GeForce GPU's HD video capabilities â 17 November 2008, 08:54") and allows the HD video capabilities of modern GeForce GPUs to be utilised under Linux.

<!-- -->

- Christoph Hellwig provides an overview of the latest XFS file system developments in his "[XFS status update for August 2009](http://thread.gmane.org/gmane.comp.file-systems.xfs.general/30434)."

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the Kernel Log at The H Open Source:*

- [The Next Round â€“ The new features of Linux 2.6.31](../site/open/features/The-Next-Round-The-new-features-of-Linux-2-6-31-746619.html "The Next Round – The new features of Linux 2.6.31 â 10 September 2009, 07:33")
- [Kernel Log â€“ Extra round for 2.6.31, X.org 7.5 on the horizon, staging area to be cleaned up](../site/news/item/Kernel-Log-Extra-round-for-2-6-31-X-org-7-5-on-the-horizon-staging-area-to-be-cleaned-up-743289.html "Kernel Log – Extra round for 2.6.31, X.org 7.5 on the horizon, staging area to be cleaned up â 08 September 2009, 10:06")
- [Kernel Log - Coming in 2.6.31 - Part 5: CUSE, USB 3.0, FireWire networking and the rest](../site/news/item/Kernel-Log-Coming-in-2-6-31-Part-5-CUSE-USB-3-0-FireWire-networking-and-the-rest-743173.html "Kernel Log: Coming in 2.6.31 - Part 5: CUSE, USB 3.0, FireWire networking and the rest â 31 August 2009, 08:02")
- [Kernel Log - Coming in 2.6.31 â€“ Part 4: Tracing, architecture, virtualisation](../site/news/item/Kernel-Log-Coming-in-2-6-31-Part-4-Tracing-architecture-virtualisation-743099.html "Kernel Log - Coming in 2.6.31 – Part 4: Tracing, architecture, virtualisation â 26 August 2009, 10:36")
- [Kernel Log â€“ Coming in 2.6.31 - Part 3: Storage and file systems](../site/news/item/Kernel-Log-Coming-in-2-6-31-Part-3-Storage-and-file-systems-742967.html "Kernel Log – Coming in 2.6.31 - Part 3: Storage and file systems â 17 August 2009, 09:48")
- [Kernel Log - Coming in 2.6.31 - Part 2: Graphics, audio and video](../site/news/item/Kernel-Log-Coming-in-2-6-31-Part-2-Graphics-audio-and-video-742867.html "Kernel Log - Coming in 2.6.31 - Part 2: Graphics, audio and video â 07 August 2009, 15:53")
- [Kernel Log: X server 1.7 delayed; Compiz runs on newer Radeon GPUs; DRBD in kernel soon](../site/news/item/Kernel-Log-X-server-1-7-delayed-Compiz-runs-on-newer-Radeon-GPUs-DRBD-in-kernel-soon-742829.html "Kernel Log: X server 1.7 delayed; Compiz runs on newer Radeon GPUs; DRBD in kernel soon â 05 August 2009, 16:55")

*Older Kernel Logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/).*

([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
