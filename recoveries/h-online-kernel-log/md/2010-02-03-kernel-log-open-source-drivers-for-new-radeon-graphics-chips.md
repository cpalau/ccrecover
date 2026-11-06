---
title: "Kernel Log: Open source drivers for new Radeon graphics chips"
date: 2010-02-03
author: "Chris von Eitzen"
source: http://www.h-online.com/open/news/item/Kernel-Log-Open-source-drivers-for-new-Radeon-graphics-chips-920631.html
pages: 1
---

# Kernel Log: Open source drivers for new Radeon graphics chips

**Chris von Eitzen**

#### ![Kernel Log Logo](../site/imgs/43/4/7/6/1/5/4/KL.jpg-1f663d67fe8a53b0.jpeg) by Thorsten Leemhuis

**The X.org and kernel developers are working on drivers to support the DirectX 11 graphics cards in AMD's Radeon HD 5000 series. While the proprietary AMD drivers have been supported for some time, not even the latest, recently released version co-operates with X Server 1.7, which has already been available for several months. The kernel developers have released numerous new stable kernels and are discussing the integration of utrace in great detail.**

Following an [announcement in his blog](http://www.botchco.com/agd5f/?p=48), AMD employee and long-term open source developer Alex Deucher has [extended](http://cgit.freedesktop.org/xorg/driver/xf86-video-ati/log/) the development branch of the [xf86-video-ati](http://cgit.freedesktop.org/xorg/driver/xf86-video-ati/) driver package to support AMD's Evergreen graphics chips. A kernel driver to support Kernel-based Mode Setting (KMS) is apparently also close to completion; however, 2D and 3D acceleration aren't supported with either driver and aren't likely to be, at least for the near future.

Evergreen GPUs with DirectX 11 support are used on various graphics cards in the Radeon HD 5000 series, which was introduced last September and has gradually been extended to include further models. Until now, these graphics cards could only be used with generic VESA drivers or AMD's proprietary Linux driver known as Catalyst or Fglrx – due to the legal controversies around using non-GPL kernel modules, many distributions completely avoid these drivers or try to bypass the problem, for instance, by retrieving the drivers from the internet.

AMD has recently made version 10.1 of the Catalyst driver available to [download](http://support.amd.com/us/gpudownload/). According to the [release notes![PDF](../site/icons/file-pdf.gif "PDF document")](http://www2.ati.com/drivers/linux/catalyst_101_linux.pdf), the new version now officially supports Ubuntu 9.10 and offers several bug fixes – including one designed to prevent crashes when hot-plugging HDMI monitors. Like previous versions, however, the current version is apparently not suitable for series 1.7 X Servers. Series 1.7 X Servers are part of X.org 7.5, have been available since [early last October](../site/news/item/X-org-Server-1-7-0-released-812407.html "X.org Server 1.7.0 released – 02 October 2009, 10:31") and are included in Fedora 12 as well as other distributions released in the past few months or currently in development.

### Linux version status

Since the [previous Kernel Log](../site/news/item/Kernel-Log-Long-term-maintenance-for-2-6-32-util-linux-ng-extended-910616.html "Kernel Log: Long-term maintenance for 2.6.32, util-linux-ng extended – 22 January 2010, 13:24"), the maintainers of the stable series have released kernel versions [2.6.27.45](http://thread.gmane.org/gmane.linux.kernel/943819), [2.6.32.5](http://thread.gmane.org/gmane.linux.kernel/941689), [2.6.32.6](http://thread.gmane.org/gmane.linux.kernel/942348) and [2.6.32.7](http://thread.gmane.org/gmane.linux.kernel/943818). As usual, the new versions predominantly correct flaws found in previous versions, and updating to the new versions is explicitly recommended, although there is no direct indication of whether the updates close any security holes. Recently released by Willy Tarreau, kernel versions [2.4.37.8](http://thread.gmane.org/gmane.linux.kernel/944532) and [2.4.37.9](http://thread.gmane.org/gmane.linux.kernel/945095) fix such a hole in the e1000 network driver for addressing various Gigabit LAN chips by Intel.

With the release of [2.6.33-rc6](http://thread.gmane.org/gmane.linux.kernel/944249) last Friday, the development of Linux 2.6.33 has progressed at its usual speed. A [long email thread](http://thread.gmane.org/gmane.linux.kernel.utrace/3258/) on the LKML discussed the integration of utrace in Linux-Next in the last weeks of January. Linus Torvalds was among those who argued against integrating the kernel framework used by [Systemtap](http://sourceware.org/systemtap/) for analysing the runtime behaviour of userspace applications. Find a summary of portions of this discussion and some topical background information in this [article on LWN.net](http://lwn.net/Articles/370322/).

### In brief

*Kernel*

- The developer of a proprietary Linux driver recently met a lot of opposition on the LKML when he [asked for](http://thread.gmane.org/gmane.linux.kernel/944030/) the GPL-only symbols of some kernel functions ("EXPORT_SYMBOL_GPL") to be removed so he could use them in his driver. Rik van Riel, for instance, [explained](http://thread.gmane.org/gmane.linux.kernel/944030/focus%3D944036) that the code used by one of the functions involves patented technologies that are only permitted to be used with GPL code. Greg Kroah-Hartman also objected against the proposal, [explaining in this context](http://thread.gmane.org/gmane.linux.kernel/944030/focus%3D944242) that he has already successfully taken companies to court who tried to bypass the "GPL-only" restrictions in the basic driver infrastructure ("driver core") ("*I've already successfully taken legal action against companies who have tried to go around the driver core's GPL-only symbols, so I can not, and will not, make this change.*").
- Simon Kagstrom has [developed a patch](http://thread.gmane.org/gmane.linux.kernel/942633) which causes the kernel to crash in various different ways and allows developers to test the code that is being executed at the time.
- On a personal note: During the [Chemnitz Linux Days](http://chemnitzer.linux-tage.de/2010/), the author of the Kernel Log will [present](http://chemnitzer.linux-tage.de/2010/vortraege/detail.html?idx=392) the current developments in the Linux kernel area – that is, the very same topics discussed in the Kernel Log.

*Kernel environment ("plumbing layer") and userland drivers*

- The Grub developers have [released](http://lists.gnu.org/archive/html/grub-devel/2010-01/msg00316.html) version 1.97.2 of the boot loader.
- The developers of the [Gphoto project](http://gphoto.sourceforge.net/) have made version 2.4.8 of the libgphoto2 library used for accessing many digital cameras available to download. It offers a number of [minor improvements](http://gphoto.sourceforge.net/news/) for cameras and PTP devices by various manufacturers – and, for instance, now supports several new cameras by Canon, Fuji, Kodak and Nikon.
- The developers from the [Flashrom project](http://www.flashrom.org/) released [version 0.9.1 of Flashrom](http://www.flashrom.org/pipermail/flashrom/2010-February/002093.html), which can be used to identify, read, write, verify and erase lots of flash chips which store motherboard BIOS code.

*Graphics*

- In an [extensive blog post](http://virtuousgeek.org/blog/index.php/jbarnes/2010/01/29/progress), PCI subsystem maintainer and driver developer Jesse Barnes has provided an overview of the developments in his area of work. These include recently developed extensions to the KMS code and the DRI2 protocol for synchronising image display when changing pages; the developer also describes his work on the code for accelerating the graphics core of Westmere processors when the relevant CPU cores are working below full capacity ([Turbo Boost/Intelligent Power Sharing/IPS](http://software.intel.com/sites/oss/platform_spotlight.htm)). Westmere processors are used in notebooks.
- In three blog posts, X and kernel developer Dave Airlie describes his work on the code for supporting hybrid graphics on a Lenovo W500 ([1](http://airlied.livejournal.com/70348.html), [2](http://airlied.livejournal.com/70480.html), [3](http://airlied.livejournal.com/70828.html)) The code is designed to allow switching between the Intel chip-set graphics and the Radeon GPU during operation – however, Airlie points out that restarting the X Server when switching will remain inevitable in the foreseeable future.
- Tiago Vignatti provides background information and a progress report concerning the modularisation of X.org [in his blog](http://vignatti.wordpress.com/2010/01/23/xorg-customization-and-true-modularization/).

*Older Kernel Logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/). New editions of Kernel Logs are also mentioned on* [Identi.ca](http://identi.ca/kernellog2) *and* [Twitter](http://twitter.com/kernellog2) *via "@kernellog2". The Kernel Log author also posts updates about various topics on* [Identi.ca](http://identi.ca/kernellogauthor) *and* [Twitter](http://twitter.com/kernellogauthor) *via "@kernellogauthor".* ([thl](mailto:thl@ct.de))

([crve](mailto:crve@h-online.com "Chris von Eitzen "))
