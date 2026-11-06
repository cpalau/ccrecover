---
title: "Kernel Log: Ext4 completes development phase as interim step to btrfs"
date: 2008-10-17
author:
source: http://www.h-online.com/open/news/item/Kernel-Log-Ext4-completes-development-phase-as-interim-step-to-btrfs-737697.html
pages: 1
---

# Kernel Log: Ext4 completes development phase as interim step to btrfs

![](../site/imgs/43/3/6/4/4/6/8/93e8ea3d0acdf147.jpg) Linus Torvalds has integrated a large [collection of patches](http://thread.gmane.org/gmane.comp.file-systems.ext4/9283) prepared by (Ext) filesystem developer Theodore Ts'o (tytso) into the main development branch of Linux. It contains [a patch for Ext4](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=03010a3350301baac2154fa66de925ae2981b7e3) which allows it to present itself as ext4 instead of ext4dev. This signals that with the next kernel version 2.6.28, the successor to ext3 will finally leave behind its "hot" development phase. The kernel developers integrated an early version of Ext4 in the main development branch of Linux 2.6.19 in order to jointly develop it to maturity there.

This by no means concludes the development of Ext4 and it is expected that the developers will steadily continue to develop the filesystem in the same way they developed Ext3, not only fixing bugs but also adding the occasional function. The filesystem structures used on storage media are no longer going to be affected by these changes – therefore, the file backup and media reformatting tasks required during the development of Ext4 within the official Linux kernel should no longer be necessary. Users will also no longer be required to ensure that their kernel version, Ext4 utilities (e2fsprogs) and storage media formats match up.

It is a matter of opinion whether this makes Ext4 ready for production use – administrators in corporate environments and the developers of the Enterprise distributions of Novell and Red Hat will probably wait a little longer and observe how the filesystem functions on an everyday basis for Fedora and OpenSuse users. A Red Hat developer has already [integrated](https://www.redhat.com/archives/fedora-devel-list/2008-October/msg00562.html) the patches intended for 2.6.28 into the kernel of Fedora Rawhide. Rawhide is going to be basis of Fedora 10, which is due out at the end of November. The installer will only be able to set up Ext4 file systems if the system is booted [particular parameter set](https://www.redhat.com/archives/fedora-devel-list/2008-October/msg00575.html). A separate boot partition containing one of the current filesystems is also required because boot loaders like Grub are still incapable of loading the kernel from a partition in Ext4 format.

Probably as important as the completion of Ext4's development phase may be is the information posted by Theodore Ts'o to the [Linux Kernel Mailing List](http://www.kernel.org/pub/linux/docs/lkml/) (LKML) [in a long email](http://thread.gmane.org/gmane.linux.file-systems/26246/focus%3D26492) a few days ago. In his contribution to the discussions around a possible inclusion of the btrfs filesystem, usually pronounced "butter FS", recently mentioned in the kernel log ([1](../site/news/item/Kernel-Log-2-6-27-nearing-completion-Btrfs-to-be-added-to-the-kernel-737489.html "Kernel Log: 2.6.27 nearing completion; Btrfs to be added to the kernel? – 01 October 2008, 09:23"), [2](../site/news/item/Kernel-Log-problem-with-e1000e-bypassed-Morton-praises-Btrfs-737561.html "Kernel Log: problem with e1000e bypassed, Morton praises Btrfs – 07 October 2008, 08:47")), Theodore Ts'o mentioned that he and several other well-known filesystem developers met for a "Next Generation Filesystem" workshop (NGFS) a little less than a year ago. According to Ts'o, participants agreed that Linux needs a "next generation filesystem":"*At the end of the that workshop, there was unanimous agreement (including from yours truly) that (a) Linux needed a next generation filesystem to be competitive, (b) Chris Mason's btrfs (with some changes/enhancements discussed during the workshop) was the best long-term solution for NGFS, and (c) because creating a new enterprise filesystem always takes longer than people expect, and even then, it takes a while for enterprise users to trust a new filesystem for their most critical data, ext4 in the next generation of filesystems was needed as the bridge to the NGFS.*".

With these hardly publicised recommendations, the workshop participants hoped to inspire various companies and their developers to contribute to the development of btrfs. The participants also hoped to get the distributions to back up their plans. This seems to have worked to some degree, because according to Theodore Ts'o, "But I think it is fair to say that btrfs isn't just a private a project of a single Linux kernel developer, but rather the design has been discussed and reviewed by a large number of experienced filesystem architects."

The Ext4 developer also praised btrfs developer Chris Mason who used to be responsible for Reiserfs at Suse and now works for Oracle. He said that Mason is a respected and trustworthy kernel developer who can write good code and also maintain it. Theodore Ts'o, like [Andrew Morton recently](../site/news/item/Kernel-Log-problem-with-e1000e-bypassed-Morton-praises-Btrfs-737561.html "Kernel Log: problem with e1000e bypassed, Morton praises Btrfs – 07 October 2008, 08:47"), advocates the inclusion of btrfs into the main development branch of Linux in the near future. There, it can continue to be developed and mature in the coming months and years – similar to how the kernel developers handled Ext4 in the last few months and years.

**In Brief**

- It's not just the developers of ext4 and btrfs who have been busy. The programmers of [ntfs-3g](http://www.ntfs-3g.org/), which was developed using [FUSE](http://fuse.sourceforge.net/) (Filesystem in Userspace), have had some success. [Version 1.5012](http://article.gmane.org/gmane.comp.file-systems.ntfs-3g.devel/638) is the first version to be able to create or delete any number of files and directories within the maximum limits defined by NTFS. The developers successfully used a predecessor of the new version to create 54 million files on a parition formatted with NTFS.

<!-- -->

- The developers of the [Gutenprint](http://gutenprint.sourceforge.net/) collection of printer drivers have [released the first release candidate of Gutenprint 5.2](http://sourceforge.net/project/shownotes.php?group_id=1537&release_id=630990).

<!-- -->

- [Peter Hutterer has given an overview of the "device properties"](http://who-t.blogspot.com/2008/10/device-properties-have-landed.html), in his blog. Device Properties are intended for X Input Extension 1.5 which will allow users to adjust, the parameters of input devices such as Synaptics touchpads during operation.

<!-- -->

- The developers of the [radeonhd](http://wiki.x.org/wiki/radeonhd) graphics driver have released versions [1.2.2](http://lists.freedesktop.org/archives/xorg/2008-October/039353.html) and [1.2.3](http://lists.freedesktop.org/archives/xorg/2008-October/039357.htm). Amongst the changes, these versions offer Xvideo support and, if used with current versions of X Server, Mesa 3D support for graphics hardware incorporating the R5*xx* (Radeon X1000 series) and RS6*xx* (for example the 690G mainboard chipset) Radeon GPUs.

<!-- -->

- First results of the [survey about the Git source code management system](http://thread.gmane.org/gmane.comp.version-control.git/94511/focus%3D98169) used in Linux development and started by Linus Torvalds have [recently gone online](http://git.or.cz/gitwiki/GitSurvey2008).

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: Linux 2.6.27 Released](../site/open/features/Kernel-Log-Linux-2-6-27-Released-746496.html "Kernel Log: Linux 2.6.27 Released – 10 October 2008, 08:38")
- [Kernel Log: problem with e1000e bypassed, Morton praises Btrfs](../site/news/item/Kernel-Log-problem-with-e1000e-bypassed-Morton-praises-Btrfs-737561.html "Kernel Log: problem with e1000e bypassed, Morton praises Btrfs – 07 October 2008, 08:47")
- [Kernel Log: 2.6.27 nearing completion; Btrfs to be added to the kernel?](../site/news/item/Kernel-Log-2-6-27-nearing-completion-Btrfs-to-be-added-to-the-kernel-737489.html "Kernel Log: 2.6.27 nearing completion; Btrfs to be added to the kernel? – 01 October 2008, 09:23")
- [Kernel Log: Kernel Summit info; Plumbers keynote online; the latest on the e1000e problem](../site/news/item/Kernel-Log-Kernel-Summit-info-Plumbers-keynote-online-the-latest-on-the-e1000e-problem-737443.html "Kernel Log: Kernel Summit info; Plumbers keynote online; the latest on the e1000e problem – 26 September 2008, 10:59")
- [Kernel Log: The second day of Kernel Summit 2008; criticism of Ubuntu at the opening of the Linux Plumbers Conference](../site/news/item/Kernel-Log-The-second-day-of-Kernel-Summit-2008-criticism-of-Ubuntu-at-the-opening-of-the-Linux-Plumbers-Conference-737379.html "Kernel Log: The second day of Kernel Summit 2008; criticism of Ubuntu at the opening of the Linux Plumbers Conference – 19 September 2008, 15:58")
- [Kernel Log: Hard core Linux developers discuss the future of Linux at the Kernel Summit](../site/news/item/Kernel-Log-Hard-core-Linux-developers-discuss-the-future-of-Linux-at-the-Kernel-Summit-737327.html "Kernel-Log: Hard core Linux developers discuss the future of Linux at the Kernel Summit – 17 September 2008, 11:48")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
