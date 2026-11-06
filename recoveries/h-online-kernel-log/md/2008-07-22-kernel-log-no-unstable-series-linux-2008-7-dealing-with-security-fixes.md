---
title: "Kernel Log: No unstable series; Linux 2008.7; dealing with security fixes"
date: 2008-07-22
author: "Terry Relph-Knight"
source: http://www.h-online.com/open/news/item/Kernel-Log-No-unstable-series-Linux-2008-7-dealing-with-security-fixes-736557.html
pages: 1
---

# Kernel Log: No unstable series; Linux 2008.7; dealing with security fixes

**Terry Relph-Knight**

![Kernel Log logo](../site/imgs/43/3/6/3/3/3/0/a345f5e7c547062f.jpg) Along with 2.6.27 development ramping up, there is a variety of other Linux kernel news. Shortly after the release of [Linux 2.6.26](../site/open/features/Polish-and-add-ons-the-latest-updates-in-Linux-2-6-26-746492.html "Polish and add-ons; the latest updates in Linux 2.6.26 – 18 July 2008, 10:22"), [someone on the Linux Kernel Mailing List (LKML) asked](http://thread.gmane.org/gmane.linux.kernel/706578) what sort of changes – either potentially or already in the works – might give rise to a 2.7 development series. Torvalds did not even wait 20 minutes to [respond](http://thread.gmane.org/gmane.linux.kernel/706578/focus%3D706594), "Nothing. I'm not going back to the old model. The new model is so much better that it's not even worth entertaining as a theory to go back."

The 2.6 series of Linux kernel development, which has been going on for several years now, is well established. In the old model, a 2.7 unstable series would lead to Linux 2.8 or 3.0, just as Linux 2.3 and 2.5 prepared the way for the 2.4 and 2.6 series. This is not expected to happen now. Since none of the changes introduced in the new kernel versions would justify a jump to version 2.8 or 3.0, Torvalds is thinking about changing the numbering scheme.

He does not want to simply drop the 2.6 prefix – he and others do not like such high version numbers. That is why he is [considering a model that roughly corresponds to the year and month](http://thread.gmane.org/gmane.linux.kernel/706578/focus%3D706594) – Linux 2.6.26 might then be called 2008.7. But he is also considering [other models, in which the year influences the first and second places](http://thread.gmane.org/gmane.linux.kernel/706578/focus%3D706626) – the next kernel version this year might be called 2.8.1, the first version next year would then be 2.9.1, and in 2010, it would be called 3.0.1. However, it is obvious that Torvalds does not have any concrete plan yet; perhaps the Linux father wants to continue to keep an eye on the discussion triggered by his statement and consider a new scheme more carefully with other kernel developers.

There were numerous debates accompanying the Linux Stable Team kernel version releases, echoing those that took place a few days ago with the release of [Linux 2.6.25.11](../site/news/item/Several-vulnerabilities-closed-in-the-Linux-kernel-736465.html "Several vulnerabilities closed in the Linux kernel – 14 July 2008, 12:41"), about how much and at what level of detail kernel developers should describe security-critical patches when releasing new kernel versions. These discussions got rather heated, especially once Torvalds himself weighed in ([1](http://thread.gmane.org/gmane.linux.kernel/701694/),[2](http://thread.gmane.org/gmane.linux.kernel/707127/)). He underscored that he simply wanted to fix the bugs – security-critical or not. He also made it clear that he disliked [embargoes](http://thread.gmane.org/gmane.linux.kernel/701694/focus%3D707301), bugs that, instead of being fixed immediately, are corrected and released only after coordinating with Linux distributors, adding that embargoes did not work anyway.

Developer Theodore Ts'o, known among other things for his work on the ext file systems, attempted to mediate and [explained](http://thread.gmane.org/gmane.linux.kernel/701694/focus%3D707301) the points of view of Torvalds and other developers. The discussion, as of the writing of this Kernel Log, can roughly be summed up as; Many kernel developers are very keen to work on fixes for security-critical bugs and other problems. They also admit to the bugs and stand behind their fixes. The work associated with publicly announcing bug fixes, which has become standard procedure in IT security circles – things like writing detailed bug reports or coordination with the Linux distributors – is in the eyes of some kernel developers make-work that can quickly add up using time that could better be used fixing actual bugs. That is why they prefer to leave this work to the [Linux kernel security team](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob;f=Documentation/SecurityBugs;hb=HEAD) and Linux distributors.

On the Japanese Linux Foundation site, several kernel developer presentations have recently been made available as PDF documents. These include presentations like "[The Completely Fair Scheduler](http://www.linux-foundation.jp/uploads/seminar20080709/lfjp2008.pdf)" by Thomas Gleixner, "[SELinux Project Overview](http://www.linux-foundation.jp/uploads/seminar20080709/James-SELinux.pdf)" by James Morris and "[Status and Direction of Kernel Development](http://www.linux-foundation.jp/uploads/seminar20080709/Andrew-symposium-2008.pdf)" by Andrew Morton. In the latter presentation, the number two kernel developer provides a close-up view of the development process and linux-next. Morton also describes problems with the available file system. Linux still does not have a file system compatible with SSDs (solid state drives) and ext4 only remedies some of the limitations of ext3. Morton is putting his long-term hopes on the not yet fully developed [Btrfs](http://btrfs.wiki.kernel.org/index.php/Main_Page).

**Kernel Log highlights**:

- [According to one of its developers](http://egbert-e.livejournal.com/1768.html), the radeonhd graphics driver now supports the recently introduced Radeon 4800 models.
- In his blog, kernel hacker Dave Jones [criticized Ubuntu developers](http://kernelslacker.livejournal.com/127218.html) who in his view did not adequately help to develop the Linux main development line. In a recent presentation at Google ([Video](http://youtube.com/watch?v=L2SED6sewRw), [Cycle Gap notes](http://cycle-gap.blogspot.com/2008/07/linux-kernel-development-stats-from.html)), Greg Kroah-Hartmann also emphasized that Ubuntu sponsor Canonical made very little contribution to kernel development.
- Following a period of relative inactivity over the past few weeks on the 2.6.16 kernel series, its administrator posted a [pre-release of 2.6.16.61](http://thread.gmane.org/gmane.linux.kernel/706432), praising its improvements.
- A [discussion among WLAN developers](http://thread.gmane.org/gmane.linux.kernel.wireless.general/17686/focus%3D17693) showed, once again, that even developers have different interpretations of the meaning of the CONFIG_EXPERIMENTAL kernel configuration flag.
- [The Systemtap developers](http://sourceware.org/systemtap/) have released version 0.7 of the debugging and analysis software.

*More information and background on developments in the Linux kernel and its environment can also be found in previous issues of the Kernel Log on heise open source:*

**Kernel Logs in brief:**

- 18.07.2008: [Polish and add-ons](../site/open/features/Polish-and-add-ons-the-latest-updates-in-Linux-2-6-26-746492.html "Polish and add-ons; the latest updates in Linux 2.6.26 – 18 July 2008, 10:22") – What's new in Linux 2.6.26
- 26.06.2008: [Kernel Log: New graphics drivers and stable kernels; details about Linux-staging](../site/news/item/Kernel-log-New-graphics-drivers-and-stable-kernels-details-about-Linux-staging-736303.html "Kernel log: New graphics drivers and stable kernels; details about Linux-staging – 26 June 2008, 15:45")
- 17.06.2008: [Kernel Log: Linux-staging branch will help with integration; Linux kernel 2.6.25.6 and 2.6.26-rc6](../site/news/item/Kernel-Log-Linux-staging-branch-will-help-with-integration-Linux-kernel-2-6-25-6-and-2-6-26-rc6-735507.html "Kernel Log: Linux-staging branch will help with integration; Linux kernel 2.6.25.6 and 2.6.26-rc6 – 17 June 2008, 11:31")
- 10.06.2008: [Kernel Log: Users of 2.4 provide feedback, 2.4.36.5 and 2.6.26-rc5 released](../site/news/item/Kernel-Log-Users-of-2-4-provide-feedback-2-4-36-5-and-2-6-26-rc5-released-735437.html "Kernel-Log: Users of 2.4 provide feedback, 2.4.36.5 and 2.6.26-rc5 released – 10 June 2008, 15:20")
- 30.05.2008: [Kernel Log: new gfx drivers for GeForce & Radeon GPUs; Kernel Track at LinuxTAG](../site/news/item/Kernel-log-new-gfx-drivers-for-GeForce-Radeon-GPUs-Kernel-Track-at-LinuxTAG-735349.html "Kernel log: new gfx drivers for GeForce & Radeon GPUs; Kernel Track at LinuxTAG – 30 May 2008, 14:23")

*Older Kernel Logs can be found in [the archive](http://www.heise-online.co.uk/open/news/archive/) or using [the search function](http://www.heise-online.co.uk/open/search/) on [heise online UK Open Source](http://www.heise-online.co.uk/open/).*

([trk](mailto:trk@h-online.com "Terry Relph-Knight"))
