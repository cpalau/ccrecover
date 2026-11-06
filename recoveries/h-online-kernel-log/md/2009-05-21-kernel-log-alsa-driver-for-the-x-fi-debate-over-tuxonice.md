---
title: "Kernel Log: ALSA driver for the X-Fi, debate over TuxOnIce"
date: 2009-05-21
author: "Terry Relph-Knight"
source: http://www.h-online.com/open/news/item/Kernel-Log-ALSA-driver-for-the-X-Fi-debate-over-TuxOnIce-741673.html
pages: 1
---

# Kernel Log: ALSA driver for the X-Fi, debate over TuxOnIce

**Terry Relph-Knight**

![Kernel Log Penguin](../site/imgs/43/3/6/8/1/0/5/93e8ea3d0acdf147.jpg)

#### by Thorsten Leemhuis

**The Linux kernel will soon include a driver for Creative's X-Fi sound cards. After a long pause, the kernel development team are once again debating merging TuxOnIce.**

ALSA and kernel developer Takashi Iwai has received an open source driver for X-Fi PCI sound cards from Creative, which he evaluates as being of a sufficiently high standard to be included in the [ALSA driver package](http://www.alsa-project.org/) and the Linux kernel. Not being a proud X-Fi owner, however, he has been unable to test the snd-ctxfi driver himself and has therefore called on users who do own an X-Fi card to give the driver a whirl – and over the last few days several users have indeed done so, providing [plenty of feedback](http://mailman.alsa-project.org/pipermail/alsa-devel/2009-May/thread.html#17332).

The odds look good that the new driver will find its way into the next version of ALSA and into version 2.6.31 of the Linux kernel. This should be the end of a long odyssey for X-Fi sound card Linux drivers. Creative originally made repeated promises of a proprietary driver, but never delivered. A preliminary version of the driver was released in 2007, but it had so many rough edges as to be more or less unusable. An open source driver for the more or less obsolete Open Sound System (OSS) was released out of the blue in [early 2008](../site/news/item/Creative-Labs-opens-up-driver-development-734163.html "Creative Labs opens up driver development – 09 February 2008, 13:08"), and there were also reports that Creative planned to provide open source developers with documentation for their sound chips. This was followed by another long silence, before Creative finally released their own open source driver [in November](../site/news/item/Kernel-Log-New-kernels-open-audio-drivers-for-X-Fi-738061.html "Kernel Log: New kernels, open audio drivers for X-Fi – 11 November 2008, 10:03"). However this driver again proved to be a little too rough and ready and was taken up by only a small number of distributions. The snd-ctxfi driver should be spared this fate, since its merger into the kernel will see it included in most new distributions.

**Back again**

By contrast, one odyssey which doesn't look like coming to an end is that of [TuxOnIce](http://www.tuxonice.net/). Now however, TuxOnIce developer Nigel Cunningham is once again petitioning [for the merger](http://thread.gmane.org/gmane.linux.power-management.general/14104) of the alternative suspend to disk and hibernation framework. This is not Cunningham's first shot at this, in fact the developer behind previous frameworks Suspend2 and Swsusp2 (Software Suspend 2) has made many previous attempts to have the framework adopted.

However, as before, the developers responsible for the kernel's software suspend support have once again rejected its inclusion. [One reason given for this](http://thread.gmane.org/gmane.linux.power-management.general/14104/focus%3D14248) was that they did not wish to maintain two suspend to disc technologies within the kernel in parallel or to simply replace the tried and tested Linux code with the TuxOnIce code, which offers both advantages and disadvantages and is not as well tested. Additionally, before being merged the TuxOnIce code would require auditing – a daunting task in view of the volume of code.

The proposed solution once again boils down to the suggestion that the TuxOnIce developer should split his code into bite-sized chunks, which would gradually enhance the kernel's software suspend support, so that the process would produce a reliable solution which satisfies all users and developers. This may prove more successful than past attempts, as Rafael J. Wysocki, who is primarily involved in developing the Linux kernel's software suspend code, has shown [more persistent](http://thread.gmane.org/gmane.linux.power-management.general/14104/focus%3D14248) interest in collaborating with Cunningham than on previous occasions, even heading off Pavel Machek, the official administrator of software suspend support and [declaring](http://thread.gmane.org/gmane.linux.power-management.general/14104/focus%3D14173) that he did not plan on taking part in flame wars between the two this time round.

**Kernel status**

- Following the release of [2.6.27.23](http://thread.gmane.org/gmane.linux.kernel/834235) and [2.6.29.3](http://thread.gmane.org/gmane.linux.kernel/834236) on 9th May, the stable series administrators this morning released kernel versions [2.6.27.24](http://thread.gmane.org/gmane.linux.kernel/839011) and [2.6.29.4](http://thread.gmane.org/gmane.linux.kernel/839013). As usual, all users of older versions of kernel.org kernels "*are very strongly encouraged to upgrade.*". It is not clear, however, whether the dozens of minor enhancements and bug fixes also include fixes to security vulnerabilities.

<!-- -->

- The development process for kernel 2.6.30 has now reached the [sixth pre-release version](http://article.gmane.org/gmane.linux.kernel/798141).

**X status**

- As usual, in parallel to its Catalyst graphics drivers for Windows, AMD has also made version 9.5 of the Linux version of the drivers available [for download](http://support.amd.com/us/gpudownload/Pages/index.aspx). The [release notes](http://www2.ati.com/drivers/linux/catalyst_95_linux.pdf)![PDF](../site/icons/file-pdf.gif "PDF document") list some of the fixes in the new version; no new features are listed. Version 9.5 of the proprietary graphics driver is, however, just as incompatible with the latest Linux kernel, version 2.6.29, [released in March](../site/open/features/Steady-growth-What-s-new-in-Linux-2-6-29-746553.html "Steady growth - What's new in Linux 2.6.29 – 24 March 2009, 15:26"), as its predecessors.

<!-- -->

- The developers of the open source driver for Intel hardware have released [version 2.7.1](http://lists.freedesktop.org/archives/xorg-announce/2009-May/000846.html). It includes a number of changes which should put paid to the crashes which occur with version 2.7.0.

<!-- -->

- AMD staffer Alex Deucher has recently announced the release of a "[R6xx/R7xx 3D programming guide](http://www.x.org/docs/AMD/R6xx_R7xx_3D.pdf)"![PDF](../site/icons/file-pdf.gif "PDF document"), which contains a wide range of information on programming 3D graphics drivers for the GPUs used in the Radeon HD 2000, 3000 and 4000 series.

**Kernel Log in brief**

- The development team behind the [Ksplice framework](http://www.ksplice.com/), which allows many security-related Linux kernel bugs to be patched at runtime, have won the \$100,000 prize in the Massachusetts Institute of Technology's (MIT) [100k competition](http://www.mit100k.org/). The KSplice development team are currently actively working on merging the kernel portion of their code into the Linux main development tree. The odds of the code being adopted look good, though it is not yet clear when this is likely to take place.

<!-- -->

- Jeremy Fitzhardinge has sent a series of groups of patches to LKML for evaluation. The patches add kernel support for operation as hypervisor-controlling Xen domains (Dom0) (see also [The free Xen 3.4 hypervisor and virtualisation strategy](../site/news/item/The-free-Xen-3-4-hypervisor-and-virtualisation-strategy-741645.html "The free Xen 3.4 hypervisor and virtualisation strategy – 19 May 2009, 16:24")). Various kernel hackers have expressed in some cases major reservations about portions of the patches in discussions and on the "[Where do we stand with the Xen patches?](http://thread.gmane.org/gmane.comp.emulators.xen.devel/66041)" thread. It therefore currently looks unlikely, though not impossible, that Linux 2.6.31 will include Xen Dom0 support.

<!-- -->

- [Since the start of this month](http://thread.gmane.org/gmane.linux.kernel/831676/focus%3D835188), Jon Masters has been producing an "[LKML Summary Podcast](http://podcasts.jonmasters.org/kernel/kernel.xml)", in which he briefly summarises the most important discussions on LKML. A text versions is available on the [Kernel Newbies wiki](http://kernelnewbies.org/KernelPodcast).

<!-- -->

- The [SANE](http://www.sane-project.org/) (Scanner Access Now Easy) project has released [version 1.0.20](http://lists.alioth.debian.org/pipermail/sane-announce/2009/000026.html) of the SANE back end. It contains four new drivers and supports 75 scanners not supported in the previous version.

<!-- -->

- Luis R. Rodriguez, an old hand in the Linux WLAN driver field and nowadays also an old hand at Atheros [recently publicly asked](http://thread.gmane.org/gmane.linux.drivers.madwifi.project/111) whether it was time to kill MadWifi development, since the kernel drivers were now able to address all hardware supported by the MadWifi driver. Some users and developers were, however, far from thrilled by the suggestion, as can be seen from some of the [contributions to the discussion](http://article.gmane.org/gmane.linux.drivers.madwifi.project/115).

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the Kernel Log at The H Open Source:*

- [Kernel Log: What's coming in 2.6.30 - Storage: RAID improvements, optimised CFQ Scheduler, SAS drivers](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-Storage-RAID-improvements-optimised-CFQ-Scheduler-SAS-drivers-741597.html "Kernel Log: What's coming in 2.6.30 - Storage: RAID improvements, optimised CFQ Scheduler, SAS drivers – 15 May 2009, 17:01")
- [Kernel Log: X.org 7.5 coming in summer, re-write for Intel's graphics driver](../site/news/item/Kernel-Log-X-org-7-5-coming-in-summer-re-write-for-Intel-s-graphics-driver-741405.html "Kernel Log: X.org 7.5 coming in summer, re-write for Intel's graphics driver – 04 May 2009, 07:09")
- [Kernel Log: What's coming in 2.6.30 - File systems: New and revamped file systems](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-File-systems-New-and-revamped-file-systems-741319.html "Kernel Log: What's coming in 2.6.30 - File systems: New and revamped file systems – 27 April 2009, 16:11")
- [Kernel Log: 3D support for the new Radeon driver; new Intel drivers](../site/news/item/Kernel-Log-3D-support-for-the-new-Radeon-driver-new-Intel-drivers-741271.html " Kernel Log: 3D support for the new Radeon driver; new Intel drivers – 22 April 2009, 17:06")
- [Kernel Log: What's coming in 2.6.30 - Network: New Wi-Fi drivers and other network novelties](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-Network-New-Wi-Fi-drivers-and-other-network-novelties-741197.html "Kernel Log: What's coming in 2.6.30 - Network: New Wi-Fi drivers and other network novelties – 17 April 2009, 10:51")
- [Kernel Log: Linux 2.6.30 is taking shape](../site/news/item/Kernel-Log-Linux-2-6-30-is-taking-shape-741093.html "Kernel Log: Linux 2.6.30 is taking shape – 09 April 2009, 06:41")

*Older Kernel Logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/).*

([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([trk](mailto:trk@h-online.com "Terry Relph-Knight"))
