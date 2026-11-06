---
title: "Kernel Log: Development of 2.6.30 is under way"
date: 2009-03-27
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-Development-of-2-6-30-is-under-way-740805.html
pages: 1
---

# Kernel Log: Development of 2.6.30 is under way

**Dj Walker-Morgan**

![Kernel Log Penguin](../site/imgs/43/3/6/7/2/3/7/93e8ea3d0acdf147.jpg) Shortly after the release of [Linux 2.6.29 last Tuesday](../site/open/features/Steady-growth-What-s-new-in-Linux-2-6-29-746553.html), the kernel subsystem developers began to prepare the first changes to be merged into the main development branch for Linux 2.6.30. This is usually done by sending a "Git pull request" – an email which includes the URL to a Git tree with the proposed changes as well as a diffstat and a list of individual patches – not only to Linus Torvalds, but usually also to the LKML (Linux Kernel Mailing List). Often, the maintainer of the subsystem starts the email with a short summary of the proposed changes, highlighting the most important ones, or putting the changes into context.

**Development of 2.6.30 is under way**

The [pull request email](http://thread.gmane.org/gmane.linux.kernel/811233) with the changes to the ALSA subsystem, for example, mentions a newly integrated driver for an ISA sound hardware component as well as several changes that aim at simplifying dynamic reconfiguration. Among the [changes to KVM virtualisation proposed for 2.6.30](http://thread.gmane.org/gmane.comp.emulators.kvm.devel/29706) is the support of [nested virtualisation](http://avikivity.blogspot.com/2008/09/nested-svm-virtualization-for-kvm.html) for AMD processors; the patches are also intended to further improve the performance and reliability of KVM.

In addition to the [improvements for 2.6.29 we've previously mentioned](../site/open/Steady-growth-What-s-new-in-Linux-2-6-29--/features/112914/5), Mdadm maintainer Neil Brown is preparing [further changes for 2.6.30](http://thread.gmane.org/gmane.linux.raid/21929). They are designed to make it possible to reduce the number of devices in Linux level 4, 5 and 6 software RAIDs. Andrew Morton has [released a list](http://thread.gmane.org/gmane.linux.kernel/811220) of MM development branch patches he intends to merge into the main development branch of Linux – among them the [NILFS2](http://www.nilfs.org/en/) "continuous snapshotting" file system.

The maintainer of the Xen kernel code has prepared [several patch collections](http://thread.gmane.org/gmane.comp.emulators.xen.devel/63711), for example to support privileged Xen domain (Dom0) operation. Recently, Andrew Morton still [questioned whether this should be integrated at all](../site/news/item/Kernel-Log-Morton-questions-acceptance-of-Xen-Dom0-code-file-systems-for-SSDs-740375.html "Kernel Log: Morton questions acceptance of Xen Dom0 code; file systems for SSDs – 06 March 2009, 08:57") – but now it looks like the concerns have been addressed. However, the code review has not been completed yet, which puts a question mark on whether the code will be ready to be merged with 2.6.30.

Linus Torvalds usually takes another look at the proposed changes before he merges them into the Linux source code management system. If he doesn't like what he sees, he has been known to occasionally let changes fall by the wayside. Usually, the patches are then reworked and will find their way into the main development branch eventually; sometimes, however, Torvalds' criticism is so harsh that changes that seemed sure to be integrated don't make it into the Linux kernel at all and are eventually forgotten.

So far, Torvalds has not merged any changes for 2.6.30; when releasing 2.6.29, he already [mentioned](http://thread.gmane.org/gmane.linux.kernel/811167) that he intends to wait a couple of days to give people a chance to test 2.6.29 ("*This obviously starts the merge window for 2.6.30, although as usual, I'll probably wait a day or two before I start actively merging. I do that in order to hopefully result in people testing the final plain 2.6.29 a bit more before all the crazy changes start up again.*")

**Statistics and staging**

Wang Chen has [expanded](http://thread.gmane.org/gmane.linux.kernel/811200) his [Linux Kernel Patch Statistic](http://remword.com/kps_result/) website to include the results for Linux 2.6.29. Just as in the LWN.net article entitled "[Where 2.6.29 came from](http://lwn.net/Articles/324046/)", which became freely available yesterday, Novell (or rather, Novell employee Greg Kroah-Hartman) fares decidedly better here than in previous reports – this is mainly due to the [staging area](../site/news/item/Kernel-Log-Linux-staging-branch-will-help-with-integration-Linux-kernel-2-6-25-6-and-2-6-26-rc6-735507.html "Kernel Log: Linux-staging branch will help with integration; Linux kernel 2.6.25.6 and 2.6.26-rc6 – 17 June 2008, 11:31"), which was integrated into the main development branch [2.6.28](../site/open/Kernel-Log-Higher-and-Further-The-innovations-of-Linux-2-6-28--/features/112299/4#moredriverswith) and is maintained by Greg Kroah-Hartman. This area contains a multitude of drivers and other code which is not yet up to the standards required by the kernel developers.

In [an email to the LKML](http://thread.gmane.org/gmane.linux.kernel/808938) as well as [in his blog](http://www.kroah.com/log/linux/linux-staging-update.html), Kroah-Hartman recently reiterated the purpose of the staging area in detail. Dave Airlie, however, [criticised the concept](http://thread.gmane.org/gmane.linux.kernel/808938/focus%3D809680) in one of the discussions. A [patch](http://thread.gmane.org/gmane.linux.kernel.wireless.general/30461) recently released on the Linux Wireless Mailing List also indicates that some of the kernel hackers don't seem too happy with the staging area. The patch says that the Linux Wi-Fi developers don't want to have anything to do with some of the staging drivers (*"Please send any patches or complaints about this driver to Greg Kroah-Hartman and don't bother the upstream wireless kernel developers about it, they want nothing to do with it."*)

After a lengthy discussion, Kroah-Hartman also [gave up on the idea](http://thread.gmane.org/gmane.linux.kernel/809146/focus%3D810176) of incorporating DRM support for the proprietary parts of a US15W graphics driver [into the staging area](http://thread.gmane.org/gmane.linux.kernel/809146). At least the current versions of a graphics driver for Intel's US15W (Poulsbo) seem to be due for release soon, although chances are that this driver won't offer 3D acceleration, it is likely that it will work with the current X.org and Linux kernel versions, unlike the [drivers that are currently available](../site/news/item/Kernel-Log-Stable-series-development-is-speeding-up-X-Server-1-6-available-soon-740203.html "Kernel Log: Stable series development is speeding up, X Server 1.6 available soon – 23 February 2009, 10:46").

**Kernel status**

In parallel to the release of Linux 2.6.30, the maintainers of the stable kernel series have released the Linux versions [2.6.27.21](http://thread.gmane.org/gmane.linux.kernel/811155) and [2.6.28.9](http://thread.gmane.org/gmane.linux.kernel/811153), which both offer a number of minor corrections and improvements. As always, the release emails recommend that all users update to the latest version without giving explicit details about whether there were any security issues. However, the recommendation to update only applies to those who self-compiled a previous kernel.

With the release of 2.6.29, the maintenance of the 2.6.27 series would normally soon be discontinued, but Greg Kroah-Hartman has indicated that he intends to maintain [2.6.27](http://thread.gmane.org/gmane.linux.kernel/742570/focus%3D743396) a little longer; Adrian Bunk will continue to maintain it after him, as he already announced [last October](../site/news/item/Kernel-Log-New-stable-kernels-and-Nvidia-drivers-long-term-maintenance-for-2-6-27-737641.html "Kernel Log: New stable kernels and Nvidia drivers, long-term maintenance for 2.6.27 – 13 October 2008, 16:48").

**In brief**

- Following the previous disagreements about (Ext) file systems, as discussed in [yesterday's The H Open Source article](../site/news/item/Kernel-developers-squabble-over-Ext3-and-Ext4-740787.html), the kernel developers continued [their debate](http://thread.gmane.org/gmane.linux.kernel/811167/focus%3D811228) last night; in this context, Jeff Garzik released [a patch](http://thread.gmane.org/gmane.linux.kernel/811167/focus%3D812574) to fix some of the problems discussed.

<!-- -->

- AMD's Alex Deucher has [released](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/584) version 6.12.1 of the xf86-video-ati driver collection that includes the radeon driver. This version fixes several bugs contained in the recently released version 6.12.0.

<!-- -->

- Nvidia has released the pre-release version of a proprietary GeForce graphics driver for Linux and other operating systems which implements [OpenGL 3.1](../site/news/item/Specification-adopted-for-OpenGL-3-1-740766.html "Specification adopted for OpenGL 3.1 – 25 March 2009, 15:16"); OpenGL 3.1 was recently approved by the Khronos Group.

<!-- -->

- After nine years of development outside of the main development branch, the [DRBD](http://www.drbd.org/) (Distributed Replicated Block Device) developers are ([once more](http://thread.gmane.org/gmane.linux.kernel/558765)) [putting effort into](http://thread.gmane.org/gmane.linux.kernel/810953) having their HA solution merged into the official Linux kernel.

<!-- -->

- Alexandre Oliva has released version 2.6.28.8 of [Linux-Libre](http://thread.gmane.org/gmane.linux.kernel.libre/432) – a version of Linux 2.6.28.8 in which any non-open components, like firmware, have been removed.

<!-- -->

- VIA has released WiFi drivers for the [VT6655](http://www.viaarena.com/Driver/vt6655_linux_src_v1.19.12_x86.zip) and [VT6656](http://www.viaarena.com/Driver/VT6656_Linux_src_v1.19_12_x86.zip) chips under an open source licence.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at The H Open Source:*

- [Steady Growth: What's new in Linux 2.6.29](../site/open/features/Steady-growth-What-s-new-in-Linux-2-6-29-746553.html)
- [Kernel Log: Tasmanian devil to be Linux's temporary mascot, new Radeon drivers](../site/news/item/Kernel-Log-Tasmanian-devil-to-be-Linux-s-temporary-mascot-new-Radeon-drivers-740667.html "Kernel Log: Tasmanian devil to be Linux's temporary mascot, new Radeon drivers – 19 March 2009, 15:43")
- [Kernel Log: What's new in 2.6.29 - Part 8: Faster start-up and other behind the scenes changes](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-8-Faster-start-up-and-other-behind-the-scenes-changes-740591.html "Kernel Log: What's new in 2.6.29 - Part 8: Faster start-up and other behind the scenes changes – 18 March 2009, 08:33")
- [Kernel Log: What's new in 2.6.29 - Part 7: Audio, FireWire, USB, Video and more](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-7-Audio-FireWire-USB-Video-and-more-740561.html "Kernel Log: What's new in 2.6.29 - Part 7: Audio, FireWire, USB, Video and more – 16 March 2009, 13:07")
- [Kernel Log: What's new in 2.6.29 - Part 6: Storage, IDE/PATA, SCSI](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-6-Storage-IDE-PATA-SCSI-740501.html "Kernel Log: What's new in 2.6.29 - Part 6: Storage, IDE/PATA, SCSI – 13 March 2009, 13:45")
- [Kernel Log: What's new in 2.6.29 - Part 5: Filesystems Btrfs, SquashFS, Ext4 without journaling](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-5-Filesystems-Btrfs-SquashFS-Ext4-without-journaling-740499.html "Kernel Log: What's new in 2.6.29 - Part 5: Filesystems Btrfs, SquashFS, Ext4 without journaling – 12 March 2009, 15:13")
- [Kernel Log: Morton questions acceptance of Xen Dom0 code; file systems for SSDs](../site/news/item/Kernel-Log-Morton-questions-acceptance-of-Xen-Dom0-code-file-systems-for-SSDs-740375.html "Kernel Log: Morton questions acceptance of Xen Dom0 code; file systems for SSDs – 06 March 2009, 08:57")

*Older Kernel logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/).* ([thl](mailto:thl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
