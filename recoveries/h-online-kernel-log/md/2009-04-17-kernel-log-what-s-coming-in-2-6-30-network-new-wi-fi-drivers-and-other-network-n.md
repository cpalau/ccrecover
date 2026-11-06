---
title: "Kernel Log: What's coming in 2.6.30 - Network: New Wi-Fi drivers and other network novelties"
date: 2009-04-17
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-What-s-coming-in-2-6-30-Network-New-Wi-Fi-drivers-and-other-network-novelties-741197.html
pages: 1
---

# Kernel Log: What's coming in 2.6.30 - Network: New Wi-Fi drivers and other network novelties

**Dj Walker-Morgan**

![Kernel Log Penguin](../site/imgs/43/3/6/7/6/2/9/93e8ea3d0acdf147.jpg) The next major Linux version will include new Wi-Fi drivers for chips from Atheros, Intel, Intersil/Prism and Marvell and new drivers for Intel LAN chips. The kernel will also in future make better use of energy saving features in the latest Wi-Fi hardware and Oracle is contributing code for the Reliable Datagram Sockets (RDS) cluster protocol.

As with previous kernel versions, the recent [release](http://thread.gmane.org/gmane.linux.kernel/822502) of the second pre-release version of Linux 2.6.30 saw a good few major patches which had missed the merge window find their way into the main Linux development tree. Further major changes are rare in the second phase of the development cycle, so that the second pre-release version should now contain all the major changes for the next major kernel revision.

The Kernel Log on The H is taking the opportunity to open the "What's coming in 2.6.30" series with a description of the major networking-related changes and will be extended with further instalments over the next few weeks, building up to a detailed description of all the major changes in 2.6.30 in the various functional areas within the Linux kernel, until Linus Torvalds releases Linux kernel 2.6.30 in around seven to ten weeks time.

**Code recycling**

In version 2.6.30, Linux will for the first time include the [ar9170](http://wireless.kernel.org/en/users/Drivers/ar9170) Wi-Fi driver for Atheros' eponymous 802.11n USB chip set ([1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=23b53f4f55d833ecc5a11b5fba646c78d3876927), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e9348cdd280eb6a1d6d38fef513b578dc9ead363), [3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6cb19353535f9f02fc2a753e3261a255406ba8fa), [4](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b63a2cb30405777033d58045c562a3b04d87d702), [5](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=75ca88c9701bf8f65fc1f009f10dd64b0378b977), [6](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=de00c04ecbb482507ace2197782123446a1cfdca)). The driver is brand spanking new, but re-uses some of the code from Atheros' [otus driver](http://wireless.kernel.org/en/users/Drivers/otus), which was released [a few months](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-6-Changes-to-the-audio-drivers-739369.html "Kernel Log: What's coming in 2.6.28 - Part 6: Changes to the audio drivers – 15 December 2008, 17:53") ago. The latter was added to the staging area in Linux 2.6.29; in the opinion of some Wi-Fi driver developers, however, re-jigging and improving the staging driver to meet kernel hacker quality standards would have taken more work than writing a new driver tailored to the kernel's Wi-Fi stack, resulting in the development of the new driver.

Also [making its debut](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a66098daacee2f354dab311b58011e7076aa248c), driven largely by Marvell developers, is the [mwl8k](http://wireless.kernel.org/en/users/Drivers/mwl8k) driver for Marvell 88w8xxx (Topdog) series PCI and PCIe Wi-Fi chips. Currently, however, it only supports the 88w8687 Wi-Fi chip in STA mode on channels 1 to 11. Also still some way off technical maturity is the [new](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1264b951463a00efebe1bb596499aaad620ec8af) [at76c50x-usb](http://wireless.kernel.org/en/users/Drivers/at76c50x-usb) driver for Atmel's old at76c503, at76c505 and at76c505a Wi-Fi chips. In the long term it is intended to replace the [at76_usb](http://wireless.kernel.org/en/users/Drivers/at76_usb) driver, which was incorporated into the kernel's staging area in 2.6.28. As with otus and ar9170, some of the old driver code has found its way into the new driver, which is based on the kernel's Mac80211 Wi-Fi stack.

**Clean up work and energy saving functions**

To simplify maintenance, the kernel development team has combined parts of the [iwl3945](http://wireless.kernel.org/en/users/Drivers/iwl3945) driver with the files for drivers for newer Intel Wi-Fi chips (e.g. [1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=775a6e27bfca9d19f3ea6006a7e60a4a54aaf69c), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=77fecfb88f8ad64420e06a96f1bd3b38498bfb4f), [3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d25aabb0a1a2f659206ba21f6ac8ec28047e5595), [4](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7dc45f25d39ea959fdc1d5f636e9fc6cbe7ac7e0)). The latter have been extended to include support for Intel's 1000, 6000 and 6050 Wi-Fi chips ([1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2264596d6d0a5c1e569af809625c11f8f2d89435), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e1228374d648efe451973bc5f3d1f9a8e943ec0b), [3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c5d0569882b9c264be31dcb0758961bfc479deea), [4](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=77dcb6a9526b1e0d159a9300e512c7271bff3163)).

The kernel hackers have also improved support for runtime energy saving features in modern Wi-Fi hardware in both the Mac80211 Wi-Fi stack and in some drivers (e.g. [1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4be8c3873e0b88397866d3ede578503e188f9ad2), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a97b77b90decf27a86ac40ea53a741ffb5ead21a), [3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=869717fbe43eb831cbebd03a9a66a4a4c3b406a9); further commits can be found in the list at the end of this article). There have also been enhancements to the code for suspending to, and resuming from, RAM and disk.

**Wired**

The kernel development team have added support for the Generic Receive Offload (GRO) infrastructure, [introduced in 2.6.29](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-1-Dodgy-Wifi-drivers-and-AP-support-739619.html "Kernel Log: What's new in 2.6.29 - Part 1: Dodgy Wifi drivers and AP support – 11 January 2009, 16:08"), to many LAN drivers. These include the [igbvf](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d4e0fe01a38a073568aee541a0247fe734095979) network driver for Intel's 82576, [ethoc](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a1702857724fb39cb68ce581490010df99168fd0) for OpenCores' 10/100 Mbit LAN Chip and vxge for Neterion's X3100 series 10GbE PCIe I/O Virtualized Server adapters (e.g. [1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=40a3a9156dc66f23cc79758981886c1896887341), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f1782852adb57c8daf76a56146424f6c2f7410b6), [Documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5adfb64bdd4eee07e0677cbad12a2f80fecc6715)).

Also new in 2.6.30 is code introduced by one Oracle developer ([Documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0c5f9b8830aa0ff8f97e4efdfe1e1c4fe08ec71c)) to provide support for the Reliable Datagram Sockets ([RDS](http://oss.oracle.com/projects/rds/)) server cluster protocol. This was originally developed jointly by Cisco Systems and Oracle, before being transferred to the Open Fabrics Alliance software stack.

**In Brief**

*LAN*

- Having offloaded the firmware code for many network drivers into separate files in 2.6.27, .28 and .29, the kernel developers are continuing the process in 2.6.30.

*Wi-Fi*

- The new [libertas_spi](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d2b21f191753abd12c4063776cb1a3d635397509) drivers for the Marvell 8686 and the experimental [p54spi](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cd8d3d321285a34b4e29cb7b04e552c49cc0f018) driver for Prism's stlc4550 and stlc4560 chips, designed for Nokia's N800 and N810 devices, are tailored to Wi-Fi chips with SPI ([Serial Peripheral Interface](http://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus)).
- Cfg80211 and nl80211 now include autonomous support for [scanning for Wi-Fi networks](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2a5193119269062608582418deba7af82844159a).

*Netfilter*

- The packet filter code now offers a userspace interface allowing packets to be [time stamped](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cb9eff097831007afb30d64373f29d99825d0068).

*Miscellaneous*

- Bluetooth: Kernel hackers have [adapted](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8c1b235594fbab9a13240a1dac12ea9fd99b6440) the Bluetooth stack security model for the changes made in Bluetooth 2.1, as a result of which the kernel can now utilise [Secure Simple Pairing](http://www.bluetooth.com/NR/rdonlyres/0A0B3F36-D15F-4470-85A6-F2CCFA26F70F/0/SimplePairing_WP_V10r00.pdf)![PDF](../site/icons/file-pdf.gif "PDF document").

**Minor gems**

The changes described are just some of the more significant changes recently undertaken by kernel hackers in the networking field. The following list includes numerous further major commits for 2.6.30 in the main Linux development tree; the links lead directly to the Git version control system [web interface](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=summary), where comments on the commits and patches themselves provide wide-ranging information on the less important, but far from insignificant, changes.

**Network**

Most relevant Git-Pull-Request:

- Network: [1](http://thread.gmane.org/gmane.linux.network/123690), [2](http://thread.gmane.org/gmane.linux.network/123953), [3](http://thread.gmane.org/gmane.linux.network/124061), [4](http://thread.gmane.org/gmane.linux.network/124761), [5](http://thread.gmane.org/gmane.linux.network/124915)

<!-- -->

- Infiniband: [1](http://thread.gmane.org/gmane.linux.drivers.openib/61631)

***LAN***

- [3C359: use request_firmware](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4b6ece97e0b61306d4b8de6820f602e4cf5d8d6b)
- [bnx2: Use request_firmware()](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=57579f7629a3d46c307405fbd2ea6bdb650d692f)
- [bnx2x: MSI support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8badd27aa0d7c02572fcd1a4a3c6b57d67f40b78)
- [bnx2x: Multi-queue](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=555f6c78373f969f14487253abe331d085449360)
- [bnx2x: New FW](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8d9c5f34a25d6a30d15a800d83a3428ad44271d8)
- [bnx2x: Register dump](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0a64ea57486acd9e17b80bb70b966e81d904b61c)
- [bnx2x: Supporting BCM8726 PHY](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=589abe3a0f594a7707a15674ca9e80370c972832)
- [bnx2x: Supporting new BCM8726 FW](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cc1cb004dfa27c63b43941076b490045a43d5fbd)
- [cxgb3: Replace LRO with GRO](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7be2df451fa916f93e37763a58d33483feb0909f)
- [dsa: add support for the Marvell 88E6095/6095F switch chips](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=076d3e10a54caa2c148de5732c126c7a31381d48)
- [dsa: add switch chip cascading support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e84665c9cb4db963393fafad6fefe5efdd7e4a09)
- [e1000e: add aer support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=111b9dc5c981ba608b4afede37237cfeb67b07f2)
- [e1000e: add support for 82574 device ID 0x10F6](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bef28b11597a4da9ef3b8a51776b8cb14b427e5e)
- [e1000e: add support for 82583 device id](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8c81c9c315b7e7e240906fab0e8dde1595101bd2)
- [e1000e: Invoke VLAN GRO handler](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c405b828161286729b6a5a729159114dca122923)
- [e100: add support for 82552 10/100 adapter](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b55de80e49892002a1878013ab9aee1a30970be6)
- [fec: Add support for Freescale MX27](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=196719ecec0c526de273dcb902f0be956a193232)
- [forcedeth: add new optimization mode](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9e184767c956e71d9535c9fc8433e140f819d07d)
- [forcedeth: enable msix to default](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=394827913e371b058849349c6fc9d52c59c31a3d)
- [forcedeth: remove msix + napi](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d41c628c514bceb33037c26f83585c629594bed5)
- [igb: add support for 82576 quad copper adapter](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c8ea5ea9da338d6af015148105f07fc35eda8a92)
- [igb: add support for another dual port 82576 non-security nic](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9eb2341d0df6e5d33508008879987bf5bb146804)
- [igb: Add support for enabling VFs to PF driver.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4ae196dfd61d06b061c069edcdd7c73121e60a21)
- [igb: remove LRO Kconfig option](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5fbbcb79e5371d99565826a352c1003d0f1f0678)
- [igb: Replace LRO with GRO](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5c0999b72b34541a3734a9138c43d5c024a42d47)
- [ixgbe: Add 82598 support for BX mezzanine devices](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2f21bdd3542838dc5513a585a32aa13f01b019e7)
- [ixgbe: Add 82599 device id's, hook it up into the main driver.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e8e26350f114fa212e277ea02332d9347c59865d)
- [ixgbe: Add DCB for 82599, remove BCN support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=235ea828a1640ed493562a5fe08aa666ff84fbc4)
- [ixgbe: Add documentation for the driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=09e1c061484005aa26264c3f82f2c83a273c4094)
- [ixgbe: Add hardware specific initialization code for 82599 devices](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=11afc1b1fd802c11dc0fa986c210602c177f1e21)
- [ixgbe: add support KX/KX4 device](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1e336d0fc99f159ed636ffb9128bc84e09ccc279)
- [ixgbe: Replace LRO with GRO](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=78b6f4ce58d1c85190003840912cc9097cbb8146)
- [mlx4_core: Add device IDs for MT25458 10GigE devices](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=085343b47592b33276abf58a71c52ea29f0a338b)
- [mv643xx_eth: implement Large Receive Offload](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=eaf5d59092dbed853bfab956ce123293832998f5)
- [mv643xx_eth: make LRO unconditional](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ab307a3983a7fa28f260f3123293c7b91d5d629e)
- [net: Add support for the OpenCores 10/100 Mbps Ethernet MAC.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a1702857724fb39cb68ce581490010df99168fd0)
- [niu: Add GRO support.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4099e01224e2afcaeea439cd92db3e7cf6e0f84f)
- [phy: add new LAN8710 and LAN8720 device ids to smsc phy driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e072b639dc13b06b65be487633dad9bb3d2067d5)
- [qlge: Add support for device ID 8000.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cdca8d02ea4229c2ccf3c27fb537b150843f67c9)
- [qlge: Add support for GRO.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=22bdd4f599b87734b7fc8137f47e62c13ab27e93)
- [sfc: Add support for QT2025C PHY](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d2d2c3731474614bff5cf47a605e59e847882f5d)
- [sfc: Add support for SFN4112F SFP+ reference design](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=94f52cd152ce20aa72415bcf0804faee0d31d023)
- [sfc: Replace LRO with GRO](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=da3bc07171dff957906cbe2ad5abb443eccf57c4)
- [tehuti: Use request_firmware()](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=06e1f9ffa023c030bc87491e75f625f5da4e7d97)
- [tg3: Add GRO support.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1383bdb98c01bbd28d72336d1bf614ce79114d29)
- [typhoon: Use request_firmware()](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b775a750c3afacbfac884537d466d34d50b1023b)
- [virtio_net: Add a MAC filter table](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f565a7c259d71cc186753653d978c646d2354b36)
- [virtio_net: Add support for VLAN filtering in the hypervisor](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0bde95690d65653e420d04856c5d5783155c747c)
- [yam: use request_firmware](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a7a5eb9d4eb9908709df66e8f8f1724b5b108258)

***Wi-Fi***

- [Add mesh point functionality to ath9k](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9cb5412b0760981d43ac3e612992c90cea690e72)
- [Add new rt73usb USB ID](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=964d6ad935d96a002fdbbdfcac38f02a084f75d9)
- [ath5k: Add tx power calibration support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8f655dde240293f3b82313cae91c64ffd7b64c50)
- [ath5k: support LEDs on Acer Aspire One netbook](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=63649b6cf0a964582af2b4d4734e28ca90ec8f5c)
- [ath5k: Support LED's on Acer Extensa 5620z](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=af83debf5bb44257082d4489ac86123a0cadf6d3)
- [ath9k: Add support for multiple virtual AP interfaces](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4ed96f04f8a1869757f4dd4a9283a18ec63c442f)
- [ath9k: Enable Bluetooth Coexistence support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c97c92d92715ea4ea2d7cf00957e8a014439bdd8)
- [ath9k: Enable dynamic power save in ath9k.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3cbb5dd73697b3f1c677daffe29f00ace22b71e9)
- [ath9k: enable support for AR9100](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0c1aa495961f03c964b3287cf5800217cf6f2cee)
- [b43: Add BCM4307 PCI-ID](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=dd970e43d86c253ff159d9668499aaf42d175722)
- [b43: Add LP 2062 radio init](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=24b5bcc6aef46346edd69becf62d2125c0b3208e)
- [b43: Add parts of LP-PHY TX power control](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ce1a9ee33a5864f3d199baa1d3e154a1f9a6f3dd)
- [b43: Automatically probe for opensource firmware](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1a9f509368ceb24fc66be961be15c69966f5eb5d)
- [b43: Change schedule for old-fw support removal](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c557289cb8ea063bd09db88f8a687a841556e291)
- [b43: detect N PHY revision/radio](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bb519bee07eed4fac9921ad658fb1f7ed78defb5)
- [b43/ssb: Add SPROM8 extraction and LP-PHY detection](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6b1c7c67603efdf0b39f6056989b0f8194cdc1f3)
- [cfg80211: add PM hooks](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0378b3f1c49d48ed524eabda7e4340163d9483c9)
- [cfg80211: add regulatory netlink multicast group](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=73d54c9e74c4d8ee8a41bc516f481f0f754eca32)
- [cfg80211: Allow for strict regulatory settings](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f976376de0d6a9697fb635369f12ae00251f4566)
- [cfg80211: default CONFIG_WIRELESS_OLD_REGULATORY to n](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8a5117d80fe93de5df5b56480054f7df1fd20755)
- [iwl3945: use rx queue management infrastructure from iwlcore](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=51af3d3fbbe326077a7e245268a7de325de6ecd2)
- [iwlwifi: Fix and rework Kconfig file](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=80bc53931bdf8284c5a95ba96d86ab6c2473a5f8)
- [iwlwifi: support 11h](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b1c6019bc0fe829309258d888f47d9ae54353039)
- [iwlwifi: update 5150 API version to support new firmware](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=39e6d2256b8b8265ef16297887b5521f3e0155c6)
- [mac80211: 802.11w - Add BIP (AES-128-CMAC)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=765cb46a3fc856245ea68a7c961ac87c77e4ae2d)
- [mac80211: 802.11w - Use BIP (AES-128-CMAC)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3cfcf6ac6d69dc290e96416731eea5c88ac7d426)
- [mac80211: Add 802.11h CSA support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c481ec9705d4a5d566393bc17374cfd82c870715)
- [mac80211: add beacon filtering support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=04de83815993714a7ba2618f637fa1092a5f664b)
- [mac80211: Add documentation bits for mac80211_rate_control_flags](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2134e7e724798cf8d54ae822afe235abb607d9b2)
- [mac80211: add suspend/resume callbacks](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=665af4fc8979734d8f73c9a6732be07e545ce4cc)
- [mac80211: disable power save when scanning](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9050bdd8589c373e01e41ddbd9a192de2ff01ef0)
- [mac80211_hwsim: add support for 5 GHz](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=22cad73587ac85e2e9d1f52aae62023aec093654)
- [mac80211: resume properly, add suspend/resume test](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=827b1fb44b7e41377a5498b9d070a11dfae2c283)
- [p54: enable power save support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=94041b294094bbd9fbbe11aa71278fdc70d29d6d)
- [p54: initial SoftLED support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d0b45aef4f628e69f8da8c670d6879a8a02fe0f2)
- [p54: power save management](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2b8d4e2eea711b6dfe1878ff3c94ebe757656f6d)
- [rt2x00: Add mesh support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a07dbea210e146aedf8929cdabe082b58696260c)
- [rt2x00: Add RFKILL support to rt2500usb and rt73usb](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7396faf4f3228b88c6c815c7a93081b456716d5f)
- [rt2x00: Add various new USB IDs for rt73usb](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=144d9ad98ef90072fd939e620f374d6918155a06)
- [rt2x00: Implement Powersaving](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7d7f19ccb777946df0a8fb7c83189ba2ae08b02e)
- [rt2x00: New USB ID for rt73usb](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=14344b81ec264efbe59de0183f5ba38650a479a6)
- [rt2x00: Release rt2x00 2.3.0](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=754be3098b22d1bea9620b40fe2f9f2286c55101)
- [rt2x00: Replace RFKILL with INPUT](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cca3e99861e883358ceb39ad17c9eaee082138a5)
- [rt2x00: Update MAINTAINERS entry: new mailinglist](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6d5eaafa558783a669bb46c3dba902370e8f0ffc)
- [ssb/b43: add new N PHY device](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=92d6128e1766bb7a7b6dc58f012fdf772fdf1100)
- [wireless: Add channel/frequency conversions to ieee80211.h](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9ee677c2276bfcbcf68042ec2718a504af0c5fd7)

***RDS***

- [RDS: Add iWARP support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fcd8b7c0ecf792dd824b2edcd63cb2c08563c340)
- [RDS: Add MAINTAINERS entry](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a09ed661f756d3209a19271192abe9b892b59c7d)
- [RDS: Add userspace header](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=db49b9d26c1966c683efced9e1c37f391d8f8182)
- [RDS: Common RDMA transport code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=55b7ed0b582f9ff4bf3b9b44969cddda8c6763ea)
- [RDS: Connection handling](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=00e0f34c616603ba6500f41943cbf89eb4a8a5be)
- [RDS/IB: Infiniband transport](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ec16227e14141e4fd7ae76354c09dadfe2449d9e)
- [RDS: Kconfig and Makefile](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fe17f84f5f2a7d6c1a31c04c06a016d4ad5f7dec)
- [RDS: Main header file](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=39de8281791c4a01abcb0d32879530ffa5863c01)
- [RDS: RDMA support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=eff5f53bef75c0864a5da06bb688939092b848dc)
- [RDS: Socket interface](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=639b321b4d8f4e412bfbb2a4a19bfebc1e68ace4)
- [RDS: Transport code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0fbc78cbf51f3edee17c2ede42c7b3c13736158a)

***Others***

- [gigaset: documentation update](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c69c6d107ab18e330f22f9380da353fed29c296b)
- [IPoIB: Document newish features](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6a3335b43342b42dd6c69b4bbbde15d622cb49ca)
- [RDMA/nes: Add support for new SFP+ PHY](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4303565df4eb425851ddd22136fec69bdfeede61)
- [RDMA/nes: Add wide_ppm_offset parm for switch compatibility](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a4849fc157cdbe4fb68cfe37e7222697f003deb5)
- [wimax/i2400m: implement RX reorder support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c747583d19d5d5147a9f0eae480c1fdbc84c4252)
- [wimax/i2400m: support extended data RX protocol (no need to reallocate skbs)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fd5c565c0c04d2716cfdac3f1de3c2261d6a457d)

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the Kernel Log at The H Open Source:*

- [Kernel Log: Linux 2.6.30 is taking shape](../site/news/item/Kernel-Log-Linux-2-6-30-is-taking-shape-741093.html "Kernel Log: Linux 2.6.30 is taking shape – 09 April 2009, 06:41")
- [Kernel Log: Development of 2.6.30 is under way](../site/news/item/Kernel-Log-Development-of-2-6-30-is-under-way-740805.html "Kernel Log: Development of 2.6.30 is under way – 27 March 2009, 17:33")
- [Steady Growth: What's new in Linux 2.6.29](../site/open/features/Steady-growth-What-s-new-in-Linux-2-6-29-746553.html "Steady growth - What's new in Linux 2.6.29 – 24 March 2009, 15:26")
- [Kernel Log: Tasmanian devil to be Linux's temporary mascot, new Radeon drivers](../site/news/item/Kernel-Log-Tasmanian-devil-to-be-Linux-s-temporary-mascot-new-Radeon-drivers-740667.html "Kernel Log: Tasmanian devil to be Linux's temporary mascot, new Radeon drivers – 19 March 2009, 15:43")

*Older Kernel logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
