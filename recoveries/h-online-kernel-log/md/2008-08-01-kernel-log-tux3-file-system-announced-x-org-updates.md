---
title: "Kernel Log : Tux3 file system announced, X.org updates"
date: 2008-08-01
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-Tux3-file-system-announced-X-org-updates-736707.html
pages: 1
---

# Kernel Log : Tux3 file system announced, X.org updates

*In Brief*

**Dj Walker-Morgan**

Kernel developer of many years, Daniel Phillips posted [several](http://thread.gmane.org/gmane.linux.file-systems/24830) [emails](http://thread.gmane.org/gmane.os.solaris.opensolaris.zfs/17876) concerning file system design, then announced he was planning to take these ideas and apply them to the design and development of [Tux3](http://tux3.org/), although there is no currently functioning Tux 3 source code. The [Tux3 announcement](http://thread.gmane.org/gmane.linux.file-systems/24998) also discusses the details and differences of existing file systems, but Phillips has had no response to his posting. It will be seen in time whether Phillips' Tux3 has any more success over his predecessor project, Tux2, which was never published due to [patent problems](http://ussg.iu.edu/hypermail/linux/kernel/0010.0/0343.html).

[Btrfs](http://btrfs.wiki.kernel.org/index.php/Main_Page) already exists and, like Tux3, offers some of the features of the Solaris ZFS file system for addressing the limitations of current file systems. This is in addition to the quite young and not completely finished Ext4, successor to the widespread Ext3 file system. Btrfs is still in a early development stage, but compared with the only vaguely outlined Tux3, it's lengths ahead; started by Oracle developer Chris Mason, Btrfs already has numerous developers and companies supporting it.

------------------------------------------------------------------------

Originally, the X Window System version 7.4 was planned to be released by X.org at the end of April, but the developers have been waiting on the release of Mesa 7.1. As a foretaste of the next release, X.org have released a preview version of xorg-server 1.4.99.906, the server which will be in 7.4. This, from the outside, may appear to be chaotic release management of X.org, but it could resolve itself at the [X Developers Summit (XDS) which is being held at the start of September in Edinburgh](http://www.x.org/wiki/Events/XDS2008).

The developers of the X.org graphics driver for Intel have released [version 2.4.0](http://lists.freedesktop.org/archives/xorg-announce/2008-July/000621.html) which now supports the Intel Series 4 chip-sets (G43, G45 and co.), displays connected using HDMI and improved rendering performance on the 965 chipset. Meanwhile, one of the developers of the Intel graphics drivers gave a [status report](http://virtuousgeek.org/blog/index.php/2008/07/22/waiting_for_vblank) on working on reducing vblank interrupts to save power of notebooks.

AMD has also released a parser for the [ATOM BIOS](http://lists.freedesktop.org/archives/xorg/2008-July/037526.html) which should make development of Linux graphics drivers which do kernel based mode-setting (kms) [easier](http://tirdc.livejournal.com/22940.html). An rudimentary version that works with cards such as the Radeon X1000 was announced by the developer of the developer of the Radeon driver. RadeonHD developer Luc Verhaegen explained in his blog, [the advantages of a new branch](http://libv.livejournal.com/16709.html) of the RadeonHD driver which supports Command Submission (CS).

------------------------------------------------------------------------

Jonathan Corber, kernel developer and manager of LWN.net, released several long documents [as a patch to the Linux documentation](http://thread.gmane.org/gmane.linux.kernel/713492) which describe in detail how the Linux kernel development process works. He also explains why the framework is important for programmers and why programmers should bring all improvements into the main development branch. It also covers what is important when submitting a patch. This process was also described by Andi Kleen in his lecture [*On submitting kernel patches*](http://ols.fedoraproject.org/OLS/Reprints-2008/kleen-reprint.pdf) â€“ one of the many useful presentations from [Ottawa Linux Symposium 2008](../site/open/features/In-depth-insights-Linux-information-from-the-OLS-746494.html "In-depth insights – Linux information from the OLS â 31 July 2008, 12:43").

------------------------------------------------------------------------

## In Brief

- File system expert Valerie (Val) Henson is becoming a part time employee at Red Hat and talks about what she'll be doing there [in her blog](http://valhenson.livejournal.com/20439.html).
- Linus Torvalds talks about his [linux-next](http://thread.gmane.org/gmane.linux.kernel/713115/focus%3D713407) experience since using it for 2.6.27-rc1.
- IBM DeveloperWorks have published an [article](http://www.ibm.com/developerworks/linux/library/l-lkm/index.html) on how loadable kernel modules work.
- The main development branch has had [Oprofile support patched](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4b9f12a3779c548b68bc9af7d94030868ad3aa1b) ready for Intel's [Nehalam](http://en.wikipedia.org/wiki/Nehalem_%28microarchitecture%29) processors to arrive. Adding support for the XSAVE and XRSTOR in the E0 stepping series of Core 2 Duo E8000, Core 2 Quad Q9000 and Intel Xeon 3000 is also [in progress](http://thread.gmane.org/gmane.linux.kernel/713419/).
- An AMD developer has introduced [AMD microcode patch loading support](http://thread.gmane.org/gmane.linux.kernel/711795), refactoring the code into multiple modules to allow Intel microcode patch loading to live alongside it.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise Open Source:*

- [Kernel Log: 2.6.25.13 corrects a vulnerability, problems with ACPI](../site/news/item/Kernel-log-2-6-25-13-corrects-a-vulnerability-problems-with-ACPI-736703.html "Kernel log: 2.6.25.13 corrects a vulnerability, problems with ACPI â 31 July 2008, 14:42")
- [Kernel Log: First release candidate concludes the hot development phase of 2.6.27](../site/news/item/Kernel-Log-First-release-candidate-concludes-the-hot-development-phase-of-2-6-27-736695.html "Kernel Log: First release candidate concludes the hot development phase of 2.6.27 â 31 July 2008, 12:23")
- Kernel Log: Practical Practices - Ottawa Linux Symposium Notes
- [Kernel Log: Centrino 2 WLAN driver iwl 5000 and webcam driver gscpa in Linux 2.6.27](../site/news/item/Kernel-Log-Centrino-2-WiFi-driver-iwl-5000-and-webcam-driver-gscpa-in-Linux-2-6-27-736569.html "Kernel Log: Centrino 2 WiFi driver iwl 5000 and webcam driver gscpa in Linux 2.6.27 â 23 July 2008, 16:46")
- [Kernel Log: ath9k driver for new Atheros WLAN chips, discussions of Nvidia drivers](../site/news/item/Kernel-log-ath9k-driver-for-new-Atheros-WLAN-chips-discussions-of-Nvidia-drivers-736563.html "Kernel log: ath9k driver for new Atheros WLAN chips, discussions of Nvidia drivers â 22 July 2008, 15:48")
- [Kernel Log: No unstable series; Linux 2008.7, dealing with security fixes](../site/news/item/Kernel-Log-No-unstable-series-Linux-2008-7-dealing-with-security-fixes-736557.html "Kernel Log: No unstable series; Linux 2008.7; dealing with security fixes â 22 July 2008, 01:47")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).*

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
