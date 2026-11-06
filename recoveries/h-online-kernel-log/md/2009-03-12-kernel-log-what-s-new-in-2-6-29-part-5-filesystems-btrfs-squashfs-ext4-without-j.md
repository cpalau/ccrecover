---
title: "Kernel Log: What's new in 2.6.29 - Part 5: Filesystems Btrfs, SquashFS, Ext4 without journaling"
date: 2009-03-12
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-5-Filesystems-Btrfs-SquashFS-Ext4-without-journaling-740499.html
pages: 1
---

# Kernel Log: What's new in 2.6.29 - Part 5: Filesystems Btrfs, SquashFS, Ext4 without journaling

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/6/9/3/1/93e8ea3d0acdf147.jpg) If we are to believe the [statements made](http://thread.gmane.org/gmane.linux.kernel/802158) by Linus Torvalds when presenting the seventh release candidate of 2.6.29, and assuming release candidates come weekly, it will be at least another week or two before Linux kernel 2.6.29 becomes available. The Kernel Log will, therefore, continue its report about the new features scheduled for 2.6.29 with what's new in terms of file systems.

### Butter file system

As already [mentioned](../site/news/item/Btrfs-and-Squashfs-merged-into-Linux-kernel-739613.html "Btrfs and Squashfs merged into Linux kernel â 10 January 2009, 15:44") during the merge window of 2.6.29, the kernel developers have integrated the experimental [Btrfs](../site/news/item/Kernel-Log-Ext4-completes-development-phase-as-interim-step-to-btrfs-737697.html "Kernel Log: Ext4 completes development phase as interim step to btrfs â 17 October 2008, 09:52") file system. This doesn't imply that Btrfs is now complete â€“ it rather means that the kernel hackers intend to further develop and mature it within the Linux kernel framework as they did Ext4. Ext4 was integrated into Linux 2.6.19 in autumn 2006 and recently completed its main development phase in Linux 2.6.28.

Btrfs â€“ short for B-tree FS, but generally referred to as butterÂ FS â€“ is a "copy-on-write" file system originally created by kernel developer Chris Mason, who works at Oracle and had previously spent some time handling ReiserFS for Suse. After the first announcement of Btrfs on the Linux Kernel Mailing List (LKML) [in July 2007](http://thread.gmane.org/gmane.linux.kernel/541837), Mason quickly found support from other developers â€“ the comments to the commit were authored by developers employed, for example, by HP, Intel, Novell/Suse and Red Hat.

As Theodore Ts'o (also called Ted Tso or Tytso) the developer of Ext4 (and Ext2&3) revealed [in an email](http://thread.gmane.org/gmane.linux.file-systems/26246/focus%3D26492), several months ago at a meeting in autumn 2007, a number of key Linux file system developers already agreed that Btrfs should become the "next generation file system for Linux," . Ts'o says that he and other developers will still continue to develop Ext4, as its tried and tested Ext3 basis and its more advanced development, make it suitable as a bridge, until Btrfs has matured enough to earn the trust of enterprise users.

The [Btrfs wiki](http://btrfs.wiki.kernel.org) offers an overview of the most important features of this file system, which was specifically designed for Linux from scratch:

- Extent-based file storage (maximum file size 2^64 bytes)
- Space efficient packing of small files and indexed directories to minimise storage requirements
- Dynamic inode allocation
- Writable snapshots
- Subvolumes
- Checksums on data and metadata
- Compression
- Integrated multiple device support for combining several devices into one volume with several RAID algorithms
- On line file system check and defragmentation
- Very fast off line file system check
- Efficient incremental backup and file system mirroring
- Optional SSD optimisation

The [development time line](http://btrfs.wiki.kernel.org/index.php/Development_timeline) explains a few things that are still on the developers' to-do list, while the [changelog](http://btrfs.wiki.kernel.org/index.php/Changelog) offers a good overview of their achievements so far. The file system's structure and operation are explained in [another wiki document](http://btrfs.wiki.kernel.org/index.php/Btrfs_design), and frequently asked questions are answered in the [FAQ](http://btrfs.wiki.kernel.org/index.php/FAQ). While the "on disk" layout of the file system underwent several modifications during the development of Ext4, making it necessary to reformat when switching to a new kernel, the developers of Btrfs plan to spare users this hassle from now on â€“ although further changes to the on disk format of Btrfs can't be ruled out completely, of course.

Btrfs was integrated with its entire development history, which adds up to a total of more than 900 minor and major commits in the Linux source code management system. After its integration in early January this year, the kernel hackers extended the file system to include new features like the [support of SELinux](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0279b4cd86685b5eea467c1b74ce94f0add2c0a3). Further changes for 2.6.30 are already being prepared â€“ some of them designed to further improve performance.

While some of the Linux distributions are now considering Ext4 as their standard file system, it will probably be quite some time before the same is true for Btrfs. The Fedora developers, however, have already extended their development branch [installer and kernel](../site/news/item/Ext4-to-be-standard-for-Fedora-11-Btrfs-also-included-739769.html "Ext4 to be standard for Fedora 11, Btrfs also included â 22 January 2009, 10:44") to include Btrfs support.

### Squash file system

While the integration of the experimental Btrfs is initially unlikely to affect the majority of users and distribution developers, the addition of [SquashFS](http://squashfs.sourceforge.net/) should have a more immediate impact. SquashFS is a compressed read-only file system that various Linux distributions already use on their installation and live media (USB, CD or DVD) to minimise storage requirements. For the same reason, SqaushFS is often used in the embedded area as an alternative to Cramfs. The [kernel documentation for Squashfs](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob;f=Documentation/filesystems/squashfs.txt;hb=HEAD) offers detailed explanations of the differences between Cramfs and Squashfs and discusses the new file system's operation.

Several times in the past few years, the developers of SquashFS have tried to get their file system integrated into the Linux kernel, but they didn't manage to comply with the kernel hacker's high quality standards. Although they have worked to improve the criticised code segments in the now integrated version 4.0, the integration of SquashFS still came as quite a surprise â€“ following a long [discussion](http://thread.gmane.org/gmane.linux.file-systems/28733/) about the pros and cons, as well as several problems in the current code, [Linus Torvalds said](http://thread.gmane.org/gmane.linux.file-systems/28733/focus%3D28877) that it wouldn't make sense not to integrate it if everyone uses it anyway ("*if this is really in use by everybody, then not merging it is kind of pointless.* "); shortly afterwards, he merged the SquashFS patches into the main development branch.

### Even more about file systems

There are also a considerable number of changes to the kernel's long standing file systems. The kernel is now capable of a temporary file system freeze ([1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c4be0c1dc4cdc37b175579be1460f15ac6495e9a), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fcccf502540e3d752d33b2d8e976034dee81f9f7), [3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8e961870bb9804110d5c8211d5d9d500451c4518), [LWN article](http://lwn.net/Articles/287435/)) â€“ this is, for example, relevant for container virtualisation and for backup solutions. eCryptfs can now encrypt file names (for example [1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9c79f34f7ee71cd28272332b424ca64b2be006ab), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=51ca58dcc9f0d6b1e78954d08bd4954fb6a1421c), [3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=51ca58dcc9f0d6b1e78954d08bd4954fb6a1421c), [4](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=87c94c4df0149786ad91d8a03c738a03369ee9c8)); the developers incorporated numerous major changes to the Btree algorithm in XFS. They also made [major changes](http://thread.gmane.org/gmane.linux.kernel/775637) to the OCFS2 cluster file system, which now supports ACLs, security attributes, quotas and metadata checksums.

The developers also improved, tidied up and corrected Ext4 in [many](http://thread.gmane.org/gmane.comp.file-systems.ext4/10925) minor ways â€“ some of the changes have even been integrated into the 2.6.27 and 2.6.28 stable kernel series. In addition, the Ext4 developers adapted the [documentation for activating](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8e1a4857cd92e32e642b3e7184c7f6bf85c96e2e) write barriers, which had recently sparked prolonged discussions (see also the related [LWN article](http://lwn.net/Articles/283161/)). [Several changes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=30773840c19cea60dcef39545960d541b1ac1cf8) were made to the Fsync algorithm to marginally improve performance.

Thanks to several changes introduced by Google developers, Ext4 file systems can now be run without journaling to [further improve their speed](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0390131ba84fd3f726f9e24fc4553828125700bb) â€“ until now, some users still stuck with Ext2 to avoid the journaling overhead. A recent [blog entry by Theodore Ts'o](http://thunk.org/tytso/blog/2009/03/01/ssds-journaling-and-noatimerelatime/) contains a few test results detailing the impact journaling has on performance and some thoughts about using Ext file systems on SSDs. Those who are interested in Ext4 can find a lot of additional background information in a recently published [article on IBM's developerworks](http://www.ibm.com/developerworks/linux/library/l-anatomy-ext4/index.html).

The support of online defragmentation ("online defrag") in Ext4 has not yet been integrated in 2.6.29; at the end of January, a [new version was released](http://thread.gmane.org/gmane.comp.file-systems.ext4/11294) which also incorporates changes to some of the previously criticised code segments (see also the related [LWN article](http://lwn.net/Articles/317787/)).

### Many other changes

As well as the changes we've already discussed, 2.6.29 also supports many other important new file system features for the Linux kernel:

*Btrfs*

- There are too many commits to list, but these Git pull requests offer an overview ([1](http://thread.gmane.org/gmane.linux.kernel/791186), [2](http://thread.gmane.org/gmane.linux.kernel/794355), [3](http://thread.gmane.org/gmane.linux.kernel/797450), [4](http://thread.gmane.org/gmane.linux.kernel/799929), [5](http://thread.gmane.org/gmane.linux.kernel/799930), [6](http://thread.gmane.org/gmane.linux.kernel/804374)) as well as [the Git web interface](http://git.kernel.org/?p=linux%2Fkernel%2Fgit%2Ftorvalds%2Flinux-2.6.git&a=search&h=HEAD&st=commit&s=btrfs) at kernel.org.

*CIFS*

- [CIFS: add mount option to send mandatory rather than advisory locks](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=13a6e42af8d90e2e8eb7fa50adf862a525b70518)

*Ext\[234\]*

- [ext3: Add support for non-native signed/unsigned htree hash algorithms](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5e1f8c9e20a92743eefc9a82c2db835213905e26)
- [ext4: Add markers for better debuggability](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ba80b1019aa722b24506db1ee755e0bb2f513022)
- [ext4: Add mount option to set kjournald's I/O priority](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b3881f74b31b7d47d0f1c4d89ac3e7f0b9c05e3e)
- [ext4: Add sanity checks for the superblock before mounting the filesystem](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4ec110281379826c5cf6ed14735e47027c3c5765)
- [ext4: Add support for non-native signed/unsigned htree hash algorithms](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f99b25897a86fcfff9140396a97261ae65fed872)
- [ext4: Remove code to create the journal inode](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c31910672376dfb8d020e32afa7249763bcd924a)
- [ext4: Remove "extents" mount option](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=83982b6f47201c4c7767210d24d7d8c99567a0b3)
- [Update Documentation/file systems/ext4.txt](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8e1a4857cd92e32e642b3e7184c7f6bf85c96e2e)

*Fuse*

- [fuse: implement ioctl support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=59efec7b903987dcb60b9ebc85c7acd4443a11a1)
- [fuse: implement poll support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=95668a69a4bb862063c4d28a746e55107dee7b98)
- [fuse: implement unsolicited notification](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8599396b5062bf6bd2a0b433503849e2322df1c2)
- [fuse: update interface version](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1f55ed06cf0c361b293b32e5947d35d173eff2aa)

*OCFS2*

- [ocfs2: add mount option and Kconfig option for acl](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a68979b857283daf4acc405e476dcc8812a3ff2b)
- [ocfs2: add POSIX ACL API](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=929fb014e041c6572c5e8c3686f1e32742b5b953)
- [ocfs2: Add quota calls for allocation and freeing of inodes and space](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a90714c150e3ce677c57a9dac3ab1ec342c75a95)
- [ocfs2: add security xattr API](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=923f7f3102b80403152e05aee3d55ecfce240440)
- [ocfs2: Add the on-disk structures for metadata checksums.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ab552d54673f262d7f70014003d3928d29270f22)
- [ocfs2: Add the underlying blockcheck code.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=70ad1ba7b48364d758a112df0823edc5ca6632aa)
- [ocfs2: Assign feature bits and system inodes to quota feature and quota files](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1a224ad11eeb190da4a123e156601aad1bb67f24)
- [ocfs2: Enable quota accounting on mount, disable on umount](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=19ece546a418997226bd91552fbc41abcb05cea6)
- [ocfs2: Implementation of local and global quota file handling](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9e33d69f553aaf11377307e8d6f82deb3385e351)
- [ocfs2: Implement quota recovery](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2205363dce7447b8e85f1ead14387664c1a98753)
- [ocfs2: Periodic quota syncing](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=171bf93ce11f4c9929fdce6ce63df8da2f3c4475)
- [ocfs2: Remove JBD compatibility layer](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=53ef99cad9878f02f27bb30bc304fc42af8bdd6e)
- [ocfs2/xattr: Merge xattr set transaction.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=85db90e77806d48a19fda77dabe8897d369a1710)

*SquashFS*

- [MAINTAINERS: squashfs entry](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fc55584175589b70f4c30cb594f09f4bd6ad5d40)
- [Squashfs: block operations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e2780ab159ac60ef5bfc083081f44f8ff58579dc)
- [Squashfs: cache operations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f400e12656ab518be107febfe2315fb1eab5a342)
- [Squashfs: directory lookup operations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c88da2c979369e6bf8d2c0c80fad2f90c35e64ce)
- [Squashfs: directory readdir operations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=07972dde75c321162d076a925e3464ba259e73d7)
- [Squashfs: documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9eb425c046f4129f1dafce7c04e949652e69fb01)
- [Squashfs: export operations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=122601408d20c77704268f1dea9f9ce4abf997c2)
- [Squashfs: fragment block operations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=122edd1514aaaa90fd894663ecfcb4135063c63d)
- [Squashfs: header files](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ffae2cd73a9e828b1a188f83c5dedce16f7c0c68)
- [Squashfs: initrd support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b8fed87d3265d21d6f90e34934d93f70cb1e5cc1)
- [Squashfs: inode operations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6545b246a2c815a8fcd07d58240effb6ec3481b1)
- [Squashfs: Kconfig entry](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6ab5c1ca71ea8e04e97cd8ed473bd04e636850fd)
- [Squashfs: Makefiles](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fcef6fb6c5cf54927e1ca86b86a991e7aa9391f5)
- [Squashfs: regular file operations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1701aecb6849cc69bd54890532bcf92eedb00b74)
- [Squashfs: super block operations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0aa666190509ffab81c202c5095a166be23961ac)
- [Squashfs: symlink operations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1dc4bba39dd29c6d6f77ca7bf63cd3adeb6fc162)
- [Squashfs: uid/gid lookup operations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8256c8f631937bb08b3881c380c42ff6874a82f0)

*UBIFS*

- [UBIFS: add debugfs support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=552ff3179d1e93a3e982357544c059f3e9a5516e)
- [UBIFS: introduce compression mount options](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=553dea4dd531562688ba01c641c7f8fc7abaaf8c)
- [UBIFS: remove fast unmounting](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=27ad27993313312a4ad0047d0a944c425cd511a5)
- [UBIFS: separate debugging fields out](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=17c2f9f85c896b48a5d74a9155d99ec5b241a0e6)
- [UBIFS: slight compression optimisation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=062e4fee4400f283307cf8ac1b7931c939010229)
- [UBIFS: use bit-fields to store compression type](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a1dc080c27ec8ea7ca1c8a9b499362a71ebff792)

*XFS*

- [XFS: add generic btree types](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=de227dd9604934d2a6d33cd332d1be431719c93e)
- [XFS: add new btree statistics](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=854929f05831d3a290a802815ee955b96c740c61)
- [XFS: implement generic xfs_btree_decrement](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8df4da4a0a642d3a016028c0d922bcb4d5a4a6d7)
- [XFS: implement generic xfs_btree_delete/delrec](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=91cca5df9bc85efdabfa645f51d54259ed09f4bf)
- [XFS: implement generic xfs_btree_increment](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=637aa50f461b8ea6b1e8bf9877b0d13d00085043)
- [XFS: implement generic xfs_btree_insert/insrec](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4b22a57188d87e873346b73c227607715be96399)
- [XFS: implement generic xfs_btree_lookup](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fe033cc848489851f0c7de48f0b1bab5d744ad8a)
- [XFS: implement generic xfs_btree_rshift](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9eaead51bed957af0070a277d945744a76df0c8b)
- [XFS: implement generic xfs_btree_split](http://git.kernel.org/git/?p=3Dlinux/kernel/git/torvalds/li=)
- [XFS: make btree root in inode support generic](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8186e517fab1854554c48955cdbcbb6710e7baef)
- [XFS: make btree tracing generic](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8c4ed633e65d0bd0a25d45aad9b4646e3236cad7)
- [XFS: refactor xfs_btree_readahead](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b524bfeee2152fa64b6210f28ced80489b9d2439)
- [XFS: Sync up kernel and user-space headers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=847fff5ca881670ca8ec617afeb943950f0c804b)
- [XFS: Update maintainers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0335cb76aa3fa913a2164bc9b669e5aef9d56fa3)

*VFS, other file systems*

- [fs: use menuconfig to control the Misc. file systems menu](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=67ec7d3ab779ad9001ef57a6b4cfdf80ac9f9acc)
- [filesystem notification: create fs/notify to contain all fs notification](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=272eb01485dda98e3b8910c7c1a53d597616b0a0)
- [fix f_count description in Documentation/file systems/files.txt](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fd659fd6275d3426d7967da1f0e3638bbbd2fedb)
- [introduce new LSM hooks where vfsmount is available.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=be6d3e56a6b9b3a4ee44a0685e39e595073c6f0d)
- [kill -\>dir_notify()](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6badd79bd002788aaec27b50a74ab69ef65ab8ee)
- [nfsd: document new filehandle fsid types](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=548eaca46b3cf4419b6c2be839a106d8641ffb70)
- [NFSD: Add documenting comments for nfsctl interface](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=262a09823bb07c6aafb6c1d312cde613d0b90c85)
- [GFS2: Support for FIEMAP ioctl](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e9079cce201784632aed4b1a3121ee38c1ced0b6)
- [GFS2: Kill two daemons with one patch](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=97cc1025b1a91c52e84f12478dcf0f853abc6564)
- [quota: Allow to separately enable quota accounting and enforcing limits](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f55abc0fb9c3189de3da829adf3220322c0da43e)
- [poll: allow f_op-\>poll to sleep](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5f820f648c92a5ecc771a96b3c29aa6e90013bba)

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at The H Open Source:*

- [Kernel Log: Morton questions acceptance of Xen Dom0 code; file systems for SSDs](../site/news/item/Kernel-Log-Morton-questions-acceptance-of-Xen-Dom0-code-file-systems-for-SSDs-740375.html)
- [Kernel Log: Stable series development is speeding up, X Server 1.6 available soon](../site/news/item/Kernel-Log-Stable-series-development-is-speeding-up-X-Server-1-6-available-soon-740203.html "Kernel Log: Stable series development is speeding up, X Server 1.6 available soon â 23 February 2009, 10:46")
- [Kernel Log: What's new in 2.6.29 - Part 4: ACPI, PCI, PM â€“ notebooks and power saving improvements](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-4-ACPI-PCI-PM-notebooks-and-power-saving-improvements-739889.html "Kernel Log: What's new in 2.6.29 - Part 4: ACPI, PCI, PM – notebooks and power saving improvements â 31 January 2009, 15:01")
- [Kernel Log: New stable kernels, AMD 3D documentation and Mesa 7.3 released](../site/news/item/Kernel-Log-New-stable-kernels-AMD-3D-documentation-and-Mesa-7-3-released-739845.html "Kernel Log: New stable kernels, AMD 3D documentation and Mesa 7.3 released â 28 January 2009, 11:41")
- [Kernel Log: What's new in 2.6.29 - Part 3: Kernel controlled graphics modes](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-3-Kernel-controlled-graphics-modes-739697.html "Kernel Log: What's new in 2.6.29 - Part 3: Kernel controlled graphics modes â 17 January 2009, 07:36")
- [Kernel Log: main development phase for 2.6.29 ends, new X.org drivers](../site/news/item/Kernel-Log-main-development-phase-for-2-6-29-ends-new-X-org-drivers-739633.html "Kernel Log: main development phase for 2.6.29 ends, new X.org drivers â 12 January 2009, 17:09")
- [Kernel Log: What's new in 2.6.29 - Part 2: WiMax](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-2-WiMAX-739621.html "Kernel Log: What's new in 2.6.29 - Part 2: WiMAX â 12 January 2009, 10:19")
- [Kernel Log: What's new in 2.6.29 - Part 1: Dodgy Wifi drivers and AP support](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-1-Dodgy-Wifi-drivers-and-AP-support-739619.html "Kernel Log: What's new in 2.6.29 - Part 1: Dodgy Wifi drivers and AP support â 11 January 2009, 16:08")

*Older Kernel logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
