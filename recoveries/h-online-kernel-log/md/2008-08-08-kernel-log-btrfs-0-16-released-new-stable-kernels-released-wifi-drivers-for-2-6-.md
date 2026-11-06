---
title: "Kernel Log: Btrfs 0.16 released, new stable kernels released, Wifi drivers for 2.6.27 merged"
date: 2008-08-08
author:
source: http://www.h-online.com/open/news/item/Kernel-Log-Btrfs-0-16-released-new-stable-kernels-released-Wifi-drivers-for-2-6-27-merged-736815.html
pages: 1
---

# Kernel Log: Btrfs 0.16 released, new stable kernels released, Wifi drivers for 2.6.27 merged

*In Brief*

The developers of Btrfs have released [version 0.16](http://thread.gmane.org/gmane.comp.file-systems.btrfs/1006/) of the still experimental file system. new features include Access Control Lists, support for which is needed by SE Linux, and orphan inode protection to stop losing files after a crash. Alongside these new features are improvements in the scalability and performance of the new file system.

In a [discussion on the future of the Reiser4 file system](http://thread.gmane.org/gmane.linux.kernel/715139/), Ext file system developer [Theodore Ts'o](http://thunk.org/tytso/) suggested that Reiser4 fans should have a look at Btrfs as it had a number of the same design ideas as Reiser file systems adding "the filesystem format has support for some advanced features that are designed to leapfrog ZFS", the Sun Microsystems file system.

Version 1.0 of Btrfs is, according to the [development timeline](http://btrfs.wiki.kernel.org/index.php/Development_timeline) on the [Btrfs wiki](http://btrfs.wiki.kernel.org/), due at the end of the year. Some of the planned changes include modifications to the on disk format of the file system, so testers will have to clear out their previous Btrfs file system and rebuild; this is also the case for the 0.16 update, which changes disk format from 0.15.

------------------------------------------------------------------------

[As expected](../site/news/item/Kernel-Log-New-Stable-kernel-DRI2-postponed-Xgl-removed-from-X-org-736743.html "Kernel Log: New Stable kernel, DRI2 postponed, Xgl removed from X.org – 05 August 2008, 10:31"), Greg Kroah-Hartman released Linux kernel versions [2.6.25.15](http://thread.gmane.org/gmane.linux.kernel/717649) and [2.6.26.2](http://thread.gmane.org/gmane.linux.kernel/717651/). There are some changes in hardware support, but the bulk of the changes are bug fixes throughout the kernel.

Again, it is not clear if the bug fixes close any vulnerabilities; the release mails only suggest users of the previous releases of the kernel upgrade to these new releases. This appears to be the new standard text for release mails, which first appeared with [the release of 2.6.15.13](../site/news/item/Kernel-log-2-6-25-13-corrects-a-vulnerability-problems-with-ACPI-736703.html "Kernel log: 2.6.25.13 corrects a vulnerability, problems with ACPI – 31 July 2008, 14:42"), where a security issue was resolved by not explicity noted.

Developers who compile and install their own kernels should install these updates, because without a laborious search through the changelogs, there's no easy way of determining whether a security issue has been addressed. Users who want to avoid this work should leave it to a Linux distributor and run with that distributions kernel, as they will advise when security issues are being addressed.

------------------------------------------------------------------------

Linux 2.6.27 development continues to move forward with Linus Torvalds publishing the second release candidate (rc) of the next main development branch. According to [`diffstat`](http://invisible-island.net/diffstat/), since 2.6.26, 11,628 files have changed with 884,674 lines of code inserted and 747,723 lines deleted. This is [considerably more](http://www.heise-online.co.uk/open/Polish-and-add-ons-the-latest-updates-in-Linux-2-6-26--/features/111079/4) than 2.6.24 and 2.6.25. Apart from bigger patches, a lot of this change is due to renaming of architectures in the source tree; see the commits for [ARM](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4baa9922430662431231ac637adedddbb0cfb2d7), [IA64](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=7f30491ccd28627742e37899453ae20e3da8e18f), [PowerPC](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b8b572e1015f81b4e748417be2629dfe51ab99f9) and [SPARC](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a439fe51a1f8eb087c22dd24d69cebae4a3addac) for examples. Taking these changes into account, then only 10,002 files have changed with 621,877 lines of code inserted and 499,076 lines removed.

Before the release of 2.6.27-rc2, some major structural changes occurred in the network are of the main development branch. Among the changes ([1](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e227ceac8429ecd775c213838f0415700727b7b4),[2](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=25bc2deda9e8a430ed49f507a1120fb2c86abf33) and [3](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4fc22b21b3fcb3580c32b70605ef114178f8e611)), the driver code for the Intel 802.11n Wifi chips, previously know as the iwl4965 driver and the code which was introduced at the start of 2.6.27 for the Wifi in Centrino-2 notebooks has been merged together to creat the iwl-agn driver module. There were also changes in the [ath5k driver](http://madwifi.org/wiki/About/ath5k) unblocking the Atheros AR2425 WLAN chips used in the first generation of EEE PCs.

The [attk9k](../site/news/item/Kernel-log-ath9k-driver-for-new-Atheros-WLAN-chips-discussions-of-Nvidia-drivers-736563.html "Kernel log: ath9k driver for new Atheros WLAN chips, discussions of Nvidia drivers – 22 July 2008, 15:48") driver for the current 802.11n Atheros chipset has [not quite made it into the main development branch](http://thread.gmane.org/gmane.linux.kernel.wireless.general/19276/focus%3D19316), but it looks like this will happen soon. The ath9k developers have [a wiki page about the driver](http://wireless.kernel.org/en/users/Drivers/ath9k) and [a longer To Do list](http://wireless.kernel.org/en/users/Drivers/ath9k#TODO).

------------------------------------------------------------------------

Linus Torvalds emphasised how stable interfaces are very important for userland applications in a recent [debate](http://thread.gmane.org/gmane.linux.kernel.next/2028/focus%3D2083) on the LKML. A change was proposed to fix the synaptics touch driver on 2.6.28 by changing a kernel api. But the issue was not with the kernel, but with a previously undiscovered bug in the synaptics drivers. At the insistence or and with the help of Torvalds, a [kernel patch](http://article.gmane.org/gmane.linux.kernel.input/5480) was put together to ensure that the driver worked with future kernel versions.

## In Brief

- Ulrich Drepper explains how applications work with secure file descriptor handing in 2.6.27 in a [blog post](http://udrepper.livejournal.com/20407.html)
- In an [email](http://thread.gmane.org/gmane.comp.freedesktop.xorg/30989/focus%3D31011) Kristian Høgsberg explains his reasons for the \[ticker:uk_111242\]removal of DRI2 in X Server 1.5\] and his planned redesign.
- Keith Packard [reveals in his blog](http://keithp.com/blogs/UMA_Acceleration_Architecture/) details about the experimental extension for GEM named UXA, UMA Acceleration Architecture.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kenrel Log: New Stable kernel, DRI2 postponed, Xgl removed from X.org](../site/news/item/Kernel-Log-New-Stable-kernel-DRI2-postponed-Xgl-removed-from-X-org-736743.html "Kernel Log: New Stable kernel, DRI2 postponed, Xgl removed from X.org – 05 August 2008, 10:31")
- [Kernel Log: New Nvidia drivers are still slow, Linux 2.6.26.1 soon](../site/news/item/Kernel-Log-New-Nvidia-drivers-are-still-slow-Linux-2-6-26-1-soon-736723.html "Kernel Log: New Nvidia drivers are still slow, Linux 2.6.26.1 soon – 04 August 2008, 09:07")
- [Kernel Log : Tux3 file system announced, X.org updates](../site/news/item/Kernel-Log-Tux3-file-system-announced-X-org-updates-736707.html "Kernel Log : Tux3 file system announced, X.org updates – 01 August 2008, 09:17")
- [Kernel Log: 2.6.25.13 corrects a vulnerability, problems with ACPI](../site/news/item/Kernel-log-2-6-25-13-corrects-a-vulnerability-problems-with-ACPI-736703.html "Kernel log: 2.6.25.13 corrects a vulnerability, problems with ACPI – 31 July 2008, 14:42")
- [Kernel Log: First release candidate concludes the hot development phase of 2.6.27](../site/news/item/Kernel-Log-First-release-candidate-concludes-the-hot-development-phase-of-2-6-27-736695.html "Kernel Log: First release candidate concludes the hot development phase of 2.6.27 – 31 July 2008, 12:23")
- Kernel Log: Practical Practices - Ottawa Linux Symposium Notes

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
