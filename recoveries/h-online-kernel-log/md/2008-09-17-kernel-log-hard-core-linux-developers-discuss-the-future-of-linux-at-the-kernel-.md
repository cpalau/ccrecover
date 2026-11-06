---
title: "Kernel-Log: Hard core Linux developers discuss the future of Linux at the Kernel Summit"
date: 2008-09-17
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-Hard-core-Linux-developers-discuss-the-future-of-Linux-at-the-Kernel-Summit-737327.html
pages: 1
---

# Kernel-Log: Hard core Linux developers discuss the future of Linux at the Kernel Summit

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/4/0/9/8/93e8ea3d0acdf147.jpg) Linus Torvalds, Andrew Morton and eighty other important kernel developers are now debating how they plan to proceed with the future development of Linux at the [Kernel Summit 2008](http://www.linuxfoundation.org/events/kernel) in Portland, Oregon. They are less concerned with drawing up a road map or working on specifying new kernel functions – the former doesn't exist and the latter is part of the day-to-day business on the Linux Kernel Mailing List (LKML).

What they are doing is exchanging experiences and discussing the most fundamental issues around the Linux kernel, because these are things that don't work so well on mailing lists. So there are many process questions on the [conference agenda](https://lists.linux-foundation.org/pipermail/ksummit-2008-discuss/2008-September/000632.html) such as what is the procedure for developing and releasing new versions and how are drivers included or removed from the kernel.

Jonathan Corbet, co-founder and executive editor of [Linux Weekly News](http://lwn.net) (LWN), who is also a kernel developer, is reporting on the conference in detail on LWN.net. Until the 25th of September though, [his articles](http://lwn.net/Articles/298587/) on the various topics will only be available to LWN.net subscribers. Other news sources are scarce, and what the kernel developers have been agreeing on only gradually leaks out via blogs or postings on the LKML.

According to one report on LWN.net, a proposal submitted in advance by Alan Cox as an [email](https://lists.linux-foundation.org/pipermail/ksummit-2008-discuss/2008-August/000557.html), that outmoded and now little used drivers and subsystems should be removed and that the resulting kernel versions should be identified with a jump in version number to 2.8 or 3.0, met with no acceptance from his fellow kernel developers. Torvalds in particular is reported to have opposed the idea, emphasizing that maintaining old drivers and subsystems required hardly any work and that some hardware that kernel developers considered antiquated and no longer widely used was still in use in many parts of the world. So it looks as though support for the ISA bus and for the first generation of Video-4-Linux will remain in the kernel for the foreseeable future at least, and not be eliminated as Cox had proposed.

There were also discussions on what would be the best time to incorporate new drivers. One camp opined that only reasonably mature drivers should be integrated, because that was the only way to put pressure on driver programmers to improve their code. The other camp wanted drivers to be incorporated as soon as possible as long as their Userspace API was mature and no obvious security holes could be found. Even bad drivers would usually quickly improve by being accepted into the kernel, they said, because more developers were working on the drivers contained in the kernel than were doing so on separately managed drivers.

Torvalds was a member of the second camp, whose strategy largely corresponds with what the kernel developers have already been doing in the last two to three years in further developing the 2.6 series. The developers want to continue this practice even after the discussion, but in preparing drivers for acceptance into the main line of development of Linux, more importance should be given to [Linux staging](../site/news/item/Kernel-Log-Linux-staging-branch-will-help-with-integration-Linux-kernel-2-6-25-6-and-2-6-26-rc6-735507.html "Kernel Log: Linux-staging branch will help with integration; Linux kernel 2.6.25.6 and 2.6.26-rc6 – 17 June 2008, 11:31"). Its maintainer, Greg Kroah-Hartman, stressed that the kernel tree, which was still quite new, had been a big success and had helped to improve the drivers contained there.

Many other things were also discussed. Dave Jones, a long-standing kernel hacker and a leading kernel maintainer in the Fedora project, brought up the subject of Initramfs/Initrd, arguing for unification of the userland code running in the context of the Initramfs to link in the Root-filing system and for it to be managed together with the kernel so that when changes are made to the kernel the code can be adapted to them immediately. Mini-summits were held to discuss status and plans regarding power management, container virtualisation, and wireless support.

At the end of the first day of the conference, talk was generally about improving the quality of the Linux kernel and the procedure to be followed in developing and releasing new versions. Among other things, Torvalds would like [kernel oops reports](http://kerneloops.org/) to reach more developers so that they will spot and eliminate bugs. As part of the discussion of shortening the development cycle, a development period of approximately six weeks for every new kernel version was considered, with a merge window of only one week. This was almost decided on, but was then again rejected following further discussion.

Apart from an incidental mention in the report on Cox's proposal, none of the LWN.net articles deals in more detail with a new numbering pattern. Whether there will soon be a Linux 2.8.0, 3.0.0 or 2008.10, as [suggested by Torvalds himself a few weeks ago](../site/news/item/Kernel-Log-No-unstable-series-Linux-2008-7-dealing-with-security-fixes-736557.html "Kernel Log: No unstable series; Linux 2008.7; dealing with security fixes – 22 July 2008, 01:47"), is therefore still uncertain. It's possible that they are discussing this on the second day of the Kernel Summit, on which LWN.net plans to report in detail.

At the close of the day's programme, six new members of the [Technical Advisory Board](http://www.linuxfoundation.org/en/Technical_Advisory_Board_%28Table%29), TAB, of the Linux Foundation [will be elected](http://thread.gmane.org/gmane.linux.kernel/724063/focus%3D733589) – the date for the election was set so that those concerned would all be at the same place and non-kernel developers at the [Linux Plumbers Conference](http://linuxplumbersconf.org/) could also take part.

**In Brief**

- Almost a week ago, Linus Torvalds [released kernel version 2.6.27-rc6](http://thread.gmane.org/gmane.linux.kernel/731802), which currently includes [updated lists](http://thread.gmane.org/gmane.linux.kernel.kernel-testers/1420) of the errors that have occurred since 2.6.26 and other unsolved problems.

<!-- -->

- The X.org synaptics touchpad driver administrator has released new driver versions [0.15.1](http://list.freedesktop.org/archives/xorg-announce/2008-September/000651.html) and [2003/000652.html 0.15.2](http://list.freedesktop.org/archives/xorg-announce/2008-September), which are mainly bug fixes of errors in preceding versions.

<!-- -->

- Mesa 7.1 is not yet one month old, but the Mesa developers are already preparing [version 7.2](http://thread.gmane.org/gmane.comp.video.mesa3d.announce/65), which will be the new stable release, fixing issues with the 7.1 development release.

<!-- -->

- X.org 7.4 was supposed to have been released last Wednesday – so far though, nothing has been seen of the new X.org package. The developers [are now planning](http://list.freedesktop.org/archives/xorg/2008-September/038474.html) roughtly X server versions 1.6 and 1.7, as well as X.org 7.5 , which will be based on X server 1.7.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel-Log: New stable and developer kernel, Mesa 7.1 and X-Server 1.5 released](../site/news/item/Kernel-Log-New-stable-and-developer-kernel-Mesa-7-1-and-X-Server-1-5-released-737227.html "Kernel-Log: New stable and developer kernel, Mesa 7.1 and X-Server 1.5 released. – 09 September 2008, 15:02")
- [Kernel Log: New stable and pre-release kernels, Ubuntu 8.10 with 2.6.27?](../site/news/item/Kernel-Log-New-stable-and-pre-release-kernels-Ubuntu-8-10-with-2-6-27-737021.html "Kernel Log: New stable and pre-release kernels, Ubuntu 8.10 with 2.6.27? – 25 August 2008, 11:32")
- [Kernel Log: New video drivers for AMD, Intel, Nvidia and VIA hardware](../site/news/item/Kernel-Log-New-video-drivers-for-AMD-Intel-Nvidia-and-VIA-hardware-736997.html "Kernel Log: New video drivers for AMD, Intel, Nvidia and VIA hardware – 22 August 2008, 11:59")
- [Kernel Log: Kernel development explained, new Synaptics driver, Linux 2.6.27-rc3 published](../site/news/item/Kernel-Log-Kernel-development-explained-new-Synaptics-driver-Linux-2-6-27-rc3-published-736911.html "Kernel Log: Kernel development explained, new Synaptics driver, Linux 2.6.27-rc3 published – 15 August 2008, 11:13")
- [Kernel Log: Ath9k driver for Atheros Wifi in 2.6.27; reading material and videos for Linux experts](../site/news/item/Kernel-Log-Ath9k-driver-for-Atheros-Wifi-in-2-6-27-reading-material-and-videos-for-Linux-experts-736829.html "Kernel Log: Ath9k driver for Atheros Wifi in 2.6.27; reading material and videos for Linux experts – 11 August 2008, 11:36")
- [Kernel Log: Btrfs 0.16 released, new stable kernels released, Wifi drivers for 2.6.27 merged](../site/news/item/Kernel-Log-Btrfs-0-16-released-new-stable-kernels-released-Wifi-drivers-for-2-6-27-merged-736815.html "Kernel Log: Btrfs 0.16 released, new stable kernels released, Wifi drivers for 2.6.27 merged – 08 August 2008, 14:32")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
