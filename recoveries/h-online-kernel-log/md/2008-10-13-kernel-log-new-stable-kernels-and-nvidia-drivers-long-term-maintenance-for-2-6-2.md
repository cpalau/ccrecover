---
title: "Kernel Log: New stable kernels and Nvidia drivers, long-term maintenance for 2.6.27"
date: 2008-10-13
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-New-stable-kernels-and-Nvidia-drivers-long-term-maintenance-for-2-6-27-737641.html
pages: 1
---

# Kernel Log: New stable kernels and Nvidia drivers, long-term maintenance for 2.6.27

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/4/4/1/2/93e8ea3d0acdf147.jpg) Almost in parallel with the [release of Linux 2.6.27](../site/open/features/Kernel-Log-Linux-2-6-27-Released-746496.html "Kernel Log: Linux 2.6.27 Released – 10 October 2008, 08:38") at the end of last week, the maintainers of the Linux stable series have also released two new kernels, [2.6.25.18](http://thread.gmane.org/gmane.linux.kernel/742146) and [2.6.26.6](http://thread.gmane.org/gmane.linux.kernel/742149). Both kernels offer a number of minor corrections and improvements over the two previous series 2.6.*x* kernel versions. As it has become [customary with the stable series](http://www.heise-online.co.uk/open/Kernel-Log-Linux-2-6-27-Released--/features/111671/5#trust), it remains unclear whether the updates to the two kernels also resolve security issues.

Adrian Bunk has announced that he intends to [maintain the 2.6.27 kernel in the long term](http://thread.gmane.org/gmane.linux.kernel/742570/focus%3D743377), turning it into a "longtime supported kernel". He wants to take over the maintenance of the 2.6.27 kernel series when the maintainers of the Linux stable series stop their support – this should happen just before or shortly after the release of Linux 2.6.29, which is due in about five to six months according the general maintenance strategy.

Bunk wants to offer users an alternative to the distribution kernels which are only sometimes maintained for a long period of time. He admits that the group of users interested in this project *"might be a small part of the userbase..."*. In his announcement, the kernel hacker also had to concede that he recently hasn't quite kept up the maintenance of Linux kernel series 2.6.16.*x*, which is also his responsibility. He plans to rectify this shortly and maintain 2.6.16.*x* at least until mid 2009.

This would keep 2.6.16 maintained for at least three years and four months. The kernel developers usually only maintain the two latest 2.6.*x* kernels, giving each version a maintenance cycle of about five to six months. Some of the kernels of the Red Hat and Novell Enterprise distributions are maintained for more than seven years; non-paying customers also get to enjoy this level of support through free clones of those distributions, such as [CentOS](http://www.centos.org/).

Following the release of [Linux 2.6.27](../site/open/features/Kernel-Log-Linux-2-6-27-Released-746496.html "Kernel Log: Linux 2.6.27 Released – 10 October 2008, 08:38"), Linus Torvalds has published some [thoughts about the new kernel's release](http://torvalds-family.blogspot.com/2008/10/on-making-releases.html) in his new personal blog and James Morris has posted a [blog entry](http://james-morris.livejournal.com/35287.html) summarising once more the details of the SELinux improvements in 2.6.27.

In the last few days, Linus Torvalds has already integrated 3000 commits into the main development branch of Linux which will be used to produce Linux version 2.6.28 in about three months. Once the patches are reviewed a future kernel log will examine the changes in the various kernel areas in a few days.

After numerous beta versions in the past few weeks and months, Nvidia has released the new version 177.80 of its [proprietary graphics drivers](http://www.nvidia.com/object/unix.html) for [x86-32](http://www.nvidia.com/object/linux_display_ia32_177.80.html) and [x86-64](http://www.nvidia.com/object/linux_display_amd64_177.80.html) systems. The new versions have been created solve some of the severe performance problems that the previous driver versions had when working with recent graphics cards and running KDE 4 or Firefox.

Nvidia also improved the drivers to support several new graphics cards and chipsets – including the GTX series GeForce models as well as various series 9 models. What Nvidia doesn't point out in great detail in the release notes: the new driver [no longer supports GeForce series 5 graphics cards](http://us.download.nvidia.com/XFree86/Linux-x86/177.80/README/appendix-a.html). The vendor intends to service those models with the 173.14.*xx* series of drivers – which will make it Nvidia's third "legacy" driver series. How much or little effort the vendor puts into these projects can be seen with X.org's X Server 1.5 in [X.org 7.4](../site/news/item/X-org-7-4-comes-complete-with-new-functions-new-drivers-and-new-incompatibilities-737419.html "X.org 7.4 comes complete with new functions, new drivers and new incompatibilities – 24 September 2008, 15:48"). This server isn't even supported by the latest series 71.86.*xx* and 96.43.*xx* legacy drivers. Users of Fedora 9 have already felt the consequences since last May, as Fedora 9 includes a pre-release version of this X Server. Other distributions, however, have also begun to supply the new X Server in the meantime; Ubuntu 8.10 will be joining their ranks soon.

**In Brief**

- [X Server 1.5.2](http://lists.freedesktop.org/archives/xorg-announce/2008-October/000662.html) corrects several bugs in the X Server shipped with [X.org 7.4](../site/news/item/X-org-7-4-comes-complete-with-new-functions-new-drivers-and-new-incompatibilities-737419.html "X.org 7.4 comes complete with new functions, new drivers and new incompatibilities – 24 September 2008, 15:48").

<!-- -->

- On the Alsa mailing list, [Takashi Iwai has introduced a first version of sbxfi](http://mailman.alsa-project.org/pipermail/alsa-devel/2008-October/011270.html), his very experimental and embryonic driver that supports several sound cards from Creative's X-Fi series.

<!-- -->

- There has recently been quite a stir in the media about a supposedly new and partially [proprietary Linux driver](http://www.broadcom.com/support/802.11/linux_sta.php) for Wi-Fi hardware by Broadcom – as it turns out, however, Broadcom already quietly released this driver at the beginning of June and some distributions have included it for since then.

<!-- -->

- In the article *[Powering down](http://portal.acm.org/citation.cfm?id=1378740)*, which can be downloaded free of charge at [ACM](http://www.acm.org/), kernel developer Matthew Garrett discusses several general and Linux specific power management aspects.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: Linux 2.6.27 Released](../site/open/features/Kernel-Log-Linux-2-6-27-Released-746496.html "Kernel Log: Linux 2.6.27 Released – 10 October 2008, 08:38")
- [Kernel Log: problem with e1000e bypassed, Morton praises Btrfs](../site/news/item/Kernel-Log-problem-with-e1000e-bypassed-Morton-praises-Btrfs-737561.html "Kernel Log: problem with e1000e bypassed, Morton praises Btrfs – 07 October 2008, 08:47")
- [Kernel Log: 2.6.27 nearing completion; Btrfs to be added to the kernel?](../site/news/item/Kernel-Log-2-6-27-nearing-completion-Btrfs-to-be-added-to-the-kernel-737489.html "Kernel Log: 2.6.27 nearing completion; Btrfs to be added to the kernel? – 01 October 2008, 09:23")
- [Kernel Log: Kernel Summit info; Plumbers keynote online; the latest on the e1000e problem](../site/news/item/Kernel-Log-Kernel-Summit-info-Plumbers-keynote-online-the-latest-on-the-e1000e-problem-737443.html "Kernel Log: Kernel Summit info; Plumbers keynote online; the latest on the e1000e problem – 26 September 2008, 10:59")
- [Kernel Log: The second day of Kernel Summit 2008; criticism of Ubuntu at the opening of the Linux Plumbers Conference](../site/news/item/Kernel-Log-The-second-day-of-Kernel-Summit-2008-criticism-of-Ubuntu-at-the-opening-of-the-Linux-Plumbers-Conference-737379.html "Kernel Log: The second day of Kernel Summit 2008; criticism of Ubuntu at the opening of the Linux Plumbers Conference – 19 September 2008, 15:58")
- [Kernel Log: Hard core Linux developers discuss the future of Linux at the Kernel Summit](../site/news/item/Kernel-Log-Hard-core-Linux-developers-discuss-the-future-of-Linux-at-the-Kernel-Summit-737327.html "Kernel-Log: Hard core Linux developers discuss the future of Linux at the Kernel Summit – 17 September 2008, 11:48")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
