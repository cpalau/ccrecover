---
title: "Kernel Log: new Catalyst drivers, 2.6.27.1 resolves cause of e1000e problem"
date: 2008-10-18
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-new-Catalyst-drivers-2-6-27-1-resolves-cause-of-e1000e-problem-737701.html
pages: 1
---

# Kernel Log: new Catalyst drivers, 2.6.27.1 resolves cause of e1000e problem

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/4/4/7/2/93e8ea3d0acdf147.jpg) AMD has released version 8.10 of its proprietary [x86-32](http://ati.amd.com/support/drivers/linux/linux-radeon.html) and [x86-64](http://ati.amd.com/support/drivers/linux64/linux64-radeon.html) Linux graphics drivers. The release notes for the latest version of the driver, also known as Catalyst or fglrx, are still missing. According to the [ATI RSS feed](http://ati.amd.com/online/rss/atilinuxdriver.rss?OTC-rssfeedlinux), the new version supports Red Hat Enterprise Linux 4.7 and contains libraries for AMD's [CAL](http://ati.amd.com/technology/streamcomputing/faq.html#cal1) (Computer Abstraction Layer) designed for [stream computing](http://ati.amd.com/technology/streamcomputing/).

In contrast to speculation on internet, the new version does not support X Server 1.5, which is part of [X.org 7.4](../site/news/item/X-org-7-4-comes-complete-with-new-functions-new-drivers-and-new-incompatibilities-737419.html "X.org 7.4 comes complete with new functions, new drivers and new incompatibilities – 24 September 2008, 15:48"). Xorg 7.4's driver ABI ([Application Binary Interface](http://en.wikipedia.org/wiki/Application_binary_interface)) is incompatible with that of previous X Servers. Some distributions have already started to supply X Server 1.5 – Fedora 9 contained a pre-release version in May, which made the AMD drivers inoperable for Fedora users. According to a [report by Phoronix](http://www.phoronix.com/scan.php?page=article&item=canonical_catalyst_811&num=1), the users of Ubuntu 8.10, which is due for release in a fortnight, will be spared such problems, because the Ubuntu developers recently co-operated with AMD to integrate a pre-release version of the Catalyst 8.11 driver, expected next month, into the package repositories of the X.org 7.4 based distribution.

**New 2.6.27 variant**

Greg Kroah-Hartman has released Linux version [2.6.27.1](http://thread.gmane.org/gmane.linux.kernel/744924). The only difference between it and version [2.6.27](../site/open/features/Kernel-Log-Linux-2-6-27-Released-746496.html "Kernel Log: Linux 2.6.27 Released – 10 October 2008, 08:38"), which was released last week, is [a patch](http://git.kernel.org/?p=linux/kernel/git/stable/linux-2.6.27.y.git;a=commitdiff;h=d23d43386311fde5f11e06c16d4185e94a8d6d06) which marks the DYNAMIC_FTRACE kernel configuration option as "broken" and disables this new function in 2.6.27.

The rather lengthy [commit notes](http://git.kernel.org/?p=linux/kernel/git/stable/linux-2.6.27.y.git;a=commitdiff;h=d23d43386311fde5f11e06c16d4185e94a8d6d06) explain the background in detail. According to the notes, the Ftrace code activated through this configuration option is strongly suspected to be responsible for the accidental overwriting of the non-volatile memory (NVM) in Intel networking chips, among other things. This rendered Intel's networking chips inoperable on some boards with recent Intel southbridges; a [modification integrated](../site/news/item/Kernel-Log-problem-with-e1000e-bypassed-Morton-praises-Btrfs-737561.html "Kernel Log: problem with e1000e bypassed, Morton praises Btrfs – 07 October 2008, 08:47") just before the completion of 2.6.27, is already designed to prevent the accidental overwriting of the non-volatile memory.

**In brief**

- After the discussions sparked by Linus Torvalds around a new naming scheme [several weeks ago](../site/news/item/Kernel-Log-No-unstable-series-Linux-2008-7-dealing-with-security-fixes-736557.html "Kernel Log: No unstable series; Linux 2008.7; dealing with security fixes – 22 July 2008, 01:47") fizzled out rather quickly by LKML standards, Greg Kroah-Hartman has now tried to revive them with [a new proposal](http://thread.gmane.org/gmane.linux.kernel/744941).

<!-- -->

- The Intel developers of the [linuxwimax.org](http://linuxwimax.org) project have [released version 1.3 of the Wimax infrastructure and drivers for Linux](http://thread.gmane.org/gmane.linux.kernel.wireless.general/22285) which they developed as part of this project.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: Ext4 completes development phase as interim step to btrfs](../site/news/item/Kernel-Log-Ext4-completes-development-phase-as-interim-step-to-btrfs-737697.html "Kernel Log: Ext4 completes development phase as interim step to btrfs – 17 October 2008, 09:52")
- [Kernel Log: Linux 2.6.27 Released](../site/open/features/Kernel-Log-Linux-2-6-27-Released-746496.html "Kernel Log: Linux 2.6.27 Released – 10 October 2008, 08:38")
- [Kernel Log: problem with e1000e bypassed, Morton praises Btrfs](../site/news/item/Kernel-Log-problem-with-e1000e-bypassed-Morton-praises-Btrfs-737561.html "Kernel Log: problem with e1000e bypassed, Morton praises Btrfs – 07 October 2008, 08:47")
- [Kernel Log: 2.6.27 nearing completion; Btrfs to be added to the kernel?](../site/news/item/Kernel-Log-2-6-27-nearing-completion-Btrfs-to-be-added-to-the-kernel-737489.html "Kernel Log: 2.6.27 nearing completion; Btrfs to be added to the kernel? – 01 October 2008, 09:23")
- [Kernel Log: Kernel Summit info; Plumbers keynote online; the latest on the e1000e problem](../site/news/item/Kernel-Log-Kernel-Summit-info-Plumbers-keynote-online-the-latest-on-the-e1000e-problem-737443.html "Kernel Log: Kernel Summit info; Plumbers keynote online; the latest on the e1000e problem – 26 September 2008, 10:59")
- [Kernel Log: The second day of Kernel Summit 2008; criticism of Ubuntu at the opening of the Linux Plumbers Conference](../site/news/item/Kernel-Log-The-second-day-of-Kernel-Summit-2008-criticism-of-Ubuntu-at-the-opening-of-the-Linux-Plumbers-Conference-737379.html "Kernel Log: The second day of Kernel Summit 2008; criticism of Ubuntu at the opening of the Linux Plumbers Conference – 19 September 2008, 15:58")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
