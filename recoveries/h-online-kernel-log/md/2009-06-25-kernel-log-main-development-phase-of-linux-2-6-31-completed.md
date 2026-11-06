---
title: "Kernel Log: Main development phase of Linux 2.6.31 completed"
date: 2009-06-25
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-Main-development-phase-of-Linux-2-6-31-completed-742199.html
pages: 1
---

# Kernel Log: Main development phase of Linux 2.6.31 completed

**Dj Walker-Morgan**

![Kernel Log Penguin](../site/imgs/43/3/6/8/6/3/0/93e8ea3d0acdf147.jpg) Just over two weeks after the [release of Linux 2.6.30](../site/open/features/Fine-tuning-What-s-new-in-Linux-2-6-30-746581.html "Fine tuning – What's new in Linux 2.6.30 â 10 June 2009, 09:34"), Linus Torvalds has [released](http://thread.gmane.org/gmane.linux.kernel/857043) 2.6.31-rc1, the first release candidate of Linux 2.6.31. As usual, "rc1" completes the merge window during which the kernel hackers incorporate the majority of new features into the respective new version's main development branch. In the eight to eleven weeks that follow, the programmers tend to integrate only smaller changes to fix bugs in the newly merged code without causing any further problems. If the kernel hackers stick to their usual pace despite the summer and holiday season in the northern hemisphere, Linux 2.6.31 will probably be released in late August or early September.

As is often the case, the [list](http://kernel.org/pub/linux/kernel/v2.6/testing/ChangeLog-2.6.31-rc1) of changes is rather long. For instance, 2.6.31 will be capable of [kernel-based mode setting](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-3-Kernel-controlled-graphics-modes-739697.html "Kernel Log: What's new in 2.6.29 - Part 3: Kernel controlled graphics modes â 17 January 2009, 07:36") (KMS) with the Radeon models up to X1950Â XTX. However, the code hasn't reached the developers' quality and security standards yet â€“ they have classified the KMS driver as a staging driver which will mark the kernel [as "crap"](../site/open/Kernel-Log-Higher-and-Further-The-innovations-of-Linux-2-6-28--/features/112299/4#staging) when loaded. As expected, the kernel developers have also integrated [a driver](../site/news/item/Kernel-Log-ALSA-driver-for-the-X-Fi-debate-over-TuxOnIce-741673.html "Kernel Log: ALSA driver for the X-Fi, debate over TuxOnIce â 21 May 2009, 09:24") for several PCI sound cards from Creative's Sound Blaster X-Fi series as well as [drivers and an infrastructure](../site/news/item/First-Linux-USB-3-0-drivers-emerge-741965.html "First Linux USB 3.0 drivers emerge â 10 June 2009, 10:06") for addressing USB 3.0 controllers with the Extensible Host Controller Interface (xHCI).

Major changes to the, still very experimental, Btrfs file system aim at discernibly boosting performance in a variety of scenarios. To achieve this, however, Btrfs uses a [different format](http://thread.gmane.org/gmane.comp.file-systems.btrfs/3123) on the physical disk. Existing Btrfs file systems will automatically be transferred during installation â€“ but kernels with an older version of the Btrfs code can no longer integrate file systems modified in this way.

Operating partly in the kernel and partly in the userspace, the "performance counters" code can be used for retrieving the performance data offered by modern processors. This performance data quantifies various CPU processes that have an impact on CPU performance â€“ providing an in-depth analysis and allowing developers to optimise the code segments that are relevant to processing speed. Similar results have been possible with [perfmon](http://perfmon2.sourceforge.net/) for quite a while, but its developers have been unsuccessful in their attempts to get perfmon integrated into the official Linux kernel.

These are only a few of the most important changes. The Kernel Log on The H, in association with [heise online](http://heise.de), will soon begin the "What's new in 2.6.31" mini series which will describe these and many further important changes in detail over the coming weeks.

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
