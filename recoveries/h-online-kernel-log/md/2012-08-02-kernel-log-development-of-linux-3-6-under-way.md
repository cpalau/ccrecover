---
title: "Kernel Log: Development of Linux 3.6 under way"
date: 2012-08-02
author: "Thorsten Leemhuis"
source: http://www.h-online.com/open/features/Kernel-Log-Development-of-Linux-3-6-under-way-1657742.html
pages: 1
---

# Kernel Log: Development of Linux 3.6 under way

**Thorsten Leemhuis**

**The kernel developers have added the VFIO userspace driver framework and a hybrid standby option to Linux 3.6. The 64-bit ARM code will be called "arm64" after all. The widely used software collection util-linux has been extended to include a range of new tools.**

Less than 24 hours after [releasing](../site/open/features/What-s-new-in-Linux-3-5-1637461.html "What's new in Linux 3.5 – 22 July 2012") Linux 3.5, Linus Torvalds integrated the first changes for Linux 3.6 into the main development branch of Linux. [As expected](../site/open/features/What-s-new-in-Linux-3-5-1637461.html?anchor=summary), the newly added features include support for IOMMU (Input/Output Memory Management Unit) groups and the VFIO (Virtual Function I/O) userspace driver framework that is based on it.

The kernel developers have [also added](http://git.kernel.org/linus/62c552ccc3eda1198632a4f344aa32623d226bab) a "suspend to both" feature that makes hybrid standby possible. This feature allows memory contents to be buffered in RAM and on a system's storage device while the system is sleeping. Normally, the computer will then use the data in memory and resume just like it normally would from Suspend to RAM; in case of a power cut, however, the system will retrieve the previous RAM contents from the drive as it would do when resuming from Suspend to Disk. This allows users to always find their working environment as it was before the system went to sleep – even if, for instance, the notebook battery had lost all of its power in the interim.

The merge window phase during which Torvalds adds the majority of important new features to Linux 3.6 will end this weekend; it will be followed by a stabilisation phase that, for recent releases, lasted about seven or eight weeks.

### ![Kernel Log penguin](../site/open/imgs/45/8/9/8/3/1/8/Kernel_Log_Penguin-4677d3004996dcc3.jpeg) Linux kernel

- Stable and long-term kernel versions [Linux 3.2.24](http://thread.gmane.org/gmane.linux.kernel/1333347) and [Linux 3.4.7](http://thread.gmane.org/gmane.linux.kernel/1335133) have been released in the past few days; kernel version [3.0.39](http://thread.gmane.org/gmane.linux.kernel/1336505) was also released while [3.2.25](http://thread.gmane.org/gmane.linux.kernel/1335483) is currently in preparation. The latter two kernel versions incorporate a number of performance optimisations which, in the past, would not have been allowed to be introduced into long-term kernel releases. In order to integrate changes like these, the developers recently [modified](../site/open/features/Kernel-Log-Coming-in-3-5-Part-5-Infrastructure-1635017.html "Kernel Log: Coming in 3.5 (Part 5) - Infrastructure – 13 July 2012") the rules governing the inclusion of patches in stable and long-term kernels.

<!-- -->

- Christoph Hellwig mentions some of the most recent XFS filesystem developments in his "[XFS status update for June 2012](http://thread.gmane.org/gmane.linux.kernel/1332314)".

<!-- -->

- As [reported](http://www.theregister.co.uk/2012/07/26/andre_hedrick/?2) by *The Register* and other sites, former kernel developer Andre Hedrick killed himself. About 10 years ago, Hedrick maintained the Linux kernel's IDE drivers for quite some time. Jeff Garzik, who developed the libata subsystem that is the basis of the SATA and PATA/IDE drivers of modern Linux distributions, [calls](http://thread.gmane.org/gmane.linux.kernel/1330661/focus%3D52498) Hedrick "one of the grandfathers of libata" for having taught him "a lot about ATA"; Garzik also [posted](http://article.gmane.org/gmane.linux.ide/52517) an obituary to the LKML. A decade ago, Hedrick was among the important kernel developers, though he hadn't directly contributed to the Linux kernel for many years.

<!-- -->

- The [klang.eudyptula.org](http://klang.eudyptula.org/) web site presents the concept of KLANG (Kernel Level Audio Next Generation), an audio system for Linux and FreeBSD in which the kernel handles a greater number of audio processing tasks. According to the main project page, KLANG is designed to offer minimal latencies and is currently in development; however, the project's [news section](http://klang.eudyptula.org/news/) puts a damper on any expectations by saying that the web site is intended as a placeholder, and that KLANG has not been officially announced yet. Wolfgang Draxinger, aka "datenwolf", is thought to be behind the project.

### Graphics

- Intel has [released](http://lists.x.org/archives/xorg-announce/2012-July/002044.html) version 2.20.2 of its drivers for X.org's X Server; it fixes a nine-month-old bug that caused HD2500 graphics cores (Ivy Bridge GT1 systems) to crash.

<!-- -->

- A [modification](http://thread.gmane.org/gmane.comp.video.dri.devel/71815/focus%3D71912) that was introduced with Linux 3.5 has caused power consumption to increase on SCSI subsystem maintainer James Bottomley's [antiquated](http://thread.gmane.org/gmane.comp.video.dri.devel/71815/focus%3D71830) Thinkpad x220i; however, there is currently no evidence that the problem also affects modern hardware. **Update 02-08-12:** Some of the information supplied by Bottomley appears to have been incorrect. Most of the details provided indicate that his Thinkpad features an Intel Sandy Bridge processor, and is not a antiquated laptop with an Intel 845 chipset, as he had once mentioned.

### Userland

- With the [first RC](http://thread.gmane.org/gmane.linux.file-systems/66273) of the util-linux 2.22 tool collection, the blkid, findmnt, mount, swapon and umount programs have been extended to include code that allows them to find storage devices by their labels as well as by their UUIDs (Universally Unique Identifiers). The Dmesg program now supports the [changes to the logging mechanisms](../site/open/features/Kernel-Log-Coming-in-3-5-Part-5-Infrastructure-1635017.html "Kernel Log: Coming in 3.5 (Part 5) - Infrastructure – 13 July 2012") that were integrated in Linux 3.5; it uses these mechanisms to offer a "follow" feature which, similar to "tail -f", waits for new kernel messages and outputs them as they arrive. The developers have also integrated the eject, su, sulogin and utmpdumpa programs into the tool collection. Util-linux is included in all mainstream distributions.

<!-- -->

- Junio C. Hamano has [released](http://git-blame.blogspot.de/2012/07/git-1712-rc1.html) the first RC of Git 1.7.12.

### LKML discussions

- Citrix developer Stefano Stabellini has submitted various kernel patches to the LKML [for review](http://thread.gmane.org/gmane.linux.kernel/1333732); the patches extend the Linux Xen code to support the virtualisation extensions that are available with the Cortex A7 and A15 cores from the ARMv7-A family. In early July, Virtual Open Systems developer Christoffer Dall sent the ninth revision of the KVM patches to support these ARM virtualisation features to the KVM developers [for review](http://thread.gmane.org/gmane.comp.emulators.kvm.devel/93514/); a patch that provides the required basics was recently [added to](http://git.kernel.org/linus/a1e4ccb990447df0fe83d164d9a7bc2e6c4b7db7) Linux 3.6.

<!-- -->

- [The latest planning notes](http://thread.gmane.org/gmane.linux.kernel/1324121/focus%3D1333603) suggest that the subdirectory containing the Linux code to support the 64-bit ARM architecture is to be called "arm64". The [original name](../site/news/item/64-bit-ARM-support-for-Linux-AArch64-1634610.html "64-bit ARM support for Linux AArch64 – 09 July 2012"), Aarch64, was considered to be too bulky and cryptic by some developers.

*Further background information about the developments in the Linux kernel area can be found using [the search function](../site/search/?sort=d;rm=search;mediatype=3;q=kernel-log) at [The H Open Source](../site/open/). Information about previous Linux kernel releases can be found in [The H's Linux Kernel History](../site/open/features/The-H-s-Linux-Kernel-History-1221120.html "The H's Linux Kernel History – 15 July 2011"). New editions of Kernel Logs are also mentioned on [Identi.ca](http://identi.ca/kernellog2) and [Twitter](http://twitter.com/#!/kernellog2) by @kernellog2. The Kernel Log author also posts updates about various topics on [Identi.ca](http://identi.ca/kernellogauthor) and [Twitter](http://twitter.com/#!/kernellogauthor) as @kernellogauthor.*
