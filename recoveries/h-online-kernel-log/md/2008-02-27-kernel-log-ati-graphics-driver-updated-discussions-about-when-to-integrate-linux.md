---
title: "Kernel Log: ati graphics driver updated, discussions about when to integrate Linux drivers"
date: 2008-02-27
author: "Jonathan Bennett"
source: http://www.h-online.com/open/news/item/Kernel-Log-ati-graphics-driver-updated-discussions-about-when-to-integrate-Linux-drivers-734361.html
pages: 1
---

# Kernel Log: ati graphics driver updated, discussions about when to integrate Linux drivers

**Jonathan Bennett**

![Kernel Log](../site/imgs/43/3/6/1/1/3/6/a345f5e7c547062f.jpg) Programmers at X.org who have long developed the "**ati**" driver package have now – after numerous preliminary versions – released version 6.8 of the graphics drivers for both older and more recent AMD/ATI graphics chips. The [new version offers many new features](http://lists.freedesktop.org/archives/xorg-announce/2008-February/000450.html). The most important one of them is probably the support for the three latest generations of Radeon graphics cards (Radeon X1xxx – X3xxx). Until autumn 2007, AMD/ATI's proprietary Fglrx driver had to be used for cards distributed in the last two years, as ATI did not release any information about the chips and no open source drivers could be developed as a result.

With the release of the graphics chip documentation by AMD/ATI last year, the "radeonhd" open source driver, which only supports the three latest generations of Radeon graphics cards, was developed mainly by Novell developers. A short time later, X developer Alex Deucher, who recently took a job with AMD, and Red Hat kernel developer Dave Airlie also integrated support for the latest Radeon generations into the development branch of the "ati" driver package, which has probably resulted in the now released version 6.8. This version is likely to support both older ATI chips like mach64 and r128 and the latest Radeon chips now exclusively distributed under the AMD logo. Which of the two open source drivers will prevail in the long run can't be established at this time.

Meanwhile, kernel developers are [discussing](http://thread.gmane.org/gmane.linux.drivers.openib/50038/focus%3D50190) how far evolved the code of new drivers should be before they **integrate it**. This debate was triggered by a driver incorporated into the main Linux development branch which is still very young and, according to some kernel developers, exhibits a number of obvious problems. This gave rise to the question whether the driver was suitably reviewed before it was integrated into the kernel.

The administrator of the subsystem in question claims to have reviewed the driver and requested several improvements which were subsequently implemented by the driver programmers. While the reviewer saw more room for improvement, he wanted to continue driver development within the normal kernel development branch and, therefore, submitted it to Linus Torvalds, who integrated it into the main development branch leading to 2.6.25.

Whether this happened prematurely and whether there was sufficient reviewing is now the main point of the debate. Some developers, including [Torvalds himself](http://thread.gmane.org/gmane.linux.drivers.openib/50038/focus%3D50192), consider the taken line of action acceptable because it enables other programmers to send in corrections and driver development can continue co-operatively this way. Torvalds also generally advocates integrating new drivers early ("… *I really do believe that we should merge drivers in particular a lot more aggressively*").

In the past, some of the kernel developers demanded quite a high standard from the programmers of new kernel drivers. This sometimes presented too much of a hurdle for developers, and they opted for developing their open source drivers independently of the kernel instead. Numerous examples include the Lirc kernel drivers and various wireless network and webcam drivers like [gspcav](http://mxhaard.free.fr/download.html), to name a few. Users were often the ones who had to bear the consequences: If the distribution kernel's administrators didn't integrate the drivers, users had to install and maintain them individually - a time-consuming and often elaborate task which tends to be avoided by distribution kernel admins for the same reasons.

Should kernel developers decide to further lower integration criteria this could cause quite a few of the external drivers to be integrated into the official Linux kernel sooner or later. In combination with Greg Kroah-Hartman's driver development project, this should give Linux better hardware support and solve a few problems for users and distributors. While driver quality may initially not be ideal, experience has shown that drivers usually evolve much better than their external counterparts even a short time after integration into the kernel, because other Linux developers can contribute their corrections and improvements in the usual ways.

### Kernel Log in brief

- Hdparm 8.1 has been superseded by [version 8.2](http://thread.gmane.org/gmane.linux.ide/28774), which contains several important corrections - the author therefore recommends that users update to the latest version.
- The developers of the realtime kernel branch have released a [new version](http://thread.gmane.org/gmane.linux.rt.user/2452) of the RT tree which now utilises the Ftrace infrastructure for latency tracking scheduled for integration into the official kernel branch.
- The experimental Btrfs file system is now available in [version 0.13](http://thread.gmane.org/gmane.linux.file-systems/21309).

([jbe](mailto: "Jonathan Bennett"))
