---
title: "Kernel Log: Linux and hard disks with 4-KByte sectors"
date: 2010-02-24
author: "Chris von Eitzen"
source: http://www.h-online.com/open/news/item/Kernel-Log-Linux-and-hard-disks-with-4-KByte-sectors-939523.html
pages: 1
---

# Kernel Log: Linux and hard disks with 4-KByte sectors

**Chris von Eitzen**

#### ![Kernel Log](../site/imgs/43/4/8/6/7/3/9/KL.jpg-1f663d67fe8a53b0.jpeg) by Thorsten Leemhuis

**In future, fdisk will arrange partitions in such a way that the new hard disks with 4-KByte sectors can achieve optimum performance – although, for now, users will still need to select fdisk's appropriate mode of operation manually. The developers of Realtime Linux have released new kernel versions, and the completion of 2.6.32.9 and 2.6.33 is also approaching.**

Red Hat developer Karel Zak has [released](http://thread.gmane.org/gmane.linux.file-systems/38367) version 2.17.1 of the util-linux-ng tool collection used in many Linux distributions. It includes the "fdisk" command line program which, in its sector-based mode of operation, activated via the "-u" option, will from now on try to align partitions along megabyte boundaries in the same way as Windows 7 and Vista have done for some time. While this sounds like a minor change, it is essential for the gradually emerging large hard disks that work with 4-KByte sectors internally while, for compatibility reasons, externally pretending to use 512-Byte sectors like any other desktop hard disk released in the past 20 years.

Linux file systems prefer to read and write in 4-KByte blocks, but older versions of fdisk arrange the first partition in such a way that it begins with the (512-Byte) sector 63 by default – which is right in the middle of a physical (4-KByte) sector. Writing 4 KBytes of data to the beginning of the partition consequently requires the hard disk to read two physical sectors of 4 KBytes, distribute the 4 KBytes of data across these two physical sectors, wait for the disks to do an extra round and then write the two sectors back to disk.

This causes the data throughput of all 4-KByte sectored hard disks (as well as some RAID arrays) to be significantly lower than that of a volume whose partitions start at (512-Byte) sector numbers which are divisible by eight. More background information can be found in an article at [LWN.net](http://lwn.net/Articles/322777/). Western Digital's WD10EARS, for example, is one of the first desktop SATA hard disks on the shelves that uses 4-KByte sectors internally.

Only recently, the problem sparked prolonged discussions at [Slashdot](http://hardware.slashdot.org/story/10/02/14/1541244/Linux-Not-Quite-Ready-For-New-4K-Sector-Drives) following the release of an [article](http://www.osnews.com/story/22872/Linux_Not_Fully_Prepared_for_4096-Byte_Sector_Hard_Drives) entitled "Linux not fully prepared for 4096-Byte sector hard drives" by OSNews. The correctness of this headline varies with the [interpretation of the term "Linux"](../site/open/features/When-is-it-worth-saying-it-s-Linux-917518.html "When is it worth saying it's Linux? – 29 January 2010, 18:22"), as the Linux kernel is hardly at fault; it has already informed userland applications about the parameters relevant for optimum partition alignment since the [I/O topology patches in Linux 2.6.31](../site/open/features/The-nitty-gritty-proceedings-of-the-Linux-Symposium-2009-746605.html "The nitty gritty - proceedings of the Linux Symposium 2009 – 11 August 2009, 16:03").

Fdisk, on the other hand, has only used this information since the [January version of util-linux-ng](../site/news/item/Kernel-Log-Long-term-maintenance-for-2-6-32-util-linux-ng-extended-910616.html "Kernel Log: Long-term maintenance for 2.6.32, util-linux-ng extended – 22 January 2010, 13:24"). However, this doesn't fully eradicate the problem because fdisk isn't the only partitioning tool included in Linux distributions. The distribution installers also need to be adapted or need to use fdisk in the correct way – [in a comment](http://www.osnews.com/thread?409410) concerning the OSNews article mentioned above, the developer of the I/O topology patches, Martin K. Petersen, suspects that this is currently only the case in Fedora.

The version of fdisk used in the current util-linux-ng 2.17.1 not only aligns partitions along megabyte boundaries, it also recognises the "-c" parameter. This parameter disables a DOS compatibility mode which is incompatible with the new approach because it involves aligning partitions along logical cylinder boundaries – this was required by DOS before the advent of LBA addressing and is still used by fdisk unless the tool is switched to sector-based operation by adding "u" or the "-u" command line parameter. While the DOS mode has been marked as deprecated, this version is the last to include it as its default for compatibility reasons. Until this changes, the sector-based display should be activated manually to ensure that 4-KByte hard disks are aligned correctly.

### Linux version status

A week after the release of the [previous regular Kernel Log](../site/news/item/Kernel-Log-Long-term-maintenance-for-2-6-32-util-linux-ng-extended-910616.html "Kernel Log: Long-term maintenance for 2.6.32, util-linux-ng extended – 22 January 2010, 13:24"), the maintainers of the Stable Series have released kernel version [2.6.32.8](http://thread.gmane.org/gmane.linux.kernel/948081), which differs from its predecessor by [more than 70 patches](http://thread.gmane.org/gmane.linux.kernel/946506). Kernel developer Greg Kroah-Hartman [released](http://thread.gmane.org/gmane.linux.kernel/953294) Linux kernel version 2.6.32.9 just 24 hours ago.

The eighth release candidate of 2.6.33 is now [more than 10 days old](http://thread.gmane.org/gmane.linux.kernel/949447). Although, in this phase of the development cycle, Torvalds usually releases a new RC every week, we dare not predict whether this indicates the imminent release of Linux 2.6.33, or whether a 2.6.33-rc9 will be appear beforehand.

The past few days have also seen a lot of activity from the developers of the RT branch, who develop Linux kernels with real-time functionality. For instance, [an announcement](http://www.osadl.org/Single-View.111+M5ce948a0fdf.0.html) posted by the OSADL (Open Source Automation Development Lab) says the [recently released version 2.6.31.12-rt21](http://thread.gmane.org/gmane.linux.kernel/879066/focus%3D5546) is now considered the "Latest Stable". The OSADL web page also offers [a short report](http://www.osadl.org/Single-View.111+M5602c30ec73.0.html) about the renamed spinlocks mentioned in [part 4](../site/news/item/Kernel-Log-Coming-in-2-6-33-Part-4-Architecture-and-virtualisation-929402.html "Kernel Log: Coming in 2.6.33 (Part 4) - Architecture and virtualisation – 12 February 2010, 15:51") of the Kernel Log's "Coming in 2.6.33" mini series. Thomas Gleixner [writes](http://lkml.indiana.edu/hypermail/linux/kernel/1002.2/02212.html) that the renaming measure has significantly reduced the size of the real-time patches, in the release email for Linux 2.6.33-rc8-rt1 – the first RT kernel to be based on the current release candidates of Linux 2.6.33.

### In brief

*Kernel*

- In mid February, the developers had [a long discussion](http://thread.gmane.org/gmane.linux.kernel/949008) on the LKML about switching the kernel archives at kernel.org to the "XZ" compression format. While no summary or appropriate road map has so far been released, there is evidence to suggest that the kernel sources will also become available in XZ format. XZ compresses more efficiently than Gzip (.gz) and is faster than Bzip2 (.bz2). In the long term the latter may be abandoned and the old files removed; however, files compressed with Gzip will probably remain available.
- In his "[XFS status update for January 2010](http://thread.gmane.org/gmane.linux.kernel/948648)", Christoph Hellwig gives an overview of the latest developments in the XFS filesystem area.

*Kernel environment ("plumbing layer") and userland drivers*

- Theodore Ts'o has [released](http://thread.gmane.org/gmane.comp.file-systems.ext4/17599) E2fsprogs version 1.41.10, which includes numerous bug fixes and several, mostly minor, improvements.
- Shortly after the [previous regular Kernel Log](../site/news/item/Kernel-Log-Long-term-maintenance-for-2-6-32-util-linux-ng-extended-910616.html "Kernel Log: Long-term maintenance for 2.6.32, util-linux-ng extended – 22 January 2010, 13:24"), Jean Delvare [released](http://lists.lm-sensors.org/pipermail/lm-sensors/2010-February/027759.html) lm-sensors version 3.1.2, which offers various, mostly minor, improvements and supports recent kernels.
- In his blog, Novell developer Michael Meeks has released a [presentation![PDF](../site/icons/file-pdf.gif "PDF document")](http://www.gnome.org/~michael/data/2010-02-09-bootchart2.pdf) to demonstrate some of the advantages of Bootchart2, which he contributed to, over the first "Bootchart" boot analysis program.
- An article at IBM Developerworks entitled "[Virtio: An I/O virtualization framework for Linux](http://www.ibm.com/developerworks/linux/library/l-virtio/index.html)" provides some background about the Virtio framework, which is used for paravirtualised drivers by Lguest and KVM.
- The developers of [project Gutenprint](http://gutenprint.sourceforge.net/) have [released](http://sourceforge.net/projects/gimp-print/files/gutenprint-5.2/5.2.5/NEWS/view) version 5.2.5 of their identically named printer driver collection. It supports numerous Epson printers its predecessor wasn't able to handle.
- Till Kamppeter has released [version 4.0.4](http://forums.linux-foundation.org/read.php?21,11485,11485#msg-11485) of Foomatic, which many Linux distributions use when configuring and addressing printers. Recently, Kamppeter [also announced](http://forums.linux-foundation.org/read.php?21,11512,11512#msg-11512) that the OpenPrinting web site and its printer driver information database have been upgraded.
- The recently [released version 2.8](http://lkml.indiana.edu/hypermail/linux/kernel/1002.2/02108.html) of the [Gujin](http://gujin.sourceforge.net/) boot loader now supports GPT (GUID Partition Table) partitions.

*Graphics*

- Peter Hutterer has [released](http://thread.gmane.org/gmane.comp.freedesktop.xorg/42458) version 1.7.5 of the X.org X Server. It is the last planned update in this series: With hardly any further patches being submitted, Hutterer plans to release future new versions in this series only if there is a reason for doing so. Keith Packard has [released](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/996) the first release candidate of X Server 1.8.
- AMD has released version 10.2 of its proprietary graphics drivers for Linux known as Catalyst or Fglrx. According to the [release notes![PDF](../site/icons/file-pdf.gif "PDF document")](http://www2.ati.com/drivers/linux/catalyst_102_linux.pdf), the drivers now officially support OpenSuse 11.2; however, the series 1.7 X Servers, which are part of X.org 7.5 and were [released](../site/news/item/X-org-Server-1-7-0-released-812407.html "X.org Server 1.7.0 released – 02 October 2009, 10:31") last October, still remain unsupported.
- Having posted two blog items about the development work to support hybrid graphics, as already mentioned in the [previous Kernel Log](../site/news/item/Kernel-Log-Long-term-maintenance-for-2-6-32-util-linux-ng-extended-910616.html "Kernel Log: Long-term maintenance for 2.6.32, util-linux-ng extended – 22 January 2010, 13:24"), Dave Airlie has written a [third post](http://airlied.livejournal.com/70828.html) on this topic and [released a video](http://airlied.livejournal.com/71012.html) which shows how to switch between two graphics chips.
- This year's X Developers' Summit [is to be held](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/990) in Toulouse in September.
- Bart Massey, the secretary of [X.Org's Foundation Board](http://wiki.x.org/wiki/BoardOfDirectors), has given an overview of some of the most recent developments in the work of the X.Org Foundation in an email entitled "[The State of The X.Org Foundation 2010](http://thread.gmane.org/gmane.comp.freedesktop.xorg/42627)". Shortly afterwards, he also [announced](http://thread.gmane.org/gmane.comp.freedesktop.xorg/42626) the results of the recent X.Org Foundation Board elections, which appointed Alex Deucher (AMD), Matthias Hopf (SuSE GmbH) and Keith Packard (Intel), among others.
- Carl Worth has [released](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/1000) version 2.4.18 of the libdrm to fix some problems with Intel hardware.
- [In his blog](http://zrusin.blogspot.com/2010/02/new-features.html), Zack Rusin gives some details about some planned future features of Gallium3D, also mentioning that, in the long run, the framework is to support the DirectX 11 API. This was misinterpreted as "DirectX-11 support for Linux" by various magazine and blog authors, which prompted Rusin to return to the topic [in a second blog post](http://zrusin.blogspot.com/2010/02/3d-apis.html), where he explains that the improved DirectX support he described "simply means nothing" for Linux, and that it won't make running Windows games on Linux or porting them to Linux any easier.

*See also:*

- [New attempt to integrate AppArmor into Linux](../site/news/item/New-attempt-to-integrate-AppArmor-into-Linux-935911.html "New attempt to integrate AppArmor into Linux – 19 February 2010, 15:08")
- [Git 1.7 brings some compatibility changes](../site/news/item/Git-1-7-brings-some-compatibility-changes-931300.html "Git 1.7 brings some compatibility changes – 15 February 2010, 15:23")
- [Nouveau offers experimental 3D support in Fedora 13](../site/news/item/Nouveau-offers-experimental-3D-support-in-Fedora-13-930823.html "Nouveau offers experimental 3D support in Fedora 13 – 15 February 2010, 11:42")
- [Ksplice Uptrack - reboot free Linux kernel patching](../site/news/item/Ksplice-Uptrack-reboot-free-Linux-kernel-patching-926521.html "Ksplice Uptrack - reboot free Linux kernel patching – 10 February 2010, 10:58")
- [Android code removed from Linux kernel](../site/news/item/Android-code-removed-from-Linux-kernel-920688.html "Android code removed from Linux kernel – 03 February 2010, 09:33")

Older Kernel Logs can be found in *[the archives](../site/open/news/archive/)* or by using *[the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log)* at *[The H Open Source](../site/open/)*. New editions of Kernel Logs are also mentioned on [Identi.ca](http://identi.ca/kernellog2) and [Twitter](http://twitter.com/kernellog2) via "@kernellog2". The Kernel Log author also posts updates about various topics on [Identi.ca](http://identi.ca/kernellogauthor) and [Twitter](http://twitter.com/kernellogauthor) via "@kernellogauthor".

([thl](mailto:thl@ct.heise.de))

([crve](mailto:crve@h-online.com "Chris von Eitzen "))
