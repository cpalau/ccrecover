---
title: "Kernel Log: X.org 7.5 coming in summer, re-write for Intel's graphics driver"
date: 2009-05-04
author: "Terry Relph-Knight"
source: http://www.h-online.com/open/news/item/Kernel-Log-X-org-7-5-coming-in-summer-re-write-for-Intel-s-graphics-driver-741405.html
pages: 1
---

# Kernel Log: X.org 7.5 coming in summer, re-write for Intel's graphics driver

**Terry Relph-Knight**

![Kernel Log logo](../site/imgs/43/3/6/7/8/3/7/a345f5e7c547062f.jpg) **X.org 7.5 is scheduled to appear in summer, and could include a new Intel graphics driver. The developers have slashed its code to boost reliability and performance. The kernel developers have now presented versions 2.6.30-rc4 and 2.6.29.2 of Linux, 2.6.27.22 and 2.6.28.10 are released and guest mascot Tuz bows out.**

On the X.org mailing list, X.org programmer Daniel Stone has presented a [new schedule](http://thread.gmane.org/gmane.comp.freedesktop.xorg/31957/focus%3D668) for the development and release of [X.org 7.5](http://xorg.freedesktop.org/wiki/Releases/7.5) and the X Server 1.7 provided for it. He concedes that the original plan to complete X.org 7.5 for early April has come to nothing, and now suggests mid-July as a new target date.

The developers plan to accept all the essential new functions by the end of May and begin releasing beta versions in the second half of June. Stone says in his posting that the integration of ([X input 2](http://lists.x.org/archives/xorg-devel/2009-March/000514.html)) of XI2 is steaming ahead; he's planning to incorporate XKB2 (X Keyboard Extension 2) itself in the coming weeks. The [X.org Wiki](http://xorg.freedesktop.org/wiki/Releases/7.5) says the planned [Multi-Pointer X](http://wearables.unisa.edu.au/mpx/) (MPX), [input device properties](http://who-t.blogspot.com/2008/07/input-device-properties.html) (IDP) and [predictable pointer acceleration](http://xorg.freedesktop.org/wiki/Development/Documentation/PointerAcceleration) are already partially contained in the X.org 7.5/X Server 1.7 development tree.

However, as Stone emphasises, this is only a temporary plan. Experience with previous versions of X.org and X Server does show that X developers not infrequently miss their own planned release dates by weeks, [X Server 1.6, for example](../site/news/item/X-Server-1-6-released-740261.html "X Server 1.6 released – 26 February 2009, 10:03"), or even several months, as they did with [X.org 7.4](../site/news/item/X-org-7-4-comes-complete-with-new-functions-new-drivers-and-new-incompatibilities-737419.html "X.org 7.4 comes complete with new functions, new drivers and new incompatibilities – 24 September 2008, 15:48").

**Slimming down**

Intel developer Carl Worth has now [released](http://thread.gmane.org/gmane.comp.freedesktop.xorg/38741) "2.7.99.1 snapshot", the first pre-release version of 2.8-series drivers for the xf86-video-intel X.org graphics driver, usually known for short as "[intel](http://wiki.x.org/wiki/intel)". It's about 10 per cent smaller than Intel's current 2.7-series drivers, and could possibly be delivered later along with X.org 7.5. It was possible to reduce the code by removing support for the XAA and EXA 2D graphics acceleration architectures and relying on the Intel-specific UXA, a derivative of EXA; support for DRI1 has also been ditched. However this change does mean that the driver now requires at least X Server 1.6 or later.

The aim of this step is to simplify driver maintenance and improve quality, because it makes it much more likely that actually tested code paths will be used. Keith Packard, an X developer of many years' experience, explains the background to this procedure in more detail in his blog entry "[Sharpening the Intel Driver Focus](http://keithp.com/blogs/Sharpening_the_Intel_Driver_Focus/)". Here he describes the various techniques used for mode setting (User mode, kernel-based mode setting/KMS), for direct rendering (no DRI, DRI1, DRI2), memory management (X Server/drivers, GEM) and 2D acceleration (none, XAA, EXA, UXA), and calculates that these can theoretically be combined with each other in 48 different ways. Some of them, he says, won't work together at all, while only a few have been tested and optimised for speed. Some combinations work better on new hardware, others on older kit.

This will cause [many problems](../site/open/features/Ubuntu-9-04-and-Intel-graphics-746438.html "Ubuntu 9.04 and Intel graphics – 02 May 2009, 10:31") in practice, so the developers plan to focus on KMS, DRI2, GEM and UXA in future. The ten-per-cent reduction in code in the pre-release versions of the 2.8-series drivers is only the beginning, says Packard, who hopes to shrink the code for the next generation of drivers by 50 per cent. The many possible combinations and the ensuing problems are already causing plenty of headaches for some users and for the developers of the [recently presented Ubuntu 9.04](../site/open/features/Ubuntu-9-04-on-the-test-bench-746436.html "Ubuntu 9.04 on the test bench – 24 April 2009, 12:12"). The Intel driver, according to some internet user reports and some tests run by the editors of c't, occasionally suffers serious performance problems. These can sometimes be eliminated or reduced, however, using some of the [tricks assembled](https://wiki.ubuntu.com/X/Troubleshooting/IntelPerformance) in the Ubuntu Wiki.

![Tuz](../site/imgs/43/3/6/7/8/3/7/86c7b1360b88b6e8.jpg) **Kernel status**

- Following the release [of 2.6.30-rc3](http://thread.gmane.org/gmane.linux.kernel/825801) last week, Linus Torvalds [launched](http://thread.gmane.org/gmane.linux.kernel/829860) the fourth pre-release version of 2.6.30 in the middle of this week. Instead of "Temporary Tasmanian Devil" it's now [called](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=091438dd5668396328a3419abcbc6591159eb8d1) "Vindictive Armadillo". Tuz, who [served as a guest Linux mascot](../site/news/item/Kernel-Log-Tasmanian-devil-to-be-Linux-s-temporary-mascot-new-Radeon-drivers-740667.html "Kernel Log: Tasmanian devil to be Linux's temporary mascot, new Radeon drivers – 19 March 2009, 15:43"), [has been relieved of his task](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3d4f16348b77efbf81b7fa186a18a0eb815b6b84), handing the job back to Tux.

<!-- -->

- The minders of the Linux stable series have [released version 2.6.29.2 of the kernel](http://thread.gmane.org/gmane.linux.kernel/828139). This contains around a hundred minor improvements and corrections, some of which eliminate security-related errors. A new 2.6.28 version, [2.6.28.10](http://thread.gmane.org/gmane.linux.kernel/831202), has been released. This will be the last one, since Greg Kroah-Hartman has announced the end of maintenance for the 2.6.28 series. Some kernel developers are unhappy about this, because a series is normally maintained until its second successor arrives (2.6.30 in this case). The stable team has not yet written off the 2.6.27 series and has released [version 2.6.27.22](http://thread.gmane.org/gmane.linux.kernel/831201) over the weekend.

**In Brief**

- The developers of the [Hplip project](http://hplipopensource.com/) have published [versions 3.9.4 and 3.9.4b](http://hplipopensource.com/hplip-web/release_notes.html) of the Hplip drivers for HP printers and multifunction devices. These include support for the HP LaserJet p1009, Designjet models 4020ps, 4520ps and 4520mfp, and Officejet 6500 with or without WLAN module.

<!-- -->

- Things were very very quiet for usbutils for a long time, but Greg Kroah-Hartman has published [version 0.81](http://thread.gmane.org/gmane.linux.usb.general/17119) of the package, which contains lsusb among other things.

<!-- -->

- Jerome Glisse gives an overview [in his blog](http://jglisse.livejournal.com/1822.html) of the latest developments in support for kernel-based mode setting (KMS) for Radeon graphics hardware.

<!-- -->

- The developers of Intel graphics drivers for Linux have [presented](http://lists.freedesktop.org/archives/xorg-announce/2009-April/000830.html) "intel-gpu-tools". These include some useful programs for developing drivers and trouble-shooting.

<!-- -->

- In her blog posting "[Don't Panic - fsync(), ext3/4, and your data](http://valhenson.livejournal.com/37921.html)", Valerie Aurora (formerly Henson) explains some aspects of the much discussed features of Ext3 and Ext4 that are important for programmers and were recently also discussed in detail in the Kernel Log "[What's coming in 2.6.30: File Systems](../site/open/Kernel-Log-What-s-coming-in-2-6-30-File-systems-New-and-revamped-file-systems--/news/113157)" as part of the "What's coming in 2.6.30" series of articles.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the Kernel Log at The H Open Source:*

- [Kernel Log: What's coming in 2.6.30 - File systems: New and revamped file systems](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-File-systems-New-and-revamped-file-systems-741319.html "Kernel Log: What's coming in 2.6.30 - File systems: New and revamped file systems – 27 April 2009, 16:11")
- [Kernel Log: 3D support for the new Radeon driver; new Intel drivers](../site/news/item/Kernel-Log-3D-support-for-the-new-Radeon-driver-new-Intel-drivers-741271.html " Kernel Log: 3D support for the new Radeon driver; new Intel drivers – 22 April 2009, 17:06")
- [Kernel Log: What's coming in 2.6.30 - Network: New Wi-Fi drivers and other network novelties](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-Network-New-Wi-Fi-drivers-and-other-network-novelties-741197.html "Kernel Log: What's coming in 2.6.30 - Network: New Wi-Fi drivers and other network novelties – 17 April 2009, 10:51")
- [Kernel Log: Linux 2.6.30 is taking shape](../site/news/item/Kernel-Log-Linux-2-6-30-is-taking-shape-741093.html "Kernel Log: Linux 2.6.30 is taking shape – 09 April 2009, 06:41")
- [Kernel Log: Development of 2.6.30 is under way](../site/news/item/Kernel-Log-Development-of-2-6-30-is-under-way-740805.html "Kernel Log: Development of 2.6.30 is under way – 27 March 2009, 17:33")
- [Steady Growth: What's new in Linux 2.6.29](../site/open/features/Steady-growth-What-s-new-in-Linux-2-6-29-746553.html)

*Older Kernel Logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([trk](mailto:trk@h-online.com "Terry Relph-Knight"))
