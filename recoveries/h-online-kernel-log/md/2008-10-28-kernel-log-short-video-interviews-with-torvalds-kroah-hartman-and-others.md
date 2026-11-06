---
title: "Kernel Log: Short video interviews with Torvalds, Kroah-Hartman and others"
date: 2008-10-28
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-Short-video-interviews-with-Torvalds-Kroah-Hartman-and-others-737833.html
pages: 1
---

# Kernel Log: Short video interviews with Torvalds, Kroah-Hartman and others

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/4/6/0/4/93e8ea3d0acdf147.jpg) The [Linux Foundation](http://www.linuxfoundation.org/) has released [15 short video interviews](http://www.linuxfoundation.org/events/Kernel+Summit+2008/video) with well-known kernel developers. The five to ten minute videos were taken during the [Kernel Summit 2008](https://www.linuxfoundation.org/events/kernel) in mid September and are available in Ogg or Flash format.

Among those interviewed are Linus Torvalds, Greg Kroah-Hartman (the maintainer of the Stable Kernel series and the USB subsystem), David Miller (the maintainer of the network subsystem) and Theodore Ts'o (the maintainer of the Ext\[234\] filesystems). The interview with Linus Torvalds discusses issues like the practical value of the Kernel Summit, quality issues related to the kernel development and the interaction between kernel and kernel related userland applications. It also mentions the development cycle and the ongoing development within the 2.6 series. Linus Torvalds says that nobody voiced any major criticism of the current model and that minor improvements are being suggested instead. He says that this is a good sign which speaks in favour of the current development model.

### New kernel versions

[As expected](../site/news/item/Kernel-log-2-6-28-rc1-released-new-graphics-and-camera-drivers-737795.html "Kernel log: 2.6.28-rc1 released, new graphics and camera drivers – 27 October 2008, 09:10"), the maintainers of the Stable Kernel series have recently released kernel version [2.6.27.4](http://thread.gmane.org/gmane.linux.kernel/749391); it offers several minor improvements and corrects [CVE-2008-3528](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2008-3528), a security hole which allows Denial of Service attacks via the Ext2, Ext3 and Ext4 file systems.

Only a few days after the [release of 2.6.28-rc1](../site/news/item/Kernel-log-2-6-28-rc1-released-new-graphics-and-camera-drivers-737795.html "Kernel log: 2.6.28-rc1 released, new graphics and camera drivers – 27 October 2008, 09:10"), Linus Torvalds has already issued the second release candidate of Linux 2.6.28, [2.6.28-rc2](http://thread.gmane.org/gmane.linux.kernel/749546). Torvalds made this decision because the "[ridiculous count](http://article.gmane.org/gmane.linux.kernel/247735/match%3Dridiculous+count)" 1 of Linux 2.6.28 contained several bugs which gave testers a difficult time. The bugs are explained in detail[in the release email](http://thread.gmane.org/gmane.linux.kernel/749546).

Rafael J. Wysocki has released the [first list of bugs](http://thread.gmane.org/gmane.linux.power-management.general/11956) currently contained in the main development branch, but not in Linux version 2.6.27. As a test, he has also released [a first list](http://thread.gmane.org/gmane.linux.kernel.kernel-testers/1892%26quot%3B) of bugs contained in the main development branch, but not in Linux 2.6.26.

### In brief

- According to a [discussion on the X.org developers mailing list](http://thread.gmane.org/gmane.comp.freedesktop.xorg/32263/) it looks like the CTRL+ALT+Backspace key combination will [no longer terminate](http://cgit.freedesktop.org/xorg/xserver/commit/?id=9d135ac10a7374c7ccda705f1eeb02cc53076c34) the X Server in future (DontZap).

<!-- -->

- Frank Ch. Eigler has [summarised](http://thread.gmane.org/gmane.linux.kernel/748628) several key points of the discussions at the Kernel Summit and the [Linux Plumbers Conference](http://linuxplumbersconf.org/) in an email. The discussions focus on Systemtap and other debugging infrastructures in and around the Linux kernel.

<!-- -->

- Novell developer Luc Verhaegen [reports in his blog](http://libv.livejournal.com/17763.html) that the development version of the radeonhd open source graphics driver now supports audio output via HDMI. He also mentions the Command Submission (CS) support only recently integrated into the driver's main development branch. This feature makes it easier to control the various Radeon chips and optimises the structure of the code.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: 2.6.28-rc1 released, new graphics and camera drivers](../site/news/item/Kernel-log-2-6-28-rc1-released-new-graphics-and-camera-drivers-737795.html "Kernel log: 2.6.28-rc1 released, new graphics and camera drivers – 27 October 2008, 09:10")
- [Kernel Log: What's coming in 2.6.28 - Part 4: Improved graphics support](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-4-Improved-graphics-support-737779.html "Kernel Log: What's coming in 2.6.28 - Part 4: Improved graphics support – 25 October 2008, 08:02")
- [Kernel Log: New Atheros WLAN drivers and stable kernels, radeon vs. radeonhd](../site/news/item/Kernel-Log-New-Atheros-WLAN-drivers-and-stable-kernels-radeon-vs-radeonhd-737773.html "Kernel Log: New Atheros WLAN drivers and stable kernels, radeon vs. radeonhd – 24 October 2008, 10:59")
- [Kernel Log: What's coming in 2.6.28 - Part 3: Dodgy drivers](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-3-Dodgy-drivers-737747.html "Kernel Log: What's coming in 2.6.28 - Part 3: Dodgy drivers – 22 October 2008, 09:29")
- [Kernel Log: More than 10 million lines of Linux source files](../site/news/item/Kernel-Log-More-than-10-million-lines-of-Linux-source-files-737731.html "Kernel Log: More than 10 million lines of Linux source files – 21 October 2008, 14:50")
- [Kernel Log: Coming in 2.6.28 - Part 2: network infrastructure and network drivers](../site/news/item/Kernel-Log-Coming-in-2-6-28-Part-2-network-infrastructure-and-network-drivers-737711.html "Kernel Log: Coming in 2.6.28 - Part 2: network infrastructure and network drivers – 20 October 2008, 09:39")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
