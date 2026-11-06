---
title: "Kernel Log: New Stable kernel, DRI2 postponed, Xgl removed from X.org"
date: 2008-08-05
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-New-Stable-kernel-DRI2-postponed-Xgl-removed-from-X-org-736743.html
pages: 1
---

# Kernel Log: New Stable kernel, DRI2 postponed, Xgl removed from X.org

*In Brief*

**Dj Walker-Morgan**

[Greg Kroah-Hartman has, as expected](../site/news/item/Kernel-Log-New-Nvidia-drivers-are-still-slow-Linux-2-6-26-1-soon-736723.html "Kernel Log: New Nvidia drivers are still slow, Linux 2.6.26.1 soon – 04 August 2008, 09:07") released stable Linux versions [2.6.25.14](http://thread.gmane.org/gmane.linux.kernel/715475) and [2.6.26.1](http://thread.gmane.org/gmane.linux.kernel/715477/). Both bring minor corrections and enhancements in various areas of the kernel. The ath5k driver, for example, doesn't use MSI (Message Signal Interrupts) now and the uvcvideo web cam driver works with Medion Akoya mini E1210 netbook camera.

In the release mails for the two new kernels, Greg Kroah-Hartman advises all users to upgrade to one of the two versions. As with the [2.6.25.13 Linux release](../site/news/item/Kernel-log-2-6-25-13-corrects-a-vulnerability-problems-with-ACPI-736703.html "Kernel log: 2.6.25.13 corrects a vulnerability, problems with ACPI – 31 July 2008, 14:42"), security related corrections are not emphasised and the release mail directs the reader to the attached changelog which contains short descriptions of the individual changes.

This follows on from [discussions](../site/news/item/Kernel-Log-No-unstable-series-Linux-2008-7-dealing-with-security-fixes-736557.html "Kernel Log: No unstable series; Linux 2008.7; dealing with security fixes – 22 July 2008, 01:47") about the way security related updates are handled. Users who compile their kernel must either update when the stable kernel recommends updating or search the change log for relevant changes and decide wether to update based on that.

Meanwhile, Kroah-Hartman has moved on to preparing [2.6.25.15](http://thread.gmane.org/gmane.linux.kernel/716481) and [2.6.26.2](http://thread.gmane.org/gmane.linux.kernel/716564). Developers and reviewers have till late Wednesday (12:00 UTC) to make comments on the proposed patches. The next release is usually made within 24 or 48 hours of the comments closing.

------------------------------------------------------------------------

After Intel developers revealed they were working on the management of graphics memory with GEM (Graphics Execution Manager), [aimed at replacing TTM](http://lwn.net/Articles/283793/), Kristian Høgsberg has proposed rethinking DRI2. He is [proposing to](http://lists.freedesktop.org/archives/xorg/2008-August/037795.html) back out DRI2 from the X Server 1.5 release. The development of GEM is progressing with [kernel patches](http://thread.gmane.org/gmane.linux.kernel/715029/focus) being released to the Linux Kernel Mailing List, aiming for inclusion in Linux 2.6.28.

Adam Jackson, X developer removed the code of [Xgl](http://en.opensuse.org/Xgl) from the [source code management of the X.org X server](http://gitweb.freedesktop.org/?p=xorg/xserver.git;a=commit;h=d15b3790307053587df8daed1936ff6923881b63). The future of Xgl is not rosy; the code had not been updated to a current equivalent of other distributions, and newer distributions primarly use Aiglx for the base technology for desktop effects with Compiz and the like.

------------------------------------------------------------------------

ACPI and power saving aspects have been blogged about by kernel developers in the past few weeks. Matthew Garrett has been looking at the [ACPI tables on the Acer Aspire One](http://mjg59.livejournal.com/96270.html) and has found some power saving mechanisms and hardware functions will only operate with Windows Vista. Foxconn released BIOS updated for the [much discussed ACPI issues](../site/news/item/Kernel-log-2-6-25-13-corrects-a-vulnerability-problems-with-ACPI-736703.html "Kernel log: 2.6.25.13 corrects a vulnerability, problems with ACPI – 31 July 2008, 14:42"), with Foxconn [announcing the updates in the Ubuntu Forums](http://ubuntuforums.org/showthread.php?t=877721). There are still issues within the Linux kernel, with newer kernel versions offering a partial remedy.

------------------------------------------------------------------------

On track for inclusion in the main branch are patches for the ath5k driver, which supports the Atheros Wifi chipset found in the first generation of EEE PC. Also on track is the ath9k driver which [could be in soon](http://thread.gmane.org/gmane.linux.kernel.wireless.general/19066/) and signifigantly improve Wifi support in 2.6.27. David Ella has [been looking at the legal problems that are inhibiting development](http://thread.gmane.org/gmane.linux.drivers.acx100/1337) of the [tiacx/acx100 drivers](http://acx100.sourceforge.net/).

## In Brief

- Len Brown has posted [notes from the Linux Power Management "Mini Summit"](http://thread.gmane.org/gmane.linux.acpi.devel/33176)
- There are [discussions on the LKML](http://thread.gmane.org/gmane.linux.kernel/715139/) about the future development of the Reiser4 file system.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: New Nvidia drivers are still slow, Linux 2.6.26.1 soon](../site/news/item/Kernel-Log-New-Nvidia-drivers-are-still-slow-Linux-2-6-26-1-soon-736723.html "Kernel Log: New Nvidia drivers are still slow, Linux 2.6.26.1 soon – 04 August 2008, 09:07")
- [Kernel Log : Tux3 file system announced, X.org updates](../site/news/item/Kernel-Log-Tux3-file-system-announced-X-org-updates-736707.html "Kernel Log : Tux3 file system announced, X.org updates – 01 August 2008, 09:17")
- [Kernel Log: 2.6.25.13 corrects a vulnerability, problems with ACPI](../site/news/item/Kernel-log-2-6-25-13-corrects-a-vulnerability-problems-with-ACPI-736703.html "Kernel log: 2.6.25.13 corrects a vulnerability, problems with ACPI – 31 July 2008, 14:42")
- [Kernel Log: First release candidate concludes the hot development phase of 2.6.27](../site/news/item/Kernel-Log-First-release-candidate-concludes-the-hot-development-phase-of-2-6-27-736695.html "Kernel Log: First release candidate concludes the hot development phase of 2.6.27 – 31 July 2008, 12:23")
- Kernel Log: Practical Practices - Ottawa Linux Symposium Notes
- [Kernel Log: Centrino 2 WLAN driver iwl 5000 and webcam driver gscpa in Linux 2.6.27](../site/news/item/Kernel-Log-Centrino-2-WiFi-driver-iwl-5000-and-webcam-driver-gscpa-in-Linux-2-6-27-736569.html "Kernel Log: Centrino 2 WiFi driver iwl 5000 and webcam driver gscpa in Linux 2.6.27 – 23 July 2008, 16:46")
- [Kernel Log: ath9k driver for new Atheros WLAN chips, discussions of Nvidia drivers](../site/news/item/Kernel-log-ath9k-driver-for-new-Atheros-WLAN-chips-discussions-of-Nvidia-drivers-736563.html "Kernel log: ath9k driver for new Atheros WLAN chips, discussions of Nvidia drivers – 22 July 2008, 15:48")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
