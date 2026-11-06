---
title: "Kernel Log: Kernel Summit info; Plumbers keynote online; the latest on the e1000e problem"
date: 2008-09-26
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-Kernel-Summit-info-Plumbers-keynote-online-the-latest-on-the-e1000e-problem-737443.html
pages: 1
---

# Kernel Log: Kernel Summit info; Plumbers keynote online; the latest on the e1000e problem

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/4/2/1/4/93e8ea3d0acdf147.jpg) Following the two Kernel Logs last week ([1](../site/news/item/Kernel-Log-Hard-core-Linux-developers-discuss-the-future-of-Linux-at-the-Kernel-Summit-737327.html "Kernel-Log: Hard core Linux developers discuss the future of Linux at the Kernel Summit – 17 September 2008, 11:48"),[2](../site/news/item/Kernel-Log-The-second-day-of-Kernel-Summit-2008-criticism-of-Ubuntu-at-the-opening-of-the-Linux-Plumbers-Conference-737379.html "Kernel Log: The second day of Kernel Summit 2008; criticism of Ubuntu at the opening of the Linux Plumbers Conference – 19 September 2008, 15:58")) which summarised the salient information from the LWN.net Kernel Summit 2008 reports available only to subscribers, the [LWN.net articles are now available](http://lwn.net/Articles/KernelSummit2008/) to anyone who wants to know exactly what went on. Other sources of information from the conference, which was open only to invited kernel developers, are still hard to come by.

On the Linux Kernel Mailing List (LKML), initial results of the developer conference are evident. Kernel hackers [decided](http://lwn.net/Articles/298570/) to integrate the [Linux-staging](../site/news/item/Kernel-Log-Linux-staging-branch-will-help-with-integration-Linux-kernel-2-6-25-6-and-2-6-26-rc6-735507.html "Kernel Log: Linux-staging branch will help with integration; Linux kernel 2.6.25.6 and 2.6.26-rc6 – 17 June 2008, 11:31") development branch more fully into the main development branch. Greg Kroah-Hartman took the first steps in this direction with his [patch series](http://thread.gmane.org/gmane.linux.kernel/736852) sent as an RFC to the LKML.

This means that drivers that are not ready to be merged into the Kernel, which until now have been stored in a separately administered staging branch, will be moved to the main development branch in a `drivers/staging/` folder. This is intended both to help the kernel developers to keep a better eye on the drivers, and to motivate the hackers to improve them. The kernel will flag such drivers with a `TAINT_CRAP` flag so that developers will not spend time investigating error messages from systems in which one these sub-par drivers were active.

------------------------------------------------------------------------

Numerous kernel and distribution developers are feverishly at work on the e1000e driver and the [problem](../site/news/item/Intel-e1000e-user-Don-t-install-the-new-SUSE-betas-737395.html "Intel e1000e user? Don't install the new SUSE betas – 23 September 2008, 09:14") associated with it that renders Intel PCI Express gigabit network chips useless. So far, it does not appear that either a solution or the exact cause of the overwriting of data in the network chip's EEPROM is anywhere in sight. It is therefore, not surprising, that the information contained in various [blogs](http://blog.mandriva.com/2008/09/23/urgent-notification-major-bug-in-all-mandriva-linux-2009-pre-releases/), [bug trackers](http://bugzilla.kernel.org/show_bug.cgi?id=11382), and mailing list postings sometimes contradicts itself.

For security reasons numerous distributions have now deactivated the drivers in their development branches. The drivers are for the most part programmed and maintained by Intel. Intel employee Jesse Brandeburg strongly advises users to back up EEPROM [to a file](http://bugzilla.kernel.org/show_bug.cgi?id=11382#c17) – a program that will use the resulting file to reinstall the data is under development. Others specifically advise against trying to perform the repair using the Intel Boot Agent utility.

In reports on the issue, there is consensus that the bug only occurs in pre-releases of Linux 2.6.27 on motherboards that use the network functions on the ICH8 and ICH9 Intel southbridges. Discussions on the LKML indicate that it may not necessarily be the driver that is causing the problem. Bug reports from affected users indicate that perhaps the X server, other hardware-related user space programs, or the still relatively new PAT support may at least be part of the problem. Considering the number of kernel hackers working on the problem, the exact cause and at its solution are likely to be found soon. For the time being, kernel and X hacker Dave Airlie is using his notebook as a paperweight as [testing continues](http://article.gmane.org/gmane.linux.kernel.kernel-testers/1653/).

------------------------------------------------------------------------

A video of the keynote speech that Greg Kroah-Hartman delivered at the opening of the Linux Plumbers Conference is now [available on Google Video](http://video.google.com/videoplay?docid=3385088017824733336). In the speech the kernel hacker sharply criticised Ubuntu sponsor Canonical and its employees for their lacklustre contribution to the Linux kernel and other basic Linux software. In his [blog](http://www.kroah.com/log/linux/lpc_2008_law_and_gospel.html), he discusses his speech in greater detail – he [posted](http://www.kroah.com/log/linux/lpc_2008_keynote.html) the slides from his presentation last week. Meanwhile, Ubuntu developers have started their [Ubuntu Upstream Report](https://edge.launchpad.net/ubuntu/+upstreamreport#), which has been in preparation for some time. The report is intended to help feed Ubuntu bug reports to upstream projects. Ubuntu developer Jorge describes the background and goals of the report [on his blog](http://stompbox.typepad.com/blog/2008/09/introducing-the.html).

**Kernel Log highlights**

- Neil Brown has made an early pre-release version of mdadm 3.0 [available](http://thread.gmane.org/gmane.linux.raid/20086). mdadm, like dmraid in conjunction with add-on patches, can access a RAID5 connection set up with the RAID functions of the current Intel southbridges

<!-- -->

- Linus Torvalds has approved the seventh pre-release of [Linux 2.6.27](http://thread.gmane.org/gmane.linux.kernel/735406).

<!-- -->

- The Mesa project has released [Mesa version 7.2](http://www.mesa3d.org./relnotes-7.2.html), which has for the most part remedied the bugs in version 7.1.

<!-- -->

- In response to repeated questions on adherence to the GPL in VMware's ESX Server, [research conducted by CNET](http://news.cnet.com/8301-13505_3-10044214-16.html) indicates that VMware has included an explicit notice about the use of open source software and issued a warning on the potential for legal claims.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: The second day of Kernel Summit 2008; criticism of Ubuntu at the opening of the Linux Plumbers Conference](../site/news/item/Kernel-Log-The-second-day-of-Kernel-Summit-2008-criticism-of-Ubuntu-at-the-opening-of-the-Linux-Plumbers-Conference-737379.html "Kernel Log: The second day of Kernel Summit 2008; criticism of Ubuntu at the opening of the Linux Plumbers Conference – 19 September 2008, 15:58")
- [Kernel-Log: Hard core Linux developers discuss the future of Linux at the Kernel Summit](../site/news/item/Kernel-Log-Hard-core-Linux-developers-discuss-the-future-of-Linux-at-the-Kernel-Summit-737327.html "Kernel-Log: Hard core Linux developers discuss the future of Linux at the Kernel Summit – 17 September 2008, 11:48")
- [Kernel-Log: New stable and developer kernel, Mesa 7.1 and X-Server 1.5 released](../site/news/item/Kernel-Log-New-stable-and-developer-kernel-Mesa-7-1-and-X-Server-1-5-released-737227.html "Kernel-Log: New stable and developer kernel, Mesa 7.1 and X-Server 1.5 released. – 09 September 2008, 15:02")
- [Kernel Log: New stable and pre-release kernels, Ubuntu 8.10 with 2.6.27?](../site/news/item/Kernel-Log-New-stable-and-pre-release-kernels-Ubuntu-8-10-with-2-6-27-737021.html "Kernel Log: New stable and pre-release kernels, Ubuntu 8.10 with 2.6.27? – 25 August 2008, 11:32")
- [Kernel Log: New video drivers for AMD, Intel, Nvidia and VIA hardware](../site/news/item/Kernel-Log-New-video-drivers-for-AMD-Intel-Nvidia-and-VIA-hardware-736997.html "Kernel Log: New video drivers for AMD, Intel, Nvidia and VIA hardware – 22 August 2008, 11:59")
- [Kernel Log: Kernel development explained, new Synaptics driver, Linux 2.6.27-rc3 published](../site/news/item/Kernel-Log-Kernel-development-explained-new-Synaptics-driver-Linux-2-6-27-rc3-published-736911.html "Kernel Log: Kernel development explained, new Synaptics driver, Linux 2.6.27-rc3 published – 15 August 2008, 11:13")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
