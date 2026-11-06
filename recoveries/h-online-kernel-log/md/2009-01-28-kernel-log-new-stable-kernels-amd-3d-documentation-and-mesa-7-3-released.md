---
title: "Kernel Log: New stable kernels, AMD 3D documentation and Mesa 7.3 released"
date: 2009-01-28
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-New-stable-kernels-AMD-3D-documentation-and-Mesa-7-3-released-739845.html
pages: 1
---

# Kernel Log: New stable kernels, AMD 3D documentation and Mesa 7.3 released

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/6/2/7/7/93e8ea3d0acdf147.jpg) Over the last two weeks, the kernel developers have released versions [2.6.27.11](http://thread.gmane.org/gmane.linux.kernel/780764), [2.6.27.12](http://thread.gmane.org/gmane.linux.kernel/782775) and [2.6.28.1](http://lkml.indiana.edu/hypermail/linux/kernel/0901.2/00904.html) of the stable kernel and at the weekend they added versions [2.6.27.13](http://thread.gmane.org/gmane.linux.kernel/785311) and [2.6.28.2](http://thread.gmane.org/gmane.linux.kernel/785313). All of these versions incorporate corrections and minor improvements, including a whole set of patches, contributed by IBM's Heiko Carstens, to eliminate a security vulnerability listed as [CVE-2009-0029](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-0029) that is said to affect only S390, PowerPC, SPARC64 and MIPS architectures. A little earlier, Torvalds accepted similar changes ([1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1a94bc34768e463a93cb3751819709ab0ea80a01), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4c696ba7982501d43dea11dbbaabd2aa8a19cc42) and [3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2ed7c03ec17779afb4fcfa3b8c61df61bd4879ba)) into the main development tree.

There were virtually no changes last week, because Torvalds was attending [LCA 2009](http://linux.conf.au/), where he spent some time with his "[Tasmanian Devil](http://torvalds-family.blogspot.com/2009/01/now-thats-cute.html)" and tried his hand at [hairdressing](http://lwn.net/Articles/316282/). Last night, following the week off, he resumed accepting changes for Linux 2.6.29, so 2.6.29-rc3 will probably appear next week.

**No Linux 2.8/3.0**

[Interviewed](http://www.thestandard.com/news/2009/01/22/open-source-identity-linux-founder-linus-torvalds) at the LCA, he again made it clear that he had no plans to go back to a development model with an unstable series (Linux 2.3.x, 2.5.x), but was happy with the current model and planned to continue further development of the 2.6 series. He also mentioned ZFS and Btrfs, source-code management systems, Windows 7, and his preferred Linux distribution, saying he had switched from KDE to GNOME because KDE 4.0 was "a disaster", even though just a few years ago he was still [harshly criticising](http://linux.slashdot.org/article.pl?sid=05/12/13/1340215) the GNOME team.

Meanwhile, two short discussions have erupted on the Linux Kernel Mailing List (LKML) about the usefulness of the staging branch incorporated into the main development tree by 2.6.28 ([integrated staging branch](http://www.heise-online.co.uk/open/features/112299/4)). The first question was whether file systems should be allowed into the staging area, as Greg Kroah-Hartman [currently](http://thread.gmane.org/gmane.linux.kernel/780244/focus%3D780290) plans with [DST](http://www.ioremap.net/projects/dst) (distributed (network) storage). After some tos and fros involving Andrew Morton and other kernel hackers, silence fell for almost a week, then [Dave Jones](http://thread.gmane.org/gmane.linux.file-systems/28733/focus%3D29439) brought the point up again in a thread that was by now growing rather cold. The concept of the staging area and the idea behind it were then criticised in general terms. Andrew Morton himself doesn't seem entirely sure that accepting it into the main development tree [was a good idea](http://thread.gmane.org/gmane.linux.file-systems/28733/focus%3D29458).

Some other recent discussions on the LKML revolved around SLQB ([1](http://thread.gmane.org/gmane.linux.kernel/780475/), [2](http://thread.gmane.org/gmane.linux.kernel.mm/30358/), [3](http://thread.gmane.org/gmane.linux.kernel/780166/focus%3D47936)) – a new memory management infrastructure that Nick Piggin thinks should replace the current memory managers SLAB and SLUB. When integrated into [Linux 2.6.22](http://kernelnewbies.org/Linux_2_6_22), SLUB was really intended to be SLAB's successor, but it then turned out to have lower scores on some benchmarks.

SLQB and SLUB developers are debating the detailed differences between their two new memory managers on the LKML. These are described in simple terms in an [LWN.net article on SLQB](http://lwn.net/Articles/311502/). SLQB has [recently](http://thread.gmane.org/gmane.linux.kernel.mm/30358/focus%3D785542) been added to linux-next, so the chances are that Linux 2.6.30 will include it. Presumably, in the long run, two of the three memory managers will be eliminated.

**Mesa 7.3**

The [Mesa project](http://mesa3d.sourceforge.net/) has [issued](http://thread.gmane.org/gmane.comp.video.mesa3d.announce/70) version 7.3 of its free OpenGL implementation for Linux and other Unix-like systems. This version, which is aimed at developers, will lead on to Mesa 7.4, which will then take over from version 7.2, currently the latest version for users. Apart from bug fixes, the [innovations in 7.3](http://mesa3d.sourceforge.net/relnotes-7.3.html) include support for GEM and DRI in Mesa code for Intel graphics hardware. Mesa now also implements OpenGL Shading Language ([GLSL](http://en.wikipedia.org/wiki/GLSL)) 1.2.

The intention is now to prepare versions 7.5/7.6 in the main Mesa development tree. [Gallium3D](http://www.tungstengraphics.com/wiki/index.php/Gallium3D), the new architecture developed by Tungsten Graphics to ease the programming of support for 3D, will also be accepted. Work is [currently in progress](http://tirdc.livejournal.com/23805.html) to get the Radeon graphics driver to support Gallium3D. The recently published "[Nouveau Companion 42](http://nouveau.freedesktop.org/wiki/Nouveau%20Companion%2042)" reports that the developers of the experimental Nouveau open source 3D drivers for nVidia cards, are already working on Gallium3D.

**All about X.org**

Although the development of X server 1.6 seemed largely to have [come to a halt](http://www.phoronix.com/scan.php?page=news_item&px=Njk3MA) at the end of the year, it sprang back into life in mid-month when the [first release candidate (RC)](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/522) was announced. Momentum was lost again last week when some key X.org developers went off to attend [LCA 2009](http://linux.conf.au/).

The X.org programmers have completed the development of version 2.6.0 of the [xf86-video-intel](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/526) graphics driver package, usually known as "intel" for short, and shortly thereafter they followed this up with [version 2.6.1](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/528). The [drivers page](http://intellinuxgraphics.org/2008Q4.html) lists some main innovations: support for HDMI audio, the DRI2 (Direct Rendering Infrastructure) for X Server 1.6 and the Graphics Execution Manager (GEM) accompanying Linux 2.6.28 ([Linux 2.6.28's five best features - Computerworld Blogs](http://blogs.computerworld.com/linux_2_6_28s_five_best_features)).

Rudimentary code for exploiting the 3D units of new AMD chips was published a few weeks ago, and AMD's Alex Deucher has now [announced](http://lists.freedesktop.org/archives/xorg/2009-January/042975.html) the release [of a document](http://www.x.org/docs/AMD/R6xx_3D_Registers.pdf)![PDF](../site/icons/file-pdf.gif "PDF document") giving a more detailed description of the 3D register of the R6xx and R7xx GPUs. That should make it easier to extend the 3D infrastructure, including the Radeon and Radeon HD graphics drivers, to include 3D support for Radeon cards in the 1000, 2000, 3000 and 4000 series.

**In Brief**

- The developers of the ALSA project released version 1.0.19 of the main ALSA components at the beginning of last week. The change log lists all the changes made since [version 1.0.18](http://alsa-project.org/main/index.php/Changes_v1.0.18_v1.0.19). Many of the changes to the ALSA drivers are already in the main kernel development tree, so will be components of Linux 2.6.29.

<!-- -->

- Luis R. Rodriguez (mcgrof) [released](http://article.gmane.org/gmane.linux.kernel.wireless.general/27655) version 1.0 of the Central Regulatory Domain Agent ([CRDA](http://wireless.kernel.org/en/developers/Regulatory/CRDA)) and [version 1.0.1](http://thread.gmane.org/gmane.linux.kernel.wireless.general/27714) shortly afterwards. CRDA is the userspace counterpart of the new Wireless Regulatory Infrastructure in Linux 2.6.28 ([Regulatory - Linux Wireless](http://linuxwireless.org/en/developers/Regulatory)).

<!-- -->

- The Linux WLAN developers are considering whether to accept the recently presented open source firmware for the 4306, 4311, 4318 and 4320 broadcast WLAN chips [into the kernel](http://thread.gmane.org/gmane.linux.kernel.wireless.general/27579/). That would save users having to snip the firmware out of the archive containing the Windows drivers, using such tools as b43-fwcutter.

<!-- -->

- VIA, which for some months has been fulfilling its commitment to open source development by supporting the development of [openChrome](http://www.via.com.tw/en/resources/pressroom/pressrelease.jsp?press_release_no=2887), has further underpinned that commitment by [releasing additional](http://laforge.gnumonks.org/weblog/2009/01/13#20090113-vtbridge) [documentation for VIA hardware](ftp://ftp.vtbridge.org/Docs/).

<!-- -->

- [In his blog](http://www.codemonkey.org.uk/2009/01/18/forthcoming-p4clockmod/), Dave Jones explains some changes to the p4-clockmod driver that have been accepted for 2.6.29. He again explains why the throttling of modern CPUs increases the power consumption of most systems over time, rather than reducing it, as is often assumed.

<!-- -->

- Chris Ball presents a video in [his blog](http://blog.printf.net/articles/2009/01/26/multi-pointer-remote-desktop), showing an area of application for Multi-pointer X ([MPX](http://wearables.unisa.edu.au/mpx/)). MPX, which is to be a component of X.org 7.5, allows several mouse cursors and keyboards to be used with one X Server. The GTK+ developers are also [working on support for MPX](http://live.gnome.org/GTK%2B/MPX), and some of their work is shown in [videos in Carlos Garnacho's blog](http://blogs.gnome.org/carlosg/2009/01/19/more-multitouchy-fun/).

<!-- -->

- The [Gphoto project](http://gphoto.sourceforge.net) has released [version 2.4.4](http://gphoto.sourceforge.net/news/) of the libgphoto2 library, which can be used to access a great many cameras, [for download](http://sourceforge.net/project/showfiles.php?group_id=8874&package_id=8957). It includes [a number of minor improvements](http://gphoto.sourceforge.net/news/) for a variety of cameras and PTP devices.

<!-- -->

- Linux block layer maintainer Jens Axboe gives an overview of ongoing work to improve the Linux kernel's asynchronous I/O support [in his blog](http://axboe.livejournal.com/1718.html).

<!-- -->

- The Ndiswrapper team has [issued](http://sourceforge.net/project/showfiles.php?group_id=93482&release_id=655469) Ndiswrapper [version 1.54](http://sourceforge.net/project/shownotes.php?release_id=655469).

<!-- -->

- The developers of Linux WLAN drivers and the infrastructure surrounding them have opened up an [IRC channel](http://thread.gmane.org/gmane.linux.kernel.wireless.general/27110).

<!-- -->

- An analysis by Greg Kroah-Hartman at [I write too much email](http://www.kroah.com/log/linux/email_summary_2008.html) shows the impressive amount of emails written by some kernel developers.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: What's new in 2.6.29 - Part 3: Kernel controlled graphics modes](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-3-Kernel-controlled-graphics-modes-739697.html "Kernel Log: What's new in 2.6.29 - Part 3: Kernel controlled graphics modes – 17 January 2009, 07:36")
- [Kernel Log: main development phase for 2.6.29 ends, new X.org drivers](../site/news/item/Kernel-Log-main-development-phase-for-2-6-29-ends-new-X-org-drivers-739633.html "Kernel Log: main development phase for 2.6.29 ends, new X.org drivers – 12 January 2009, 17:09")
- [Kernel Log: What's new in 2.6.29 - Part 2: WiMax](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-2-WiMAX-739621.html "Kernel Log: What's new in 2.6.29 - Part 2: WiMAX – 12 January 2009, 10:19")
- [Kernel Log: What's new in 2.6.29 - Part 1: Dodgy Wifi drivers and AP support](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-1-Dodgy-Wifi-drivers-and-AP-support-739619.html "Kernel Log: What's new in 2.6.29 - Part 1: Dodgy Wifi drivers and AP support – 11 January 2009, 16:08")
- [Kernel Log: 2.6.29 development kicks off, improved 3D support](../site/news/item/Kernel-Log-2-6-29-development-kicks-off-improved-3D-support-739551.html "Kernel Log: 2.6.29 development kicks off, improved 3D support – 05 January 2009, 17:29")
- [Kernel Log: Higher and Further, The innovations of Linux 2.6.28](../site/open/features/Kernel-Log-Higher-and-Further-The-innovations-of-Linux-2-6-28-746519.html "Kernel Log: Higher and Further, The innovations of Linux 2.6.28 – 23 December 2008, 15:55")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
