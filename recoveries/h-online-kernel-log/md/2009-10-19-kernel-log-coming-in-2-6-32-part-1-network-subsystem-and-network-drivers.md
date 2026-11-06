---
title: "Kernel Log: Coming in 2.6.32 (Part 1) – Network subsystem and network drivers"
date: 2009-10-19
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-Coming-in-2-6-32-Part-1-Network-subsystem-and-network-drivers-832229.html
pages: 1
---

# Kernel Log: Coming in 2.6.32 (Part 1) – Network subsystem and network drivers

**Dj Walker-Morgan**

![](../site/imgs/43/4/2/4/8/7/7/kernellogpenguin.jpg-93e8ea3d0acdf147.jpeg)

**by Thorsten Leemhuis**

Between Thursday evening and Friday morning, Linus Torvalds [released](http://thread.gmane.org/gmane.linux.kernel/903346) the fourth release candidate of Linux version 2.6.32, although, due to the [typing error](../site/news/item/Kernel-Log-Improved-USB-3-0-support-X-org-drivers-to-move-back-into-X-Server-819872.html "Kernel Log - Improved USB 3. 0 support, X.org drivers to move back into X Server – 07 October 2009, 16:18") in the first release candidate (RC1 was mis-labeled RC2), it is called 2.6.32-rc5 instead of 2.6.32-rc4.

Torvalds released this version only a few days after [RC4](http://thread.gmane.org/gmane.linux.kernel/900833), as he and many other kernel hackers will spend the weekend travelling to this year's [Linux Kernel Summit](http://events.linuxfoundation.org/events/kernel-summit) held in Tokyo next week; therefore few changes are expected to make their way into the Linux kernel's source code management system during this time.

Another major SCSI driver was merged into the Linux kernel's main development branch with RC4 and RC5 offers two further network drivers. Such stragglers can be found in almost any development cycle. As usual, however, the majority of changes were incorporated during the merge window, which lasts two weeks and was closed by Torvalds with the release of the first RC at the end of September. The Kernel Log is, therefore, already in a position to provide an overview of some of the major enhancements of Linux 2.6.32, which is expected to be released at the beginning of December. We are starting our "What's coming in 2.6.32" mini series with the most important changes to the kernel's network support; major changes in other kernel areas will be discussed in further editions of the series over the next few weeks.

### Wireless

The developers have [re-activated](http://git.kernel.org/linus/e0f114e82e3781087a0ad0e92c94ff0d55012c1a) the p54 driver's power saving support. While, to bypass a [bug](http://bugzilla.intellinuxwireless.org/show_bug.cgi?id=1982) that is presumed to be hardware-related, they have done the opposite with the iwl4965 driver for Intel's Wireless Wi-Fi Link 4965AGN, and [disabled](http://git.kernel.org/linus/559a4741b8a5b4551b8c7e8e0de7f3e41a79bb5a) it. It is yet uncertain if they will ever be able to re-activate the power saving features. However, the kernel hackers also improved the driver for Intel Wi-Fi chips, which can now [automatically select](http://git.kernel.org/linus/e312c24cf8229f9b6e76dbfd5d99eefe21f4ac0a) the appropriate sleep state for the Wi-Fi hardware using information gathered via pm_qos (Power Management Quality of Service).

Following various restructuring measures to the [ath9k](http://linuxwireless.org/en/users/Drivers/ath9k) driver for many recent Atheros Wi-Fi chips, the developers have [extended](http://git.kernel.org/linus/ac88b6ecdfa629fd1261dab1504d78a56fd4cabf) the driver to support AR9287 Wi-Fi chips; [some rudimentary first](http://git.kernel.org/linus/d7e7d229c7d1395283e1e1fda8727af60ca6f4ad) components for examining the AR9271 were also incorporated into the kernel.

The MAC8021 Wi-Fi stack now scans for Wi-Fi networks in the background, which allows access point connections to continue transmitting data. This is an interesting feature for location-based services and roaming, as highlighted in a [blog post](http://blogs.gnome.org/dcbw/2009/10/06/whipping-out-the-pipe-snake/) by Dan Williams, the main developer of NetworkManager.

A new addition is the [wl1271](http://git.kernel.org/linus/f5fc0f86b02afef1119b523623b4cde41475bc8c) driver for the Wi-Fi part of Texas Instruments' WiLink 6.0 mobile platform used in the embedded area. The b43 driver for Wi-Fi chips by Broadcom can now also handle low power PHYs (LP-PHY) such as the [BCM4312](http://git.kernel.org/linus/867b2efe68b6bb929e3bd1c6d699ba61ff2cf847), which can be found in some notebooks and in the embedded area. The prism54 driver, which has been superseded by the p54pci driver, is now planned for removal from the kernel in version [2.6.34](http://git.kernel.org/linus/4d8cd26849737e141ff0aa23fedacef4ea76ea4f).

### Networking

Just in time for RC5, the kernel hackers have incorporated the [vmxnet3 driver into the main development branch](http://git.kernel.org/linus/d1a890fa37f27d6aca3abc6e25e4148efc3223a6). It is able to communicate with the "vmxnet3 virtual ethernet NIC" - a network adaptor that emulates several virtualisation solutions by VMware. In addition, Linux 2.6.32 [will offer the infrastructure](http://git.kernel.org/linus/05c6a8d7a7d778f26d8eb821556988993b766092) required for updating ("flashing") the firmware of network chips using the ethtool program.

The r8169 driver for recent network hardware by Realtek now also supports the RTL8168D chip. However, this is only one of many network drivers that have been extended to support new hardware – more information about these changes can be found in the commits in the "Minor Gems" section at the end of this article.

The btusb driver [is now capable of](http://git.kernel.org/linus/7bee549e197c9c0e92b89857a409675c1d5e9dff) USB autosuspending – with Bluetooth chips that don't support remote wake-up, however, the interface must be shut down for the power saving mechanisms to take effect. The [btmrvl](http://git.kernel.org/linus/132ff4e5fa8dfb71a7d99902f88043113947e972) and [btmrvl_sdio](http://git.kernel.org/linus/789221ecc870117b77e354d488d5d29f15410de8) drivers for Bluetooth chips by Marvell ([documentation](http://git.kernel.org/linus/196be0cd018068d545e1d764094c7b07aaf0bcfe)) are new additions. The kernel developers also integrated several mISDN drivers:

- [avmfritz](http://git.kernel.org/linus/6115d2f3fcaebed5b88fa9cefd178bb5b07461ff) for AVM PCI cards in the Fritz! series
- [netjet](http://git.kernel.org/linus/a900845e56617edc005fd8f35bfd5a407aaf96c8) for NETJet PCI cards by Traverse Technologies
- [mISDNinfineon](http://git.kernel.org/linus/cae86d4a4e56eeda1afdea38f230d222edda7dd5) for various ISDN chips by Siemens and Infineon
- [speedfax](http://git.kernel.org/linus/da2272c91ae81b41ae6fa6ebdc767a6cef73b770) for the ISAR DSP chip by Siemens used in Speedfax+ hardware
- [w6692](http://git.kernel.org/linus/707b2ce6c1f4f1261788f2ff09ad82c35e0e6240) for PCI cards with Winbond W6692

Another kernel first is a driver for the CAN controller on Atmel AT91SAM9263 chips, which was introduced by a [Pengutronix](http://www.pengutronix.de) employee ([1](http://git.kernel.org/linus/68f40152747da28ae0de21633c9062671448b66c), [2](http://git.kernel.org/linus/99c4a6344f6574c97019ac16e8d54bfe5ad21f2d)). Predominantly introduced by Oracle developers, the code that supports the Reliable Datagram Sockets ([RDS](http://oss.oracle.com/projects/rds)) protocol created for server clusters [now also supports](http://git.kernel.org/linus/70041088e3b976627ba9a183b812f39ef8a9ba0e) transmissions via TCP.

### Minor Gems

The kernel hackers have considerably improved the support of wireless extensions (WE) and network namespaces. Some of these and further minor, but by no means insignificant, changes can be found in the list below. Like many of the references in the text above, the links point to the relevant commit in the [web front end](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=summary) of the main Linux development branch, where the commit comments and the patches themselves provide extensive further information on the respective changes.

##### **LAN**

- [Add support for w90p910 mac driver](http://git.kernel.org/linus/5be93b9a865344cf69958777c8d7c6f758cba416)
- [be2net: Add GRO support to the be2net driver. LRO is not supported anymore.](http://git.kernel.org/linus/5be93b9a865344cf69958777c8d7c6f758cba416)
- [be2net: Changes to support flashing of the be2 network adapter](http://git.kernel.org/linus/84517482e19bc775de7b3b4e998dee2f506bc34e)
- [bnx2: Update firmware to 5.0.0.j3.](http://git.kernel.org/linus/078b0735881c7969aaf21469f3577831cddd9f8c)
- [bnx2x: Adding XAUI CL73 autoneg support](http://git.kernel.org/linus/239d686d494f10ecd83a89ddc4e31f9462ca4901)
- [bnx2x: Fan failure](http://git.kernel.org/linus/fd4ef40d5977e1c226e9cd9659398e82cc4a1e85)
- [bnx2x: Fan failure early detection](http://git.kernel.org/linus/eb8da205a6cac953a46a247b8dd19505eba944e2)
- [bnx2x: New FW files](http://git.kernel.org/linus/6200f09036ee6f12822a9133dba7ed011b179c69)
- [bnx2x: Removing old FW files](http://git.kernel.org/linus/a1d58179d1337ff8f8530c9fac8b9e98b2f7761f)
- [bnx2x: Supporting BCM8727 PHY](http://git.kernel.org/linus/4d295db0efd2ccf06edb7a45ad885b40c56b7161)
- [bnx2x: Supporting Device Control Channel](http://git.kernel.org/linus/2691d51d7243560aa0870dadbf5c6b98f647f751)
- [bnx2x: Supporting PHY FW upgrade](http://git.kernel.org/linus/f57a60256d02daba1316c98da472f02cd98a58d3)
- [bnx2x: Using the new FW](http://git.kernel.org/linus/ca00392cb8f5227c67ff52c656d91a764d022ab9)
- [broadcom: Add AC131 phy support](http://git.kernel.org/linus/d7a2ed9248a3c3ec6afe3be0c351bd1ca9e981f3)
- [broadcom: Add BCM50610M support](http://git.kernel.org/linus/4f4598fd0a87f39955e71bcb7447f403dafc20ba)
- [can: sja1000: Add support for the new 4 channel EMS CPC-PCI cards](http://git.kernel.org/linus/dd52856ba24ed2f67679c86f207e5a9bab1eb93b)
- [dm9000: add checksum offload support](http://git.kernel.org/linus/5dcc60b71886795965fd5029b5d9a9ba7b5a2c17)
- [drivers/net: ks8851_mll ethernet network driver](http://git.kernel.org/linus/a55c0a0ed41533b3a7b32a6c8acdc1bb04a017b5)
- [e1000: allow ethtool coalesece to adjust interrupts per second](http://git.kernel.org/linus/94c9e5a89349a1f1ebabe0876c059dc387b8b2a0)
- [e1000: drop dead pcie code from e1000](http://git.kernel.org/linus/1532ecea1debf8d2cd50c99e299ad35f43a55291)
- [e1000: implement jumbo receive with partial descriptors](http://git.kernel.org/linus/edbbb3ca107715067b27a71e6ea7f58750912aa2)
- [igb: add support for 82576 mezzanine card](http://git.kernel.org/linus/4703bf73bd5b0d43c3eb5b547398d4f62dc5d4e1)
- [igb: make serdes power down available for 82575 in addition to 82576 parts](http://git.kernel.org/linus/099e1cb700da6359b784ac7fb65099091b7b961e)
- [ixgbe: Add device support for a new copper 82598 device](http://git.kernel.org/linus/3845bec0f33f7c2604ba985f6f80983d0c139d46)
- [ixgbe: add support for 82599 based X520 10G Dual KX4 Mezz card](http://git.kernel.org/linus/dbfec662f2aaf640f4a59242bd233206c3905bb8)
- [ixgbe: add support for 82599 Combined Backplane](http://git.kernel.org/linus/312eb9316fe2673100769e4028af2c1ee33cc40d)
- [ixgbe: Add support for using FCoE DDP in 82599 as FCoE targets](http://git.kernel.org/linus/d4ab88194e982a0d213000a75475d3e76b2626f0)
- [macvlan: add multiqueue capability](http://git.kernel.org/linus/2c11455321f37da6fe6cc36353149f9ac9183334)
- [MIPS: BCM63XX: Add integrated ethernet PHY support for phylib.](http://git.kernel.org/linus/09bb9aa0ed22bea814b0f137390f911af33ddd1b)
- [mlx4_core: Add 40GigE device ID](http://git.kernel.org/linus/e76d0b67d022fe70def07cfff3cdb36138b4c3f2)
- [net: Add DEVTYPE support for Ethernet based devices](http://git.kernel.org/linus/384912ed194e43c03ad1cdaa09b0b1e488c34d46)
- [net: add support for STMicroelectronics Ethernet controllers.](http://git.kernel.org/linus/47dd7a540b8a0cdc028914b7351fca0cf0a1d305)
- [net: add Xilinx emac lite device driver](http://git.kernel.org/linus/bb81b2ddfa194b6d12761a350b5b5985cecae0a9)
- [net: Teach pegasus driver to ignore bluetoother adapters with clashing Vendor:Product IDs](http://git.kernel.org/linus/ab854b24a2113ec0c17343e72d22b8876930d0a3)
- [netxen: add hardware LRO support](http://git.kernel.org/linus/c1c00ab8626298ac784ea344bf10e94b5bd9bcb5)
- [netxen: add vlan tx acceleration support](http://git.kernel.org/linus/028afe719855a157e32450c36b7a12e1f9e85abe)
- [netxen: ethtool statistics and control for LRO](http://git.kernel.org/linus/1bb482f8a46000f77577948ff1c350275bba7dc9)
- [netxen: firmware hang detection](http://git.kernel.org/linus/6a581e93981e8838c85e407303186faf937830d3)
- [pcnet_cs: add cis of Linksys multifunction pcmcia card](http://git.kernel.org/linus/531afd64d027e3d798c416b2b37b3cfb1de417d9)
- [pcnet_cs: add cis of National Semicondoctor's multifunction pcmcia card](http://git.kernel.org/linus/bf6fda63c452205f0e240ed8c511db5693857e93)
- [smsc95xx: add additional USB product IDs](http://git.kernel.org/linus/6f41d12bab6e5ce317b0494f5b3cd0b60e14ebc3)
- [tg3: Add 5717 asic rev](http://git.kernel.org/linus/f6eb9b1fc1411d22c073f5264e5630a541d0f7df)
- [tg3: Add 57788, remove 57720](http://git.kernel.org/linus/5e7ccf2003e6a9c35b5aa24953ba5009a1a8b653)
- [tg3: Add MSI-X support](http://git.kernel.org/linus/679563f47cd2547a0e091b5bd3ddf30027af6b08)
- [tg3: Add new 5785 10/100 only device ID](http://git.kernel.org/linus/2befdcea96fcd9a13e94373c66ea1dd7365d2a74)
- [tg3: Add RSS support](http://git.kernel.org/linus/baf8a94a572928710e9e60967d153a7bf3aebd9c)
- [tg3: Add TSS support](http://git.kernel.org/linus/fe5f5787f0866e9f883bdd90018a354f2f3defd1)
- [ucc_geth: Implement suspend/resume and Wake-On-LAN support](http://git.kernel.org/linus/2394905f67aeec5f9452f2881cbeb2b42009de0e)
- [vlan: multiqueue vlan device](http://git.kernel.org/linus/2e59af3dcbdf11635c03f22bfc9706744465d589)

**WLAN**

- [ar9170: remove EXPERIMENTAL marker](http://git.kernel.org/linus/91b092d73435489d7336f94e927d96224b26c9a8)
- [ar9170usb: add usbid for TP-Link TL-WN821N v2](http://git.kernel.org/linus/fe9f6342c86292aee1941447f22dc5470735e5a1)
- [ath5k: add hardware CCMP encyption support](http://git.kernel.org/linus/1c81874078dc96b8158ce7b0dab54afe43c8d03e)
- [ath5k: enable hardware LEDs](http://git.kernel.org/linus/f0f3d388baabdbc613548d6ad8e5da7616b1cbd1)
- [ath5k: remove EXPERIMENTAL marker](http://git.kernel.org/linus/75323fa3dec54abb0bcba8ce6b4994020af210ca)
- [ath9k: add ar9271 revision and subrevision ID helpers](http://git.kernel.org/linus/edb1f9152f1f346381336554674f5d443fc5f473)
- [ath9k: Add Bluetooth Coexistence 3-wire support](http://git.kernel.org/linus/1773912bd25196c2a3ca6c174574561363f43b2b)
- [ath9k: update kconfig to indicate support for AR9002 family](http://git.kernel.org/linus/2a219eb26793fc4c47b3ad7b84bded7b66f6e2c4)
- [ath: simplify kconfig dependency and add documentation](http://git.kernel.org/linus/b820b3bcb02a97091b969faf2b5f19f1218953f9)
- [b43: Add LP 2063 radio init](http://git.kernel.org/linus/c10e47f458653a68b1d3956237b7bf2e1ab1e8da)
- [b43: Add LP PHY Analog Switch Support](http://git.kernel.org/linus/9308779aad721cab8434fd5f98d3c85d3716fdec)
- [b43: Add LP-PHY firmware loading support](http://git.kernel.org/linus/759b973bb2d24adecaa526957435eabb00f02725)
- [b43: Add optional verbose runtime statistics](http://git.kernel.org/linus/990b86f4f9c54f83085d4136498ac44719b17654)
- [b43: Add Soft-MAC SDIO device support](http://git.kernel.org/linus/3dbba8e281552da640080f08a0f127d48456669f)
- [b43: Fix and update LP-PHY code](http://git.kernel.org/linus/68ec53292c7f09056152efa9a6ee2591c794f08c)
- [b43: Implement RFKILL status for LP PHY](http://git.kernel.org/linus/692e565e4b07ed872e6de5e1e3a6ae5b950e0369)
- [b43: LP-PHY: Implement channel switching for rev0/1/B2062 radio](http://git.kernel.org/linus/1e711bee566e26f03e51d5a754e7c8a57e489f9f)
- [b43: LP-PHY: Implement channel switching for rev2+/B2063 radio](http://git.kernel.org/linus/588f8377c5470fab611c14ead768f7f9af87da94)
- [b43: Make LP-PHY testable](http://git.kernel.org/linus/9d86a2d531c722feb0046e5a0b81809efb10422a)
- [b43: PCMCIA is not experimental anymore](http://git.kernel.org/linus/fd413da852991e96c555ad7253cc481bc133e221)
- [b43: Remove BROKEN attribute from SDIO](http://git.kernel.org/linus/4963cceea830f6afa65f0b921cfaff6765ac7748)
- [b43: Rewrite suspend/resume code](http://git.kernel.org/linus/a78b3bb2f3ab9afcf78dbcff18fd7bf900c7c27e)
- [b43: Use a threaded IRQ handler](http://git.kernel.org/linus/36dbd9548e92268127b0c31b0e121e63e9207108)
- [cfg80211: enable country IE support to all cfg80211 drivers](http://git.kernel.org/linus/8b19e6ca3bac7e04e93fb73f561d670e77c5fae6)
- [cfg80211: introduce nl80211 testmode command](http://git.kernel.org/linus/aff89a9b9084931e51b89d8f3ee3c547bea6c422)
- [cfg80211: make aware of net namespaces](http://git.kernel.org/linus/463d018323851a608eef52a9427b0585005c647f)
- [cfg80211: rework key operation](http://git.kernel.org/linus/fffd0934b9390f34bec45762192b7edd3b12b4b5)
- [cfg80211: self-contained wext handling where possible](http://git.kernel.org/linus/a9a11622c5c742c115fad371c0397ae86dd3bb67)
- [cfg80211: validate channel settings across interfaces](http://git.kernel.org/linus/59bbb6f7574bc693ed8313b98eac641116c95b94)
- [ieee802154: add a sysfs representation of WPAN master devices](http://git.kernel.org/linus/2bfb1070ba1fdb8cbc2b0b9ff61a3b0701ab40de)
- [ipw2x00: update contact information](http://git.kernel.org/linus/c1eb2c82e5ccc9b691f737c3150e746c9af3ffab)
- [iwlwifi: add thermal throttling support to 5150](http://git.kernel.org/linus/15993e08ac027b64b6f3400d32754966b4cac7b0)
- [iwlwifi: critical temperature enter/exit condition](http://git.kernel.org/linus/672639de13c4db92ed6a47e68043a4317e219902)
- [iwlwifi: disable PS by default](http://git.kernel.org/linus/b23da49e6db341f4721476394dd8b95e0be2d179)
- [iwlwifi: Handle new firmware file with ucode build number in header](http://git.kernel.org/linus/cc0f555d511a5fe9d4519334c8f674a1dbab9e3a)
- [iwlwifi: inform user about rfkill state changes](http://git.kernel.org/linus/4c423a2b0cc3c85137988962e6ba3f01baef0b4e)
- [iwlwifi: make debug level more user friendly](http://git.kernel.org/linus/a562a9dda7f47e7cac58d80bf1ffe441feca510e)
- [iwlwifi: Thermal Throttling Management - Part 1](http://git.kernel.org/linus/39b73fb15e4704fd4d1e33688135810637f5f3fb)
- [iwlwifi: Thermal Throttling Management - part 2](http://git.kernel.org/linus/46f9381aa3fb62f6a141bfd41dcbeda1ec5fa26e)
- [iwmc3200wifi: cfg80211 key hooks implemetation](http://git.kernel.org/linus/13e0fe70960e95cdea89b71aa3d046ec71efac8c)
- [iwmc3200wifi: cfg80211 managed mode port](http://git.kernel.org/linus/9967d46aa5ba065650d3352ab5d906f56ba17648)
- [libertas: Add support for Marvell Libertas CF8305](http://git.kernel.org/linus/9d45368a3825349d8ba686bc36df589d16577dd4)
- [mac80211: allow using network namespaces](http://git.kernel.org/linus/a272a720660059c30fa038113b77fa2a096437d9)
- [mac80211: cooperate more with network namespaces](http://git.kernel.org/linus/5061b0c2b9066de426fbc63f1278d2210e789412)
- [mac80211: driver operation debugging](http://git.kernel.org/linus/0a2b8bb24d4eb67788edd71d1ef8aa86c2e17e0f)
- [mac80211: Fix \[re\]association power saving issue on AP side](http://git.kernel.org/linus/1f08e84ff642294e42d138442a388989ffb20865)
- [mac80211: redefine usage of the mac80211 workqueue](http://git.kernel.org/linus/42935ecaf4e784d0815afa9a7e5fe7e141157ca3)
- [mac80211: remove deprecated API](http://git.kernel.org/linus/f424afa17899408cbd267a4c4534ca6fc9d8f71c)
- [mac80211: remove master netdev](http://git.kernel.org/linus/3b8d81e020f77c9da8b85b0685c8cd2ca7c7b150)
- [mac80211: Update mesh config IE to 11s draft 3.02](http://git.kernel.org/linus/9e03fdfd05e733e1136d431973625b174029c5e6)
- [MAINTAINERS: Add Atheros Linux wireless drivers home page](http://git.kernel.org/linus/72c706b775777e8ae546756a5d07ffda4a05ed7b)
- [MAINTAINERS: add information for mwl8k wireless driver](http://git.kernel.org/linus/a2c3f6567c9ac327f1ef1272551f3a7595ec885e)
- [MAINTAINERS: add information for wl1271 wireless driver](http://git.kernel.org/linus/5e68ff6563ef79d87296c70f8eb2bee454d3fe75)
- [MAINTAINERS: add wl1251 wireless driver](http://git.kernel.org/linus/834da346041cd8969897feea2cdb09269120599f)
- [net/compat/wext: send different messages to compat tasks](http://git.kernel.org/linus/1dacc76d0014a034b8aca14237c127d7c19d7726)
- [p54: implement rfkill](http://git.kernel.org/linus/6208f8b22cb24e446f24eb9f4aa9f4c3a9a1d52e)
- [p54usb: add Zcomax XG-705A usbid](http://git.kernel.org/linus/c3de943ad6e535ceb5238b3b7d3903c6e294061a)
- [p54usb: add Zcomax XG-705A usbid](http://git.kernel.org/linus/f7f71173ea69d4dabf166533beffa9294090b7ef)
- [rfkill: relicense header file](http://git.kernel.org/linus/8bc11b491b6cad75e737f1d38bb4b261bd95b291)
- [rt2x00: Add new RF chip defines](http://git.kernel.org/linus/05a32730f16e7b91e9fd2d11f26db152e5c9a68d)
- [rt2x00: move experimental on kconfig only to rt2800usb](http://git.kernel.org/linus/33172899a9d922b04081e12dced3ae474d46d620)
- [rt2x00: Thrustmaster FunAccess WIFI USB and rt73usb](http://git.kernel.org/linus/78bd6bbf3c12f49e2cb6897bfd73a62325ed3aaa)
- [rt2x00: use wiphy rfkill interface](http://git.kernel.org/linus/e47a5cddf893815e7da16e3226b959af785d8aaf)
- [rtl8187: Implement rfkill support](http://git.kernel.org/linus/ca9152e37f57259ca92486ca5753af16fd9155c6)
- [ssb: Implement SDIO host bus support](http://git.kernel.org/linus/24ea602e183ca20a7577ebe253323d0e5d0f9847)
- [wext: add back wireless/ dir in sysfs for cfg80211 interfaces](http://git.kernel.org/linus/8f1546cadf7ac5e9a40d54089a1c7302264ec49b)
- [wext: default to y](http://git.kernel.org/linus/898324025fc12132d3ed98f8baf4fb3fa45327e0)
- [wireless: default CONFIG_WLAN to y](http://git.kernel.org/linus/7ab44f17bc5b16ab1b4fc4dad4a0667c21e727b5)
- [wireless: default CONFIG_WLAN to y](http://git.kernel.org/linus/ff4d572a186c1276ea2118e405528432eb1f747c)
- [wireless: update cfg80211 kconfig entry](http://git.kernel.org/linus/b275f28535fc774325bb8ad5f664e6c44a8fbc9b)
- [wl1251: add sdio support](http://git.kernel.org/linus/3ec410d747fa1da035183c43775a64c0e285e399)
- [wl1271: add wl1271 to Kconfig and the Makefile](http://git.kernel.org/linus/30d742d5468c954969766bb0e809f218abc73af7)
- [wl12xx: add support for new WL1271 chip revision](http://git.kernel.org/linus/27797d68f70b28e77e6d183910dc7b3d7505105d)
- [wl12xx: rename driver to wl1251](http://git.kernel.org/linus/c5ce901b3fdb2312f896f138ac864a7ef363c02d)
- [zd1211rw: adding Accton Technology Corp (083a:e501) as a ZD1211B device](http://git.kernel.org/linus/8f75e07aa14107668d33f60fa4d78afa2d7aa22b)

**Various other commits**

- [at91sam9263: add at91_can device to generic device definition](http://git.kernel.org/linus/58a587dc2abd436a6a8d0de729d9ed7e40ce0ac9)
- [Bluetooth: Add configuration support for ERTM and Streaming mode](http://git.kernel.org/linus/f2fcfcd670257236ebf2088bbdf26f6a8ef459fe)
- [Bluetooth: Add initial support for ERTM packets transfers](http://git.kernel.org/linus/1c2acffb76d4bc5fd27c4ea55cc27ad8ead10f9a)
- [Bluetooth: Add support for FCS option to L2CAP](http://git.kernel.org/linus/fcc203c30d72dde82692f6b761a80e5ca5fdd8fa)
- [Bluetooth: Add support for L2CAP 'Send RRorRNR' action](http://git.kernel.org/linus/7e7430908c3ccaf71f0851050c8ccaf9ecfb3b56)
- [Bluetooth: Add support for L2CAP SREJ exception](http://git.kernel.org/linus/8f17154f1f70fcc6faa31ac82164fcf7f0599f38)
- [Bluetooth: Add support for Retransmission and Monitor Timers](http://git.kernel.org/linus/e90bac061b17cd81bd0df30606c64f4543bf5ca0)
- [Bluetooth: Add support for Segmentation and Reassembly of SDUs](http://git.kernel.org/linus/c74e560cd0101455f1889515e1527e4c2e266113)
- [Bluetooth: Enable Streaming Mode for L2CAP](http://git.kernel.org/linus/6840ed0770d79b9bb0800e5e026a067040ef18f5)
- [Bluetooth: Improve USB driver throughput by increasing the frame size](http://git.kernel.org/linus/290ba200815fdecb4d40dc942499c4ea6d0c4624)
- [Documentation: expand isdn/INTERFACE.CAPI document](http://git.kernel.org/linus/f1af9f58546e2d98ef078fa30b2ef80a9042131e)
- [genetlink: make netns aware](http://git.kernel.org/linus/134e63756d5f3d0f7604dfcca847b09d1b14fd66)
- [ieee802154: add support for channel pages from IEEE 802.15.4-2006](http://git.kernel.org/linus/16eea493da563b5a3356a77c6d8776dffc29d3b6)
- [net: Add patchwork URL to MAINTAINERS](http://git.kernel.org/linus/d1f6803a58e827fda7b810dcb7cbdb490d32ab9e)
- [net/bridge: Add 'hairpin' port forwarding mode](http://git.kernel.org/linus/3982d3d28b02bed5312015762fe2112ccbaf9051)
- [net: force bridge module(s) to be GPL](http://git.kernel.org/linus/4fb019a01a7f67342d4a88d26c0817afe392c669)
- [pktgen: Fix multiqueue handling](http://git.kernel.org/linus/896a7cf8d846a9e86fb823be16f4f14ffeb7f074)
- [RDS/IB: Handle connections using RDS 3.0 wire protocol](http://git.kernel.org/linus/02a6a2592e41d27644d647f3bce23598649961bc)
- [rfkill: add the GPS radio type](http://git.kernel.org/linus/3ad201496badddd8e1cda87ee6d29e8b3b8e1279)

For other articles on 2.6.32 and links to the rest of the "Coming in 2.6.32" series, see [The H's Kernel Log - 2.6.32 Tracking](../site/open/features/2-6-32-Tracking-816707.html "2.6.32 Tracking – 05 October 2009, 17:04") page.

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
