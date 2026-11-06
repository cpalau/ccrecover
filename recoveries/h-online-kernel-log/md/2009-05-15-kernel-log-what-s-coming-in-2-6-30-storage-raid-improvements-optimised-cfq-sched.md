---
title: "Kernel Log: What's coming in 2.6.30 - Storage: RAID improvements, optimised CFQ Scheduler, SAS drivers"
date: 2009-05-15
author:
source: http://www.h-online.com/open/news/item/Kernel-Log-What-s-coming-in-2-6-30-Storage-RAID-improvements-optimised-CFQ-Scheduler-SAS-drivers-741597.html
pages: 1
---

# Kernel Log: What's coming in 2.6.30 - Storage: RAID improvements, optimised CFQ Scheduler, SAS drivers

![The Kernel Log Penguin](../site/imgs/43/3/6/8/0/2/9/93e8ea3d0acdf147.jpg)

#### by Thorsten Leemhuis

**The next kernel version is to provide all that's necessary to convert, for example, a RAID 5 into a RAID 6 and vice versa. There are changes to the block layer designed to speed up the system, and new and improved drivers will offer better SAS support.**

With the [fifth release candidate](http://thread.gmane.org/gmane.linux.kernel/834261) of Linux 2.6.30 out a few days ago, the development of the next kernel version in the main development line continues to progress. As indicated by Linus Torvalds in his release email, the changes are slowly decreasing in number and size, which is what usually happens at this development stage.

As every development cycle tends to have eight or nine pre-release versions which often appear on a weekly basis, it will be another few weeks before Torvalds releases Linux 2.6.30. Nevertheless, the Kernel Log will continue its review of the major changes in Linux 2.6.30 with the following overview of the new developments in the storage infrastructure and driver areas.

**Flexible cooperation**

The developers have made quite a few changes to the code for MD (Multiple Device) software RAIDs (see list at the end of this article), which now also allow the number of devices in a RAID 5 to be [reduced](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ec32a2bd35bd6b933a5db6542c48210ce069a376). As a result, a RAID-5 array can now be converted into a RAID 6 and back again; in addition, the kernel can convert a RAID 1 into a RAID 5. However, the current version of the mdadm userland tool is unable to handle these extensive conversions.

The MD code [now also offers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3f9d99c12a533809342b475c95452e82761bcc1c) "data integrity support", which was [first included](../site/open/Kernel-Log-Linux-2-6-27-Released--/features/111671/2) in 2.6.27, as long as all the devices in an MD array and their respective controllers are also capable of it. Due to [various changes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9c47008d13add50ec4597a8b9eee200c515282c8), the same applies to the Device Mapper (DM), which now supports barriers better than it did before ([1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=692d0eb9e02cf81fb387ff891f53840db2f3110a), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=af7e466a1acededbc10beaba9eec8531d561c566)).

Numerous changes have been made to the block layer and its CFQ I/O scheduler after the developers found some performance issues in this area while doing tests that related to the [lengthy discussions around Ext3 and Ext4](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-File-systems-New-and-revamped-file-systems-741319.html "Kernel Log: What's coming in 2.6.30 - File systems: New and revamped file systems – 27 April 2009, 16:11") – some of the issues were so serious that Torvalds even threatened to replace the standard I/O scheduler. However, the developers were able to track down and eliminate the causes. In some cases this results not only in measurable, but also in noticeable performance improvements (see also the LWN.net article "[Solving the ext3 latency problem](http://lwn.net/Articles/328363/)").

#### Storage

Relevant Git-Pull-Requests:

- Block layer [1](http://thread.gmane.org/gmane.linux.kernel/812808), [2](http://thread.gmane.org/gmane.linux.kernel/818716), [3](http://thread.gmane.org/gmane.linux.kernel/822773), [4](http://thread.gmane.org/gmane.linux.kernel/826504)
- Device Mapper (DM): [1](http://thread.gmane.org/gmane.linux.kernel.device-mapper.devel/7766), [2](http://thread.gmane.org/gmane.linux.kernel.device-mapper.devel/7870)
- IDE: [1](http://thread.gmane.org/gmane.linux.ide/39290), [2](http://thread.gmane.org/gmane.linux.ide/39355), [3](http://thread.gmane.org/gmane.linux.ide/39423), [4](http://thread.gmane.org/gmane.linux.ide/39649)

<!-- -->

- Libata: [1](http://thread.gmane.org/gmane.linux.ide/39301), [2](http://news.gmane.org/find-root.php?message_id=20090407014232.GA5966@havoc.gtf.org)
- [Multiple Device (MD)](http://thread.gmane.org/gmane.linux.raid/22043)
- [MFD](http://thread.gmane.org/gmane.linux.kernel/817675)

<!-- -->

- SCSI: [1](http://thread.gmane.org/gmane.linux.scsi/49509), [2](http://thread.gmane.org/gmane.linux.scsi/49736)

**Substructure**

As we already mentioned in the [second part](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-File-systems-New-and-revamped-file-systems-741319.html "Kernel Log: What's coming in 2.6.30 - File systems: New and revamped file systems – 27 April 2009, 16:11") of the "What's coming in 2.6.30" mini series of the Kernel Log, the SCSI subsystem now also supports the rather exotic OSDs ([Object-based Storage Devices](http://en.wikipedia.org/wiki/Object_storage_device)) (for example [1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=02941a530ef736210b4cf8b24dd34c238d5d5a40), [2](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c6572c983726fe3f3bb5f07e9afe3a9b8e402d1b), [documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=78e0c621deca08e5f802383dbe75fd20b258ea4e)). For the first time, the [mpt2sas](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=635374e7eb110e80d9918b8611198edd56a32975) SCSI driver for SAS2004, SAS2008, SAS2108 and SAS2116 SAS-2.0 controllers by LSI has been included in the kernel. The stex driver [now also supports some of the SAS-6G controllers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0f3f6ee68f771b61dc6bc5ae7c2e355cfc5884d1) by Promise. [New in 2.6.29](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-6-Storage-IDE-PATA-SCSI-740501.html "Kernel Log: What's new in 2.6.29 - Part 6: Storage, IDE/PATA, SCSI – 13 March 2009, 13:45"), Fibre Channel over Ethernet [can now also handle](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=97c8389d54b9665c38105ea72a428a44b97ff2f6) FIP (FCoE Initialization Protocol), which serves for detecting and integrating Fibre Channel Forwarders (FCFs). After they already placed the firmware code of numerous SCSI drivers in separate files in versions 2.6.27, .28 and .29, the kernel developers have continued this work in 2.6.30 and split up a further few drivers.

Bartlomiej Zolnierkiewicz [announced](http://thread.gmane.org/gmane.linux.ide/39009) [a few weeks ago](../site/news/item/Kernel-Log-Tasmanian-devil-to-be-Linux-s-temporary-mascot-new-Radeon-drivers-740667.html "Kernel Log: Tasmanian devil to be Linux's temporary mascot, new Radeon drivers – 19 March 2009, 15:43") that he completed all of the planned IDE subsystem restructuring tasks and will from now on focus mainly on the subsystem's maintenance and on minor extensions. This has already been noticeable during the development of 2.6.30, where we've seen considerably less activity compared to the sometimes comprehensive changes to the IDE code in the previous few kernel versions. Comparatively few major changes – among them the [support of ATAPI devices](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=da14265e776f35067045b8555b5f5f7521e50bc4) in the sata_mvdriver, which handles Marvell ATA chips – were also made to the Libata subsystem, whose PATA drivers are used for the IDE adapters in most mainstream distributions.

#### Kernel Log – What's coming in 2.6.30

Other parts of the "What's coming in 2.6.30" mini series of the Kernel Log:

1\. [Network: New Wi-Fi drivers and other network novelties](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-Network-New-Wi-Fi-drivers-and-other-network-novelties-741197.html "Kernel Log: What's coming in 2.6.30 - Network: New Wi-Fi drivers and other network novelties – 17 April 2009, 10:51")

2\. [File systems: New and revamped file systems](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-File-systems-New-and-revamped-file-systems-741319.html "Kernel Log: What's coming in 2.6.30 - File systems: New and revamped file systems – 27 April 2009, 16:11")

The article ""[Steady growth: What's new in Linux 2.6.29](../site/open/features/Steady-growth-What-s-new-in-Linux-2-6-29-746553.html "Steady growth - What's new in Linux 2.6.29 – 24 March 2009, 15:26")" describes the new features of the kernel version in the main development line, current at the article's time of writing.

Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the Kernel Log at The H Open Source.

**Minor gems**

The kernel developers also [discussed](http://thread.gmane.org/gmane.linux.ide/39461/) extensions to incorporate ATA-TRIM, which allows the kernel to tell SSDs that support the relatively recent ATA command which areas no longer hold any data ("discard"). However, only a [patch](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0c659b82d11eaf5e1bee1f2bcb9994b9d09d175c) has been included in the kernel to provide the basis for further changes likely to be integrated with 2.6.31.

What we have mentioned so far only describes the most important and recent changes the kernel hackers have made to the storage-related code of Linux. Many further changes can be found in the following list containing the respective commits in the main development branch; the links directly display the changes in a [web frontend](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=summary), where the commit comment and the patch itself offer more information about the perhaps minor, but by no means unimportant changes.

**Block Layer**

- [as-iosched: get rid of private REQ_SYNC/REQ_ASYNC defines](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1d6bfbdf38f37bcc259e7c56c8c73664772651fb)
- [block: Add flag for telling the IO schedulers NOT to anticipate more IO](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=aeb6fafb8fa53266d70ca7474fcda2bdaf96524a)
- [block: update biodoc.txt on plugging](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=329007ce25d56fc7113df7b4828d607806d8bc21)
- [brd: support barriers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=dfbc4752eab33e66f113f9daa2effbe241cd661d)
- [cfq-iosched: add close cooperator code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a36e71f996e25d6213f57951f7ae1874086ec57e)
- [cfq-iosched: change dispatch logic to deal with single requests at the time](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2f5cb7381b737e24c8046fd4aeab571fb71315f5)
- [cfq-iosched: don't delay queue kick for a merged request](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d6ceb25e8d8bccf826848c2621a50d02c0a7f4ae)
- [cfq-iosched: don't let idling interfere with plugging](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b029195dda0129b427c6e579a3bb3ae752da3a93)
- [cfq-iosched: tweak kick logic a bit more](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2d870722965211de072bb36b446a4df99dae07e1)
- [Document and move the various READ/WRITE types](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=48e70bc18ac81881dedd3aa327c55b924fc41ecf)
- [loop: add ioctl to resize a loop device](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=53d6660836f233df66490707365ab177e5fb2bb4)
- [loop: support barrier writes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=68db1961bbf4e16c220ccec4a780e966bc1fece3)

**Device Mapper (DM)**

- [dm raid1: add is_remote_recovering hook for clusters](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7513c2a761d69d2a93f17146b3563527d3618ba0)

**IDE**

- [ide: merge ide_arm and ide_generic host drivers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4465461ece2b9249d6c0cf57bc0002100823e361)
- [ide: move xfer mode tuning code to ide-xfer-mode.c](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7eeaaaa52285d5e6cb79f515e99c591dcb9d04fe)

**Libata**

- [ahci: force CAP_NCQ for earlier NV MCPs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=aa431dd39d560586db22209b7f78c33455e1a786)
- [ata_piix: ICH7 does not support correct MWDMA timings](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c611bed780a51222ece8eaf303c779ef82d9d253)
- [ata: Report 16/32bit PIO as best we can](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e3cf95dd6d352954b663d2934110d6e30af2406d)
- [libata: ahci enclosure management bios workaround](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4c1e9aa41b2f9afe8f26e2efe5bb4695f6c40772)
- [pata_hpt37x: fix HPT370 DMA timeouts](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=265b7215aed36941620b65ecfff516200fb190c1)
- [sata_mv: introduce support for ATAPI devices](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=da14265e776f35067045b8555b5f5f7521e50bc4)

**Mapper Device (DM)**

- [Documentation/md.txt update](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=11373542344bdc35be1e6e68b0baadd1b6f7acbb)
- [md: add explicit method to signal the end of a reshape.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cea9c22800773cecb1d41f4a6139f9eb6a95368b)
- [md: add -\>takeover method for raid5 to be able to take over raid1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d562b0c4313e3ddea402a400371afa47ddf679f9)
- [md: add -\>takeover method to support changing the personality managing an array](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=245f46c2c221ef09c7db892f0e3fc2149be42052)
- [md: add takeover support for converting raid6 back into raid5](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fc9739c6d626ee79a148ec367d143b0601299a9d)
- [md: add takeover support for raid4 -\> raid5 conversion.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e9d4758f6e93488dc719a1445ce54659a570938f)
- [md: allow number of drives in raid5 to be reduced](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ec32a2bd35bd6b933a5db6542c48210ce069a376)
- [md: enable suspend/resume of md devices.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=409c57f3801701dfee27a28103dda4831306cb20)
- [md: occasionally checkpoint drive recovery to reduce duplicate effort after a crash](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=97e4f42d62badb0f9fbc27c013e89bc1336a03bc)
- [md/raid5: Add support for new layouts for raid5 and raid6.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=99c0fb5f92828ae96909d390f2df137b89093b37)
- [md/raid5: allow layout and chunksize to be changed on active array.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=88ce4930e2b80378d45506ce2c3bb5820e156e85)
- [md/raid5: allow layout/chunksize to be changed on an active 2-drive raid5.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b3546035277847028df650b147469fc943cf5c71)
- [md/raid5: finish support for DDF/raid6](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=67cc2b8165857ba019920d1f00d64bcc4140075d)
- [md/raid6: move raid6 data processing to raid6_pq.ko](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f701d589aa34d7531183c9ac6f7713ba14212b02)
- [md: remove CONFIG_MD_RAID_RESHAPE config option.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2cffc4a01dd90a502324e3453d7b245d6d16e1c2)
- [md: support bitmaps on RAID10 arrays larger then 2 terabytes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1f59390339f263c0fe7908fbe54466dbf3a64b58)

**MMC**

- [mmc: add MODALIAS linkage for MMC/SD devices](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6b0b62853b2553be375033776902640320970846)
- [mmc: SDIO driver for Marvell SoCs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=236caa7cc351f885874a2776b7dd1b5667359dc8)
- [sdhci: Add support for bus-specific IO memory accessors](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4e4141a526dd7f5ac3ce1458ae79ea6e5a515b06)
- [sdhci: Add support for card-detection polling](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=68d1fb7e229c6f95be4fbbe3eb46b24e41184924)

**MTD**

- [MTD-CHIPS: Add JEDEC probe support for the SST 39VF3201 flash chip](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bd50a0ffca0bbb9baa60ab1ef2c09cf7561e1223)
- [MTD-NAND: Add parent info for CAFÉ controller](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c451c7c4c9c4f59c7808a7d397d32bef160c14d9)
- [MTD-NAND: Add support for 4KiB pages.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=81ec5364a58c0545b694dee02fe65b9ae48f37b6)
- [MTD-NAND: Add support for NAND on the Socrates board](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1b578193af3b94c3d55d9aaf6b53275b1cb59a41)
- [MTD-NAND: davinci_nand driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ff4569c752c577c7e71e03c9d59e6ef85ca763c0)
- [MTD-NAND: FSL-UPM: add multi chip support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b6e0e8c07754c8aefd6ff3536463fed5f71405a0)
- [MTD-NAND: FSL-UPM: Add wait flags to support board/chip specific delays](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ade92a636f15d7e5b92e2df22e8fcb6c7640cd4f)
- [MTD-NAND: pxa3xx_nand: add ability to keep controller settings defined by OBM/bootloader](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f271049e2010b918f83dc1c7bbd5d75f4710506a)
- [MTD-NAND: TXx9: add NDFMC support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a591f5d35e89be90c04830d7de01c276af68aeb7)
- [MTD-NOR: Add device parent info to physmap_of](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=db99a5523175ba15fef4719c722cea11b94911bb)
- [MTD-OneNAND: Add write-while-program support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9ce969082e490d0a5a81862b364337c93dc3482a)
- [MTD: RBTX4939: add MTD support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cbf77c1bd9c79d1742976862d0b2bebaff1ea14d)
- [MTD: RBTX4939 map driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=610f75e74b636f933bc3e379a88a10f883b91332)
- [MTD: TXx9 SoC NAND Flash Memory Controller driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=64fb65baffa5b8f6f2eb3f628dec43c22cd1031f)
- [NOMMU: Make it possible for RomFS to use MTD devices directly](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=da4458bda237aa0cb1688f6c359477f203788f6a)

**SCSI**

- [SCSI: 3w-9xxx: add power management support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7a252fe7bcf64f1174b55c5c696ef2506b849f80)
- [SCSI: aacraid driver update](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d8e965076514dcb16410c0d18c6c8de4dcba19fc)
- [SCSI: advansys: use request_firmware](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=989bb5f58c14b87f059755f4bbb4b72408c76d9a)
- [SCSI: fcoe, libfc: add libfcoe module](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9b34ecffd59d6ed66fdd6906e8a092a33e7c8564)
- [SCSI: libosd: attributes Support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4ef1a3d70d02663f6bfe901db629e8e608da15b1)
- [SCSI: libosd: SCSI/OSD Sense decoding support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=98f3aea2bd4b4f9cd7a6a6479ed9410787f756fd)
- [SCSI: major.h: char-major number for OSD device driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=71969fd9e2c523d22bf1742eb31f1562247710eb)
- [SCSI: mpt2sas : Identify Dell series-7 adapters at driver load time](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f0f9cc1fb8a21f3ff90900505fc82a43d29d0975)
- [SCSI: osd: Kconfig file for in-tree builds](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6864abd8b730435d6ae9cb061095229a5a85153f)
- [SCSI: osd_uld: OSD scsi ULD](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=95b05a7db5865855c32e0bb8b244c3a7aac1cfeb)
- [SCSI: qla1280: use request_firmware](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1bfa11db712cbf4af1ae037cd25fd4f781f0c215)
- [SCSI: qla2xxx: Add Flash-Access-Control support for recent ISPs.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1d2874de809a14e6780246b99a18bbc0fc0a8f2a)
- [SCSI: qla2xxx: Add reset capabilities for application support.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6e181be508cf81fda4407b4689befeb7e4149607)
- [SCSI: qlogicpti: use request_firmware](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f894e74dc1983062d30d4e1b79bdb90b8a847f52)
- [SCSI: scsi: Add osd library to build system](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=68274794c69991121eaf0a4a35b78aa7f088ec2c)
- [SCSI: stex: add MSI support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=99946f8141f65a8bd5034ac5b1a53237aec8743e)
- [SCSI: stex: Add new device id](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=62e5b3d850f76190633e5a3cc8d6cc611ef96cfc)

**Various**

- [mflash: initial support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3fbed4c61abd8458896e38633d10110cb5a589d4)
- [UBI: add fsync capability](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1b24bc3aaba899f4e7f681cbbc3b93cadcf4d770)

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the Kernel Log at The H Open Source:*

- [Kernel Log: X.org 7.5 coming in summer, re-write for Intel's graphics driver](../site/news/item/Kernel-Log-X-org-7-5-coming-in-summer-re-write-for-Intel-s-graphics-driver-741405.html "Kernel Log: X.org 7.5 coming in summer, re-write for Intel's graphics driver – 04 May 2009, 07:09")
- [Kernel Log: What's coming in 2.6.30 - File systems: New and revamped file systems](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-File-systems-New-and-revamped-file-systems-741319.html "Kernel Log: What's coming in 2.6.30 - File systems: New and revamped file systems – 27 April 2009, 16:11")
- [Kernel Log: 3D support for the new Radeon driver; new Intel drivers](../site/news/item/Kernel-Log-3D-support-for-the-new-Radeon-driver-new-Intel-drivers-741271.html " Kernel Log: 3D support for the new Radeon driver; new Intel drivers – 22 April 2009, 17:06")
- [Kernel Log: What's coming in 2.6.30 - Network: New Wi-Fi drivers and other network novelties](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-Network-New-Wi-Fi-drivers-and-other-network-novelties-741197.html "Kernel Log: What's coming in 2.6.30 - Network: New Wi-Fi drivers and other network novelties – 17 April 2009, 10:51")
- [Kernel Log: Linux 2.6.30 is taking shape](../site/news/item/Kernel-Log-Linux-2-6-30-is-taking-shape-741093.html "Kernel Log: Linux 2.6.30 is taking shape – 09 April 2009, 06:41")
- [Kernel Log: Development of 2.6.30 is under way](../site/news/item/Kernel-Log-Development-of-2-6-30-is-under-way-740805.html "Kernel Log: Development of 2.6.30 is under way – 27 March 2009, 17:33")

*Older Kernel Logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/).*

([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
