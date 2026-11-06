---
title: "Kernel Log: What's coming in 2.6.28 - Part 9: Fastboot and other remainders"
date: 2008-12-19
author: "Terry Relph-Knight"
source: http://www.h-online.com/open/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-9-Fastboot-and-other-remainders-739431.html
pages: 1
---

# Kernel Log: What's coming in 2.6.28 - Part 9: Fastboot and other remainders

**Terry Relph-Knight**

![Kernel Log logo](../site/imgs/43/3/6/5/8/6/3/a345f5e7c547062f.jpg) The previous eight parts of the kernel log's "What's coming in 2.6.28" series discussed some of the most important changes to the Linux kernel incorporated with 2.6.28. Quite a few of the commits for the main development branch, however, don't really belong to any of the topics discussed in the series so far and as a result, haven't yet been mentioned. In other cases, the kernel developers have made minor, but significant changes to some kernel areas, after we had covered them.

For example, we haven't mentioned some of the [changes introduced](http://thread.gmane.org/gmane.linux.kernel/743932) by Intel developer Arjan van de Ven to speed up hardware initialisation and booting (see [1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8bd9890e94627bc1ef372085e64dda7f9e307e82), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=709790a9aafe424785dd02bcb31b0dddb4ef59e4), [3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=589f800bb12c5cd6c9167bbf9bf3cb70cd8e422c), [4](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=02c15def8400a974fbce02b4f2d65b38c839e88b)). Van de Ven used these and several other changes [rejected](http://thread.gmane.org/gmane.linux.kernel/742582/focus%3D743021) by Linus Torvalds on a netbook that only required [five seconds for starting Linux](http://lwn.net/Articles/299483/) in a demonstration at the Linux Plumbers Conference. With the majority of systems, however, Linux 2.6.28 will start up only marginally faster, despite the fastboot patches, as the popular mainstream distributions waste most of their time initialising userspace services and loading the log-in manager and desktop environment. Those who want to analyse the required kernel initialisation time for optimisation regardless, now have access to a new tracing infrastructure specifically [designed for this purpose](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=aa5d9151f745b6ee6a236a1f109118034277eb92).

Apart from the heise Kernel Log, several other kernel developers and numerous online media have taken a closer look at the changes incorporated with Linux 2.6.28. The [overview at kernelnewbies.org](http://kernelnewbies.org/Linux_2_6_28), for example, offers its usual detailed review, while LWN.net founder and executive editor Jonathan Corbet, keeps his summary brief in the Linux Foundation's [Linux Weather Forecast](http://www.linux-foundation.org/en/Linux_Weather_Forecast) and in a relevant [blog entry](http://linux-foundation.org/weblogs/lwf/2008/10/24/2628-takes-shape/). However, Corbet discusses the changes in more detail in three articles on LWN.net, which also include mention of the changes to the kernel's programming interfaces that are important for developers ([1](http://lwn.net/Articles/302754/), [2](http://lwn.net/Articles/303609/), [3](http://lwn.net/Articles/304592/)). The developers of the WLAN subsystem have summarised the most important developments in the WLAN area [in their wiki](http://wireless.kernel.org/News/kernel-2.6.28). The [wiki of the FireWire developers](http://ieee1394.wiki.kernel.org/index.php/Release_Notes#Linux_2.6.28) divulges that some, seemingly inconspicuous, commits in the FireWire subsystem are designed to make this subsystem more resilient against connection terminations.

Linux 2.6.28 will probably be out in the next few days, as Linus Torvalds made the kernel's ninth release candidate available a few hours ago, [announcing](http://thread.gmane.org/gmane.linux.kernel/770804) that 2.6.28 will be a "Christmas release". ("*And btw, I do think that I'll make 2.6.28 be a Christmas release (or Hanukkah, Kwanzaa, Solstice, Insert-Favorite-Holiday, whatever). Because quite frankly, this kind of boredom won't help anything and I'll go stir crazy if I have to do this for another two weeks.*") Torvalds wants to extend the next kernel version's merge window, which is usually open for the two weeks directly after a new release, to give the kernel hackers that are taking time off during the holidays, enough time to prepare and submit their changes for the next kernel version.

*Numerous other important, but not quite as relevant changes in 2.6.28 we haven't discussed so far:*

**ACPI:**

- [ACPI: delete OSI(Linux) DMI dmesg spam](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a6e0887f21bbab337ee32d9c0a84d7c0b6e9141b)
- [ACPI: thinkpad-acpi: fix fan sleep/resume path](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0081b162023690877e0096ef17a82ba1969befa8)

**Networks:**

- [phylib: Add Vitesse VSC8221 SGMII PHY](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=11c6dd2c723a9ff9bdd4ee11b2798a08abc94e98)
- [phy: Add support for Marvell 88E1118 PHY](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=605f196efbf8dcbb3581e76ddd0573899dffcf1f)
- [rtl8187 : support for Sitecom WL-168 0001 v4](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f3c769185a28b7947d97b3552a977102c1fac3f2)

**File Systems:**

- [autofs4: add miscellaneous device for ioctls](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8d7b48e0bc5fa01a818eac713d4cb0763090cd0e)
- [autofs4: device node ioctl documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4b22ff13415fa30b6282c88da790c82b4c6e5127)
- [CIFS: Add nodfs mount option](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2c1b861539c15491593625920058e06452cd3747)
- [ext4: Fix file fragmentation during large file write.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=22208dedbd7626e5fc4339c417f8d24cc21f79d7)
- [ext4: Improve the documentation for ext4's /proc tunables](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=37515facd001942221d68171c81c1f46d54ffdd0)
- [ext4: Remove old legacy block allocator](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c2ea3fde61f1df1dbf062345f23277dcd6f01dfe)
- [ext4: Rename ext4dev to ext4](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=03010a3350301baac2154fa66de925ae2981b7e3)
- [ext4: Update Documentation/filesystems/ext4.txt](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=22359f5745eb26bd3205a1ede7968c8944398220)
- [GFS2: Fix metafs mounts](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9b8df98fc8973ad1c5f0d7c4cf71c7fb84fe22c5)
- [GFS2: Support for I/O barriers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=254db57f9b12daba841a4d91ddb9a8161e9c74ba)
- [ocfs2: Add extended attribute support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=cf1d6c763fbcb115263114302485ad17e7933d87)
- [ocfs2: Enable xattr set in index btree](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=012255961c9ecfe22b7a1df47ac26ab37818cb1e)
- [ocfs2: POSIX file locks support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=53da4939f349d4edd283b043219221ca5b78e4d4)
- [ocfs2: Switch over to JBD2.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2b4e30fbde425828b17f0e9c8f8e3fd3ecb2bc75)
- [vfs: vfs-level fiemap interface](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c4b929b85bdb64afacbbf6453b1f2bf7e14c9e89)
- [XFS: Account for allocated blocks when expanding directories](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6f9f51adb6ac0a49fce49e01c47dcfc2810c6e9d)
- [XFS: Wait for all I/O on truncate to zero file size](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2cf7f0da3ae225848a2ee10d4e216448a770fd00)
- [XFS: XFS: Check for valid transaction headers in recovery](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=220ca310a53200b4bfbc7c4c6e365eea284ec44f)

**Storage:**

- [ata: Fix experimental tags](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e3389cbc65ecc486d4aea2f0e9114abc0f849be2)
- [ahci: Add support for Promise PDC42819](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c77a036beceabbfd85b366193685cb49f38292bd)
- [ide: add generic ATA/ATAPI disk driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=806f80a6fc203ad0bde84e5a9e94572617d2ae45)
- [libata: add whitelist for devices with known good pata-sata bridges](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9ce8e3073d9cfd6f859c22a25441db41b85cbf6e)
- [libata: Avoid overflow in ata_tf_read_block() when tf-\>hba_lbal \> 127](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=44901a96847b9967c057832b185e2f34ee6a14e5)
- [libata: improve phantom device detection](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6a6b97d360702b98c02c7fca4c4e088dcf3a2985)
- [libata: pata_cs553\*.c: cleanup kernel-doc](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=bd6b52a17b9af630c38bb4f89609be5654d71e1e)
- [libata: pata_pcmcia: another memory card support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a12d6c9a09c644cb4a35be099eb5124d38e4feb8)
- [libata: pata_sch: notice attached slave devices](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=bc170e656881306d65eb1318c98032e1ab305ee8)
- [libata: switch to using block layer tagging support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2fca5ccf97d2c28bcfce44f5b07d85e74e3cd18e)
- [pata_hpt366: no ATAPI DMA](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3ee89f177e3cef0b5b024bcb6df683a3fa7d795f)
- [piix: add Hercules EC-900 mini-notebook to ich_laptop short cable list](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a8269e5423387ca0c6f6c75c42dad57c501025d3)
- [sata_sil24: configure max read request size to 4k](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e8b3b5e9f54512bfdb7c154da07ec0408cbd6c56)
- [sata_via: fix support for 5287](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b9d5b89b487517cbd4cb4702da829e07ef9e4432)
- [SCSI lpfc 8.2.8 : Add MSI-X support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9399627f340794baebf7e4581470ccb92f019acc)
- [SCSI lpfc 8.2.8 : Miscellaneous Bug Fixes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d7c255b26d8e3f12164d82093de3bf22efad2b4a)
- [SCSI lpfc 8.2.8 : Update driver for new SLI-3 features](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=34b02dcdcf1865405f4762b991965c0c3b8a3ae0)
- [SCSI lpfc 8.2.8 v2 : Add statistical reporting control and additional fc vendor events](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ea2151b4e142fa2de0319d9dd80413a997bf435a)
- [SCSI zfcp: attach and release SAN nameserver port on demand](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5ab944f97e09a3d52951fe903eed9a7b88d810b2)
- [SCSI zfcp: remove unused references, declarations and flags](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=44cc76f2d154aa24340354b4711a0fe7f8f08adc)
- [USB: storage: Avoid I/O errors when issuing SCSI ioctls to JMicron USB/ATA bridge](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3030ca4cf4abbdd2dd850a14d20e9fca5937ffb5)

**Graphics:**

- [drm/i915: Filter pci devices based on PCI_CLASS_DISPLAY_VGA](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=afa21e0584f78964c092981fad94e45d38cda249)
- [drm/radeon: map registers at load time](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=78538bf14995a136c2d9a22159ada49937359119)
- [drm: Remove infrastructure for supporting i915's vblank swapping.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5d8e6bb7a20b6206e1fe44565efc383a941b81fa)
- [efifb/imacfb consolidation + hardware support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=7c08c9ae0c145807c0dae4a55f240fa3d4fd5262)
- [fbdev: add new TMIO framebuffer driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b53cde3557b8f97e6a635782875d442551a89bf1)
- [i915: Save/restore MCHBAR_RENDER_STANDBY on GM965/GM45](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=881ee9889c8b98671c5491e43666bf5d4f78a180)
- [radeonfb: accelerate imageblit and other improvements](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b1ee26bab14886350ba12a5c10cbc0696ac679bf)
- [viafb: MAINTAINERS entry](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=69e4a7c27c1f0009b5a76b457f2ceeba6e557156)
- [viafb: Makefile, Kconfig](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6bde3ed98d9d0bc2e71b3123b003d5614debda74)
- [viafb: viafbdev.c, viafbdev.h](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=29b619fae69a0638ce10d5d6bb3c53f5d3ca0390)
- [viafb: viafb.modes, viafb.txt](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=09a525ec1cf5a142f2e73f15527c169dafc6ff52)
- [viafb: via_i2c.c, via_i2c.h, viamode.c, viamode.h](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9f291634aa2d79dee2d8a61c5bdffe166001c580)
- [viafb: via_utility.c, via_utility.h, vt1636.c, vt1636.h](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=23966d5b52e6ee1f90bb343766a9703dafceae83)

**Documentation:**

- [Add the development process document](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=75b021468368288ac8fec1a86a13f5cf2229139e)
- [Add a reference to paper to SubmittingPatches](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=12caa1b6fc3a9772535227c723c11878b5ca618e)
- [Create/use more directory structure in the Documentation/ tree.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=31c00fc15ebd35c1647775dbfc167a15d46657fd)
- [Documentation/kernel-parameters.txt: add min_addr, fix max_addr](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1c207f952a3a39f9d07a3e9de0cf6b9a9464eeaa)
- [PCI: document the pcie_aspm kernel parameter](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e5665a45fa28d0114f61b5d534a3b2678592219d)
- [PCI: Document that most pci options are shared between i386 and x86-64](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c01156061bdd5976397dfb173f8c70ae351a6cb6)
- [CFS scheduler: documentation about scheduling policies](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1a73ef6ac3f4b44abc9d1875eb9240d7524a7cf7)
- [sched: new documentation about CFS](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f58e2c33ffa31b8d4a71609a5e71e8d893574a07)
- [Document kernel taint flags properly](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=bb20698d46bac1b2b48cfe1fcb33e54ac885946a)

**Miscellaneous infrastructure and architecture support:**

- [block: add BIG FAT WARNING to CONFIG_DEBUG_BLOCK_EXT_DEVT](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0e11e342bac31f51ea055b147d20f77b59b9dd2c)
- [compat: generic compat get/settimeofday](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b418da16dd44810e5d5a22bba377cca80512a524)
- [Configure out AIO support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ebf3f09c634906d371f2bfd71b41c7e0c52efe7e)
- [cpumask: introduce new API, without changing anything](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2d3854a37e8b767a51aba38ed6d22817b0631e33)
- [cpumask: introduce new API, without changing anything, v3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=984f2f377fdfd098f5ae58d09ee04d5e29e6112b)
- [cpumask: new API, v2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=cd83e42c6b0413dcbb548c2ead799111ff7e6a13)
- [crypto: tcrypt - Add alg_test interface](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=01b323245e4f6d4a22ffd73754f145f45c85988c)
- [crypto: tcrypt - Avoid using contiguous pages](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f139cfa7cdccd0b315fad098889897b5fcd389b0)
- [deadline-iosched: allow non-sequential batching](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=63de428b139d3d31d86ebe25ae97b33f6540fb7e)
- [doc: unevictable LRU and mlocked pages documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fa07e787733416c42938a310a8e717295934e33c)
- [driver core: basic infrastructure for per-module dynamic debug messages](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=346e15beb5343c2eb8216d820f2ed8f150822b08)
- [dsa: fix master interface allmulti/promisc handling](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=df02c6ff2e3937379b31ea161b53229134fe92f7)
- [ftrace: add stack tracer](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e5a81b629ea8feb9e7530cfac35cfb41c45facf3)
- [ftrace: disable tracing on resize](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=bf5e6519b85b3853f2d0bb4f17a4e2eaeffeb574)
- [ftrace: remove daemon](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=cb7be3b2fc2cf089ee52b16f0fd9ebb29e9944e1)
- [ftrace: rename FTRACE to FUNCTION_TRACER](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=606576ce816603d9fe1fb453a88bc6eea16ca709)
- [ftrace: update txt document](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9b803c0fc37dc49d06d99d63741e78274801c644)
- [genirq: revert dynarray](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d6c88a507ef0b6afdb013cba4e7804ba7324d99a)
- [KEYS: Make request key instantiate the per-user keyrings](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1f8f5cf6e4f038552a3e47b66085452c08556d71)
- [md: allow extended partitions on md devices.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=92850bbd71228730c80efd491e7427650188d359)
- [md: destroy partitions and notify udev when md array is stopped.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=934d9c23b4c7e31840a895ba4b7e88d6413c81f3)
- [mfd: Add WM8350 audio register definitions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=06532c474718e330a7e3625ef91b94e22991128c)
- [MIPS: Add support for NXP PNX833x (STB222/5) into linux kernel](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=edb6310aaa0dfc3da303a4ba6dff9dce3fbaa8d3)
- [modules: fix module "notes" kobject leak](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e94320939f44e0cbaccc3f259a5778abced4949c)
- [mutex: speed up generic mutex implementations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a8ddac7e53e89cb877965097d05adfeb1c91def3)
- [netlabel: Add functionality to set the security attributes of a packet](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=948bf85c1bc9a84754786a9d5dd99b7ecc46451e)
- [netlabel: Add network address selectors to the NetLabel/LSM domain mapping](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=63c41688743760631188cf0f4ae986a6793ccb0a)
- [nohz: disable tick_nohz_kick_tick() for now](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ae99286b4f1be7788f2d6947c66a91dbd6351eec)
- [oprofile: Implement Intel architectural perfmon support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b99170288421c79f0c2efa8b33e26e65f4bb7fb8)
- [printk: robustify printk](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b845b517b5e3706a3729f6ea83b88ab85f0725b0)
- [printk: robustify printk, fix](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ced9cd40ac14111befd6b0c73ec90106c22a3fd7)
- [printk: robustify printk, fix \#2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fa33507a22623b3bd543b15a21c362cf364b6cff)
- [printk: robustify printk, update comment](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1fa63a817d27af7dc0d5ed454eb8fe5dec65fac7)
- [profiling: dynamically enable readprofile at runtime](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=22b8ce94708f7cdf0b04965c6f7443dfd374c35c)
- [reintroduce accept4](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=de11defebf00007677fb7ee91d9b089b78786fbb)
- [ring_buffer: implement new locking](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d769041f865330034131525ee6a7f72eb4af2a24)
- [sched: improve sched_clock() performance](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0d12cdd5f883f508d33b85c1bae98fa28987c8c7)
- [sched: release buddies on yield](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2002c69595a092518107f7e3c1294c9710bc92ae)
- [Schedule removal of the legacy i2c device driver binding model](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=00155a94a691c25d6672c16c8f2cafa7f9a722a3)
- [select: switch select() and poll() over to hrtimers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8ff3e8e85fa6c312051134b3953e397feb639f51)
- [SELinux: add boundary support and thread context assignment](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d9250dea3f89fe808a525f08888016b495240ed4)
- [ssb: Fix DMA-API compilation for non-PCI systems](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fd0fcf5c29dd0339c5f5d86eb2cbe9fdad5bcd73)
- [sysfs: crash debugging](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ae87221d3ce49d9de1e43756da834fd0bf05a2ad)
- [timers: handle HRTIMER_CB_IRQSAFE_UNLOCKED correctly from softirq context](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5d5254f0d3b9bebc47d97e357374c0ad0c291a7d)
- [tracing, sched: LTTng instrumentation - scheduler](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0a16b6075843325dc402edf80c1662838b929aff)
- [x86: more general identifier for Phoenix BIOS](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0af40a4b1050c050e62eb1dc30b82d5ab22bf221)
- [xtensa: Add config files for Diamond 232L - Rev B processor variant](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0025427eee4b5c005b4ac7a6489adc773e38611d)

**Various drivers:**

- [backlight: add support for Sharp SL-6000 LCD and backlight drivers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fbd1b17b43b8783a5408ec18c293dd8ebdc7e2cd)
- [coldfire: scheduled SERIAL_COLDFIRE removal](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=02f11f392434656f00fdcc8c51348d52bd39afe8)
- [crypto: rng - RNG interface and implementation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=17f0f4a47df9aea9ee26c939f8057c35e0be1847)
- [dm raid1: separate region_hash interface part1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1f965b19437017cea6d3f3f46acdc5acae5fd011)
- [HID: add quirk entry for no-name keyboard (0x13ba/0x0017)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fa157bdfe87c5ea98a80b96cb08f1ab509e21a52)
- [HID: add support for another Gyration remote control](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1e093206734568e780c2717da1c89b97e9471954)
- [HID: Add support for Sony Vaio VGX-TP1E](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=cc6e0bbb47f02fd36cd55b3189c0c79079096ab8)
- [i2c-i801: Add support for Intel Ibex Peak](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c429a247f56d277f12eaffd6525922353e9539a5)
- [i7300_idle driver v1.55](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=27471fdb32e77ecb92f09d4ac5757785b4dc33bc)
- [IA64 Add Variable Page Size and IA64 Support in Intel IOMMU](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=62fdd7678a26efadd6ac5c2869543caff77d2df0)
- [ics932s401: new clock generator chip driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a412ae3fb90ab49072b82c8cfa1e3e60d2b27005)
- [ide: Add tx4939ide driver (v6)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=37897989232e6533772b0e24369b35ee9f56c8b6)
- [intel-iommu: IA64 support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5b6985ce8ec7127b4d60ad450b64ca8b82748a3b)
- [leds: Add driver for HP harddisk protection LEDs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9c78ff6e65cad9f9fcf0bbde2bfbbf3a544fb704)
- [lm85: support adt7468 chips](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=79b92f2bab0dc5ac70e8391548f75ac3268426e4)
- [mfd: Add WM8350 interrupt support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ebccec0fa4e35dff0c18663a492a65f4dc6cad7a)
- [mfd: Core support for the WM8350 AudioPlus PMIC](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=89b4012befb1abca5e86d232bc0e2a797b0d9825)
- [mfd: Core support for the WM8400 AudioPlus HiFi CODEC and PMU](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1d9f9f040035da73d6ee5d2b3b3a25483a980da3)
- [mfd: TWL4030 core driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a603a7fa8717fb778bba91b5a879babf333dc6a3)
- [mfd: twl4030-gpio driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e9d359471dfed51a1bdeaa484ee7dac0679d0a20)
- [mlx4_core: Add Ethernet PCI device IDs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=57893d1cff4606915c13a4610d4e2d6048633f8e)
- [mlx4_core: Multiple port type support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=7ff93f8b7ecbc36e7ffc5c11a61643821c1bfee5)
- [mlx4_en: Add driver for Mellanox ConnectX 10GbE NIC](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c27a02cd94d6695fbe5858ca364b1e415af02212)
- [regulator: Add WM8350 regulator support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=da09155ac8d3f04c299b3d82a6ab0df8d03da632)
- [regulator: Add WM8400 regulator support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=42fad570b666256a3fd009e23e74cbb365a29ca8)
- [regulator: core - Rework machine API to remove string based functions.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a5766f11cfd3a0c03450d99c8fe548c2940be884)
- [Remove videobook.tmpl](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=7e3975617df8dd8b7fd94f14200abdec9f71729e)
- [sfc: Correct address of gPXE boot configuration in EEPROM](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=cd17fa7b8f1dd24b23c464ebcb14e7c058e15097)
- [sis190: add identifier for Atheros AR8021 PHY](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=708f6e27c3f75166433b69174a8348308e55d073)
- [Staging: add poch driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a14edddac99eff625cfcb44829ce206ec04be71a)
- [xtensa: Add support for the Sonic Ethernet device for the XT2000 board.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=74f2a5f0ef643b7b277f7a270f85573f88d930d1)
- [zd1211rw: Add 2 device IDs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0feec9dfe7b8880ab3b4c38d7cc4107dd706ea7f)

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: What's coming in 2.6.28 - Part 8: Video4Linux/DVB, (Wireless) USB, hardware monitoring, and input devices](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-8-Video4Linux-DVB-Wireless-USB-hardware-monitoring-and-input-devices-739405.html "Kernel Log: What's coming in 2.6.28 - Part 8: Video4Linux/DVB, (Wireless) USB, hardware monitoring, and input devices – 18 December 2008, 08:16")
- [Kernel Log: What's coming in 2.6.28 - Part 7: architecture support, memory subsystem and virtualisation](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-7-architecture-support-memory-subsystem-and-virtualisation-739397.html "Kernel Log: What's coming in 2.6.28 - Part 7: architecture support, memory subsystem and virtualisation – 17 December 2008, 10:35")
- [Kernel Log: What's coming in 2.6.28 - Part 6: Changes to the audio drivers](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-6-Changes-to-the-audio-drivers-739369.html "Kernel Log: What's coming in 2.6.28 - Part 6: Changes to the audio drivers – 15 December 2008, 17:53")
- [Kernel Log: New kernel versions, progress with Btrfs and Tux3](../site/news/item/Kernel-Log-New-kernel-versions-progress-with-Btrfs-and-Tux3-739341.html "Kernel Log: New kernel versions, progress with Btrfs and Tux3 – 13 December 2008, 11:07")
- [Kernel Log: VIA co-operates with the open source developers of openChrome](../site/news/item/Kernel-Log-VIA-co-operates-with-the-open-source-developers-of-openChrome-738911.html "Kernel Log: VIA co-operates with the open source developers of openChrome – 21 November 2008, 14:56")
- [Kernel Log: New graphics drivers and Linux versions: Dom0 patches for 2.6.29?](../site/news/item/Kernel-Log-New-graphics-drivers-and-Linux-versions-Dom0-patches-for-2-6-29-738149.html "Kernel Log: New graphics drivers and Linux versions: Dom0 patches for 2.6.29? – 17 November 2008, 13:14")
- [Kernel Log: What's coming in 2.6.28 - Part 5: updates for netbooks and notebooks](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-5-updates-for-netbooks-and-notebooks-738121.html "Kernel Log: What's coming in 2.6.28 - Part 5: updates for netbooks and notebooks – 14 November 2008, 12:51")
- [Kernel Log: New kernels, open audio drivers for X-Fi](../site/news/item/Kernel-Log-New-kernels-open-audio-drivers-for-X-Fi-738061.html "Kernel Log: New kernels, open audio drivers for X-Fi – 11 November 2008, 10:03")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).*

([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([trk](mailto:trk@h-online.com "Terry Relph-Knight"))
