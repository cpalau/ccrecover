---
title: "Kernel Log: What's coming in 2.6.30 - File systems: New and revamped file systems"
date: 2009-04-27
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-What-s-coming-in-2-6-30-File-systems-New-and-revamped-file-systems-741319.html
pages: 1
---

# Kernel Log: What's coming in 2.6.30 - File systems: New and revamped file systems

**Dj Walker-Morgan**

![Kernel Log Penguin](../site/imgs/43/3/6/7/7/5/1/93e8ea3d0acdf147.jpg) The patches adopted in Linux 2.6.30 introduce many significant changes affecting data security and Ext3 and Ext4 performance. Support for the EXOFS and NILFS2 file systems is new, as is the cache for the AFS and NFS network file systems. There are also a few fixes for the almost forgotten ReiserFS file system.

Released mid-week, as is normal for the second phase of the development cycle, the [third pre-release version](http://thread.gmane.org/gmane.linux.kernel/825801) of Linux 2.6.30 included mostly minor enhancements and fixes, although there were two code restructures.

The [interminable discussions](http://thread.gmane.org/gmane.linux.kernel/811167/) of the Ext3 and Ext4 file systems and the way they interact with other kernel subsystems have largely subsided. The H Open has [reported](../site/news/item/Kernel-developers-squabble-over-Ext3-and-Ext4-740787.html "Kernel developers squabble over Ext3 and Ext4 – 26 March 2009, 14:01") on the early stages of these discussions – the occasionally abrasive discussion on the LKML (Linux Kernel Mailing List) continued for a further week, with a total of [650 emails](http://thread.gmane.org/gmane.linux.kernel/811167/), not counting other threads triggered by the discussion.

The debate has been far from fruitless and has led to the development of various modifications which Torvalds has integrated, in some cases immediately, into the main development tree leading to Linux 2.6.30. This part of the "What's coming in 2.6.30" Kernel Log series gives an overview of these and many other changes to the code for the various file systems supported by Linux.

**Access time**

At a relatively early stage of the above discussion, an old, previously much discussed issue affecting all file systems once more reared its head – when and how frequently should the kernel update a file's atime (last access time)? This information is of importance to only a handful of applications and each update of the atime requires a write process. This not only has a time overhead, it is also somewhat surplus to requirements for SSDs and laptops running on battery.

Spurred on by this, Matthew Garrett has produced a number of patches which result in the kernel now updating last access time [just once a day](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=11ff6f05f1e836a6a02369a4c4b64757e484adc1) (Relative atime/relatime). It took Linus Torvalds just a few hours to make this one of the first patches to be incorporated into the main development tree following the release of 2.6.29. A further patch from Garrett makes relatime [the default](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d0adde574b8487ef30f69e2d08bba769e4be513f). The old style behaviour can be restored using [strictatime](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0a1c01c9477602ee8b44548a9405b2c1d587b5a2).

But even these changes, which many kernel hackers have long been calling for, did not satisfy everyone – Valerie Aurora (formally Henson) has listed various criticisms [on her blog](http://valhenson.livejournal.com/36519.html). Expect this one to run and run.

**Latencies**

A user reporting long latencies when applications use fsync() to flush the Ext3 write buffer when the kernel is working through large read processes prompted a discussion on LKML. The problem has been known about for several months, but the available workarounds were somewhat controversial.

Ext\[2/3/4\] file system developer Ted Ts'o put the blame squarely on application developers who, he opined, could save the file system a deal of work with a little more prudence. Other kernel developers disagreed. Ts'o has, however, already developed a number of less controversial [patches for Ext3 and Ext4](http://thread.gmane.org/gmane.comp.file-systems.ext4/12492) which, according to his measurements, reduce latency and which have subsequently been incorporated into 2.6.30.

Subsequent tests by Torvalds, however, determined that some of the blame for latencies must be placed on the block layer's CFQ scheduler. Jens Axboe analysed the problem and quickly developed more changes which further reduce latencies. This will in some cases increase the speed of desktop systems not just measurably, but tangibly.

**Latency II**

|  |
|----|
| **Debate and details** This article only describes the most critical points and outcomes of the discussions on Ext3 and Ext4 mentioned above and their interaction with other kernel subsystems such as the block layer. Linux Weekly News (LWN.net) has taken a more detailed look at the discussion and the changes arising from it in the articles *[That massive filesystem thread](http://lwn.net/Articles/326471/)* and *[Solving the ext3 latency problem](http://lwn.net/Articles/328363/)*. The articles "Linux Storage and Filesystem workshop" [Day 1](http://lwn.net/Articles/327601/) and [Day 2](http://lwn.net/Articles/327740/) also in part explore the issues discussed. The article *[ext4 and data loss](http://lwn.net/Articles/322823/)* looks at the problem of potential data loss in Ext4. |

Another major factor in the problem of latencies is Ext3's habit of loading the file system as 'data=ordered' by default. Ted Ts'o has [even publicly repented](http://thread.gmane.org/gmane.linux.kernel/814249) of having taken the decision to make this mode the default several years ago.

Though it initially looked as if the debate would be fruitless, Torvalds adopted some of Ts'o's patches a few days later. [These included one patch](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bbae8bcc49bc4d002221dab52c79a50a82e7cd1f) through which the kernel loads the Ext3 file system with 'data=writeback' unless the user explicitly states otherwise during kernel configuration or mounting. This should improve performance, but increases the risk of data loss in the event of a crash or if the computer is turned off without shutting down. There is also a risk that data from previously deleted files belonging to other users could find its way into new files incompletely written to disk before a crash.

The 'data=guarded' [mode developed](http://thread.gmane.org/gmane.comp.file-systems.ext4/12696) by chief Btrfs developer Chris Mason should resolve some of these problems. Two of the enhancements coded as part of this development have already been incorporated into the main development tree. The rest have been put on hold, with the development cycle already entering the stabilisation phase.

**Data security**

In the tumult of the discussion, the [risk of data loss](../site/news/item/Possible-data-loss-in-Ext4-740467.html "Possible data loss in Ext4 – 11 March 2009, 11:01") in Ext4 as a result of delayed allocation once more reared its ugly head. This risk should be significantly reduced by a number of patches for the Ext4 code which have now, [as planned](../site/news/item/Kernel-Log-Tasmanian-devil-to-be-Linux-s-temporary-mascot-new-Radeon-drivers-740667.html "Kernel Log: Tasmanian devil to be Linux's temporary mascot, new Radeon drivers – 19 March 2009, 15:43"), made their way into the main development tree. The changes do, however, have a negative effect on performance in certain situations.

The discussion on the risk of data loss led to a debate on precisely what guarantees a file system should be offering anyway. This led to the question of whether and how kernel and file systems should ensure that data does not just end up in a disk's write cache, but actually gets written in the correct sequence. This and other performance tuning questions led to a further discussion on where the role of the kernel developers in configuration stops and where fine tuning issues are better left to the Linux distributors.

**Two new file systems**

Following the adoption of [Btrfs and SquashFS](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-5-Filesystems-Btrfs-SquashFS-Ext4-without-journaling-740499.html "Kernel Log: What's new in 2.6.29 - Part 5: Filesystems Btrfs, SquashFS, Ext4 without journaling – 12 March 2009, 15:13") in [Linux 2.6.29](../site/open/features/Steady-growth-What-s-new-in-Linux-2-6-29-746553.html "Steady growth - What's new in Linux 2.6.29 – 24 March 2009, 15:26"), the kernel development team have once more integrated two new file systems into 2.6.30 in the form of NILFS and EXOFS.

[NILFS2](http://www.nilfs.org) (New Implementation of a Log-structured Filesystem Version 2) is a log-structured file system (LFS) with continuous snapshotting optimised for the needs of solid state discs (SSD). A detailed description of how it works can be found on the [NILFS2 website](http://www.nilfs.org/) and in the [kernel documentation on NILFS2](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob;f=Documentation/filesystems/nilfs2.txt;hb=HEAD). Further details can be found in a [presentation](http://www.usenix.org/event/lsf08/tech/shin_SSD.pdf)![PDF](../site/icons/file-pdf.gif "PDF document") given as part of the Linux Storage & File system Workshop 2008 (LSF'08) in February, which includes a comparison between NILFS2 and Btrfs, Ext2 through 4, ReiserFS and XFS when running with an SSD. The presentation by Dongjun Shin, which is already somewhat long in the tooth, also takes a close look at some of the particularities of file systems for SSDs.

EXOFS stands for Extended Object File System and used to be known as OSDFS (Object-Based Storage Devices File System). As the old name suggest, it is intended for the somewhat exotic OSDs ([object-based storage devices](http://en.wikipedia.org/wiki/Object_storage_device)), which will be supported by the SCSI subsystem for the first time in 2.6.30. Users wanting further information on this kind of storage and the file system can find details in an [article on OSDs by Sun](http://developers.sun.com/solaris/articles/osd.html), the [kernel documentation on EXOFS](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob;f=Documentation/filesystems/exofs.txt;hb=HEAD), the [EXOFS developer website](http://www.open-osd.org/) and an [LWN.net article on EXOFS/OSDFS](http://lwn.net/Articles/305740/).

**Cache for the network, infusion for Btrfs**

After [several years](http://lwn.net/Articles/100321/) of development, the kernel development team have now adopted the FS-Cache patch developed primarily by Red Hat developer David Howells ([kernel documentation](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob;f=Documentation/filesystems/caching/fscache.txt;hb=HEAD)). This extension allows a file system cache to be set up to reduce network traffic when using network file systems such as AFS and NFS. This is, for instance, of interest for thin clients with no hard drive or flash media which obtain their root file system and all other data over a network.

The Btrfs development team have also been busy and have enhanced the file system code to [cope](http://thread.gmane.org/gmane.linux.kernel/815305) better with 4k stacks – further improvements along these lines remain on the to-do list. [There are also](http://thread.gmane.org/gmane.linux.kernel/815305/focus%3D817368) enhancements to improve write performance in general and for SSDs.

**ReiserFS - forgotten but not gone**

The kernel's ReiserFS code is [still officially supported](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob;f=MAINTAINERS;h=cb9571042f216e24bcea891358623dd99e93e9aa;hb=HEAD#l4710), but has long been without an official maintainer. Consequently, in recent months there have been only minor changes to ensure that the once popular file system keeps working.

Novell developer Jeff Mahoney has now added [various](http://thread.gmane.org/gmane.comp.file-systems.reiserfs.general/22106) patches developed as part of SLED/SLES, some of which are already more than two years old. They should resolve irregularities or bugs in ReiserFS, (also referred to as Reiser3). According to Mahoney's Git pull request, after incorporation of these patches ReiserFS should be considered to be in "deep maintenance-only mode". As part of the discussions on Git pull requests, Frederic Weisbecker indicated that he is [working on changes](http://thread.gmane.org/gmane.comp.file-systems.reiserfs.general/22106/focus%3D22130) to reduce the use of the Big Kernel Lock (BKL) in ReiserFS.

**Minor gems**

The kernel development team have extended DFS support in CIFS to support [access to remote servers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1bfe73c258addc388b90fe8c2c6bbc0f0c9c10dd).

The changes described are just some of the more significant changes recently undertaken by kernel hackers on the code for the various file systems. Numerous further major changes can be found from the list of commit headers from the main development tree below. The links take you directly to the changes in the main development tree [web interface](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=summary), where the commit comments and the patches themselves provide further information on these, perhaps less major, but in no way insignificant changes.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the Kernel Log at The H Open Source:*

- [Kernel Log: 3D support for the new Radeon driver; new Intel drivers](../site/news/item/Kernel-Log-3D-support-for-the-new-Radeon-driver-new-Intel-drivers-741271.html " Kernel Log: 3D support for the new Radeon driver; new Intel drivers – 22 April 2009, 17:06")
- [Kernel Log: What's coming in 2.6.30 - Network: New Wi-Fi drivers and other network novelties](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-Network-New-Wi-Fi-drivers-and-other-network-novelties-741197.html "Kernel Log: What's coming in 2.6.30 - Network: New Wi-Fi drivers and other network novelties – 17 April 2009, 10:51")
- [Kernel Log: Linux 2.6.30 is taking shape](../site/news/item/Kernel-Log-Linux-2-6-30-is-taking-shape-741093.html "Kernel Log: Linux 2.6.30 is taking shape – 09 April 2009, 06:41")
- [Kernel Log: Development of 2.6.30 is under way](../site/news/item/Kernel-Log-Development-of-2-6-30-is-under-way-740805.html "Kernel Log: Development of 2.6.30 is under way – 27 March 2009, 17:33")
- [Steady Growth: What's new in Linux 2.6.29](../site/open/features/Steady-growth-What-s-new-in-Linux-2-6-29-746553.html "Steady growth - What's new in Linux 2.6.29 – 24 March 2009, 15:26")
- [Kernel Log: Tasmanian devil to be Linux's temporary mascot, new Radeon drivers](../site/news/item/Kernel-Log-Tasmanian-devil-to-be-Linux-s-temporary-mascot-new-Radeon-drivers-740667.html "Kernel Log: Tasmanian devil to be Linux's temporary mascot, new Radeon drivers – 19 March 2009, 15:43")

*Older Kernel Logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/).*

([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

**File systems:**

*Relevant Git-Pull-Requests*

- Btrfs: [1](http://thread.gmane.org/gmane.linux.kernel/815305), [2](http://thread.gmane.org/gmane.linux.kernel/815305/focus%3D817368), [3](http://news.gmane.org/find-root.php?message_id=1240320545.4869.22.camel@think.oraclecorp.com)
- Ext3 und Ext4: [1](http://thread.gmane.org/gmane.comp.file-systems.ext4/12453), [2](http://thread.gmane.org/gmane.comp.file-systems.ext4/12492),[3](http://thread.gmane.org/gmane.comp.file-systems.ext4/12492/focus%3D12632)
- FS-Cache: [1](http://news.gmane.org/find-root.php?message_id=20090403155436.28714.23368.stgit@warthog.procyon.org.uk), [2](http://news.gmane.org/find-root.php?message_id=29650.1238774351@redhat.com)
- GFS2: [1](http://thread.gmane.org/gmane.linux.cluster.redhat.cluster.devel/3505)
- NFS: [1](http://thread.gmane.org/gmane.linux.kernel/815231/focus%3D25600)
- OCFS2: [1](http://thread.gmane.org/gmane.comp.file-systems.ocfs2.devel/3561)
- Quota: [1](http://thread.gmane.org/gmane.linux.kernel/812667)
- UBIFS: [1](http://article.gmane.org/gmane.linux.kernel/815045)
- VFS: [1](http://thread.gmane.org/gmane.linux.kernel/813625), [2](http://thread.gmane.org/gmane.linux.kernel/816876)
- XFS: [1](http://thread.gmane.org/gmane.comp.file-systems.xfs.general/28747)

*Btrfs*

- [Btrfs: add a priority queue to the async thread helpers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d313d7a31a752c88f7288692bd98e66d0789779b)
- [Btrfs: add extra flushing for renames and truncates](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5a3f23d515a2ebf0c750db80579ca57b28cbce6d)
- [Btrfs: add flushoncommit mount option](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=dccae99995089641fbac452ebc7f0cab18751ddb)
- [Btrfs: do extent allocation and reference count updates in the background](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=56bec294dea971335d4466b30f2d959f28f6e36d)
- [Btrfs: notreelog mount option](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3a5e14048a0a81276d284cbda441507a17e26147)
- [Btrfs: Optimize locking in btrfs_next_leaf()](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8e73f275011b3264a87339fd9f1690e944e381c9)
- [Btrfs: rework allocation clustering](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fa9c0d795f7b57c76560b7fac703f5d341210e28)
- [Btrfs: stop spinning on mutex_trylock and let the adaptive code spin for us](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cf47b8f3d96b0b8b10b557444a28b3ca4024ff82)
- [Btrfs: use WRITE_SYNC for synchronous writes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ffbd517d5a8c8e93ddd11046434fb029f3df73aa)

*FS-Cache*

- [CacheFiles: A cache that backs onto a mounted filesystem](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9ae326a69004dea8af2dae4fde58de27db700a8d)
- [CacheFiles: Export things for CacheFiles](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=800a964787faef3509d194fa33268628c3d1daa9)
- [CacheFiles: Permit the page lock state to be monitored](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=385e1ca5f21c4680ad6a46a3aa2ea8af99e99c92)
- [Create a dynamically sized pool of threads for doing very slow work items](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=07fe7cb7c7c179f473fd9c823348fd3eb5dad369)
- [Document the slow work thread pool](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8f0aa2f25b31ba27db84259141e52ee6ec0d2820)
- [FS-Cache: Add and document asynchronous operation handling](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=952efe7b7840e1c726ae88222245e4efe6bd88f3)
- [FS-Cache: Add cache management](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4c515dd47ab41be3f89e757d441661795470b376)
- [FS-Cache: Add cache tag handling](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0e04d4cefcf4d8fbbdb2c50e93ad541582933fd2)
- [FS-Cache: Add main configuration option, module entry points and debugging](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=06b3db1b9bccdc8c2c743122a89745279e5ecc46)
- [FS-Cache: Add netfs registration](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=726dd7ff10c217dd74329c94643dc8ebea27334b)
- [FS-Cache: Add the FS-Cache cache backend API and documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0dfc41d1efcc4180abfd32f68f0ade540e636ff6)
- [FS-Cache: Add the FS-Cache netfs API and documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2d6fff637037395cc946ef910a880b5fa67b5370)
- [FS-Cache: Add use of /proc and presentation of statistics](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7394daa8c61dfda4baa687f133748fa0b599b017)
- [FS-Cache: Bit waiting helpers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2868cbea72dc89ae0eb17693596b1dedaafff1c5)
- [FS-Cache: Implement data I/O part of netfs API](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b510882281d56873e1194021643b7c325336f84f)
- [FS-Cache: Implement the cookie management part of the netfs API](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ccc4fc3d11e91477036d1f82bfa2d442f6ce77f0)
- [FS-Cache: Make kAFS use FS-Cache](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9b3f26c9110dcea62716aca9b8c68ceb482227ef)
- [FS-Cache: Object management state machine](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=36c9559022850f919269564a74bf17fdabf4bb30)
- [FS-Cache: Provide a slab for cookie allocation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=955d00917f0c094e0f2fb88df967e980ab66b8ca)
- [FS-Cache: Recruit a page flags for cache management](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=266cf658efcf6ac33541a46740f74f50c79d2b6b)
- [FS-Cache: Release page-\>private after failed readahead](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=03fb3d2af96c2783c3a5bc03f3d984cf422f0e69)
- [FS-Cache: Root index definition](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a6891645cf2ddd4778096848a864580e7258faba)
- [Make slow-work thread pool actually dynamic](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=109d9272c423f46604d45fedfe87e21ee0b25180)
- [Make the slow work pool configurable](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=12e22c5e4bc08ab4b05ac079fe40d9891c5e81a0)
- [NFS: Add comment banners to some NFS functions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6b9b3514aa188183e74049853be43380ad49314f)
- [NFS: Add FS-Cache option bit and debug bit](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c6a6f19e22da0a3d74214ee010224c9a30a794c1)
- [NFS: Add mount options to enable local caching on NFS](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b797cac7487dee6bfddeb161631c1bbc54fa3cdb)
- [NFS: Add read context retention for FS-Cache to call back with](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1fcdf534885b65e6d39780a5a89e9dfc5431cf68)
- [NFS: Add some new I/O counters for FS-Cache doing things for NFS](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6a51091d0775cdc4a923f2172c61925ad416aa32)
- [NFS: Define and create inode-level cache objects](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=10329a5d48f5abc14a37d30b706e330f8598297a)
- [NFS: Define and create server-level objects](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=147272813e043fb44bd112527951da70c1e663de)
- [NFS: Define and create superblock-level objects](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=08734048b380103f0412f58b84c2f76a2c8b599f)
- [NFS: Display local caching state](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5d1acff159730770cbab68b19443518c92ab1000)
- [NFS: FS-Cache page management](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=545db45f0fc0d4203b045047798ce156972a3056)
- [NFS: Invalidate FsCache page flags when cache removed](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d599064a1bca7bcbaabe54b94fa73ea86952cae3)
- [NFS: nfs_readpage_async() needs to be accessible as a fallback for local caching](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f42b293d6d5259043a8944b556eeab427c695d57)
- [NFS: Permit local filesystem caching to be enabled for NFS](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3b9ce977b2f31b6c396b6fb620df9881a30fac9d)
- [NFS: Read pages from FS-Cache into an NFS inode](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9a9fc1c03315f1606596e55b4096d39e2079a041)
- [NFS: Register NFS for caching and retrieve the top-level index](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8ec442ae4c6577ed181682e534d4eef524e30b3c)
- [NFS: Store pages from an NFS inode into a local cache](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7f8e05f60c87646e12c761fef61dd71a7e67112e)
- [NFS: Use local disk inode cache](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ef79c097bbe9724e13937271b3457df560e00370)

*EXOFS*

- [exofs: address_space_operations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=beaec07ba6af35d387643b76a2920a7a6e22207b)
- [exofs: dir_inode and directory operations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e6af00f1d1697ca41ab6a55307066ef3466833a9)
- [exofs: Documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=214c8adb87b880690b103e86baffc46f8288fa62)
- [exofs: export_operations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8cf74b3936f5c65975b68333727f0540ec8350f4)
- [exofs: file and file_inode operations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e806271916ed6068a0e3e4e9298dff0688b88e0d)
- [exofs: Kbuild, Headers and osd utils](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b14f8ab2844987f013253dd04b708bde7fc1b52d)
- [exofs: super_operations and file_system_type](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ba9e5e98ca2f808fe92b103a8e6ce5271b10cc89)
- [exofs: symlink_inode and fast_symlink_inode operations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=982980d753223fda3864038236b7b94e246895cb)
- [fs: Add exofs to Kernel build](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0d8fe329a80714e0f729ae48cba8d64cbe5701cb)

*Ext\[2/3/4\]*

- [ext3: Add replace-on-rename hueristics for data=writeback mode](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e7c8f5079ed9ec9e6eb1abe3defc5fb4ebfdf1cb)
- [ext3: Add replace-on-truncate hueristics for data=writeback mode](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f7ab34ea723ed304b19698efca85d6f40cecd99b)
- [ext3: Avoid starting a transaction in writepage when not necessary](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9e80d407736161d9b8b0c5a0d44f786e44c322ea)
- [ext3: make default data ordering mode configurable](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bbae8bcc49bc4d002221dab52c79a50a82e7cd1f)
- [ext3: Try to avoid starting a transaction in writepage for data=writepage](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=430db323fae7665da721768949ade6304811c648)
- [ext4: add EXT4_IOC_ALLOC_DA_BLKS ioctl](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ccd2506bd43113659aa904d5bea5d1300605e2a6)
- [ext4: Add fine print for the 32000 subdirectory limit](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=722bde6875bfb49a0c84e5601eb82dd7ac02d27c)
- [ext4: Add sysfs support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3197ebdb130473a92760100cbfe0d7e671838f48)
- [ext4: Automatically allocate delay allocated blocks on close](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7d8f9f7d150dded7b68e61ca6403a1f166fb4edf)
- [ext4: Automatically allocate delay allocated blocks on rename](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8750c6d5fcbd3342b3d908d157f81d345c5325a7)
- [ext4: Fix discard of inode prealloc space with delayed allocation.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d6014301b5599fba395c42a1e96a7fe86f7d0b2d)
- [ext4: Regularize mount options](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=06705bff9114531a997a7d0c2520bea0f2927410)
- [ext4: remove /proc tuning knobs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b713a5ec55bf73c833f9883cdd761b20ee61a1ab)
- [ext4: Track lifetime disk writes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=afc32f7ee9febc020c73da61402351d4c90437f3)
- [trivial: document ext3 semantics of 'ro' option a bit better](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e3375ac767b847127df57d186a26abf83d055982)

*NILFS2*

- [Nilfs2: add document](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=962281a7ab3aeb97eed004b8f0bdb0979cf35347)
- [Nilfs2: add inode and other major structures](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=65b4643d3babeb203fa9571d12fd5e1bf74d27b0)
- [Nilfs2: add maintainer](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=85ef9cea02882baedd1e65336cf3dd292841dde3)
- [Nilfs2: another dat for garbage collection](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=84ef1ecfdea2f9f1e740a4bee0fa9cd629bdda70)
- [Nilfs2: avoid double error caused by nilfs_transaction_end](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=47420c799830d4676e544dbec56b2a7f787528f5)
- [Nilfs2: block cache for garbage collection](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a3d93f709e893187d301aa5458b2248db9f22bd1)
- [Nilfs2: B-tree based block mapping](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=17c76b0104e4a6513983777e1a17e0297a12b0c4)
- [Nilfs2: B-tree node cache](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a60be987d45dd510aeb54389526f9957cfab106c)
- [Nilfs2: buffer and page operations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0bd49f9446130a6a3914eb07b54db489e3222b34)
- [Nilfs2: checkpoint file](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=29619809727a4e524e26dbd7bfdc93ff7f50aa74)
- [Nilfs2: clean up indirect function calling conventions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8acfbf0939e98cc77dab94c24899c9930ddd1e13)
- [Nilfs2: cleanup nilfs_clear_inode](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a2e7d2df82cafb76f76809ddf6e2caa8afe4f75e)
- [Nilfs2: clean up sketch file](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=458c5b0822a669d170fdb7bb16c9145f652ebe06)
- [Nilfs2: direct block mapping](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=36a580eb489f54d81a0534974962e732a314b999)
- [Nilfs2: directory entry operations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2ba466d74ed74f073257f86e61519cb8f8f46184)
- [Nilfs2: disk address translator](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a17564f58b11476c011d623fa1f268602a81c27c)
- [Nilfs2: disk format and userland interface](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=eed10e39b142eb4d284c8e4c751c0eaaa0bcd707)
- [Nilfs2: extend nilfs_sustat ioctl struct](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2c2e52fc4fca251e68f90821c9ff5cb18be4df58)
- [Nilfs2: file operations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f183ff4f05317b7929337455b233496f68217c1a)
- [Nilfs2: fix buggy behavior seen in enumerating checkpoints](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=76068c4ff1cc03d9d24d17fd9e6a1475bc2f6730)
- [Nilfs2: fix gc failure on volumes keeping numerous snapshots](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b028fcfc4cd198a6aa1ffcfb872073ccc1db3459)
- [Nilfs2: fix improper return values of nilfs_get_cpinfo ioctl](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7fa10d20012296300dfe645cb3e628a4e9a0d5ef)
- [Nilfs2: fix missed-sync issue for do_sync_mapping_range()](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f30bf3e40f80ef50c17f55271deae3abc03e793e)
- [Nilfs2: fix problems of memory allocation in ioctl](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3358b4aaa84fd4c1cdd64391875e92cbb8afeb29)
- [Nilfs2: inode map file](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=43bfb45ed4feace26157778889be55e4046b7a4b)
- [Nilfs2: inode operations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=05fe58fdc10df9ebea04c0eaed57adc47af5c184)
- [Nilfs2: insert explanations in gcinode file](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=047180f2d7bf95ff5699ca04da639a7556e23435)
- [Nilfs2: integrated block mapping](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bdb265eae08db578e7cf5739be16f389d495fc75)
- [Nilfs2: introduce secondary super block](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e339ad31f59925b48a92ee3947692fdf9758b8c7)
- [Nilfs2: ioctl operations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7942b919f7321f95a777d396ff7894a7a83dc9b0)
- [Nilfs2: mark minor flag for checkpoint created by internal operation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c96fa464a567a2a8796009af0e79bc68af73f485)
- [Nilfs2: meta data file](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5eb563f5f299a2ed488d9eb52acede45ccb14c7b)
- [Nilfs2: operations for the_nilfs core object](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8a9d2191e9f43bbcd256a9a6871bd73434c83f2f)
- [Nilfs2: pathname operations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d25006523d0b9e49fd097b2e974e7c8c05bd7f54)
- [Nilfs2: persistent object allocator](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5442680fd23abc01f29af585cc1a2f793bd74565)
- [Nilfs2: recovery functions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0f3e1c7f23f8a6f8224fa1d275381f6d9279ad4b)
- [Nilfs2: remove compat ioctl code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8082d36aed26c4fb6ed43e4008303682eabf839e)
- [Nilfs2: remove timedwait ioctl command](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1088dcf4c3a0a27fdad5214781d5084b11405238)
- [Nilfs2: replace BUG_ON and BUG calls triggerable from ioctl](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1f5abe7e7dbcd83e73212c6cb135a6106cea6a0b)
- [Nilfs2: segment buffer](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=64b5a32e0b3680a9655b3f2e668a646068e71d33)
- [Nilfs2: segment constructor](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9ff05123e3bfbb1d2b68ba1d9bf1f7d1dffc1453)
- [Nilfs2: segment usage file](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6c98cd4ecb0ae35f0368c5c2190712689c2064aa)
- [Nilfs2: simplify handling of active state of segments](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cece552074c591970353ad48308d65f110aeaf28)
- [Nilfs2: super block operations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=783f61843e9d14724f5f79ae955a28c27e300467)
- [Nilfs2: super block operations fix endian bug](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e62687468588f47c32256e3c8c36157c40111b6e)
- [Nilfs2: support nanosecond timestamp](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=612392307cb09e49051225092cbbd7049bd8db93)
- [Nilfs2: update makefile and Kconfig](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0c4fb877641c5c72d4a3ce8921a256bfe44055c0)
- [Nilfs2: use fixed sized types for ioctl structures](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=dc498d09be28172846cacded35ca2378222a8c7b)
- [Nilfs2: use unlocked_ioctl](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7a9461939a46345860622ea36ff267ee4446f00f)

*Various*

- [CIFS: Add support for posix open during lookup](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a6ce4932fbdbcd8f8e8c6df76812014351c32892)
- [Documentation/filesystems: remove out of date reference to BKL being held](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=66672fefaa91802fec51c3fe0cc55bc9baea5a2d)
- [documentation: update Documentation/filesystem/proc.txt and Documentation/sysctls](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=760df93ecdd59fc1c213a491b5adee79f53606da)
- [Document /proc/fs/nfsd/pool_stats](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b5cbc369db39d9080f4932db8607aea1e1654d4d)
- [filesystem freeze: allow SysRq emergency thaw to thaw frozen filesystems](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c2d7543851849a6923680cdd7e1047ed1a84a1c5)
- [GFS2: Merge lock_dlm module into GFS2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f057f6cdf64175db1151b1f5d110e29904f119a1)
- [nfs41: common protocol definitions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=18df1884a872a2cc405a578cfd0d3adc8d227277)
- [nfsd41: control nfsv4.1 svc via /proc/fs/nfsd/versions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8daf220a6a83c47b9648c28bb819c14c60bad7f9)
- [nfsd41: Documentation/filesystems/nfs41-server.txt](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3ef1728898f0285c13aa6901f412b52835e23578)
- [ocfs2: Add a name indexed b-tree to directory inodes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9b7895efac906d66d19856194e1ba61f37e231a4)
- [ocfs2: Introduce dir free space list](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e7c17e43090afe558c40bfb66637744c27bd2aeb)
- [ocfs2: Introduce dir lookup helper struct](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4a12ca3a00a244e1fd1e673d151ea38b71e11d55)
- [ocfs2: Store dir index records inline](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4ed8a6bb083bfcc21f1ed66a474b03c0386e4b34)
- [quota: Add quota reservation support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f18df228997fb716990590d248663981a15f17d4)
- [ramfs: add support for "mode=" mount option](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c3b1b1cbf002e65a3cabd479e68b5f35886a26db)
- [reiserfs: rework reiserfs_panic](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c3a9c2109f84882b9b3178f6b1838d550d3df0ec)
- [reiserfs: rework reiserfs_warning](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=45b03d5e8e674eb6555b767e1c8eb40b671ff892)
- [reiserfs: use generic readdir for operations across all xattrs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a41f1a4715f26f7bc4d047d0bc7710145c8e69c7)
- [UBIFS: add R/O compatibility](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=963f0cf6d116d83c558a8efe9045c1c5ad7aed34)
- [udf: implement mode and dmode mounting options](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7ac9bcd5da59dd96eb1153d3fc04c3471fa5c09d)
- [vfat: Note the NLS requirement](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d29a2e943867bfa48f72ee6e99723a1b29fe6f7e)
- [xfs: Update maintainers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b58a4cc51f4f569c6a86979890f9b237a504ab6b)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
