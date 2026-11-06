---
title: "Kernel Log – Coming in 2.6.31 - Part 3: Storage and file systems"
date: 2009-08-17
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-Coming-in-2-6-31-Part-3-Storage-and-file-systems-742967.html
pages: 1
---

# Kernel Log – Coming in 2.6.31 - Part 3: Storage and file systems

**Dj Walker-Morgan**

![kernellogpenguin.jpg](../site/imgs/43/3/6/9/3/9/7/93e8ea3d0acdf147.jpg)

#### by Thorsten Leemhuis

**The experimental file system Btrfs, billed as the "next generation file system for Linux", should now be even faster. Libata drivers for IDE/PATA adaptors are pushing aside the IDE subsystem. The first components for defragmenting Ext4 file systems have been merged into the main development tree. Systems with Intel ATA chipsets now boot faster thanks to parallel hardware scanning.**

Last Thursday, Linus Torvalds [released](http://thread.gmane.org/gmane.linux.kernel/877351) the sixth pre-release version of Linux 2.6.31. As usual at this late phase of the development cycle, most of the changes from rc5 are minor. In his release email, Torvalds indicates that he expects 2.6.31 to be complete after the eighth pre-release version, probably in two to three weeks.

The Kernel Log is taking the opportunity to continue its series of reports on the major changes in Linux 2.6.31 compared to the current 2.6.30 kernel with an overview of storage and file systems. Previously, we have looked at the areas of [networking](../site/news/item/Kernel-Log-Coming-in-2-6-31-Part-1-New-Wi-Fi-drivers-and-other-network-related-changes-742309.html "Kernel Log - Coming in 2.6.31 - Part 1: New Wi-Fi drivers and other network-related changes – 02 July 2009, 12:44") and [graphics, audio and video](../site/news/item/Kernel-Log-Coming-in-2-6-31-Part-2-Graphics-audio-and-video-742867.html "Kernel Log - Coming in 2.6.31 - Part 2: Graphics, audio and video – 07 August 2009, 15:53").

### Btrfs upgraded

[Major changes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5d4f98a28c7d334091c1b7744f48a1acdd2a4ae0), in the form of a 350 KB patch, should significantly improve the experimental file system's performance by using 'mixed back references' in many areas. The patch does, however, involve a change in the structure of the file system on the storage media ('on disk format'). Kernel versions containing the new Btrfs code deal with the requisite conversion from old to new format automatically the first time the file system is mounted. However, Linux versions with older Btrfs code will thereafter no longer be able to mount file systems which have been modified by the new code.

This is flagged up clearly in the [commit comments](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5d4f98a28c7d334091c1b7744f48a1acdd2a4ae0) and [Git pull request](http://thread.gmane.org/gmane.comp.file-systems.btrfs/3123). Kernel developers usually try to avoid such situations, even with experimental file systems – the result of this change is that hardy users who choose to use Btrfs as their root file system will find themselves unable to start older kernel versions to deal with errors should the need arise. Indeed this is precisely the misfortune that befell Linus Torvalds, who was [distinctly unimpressed](http://article.gmane.org/gmane.comp.file-systems.btrfs/3131).

Very late in the development cycle, via a Git pull request, the Btrfs maintainer [sent through](http://thread.gmane.org/gmane.comp.file-systems.btrfs/3392) a number of major changes, work on which has been ongoing for some time. These should make Btrfs less memory hungry during long periods of high load (e.g. see [1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=963030817060e4f109be1993b9ae8f81dbf5e11a), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=817d52f8dba26d0295c26035531c30ce5f1e3c3e)). Btrfs developers have also improved support for using SSDs (e.g. see [1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c289811cc096c57ff35550ee8132793a4f9b5b59), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=451d7585a8bb1b9bec0d676ce3dece1923164e55)).

For other articles on 2.6.31 and links to the rest of the "Coming in 2.6.31" series, see The H's [Kernel Log - 2.6.31 Tracking](../site/open/features/Kernel-Log-2-6-31-Tracking-746446.html "Kernel Log - 2.6.31 Tracking – 02 July 2009, 11:21") page.

### Adieu IDE

Kernel developer David Miller, known for his work as maintainer of the networking subsystem and for SPARC support, has now also [taken over](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=920d44ed965b1fb842ae65fad1a51fc7570e1181) the IDE subsystem from Bartlomiej Zolnierkiewicz. The reason for this was [a clash](../site/news/item/Kernel-Log-Winding-down-the-IDE-subsystem-LinuxTag-Kernel-presentations-742159.html "Kernel Log : Winding down the IDE subsystem, LinuxTag Kernel presentations – 23 June 2009, 17:04") over a bug occurring on SPARC systems, in the course of which Miller suggested that Zolnierkiewicz had introduced a number of changes to the IDE subsystem without adequate testing.

Miller has [intimated](http://thread.gmane.org/gmane.linux.ports.sparc/11845/focus%3D11866) that he is not planning on implementing any major changes to the IDE subsystem, "*I'm going to treat IDE as pure legacy.*" The future therefore now looks definitively to belong to the PATA drivers in the Libata subsystem, which were merged into Linux 2.6.19 in late 2006. While they may not be able to control quite as many IDE/PATA adaptors as the IDE subsystem, they are able to deal with almost all common modern adaptors.

Many developers always viewed the Libata drivers as a replacement for the drivers in the older IDE subsystem, which has been a source of repeated strife between kernel developers for more than a decade. Following a period of almost complete inactivity, over the last eighteen months to two years Zolnierkiewicz had substantially revised the IDE subsystem and added a number of new drivers, so that instead of the anticipated lingering death, the two systems had started to look like competitors - a situation that now finds itself resolved.

### Body search

The new Fsnotify replaces Dnotify and Inotify and can be used to monitor changes to the file system, such as creation, deletion or modification of files ([1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=90586523eb4b349806887c62ee70685a49415124), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=63c882a05416e18de6fb59f7dd6da48f3bbe8273), [3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3c5119c05d624f95f4967d16b38c9624b816bdb9)). The actual goal of Red Hat employee Eric Paris, who developed Fsnotify, is Fanotify, which builds on Fsnotify and offers virus and malware scanners operating in userspace a handle for checking files for malware before they are actually accessed. Paris recently [invited discussion](http://thread.gmane.org/gmane.linux.kernel.malware/710) on the concept and design of Fanotify.

The idea arose from long discussions on TALPA, which set out to achieve the same purpose, but failed to win over kernel developers. Background information can be found in the LWN.net articles "[Kernel-based malware scanning](http://lwn.net/Articles/260918/)", "[The TALPA molehill](http://lwn.net/Articles/292872/)" and "[The fanotify API](http://lwn.net/Articles/339399/)".

### In Brief

The changes described above are just some of the more significant of those recently undertaken by kernel hackers in the file system and storage field. A short overview of further changes:

File systems:

- The Ext4 file system [now contains code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=748de6736c1e482e111f9d1b5a5d5b1787600cad) for de-fragmenting the file system while in use (online defrag). This is not, however, finished, as was recently [emphasised elsewhere](http://article.gmane.org/gmane.linux.kernel/869133) by Ext file system developer Theodore Tso (tytso). He goes on to say that further patches for this function still need to be evaluated and that there is still outstanding work to be done on the associated userspace program.

<!-- -->

- Support for NFS 4.1 [has been extended](http://thread.gmane.org/gmane.linux.nfs/27489), but further changes are still planned for 2.6.32.

Storage:

- Thanks to a [change merged](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=075affcbe01d4d7cefcd0e30a98df1253bcf8d92) prior to the handover from Zolnierkiewicz to Miller, the IDE subsystem now by default respects HPAs (Host Protected Areas) – users who deploy an HPA and are still using IDE subsystem drivers should not be surprised if their drive is a little smaller under 2.6.31.

<!-- -->

- IDE/PATA driver ata_piix for Intel controllers, which forms part of the Libata subsystem, now scans for drives [in parallel](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=517d3cc15b36392e518abab6bacbb72089658313), [halving](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=517d3cc15b36392e518abab6bacbb72089658313) initialisation time on the developer's Eee PC.

<!-- -->

- As a result of [one](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c72758f33784e5e2a1a4bb9421ef3e6de8f9fcf3) of [many changes](http://thread.gmane.org/gmane.linux.kernel/849063) to the block layer, the latter now exports information on I/O topology using [data supplied by the SCSI subsystem](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ea09bcc9c298d3057270abd78a973fc678d55c4c) – this includes a drive's physical sector size. This is, for example, of interest when allocating storage media with sector sizes other than 512 bytes or for optimal arrangement of data in RAID arrays. The developer behind this code explores some of the issues involved in a recently [released presentation](http://www.linuxsymposium.org/2009/ls-2009-proceedings.pdf#page=235&view=FitView)![PDF](../site/icons/file-pdf.gif "PDF document") (see pages 235-238). The MD code responsible for software RAIDs is [already able to make use](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8f6c2e4b325a8e9f8f47febb2fd0ed4fae7d45a9) of this topology information.

<!-- -->

- There have been major improvements to barrier support in the device mapper ([delay](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c927259e34e518d913d86f51c71b786a513f94d6), [mpath](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8627921fa2ef6d40fd9b787e163ba3a9ff8f471d), [snapshot](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=494b3ee7d4f69210def80aecce28d08c3f0755d5)).

<!-- -->

- Following the merger of generic support for OSDs ([Object-Based Storage Devices](http://en.wikipedia.org/wiki/Object_storage_device)) and a file system based on them [into 2.6.30](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-Storage-RAID-improvements-optimised-CFQ-Scheduler-SAS-drivers-741597.html "Kernel Log: What's coming in 2.6.30 - Storage: RAID improvements, optimised CFQ Scheduler, SAS drivers – 15 May 2009, 17:01"), kernel hackers have now merged the [osdblk](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2a13877c5ef3207a2a5c56250742e60808677f90) driver, which allows OSD objects to be used as block devices.

<!-- -->

- The MMC subsystem now includes a [driver by the name of via-sdmmc](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f0bf7f61b8405224bc52fc9a3ccd167a68126e00) for VIA SD/MMC card readers and a [platform driver for SDHCI](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a3456a2da14fb1d8246df63bb229623d58d09ce1)

<!-- -->

- An Emulex developer has contributed a nearly [340 KB patch](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=da0436e915a5c17ee79e72c1bf978a4ebb1cbf4d) which adds support for recent Emulex FightPulse fibre channel host adaptors to the lpfc (Light Pulse Fibre Channel) driver; this was followed by a [further update](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bbb9d18009373bc74bfeba760097de277f395858) which adds support for target reset handler entry points. The same programmer is also responsible for [FC (FibreChannel) pass-thru support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9e4f5e29610162fd426366f3b29e3cc6e575b858).

<!-- -->

- There's a new iSCSI driver for Broadcom's BNX2 chips: bnx2i. It can, if required, operate in conjunction with the new Cnic driver, which has previously been mentioned in the Kernel Log article on [changes in the networking field](../site/news/item/Kernel-Log-Coming-in-2-6-31-Part-1-New-Wi-Fi-drivers-and-other-network-related-changes-742309.html "Kernel Log - Coming in 2.6.31 - Part 1: New Wi-Fi drivers and other network-related changes – 02 July 2009, 12:44").

<!-- -->

- As well as [including various enhancements to existing features](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=20b09c2992fefbe78f8cede7b404fb143a413c52), SAS/SATA driver mvsas also adds support for 94xx series Marvell chips.

### Minor gems

Many additional minor, but by no means insignificant, changes can be found in the list below. Like many of the references in the text above, the links lead to the relevant commits in the [web front end](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=summary) of the main Linux development branch, where the commit comments and the patches themselves provide extensive further information on the respective changes.

**File systems**

Btrfs:

- [Btrfs: Add mount -o nossd](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3b30c22f64a6bb297719c60e494af1d26563f584)
- [Btrfs: honor nodatacow/sum mount options for new files](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9427216476d4fa75103f39d4b228c47d56ba20da)
- [Btrfs: reduce mount -o ssd CPU usage](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2c943de6ad795a174dcc424c293bb77f15ae3b8c)
- [Btrfs: update backrefs while dropping snapshot](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2c47e605a91dde6b0514f689645e7ab336c8592a)

CIFS:

- [CIFS: add addr= mount option alias for ip=](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=58f7f68f228c3aba2ba4468d92e2cec35724ba2e)
- [CIFS: Add mention of new mount parm (forceuid) to cifs readme](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f0472d0ec89bef2ea4432828c3daa1b26ef569aa)
- [CIFS: reinstate original behavior when uid=/gid= options are specified](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9b9d6b2434fe942895c341b9a982f158529788ec)
- [CIFS: show noforceuid/noforcegid mount options (try \#2)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4486d6ede16b362f89b29845af6fe1a26ae78a54)
- [CIFS: Update readme to indicate change to default mount (serverino)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c5077ec42303e07c2c685b0f6cb8eee0f2c7751c)
- [CIFS: Update readme to reflect forceuid mount parms](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d098564f3b2b5d555e51bca765a6a9e0dda8f2cd)
- [CIFS: Updates fs/cifs/CHANGES](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5bd9052d79daa4c8beb45436c408b6de672adb82)

Ext\[2,3&4\]:

- [Doc fix: ext2 can only have 32,000 subdirs, not 32,768](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ce05b2a9db1d86635a906f14427deff97eeb6183)
- [ext4: Avoid races caused by on-line resizing and SMP memory reordering](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8df9675f8b498d0bfa1f0b5b06f56bf1ff366dd5)
- [ext4: Change all super.c messages to print the device](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b31e15527a9bb71b6a11a425d17ce139a62f5af5)
- [ext4: document the "abort" mount option](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8a8a2050c844d9de224ff591e91bda3f77bd6eda)

NFS:

- [nfs41: Add ability to read RPC call direction on TCP stream.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=18dca02aeb3c49dfce87c76be643b139d05cf647)
- [nfs41: Add backchannel processing support to RPC state machine](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=55ae1aabfb108106dd095de2578ceef1c755a8b8)
- [nfs41: Add Kconfig symbols for NFSv4.1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1efae38140546db403845d628db9f2d608caa87e)
- [nfs41: add mount command option minorversion](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3fd5be9e19921a89d9ed78d6a708a379a6c3c76a)
- [nfs41: add session reset to state manager](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c3fad1b1aaf850bf692642642ace7cd0d64af0a3)
- [nfs41: add session setup to the state manager](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=76db6d9500caeaa774a3e32a997eba30bbdc176b)
- [nfs41: create_session operation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fc931582c260e53ca5ca23bd70ccc9b2265cca9f)
- [nfs41: Setup the backchannel](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0b5b7ae0a853c91015bb3b1729166ca65f693322)
- [nfs41: Use mount minorversion option](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5aae4a9ae0dd55409a42ca61b82ef1f5a840091e)
- [NFS: Add separate mountd status code decoders for each mountd version](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fb12529577541aa02f9c3d9e325329f9568dfb58)
- [NFS: add support for splice writes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bf40d3435caf49369058b1ed6bbc92f8e2bd92f1)
- [nfsd: support ext4 i_version](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c654b8a9cba6002aad1c01919e4928a79a4a6dcf)
- [NFS: Invalid mount option values should always fail, even with "sloppy"](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d23c45fd84f79a3b84899dac053dcafe9d43ebc9)
- [NFS: More "sloppy" parsing problems](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a5a16bae707cd5d2bc97d7bd1a30079f18113a77)
- [update Documentation/filesystems/00-INDEX with new nfsd related docs.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4ba170c2bb77713e999ac6fb9ffe6ddd99d2f25a)

Various:

- [add caching of ACLs in struct inode](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f19d4a8fa6f9b6ccf54df0971c97ffcaa390b7b0)
- [documentation: register ioctl entry of nilfs2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1392e3b33319fd1a2527bebfc56631c2f2d3c7c5)
- [FAT: add 'errors' mount option](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=85c7859190c4197a7c34066db14c25903c401187)
- [GFS2: Add commit= mount option](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=48c2b613616235d7c97fda5982f50100a6c79166)
- [GFS2: Add tracepoints](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=63997775b795f97ef51f3e56bc3abc9edc04bbb0)
- [GFS2: Update docs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e9ccb73ab57ada469602506496c42e5b4468ac3e)
- [hostfs: set maximum filesize in superblock for proper LFS support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=752fa51e4c5182c3c257f1cede90577a7e213c58)
- [isofs: let mode and dmode mount options override rock ridge mode setting](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=52b680c81238ea14693ab893d5d32a4d1c0a987d)
- [nilfs2: allow future expansion of metadata read out via get info ioctl](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=003ff182fddde09ddfb8d079bbdb02f9d2122082)
- [nilfs2: modify list of unsupported features in caveats](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fb6e7113ae3ba6c7d0de77c6ccbcfa659899ff0f)
- [ocfs2: Add statistics for the checksum and ecc operations.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=73be192b17e43b6dc4f492dab41d70ab5b9d2908)
- [partitions: warn about the partition exceeding device capacity](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=02c33b123e59cab5771e52a012aeb810500260a2)
- [proc: export statistics for softirq to /proc](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d3d64df21d3d0de675a0d3ffa7c10514f3644b30)
- [proc.txt: update kernel filesystem/proc.txt documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=349888ee7b2c1ffb44c806adf6f4289ca4a6fd42)
- [splice: implement pipe to pipe splicing](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7c77f0b3f9208c339a4b40737bb2cb0f0319bb8d)
- [update Documentation/filesystems/Locking](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7e325d3a6b117c7288bfc0755410e9d9d2b71326)
- [VFS: Add VFS helper functions for setting up private namespaces](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cf8d2c11cb77f129675478792122f50827e5b0ae)
- [xfs: use generic Posix ACL code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ef14f0c1578dce4b688726eb2603e50b62d6665a)

**Storage**

Block Layer:

- [Add serial number support for virtio_blk, V4a](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1d589bb16b825b3a7b4edd34d997f1f1f953033d)
- [block: enable by default support for large devices and files on 32-bit archs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=db29a6b49674085f136331014ba0eee249c16a2c)
- [block: rename CONFIG_LBD to CONFIG_LBDAF](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=90c699a9ee4be165966d40f1837909ccb8890a68)
- [block: Update topology documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7e5f5fb09e6fc657f21816b5a18ba645a913368e)
- [Make SCSI SG v4 driver enabled by default and remove EXPERIMENTAL dependency, since udev depends on BSG](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=14d9fa352592582e457cf75022202766baac1348)
- [ramdisk: remove long-deprecated "ramdisk=" boot-time parameter](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1adbee50fd6fce5af4feb34d2db93cfe4d2066a4)

Device Mapper:

- [dm ioctl: support cookies for udev](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=60935eb21d3c5bac79618000f38f92c249d153c4)
- [dm mpath: add queue length load balancer](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fd5e033908b7b743b5650790f196761dd930f988)
- [dm mpath: add service time load balancer](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f392ba889b019602976082bfe7bf486c2594f85c)
- [dm raid1: add userspace log](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f5db4af466e2dca0fe822019812d586ca910b00c)
- [dm: sysfs add suspended attribute](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=486d220fe4909b5745c4faa67faddd30a707abe2)

Libata:

- [ahci: add device ID for 82801JI sata controller](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b2dde6afe5d29212d521e69492ebc299db235001)
- [ahci: add device IDs for Ibex Peak ahci controllers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c1f57d9b9846e7366c328f916d1a82d03ba4312c)
- [ata_piix: Add new laptop short cable IDs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6034734d333c1bd01119a5b480b34a507a3adf56)
- [ata_piix: Add new short cable ID](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=760cdb7760be928e85a021552253eb1b39acdf37)
- [ata_piix: Turn on hotplugging support for older chips](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=347979a034539ab20f3bc0c30ac0ccd3c4fd4c2e)
- [libata: accept late unlocking of HPA](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5920dadfb4aec6c1372c5570e71bcd3b4837e63c)
- [libata: ahci: Restore SB600 SATA controller 64 bit DMA](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=58a09b38cfcd700b796ea07ae3d2e0efbb28b561)
- [libata: beautify module parameters](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ad5d8eac91bb04533e49bbb6434791758300711d)
- [libata: PATA driver for CF interface on AT91SAM9260 SoC](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=918d7b7c330f8afe18cb1b8692fc5f45a798634e)
- [sata_fsl: Add power mgmt support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=dc77ad4c8727d3a1c23eadcb287501dab480d634)
- [sata_sil: enable 32-bit PIO](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=31f80112cc7e7ea4c220d6f62b0a7052754befb3)

MMC:

- [sdhci: Add support for hosts that are only capable of 1-bit transfers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5fe23c7f51def59f66bc6aeee988ef1a467a2c8c)
- [sdhci-s3c: Samsung S3C based SDHCI controller glue](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0d1bb41ad4ebca92fafbab6d6c60438d7efef386)
- [sdhci: Specific quirk vor VIA SDHCI controller in VX855ES](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=557b06971b1f05cbadec2f376a305ee1954e9b0d)

MTD:

- [Documentation: add MTD sysfs docs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=19fe7f1a00023d2aa97617655b7ea56eb72f4db8)
- [mtd: add MEMERASE64 ioctl for \>4GiB devices](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0dc54e9f33e2fbcea28356bc2c8c931cb307d3b3)
- [mtd: add on-flash BBT support for Atmel NAND driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f4fa697c26bcd9e942de26bad970f4de1da5a49b)
- [mtd: add OOB ioctls for \>4GiB devices](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=aea7cea9fa9e39e71f95ad70b3daf98ba9972587)
- [mtd: add SST39SF040 chip to jedec_probe](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a0645ce9ba2e40fb2e2d74e47c90063015ee4527)
- [mtd: CFI 1.0 and CFI 1.1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e1b158abc532f5a9d355c187583038c4f75ab11d)
- [mtd: Flex-OneNAND support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5988af2319781bc8e0ce418affec4e09cfa77907)
- [mtd: m25p80: add support for Macronix MX25L12805D](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ab1ff210a86ae4ab5990b7bd2dc69fafbfa2355a)
- [mtd: nand: add OMAP2/OMAP3 NAND driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=67ce04bf2746f8a1f8c2a104b313d20c63f68378)
- [mtd: OneNAND: add support for OneNAND manufactured by Numonyx](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ee8f37688966ab1438d0cf42e0cb7c6595d9592c)
- [mtd: physmap_of: Add multiple regions and concatenation support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=143070e74630b9557e1bb64d899ff2cc5a1dcb48)
- [mtd: Restore suspend/resume support for mtd devices](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=15bce40cb3133bcc07d548013df97e4653d363c1)

SCSI:

- [explain the hidden scsi_wait_scan Kconfig variable](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5e2fb917920c62c5ad260962471aeb578b52ac40)
- [fcoe: Add runtime debug logging with module parameter debug_logging](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d5488eb9cd2b06f7dcca7053274edb337987c67c)
- [libfc: Add runtime debugging with debug_logging module parameter](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7414705ea4aef9ce438e547f3138a680d2d1096c)
- [libfcoe: Add runtime debugging with module param debug_logging](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=650bd12b9e31ec51d7ad0df3c4f94d863b827976)
- [SCSI: mpt2sas: add query task support for MPT2COMMAND ioctl](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ddf59a35e98aa12255ed64c892271339504cc65c)
- [SCSI: mpt2sas: LUN Reset Support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=993e0da7b767c0a7c1fd0079b16f3d28e6f25a48)
- [SCSI: mpt2sas: T10 DIF Support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3c621b3ee1432e7a2aca4a3b670b1d05f19ecf9c)
- [SCSI: mpt fusion: RAID device handling and Dual port Raid support is added](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a7938b0bb3b458fe0723608be3db6c4ed8d79a8c)
- [SCSI: net, libfcoe: Add the FCoE Initialization Protocol ethertype](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=226c7ffe74474257b4b87bd38ae8ba0030cf65e2)
- [SCSI: qla2xxx: Add 10Gb iiDMA support.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9f8fddeef2264a0315032b0aa2ee0052dad90076)
- [SCSI: qla2xxx: Add CPU affinity support.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=68ca949cdb04b4dc71451a999148fbc5f187a220)
- [SCSI: qla2xxx: Add QoS support.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2afa19a9377ca61b9489e44bf50029574fbe63be)
- [SCSI: zfcp: Add FC pass-through support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9d544f2b9bd4a0f7ba2784cc47e3591667a7b8d4)
- [sd: Block limits VPD support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d11b6916961d6ec7d7215332cbbe9feec086721d)
- [sd: Detect non-rotational devices](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3821d768912a47ddbd6cab52943a8284df88003c)

Various:

- [cciss: add cciss driver sysfs entries](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7fe063268e73681cdca1a6496a25f93d3332f517)
- [UBI: add notification API](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0e0ee1cc33de8f0cc603269b354085dee340afa0)

For other articles on 2.6.31 and links to the rest of the "Coming in 2.6.31" series, see The H's [Kernel Log - 2.6.31 Tracking](../site/open/features/Kernel-Log-2-6-31-Tracking-746446.html "Kernel Log - 2.6.31 Tracking – 02 July 2009, 11:21") page.

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
