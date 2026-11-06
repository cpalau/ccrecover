---
title: "Kernel Log: Linux 2.6.34 goes into testing"
date: 2010-03-10
author: "Thorsten Leemhuis"
source: http://www.h-online.com/open/features/Kernel-Log-Linux-2-6-34-goes-into-testing-950563.html
pages: 1
---

# Kernel Log: Linux 2.6.34 goes into testing

**Thorsten Leemhuis**

**![KL Logo](../site/open/imgs/45/4/9/3/2/5/4/KL.jpg-1f663d67fe8a53b0.jpeg) Linus Torvalds has released the first RC of Linux 2.6.34 and completed the integration of the next version of the kernel's most important changes. Improvements include graphics drivers for recent Radeon GPUs and for the graphics cores of some Intel processors that are only expected to be released early next year. Another new addition is the LogFS solid-state storage file system.**

With the [release of Linux 2.6.34-rc1](http://thread.gmane.org/gmane.linux.kernel/958851) on Monday night, Linus Torvalds has closed the merge window of Linux 2.6.34 – only 12 days after releasing [Linux 2.6.33](../site/news/item/Linux-kernel-2-6-33-released-935427.html "Linux kernel 2.6.33 released – 24 February 2010"). While Torvalds usually allows at least two weeks at the beginning of each development cycle for integrating the most important new features, he had already [indicated](../site/open/features/Kernel-Log-Stable-kernels-analysed-Linux-without-firmware-new-graphics-drivers-948051.html "Kernel Log: Stable kernels analysed, Linux without firmware, new graphics drivers – 08 March 2010") that the current first phase would be shorter in an attempt to get subsystem maintainers out of the habit of submitting their changes at the last minute.

The developers made numerous further changes to the graphics driver code. Among the new additions is a [KMS graphics driver for Radeon 5000 graphics cards](http://git.kernel.org/linus/bcc1c2a1d22974215e39dc87ce746ba9a39223e5) and improved support of the power-saving mechanisms in modern Radeon graphics chips. [Major restructuring measures](../site/open/features/Kernel-Log-Stable-kernels-analysed-Linux-without-firmware-new-graphics-drivers-948051.html "Kernel Log: Stable kernels analysed, Linux without firmware, new graphics drivers – 08 March 2010") in the kernel's Nouveau driver have changed the API; this has made older Nouveau drivers for X.org incompatible with the new kernel. The Nouveau code can now [generate](http://git.kernel.org/linus/d5f3c90d4f3ad6b054f9855b7b69137b97bda131) the firmware for recent graphics chips itself and no longer requires the external ctxprogs that [caused discussions](../site/news/item/Kernel-Log-Coming-in-2-6-33-Part-3-Graphics-922495.html "Kernel Log: Coming in 2.6.33 (Part 3) - Graphics – 05 February 2010") when Nouveau was first integrated.

In notebooks equipped with chip-set graphics as well as a separate graphics chip, the kernel can now switch between the two graphics systems. The developers extended the Intel graphics drivers to include [first components](http://git.kernel.org/linus/bad720ff3e8e47a04bd88d9bbc8317e7d7e049d3) for an Intel processor so far only known by its code name, Sandybridge, which contains a GPU and is expected to become available early next year. Some drivers for the pertaining motherboard chip-sets, which are currently only known as Cougar Point, were also added to the kernel during this merge window.

Another new addition is the [LogFS](http://logfs.org/logfs/) file system, which is mainly interesting for Flash media without wear levelling such as those used in embedded applications. Further additions include a driver for Apple's Magic Mouse, a Python scripting engine for the tracing subsystem, and the vhost_net Virtio server. Various power-saving techniques were also improved.

As usual, the Kernel Log at The H Open will discuss these and many other new features in a "Coming in 2.6.34" mini series in the coming few weeks. Let's, however, wait another few days before we start: Torvalds might still add a few more changes submitted by subsystem maintainers who missed the merge window. According to his [release email](http://thread.gmane.org/gmane.linux.kernel/958851), Torvalds is also considering integrating the Ceph file system and a number of debug patches. Compared with the number of changes introduced in the first RCs of previous kernels, the current release candidate, 2.6.34-rc1, contains considerably fewer changes:

|  |  |  |
|----|----|----|
| Kernel-Version | Commits | Diffstart |
| 2.6.29..v2.6.30-rc1 | 9603 | 8344 files changed, 980137 insertions(+), 372613 deletions(-) |
| 2.6.30..v2.6.31-rc1 | 8288 | 7858 files changed, 858831 insertions(+), 479565 deletions(-) |
| 2.6.31..v2.6.32-rc1 | 8742 | 8998 files changed, 977516 insertions(+), 490562 deletions(-) |
| 2.6.32..v2.6.33-rc1 | 8475 | 8637 files changed, 806090 insertions(+), 455196 deletions(-) |
| 2.6.33..v2.6.34-rc1 | 6032 | 6533 files changed, 425073 insertions(+), 187044 deletions(-) |

### 

### Google wants to integrate Android code into Linux kernel in the long run

After several insufficiently maintained drivers for Android devices were [stripped from the main development branch of Linux](../site/news/item/Android-code-removed-from-Linux-kernel-920688.html "Android code removed from Linux kernel – 03 February 2010") a few weeks ago, Chris DiBona, Google's Open Source Program Manager, said [on Zdnet](http://blogs.zdnet.com/open-source/?p=5992) that Google plans to integrate Android's kernel extensions into the main development branch of the Linux kernel – "in the next couple of years". However, the kernel extensions in question go far beyond these drivers, which has caused controversy between Google and the kernel developers.

This was apparent in a discussion between DiBona and kernel hacker Greg Kroah-Hartmann that was sparked by an [article on LWN.net](http://lwn.net/Articles/372419/) concerning the lack of co-operation between Google and the kernel community. Responding to Kroah-Hartmanns ("gregkh") complaints that Google wasn't interested in getting the Android changes integrated into the standard kernel, DiBona ("cdibona") said at the time that Android's Linux kernel requirements were very different from those of desktop or server systems. Forking the Linux kernel for Android is OK, although ultimately not Google's goal, he said. DiBona compared the Android kernel to the kernels of Red Hat Enterprise Linux and other distributions which, according to the executive, are just as much forks from the main development branch as the Android kernel.

DiBona also said that the Linux code Google use internally for their non-mobile systems is quite close to the main development branch, but that Android is a different story. At the Kernel Summit 2009 only [a few months ago](../site/news/item/Kernel-Log-Discussions-at-the-2009-Kernel-Summit-FatELF-in-the-firing-line-new-graphics-drivers-850044.html " Kernel Log - Discussions at the 2009 Kernel Summit, FatELF in the firing line, new graphics drivers – 04 November 2009"), however, a Google employee presented a report about Google's use of Linux; a summary of this presentation can be found in the article "[How Google uses Linux](http://lwn.net/Articles/357658/)" on LWN.net. According to this presentation, Google has also made comprehensive changes internally without putting major effort into getting these changes integrated into the main development branch or comparing notes with the kernel hackers. However, the presenter did say that Google wants to improve its cooperation.

### In brief

**Kernel**

- Linus Torvalds has [showed willingness](http://lkml.indiana.edu/hypermail/linux/kernel/1003.1/00251.html) to integrate AppArmor into the main development branch.
- UK magazine TuxRadar has published an article by Greg Kroah-Hartman which [explains](http://www.tuxradar.com/content/newbies-guide-hacking-linux-kernel) the first steps for new kernel programmers.
- In his "[XFS status update for February 2010](http://thread.gmane.org/gmane.linux.kernel/958445)", Christoph Hellwig gives an overview of the latest developments in the XFS file system area.

**Graphics**

- NVIDIA employee Aaron Plattner has released version 2.1.17 of the xf86-video-nv X.org graphics driver usually just called "nv". Among its new features is the support of motherboard GPUs/mGPUs in the MCP7x series (GeForce 8x00 and 9x00).

**Kernel environment ("plumbing layer"), userland drivers, Git, ...**

- Assisted by several other kernel developers, Tejun Heo has [compiled](http://ata.wiki.kernel.org/index.php/ATA_4_KiB_sector_issues) some background information about the issues concerning hard disks with 4-Kbyte sectors we've [already](../site/news/item/Kernel-Log-Long-term-maintenance-for-2-6-32-util-linux-ng-extended-910616.html "Kernel Log: Long-term maintenance for 2.6.32, util-linux-ng extended – 22 January 2010") discussed in the Kernel Log [several times](../site/news/item/Kernel-Log-Linux-and-hard-disks-with-4-KByte-sectors-939523.html "Kernel Log: Linux and hard disks with 4-KByte sectors – 24 February 2010"), inviting developers to contribute to [a discussion](http://thread.gmane.org/gmane.linux.ide/45211) which is currently in full swing.
- Junio C Hamano has [released Git 1.7.0.2](http://thread.gmane.org/gmane.linux.kernel/958528).
- The GRUB 2 developers have [released](http://lists.gnu.org/archive/html/grub-devel/2010-03/msg00017.html) version 1.98 of the boot loaders, which offers features such as multi-boot support for EFI.

*Older Kernel Logs can be found in *[the archives](../site/open/news/archive/)* or by using *[the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log)* at *[The H Open Source](../site/open/)*. New editions of Kernel Logs are also mentioned on [Identi.ca](http://identi.ca/kernellog2) and [Twitter](http://twitter.com/kernellog2) via "@kernellog2". The Kernel Log author also posts updates about various topics on [Identi.ca](http://identi.ca/kernellogauthor) and [Twitter](http://twitter.com/kernellogauthor) via "@kernellogauthor".*

([thl](mailto:thl@ct.heise.de))
