---
title: "Kernel Log: Linux 2.6.33 enters test phase"
date: 2009-12-21
author: "Chris von Eitzen"
source: http://www.h-online.com/open/news/item/Kernel-Log-Linux-2-6-33-enters-test-phase-890581.html
pages: 1
---

# Kernel Log: Linux 2.6.33 enters test phase

**Chris von Eitzen**

#### ![Kernel Log Tux](../site/imgs/43/4/5/9/8/2/8/KL.jpg-4677d3004996dcc3.jpeg) by Thorsten Leemhuis

**With the end of the next kernel version's main development phase, the most important new features of Linux 2.6.33 have been determined: DRBD, Nouveau, support of the Trim ATA command and a bandwidth controller for block devices. The developers have also improved the Radeon drivers and the support of Intel Wi-Fi chips. New stable kernels also fix a vulnerability in the code of Ext4, but will shortly be superseded by even more current versions.**

Exactly two weeks after [releasing Linux 2.6.32](../site/open/features/What-s-new-in-Linux-2-6-32-872271.html "What's new in Linux 2.6.32 – 03 December 2009, 08:22"), Linus Torvalds has now [released](http://thread.gmane.org/gmane.linux.kernel/929499) the first release candidate (RC) of Linux 2.6.33, closing the "merge window" phase of the development cycle during which the majority of changes for the next Linux version are integrated into the main Linux development branch. As previously reported, the developers have integrated a driver for [recent Ralink Wi-Fi chips](../site/news/item/Kernel-Log-New-stable-kernels-2-6-33-with-DRBD-and-RT2800PCI-883212.html "Kernel Log: New stable kernels, 2.6.33 with DRBD and RT2800PCI – 11 December 2009, 13:33"), the DRBD replication module and the kernel-side parts of the [nouveau open source graphics driver](../site/news/item/Kernel-Log-Linux-2-6-33-to-include-NVIDIA-graphics-driver-nouveau-885001.html "Kernel Log: Linux 2.6.33 to include NVIDIA graphics driver nouveau – 14 December 2009, 12:20") into the kernel.

However, these are only three particularly prominent improvements. For instance, the Libata subsystem now supports the [Trim ATA](http://en.wikipedia.org/wiki/TRIM_%28SSD_command%29) command, which optimises SSD operation. To take full advantage of this, other parts of the kernel have to inform the storage subsystem about newly disallocated areas – the [Btrfs file system](../site/open/features/The-Btrfs-file-system-746597.html "The Btrfs file system – 17 July 2009, 08:55") has already been capable of this since version 2.6.32, and the developers have now added the required code for [Ext4](../site/open/features/The-Ext4-Linux-file-system-746579.html "The Ext4 Linux file system – 29 May 2009, 08:13"). However, this code is still classified as experimental and is not used in the standard configuration.

Other changes include a new graphics driver which supports KMS for the virtual graphics chip of VMware hosts and an SCSI driver which addresses the virtual Host Bus Adapters (HBA) of some VMware products. Another addition to the kernel are the WiMax drivers for Intel's series 6050 Wi-Fi/WiMAX chips and the "Intel Wireless MultiCom 3200 top driver" for a Wi-Fi chip with GPS, Bluetooth, Wi-Fi and WiMAX support. The kernel's DRM and KMS code for Radeon graphics chips now supports IRQs, DisplayPort and audio output via HDMI.

After much to-ing and fro-ing, the "blkio controller cgroup interface" has finally made it into the kernel. It allows the maximum throughput of individual processes and groups of processes to be limited. As expected, the drivers for Google's Android have been kicked out of the staging area because nobody has been looking after them.

Now that the "merge window" has been closed, the kernel development enters a test phase of usually ten or eleven weeks during which the developers tend to release a new RC every week. Apart from picking up some stragglers likely to be submitted over the next few days and the occasional individual new driver, this phase mainly serves for making minor corrections and improvements to fix any flaws that are found – this way, the developers try to prevent major changes from introducing new problems.

### Linux version status

The maintainers of the Linux stable series have recently released versions [2.6.31.8](http://thread.gmane.org/gmane.linux.kernel/927139) and [2.6.32.1](http://thread.gmane.org/gmane.linux.kernel/927141). As usual, these versions mainly offer minor corrections and improvements – many of them affecting the code for the Ext4 file system. The latter also fix the [recently disclosed](../site/news/item/Linux-kernel-vulnerabilities-closed-882270.html "Linux kernel vulnerabilities closed – 10 December 2009, 12:06") [CVE-2009-1298](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-1298) vulnerability in Ext4.

Meanwhile, Greg Kroah-Hartman – one of the maintainers of the stable kernel series – is already preparing versions [2.6.27.42](http://thread.gmane.org/gmane.linux.kernel/928704), [2.6.31.9](http://thread.gmane.org/gmane.linux.kernel/928819) and [2.6.32.2](http://thread.gmane.org/gmane.linux.kernel/928850). With over 150 corrections, the latter is one of the stable kernels that offer a quite a large number of changes. As the time window for submitting comments about the planned changes is scheduled to close before the weekend, these three new Linux versions are likely to be released in the near future.

Those who'd like to know how Greg Kroah-Hartman incorporates changes into the stable series can find [a video demonstrating the process](http://www.kroah.com/log/linux/how-i-do-stable.html) in the developer's blog.

### In brief

**Kernel**

- Christoph Hellwig provides an overview of the latest XFS file system developments in his "[XFS status update for November 2009](http://thread.gmane.org/gmane.linux.kernel/925973)".
- Linus Torvalds recently explained his basic process and timing when naming a kernel [in an email](http://thread.gmane.org/gmane.linux.kernel/925822) to the LKML. This was triggered by the question why several kernels in a row have been called the "Man-Eating Seals of Antiquity". However, Torvalds' email is somewhat difficult to read, because the Linux Kernel Mailing List's overly ambitious spam filter has discarded some of the thread's earlier postings.
- Ben Skeggs has started [developing open source code](http://thread.gmane.org/gmane.comp.freedesktop.xorg.nouveau/4211) to replace the ["Voodoo code" or "firmware"](http://lwn.net/Articles/366266/) [parts](http://cgit.freedesktop.org/nouveau/linux-2.6/tree/firmware/nouveau) the [Nouveau driver currently relies on](../site/news/item/Kernel-Log-Linux-2-6-33-to-include-NVIDIA-graphics-driver-nouveau-885001.html "Kernel Log: Linux 2.6.33 to include NVIDIA graphics driver nouveau – 14 December 2009, 12:20"). The whole thing is experimental, however, and currently only works with GeForce generation 6 and 7 chips.

**Kernel environment ("plumbing layer") and userland drivers**

- The [Alsa developers](http://www.alsa-project.org/) have [released](http://www.mail-archive.com/alsa-announce@lists.sourceforge.net/msg00036.html) version 1.0.22 of the Alsa components – find a list of all the changes on a [page in the project's wiki](http://www.alsa-project.org/main/index.php/Changes_v1.0.21_v1.0.22).
- The developers of the [Hplip project](http://hplipopensource.com/) have released version 3.9.12 of the Hplip drivers for printers and multi-function devices by HP. [According to the release notes](http://sourceforge.net/news/?group_id=149981&id=280190), supported devices now include various devices of the Color Laserjet and Designjet ranges.

**Graphics**

- AMD has made version 9.12 of the Catalyst drivers for Linux, also known as fglrx, available [to download](http://support.amd.com/us/gpudownload/). The [release notes](http://www2.ati.com/drivers/linux/catalyst_912_linux.pdf) mention several minor improvements and corrections, but they say nothing about the support of the series 1.7 X Servers available since the end of September – it is therefore likely that, like their predecessors, the new Catalyst drivers will not work with this series.
- Aaron Plattner has [released](http://thread.gmane.org/gmane.comp.freedesktop.xorg/41725) version 2.1.16 of the "nv" (its full name is actually "xf86-video-nv") X.org graphics driver, which is predominantly maintained by Nvidia employees. Among others, it supports numerous GeForce graphics cards introduced in the past few months – including the GTX 260M, 275, 280M and 295 models.
- Dave Airlie has [released](http://airlied.livejournal.com/69648.html) version 1.6 of the radeontool program.
- In his blog posting entitled "[The \[Xx\](\[Ff\](ree)?\[86\]\|\[\\\]?\[Oo\]rg) glossary](http://who-t.blogspot.com/2009/12/xxffree86oorg-glossary.html)", Peter Hutterer tries to clarify the terms and relationships between X, X.org, Xorg, XFree86, xf86 and several other related terms.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the Kernel Log at The H Open Source:*

- [Kernel Log: Linux 2.6.33 to include Nvidia graphics driver nouveau](../site/news/item/Kernel-Log-Linux-2-6-33-to-include-NVIDIA-graphics-driver-nouveau-885001.html "Kernel Log: Linux 2.6.33 to include NVIDIA graphics driver nouveau – 14 December 2009, 12:20")
- [Kernel Log: New stable kernels, 2.6.33 with DRBD and RT2800PCI](../site/news/item/Kernel-Log-New-stable-kernels-2-6-33-with-DRBD-and-RT2800PCI-883212.html "Kernel Log: New stable kernels, 2.6.33 with DRBD and RT2800PCI – 11 December 2009, 13:33")
- [What's new in Linux 2.6.32](../site/open/features/What-s-new-in-Linux-2-6-32-872271.html "What's new in Linux 2.6.32 – 03 December 2009, 08:22")
- [Kernel Log: Coming in 2.6.32 (Part 6): Infrastructure](../site/news/item/Kernel-Log-Coming-in-2-6-32-Part-6-Infrastructure-869973.html "Kernel Log: Coming in 2.6.32 (Part 6): Infrastructure – 27 November 2009, 17:12")
- [Kernel Log: Coming in 2.6.32 (Part 5) - Architecture code, memory management, virtualisation and tracing](../site/news/item/Kernel-Log-Coming-in-2-6-32-Part-5-Architecture-code-memory-management-virtualisation-and-tracing-870357.html "Kernel Log: Coming in 2.6.32 (Part 5) - Architecture code, memory management, virtualisation and tracing – 27 November 2009, 10:10")
- [Kernel Log: Coming in 2.6.32 (Part 4) - Drivers](../site/news/item/Kernel-Log-Coming-in-2-6-32-Part-4-Drivers-868263.html "Kernel Log: Coming in 2.6.32 (Part 4) - Drivers – 25 November 2009, 14:03")

*Older Kernel Logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/). New editions of Kernel Logs are also mentioned on [Identi.ca](http://identi.ca/kernellog2) and [Twitter](http://twitter.com/kernellog2) via "@kernellog2". The Kernel Log author also posts updates about various Kernel Log topics on [Identi.ca](http://identi.ca/kernellogauthor) and [Twitter](http://twitter.com/kernellogauthor) via "@kernellogauthor".* ([thl](mailto:thl@ct.heise.de)/c't)

([crve](mailto:crve@h-online.com "Chris von Eitzen "))
