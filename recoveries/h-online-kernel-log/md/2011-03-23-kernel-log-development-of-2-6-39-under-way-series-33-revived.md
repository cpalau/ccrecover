---
title: "Kernel Log: Development of 2.6.39 under way, series 33 revived"
date: 2011-03-23
author: "Thorsten Leemhuis"
source: http://www.h-online.com/open/features/Kernel-Log-Development-of-2-6-39-under-way-series-33-revived-1212988.html
pages: 1
---

# Kernel Log: Development of 2.6.39 under way, series 33 revived

**Thorsten Leemhuis**

**Among the additions for kernel version .39 are the Xen network backend, support for ipset, and the rudimentary Poulsbo graphics driver; the kernel hackers have now also completely eradicated the BKL. Greg Kroah-Hartman has taken up maintaining the series 33 kernel again because it is the basis of the real-time branch.**

Less than 24 hours after releasing Linux 2.6.38 [on Tuesday last week](../site/open/features/What-s-new-in-Linux-2-6-38-1205467.html "What's new in Linux 2.6.38 – 15 March 2011"), Linus Torvalds started merging the changes for Linux 2.6.39. Among the commits that have already been added is the [Xen network backend](http://git.kernel.org/linus/f942dc2552b8bfdee607be867b12a8971bb9cd85) for Dom0 kernels – however, the storage backend also required for operating a meaningful Dom0 has not yet made it into the kernel.

As expected, the last remaining components that use the Big Kernel Lock (BKL) have now been removed, allowing the kernel hackers to completely eradicate the lock via a commit entitled "[BKL:That's all, folks](http://git.kernel.org/linus/4ba8216cd90560bc402f52076f64d8546e8aefcb)". Among the [new additions](http://git.kernel.org/linus/a7b4f989a629493bb4ec4a354def784d440b32c4) is the support for the sixth generation of the [ipset](http://ipset.netfilter.org/) program for optimising certain netfilter policies. In the staging area, the developers also [added](http://git.kernel.org/linus/0867b42113ec4eb8646eb361b15cbcfb741ddf5b) a [rudimentary graphics driver](../site/news/item/Rudimentary-open-source-driver-for-Intel-s-GMA500-Poulsbo-1195125.html "Rudimentary open source driver for Intel's GMA500/Poulsbo  – 23 February 2011") for the GMA500 graphics chip found in Intel's US15W chip-set, also known as Poulsbo.

These are only some of the noteworthy additions the Kernel Log will comprehensively discuss in a series of "Coming in 2.6.39" articles over the next few weeks. Further changes will be merged for 2.6.39 in the coming days, because Torvalds will only close the merge window early next week, if he keeps to his usual routine.

### Kernel version status

Earlier this week, Greg Kroah-Hartman released kernel version [2.6.33.8](http://thread.gmane.org/gmane.linux.kernel/1115749), which differs from the previous version by more than [470 patches](http://thread.gmane.org/gmane.linux.kernel/1114586/). Kroah-Hartman had originally discontinued the maintenance of series 33 months ago; now, he has input further energy because the [RT tree](https://rt.wiki.kernel.org/index.php/Main_Page) that provides real-time capabilities is still based on 2.6.33. During the review of 2.6.33.8, Thomas Gleixner [said](http://thread.gmane.org/gmane.linux.kernel/1114586/focus%3D1115365) that he is working on porting the RT tree to the current kernel version, but he didn't provide any details about the current state of development. In early March, the maintainer of the series 34 Longterm kernels, Paul Gortmaker, had [presented](http://thread.gmane.org/gmane.linux.rt.user/6615) a port of the RT tree to 2.6.34 – however, the future prospects of this port remain uncertain.

Longterm kernel version [2.6.32.34](http://thread.gmane.org/gmane.linux.kernel/1115786) and Stable kernel versions [2.6.37.5](http://thread.gmane.org/gmane.linux.kernel/1115787) and [2.6.38.1](http://thread.gmane.org/gmane.linux.kernel/1115788) are now in a review cycle that is to end late on Wednesday night (23 March); these versions should become available shortly thereafter. Kroah-Hartman hasn't indicated how long he intends to maintain series 37 – however, due to the release of 2.6.38, the series is probably beginning to approach the end of its life cycle.

### In brief

##### Kernel

- Christoph Hellwig has written his [XFS status update for February 2011](http://thread.gmane.org/gmane.linux.file-systems/51860).

<!-- -->

- In an email to the LKML, Thomas Gleixner recently outlined various [problems](http://thread.gmane.org/gmane.linux.kernel/1111888/focus%3D1111918) the kernel developers sometimes encounter while troubleshooting their code. This particular case revolved around various bug reports concerning systems that only start if the processor/intel_idle.max_cstate=1 kernel parameter is enabled. Gleixner said that the kernel developers can't usually do much about such problems because their causes tend to be "hidden deep in that black hole of ACPI/BIOS". The developer added that some vendors implement technologies in ways that weren't intended, and that they only test their implementations against "that other OS" (Windows); in this context, the developer indicated with some irony that these hardware vendors don't tend to be particularly helpful when it comes to troubleshooting. "Yes, it's sad, but reality", said Gleixner.

##### Graphics hardware support

- AMD developer Alex Deucher has [released](http://thread.gmane.org/gmane.comp.freedesktop.xorg.drivers.ati/18650) version 6.14.1 of the xf86-video-ati X.org driver package. Together with some changes introduced for Linux 2.6.39, the Radeon driver included in the package offers rudimentary support for Cayman graphics chips, which are used on series 6900 Radeon HD models.

<!-- -->

- In a discussion on a mailing list, Alex Deucher [recently](http://thread.gmane.org/gmane.linux.acpi.devel/49472/focus%3D1113675) outlined various aspects AMD needs to consider when developing open source drivers. For instance, the developer said that the video decoding functions are intimately tied in with the graphics chip's Digital Rights Management components, which apparently hampers the release of the UVD (Unified Video Decoder) documentation and drivers.

<!-- -->

- In an article entitled "[Overview of Xrandr](http://www.linuxaria.com/article/linux-xrandr)", the Linuxaria website describes the use of xrandr – a command line program for adjusting display configurations via RandR (X Resize, Rotate and Reflect Extension).

##### Kernel environment ("plumbing layer"), userland drivers, developer tools etc

- The Git tree, archives, documentation and [wiki](https://dracut.wiki.kernel.org/) pertaining to the distribution-independent Dracut initrd generation tool are [now located](http://www.harald-hoyer.de/personal/blog/dracut-moved-to-kernel.org) at kernel.org.

<!-- -->

- The developers of the [hplip](http://hplipopensource.com/) (Hewlett-Packard's Linux Imaging and Printing software) project have released version 3.11.3 of their identically named driver for printers and multi-functional devices from HP. The [release notes](http://sourceforge.net/news/?group_id=149981&id=298587) provide a detailed overview of the major new additions – such as the support of numerous DesignJet models and of the LaserJet CP1520.

<!-- -->

- Greg Kroah-Hartman has [released](http://thread.gmane.org/gmane.linux.kernel/1114656) version 002 of the usbutils.

<!-- -->

- Earlier this month, the developers released the Squashfs tools 4.2, which can compress images in the XZ format developed from LZMA; such images are supported [in Linux 2.6.38](../site/open/features/Kernel-Log-Coming-in-2-6-38-Part-5-Architecture-infrastructure-and-virtualisation-1202216.html "Kernel Log: Coming in 2.6.38 (Part 5) - Architecture, infrastructure and virtualisation – 07 March 2011").

<!-- -->

- Stephen Hemminger has [released](http://thread.gmane.org/gmane.linux.network/189878) the iproute2 collection of network configuration tools for kernel version 2.6.38; the collection follows the same numbering scheme as the kernel.

<!-- -->

- Scott James Remnant has completed [Upstart 1.1](http://thread.gmane.org/gmane.comp.sysutils.upstart.devel/1327), rapidly followed by [Upstart 1.2](http://thread.gmane.org/gmane.linux.kernel/1116357), which contained an important bugfix.

<!-- -->

- In a series of blog postings, Michael J. Schultz plans to explain how the Linux network stack works; [the first and currently only part](http://blog.beyond-syntax.com/2011/03/diving-into-linux-networking-i/) of the series describes various aspects in connection with the tasks of network drivers.

<!-- -->

- In the release email for suspend-utils 1.0, Rafael J. Wysocki said that he generally plans to discontinue the development of the s2ram program, which is particularly used in the SUSE environment, and of the whitelist he has maintained; however, the hibernate/software suspend tools also included in this tool collection will apparently continue to be maintained.

<!-- -->

- The organisers of Linux-Kongress, a conference previously attended by Linus Torvalds and many other well-known kernel hackers, have decided [not to hold](http://www.linux-kongress.org/2011/) their long-established event this year. They said that, with LinuxCon Europe, the Embedded Linux Conference Europe and the Linux Kernel Summit, there will already be three conferences in Europe this year – and that the GUUG has, therefore, decided to co-operate with the Linux Foundation and contribute in various areas to help make the LinuxCon conference a success. LinuxCon's [Call for Participation](http://events.linuxfoundation.org/events/linuxcon-europe/cfp) (CFP) will close on 8 July.

<!-- -->

- Thomas Renninger has [announced](http://thread.gmane.org/gmane.linux.kernel.cpufreq/7041) the first version of the cpupowerutils. They are based on the cpufrequtils and offer the cpupower command line tool, which is described with examples in the release email and, for instance, provides information on the use of modern processors' power management and frequency scaling features.

[![](../site/open/imgs/45/6/4/6/0/8/8/66a499bf9291905e.png)](../site/open/features/Kernel-Log-Development-of-2-6-39-under-way-series-33-revived-1212988.html?view=zoom;zoom=2) [![Zoom](../site/icons/lupe.png "Zoom")](../site/open/features/Kernel-Log-Development-of-2-6-39-under-way-series-33-revived-1212988.html?view=zoom;zoom=2) The new cpupower program provides information on the use of modern processors' power management and frequency scaling features.

*Older Kernel Logs can be found in *[the archives](../site/open/news/archive/)* or by using *[the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log)* at *[The H Open Source](../site/open/)*. New editions of Kernel Logs are also mentioned on [Identi.ca](http://identi.ca/kernellog2) and [Twitter](http://twitter.com/kernellog2) via "@kernellog2". The Kernel Log author also posts updates about various topics on [Identi.ca](http://identi.ca/kernellogauthor) and [Twitter](http://twitter.com/kernellogauthor) via "@kernellogauthor".* ([crve](mailto:crve%40h-online.com))
