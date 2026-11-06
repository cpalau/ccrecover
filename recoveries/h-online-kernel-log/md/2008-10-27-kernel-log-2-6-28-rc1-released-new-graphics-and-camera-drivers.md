---
title: "Kernel log: 2.6.28-rc1 released, new graphics and camera drivers"
date: 2008-10-27
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-log-2-6-28-rc1-released-new-graphics-and-camera-drivers-737795.html
pages: 1
---

# Kernel log: 2.6.28-rc1 released, new graphics and camera drivers

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/4/5/6/6/93e8ea3d0acdf147.jpg) The maintainers of the stable kernel have released versions [2.6.25.19](http://thread.gmane.org/gmane.linux.kernel/748042), [2.6.26.7](http://thread.gmane.org/gmane.linux.kernel/748041) and [2.6.27.3](http://thread.gmane.org/gmane.linux.kernel/748038), [as expected](../site/news/item/Kernel-Log-New-Atheros-WLAN-drivers-and-stable-kernels-radeon-vs-radeonhd-737773.html "Kernel Log: New Atheros WLAN drivers and stable kernels, radeon vs. radeonhd – 24 October 2008, 10:59"). Apart from bug fixes and minor improvements, all of the versions also offer a patch for [CVE-2008-3831](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2008-3831), the security hole in the DRI code for recent Intel graphics chipsets. In their release emails, the maintainers of the stable series once again use very general terms to invite users to update without explicitly pointing out the security related fix.

Greg Kroah-Hartman also advises all users of self-compiled kernels to switch to the latest kernel in the 2.6.27 series, as it is likely that only one more stable version each will be released for series 2.6.25 and 2.6.26 before the stable team stops maintaining these kernel series. Linux version 2.6.27.4 is already [in preparation](http://thread.gmane.org/gmane.linux.kernel/748680) and likely to be released on Sunday. The deadline for submitting comments is early on Sunday morning.

### Merge window closed

Linus Torvalds closed the merge window of the next Linux version in the main development line exactly two weeks after the release of Linux 2.6.27, with the [release of 2.6.28-rc1](http://thread.gmane.org/gmane.linux.kernel/748671), . Four kernel logs have already discussed some of the changes in detail (\[ticker:uk_11743 1\], [2](../site/news/item/Kernel-Log-Coming-in-2-6-28-Part-2-network-infrastructure-and-network-drivers-737711.html "Kernel Log: Coming in 2.6.28 - Part 2: network infrastructure and network drivers – 20 October 2008, 09:39") [3](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-3-Dodgy-drivers-737747.html "Kernel Log: What's coming in 2.6.28 - Part 3: Dodgy drivers – 22 October 2008, 09:29"), [4](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-4-Improved-graphics-support-737779.html "Kernel Log: What's coming in 2.6.28 - Part 4: Improved graphics support – 25 October 2008, 08:02")). In the coming weeks, further kernel logs will look into other kernel areas – the driver subsystems is the usual suspect for the occasional late inclusion of changes even after the end of the hot development phase of 2.6.28.

According to the [release email](http://thread.gmane.org/gmane.linux.kernel/748671), most of the changes affected the drivers. [As already reported](../site/news/item/Kernel-Log-More-than-10-million-lines-of-Linux-source-files-737731.html "Kernel Log: More than 10 million lines of Linux source files – 21 October 2008, 14:50"), the kernel sources now consist of more than 10 million lines of text:

Linus Torvalds [chose](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=57f8f7b60db6f1ed2c6918ab9230c4623a9dbe37) the name "Killer Bat of Doom" for the new version.

### New Intel graphics drivers

The recently released [version 2.5.0](http://lists.freedesktop.org/archives/xorg/2008-October/039555.html) of the "intel" X.org graphics driver greatly improves the support of the [EXA](http://en.wikipedia.org/wiki/EXA) X acceleration architecture; the code for the old XFree86 Acceleration Architecture ([XAA](http://en.wikipedia.org/wiki/XFree86_Acceleration_Architecture)) was removed at the same time.

The driver is now designed to produce clearer images with Textured Video and XvMC, and avoid [video tearing](http://en.wikipedia.org/wiki/Video_tearing) when rendering videos. As already mentioned briefly in the [previous kernel log](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-4-Improved-graphics-support-737779.html "Kernel Log: What's coming in 2.6.28 - Part 4: Improved graphics support – 25 October 2008, 08:02"), the driver can now optionally use Intel's Graphics Execution Manager (GEM), which is scheduled for integration in Linux version 2.6.28. Even [Kernel Mode Setting](http://thread.gmane.org/gmane.linux.kernel/531149) (KMS), a technology that has yet to be integrated into the main development branch of Linux, is reportedly supported by the driver – as long as the kernel used is also capable of it.

### In Brief

- The newly [created wiki](http://wireless.kernel.org/en/users/Drivers/otus) about the [recently released otus WLAN driver](../site/news/item/Kernel-Log-New-Atheros-WLAN-drivers-and-stable-kernels-radeon-vs-radeonhd-737773.html "Kernel Log: New Atheros WLAN drivers and stable kernels, radeon vs. radeonhd – 24 October 2008, 10:59") contains the model numbers of three USB Wi-Fi adapters which use one of the Atheros USB Wi-Fi chips supported by the otus driver.
- The [Gphoto project](http://gphoto.sourceforge.net) has released [version 2.4.3](http://gphoto.sourceforge.net/news/) of the libgphoto2 library [to download](http://sourceforge.net/project/showfiles.php?group_id=8874) which is used to access many cameras; the new version offers several improvements and is the first to support cameras and PTP devices by various manufacturers.
- The developers of [Gutenprint](http://gutenprint.sourceforge.net/) have [released](http://sourceforge.net/project/shownotes.php?group_id=1537&release_id=635000) version 5.2.1 of Gutenprint, as [already reported](../site/news/item/Gutenprint-5-2-1-drivers-for-Linux-and-Mac-OS-X-improve-printer-support-737789.html "Gutenprint 5.2.1 drivers for Linux and Mac OS X improve printer support – 24 October 2008, 16:25"). The new version support a much larger number of printers than version 5.0.2, which was the previous stable release.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: What's coming in 2.6.28 - Part 4: Improved graphics support](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-4-Improved-graphics-support-737779.html "Kernel Log: What's coming in 2.6.28 - Part 4: Improved graphics support – 25 October 2008, 08:02")
- [Kernel Log: New Atheros WLAN drivers and stable kernels, radeon vs. radeonhd](../site/news/item/Kernel-Log-New-Atheros-WLAN-drivers-and-stable-kernels-radeon-vs-radeonhd-737773.html "Kernel Log: New Atheros WLAN drivers and stable kernels, radeon vs. radeonhd – 24 October 2008, 10:59")
- [Kernel Log: What's coming in 2.6.28 - Part 3: Dodgy drivers](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-3-Dodgy-drivers-737747.html "Kernel Log: What's coming in 2.6.28 - Part 3: Dodgy drivers – 22 October 2008, 09:29")
- [Kernel Log: More than 10 million lines of Linux source files](../site/news/item/Kernel-Log-More-than-10-million-lines-of-Linux-source-files-737731.html "Kernel Log: More than 10 million lines of Linux source files – 21 October 2008, 14:50")
- [Kernel Log: Coming in 2.6.28 - Part 2: network infrastructure and network drivers](../site/news/item/Kernel-Log-Coming-in-2-6-28-Part-2-network-infrastructure-and-network-drivers-737711.html "Kernel Log: Coming in 2.6.28 - Part 2: network infrastructure and network drivers – 20 October 2008, 09:39")
- [Kernel Log: Coming in 2.6.28 - Part 1: ATA support and block layer](../site/news/item/Kernel-Log-Coming-in-2-6-28-Part-1-ATA-support-and-block-layer-737699.html "Kernel Log: Coming in 2.6.28 - Part 1: ATA support and block layer – 19 October 2008, 08:02")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
