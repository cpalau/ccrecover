---
title: "Kernel Log: Stable series development is speeding up, X Server 1.6 available soon"
date: 2009-02-23
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-Stable-series-development-is-speeding-up-X-Server-1-6-available-soon-740203.html
pages: 1
---

# Kernel Log: Stable series development is speeding up, X Server 1.6 available soon

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/6/6/3/5/93e8ea3d0acdf147.jpg) The development speed of the Linux stable series and the number of integrated changes, has been rising in the past few weeks. In February alone, the maintainers of the stable kernel series have released four new 2.6.28.*x* versions and five new 2.6.27.*x* kernels, to correct numerous flaws in the respective predecessors and add many minor improvements.

As usual, the release emails by the maintainers of the stable kernel series strongly advise that all users of kernel.org kernels upgrade to the latest versions, without explicitly pointing out any security issues the new versions may resolve. This is, for example, the case with the current versions [2.6.27.18](http://www.kernel.org/pub/linux/kernel/v2.6/ChangeLog-2.6.27.18) and [2.6.28.6](http://www.kernel.org/pub/linux/kernel/v2.6/ChangeLog-2.6.28.6), which plug a CVE numbered security hole in SPARC systems.

Meanwhile, [2.6.27.19](http://thread.gmane.org/gmane.linux.kernel/796642) and [2.6.28.7](http://thread.gmane.org/gmane.linux.kernel/796551) are already in progress. The window for submitting comments about the proposed changes closed on Friday night, and the two new versions should be released shortly. They are currently expected to contain a whole range of fixes to the Ext4 file system. The kernel developers completed the main development phase of Ext4 with 2.6.28.

The development progress of Linux 2.6.29 is currently uneventful; having released [2.6.29-rc5](http://thread.gmane.org/gmane.linux.kernel/794385) a week ago, Linus Torvalds will probably finalise the sixth release candidate soon. At the end of last week [the list of new flaws](http://thread.gmane.org/gmane.linux.power-management.general/13059) ("regressions") in the main development branch contained about 25Â known problems .

**Sleep**

In his release email for 2.6.29-rc3, Linus Torvalds pointed out major changes to the infrastructure required for changing into and out of the suspend modes, a topic already [covered in detail](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-4-ACPI-PCI-PM-notebooks-and-power-saving-improvements-739889.html "Kernel Log: What's new in 2.6.29 - Part 4: ACPI, PCI, PM – notebooks and power saving improvements â 31 January 2009, 15:01") by the Kernel Log's "What's new in 2.6.29" mini series. In a [lengthy discussion](http://thread.gmane.org/gmane.linux.network/118375/focus%3D118717) that began shortly afterwards, Torvalds seriously questioned the new functionality in several areas â€“ especially in terms of the PCI bridges. Some of the weaknesses he criticised have, in the meantime, been fixed by the kernel hackers.

In a [long thread](http://thread.gmane.org/gmane.linux.power-management.general/13064), the developers extensively discussed how to better incorporate the component-specific and system level power saving techniques and suspend modes offered by modern hardware. They touched on many different areas, discussing such as whether to automatically put the whole system to sleep when it is idle, in the same way as, for example, Android mobiles do. However, the S3 mode (Suspend to RAM) is still thought to be too unreliable in X86 desktop hardware; in addition, the developers said the time needed for waking up from S3 mode is often too long to use the system sleep state for very short idle times.

**X.org topics**

The [X.org project's](http://x.org) development of X ServerÂ 1.6 is in its final stages, although this has been the case for the past two weeks. It had looked like the new version of the X Server (originally [scheduled](http://lists.freedesktop.org/archives/xorg/2008-November/040290.html) for release at the beginning of the year) would be released on the 2nd of February, when [X Server 1.5.99.902](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/530) was released as RC2. This didn't work out; instead, Intel developer Keith Packard released an RC3 last [Wednesday](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/547) and plans to release this candidate as X ServerÂ 1.6, unless major problems are found ("*Here's what I'm hoping will be the server 1.6 release. Unless someone finds a brown-paper-bag bug in the next few days, I'll tag this as 1.6 and push it out soon.*").

The X.org developers have released numerous new drivers, for example [version 6.11.0](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/549) of the xf86-video-ati driver package, which includes the "radeon" graphics driver and fixes many of the flaws of the, only recently released, version 6.10. For 6.12, the developers plan to improve the support of [several acceleration features](http://www.botchco.com/agd5f/?p=37) of R6xx and R7xx GPUs. New versions of the [vesa](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/545) and [geode](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/540) graphics drivers were also released.

After several pre-release versions, Peter Hutterer [released](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/532) version 1.0.0 of the xf86-input-synaptics driver at the beginning of the month. It is suitable for the Alps and Synaptics touch pads found in many notebooks and also supports [Input Device Properties](http://who-t.blogspot.com/2008/10/device-properties-have-landed.html), a relatively young feature which allows users to configure the touch pad at run time. This has so far only been possible using tools like synclient, which is supplied with the driver, and with shared memory activated via the "SHMConfig" option in xorg.conf â€“ for security reasons, this is not enabled in the standard configurations of several distributions.

Earlier this month, developer Adam Williamson, who recently left Mandriva and [started work with Red Hat](http://www.happyassassin.net/2009/01/23/job-announcement/), took a closer look at the Linux support for the graphics core of Intel's US15W chipset. This chipset is suitable for Atom CPUs and is used in, for example, the Dell MiniÂ 12. Despite investing a day's work and intensive research he didn't manage to get the various drivers found in distributions like Moblin and Ubuntu to work in a current version of Fedora; details of his experiences are [documented in his blog](http://www.happyassassin.net/2009/01/30/intel-gma-500-poulsbo-graphics-on-linux-a-precise-and-comprehensive-summary-as-to-why-youre-screwed/). This indicates that the Linux support of the PowerVR graphics core, acquired by Intel, seems to be in considerably worse shape than that of other Intel graphics chips where the drivers are developed in house by the vendor. Linux users who don't want to use the Ubuntu offered by Dell should, therefore, avoid hardware that includes the Poulsbo graphics chips for now.

**In brief**

- Ogawa Hirofumi, the maintainer of the Linux kernel's FAT filesystem support, has released some [rudimentary code](http://thread.gmane.org/gmane.linux.kernel/786498/focus%3D787508) for the support of the [exFAT](http://en.wikipedia.org/wiki/ExFAT) file system, which is also called FAT64; however, he says that he currently has [no plans to actively continue its development](http://thread.gmane.org/gmane.linux.kernel/786498/focus%3D787127).

<!-- -->

- The developers of [Systemtap](http://sources.redhat.com/systemtap) have released [version 0.9](http://thread.gmane.org/gmane.linux.systemtap/10945/focus%3D11081) of the testing and debugging framework.

<!-- -->

- According to the [latest report](http://thread.gmane.org/gmane.linux.kernel/796770) by Daniel Phillips, the experimental version of the Tux3 file system, for which he is the main driving force, can be used as a root file system. The developers of Btrfs, which has been chosen as the [next generation Linux file system](../site/news/item/Kernel-Log-Ext4-completes-development-phase-as-interim-step-to-btrfs-737697.html "Kernel Log: Ext4 completes development phase as interim step to btrfs â 17 October 2008, 09:52"), have added numerous fixes and improvements â€“ including some SSD (Solid State Drives) optimisations. Brfs was included in the main development branch of Linux with the development start of 2.6.29 ([1](http://thread.gmane.org/gmane.linux.kernel/791186), [2](http://thread.gmane.org/gmane.linux.kernel/794355)).

<!-- -->

- Almost concurrently with the [recent release](../site/news/item/New-stable-real-time-kernel-2-6-26-rt-740097.html "New stable real-time kernel 2.6.26-rt â 12 February 2009, 15:38") of the 2.6.26-rt real time kernel branch for production use, kernel hackers Thomas Gleixner and Ingo Molnar have released the experimental [2.6.29-rc4-rt1](http://thread.gmane.org/gmane.linux.rt.user/3911) kernel. Having taken a sabbatical from preempt-rt for quite a while, the two developers now intend to use this kernel branch to renew their efforts and prepare the real time extensions of the RT tree for inclusion into the main development branch of Linux.

<!-- -->

- Jeremy Fitzhardinge has [released several patches](http://article.gmane.org/gmane.linux.kernel/795546/) to implement the core part of Xen dom0 support in the kernel; [he currently plans](http://lists.xensource.com/archives/html/xen-devel/2009-02/msg00333.html) to submit dom0 support for inclusion into Linux 2.6.30.

<!-- -->

- In [a blog entry](http://airlied.livejournal.com/65755.html) and [a post on a mailing list](http://thread.gmane.org/gmane.comp.video.dri.devel/33835), Dave Airlie describes the extensive changes to the Radeon graphics driver he is currently working on.

<!-- -->

- Neil Brown has prepared [numerous patches](http://thread.gmane.org/gmane.linux.raid/21608/) for Linux 2.6.30 that will allow converting a RAIDÂ 1 managed via the Linux software RAID code, into a RAIDÂ 5; in addition, the code can reportedly be used for allowing the kernel to convert a RAIDÂ 5 into a RAIDÂ 6.

<!-- -->

- The X.org developers have [set up](http://thread.gmane.org/gmane.comp.freedesktop.xorg/36900) the [xorg-devel](http://lists.x.org/mailman/listinfo/xorg-devel) mailing list for development discussions; they also intend to [retain](http://thread.gmane.org/gmane.comp.freedesktop.xorg/36900) the [xorg](http://lists.x.org/mailman/listinfo/xorg) mailing list they have used so far.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at The H Open Source:*

- [Kernel Log: What's new in 2.6.29 - Part 4: ACPI, PCI, PM â€“ notebooks and power saving improvements](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-4-ACPI-PCI-PM-notebooks-and-power-saving-improvements-739889.html "Kernel Log: What's new in 2.6.29 - Part 4: ACPI, PCI, PM – notebooks and power saving improvements â 31 January 2009, 15:01")
- [Kernel Log: New stable kernels, AMD 3D documentation and Mesa 7.3 released](../site/news/item/Kernel-Log-New-stable-kernels-AMD-3D-documentation-and-Mesa-7-3-released-739845.html "Kernel Log: New stable kernels, AMD 3D documentation and Mesa 7.3 released â 28 January 2009, 11:41")
- [Kernel Log: What's new in 2.6.29 - Part 3: Kernel controlled graphics modes](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-3-Kernel-controlled-graphics-modes-739697.html "Kernel Log: What's new in 2.6.29 - Part 3: Kernel controlled graphics modes â 17 January 2009, 07:36")
- [Kernel Log: main development phase for 2.6.29 ends, new X.org drivers](../site/news/item/Kernel-Log-main-development-phase-for-2-6-29-ends-new-X-org-drivers-739633.html "Kernel Log: main development phase for 2.6.29 ends, new X.org drivers â 12 January 2009, 17:09")
- [Kernel Log: What's new in 2.6.29 - Part 2: WiMax](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-2-WiMAX-739621.html "Kernel Log: What's new in 2.6.29 - Part 2: WiMAX â 12 January 2009, 10:19")
- [Kernel Log: What's new in 2.6.29 - Part 1: Dodgy Wifi drivers and AP support](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-1-Dodgy-Wifi-drivers-and-AP-support-739619.html "Kernel Log: What's new in 2.6.29 - Part 1: Dodgy Wifi drivers and AP support â 11 January 2009, 16:08")

*Older Kernel logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/).*

([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
