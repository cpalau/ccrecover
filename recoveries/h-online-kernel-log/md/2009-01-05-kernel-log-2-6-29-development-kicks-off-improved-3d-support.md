---
title: "Kernel Log: 2.6.29 development kicks off, improved 3D support"
date: 2009-01-05
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-2-6-29-development-kicks-off-improved-3D-support-739551.html
pages: 1
---

# Kernel Log: 2.6.29 development kicks off, improved 3D support

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/5/9/8/3/93e8ea3d0acdf147.jpg) Following the release of [Linux 2.6.28](../site/open/features/Kernel-Log-Higher-and-Further-The-innovations-of-Linux-2-6-28-746519.html "Kernel Log: Higher and Further, The innovations of Linux 2.6.28 – 23 December 2008, 15:55") on [Christmas Eve](../site/news/item/Linux-2-6-28-Released-739471.html "Linux 2.6.28 Released – 25 December 2008, 07:26"), the start of the hectic merge window phase of development for the next version was delayed for a few days of peace on earth, before business as usual, with Linus Torvalds begining to collect changes for 2.6.29 on the 28th of December. The 5400 odd patches so far adopted in 2.6.69 already include a number of major new features, such as [kernel-based mode setting](http://thread.gmane.org/gmane.linux.kernel/531149) for Intel graphics hardware, the merger of the Sparc and Sparc64 directories, a V4L/DVB driver for the STB0899 chip and extensive changes to the XFS file system.

As part of the "What's coming in 2.6.*xx*" series, the Kernel Log will, as for [2.6.28](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-9-Fastboot-and-other-remainders-739431.html "Kernel Log: What's coming in 2.6.28 - Part 9: Fastboot and other remainders – 19 December 2008, 12:45"), be reporting on new features integrated over the next few days and weeks. It is not yet clear how long the merge window will remain open. On this occasion and following the delays over the holiday period, Torvalds wants to allow a little more than the usual two week period for adopting major new features.

Chris Mason, the driving force behind [Btrfs](../site/news/item/Kernel-Log-Ext4-completes-development-phase-as-interim-step-to-btrfs-737697.html "Kernel Log: Ext4 completes development phase as interim step to btrfs – 17 October 2008, 09:52"), has now released an experimental version of the file system, as a patch for the current main development tree; some kernel developers have, however, criticised parts of the code, and it currently looks unlikely that the file system will be included in 2.6.29, for development to continue as part of the main development tree. Andrew Morton has released a [list of patches](http://article.gmane.org/gmane.linux.kernel/775365) to be moved from the MM branch to the main development tree.

**All about X.org**

Shortly before the New Year, AMD developer Alex Deucher [released rudimentary code](http://thread.gmane.org/gmane.comp.freedesktop.xorg.drivers.ati/6867/) for using the 3D features offered by the Radeon R600 (Radeon HD 2000 and 3000) and R700 (Radeon 4000) chip series. The code is currently intended for developers only, not for general use, but indicates, for example, how 3D features are addressed, so that it also acts as documentation. The plan is to use this information and parts of the recently released code to add extensive support for the 3D features of graphics chips, to drivers and Direct Rendering Managers (DRM). It is still likely to be a few months before end users can run Compiz, games and 3D applications on the latest generation of Radeon chips. [In his blog](http://emmes.livejournal.com/3435.html) and in [an e-mail](http://thread.gmane.org/gmane.comp.video.mesa3d.devel/11821) Radeonhd developer Matthias Hopf reveals some details of the experimental code and how to use it.

Between mid and late December, the X.org developers released [several new drivers](http://lists.freedesktop.org/archives/xorg-announce/2008-December/thread.html) and libraries, including new versions of xf86-video-{s3,s3virge,sis,vesa} and xf86-input-{synaptics,vmmouse}. There is a version 6.9.1 release candidate for the "ati" driver package which includes [many new features](http://lists.freedesktop.org/archives/xorg-announce/2008-December/000736.html), such as enhancements for HDMI and support for Radeon RV710 (Radeon HD 4300/HD 4500) and RV730 (Radeon HD 4600) chips. Developers working on the alternative radeonhd driver have something of a head start, with version 1.2.4 already supporting these chips and including enhancements for HDMI.

There is also an Intel driver 2.6 release candidate, which includes [a number of improvements](http://lists.freedesktop.org/archives/xorg-announce/2008-December/000714.html). Version 1.7.0 of the siliconmotion graphics driver is already complete and comes equipped with [a number of new features](http://lists.freedesktop.org/archives/xorg-announce/2008-December/000738.html).

**In Brief:**

- The [Zune Player](../site/news/item/30GB-Zunes-hibernating-for-2009-Update-2-739505.html "30GB Zunes hibernating for 2009? [Update 2] – 31 December 2008, 13:30") is not alone in having [come to grief over the New Year](http://thread.gmane.org/gmane.linux.kernel/774554/) – a number of Linux systems were also caught out. The code for dealing with the [leap second](http://en.wikipedia.org/wiki/Leap_second), added on New Year's Eve, was at fault. [A patch](http://thread.gmane.org/gmane.linux.kernel/774554/focus%3D774693) is now available to ensure that the problem does not arise the next time a leap second needs to be added.

<!-- -->

- A patch by Pavel Machek [published on LKML](http://thread.gmane.org/gmane.linux.documentation/336/) has triggered a wide-ranging debate on where ext3 can appropriately be used and the risks involved with its use, with and without barriers.

<!-- -->

- Three patches to enable a kernel to be compiled without Perl – required for building since 2.6.25 – have also triggered [long discussions](http://thread.gmane.org/gmane.linux.kernel/774297/) on LKML.

<!-- -->

- The [development team behind Gutenprint](http://gutenprint.sourceforge.net/) have released [version 5.2.3](http://sourceforge.net/project/shownotes.php?group_id=1537&release_id=649090) of the printer driver collection. The Hplip development team had previously released [version 2.8.12](http://sourceforge.net/forum/forum.php?forum_id=898971) of their drivers for HP printers and all-in-ones.

<!-- -->

- [As agreed at Kernel Summit 2008](http://lwn.net/Articles/298592/), the Kernel.org administrators have [set up](http://thread.gmane.org/gmane.linux.kernel/774129/) a patch tracing tool [patchwork](http://ozlabs.org/~jk/projects/patchwork/) at [patchwork.kernel.org](http://patchwork.kernel.org).

<!-- -->

- Despite security extension Grsecurity [perhaps heading for an untimely demise](../site/news/item/Grsecurity-needs-a-sponsor-to-survive-739543.html "Grsecurity needs a sponsor to survive – 05 January 2009, 12:04"), a number of users and fans have asked the kernel development team to include it in the Linux main development tree ([1](http://thread.gmane.org/gmane.linux.kernel/774825), [2](http://thread.gmane.org/gmane.linux.kernel/774825/focus%3D775126)). Torvalds [response, however, includes severe criticism](http://thread.gmane.org/gmane.linux.kernel/774825/focus%3D774824) of aspects of the implementation of Grsecurity.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: Higher and Further, The innovations of Linux 2.6.28](../site/open/features/Kernel-Log-Higher-and-Further-The-innovations-of-Linux-2-6-28-746519.html "Kernel Log: Higher and Further, The innovations of Linux 2.6.28 – 23 December 2008, 15:55")
- [Kernel Log: What's coming in 2.6.28 - Part 9: Fastboot and other remainders](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-9-Fastboot-and-other-remainders-739431.html "Kernel Log: What's coming in 2.6.28 - Part 9: Fastboot and other remainders – 19 December 2008, 12:45")
- [Kernel Log: What's coming in 2.6.28 - Part 7: architecture support, memory subsystem and virtualisation](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-7-architecture-support-memory-subsystem-and-virtualisation-739397.html "Kernel Log: What's coming in 2.6.28 - Part 7: architecture support, memory subsystem and virtualisation – 17 December 2008, 10:35")
- [Kernel Log: What's coming in 2.6.28 - Part 6: Changes to the audio drivers](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-6-Changes-to-the-audio-drivers-739369.html "Kernel Log: What's coming in 2.6.28 - Part 6: Changes to the audio drivers – 15 December 2008, 17:53")
- [Kernel Log: New kernel versions, progress with Btrfs and Tux3](../site/news/item/Kernel-Log-New-kernel-versions-progress-with-Btrfs-and-Tux3-739341.html "Kernel Log: New kernel versions, progress with Btrfs and Tux3 – 13 December 2008, 11:07")
- [Kernel Log: VIA co-operates with the open source developers of openChrome](../site/news/item/Kernel-Log-VIA-co-operates-with-the-open-source-developers-of-openChrome-738911.html "Kernel Log: VIA co-operates with the open source developers of openChrome – 21 November 2008, 14:56")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
