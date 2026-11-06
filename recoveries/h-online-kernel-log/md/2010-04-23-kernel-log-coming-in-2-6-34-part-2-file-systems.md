---
title: "Kernel Log: Coming in 2.6.34 (Part 2) - File Systems"
date: 2010-04-23
author: "Thorsten Leemhuis"
source: http://www.h-online.com/open/features/Kernel-Log-Coming-in-2-6-34-Part-2-File-Systems-985128.html
pages: 1
---

# Kernel Log: Coming in 2.6.34 (Part 2) - File Systems

**Thorsten Leemhuis**

**Version 2.6.34 of the Linux kernel will be the first to support the Ceph and LogFS file systems. A number of changes to the Btrfs and XFS code promise improved performance. The kernel should now be better at working with drives with 4 KB logical sectors.**

On Tuesday morning, Linus Torvalds [released](http://thread.gmane.org/gmane.linux.kernel/975498) the fifth pre-release version of Linux 2.6.34. One feature highlighted in Torvalds' release e-mail was a fix for [a problem in the ACPI subsystem](https://bugzilla.kernel.org/show_bug.cgi?id=15749) which had afflicted several testers.

Following the teething troubles at the start of the 2.6.34 development cycle, RC5 was released, as is usual at this point in the development cycle, around one week after [RC4](http://thread.gmane.org/gmane.linux.kernel/973119). The latter had been delayed as Torvalds and other developers spent days hunting down a bug in the kernel's memory management code. This gave rise both to a [lengthy discussion](http://thread.gmane.org/gmane.linux.kernel/968149/focus%3D969907) and to fixes for several other bugs uncovered during the search. Details of what went on and an in-depth look at parts of the virtual memory subsystem can be found in the article "[The case of the overly anonymous anon_vma](http://lwn.net/Articles/383162/)" on LWN.net.

In tandem with the ongoing development of Linux 2.6.34, Kernel Log will continue to report on major changes in the new kernel version, which is scheduled for release in May. Following on from part one of the 'What's coming in 2.6.34' series, which dealt with networking-related changes, part two deals with changes relating to file systems. This will be followed in the coming weeks with articles on graphics support, architecture code, drivers and a number of other areas.

### Two new file systems

The inclusion of [Ceph](http://ceph.newdream.net/) and [LogFS](http://logfs.org/logfs/) in 2.6.34 further expands the number of file systems supported by the Linux kernel.

Ceph ([git pull request](http://thread.gmane.org/gmane.linux.file-systems/38725)) is an [experimental](http://git.kernel.org/linus/9030aaf9bf0a1eee47a154c316c789e959638b0f), distributed, replicating network file system for clusters licensed under the LGPL. [According to the developers](http://ceph.newdream.net/about/), it is suitable for managing data volumes in the petabyte range "and beyond", is already pretty stable, and offers numerous features missing from comparable open source file systems. These include the ability to expand the file system simply by adding additional servers, with Ceph automatically distributing data across the new servers. It also aims to increase data throughout by automatically redistributing data. Although it uses parts of the still experimental Btrfs file system code for storing data, Ceph, which started out as a research project at the University of Santa Cruz' Storage Systems Research Center, should already be usable – though the developers do strongly advise users to back up important data.

The article "[Ceph: The Distributed File System Creature from the Object Lagoon](http://www.linux-mag.com/cache/7744/1.html)" in Linux Magazine (a US publication), by Dell employee and high performance computing specialist Jeffrey B. Layton, offers a good overview of Ceph. More information on the file system can be found in the [brief description of Ceph](http://git.kernel.org/linus/7ad920b504a980adcab4d3f6b85695526e6fd7bb) integrated into the file system code (distributed over more than 200 commits) and an [old article](http://lwn.net/Articles/258516/) on LWN.net, which describes an earlier Fuse-based version of the file system.

The second [new file system](http://git.kernel.org/linus/5db53f3e80dee2d9dff5e534f9e9fe1db17c9936) is again something with which the majority of users are unlikely to come into direct contact in the near future – LogFS uses [log structures](http://en.wikipedia.org/wiki/Log-structured_filesystem) and is of primary interest for flash drives with no wear levelling, used in embedded systems. Roughly speaking, the file system, which was largely developed by German developer Jörn Engel, does exactly what the firmware for solid state disks (SSDs) with SATA connectors does. It is, however, unlikely to be useful for desktop SSDs, as the Flash Translation Layer (FTL) and the file system get in each other's way. Background information on LogFS can be found in an [LWN.net article](http://lwn.net/Articles/234441/) from 2007 and in the LogFS documentation [in the kernel source code](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob;f=Documentation/filesystems/logfs.txt;hb=HEAD).

### Tuning

Btrfs maintainer Chris Mason briefly [elucidates](http://thread.gmane.org/gmane.linux.kernel/961862) some of the major changes in Btrfs (which were not merged into the main development tree until after the merge window had closed) in his git pull request. In future it will be possible to [specify](http://git.kernel.org/linus/73f73415caddbc01d9f10c03e0a677d5b3d11569) which sub-volume should be mounted by default where no volume is explicitly nominated. This should be useful for distributions which generate a Btrfs snapshot before installing updates, in order to allow users to roll back to a previous state in the event of problems. Red Hat developers are working on a similar function for [Fedora 13](https://fedoraproject.org/wiki/Features/SystemRollbackWithBtrfs). [A rewrite](http://git.kernel.org/linus/1e701a3292e25a6c4939cad9f24951dc6b6ad853) of the defrag code in Btrfs not only fixes various bugs, it also allows compression of selected files on otherwise uncompressed volumes. It is also now possible to defragment parts of a file. There have been additional [enhancements](http://thread.gmane.org/gmane.linux.kernel/961862/focus%3D5145) to allow updated files to be located more quickly.

[Various changes](http://thread.gmane.org/gmane.linux.kernel/955966) aimed at adding support for LZMA compression to SquashFS (used for Live CDs) proved not to be to Torvalds' taste. They will now be rewritten, but this [could take some time](http://thread.gmane.org/gmane.linux.kernel/976430/focus%3D117). Some of the underlying functions for LZMA and LZO compression and several [other changes](http://thread.gmane.org/gmane.linux.kernel/958071) to SquashFS were, however, merged into the main development tree.

Various enhancements to the XFS code should increase data throughput for some tasks. Details of these and other changes can be found in the [February](http://article.gmane.org/gmane.linux.kernel/958445) and [March](http://article.gmane.org/gmane.linux.kernel/975038) XFS status updates. Exofs (Extended Object File System), a file system designed for OSDs (object-based storage devices) which was merged into 2.6.30, [now supports](http://git.kernel.org/linus/5d952b8391692553c31e620a92d6e09262a9a307) RAID 0, with [RAID 5 and 6 in the pipeline](http://thread.gmane.org/gmane.linux.kernel/957455/).

The NILFS2 file system can now send [discard commands](http://git.kernel.org/linus/e902ec9906e844f4613fa6190c6fa65f162dc86e), which enables it to, for example, tell SSDs about free areas. A change to the partitioning code should allow the Linux kernel to work with hard drives with both a physical and logical 4 KB sector size. According to both [commit comments](http://git.kernel.org/linus/3fbf586cf7f245392142e5407c2a56f1cff979b6) and a recent [discussion](http://thread.gmane.org/gmane.linux.kernel/953981) on LKML, Western Digital is planning to introduce just such a hard drive in order to get around the 2 terabyte partition limit on hard drives partitioned using MBR.

### Minor gems

Many minor, but by no means insignificant, changes can be found in the list of commit headers below. The headers, as well as many of the links above, link to the [web interface](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=summary) for the git tree containing the kernel source code on kernel.org, which is maintained by Linus Torvalds. Commit comments and patches themselves generally provide extensive additional information on changes.

**Btrfs**

- [Btrfs: add a "df" ioctl for btrfs](http://git.kernel.org/linus/1406e4327be3a533a2b18582f715ce2cfbcf6804)
- [Btrfs: add ioctl and incompat flag to set the default mount subvol](http://git.kernel.org/linus/6ef5ed0d386be5c43ec66d6f2999919c0893558b)
- [Btrfs: add search and inode lookup ioctls](http://git.kernel.org/linus/ac8e9819d71f907a0532b01b22c26b56bbbcbd21)
- [Btrfs: cache the extent state everywhere we possibly can V2](http://git.kernel.org/linus/2ac55d41b5d6bf49e76bc85db5431240617e2f8f)
- [Btrfs: kill max_extent mount option](http://git.kernel.org/linus/287a0ab91d25ca982f895a76402e5893b47ed7a6)
- [Btrfs: make df be a little bit more understandable](http://git.kernel.org/linus/bd4d10888990f7e3f8029205d27eb155202d6969)
- [Btrfs: make subvolid=0 mount the original default root](http://git.kernel.org/linus/4849f01d153be0f52b8191ee1be0ce492aa96811)
- [Btrfs: run the backing dev more often in the submit_bio helper](http://git.kernel.org/linus/51684082b11c304829ea22193d4d96a5b1663b97)

**Ext-Family**

- [ext4: Add new tracepoint for jbd2_cleanup_journal_tail](http://git.kernel.org/linus/71f2be213a0009098819e5c04f75ff19f84f2122)
- [ext4: Add new tracepoints to debug delayed allocation space functions](http://git.kernel.org/linus/f8ec9d6837241865cf99bed97bb99f4399fd5a03)
- [ext4: deprecate obsoleted mount options](http://git.kernel.org/linus/437ca0fda3b442dff9e591581b5e1ffdfec24660)

**Others:**

- [9P2010.L handshake: Add mount option](http://git.kernel.org/linus/0fb80abd911a7cb1e6548b5279568dc1e8949702)
- [9p: documentation update](http://git.kernel.org/linus/9208d24253e5e644f8cb1b87b69de44897668303)
- [add several pieces to shared subtree documentation](http://git.kernel.org/linus/2f99cc6e4688faf5f03f9afe5e1c6097278c75b2)
- [CIFS: Add mmap for direct, nobrl cifs mount types](http://git.kernel.org/linus/810627a013163cd294762d57c0ea2ec055ffe4f6)
- [doc: add the documentation for mpol=local](http://git.kernel.org/linus/5574169613b40b85d6f4c67208fa4846b897a0a1)
- [Documentation/fs/: split txt and source files](http://git.kernel.org/linus/1e0051ae48a253685e4309256f9c1ec2bdb74b5d)
- [exofs: Define on-disk per-inode optional layout attribute](http://git.kernel.org/linus/d9c740d2253e75db8cef8f87a3125c450f3ebd82)
- [exofs: groups support](http://git.kernel.org/linus/50a76fd3c352ed2740eba01512efcfceee0703be)
- [fs/9p: Add hardlink support to .u extension](http://git.kernel.org/linus/5717144a01d701614cfdb15f09ed562d720cf3db)
- [FS-Cache: Remove the EXPERIMENTAL flag](http://git.kernel.org/linus/d4014030d2b2508aaf54093a5885f1c8a2275dd7)
- [net/9p: Add multi channel support.](http://git.kernel.org/linus/f75580c4afb72c156746b3fc1ec977b1a85d3dee)
- [nfsd: 4.1 has an rfc number](http://git.kernel.org/linus/73834d6f90f6833663f9effd4cf9b79b63bc36e1)
- [ocfs2_dlmfs: Add capabilities parameter.](http://git.kernel.org/linus/14a437c2b67aeee2a989a5d9c7e19094355d2fed)
- [ocfs2/userdlm: Add tracing in userdlm](http://git.kernel.org/linus/6fcef3f04a1a0f8d7a086147d2f2e650c8cc2754)
- [quota: split out compat_sys_quotactl support from quota.c](http://git.kernel.org/linus/5582c76f901d240f57329212b59b4d957ea8d6cf)
- [reiserfs: properly honor read-only devices](http://git.kernel.org/linus/3f8b5ee33293d43ca360771b535dfae8c57259dc)
- [Remove EXPERIMENTAL from NFS_FSCACHE](http://git.kernel.org/linus/4912002fffa377e66c5caefc2c311732a4ad5fb8)
- [Squashfs: add a decompressor framework](http://git.kernel.org/linus/4c0f0bb2351bee3de8dd7715ee199454a59f1230)
- [Squashfs: add decompressor entries for lzma and lzo](http://git.kernel.org/linus/dc3256782f88602953676c447b243dedb1be99ad)
- [xfs: Add trace points for per-ag refcount debugging.](http://git.kernel.org/linus/0fa800fbd549736dfdc1d7761f87e33dc8cd973b)
- [xfs: add tracing to xfs_swap_extents](http://git.kernel.org/linus/3a85cd96d3ab3c6dcf88b81fc6eaddb84e565a43)
- [xfs: implement optimized fdatasync](http://git.kernel.org/linus/66d834ea603d61bd90fedad90300ca91c5bba0a3)
- [xfs: Non-blocking inode locking in IO completion](http://git.kernel.org/linus/77d7a0c2eeb285c9069e15396703d0cb9690ac50)
- [xfs: Use delayed write for inodes rather than async V2](http://git.kernel.org/linus/c854363e80b49dd04a4de18ebc379eb8c8806674)

*For other articles on 2.6.34 and links to the rest of the "Coming in 2.6.34" series, see [The H's Kernel Log - 2.6.34 Tracking page](../site/open/features/Linux-Kernel-2-6-34-tracking-962586.html "Linux Kernel 2.6.34 tracking – 24 March 2010"). Older Kernel Logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/). New editions of Kernel Logs are also mentioned on* [Identi.ca](http://identi.ca/kernellog2) *and* [Twitter](http://twitter.com/kernellog2) *via "@kernellog2". The Kernel Log author also posts updates about various topics on* [Identi.ca](http://identi.ca/kernellogauthor) *and* [Twitter](http://twitter.com/kernellogauthor) *via "@kernellogauthor".*
