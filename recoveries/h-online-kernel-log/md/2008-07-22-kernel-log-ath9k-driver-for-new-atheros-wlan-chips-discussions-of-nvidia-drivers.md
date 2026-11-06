---
title: "Kernel log: ath9k driver for new Atheros WLAN chips, discussions of Nvidia drivers"
date: 2008-07-22
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-log-ath9k-driver-for-new-Atheros-WLAN-chips-discussions-of-Nvidia-drivers-736563.html
pages: 1
---

# Kernel log: ath9k driver for new Atheros WLAN chips, discussions of Nvidia drivers

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/3/3/3/6/93e8ea3d0acdf147.jpg) The developer Luis R. Rodriguez, who has been working at Atheros for some weeks has [presented](http://thread.gmane.org/gmane.linux.kernel.wireless.general/18019) the new ath9k open source driver, which supports the new Atheros WLAN chips that comply with IEEE draft standard 802.11n. To promote further development in the community, Rodriguez has set up a git tree and a dedicated mailing list; he also explains in a [separate email](http://thread.gmane.org/gmane.linux.kernel.wireless.general/18019) why Atheros has developed a separate driver instead of extending the existing [ath5k](http://madwifi.org/wiki/About/ath5k) driver to support the new Atheros chips.

Before his job with Atheros, Rodriguez worked on WLAN drivers for Linux, so the chances are good that the new driver, or parts of it, will soon find their way into the official kernel. Taking this together with the ongoing improvements to the ath5k driver, the kernel and future distributions should natively support a majority of the Atheros WLAN chips and eventually replace the old [Madwifi](http://madwifi.org/) WLAN driver, which is based on a proprietary kernel.

A [change](http://gitweb.freedesktop.org/?p=xorg/xserver.git;a=commit;h=66fb253082ea42179180303393e48846208987fa) made recently to X Server by the administrator of the *[nv](http://www.x.org/wiki/nv)* Nvidia open source driver, so that, with Nvidia cards, the X Server automatically loads the proprietary Nvidia driver instead of the open source nv driver (if the proprietary driver is installed on the system and no driver is specified in xorg.conf) is currently giving rise to [discussions](http://thread.gmane.org/gmane.comp.freedesktop.xorg/30570/) among X.Org developers. Some X developers don't want a driver to be preferentially used that doesn't belong to X.Org, so the change was [reversed](http://gitweb.freedesktop.org/?p=xorg/xserver.git;a=commitdiff;h=0dbfe0ebc69c307c0626ba824de15d03de1251d4) shortly afterwards with the [consent](http://thread.gmane.org/gmane.comp.freedesktop.xorg/30570/focus%3D30583) of the patch's author, following some [toing](http://thread.gmane.org/gmane.comp.freedesktop.xorg/30570/focus%3D30583) and [froing](http://thread.gmane.org/gmane.comp.freedesktop.xorg/30570/focus%3D30572) on the mailing list.

The Suse developer Stefan Dirsch however [likes the idea](http://thread.gmane.org/gmane.comp.freedesktop.xorg/30570/focus%3D30583) behind the change; he expresses his thanks for the patch and reckons that most distributions will incorporate it in the future. We'll have to see whether he's proved right; well known distributions like Debian and Fedora will probably prefer to go on configuring the open source driver, to support the open source ideal.

Nvidia has meanwhile brought out new versions of the [71.xx.xx](http://www.nvidia.com/object/linux_display_x86_71.86.06.html) and [96.xx.xx](http://www.nvidia.com/object/linux_display_x86_96.43.07.html) series of drivers, which are being kept on for older graphics cards. These can also be used together with the \[ticker:uk_11079 Linux kernel 2.6.26\] that was released a week ago.

But Nvidia is not so quick to support new X Servers, because these two drivers, unlike the current Nvidia drivers, don't work all that well with the current pre-release version of X Server 1.5, which comes with X.Org 7.4. Nvidia is thus demonstrating to owners of GeForce cards below the 5000 series one of the hazards associated with proprietary drivers, for Nvidia drivers can't normally be used with Fedora 9, introduced in May, or the current Alpha of Ubuntu 8.10. Fortunately, the users of these and other distributions based on the pre-release version of X Server 1.5 still have the open source driver as an alternative, though its range of functions is markedly narrower than with the two older versions of Nvidia's proprietary driver.

The \[ticker:uk_11143 previous kernel log\] mentioned lengthy discussions, which have now largely petered out, about handling security fixes in the Linux kernel. That kernel log also gave a link to a thread in which Torvalds once more [lashed out rather viciously](http://thread.gmane.org/gmane.linux.kernel/701694/focus%3D706950) – though his targets this time were not the developers of OpenBSD, as so many times before, but security experts.

These outbursts are not that important, even though they were echoed by some sections of the media that aren't normally very interested in Linux – it isn't that unusual for Torvalds and other kernel developers to express themselves harshly when arguing their case on the Linux Kernel Mailing List (LKML) or elsewhere. Theo de Raadt, the founder of OpenBSD, and Linus Torvalds, the father of Linux, have frequently torn each others' creations apart. Anyone who's been watching them for a few years might well conclude that this has become a game the pair of them secretly enjoy.

**Kernel log in brief**:

- Arjan van de Ven has [presented](http://thread.gmane.org/gmane.linux.kernel/709026) a series of comparatively small patches that speed up the boot-up process a little by means of parallel hardware initialization. He was able to ginger up the starting process even more with the [second version](http://thread.gmane.org/gmane.linux.kernel/709474) of his patches.

<!-- -->

- The X.Org developers have [released version 10.16.3](http://lists.freedesktop.org/archives/xorg-announce/2008-July/000619.html) of the driver for VMWare host systems; it contains some fixes to the XVideo support.

<!-- -->

- [Various open source developers](../site/news/item/Kernel-Log-No-unstable-series-Linux-2008-7-dealing-with-security-fixes-736557.html "Kernel Log: No unstable series; Linux 2008.7; dealing with security fixes – 22 July 2008, 01:47") recently criticized their Ubuntu colleagues for a lack of cooperation on the official kernel, but the Ubuntu developer Ben Collins has now shown some good will by passing on [seven small patches](http://thread.gmane.org/gmane.linux.kernel/709566) to the Linux Kernel Mailing List (LKML).

<!-- -->

- Adrian Bunk has published [Linux version 2.6.16.61](http://thread.gmane.org/gmane.linux.kernel/707809) and [is already working](http://thread.gmane.org/gmane.linux.kernel/709288) on its successor.

<!-- -->

- The gPhoto project has [released version 2.4.2](http://gphoto.sourceforge.net/news/) of the libgphoto2 library, used for reading from many cameras; this provides small improvements for cameras and PTP devices from various makers.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: No unstable series; Linux 2008.7, dealing with security fixes](../site/news/item/Kernel-Log-No-unstable-series-Linux-2008-7-dealing-with-security-fixes-736557.html "Kernel Log: No unstable series; Linux 2008.7; dealing with security fixes – 22 July 2008, 01:47")
- [Polish and add-ons; What's new in Linux 2.6.26](../site/open/features/Polish-and-add-ons-the-latest-updates-in-Linux-2-6-26-746492.html "Polish and add-ons; the latest updates in Linux 2.6.26 – 18 July 2008, 10:22")
- [Kernel Log: Linux-staging branch will help with integration; Linux kernel 2.6.25.6 and 2.6.26-rc6](../site/news/item/Kernel-Log-Linux-staging-branch-will-help-with-integration-Linux-kernel-2-6-25-6-and-2-6-26-rc6-735507.html "Kernel Log: Linux-staging branch will help with integration; Linux kernel 2.6.25.6 and 2.6.26-rc6 – 17 June 2008, 11:31")
- [Kernel log: New graphics drivers and stable kernels; details about Linux-staging](../site/news/item/Kernel-log-New-graphics-drivers-and-stable-kernels-details-about-Linux-staging-736303.html "Kernel log: New graphics drivers and stable kernels; details about Linux-staging – 26 June 2008, 15:45")
- [Kernel-Log: Users of 2.4 provide feedback, 2.4.36.5 and 2.6.26-rc5 released](../site/news/item/Kernel-Log-Users-of-2-4-provide-feedback-2-4-36-5-and-2-6-26-rc5-released-735437.html "Kernel-Log: Users of 2.4 provide feedback, 2.4.36.5 and 2.6.26-rc5 released – 10 June 2008, 15:20")
- [Kernel log: new gfx drivers for GeForce & Radeon GPUs; Kernel Track at LinuxTAG](../site/news/item/Kernel-log-new-gfx-drivers-for-GeForce-Radeon-GPUs-Kernel-Track-at-LinuxTAG-735349.html "Kernel log: new gfx drivers for GeForce & Radeon GPUs; Kernel Track at LinuxTAG – 30 May 2008, 14:23")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).*

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
