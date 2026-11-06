---
title: "Kernel Log - Main development phase of Linux 2.6.32 completed"
date: 2009-09-28
author:
source: http://www.h-online.com/open/news/item/Kernel-Log-Main-development-phase-of-Linux-2-6-32-completed-812328.html
pages: 1
---

# Kernel Log - Main development phase of Linux 2.6.32 completed

![Kernel Log Penguin](../site/imgs/43/4/1/3/7/0/7/93e8ea3d0acdf147.jpg)

#### by Thorsten Leemhuis

With the [first release candidate](http://thread.gmane.org/gmane.linux.kernel/895032) of Linux 2.6.32, last night, Linus Torvalds completed the main development phase of the next version of Linux on the main development branch. As the kernel hackers already integrate most of a new kernel version's major changes into the source code management system during this phase, called the merge window, 2.6.32-rc1 is already a good indicator of the most important new features due for release with Linux 2.6.32 in early December.

For instance, the kernel developers have made several improvements to the kernel's Direct Rendering Manager (DRM) to include 3D support and kernel-based mode setting (KMS) for Radeon series 2000, 3000 and 4000 cards; to access these new features, however, developer versions of Libdrm, Mesa\[\]3D and the X.org Radeon graphics drivers are required. Several Wi-Fi drivers and [Microsoft's Hyper-V driver](../site/news/item/Microsoft-GPLs-Linux-virtualisation-drivers-742565.html "Microsoft GPLs Linux virtualisation drivers – 20 July 2009, 17:22"), which was recently released under the GPL, have moved into the staging area which is intended for drivers that still require further development. The maintainer of the staging branch had earlier threatened to remove the drivers for Microsoft's hypervisor from the kernel with 2.6.33, because the Microsoft developers appeared to have stopped working on the code – but their swift return to visible activity seems to have averted that fate for now. Several other unmaintained staging drivers will be removed in 2.6.32.

Another added kernel feature is the support of Intel's Trusted Execution Technology ([TXT](http://www.intel.com/technology/security/)), formerly known as LaGrande Technology. The next kernel version will support several techniques for handling and avoiding memory errors (HWPOISON); these techniques were introduced with Intel CPUs with Nehalem EX cores. Numerous improvements were also made to the kernel scheduler responsible for allocating processor time to applications. Many other changes modify the tracing infrastructure and the recently introduced performance counters, which are now called performance events. In addition, the writeback infrastructure was reworked to improve the I/O throughput in SMP systems.

As expected, the KSM ("Kernel Samepage Merging") feature [explained in detail](../site/open/features/The-nitty-gritty-proceedings-of-the-Linux-Symposium-2009-746605.html "The nitty gritty - proceedings of the Linux Symposium 2009 – 11 August 2009, 16:03") at this year's Linux Symposium (formerly Ottawa Linux Symposium/OLS) has now been integrated. However, the two and a half weeks since the [release of Linux 2.6.31](../site/open/features/The-Next-Round-The-new-features-of-Linux-2-6-31-746619.html "The Next Round – The new features of Linux 2.6.31 – 10 September 2009, 07:33") have also shown that the kernel hackers can always be relied upon for surprises. For instance, they [incorporated](../site/news/item/Kernel-Log-Devtmpfs-in-2-6-32-more-discussion-about-DRBD-new-stable-kernels-812212.html "Kernel Log - Devtmpfs in 2.6.32, more discussion about DRBD, new stable kernels – 21 September 2009, 12:36") devtmpfs, which some mockingly call "Devfs 2.0", although it received sometimes harsh criticism from several well-known kernel hackers both before and after its integration. On the other hand, the [DRBD](http://www.drbd.org/) (Distributed Replicated Block Device) replication solution was not integrated, although Andrew Morton [advocated its inclusion in 2.6.32](http://thread.gmane.org/gmane.linux.kernel/862072/focus%3D867540). This was probably, at least partially, caused by the discussions about the pros and cons of DRBD [already mentioned](../site/news/item/Kernel-Log-Devtmpfs-in-2-6-32-more-discussion-about-DRBD-new-stable-kernels-812212.html "Kernel Log - Devtmpfs in 2.6.32, more discussion about DRBD, new stable kernels – 21 September 2009, 12:36") in the Kernel Log, which still continued [through last weekend](http://thread.gmane.org/gmane.linux.network.drbd.devel/953/focus%3D889988).

These are only some of the major advancements of Linux 2.6.32. The Kernel Log on The H and the "Coming in 2.6.32" mini series which will start soon, will report in detail about the changes mentioned as well as numerous further important developments in the coming few weeks.

([thl](mailto:thl@heiseopen.de))

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
