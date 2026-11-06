---
title: "Kernel Log: What's new in 2.6.29 - Part 6: Storage, IDE/PATA, SCSI"
date: 2009-03-13
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-6-Storage-IDE-PATA-SCSI-740501.html
pages: 1
---

# Kernel Log: What's new in 2.6.29 - Part 6: Storage, IDE/PATA, SCSI

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/6/9/3/3/93e8ea3d0acdf147.jpg) With Linux Torvalds saying [2.6.29 could be available](http://thread.gmane.org/gmane.linux.kernel/802158) within a week or two, the Kernel Log continues its reporting about the new features scheduled for 2.6.29 with what's new in terms of storage drivers.

### Spoilt for choice with IDE/PATA

This development cycle once again included many changes to the kernel's IDE subsystem, which mainly controls parallel ATA adapters (generally referred to as "IDE adapters", [1](http://thread.gmane.org/gmane.linux.ide/36902), [2](http://thread.gmane.org/gmane.linux.ide/36978), [3](http://thread.gmane.org/gmane.linux.ide/37130)). Bartlomiej Zolnierkiewicz, who maintains this kernel area, ported a Libata driver [for the CS5536](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a77dcc437c1c3bc73887ecac8a304e4adcabb9b7) to the IDE subsystem and [reintroduced](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=391ad1908a9c13d457ea12ce1508d6b8a7ba72ad) the IT8172 driver for ITE's chip of the same name, which was removed in 2.6.18. Major changes were also made to several basic kernel features; see the commit links at the end of the article for more details.

These changes are unlikely to have any major effects on most users, as most current Linux distributions have predominantly used the Libata subsystem's drivers for parallel and serial ATA (SATA) adapters for quite some time. The Libata-based PATA drivers introduced with 2.6.19 are, therefore, by now likely to have undergone considerably better testing than their essentially older IDE counterparts, as the IDE subsystem has been subject to constant transformation over the past few months. How long the kernel developers intend to continue maintaining these two driver varieties is uncertain. Originally, the old IDE subsystem was expected to be removed once the Libata PATA drivers have been established; but now this doesn't seem likely any time soon.

### Libata, SCSI and subsystems

The Libata developers haven't been idle themselves ([1](http://thread.gmane.org/gmane.linux.ide/36885), [2](http://thread.gmane.org/gmane.linux.ide/37197)). Alan Cox extended the Libata subsystem to include [32-bit PIO support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=871af1210f13966ab911ed2166e4ab2ce775b99d); the sata-sil driver can now handle [large block transfers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c7e324f1bd17b25fcdca33bdad01cf6eb8be4933). A new addition is the support for the [VT6415](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5955c7a2cfb6a35429adea5dc480002b15ca8cfc) (PATA), [VT8261](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6813952021a7820a505002de260bda36978671f7) (SATA), and [VX855](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e4d866cdea24543ee16ce6d07d80c513e86ba983) (PATA) VIA chips as well as that of a related chip with the PCI ID 0x0571.

As announced, the kernel hackers have removed the [ide-scsi driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=93c164af19f608c5f737eb9bed8cb4de3a872329) in the SCSI subsystem, because series 2.6 kernels and modern burn programs have long been able to access IDE CD/DVD burners without SCSI emulation. A new feature in the SCSI subsystem is [Libfc](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=42e9a92fe6a9095bd68a379aaec7ad2be0337f7a), which was predominantly developed by Intel as part of the [Open FCoE project](http://www.open-fcoe.org/) â€“ Libfc is a modular fibre channel library required for the support of [Fibre Channel over Ethernet](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=85b4aa4926a50210b683ac89326e338e7d131211), another newly integrated technology. The new kernel will for the first time also include [the cxgb3i iSCSI driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c3673464ebc004a3d82063cd41b9cf74d1b55db2) for Chelsio adapters with T3 chips.

The Sysfs pseudo file system can now be used to [tell](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1308835ffffe6d61ad1f48c5c381c9cc47f683ec) the underlying block layer for IDE, Libata and SCSI subsystems whether a device is a "rotating medium" if the kernel itself is unable to establish this. This allows other kernel subsystems and userspace programs to activate optimised access patterns for hard disks or SSDs and achieve maximum speeds for data read and write access. The Device Mapper (DM) now includes [barrier](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ab4c1424882be9cd70b89abf2b484add355712fa) support, allowing it to respond to requests by the file system to ensure that the data was actually written to the storage media in the DM pool, before moving on to the next task â€“ this also benefits the integrity of journaling file systems (see also the related [LWN article](http://lwn.net/Articles/283161/)).

### Even more changes

In addition to the changes we've already discussed, 2.6.29 also supports many other important new storage features for the Linux kernel:

**Storage**

*DM, DMA, MD, UBI sowie Block-Layer inklusive IO-Scheduler*

- [async_tx, dmaengine: document channel allocation and api rework](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=28405d8d9ce05f5bd869ef8b48da5086f9527d73)
- [block: Add Kconfig help which notes that ext4 needs CONFIG_LBD](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4d783b093cd4f3e2738527365979cbd1c5101065)
- [block: add sysfs file for controlling io stats accounting](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=bc58ba9468d94d62c56ab9b47173583ec140b165)
- [block: add text file detailing queue/ sysfs files](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=cbb5901b904e122139e97c6f4caed9b1f13c3455)
- [block: don't use plugging on SSD devices](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a31a97381cdf7dceb03b797a8faf9bc8a01c65d1)
- [block: make barrier completion more robust](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8f11b3e99a1136fcbb67316c3260f085299c0bff)
- [block: Supress Buffer I/O errors when SCSI REQ_QUIET flag set](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=08bafc0341f2f7920e9045bc32c40299cac8c21b)
- [cfq-iosched: remove limit of dispatch depth of max 4 times quantum](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=30e0dc28bff9dc456cdfc2aae4aca78b8b1a1cec)
- [dm: add name and uuid to sysfs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=784aae735d9b0bba3f8b9faef4c8b30df3bf0128)
- [dmaengine: add a release for dma class devices and dependent infrastructure](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=41d5e59c1299f27983977bcfe3b360600996051c)
- [dmaengine: remove 'bigref' infrastructure](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f27c580c3628d79b17f38976d842a6d7f3616e2e)
- [dmaengine: up-level reference counting to the module level](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6f49a57aa5a0c6d4e4e27c85f7af6c83325a12d1)
- [dm: support barriers on simple devices](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ab4c1424882be9cd70b89abf2b484add355712fa)
- [Get rid of CONFIG_LSF](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b3a6ffe16b5cc48abe7db8d04882dc45280eb693)
- [nbd: tell the block layer that it is not a rotational device](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=31dcfab0ae6eb0340d456931df4d478e17efc65d)
- [UBI: document UBI ioctls](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8e26e1d7bce73acf6f995a4d252610e46ee831a5)
- [UBI: simplify PEB protection code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=7b6c32daec3bff380ced6822002bc352bdf2c982)

*IDE*

- [ata: add CFA specific identify data words](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d42ad15b759d05a87f22b484af63987eff38ea88)
- [ide: add at91_ide driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6e5f1e1115bb041993f9f247036996364b4c84d5)
- [ide: add port and host iterators](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2bd24a1cfc99d242c2cff9a6b74ca49fcaac3fb6)
- [ide: dynamic allocation of device structures](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5e7f3a46690f7f6c9f2781c700ab4370874aa0e8)
- [ide: ide.c 'clear' fix, update "ide=nodma" documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0af80c04e2f2e45ae09fceb17df8050f828a5c40)
- [ide: update warm-plug HOWTO](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=02c84bde234eee4f2089ac3587d138607aaec777)
- [it821x: Add ultra_mask quirk for Vortex86SX](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b94b898f3107046b5c97c556e23529283ea5eadd)

*Libata*

- [ahci: Add the Device IDs for MCP89 and remove IDs of MCP7B to/from ahci.c](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=7adbe46b9289794f8fe629cd78c876169741177f)
- [ata_piix: save, use saved and restore IOCFG](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2852bcf7c12d3027c5d10f4f5ca5fada24ce8088)
- [libata ahci: Add SATA GEN3 related messages](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8522ee25f3a645577d41e71328cd4fcf8610dfeb)
- [libata ahci: Withdraw IGN_SERR_INTERNAL for SB800 SATA](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e427fe042cf90c0652eed9a85e57a8fd8af89890)
- [libata: beef up iterators](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1eca4365be25c540650693e941bc06a66cf38f94)
- [libata: blacklist NCQ on OCZ CORE 2 SSD (resend)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5ccfca974f3ce3c33be72f1fcb2b42747714ec79)
- [libata: New driver for OCTEON SOC Compact Flash interface (v7).](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3c929c6f5aa7501790586a38dd8faca8fed9a158)
- [libata: use WARN_ON_ONCE on hot paths](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=efcb3cf7f00c3c424db012380a8a974c2676a3c8)
- [pata_hpt366: reimplement mode programming](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6ecb6f25d3a52c0d032aa73bde1ff9bc454aa66c)
- [pata_hpt3x3: Workarounds for chipset](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=978ff6db23279422046c1b3f89fe2045c234dc91)
- [SATA AHCI: Blacklist system that spins off disks during ACPI power off](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1fd684346d41f6be2487c161f60d03a7feb68911)
- [SATA: Blacklisting of systems that spin off disks during ACPI power off](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2a6e58d2731dcc05dafa7f976d935e0f0627fcd7)
- [sata_mv: fix 8-port timeouts on 508x/6081 chips](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b0bccb18bc523d1d5060d25958f12438062829a9)
- [sata_mv: Fix chip type for Hightpoint RocketRaid 1740/1742](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4462254ac6be9150aae87d54d388fc348d6fcead)
- [sata_mv: no longer experimental (v2)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f9228c7ffaaa37521c46239ccea623f10fa44a27)
- [SATA PIIX: Blacklist system that spins off disks during ACPI power off](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5f451fe1ab5d73b987051f0d23c85216c552e163)
- [SATA Sil: Blacklist system that spins off disks during ACPI power off](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e57db7bde7bff95ae812736ca00c73bd5271455b)

*MMC*

- [mmc: Add 8-bit bus width support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b30f8af3358b5c66be223e3a9f3d11b3d02b4a8f)
- [mmc: Add a MX2/MX3 specific SDHC driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d96be879ff469759af6d7fcebdb66237c18da6f8)
- [mmci: Add support for ST Micro derivate](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=cc30d60e4ca0b68e7e3f906eddd1e5b995d349f8)
- [mmc_spi: Add support for OpenFirmware bindings](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9c43df57910bbba540a6cb5c9132302a9ea5f41a)
- [mmc: warn about voltage mismatches](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f6e10b865c3ea56bdaa8c6ecfee313b997900dbb)
- [ricoh_mmc: Handle newer models of Ricoh controllers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0527a60c2b6bd7ab20e82cc5e488659e20eaaacd)
- [sdhci: activate led support also when module](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=35ff8554d12ecc80a46ea0d9bce34fe28733ff38)
- [sdhci: handle built-in sdhci with modular leds class](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f9134319c81c6c56e0ddf38e7adac2492b243d9b)
- [sdricoh_cs: Add support for Bay Controller devices](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=98444d3dd975653a4a970ecc0dfc30918da92f60)

*MDT*

- [MTD: add MTD tests to compilation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9faa8153bef4d82395e6ff7f87cb7c457055007c)
- [MTD: LPDDR Command set driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c68264711ca6caf87794caf9e79c30a4ba73c032)
- [MTD: LPDDR extended physmap driver to support LPDDR flash](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d81408304b06a71c28417445202af9cd6673168d)
- [MTD: LPDDR Makefile and KConfig](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=60f26520e7bd4479dbebf77317c45fc2255ba2e8)
- [MTD: NAND ndfc driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a808ad3b0d28411e2838117c5b2ae680ae42483c)
- [MTD: physmap: make physmap compat explicit](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=dcb3e137ce9be1dfc86e306182b23e3ae5e239c4)
- [MTD: tests: add mtd_oobtest](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e3644da7563d844e94b186a468e480c5575a6572)
- [MTD update internal API to support 64-bit device size](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=69423d99fc182a81f3c5db3eb5c140acc6fc64be)

*SCSI*

- [SCSI: FC protocol definition header files](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f032c2f7cdaae0e8907cd3b26426fc651dc5c275)
- [SCSI: hptiop: Add new PCI device ID](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b73a77494292b930642fbf87de3e3196593f7593)
- [SCSI: lpfc 8.3.0 : Add BlockGuard support (T10-DIF) code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e2a0a9d69ce224c6f5b72515d81150e6bf4a905a)
- [SCSI: lpfc 8.3.0 : Add BlockGuard support (T10-DIF) structs and defs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=81301a9b05c3690bf32bf4ef37d941f0f870a7ba)
- [SCSI: lpfc 8.3.0 : Added 3 small features and improve PCI EEH support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=97207482fcdd120a60a44e9eb6bbad8da6f81c9d)
- [SCSI: lpfc 8.3.0 : Add support for Power Management Suspend/Resume operations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3a55b5327b80d805eb3c9720092fd24f15193696)
- [SCSI: qla2xxx: Add ISP81XX support.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3a03eb797ce76ae8868a1497e9e746ad0add1e3b)
- [SCSI: qla2xxx: add support for multi-queue adapter](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=73208dfd7ab19f379d73e8a0fbf30f92c203e5e8)
- [SCSI: qla2xxx: Code changes for qla data structure refactoring](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e315cd28b9ef0d7b71e462ac16e18dbaa2f5adfe)
- [SCSI: qla2xxx: Refactor qla data structures](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=7b867cf76fbcc8d77867cbec6f509f71dce8a98f)

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at The H Open Source:*

- [Kernel Log: What's new in 2.6.29 - Part 5: Filesystems Btrfs, SquashFS, Ext4 without journaling](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-5-Filesystems-Btrfs-SquashFS-Ext4-without-journaling-740499.html "Kernel Log: What's new in 2.6.29 - Part 5: Filesystems Btrfs, SquashFS, Ext4 without journaling â 12 March 2009, 15:13")
- [Kernel Log: Morton questions acceptance of Xen Dom0 code; file systems for SSDs](../site/news/item/Kernel-Log-Morton-questions-acceptance-of-Xen-Dom0-code-file-systems-for-SSDs-740375.html "Kernel Log: Morton questions acceptance of Xen Dom0 code; file systems for SSDs â 06 March 2009, 08:57")
- [Kernel Log: Stable series development is speeding up, X Server 1.6 available soon](../site/news/item/Kernel-Log-Stable-series-development-is-speeding-up-X-Server-1-6-available-soon-740203.html "Kernel Log: Stable series development is speeding up, X Server 1.6 available soon â 23 February 2009, 10:46")
- [Kernel Log: What's new in 2.6.29 - Part 4: ACPI, PCI, PM â€“ notebooks and power saving improvements](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-4-ACPI-PCI-PM-notebooks-and-power-saving-improvements-739889.html "Kernel Log: What's new in 2.6.29 - Part 4: ACPI, PCI, PM – notebooks and power saving improvements â 31 January 2009, 15:01")
- [Kernel Log: New stable kernels, AMD 3D documentation and Mesa 7.3 released](../site/news/item/Kernel-Log-New-stable-kernels-AMD-3D-documentation-and-Mesa-7-3-released-739845.html "Kernel Log: New stable kernels, AMD 3D documentation and Mesa 7.3 released â 28 January 2009, 11:41")
- [Kernel Log: What's new in 2.6.29 - Part 3: Kernel controlled graphics modes](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-3-Kernel-controlled-graphics-modes-739697.html "Kernel Log: What's new in 2.6.29 - Part 3: Kernel controlled graphics modes â 17 January 2009, 07:36")
- [Kernel Log: main development phase for 2.6.29 ends, new X.org drivers](../site/news/item/Kernel-Log-main-development-phase-for-2-6-29-ends-new-X-org-drivers-739633.html "Kernel Log: main development phase for 2.6.29 ends, new X.org drivers â 12 January 2009, 17:09")
- [Kernel Log: What's new in 2.6.29 - Part 2: WiMax](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-2-WiMAX-739621.html "Kernel Log: What's new in 2.6.29 - Part 2: WiMAX â 12 January 2009, 10:19")
- [Kernel Log: What's new in 2.6.29 - Part 1: Dodgy Wifi drivers and AP support](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-1-Dodgy-Wifi-drivers-and-AP-support-739619.html "Kernel Log: What's new in 2.6.29 - Part 1: Dodgy Wifi drivers and AP support â 11 January 2009, 16:08")

*Older Kernel logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
