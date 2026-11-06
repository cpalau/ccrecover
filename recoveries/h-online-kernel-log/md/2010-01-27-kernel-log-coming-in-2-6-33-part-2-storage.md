---
title: "Kernel Log: Coming in 2.6.33 (Part 2) - Storage"
date: 2010-01-27
author: "Chris von Eitzen"
source: http://www.h-online.com/open/news/item/Kernel-Log-Coming-in-2-6-33-Part-2-Storage-914669.html
pages: 1
---

# Kernel Log: Coming in 2.6.33 (Part 2) - Storage

**Chris von Eitzen**

#### ![Kernel Log](../site/imgs/43/4/7/3/2/2/1/KL.jpg-1f663d67fe8a53b0.jpeg) by Thorsten Leemhuis

**Extended discard support means that Linux now supports ATA TRIM, which can increase SSD lifespan and throughput. New additions to the Linux kernel include HA solution DRBD and drivers for HP, LSI and VMware storage hardware. The new kernel version, expected in early March, also includes many minor improvements to the code for the Btrfs, Ext4 and ReiserFS file systems.**

At the end of last week, Linus Torvalds [released](http://thread.gmane.org/gmane.linux.kernel/941205) the fifth pre-release version of Linux version 2.6.33, with the final release expected in 4 to 5 weeks time. At this stage in the development cycle, it is usually predominantly more minor changes and fixes which find their way into the main development tree. Kernel hackers do, however, make occasional exceptions for drivers. Linux 2.6.33-rc5 sees the addition to the kernel of a V4L/DVB driver which supports the Mantis chip-set used in a range of TV cards. However, the changes to the V4L/DVB subsystem in Linux 2.6.33 are the subject of a future article in the "Coming in 2.6.33" series.

Following on from the first article in the 2.6.33 series, which looked at [networking changes](../site/news/item/Kernel-Log-Coming-in-2-6-33-Part-1-Networking-898841.html "Kernel Log: Coming in 2.6.33 (Part 1) - Networking – 08 January 2010, 11:01"), this article examines file systems changes and changes to the kernel's storage subsystem.

### Trimming

For several months, some sections of the kernel have included a rudimentary discard infrastructure, which allows drivers for mass storage adaptors to determine whether storage areas on a disk are free – as a result, for example, of deleting a file or formatting a partition. This has been revised and extended in 2.6.33. The result is that the Libata subsystem now also [supports](http://git.kernel.org/linus/18f0f97850059303ed73b1f02084f55ca330a80c) discards and can forward information on free storage areas to mass storage devices using the ATA TRIM command. This is especially useful for SSDs ([Solid State Drives](http://en.wikipedia.org/wiki/Solid-state_drive)), as sending the internal controller information on free storage areas, allows the controller to optimise internal garbage collector. This increases both SSD performance and SSD lifespan.

For the discard infrastructure to achieve maximum impact, the storage subsystem needs to send the free area information to other parts of the kernel. The [Btrfs file system](../site/open/features/The-Btrfs-file-system-746597.html "The Btrfs file system – 17 July 2009, 08:55") has been able to do this since [Linux 2.6.32](../site/open/features/What-s-new-in-Linux-2-6-32-872271.html "What's new in Linux 2.6.32 – 03 December 2009, 08:22") and [appropriate](http://git.kernel.org/linus/5328e635315734d42080de9a5a1ee87bf4cae0a4) code has also now been added for [Ext4](../site/open/features/The-Ext4-Linux-file-system-746579.html "The Ext4 Linux file system – 29 May 2009, 08:13"). Since this has not yet been fully tested, this function will for now remain deactivated by default. [The new discard support](http://git.kernel.org/linus/681142f9211b23e6aa2984259d38b76d7bdc05a8) in the code for the FAT file system is also optional.

### Replicated

After leaving DRBD (Distributed Replicated Block Device), largely developed by Vienna-based company [Linbit](http://www.linbit.com/), [out in the cold](../site/news/item/Kernel-Log-Main-development-phase-of-Linux-2-6-32-completed-812328.html "Kernel Log - Main development phase of Linux 2.6.32 completed – 28 September 2009, 15:46") in 2.6.32, kernel hackers have finally [merged](http://git.kernel.org/linus/b411b3637fa71fce9cf2acf0639009500f5892fe) the replication solution, used predominantly in high availability environments, into Linux 2.6.33. DRBD can be roughly understood as a network-based RAID 1 device. The drive or drives on one system, designated as the master, are mirrored on a slave system, in real time. Should the master fail, the slave takes over with no downtime. In order to ensure that data remains synchronised at all times, the master considers write access to be complete only when the slave has also completed the write. A detailed explanation of DRBD can be found a [LWN.net article](http://lwn.net/Articles/329543/) and in documentation on the [DRBD website](http://www.drbd.org/).

Over recent months and years, a number of groups have worked on solutions for limiting the maximum amount of data which individual processes or groups of processes can write to or read from drives. These solutions affect various points within the kernel. The 'blkio controller cgroup interface' (blkio for short), which links into the CFQ (Completely Fair Queuing) I/O Scheduler, has [come out with its nose in front](http://git.kernel.org/linus/31e4c28d95e64f2d5d3c497a3ecf37c62de635b4). This does not represent the failure of other approaches, however, rather it is intended to offer a foundation for further enhancements and functions made possible by some of the competing solutions. Background information on this topic can be found in [a LWN.net article](http://lwn.net/Articles/360958/) and in the [documentation](http://git.kernel.org/linus/72f924f62a6eb375c7c237ecc911f95be0531d1a) for the blkio framework.

### Optimised

Developers have [removed](http://git.kernel.org/linus/492af6350a5ccf087e4964104a276ed358811458) the anticipatory I/O scheduler (AS), which, according to the commit comments, offers only a subset of the functions offered by the CFQ scheduler. The latter, which has long been the standard in many distributions, is now also [described](http://git.kernel.org/linus/08dc8726d4be85bca793141c827574fd32a681bb) as being suitable for desktop and server environments. Like the process scheduler, almost every Linux version contains numerous changes optimising the CFQ I/O scheduler for specific application scenarios. Details can be found in the links in the 'Minor gems' section at the end of this article and in the [main git pull request](http://thread.gmane.org/gmane.linux.kernel/923097) from block subsystem maintainer Jens Axboe.

Improvements have been made to the code for migrating software RAIDs managed using mdadm to a different level. The MD subsystem [now also supports](http://git.kernel.org/linus/a2826aa92e2e14db372eda01d333267258944033) write barriers. These ensure that data and file system journals are written in the sequence expected by other parts of the kernel. This should ensure better file system integrity in the event of a crash, but can palpably reduce throughput, as MD maintainer Neil Brown [notes](http://thread.gmane.org/gmane.linux.raid/25760) in his main git pull request. Support for write barriers in the device mapper (DM) has also been [extended](http://git.kernel.org/linus/10b8106a70433e14153469ebbdd189776500e238) ([git pull request](http://thread.gmane.org/gmane.linux.kernel.device-mapper.devel/10759)). This now offers a 'merge target' (e. g. [1](http://git.kernel.org/linus/1e03f97e4301f75a2f3b649787f7876516764929), [2](http://git.kernel.org/linus/d698aa4500aa3ca9559142060caf0f79da998744)), which can restore systems to a previous snapshot following, for example, a problematic system update ([LWN.net article](http://lwn.net/Articles/363575)).

### Drivers

The IDE subsystem drivers are now [officially classed as deprecated](http://git.kernel.org/linus/73ba32320da60b2e872b4f7ba9b7d4fd1218e5b3). Users are advised to switch to the Libata subsystem PATA drivers, which have long been in the kernel and are no longer classed as experimental ([1](http://git.kernel.org/linus/097dac91837b35947fffb0e303bcf71e4e4a789f), [2](http://git.kernel.org/linus/be315d46156b3db3f4d7eddd1f85549a8a70e962)). In 2.6.33, these contain numerous minor enhancements and corrections, some originating from Bartlomiej Zolnierkiewicz, who, until a few months ago, maintained the IDE subsystem.

The SCSI subsystem contains two new drivers: [3w-sas](http://git.kernel.org/linus/f619106bdd9d197c947f07108af57946f19a7f7e) for the LSI 3ware 9750 and [vmw_pvscsi](http://git.kernel.org/linus/851b164231d1117673aa44c00c7622e48b7dfcf4) for the virtual hardware seen by guest systems under some VMware hypervisors. New smart array controllers from HP can now be addressed both by the block subsystem's cciss driver, which has seen various [enhancements](http://git.kernel.org/linus/5c07a311a80adb0138fc08e8279c60255d88d0b8) in 2.6.33, and by the new [hpsa](http://git.kernel.org/linus/edd163687ea59f01d6b43c9e1fdaa0126fa30191) driver. The latter, being part of the SCSI subsystem, like all other SCSI and Libata drivers provides a standard device (/dev/sd*x*) for access. Other new entries in this week's kernel include the [pm8001](http://git.kernel.org/linus/dbf9bfe615717d1145f263c0049fe2328e6ed395) driver for SAS/SATA HBAs containing the PMC Sierra SPC 8001 chip.

### Miscellaneous

A few further file system and storage code related changes:

- [According to](http://thread.gmane.org/gmane.linux.kernel/929400) main developer Chris Mason's main git pull request for 2.6.33, Btrfs, the experimental 'next generation file system for Linux'-elect, saw primarily minor enhancements and fixes in 2.6.33.
- Ext4, which is based on the Ext2 and Ext3 file system code, can [now](http://git.kernel.org/linus/24b584240a0006ea7436cd35f5e8983eb76f1e6f) mount Ext2 and Ext3 file systems. This allows environments which require the smallest possible kernel image to save a little space.
- Distributed file system [Ceph](http://ceph.newdream.net/) was [put forward](http://thread.gmane.org/gmane.linux.file-systems/37252) for merger into 2.6.33. Torvalds has, however, chosen to omit it for now, [explaining](http://thread.gmane.org/gmane.linux.file-systems/37252/focus%3D37411) that this was partly due to time constraints and partly because there was not enough noise from kernel developers and distributors in favour of it. Background information can be found in [this article on LWN.net](http://lwn.net/Articles/367787/).
- Although the ReiserFS code has long lacked an official maintainer, one developer has still taken the trouble to significantly [reduce](http://lkml.indiana.edu/hypermail/linux/kernel/0912.0/03048.html) use of the big kernel lock (BKL) in the ReiserFS code. This should make the file system more scalable and in some cases a little more fleet of foot.
- Some of the more important changes in nilfs2 are described in the [git pull request](http://thread.gmane.org/gmane.linux.kernel/926113) from nilfs2 maintainer Ryusuke Konishi.
- Virtual File System (VFS) now [correctly implements O_SYNC](http://git.kernel.org/linus/6b2f3d1f769be5779b479c37800229d9a4809fc3). Once again, further details can be [found on LWN.net](http://lwn.net/Articles/350219/).
- There has been major restructuring work on the XFS file system code to replace XFS' own tracing code with [code](http://git.kernel.org/linus/0b1b213fcf3a8486ada99a2bab84ab8c6f51b264) which uses the kernel's own tracing structure. This is itself relatively new, but has been developed substantially over the last year.

### Minor gems

Many further minor, but by no means insignificant, changes can be found in the list below, which contains the commit headers referring to the respective change. Like many of the references in the text above, the links point to the relevant commit in the [web front end](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git&a=summary) of the Git branch for the kernel sources maintained by Linus Torvalds at kernel.org. The commit comments and the patches themselves provide extensive further information on the respective changes.

**File systems**

*Btrfs*

- [Btrfs: Avoid superfluous tree-log writeout](http://git.kernel.org/linus/8cef4e160d74920ad1725f58c89fd75ec4c4ac38)
- [Btrfs: fail mount on bad mount options](http://git.kernel.org/linus/a7a3f7cadd9bdee569243f7ead9550aa16b60e07)
- [Btrfs: Make fallocate(2) more ENOSPC friendly](http://git.kernel.org/linus/5a303d5d4b8055d2e5a03e92d04745bfc5881a22)
- [Btrfs: make metadata chunks smaller](http://git.kernel.org/linus/83d3c9696fed237a3d96fce18299e2fcf112109f)
- [Btrfs: Make truncate(2) more ENOSPC friendly](http://git.kernel.org/linus/8082510e7124cc50d728f1b875639cb4e22312cc)
- [Btrfs: Show discard option in /proc/mounts](http://git.kernel.org/linus/20a5239a5d0f340e29827a6a2d28a138001c44b8)

*Ext\[234\]*

- [ext3: make "norecovery" an alias for "noload"](http://git.kernel.org/linus/dee1d3b6270a7cf5cc65c493a2ab4ebaad1a1caf)
- [ext3: Support for vfsv1 quota format](http://git.kernel.org/linus/1aeec43432d6bfb7a300bb0363f2723b8c4c706d)
- [ext3: Unify log messages in ext3](http://git.kernel.org/linus/4cf46b67eb6de94532c1bea11d2479d085229d0e)
- [ext4: add tracepoint for ext4_forget()](http://git.kernel.org/linus/beac2da7565e42be59963824899825d0cc624295)
- [ext4: Do not override ext2 or ext3 if built they are built as modules](http://git.kernel.org/linus/a214238d3bb03723f820b0a398928d8e1637c987)
- [ext4, jbd2: Add barriers for file systems with exernal journals](http://git.kernel.org/linus/cc3e1bea5d87635c519da657303690f5538bb4eb)
- [ext4: make "norecovery" an alias for "noload"](http://git.kernel.org/linus/e3bb52ae2bb9573e84c17b8e3560378d13a5c798)
- [ext4: make trim/discard optional (and off by default)](http://git.kernel.org/linus/5328e635315734d42080de9a5a1ee87bf4cae0a4)
- [ext4: Support for 64-bit quota format](http://git.kernel.org/linus/5a20bdfcdc5c5e5f0647d8d99a998066ef5496ac)
- [ext4: Update documentation to correct the inode_readahead_blks option name](http://git.kernel.org/linus/6d3b82f2d31f22085e5711b28dddcb9fb3d97a25)

*Various others*

- [aio: implement request batching](http://git.kernel.org/linus/cfb1e33eed48165763edc7a4a067cf5f74898d0b)
- [CIFS: Enable mmap on forcedirectio mounts](http://git.kernel.org/linus/a994b8fa669f16c50728328c3735722a3f20652e)
- [direct-io: cleanup blockdev_direct_IO locking](http://git.kernel.org/linus/5fe878ae7f82fbf0830dbfaee4c5ca18f3aee442)
- [exofs: Multi-device mirror support](http://git.kernel.org/linus/04dc1e88ad9c9f9639019e9646a89ce0ebf706bb)
- [fat: make discard a mount option](http://git.kernel.org/linus/681142f9211b23e6aa2984259d38b76d7bdc05a8)
- [fiemap: Add new extent flag FIEMAP_EXTENT_SHARED](http://git.kernel.org/linus/8c0414cd524e9f1c483ffb3ff1c2d860f5c567c8)
- [GFS2: add barrier/nobarrier mount options](http://git.kernel.org/linus/f25934c5f88655a8d5c3c40a540daed1f0e6dedc)
- [GFS2: Add cached ACLs support](http://git.kernel.org/linus/106381bfba997b83b64f68f2210e154162fc38e6)
- [GFS2: Add get_xquota support](http://git.kernel.org/linus/113d6b3c99bf30d8083068d00e3c7304d91d4845)
- [GFS2: Add get_xstate quota function](http://git.kernel.org/linus/1d371b5e179d943491a5fddad211cb317f38a142)
- [GFS2: Add set_xquota support](http://git.kernel.org/linus/e285c100362762f7440643be637dd332460fdc75)
- [GFS2: Fix up system xattrs](http://git.kernel.org/linus/2646a1f61a3b5525914757f10fa12b5b94713648)
- [GFS2: Improve statfs and quota usability](http://git.kernel.org/linus/3d3c10f2ce80d2a19e5e02023c2b7ab7086c36d5)
- [kill-the-BKL/reiserfs: add reiserfs_cond_resched()](http://git.kernel.org/linus/e43d3f21c502dec786f2885a75e25859f18d6ffa)
- [nfs41: add support for callback with RPC version number 4](http://git.kernel.org/linus/07bccc2dd4e8745859f0fa7d120ea39320fbcdbf)
- [nfs41: add support for the exclusive create flags](http://git.kernel.org/linus/4882ef72cd9a5c006087ca94a228323018eac29f)
- [NFS: Display compressed (shorthand) IPv6 in /proc/mounts](http://git.kernel.org/linus/d250e190fb9b06f4c595eade88b3d0b705fb330a)
- [nfs: new subdir Documentation/filesystems/nfs](http://git.kernel.org/linus/dc7a08166f3a5f23e79e839a8a88849bd3397c32)
- [NFS: Revert default r/wsize behavior](http://git.kernel.org/linus/dd47f96c077b4516727e497e4b6fd47a06778c0a)
- [nilfs2: add cache framework for persistent object allocator](http://git.kernel.org/linus/db38d5ad323362bfca118b52fe5906f97a69fb45)
- [nilfs2: add norecovery mount option](http://git.kernel.org/linus/0234576d041b9b2cc7043691ea61d2c2ca597aaa)
- [nilfs2: update mailing list address](http://git.kernel.org/linus/6aff43f817ddc54fcd6f0215bfba5d334b0bbbbd)
- [nilfs2: Using nobarrier option instead of barrier=off](http://git.kernel.org/linus/91f1953bf3243a4215b57d8e2f317a7035924de7)
- [ocfs2: Always include ACL support](http://git.kernel.org/linus/e6aabe0cac14a495d42f629a803c5e221089bae8)
- [procfs: allow threads to rename siblings via /proc/pid/tasks/tid/comm](http://git.kernel.org/linus/4614a696bd1c3a9af3a08f0e5874830a85b889d4)
- [proc: partially revert "procfs: provide stack information for threads"](http://git.kernel.org/linus/1306d603fcf1f6682f8575d1ff23631a24184b21)
- [proc: remove docbook and example](http://git.kernel.org/linus/82c1e49ccb28534b4e8b77d5f0ff553f19912d4d)
- [quota: Implement quota format with 64-bit space and inode limits](http://git.kernel.org/linus/498c60153ebb8889d8944591383c5c12af1127d4)
- [reiserfs: kill-the-BKL](http://git.kernel.org/linus/8ebc423238341b52912c7295b045a32477b33f09)
- [reiserfs, kill-the-BKL: fix unsafe j_flush_mutex lock](http://git.kernel.org/linus/a412f9efdd6424bf4bf28c8e8c92060b5e975482)
- [reiserfs: remove /proc/fs/reiserfs/version](http://git.kernel.org/linus/904e812931f001b984912b2d2f653ea69520313c)
- [sanitize xattr handler prototypes](http://git.kernel.org/linus/431547b3c4533b8c7fd150ab36980b9a3147797b)
- [seq_file: use proc_create() in documentation](http://git.kernel.org/linus/6be4b78993498c253e99b12c4d0f7684a36955e2)
- [UBIFS: support mounting of UBI volume character devices](http://git.kernel.org/linus/9722324e65a017ea0ce39236a2f87c649bb7c39d)
- [ufs: NFS support](http://git.kernel.org/linus/f3e2a520f5fb1a1df033efd9c2e5eadb384aad9b)
- [VFS: Export dquot_send_warning](http://git.kernel.org/linus/86e931a35e93d94e6e91b57cc76456e16d188ea9)
- [xfs: event tracing support](http://git.kernel.org/linus/0b1b213fcf3a8486ada99a2bab84ab8c6f51b264)
- [xfs: improve metadata I/O merging in the elevator](http://git.kernel.org/linus/2ee1abad73a12df5521cd3f017f081f1f684a361)
- [xfs: use DECLARE_EVENT_CLASS](http://git.kernel.org/linus/ea9a48881e093a41a79305fb1545ca0794b203dc)

**Storage**

*Block*

- [Add a tracepoint for block request remapping](http://git.kernel.org/linus/1a35e0f6443f4266dad4c569c55c57a9032596fa)
- [blkio: Export disk time and sectors used by a group to user space](http://git.kernel.org/linus/220841906fccafaf4094e87bdb6d252e20cf8c7c)
- [blkio: Introduce per cfq group weights and vdisktime calculations](http://git.kernel.org/linus/25bc6b07767fe77422312eda2af99c9477f76191)
- [blkio: Introduce the notion of cfq groups](http://git.kernel.org/linus/cdb16e8f739985b8a5c9f4569b026583bbcd01a5)
- [blkio: Introduce the root service tree for cfq groups](http://git.kernel.org/linus/1fa8f6d68b5c8ca0a608fd8d296c5f07ac788cd6)
- [blkio: Some debugging aids for CFQ](http://git.kernel.org/linus/2868ef7b39490e6b41c2c61cd9a5cd891e778b54)
- [block: add helpers to run flush_dcache_page() against a bio and a request's pages](http://git.kernel.org/linus/2d4dc890b5c8fabd818a8586607e6843c4375e62)
- [block: Allow devices to indicate whether discarded blocks are zeroed](http://git.kernel.org/linus/98262f2762f0067375f83824d81ea929e37e6bfe)
- [block: allow large discard requests](http://git.kernel.org/linus/ca80650cfbde5b17a5fa957a261c7973f84599a7)
- [block: Expose discard granularity](http://git.kernel.org/linus/86b37281411cf1e9bc0a6b5406c45edb7bd9ea5d)
- [block: use normal I/O path for discard requests](http://git.kernel.org/linus/1122a26f2abe4245ccdaed95ec23f63fe086b332)
- [cfq-iosched: enable idling for last queue on priority class](http://git.kernel.org/linus/a6d44e982d3734583b3b4e1d36921af8cfd61fc0)
- [cfq-iosched: fairness for sync no-idle queues](http://git.kernel.org/linus/718eee0579b802aabe3bafacf09d0a9b0830f1dd)
- [cfq-iosched: fix no-idle preemption logic](http://git.kernel.org/linus/e4a229196a7c676514c78f6783f8994f64bf681c)
- [cfq-iosched: reimplement priorities using different service trees](http://git.kernel.org/linus/c0324a020e5b351f100569b128715985f1023af8)
- [cfq: merge cooperating cfq_queues](http://git.kernel.org/linus/df5fe3e8e13883f58dc97489076bbcc150789a21)

*DM*

- [dm: add request based barrier support](http://git.kernel.org/linus/d0bcb8786532b01206f04258eb6b7d4ac858436a)
- [dm exception store: add merge specific methods](http://git.kernel.org/linus/4454a6216f75a9ef8c4bd0a65e34b101f725ef1e)
- [dm raid1: add framework to hold bios during suspend](http://git.kernel.org/linus/04788507686d184d8166918b70ef52311bc36dcb)
- [dm raid1: support flush](http://git.kernel.org/linus/4184153f9e483f9bb63339ed316e059962fe9794)
- [dm: simplify request based suspend](http://git.kernel.org/linus/9f518b27cf682dd5155a4c1679d52cd4b5be82f2)
- [dm snapshot: add allocated metadata to snapshot status](http://git.kernel.org/linus/985903bb3a6d98623360ab6c855417f638840029)
- [dm snapshot: permit only one merge at once](http://git.kernel.org/linus/9d3b15c4c776b041f9ee81810cbd375275411829)

*Libata*

- [ahci: let users know that Promise PDC42819 support is limited to SATA devices](http://git.kernel.org/linus/7a02267e0f3938a6e91c0a0a82211e4d7007210e)
- [ata_piix: enable 32bit PIO on SATA piix](http://git.kernel.org/linus/0b67c7439fe2a5d76602de36854c88e2beab00b0)
- [libata: add comment documenting PIO latency issues on UP](http://git.kernel.org/linus/9cd13bdbae5d83399c375b34ee1eb35e16c10568)
- [libata/drivers: Add driver for Apple "MacIO" IDE controller](http://git.kernel.org/linus/88358ab08944da726e948d216977ad499dfc15c6)
- [libata: MWDMA0 is unsupported on PIIX-like PATA controllers](http://git.kernel.org/linus/82563232c79c6f0099a02f7d2652ee7aee3fe9ba)
- [libata: Report zeroed read after TRIM and max discard size](http://git.kernel.org/linus/e78db4dfb1355a895f7ea50133b702b55b8ed184)
- [pata_cs5520: remove dead VDMA support](http://git.kernel.org/linus/940a68de56c1952c29d9f3c1a769a82b1bdd2b67)
- [pata_hpt37x: add proper cable detection methods](http://git.kernel.org/linus/9e87be9edd9114b65a9cf4f93a60b5d9134a972e)
- [pata_it8213: MWDMA0 is unsupported](http://git.kernel.org/linus/fd87e792add54a5ab526e91e67107962f160ec70)
- [pata_legacy: fix QDI6580DP support](http://git.kernel.org/linus/43c7d17ee7e03433c57dc4ce457d34110108455a)
- [pata_piccolo: Driver for old Toshiba chipsets](http://git.kernel.org/linus/8e182a90f91456335756d2ce304ad470795d98e1)
- [sata_fsl: Add asynchronous notification support](http://git.kernel.org/linus/fd6c29e3dec9e44ecbcba3c57efa08af70a10f1e)
- [sata_mv: add power management support for the PCI controllers.](http://git.kernel.org/linus/b2dec48ccaad004fc706352f82725d43369d9bd7)
- [sata_mv: add power management support for the platform driver](http://git.kernel.org/linus/6481f2b52cd5411ea6342b749daf0e4f3b390d7b)
- [sata_mv: support clkdev framework](http://git.kernel.org/linus/c77a2f4e6b76c9094182dfa653ece4243f6df80c)
- [sata_sil24: MSI support, disabled by default](http://git.kernel.org/linus/dae77214fa71898b84514e43721fb7bf260b026a)

*MD*

- [md: add honouring of suspend\_{lo,hi} to raid1.](http://git.kernel.org/linus/6eef4b21ffc9207b78fdd718154f5b004644b97d)
- [md: add MODULE_DESCRIPTION for all md related modules.](http://git.kernel.org/linus/0efb9e6191e1d3d34c1db90b829b742bc36d532e)
- [md: add 'recovery_start' per-device sysfs attribute](http://git.kernel.org/linus/06e3c817b750c131a20e82eed57a17841ea88ed2)
- [md/raid1: add takeover support for raid5-\>raid1](http://git.kernel.org/linus/709ae4879ae33628ded276ce7da8cd5acfec476b)
- [md: revise Kconfig help for MD_MULTIPATH](http://git.kernel.org/linus/93bd89a6d5f268acbdb8d775e40d3a280b07b5bd)
- [md: support bitmap offset appropriate for external-metadata arrays.](http://git.kernel.org/linus/f6af949c5672115313cc3c976d85b0533f607d7e)
- [md: support updating bitmap parameters via sysfs.](http://git.kernel.org/linus/43a705076e51c5af21ec4260a35699775ea298f5)
- [md: Support write-intent bitmaps with externally managed metadata.](http://git.kernel.org/linus/ece5cff0da9e696c360fff592cb5f51b6419e4d6)
- [raid: improve MD/raid10 handling of correctable read errors.](http://git.kernel.org/linus/1e50915fe0bbf7a46db0fa7e1e604d3fc95f057d)

*MFD/MMC/MTD*

- [DaVinci: MMC: MMC/SD controller driver for DaVinci family](http://git.kernel.org/linus/b4cff4549b7a8c5fc8b88e3493b6287555f0512c)
- [mfd: Add 88PM8607 driver](http://git.kernel.org/linus/4107da2a2853c070fb3effa58a83f94dc067fc44)
- [mfd: add AB4500 driver](http://git.kernel.org/linus/0c41839e98272a317d4af4dfcb54b599b2c3dcba)
- [mfd: Add ADP5520/ADP5501 driver](http://git.kernel.org/linus/a5736e0b62fcb7c1b20892c62e1c5fe5e9387c86)
- [mfd: Add all twl4030 regulators to the twl4030 mfd driver](http://git.kernel.org/linus/ab4abe056d8828341d2a7d6463b13eafaf210181)
- [mfd: Add power control platform data to SDHI driver](http://git.kernel.org/linus/be9cd7b6f84fd0cc59c8770771073b5c66f958ac)
- [mfd: Add SuperH Mobile SDHI platform driver](http://git.kernel.org/linus/a87d563873a6f1ee98233b57af665f2d0fc90ebb)
- [mfd: Add support for remapping twl4030-power power states](http://git.kernel.org/linus/b4ead61e570d7b7bcf20a5a1733dd0bc37236c99)
- [mfd: Add support for twl6030 irq framework](http://git.kernel.org/linus/e8deb28ca8e221de0239eafb3c3d431d8854278e)
- [mfd: Add support for WM8320 PMICs](http://git.kernel.org/linus/d4e0a89e3d170affa896efcdb4320e38a2f3a546)
- [mfd: Add twl6030 regulator subdevices](http://git.kernel.org/linus/9da66539281b5e15afc4a4739014c8923059d894)
- [mfd: Initial support for twl5031](http://git.kernel.org/linus/1920a61e208fac73d1a30a7cf4005701802fe69f)
- [mmc: add module parameter to set whether cards are assumed removable](http://git.kernel.org/linus/bd68e0838fe85794b06892054772fa013a8d1986)
- [mmc: atmel-mci: new MCI2 module support in atmel-mci driver](http://git.kernel.org/linus/74791a2dc8dc2af3feeaf3242d642ff58d33bd30)
- [mmc: Blackfin SD Host Controller Driver](http://git.kernel.org/linus/eb962d5bb7da4f25e20e5d448ee3aac394144ff6)
- [mtd: add ARM pismo support](http://git.kernel.org/linus/7cb777a3d71f9d1f7eb149c7a504d21f24219ae8)
- [mtd: Add bad block table overrides to Davinci NAND driver](http://git.kernel.org/linus/f611a79fe9859a30f2a7ae94b4d24f8e2dd75c91)
- [mtd: add bcmring nand driver](http://git.kernel.org/linus/266dead21675aeb89407b1213788cd924353d5e1)
- [mtd: add lock fixup for AT49BV640D and AT49BV640DT chips](http://git.kernel.org/linus/8dbaea4bfcecacaf496a3e2ae92867baedbcab8e)
- [mtd: add nand_ecc test module](http://git.kernel.org/linus/7126bd8be4ee009c56c4ec037f07f2c0884413fc)
- [mtd: add support for switching old SST chips into QRY mode](http://git.kernel.org/linus/4a58948669702639db7acecfa2105c3172d85c93)
- [mtd: m25p80: Add support for CAT25xxx serial EEPROMs](http://git.kernel.org/linus/837479d25e221ba616de2c734f58e1decd8cdb95)
- [mtd: m25p80: add support for Macronix MX25L4005A](http://git.kernel.org/linus/df0094d7f46d37944aa26b4f6e978b4b2ad252ea)
- [mtd: maps: remove obsolete ipaq-flash driver](http://git.kernel.org/linus/9729b260ea5ef4b2c5de0643a7b764b408e275b1)
- [mtd: mtdoops: make record size configurable](http://git.kernel.org/linus/9507b0c838e37651030d453b9cf3b136cfeefe89)
- [mtd: mtdoops: refactor as a kmsg_dumper](http://git.kernel.org/linus/2e386e4bac90554887e73d6f342e845185b33fc3)
- [mtd: nand: add option to quieten off the no device found messgae](http://git.kernel.org/linus/b1c6e6db5bb7acad82e1c64914c6a9404dae3ee1)
- [mtd: nandsim: add support for 4KiB pages](http://git.kernel.org/linus/75352662c54421b48ed58200565395b123952748)
- [mtd: OneNAND: multiblock erase support](http://git.kernel.org/linus/72073027ee95d059eb5a064da4a978efab36d4ab)
- [mtd: Really add ARM pismo support](http://git.kernel.org/linus/f6a8c60960bbea378142d1fa1b3d111555ee41c7)
- [mtd: tests: fix read, speed and stress tests on NOR flash](http://git.kernel.org/linus/f5e2bae0aad03164ffc7ce9dfeee6608e2c87dba)
- [mxc_nand: Add NFC V2 support](http://git.kernel.org/linus/9467114ef43c971f0ae8aee3729d412125a2f432)
- [sdhci: add support for the SysKonnect CardBus2SDIO adapter](http://git.kernel.org/linus/a7a6186c4b96d4ce5c1d13d91b7f862b0adc0e72)
- [sdhci-of: add support for the wii sdhci controller](http://git.kernel.org/linus/1144ab5d4b2da9f964d126105c6b3ced939eb073)
- [sdhci-of: reorganize driver to support additional hardware](http://git.kernel.org/linus/7657c3a7d4bd42b832af5d6bb0e0e9bdba82d44d)

*SCSI*

- [SCSI: add scsi target reset support to scsi ioctl](http://git.kernel.org/linus/3f9daedfcb197d784c6e7ecd731e3aa9859bc951)
- [SCSI: be2iscsi: Adding msix and mcc_rings V3](http://git.kernel.org/linus/bfead3b2cb4607c71831423c3ee97d22cd0c9dcb)
- [SCSI: be2iscsi: Adding support for various Async messages from chip](http://git.kernel.org/linus/78b9fb6d38b1caf1c11cba5b10bb859e3cce071f)
- [SCSI: bnx2i: Add 5771E device support to bnx2i driver](http://git.kernel.org/linus/5d9e1fa99c2a9a5977f5757f4e0fd02697c995c2)
- [SCSI: bnx2i: update CQ arming algorith for 5771x chipsets](http://git.kernel.org/linus/8776193bc308553ac0011b3bb2dd1837e0c6ab28)
- [SCSI: fcoe: add a separate scsi transport template for NPIV vports](http://git.kernel.org/linus/e9084bb8b4414dc1cfb840ac5a86fac23fccd013)
- [SCSI: fcoe, libfc: adds enable/disable for fcoe interface](http://git.kernel.org/linus/55a66d3c1e57f7e3e554d6ec8011e840f3802f20)
- [SCSI: fcoe: vport symbolic name support](http://git.kernel.org/linus/dc8596d303bb306da9ab5326fa6209710de86b8b)
- [SCSI: fnic: Add FIP support to the fnic driver](http://git.kernel.org/linus/78112e5558064cb4d2e355aed87b2036fcdfe3dd)
- [SCSI: ibmvfc: Add FC Passthru support](http://git.kernel.org/linus/d31429e1517c007781dfc68aed9b39cb5d3350a1)
- [SCSI: libfc: Add libfc/fc_libfc.\[ch\] for libfc internal routines](http://git.kernel.org/linus/8866a5d9075b7129194576f5f810e85a693c40ba)
- [SCSI: libfc: add some generic NPIV support routines to libfc](http://git.kernel.org/linus/174e1ebffd30a7599b889900089f7acef944cc6b)
- [SCSI: libfc: add support of receiving ELS_RLS](http://git.kernel.org/linus/63e27fb80c2010678681cef7b528ab8af3624fe9)
- [SCSI: libfc, fcoe: Add FC passthrough support](http://git.kernel.org/linus/a51ab39606042e76a483547620699530caa12c40)
- [SCSI: libfcoe, fcoe: libfcoe NPIV support](http://git.kernel.org/linus/11b561886643d4e23d0fd58c205d830a448dd0a2)
- [SCSI: libiscsi: add warm target reset tmf support](http://git.kernel.org/linus/3fe5ae8b4c4d3a82c755074878da7ddb9dde381e)
- [SCSI: lpfc 8.3.5: Add AER support](http://git.kernel.org/linus/0d87841997125971b7a39d21d1435054f91884c3)
- [SCSI: lpfc 8.3.5: fix fcp command polling, add FIP mode, performance optimisations and devloss timout fixes](http://git.kernel.org/linus/45ed119035b27f240345b06e090d559874e3677a)
- [SCSI: lpfc 8.3.5: fix reset path, ELS ordering and discovery issues](http://git.kernel.org/linus/4d9ab994e214d35107017c342aca42477b137316)
- [SCSI: lpfc 8.3.5: fix sysfs parameters, vport creation and other bugs and update logging](http://git.kernel.org/linus/6a9c52cf22e4ca13816bb2bd9899129cd4445de7)
- [SCSI: lpfc 8.3.6 : FC Protocol Fixes](http://git.kernel.org/linus/5ffc266ee7a62741ebee89ede15049ec0f02fa75)
- [SCSI: megaraid_sas: Add new megaraid SAS 2 controller support to the driver](http://git.kernel.org/linus/879111224d0784eab623fe8130a1f4481e0e1966)
- [SCSI: megaraid_sas: Add poll mechanism to megaraid sas driver](http://git.kernel.org/linus/c35188377f12e5e0a74f18c3dfdd67baf88db514)
- [SCSI: megaraid_sas: add sysfs for AEN polling](http://git.kernel.org/linus/72c4fd36dc7f755a5245ef2495fe27d5084d776d)
- [SCSI: megaraid_sas: add the IEEE SGE support to SAS2 controller](http://git.kernel.org/linus/f4c9a1317d32bb0af7546ef0c1dcc3be52dc8d0a)
- [SCSI: megaraid_sas: Add the support for updating the OS after adding/removing the devices from FW](http://git.kernel.org/linus/7e8a75f4dfbff173977b2f58799c3eceb7b09afd)
- [SCSI: megaraid_sas: Update version number and documentation](http://git.kernel.org/linus/a0b7736828f7615823a7dec680632656d9a9edde)
- [SCSI: mpt2sas: Added command line option diag_buffer_enable.](http://git.kernel.org/linus/32e0eb569df09a8cb790cf370ee498721d88e5c6)
- [SCSI: mpt2sas: Add Extended Type for Diagnostic Buffer support](http://git.kernel.org/linus/1b01fe3aa58b114b2dc296676023451c6434561e)
- [SCSI: mpt2sas: Adding MPI Headers - revision L](http://git.kernel.org/linus/9fec5f9fc2fbe7c6e39db01ae296528d9a20a5b1)
- [SCSI: mpt2sas : Add support for RAID Action System Shutdown Initiated at OS shutdown](http://git.kernel.org/linus/744090d38b47ed8ead8f68b6f0c65866c0b9b17a)
- [SCSI: mpt2sas: Add support in the driver to check for valid response info](http://git.kernel.org/linus/9982f59450930138eb0bf9a4ebf865e8c06ba705)
- [SCSI: mpt2sas: New device SAS2208 support is added](http://git.kernel.org/linus/db27136a89d061bf9dceb28953a61a8ef862ca7f)
- [SCSI: mpt2sas: Support for stopping driver when Firmware encounters](http://git.kernel.org/linus/fa7f31673583a6e0876f8bb420735cdd8a3ffa57)
- [SCSI: mvsas: add support for Adaptec ASC-1045/1405 SAS/SATA HBA](http://git.kernel.org/linus/7ec4ad0125db0222e397508c190b01c8f2b5f7cd)
- [SCSI: pm8001: enhance IOMB process modules](http://git.kernel.org/linus/72d0baa089ebd058cdb8b87fde835e9157c4597a)
- [SCSI: pmcraid: support SMI-S object model of storage pool](http://git.kernel.org/linus/729c845666be7092a52bf6fcdcf223fe4d9287a4)
- [SCSI: qla2xxx: Add firmware-dump kobject uevent notification.](http://git.kernel.org/linus/3420d36cac2f1d28fc99290de12dd66dfaf65d8e)
- [SCSI: scsi: Add missing command definitions](http://git.kernel.org/linus/f57e4502cea471c69782d4790c71d8414ab49a9d)
- [SCSI: scsi_debug: Thin provisioning support](http://git.kernel.org/linus/44d9269481bb43df445adf464b06ff031e67d7ea)
- [SCSI: scsi_dh_rdac: Add two new IBM devices to rdac_dev_list](http://git.kernel.org/linus/6f4fdda41b01100cfe02afb1b84bf422cbf557d4)
- [SCSI: sd: WRITE SAME(16) / UNMAP support](http://git.kernel.org/linus/e339c1a7c09ef736dca7b3a4353c7742557d9f8f)
- [SCSI: stex: add small dma buffer support](http://git.kernel.org/linus/cbacfb5fd9a4689b55157753b8ba4455415fb85c)
- [SCSI: stex: add support for reset request from firmware](http://git.kernel.org/linus/9eb46d2a08de537e14e92216bf18e7cb541d2f67)

Various others

- [Add COH 901 318 DMA block driver v5](http://git.kernel.org/linus/61f135b92f4758bc4d4767cd0a5d2da954e27f14)
- [cs5535: add pci id for AMD based CS5535 controllers](http://git.kernel.org/linus/10ca30285d5283ac88ba7ae94111f2e9fe59c232)
- [IB: Fix typo in ipoib.txt](http://git.kernel.org/linus/f7111821e51a58ee0f548f256743121ce1b365ae)
- [MFD: twl4030: add twl4030_codec MFD as a new child to the core](http://git.kernel.org/linus/0b83ddebc6e884dc0221358cf68c461520fbdd8e)
- [MFD: twl4030: add twl4030_codec MFD as a new child to the core](http://git.kernel.org/linus/3066eec68d21cf4d468809c0b7b1fe9ee59c8f32)
- [ppc440spe-adma: adds updated ppc440spe adma driver](http://git.kernel.org/linus/12458ea06efd7b44281e68fe59c950ec7d59c649)
- [RDMA/nes: Add additional SFP+ PHY uC status check and PHY reset](http://git.kernel.org/linus/a276510328d0721c252b37044c51e2fb4efe0364)
- [RDMA/nes: Add support for IB_WR\_\*INV](http://git.kernel.org/linus/649fe4aeab8c9b90eb31c899791534add0c78e04)
- [RDMA/ucma: Add option to manually set IB path](http://git.kernel.org/linus/a7ca1f00ed2921b804d7ebda0f6fca8c9078fa42)

For other articles on 2.6.33 and links to the rest of the "Coming in 2.6.33 " series, see [The H's Kernel Log - 2.6.33 Tracking page](../site/open/features/Linux-Kernel-2-6-33-tracking-890639.html "Linux Kernel 2.6.33 tracking – 21 December 2009, 10:18"). ([thl](mailto:thl@ct.heise.de))

([crve](mailto:crve@h-online.com "Chris von Eitzen "))
