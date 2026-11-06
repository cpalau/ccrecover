---
title: "Kernel Log: Coming in 2.6.33 (Part 1) - Networking"
date: 2010-01-08
author: "Chris von Eitzen"
source: http://www.h-online.com/open/news/item/Kernel-Log-Coming-in-2-6-33-Part-1-Networking-898841.html
pages: 1
---

# Kernel Log: Coming in 2.6.33 (Part 1) - Networking

**Chris von Eitzen**

#### ![Kernel Log Logo](../site/imgs/43/4/6/4/4/0/7/KL.jpg-1f663d67fe8a53b0.jpeg) by Thorsten Leemhuis

**Linux 2.6.33 will have new and improved drivers for Wi-Fi chips by Intel, Ralink and Realtek. Several drivers for old Wi-Fi hardware have been moved to the staging area and will probably soon be discarded. New additions include various LAN chip drivers and several improvements to the network stack.**

On Tuesday night, Linus Torvalds [released](http://thread.gmane.org/gmane.linux.kernel/934810) Linux 2.6.33-rc3, the third release candidate of Linux version 2.6.33. The forthcoming version is expected to be finalised in early March and this release candidate offers a smaller number of changes than is usual at this point in the development cycle – it seems that some of the kernel hackers took some time off over Christmas.

However, most of the important new features of the next version in the Linux main development line were already integrated by Torvalds and his fellow programmers in the "merge window" phase at the start of the development cycle. As it is uncommon for newly integrated items to be discarded again in the current second phase, the Kernel Log can already provide a comprehensive overview of the most important new features of Linux 2.6.33.

To avoid being swamped by the wealth of advancements, the Kernel Log will provide the overview in its usual multi-part series of articles that together discuss the kernel's various functional areas. The first part of the "Coming in 2.6.33" series deals with the most important changes to the kernel's network support. Articles discussing the Linux kernel's storage hardware, file systems, graphics support, architecture code, drivers and other functional areas will follow over the next few weeks preceding the release of version 2.6.33 of the Linux kernel.

### Wireless

The iwlwifi driver can now address various, previously unsupported Intel series 1000, 5000 and 6000 Wi-Fi modules ([1](http://git.kernel.org/linus/4bd0914fa2a09d655c54fb0355aed7f9182b2187), [2](http://git.kernel.org/linus/ac592574a577162183b5c1dd040a188caa068a29), [3](http://git.kernel.org/linus/5953a62e7df064a5d7ba7e790d590f27c65ddf4c)) and now also supports the WiMAX function of the 6x50 series ([1](http://git.kernel.org/linus/7329012e673231dee9a21567cfb9881f5ea462ba), [2](http://git.kernel.org/linus/1933ac4d9377ed44caba45abe1531ec1bc14bb63)). A new addition is the "[Intel Wireless MultiCom 3200 top driver (iwmc3200top)](http://git.kernel.org/linus/ab69a5ae2bdc0b5e20e935a7b75f30aa3f4c3bae)" for a new Intel wireless chip that supports GPS, Bluetooth, Wi-Fi and WiMAX. The power saving features of the iwl3945 Intel Wi-Fi driver have been [temporarily disabled](http://git.kernel.org/linus/bc45a67079c916a9bd0a95b0b879cc0f259bac6e) due to some problems.

The kernel developers have also added the [rt2800pci](http://git.kernel.org/linus/a9b3a9f7214b3acc56330c2257aeaa5fa85bf520) driver, which is still considered ["very experimental", "intended for developers" and "non-functional"](http://git.kernel.org/linus/f44eafa76be981b57667adcef5153b18e8a21904) at this point in the development cycle and addresses Ralink's RT2760, RT2790, RT2860, RT2880, RT2890 and RT3052 PCI Wi-Fi chips frequently found in recent netbooks and notebooks. These chips could previously only be used with a driver developed by the vendor which was in the kernel's staging area for a few months. The staging area is the kernel area for drivers of insufficient quality or maturity. However, some distributions don't include the staging drivers and the drivers, with their separate Wi-Fi stack, occasionally have problems when interacting with configuration tools, such as the Network Manager. So the Ralink drivers, although not a proper solution, were better than nothing. Initially it's likely the situation will be the same for the rt2800pci driver.

The new driver was mainly developed by the [rt2x00](http://rt2x00.serialmonkey.com/) project which also maintains other drivers for Ralink chips. Several more of the project's drivers were improved for 2.6.33 and now support a greater variety of USB Wi-Fi hardware than ever – more details can be found via the links mentioned under "Minor gems" at the end of this article. The [new support](http://git.kernel.org/linus/f273fe55e3f3f0b66b7624c0102d3ef44bbdfe6a) of Ralink's RT3070 Wi-Fi chip in the rt2800usb driver is also classified as "[non-functional at the moment](http://git.kernel.org/linus/71eafe3230073917456973d67bc49eaa874c5a42)" – but the developers have already [prepared patches](http://thread.gmane.org/gmane.linux.kernel.wireless.general/45212) for the two rt2800 drivers which could still make it into 2.6.33 and get the drivers into a "usable state".

The kernel hackers have incorporated the rtl8192u driver for Realtek's chips of the same name into the staging area. Furthermore, the [arlan](http://git.kernel.org/linus/e38879efd336fb78b288dcebdc9ca030fd24f449), [netwave](http://git.kernel.org/linus/4b5783549730da21d88b41dce9a2b738afa44abc), [strip](http://git.kernel.org/linus/955015bb0b42167d14f776ff5947ae2463a974dc) and [wavelan](http://git.kernel.org/linus/0234f84ebb00d36c48062befa5436eef36b71ccd) drivers have been moved to the area for low-quality drivers because they are based on the Linux kernel's MAC80211 Wi-Fi stack and, according to the kernel developers, are now hardly used by anyone – therefore, they are currently not considered worth the effort of porting them to the new Wi-Fi stack. If no one comes forward to maintain these drivers they are destined to be removed in Linux 2.6.35.

### LAN, network stack etc

Further changes in the network subsystem:

- The sfc driver now supports the SFL9021 'Siena' and SFC9020 'Bethpage' 10 Gigabit ethernet controllers from Solarflare's SFC9000 series ([1](http://git.kernel.org/linus/afd4aea03f597f29421dc5767e7d1f754730ec23), [2](http://git.kernel.org/linus/8880f4ec21e668dcab3c6d387524a887e5bcbf73)).
- A new addition is the [octeon_mgmt](http://git.kernel.org/linus/d6aa60a10b2f5068e331ca2936b1e6c248ae37c1) LAN driver for CN57XX, CN56XX, CN55XX, CN54XX, CN52XX and CN6XXX Octeon chips by Cavium Networks.
- The bnx2x driver now also supports Broadcom's BCM8481/BCM84823 and BCM84823 chips ([1](http://git.kernel.org/linus/46d15cc7a09d6a7f96908b2cd812744c483893b4), [2](http://git.kernel.org/linus/4f60dab113230943fb1bc7969053d9a1b6578339)) and offers extended iSCSI support when combined with the cnic driver ([1](http://git.kernel.org/linus/37b091bacba7bd329eced9a56998b6247da414c4), [2](http://git.kernel.org/linus/e251306556d30c9c678feca60204acaaa0784cbd), [3](http://git.kernel.org/linus/71034ba845c9ff219373066f904286c0b7506922)).
- The [new recvmmsg socket syscall](http://git.kernel.org/linus/a2e2725541fad72416326798c2d7fa4dafb7d337) allows multiple messages to be received, which reduces processing workloads (see also the [short description at LWN.net](http://lwn.net/Articles/334854/)).
- The new [TCP Cookie Transactions](http://www.usenix.org/publications/login/2009-12/openpdfs/metzger.pdf)![PDF](../site/icons/file-pdf.gif "PDF document") are designed to make initialising TCP connections faster, more secure and more robust ([1](http://git.kernel.org/linus/e6b4d11367519bc71729c09d05a126b133c755be), [2](http://git.kernel.org/linus/da5c78c82629a167794436e4306b4cf1faddea90), [3](http://git.kernel.org/linus/519855c508b9a17878c0977a3cdefc09b59b30df), [4](http://git.kernel.org/linus/435cf559f02ea3a3159eb316f97dc88bdebe9432), [5](http://git.kernel.org/linus/e56fb50f2b7958b931c8a2fc0966061b3f3c8f3a), [6](http://git.kernel.org/linus/bd0388ae77075026d6a9f9eb6026dfd1d52ce0e9), [7](http://git.kernel.org/linus/4957faade11b3a278c3b3cade3411ddc20afa791)).

The first Git-Pull request by network subsystem maintainer David S. Miller alone caused [more than 1800 changes](http://thread.gmane.org/gmane.linux.network/145967) to be integrated into Linux 2.6.33 – this means that about a fifth of all the commits incorporated during the merge window of 2.6.33 have been handled by Miller, who also maintains the old IDE subsystem and the Sparc code. While the majority of changes modify C source code, some of the changes adapt the firmware that comes with the kernel and considerably increase the total number of new, deleted or moved lines of source code – this is very evident with two patches of about 1 MB each which update the firmware of the bnx2x driver ([1](http://git.kernel.org/linus/52a7a12fb560f22dd093ca74f3a768d51b044a40), [2](http://git.kernel.org/linus/69dc2df3aaee2ce5e875b14b7271436559be9a95)).

### Minor gems

Many further minor, but by no means insignificant, changes can be found in the list below, which contains the commit headers referring to the respective change. Like many of the references in the text above, the links point to the relevant commit in the [web front end](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git&a=summary) of the Git branch for the kernel sources maintained by Linus Torvalds at kernel.org. The commit comments and the patches themselves provide extensive further information on the respective changes.

**LAN**

- [atl1e: Allow TX checksum offload and TSO to be disabled and reenabled](http://git.kernel.org/linus/ac936929092dc6a5409b627c4c67305ab9b626b3)
- [be2net: Add support for ethtool self test](http://git.kernel.org/linus/ff33a6e2ab97f4cde484cdf1a41778af6d6b7cff)
- [be2net: Add support for next generation of BladeEngine device.](http://git.kernel.org/linus/12d7ea2c5a5c87834daf9fcd920aab80ff6248b1)
- [be2net: Add the new PCI IDs to PCI_DEVICE_TABLE.](http://git.kernel.org/linus/59fd5d87a4243a992f3a3e69f3627cf4c509608e)
- [be2net: Support for WoL using magic packet after suspend.](http://git.kernel.org/linus/71d8d1b58aa4025ea73a66a130a98d0ed077f9b1)
- [bnx2x: Handle Rx and Tx together in NAPI](http://git.kernel.org/linus/54b9ddaa68414fad72ab2e1042be067c902441a6)
- [DM9000: Wake on LAN support](http://git.kernel.org/linus/c029f4440fd3f0dcc6923f917536fd62d6ef5d1d)
- [e1000e: add missing tests for 82583 in ethtool functions](http://git.kernel.org/linus/f89271dda9431b432dad7505ccdcb57666233c1d)
- [e1000e: correct ICH/PCH PHY operations function pointers](http://git.kernel.org/linus/0be8401051c716be4533272e983b7eed3d83946d)
- [e1000e: enable new 82567V-3 device](http://git.kernel.org/linus/9e135a2e6266eba276f33c404a2478499bc07ff5)
- [ethtool: Add Direct Attach support to connector port reporting](http://git.kernel.org/linus/5789d290cda6854b03986031df02b965572279df)
- [fsl_pq_mdio: Add Suport for etsec2.0 devices.](http://git.kernel.org/linus/1d2397d742b7a2b39b2f09dd9da3b9d1463f55e9)
- [gianfar: Add Multiple group Support](http://git.kernel.org/linus/46ceb60ca80fa07703bc6eb8f4651f900dff5a82)
- [gianfar: Add Multiple Queue Support](http://git.kernel.org/linus/fba4ed030cfae7efdb6b79a57b0c5a9d72c9de83)
- [gianfar: Add per queue structure support](http://git.kernel.org/linus/a12f801d4b349bc57622584e70e45a4ccbef53b6)
- [gianfar: Add support for hibernation](http://git.kernel.org/linus/be926fc4046913d9ad921aeacdf9329978241c38)
- [gianfar: Introduce logical group support.](http://git.kernel.org/linus/f4983704a63b3764418905a77d48105a8cbce97f)
- [igb: Add full support for 82580 devices](http://git.kernel.org/linus/55cac248caa4a5f181a11cd2f269a672bef3d3b5)
- [igb: add new data structure for handling interrupts and NAPI](http://git.kernel.org/linus/047e0030f1e601233ae5b03910602ec93c620bce)
- [igb: add single vector msi-x testing to interrupt test](http://git.kernel.org/linus/4eefa8f0131410eddaca323cd65e1ebefe3b3328)
- [igb: add support for 82576NS SerDes adapter](http://git.kernel.org/linus/747d49baaf4e3f4ad5ae77477830da026eeef69d)
- [igb: add support for 82580 MAC](http://git.kernel.org/linus/bb2ac47bcfd47ed9431ff1676ec8d79250c941c9)
- [igb: add support for seperate tx-usecs setting in ethtool](http://git.kernel.org/linus/4fc82adfb01bdee79ec21e44557dc409ef31419a)
- [igb: add support for the 82580 phy](http://git.kernel.org/linus/2909c3f79d933b55bf2485addb1dca762210b6af)
- [igb: make use of the uta to allow for promiscous mode filter](http://git.kernel.org/linus/68d480c4defb69d834e75fd0be9069a8447afe36)
- [igb: remove microwire support from igb](http://git.kernel.org/linus/285b4167458ec7cc49008b2e61cbe0362deed335)
- [ixgbe: Add support for 82599 alternative WWNN/WWPN prefix](http://git.kernel.org/linus/383ff34bebc2eccae71686fbd72e1cd948859675)
- [ixgbe: add support for 82599 based Express Module X520-P2](http://git.kernel.org/linus/38ad1c8e8c8debf73b28543a3250a01f799f78ef)
- [ixgbe: add support for 82599 KR device 0x1517](http://git.kernel.org/linus/74757d49016a8b06ca028196886641d7aeb78de5)
- [ixgbe: Add support for netdev_ops.ndo_fcoe_get_wwn to 82599](http://git.kernel.org/linus/61a1fa102ada6d8ee9f2293d126ed9f580ca0751)
- [mwl8k: add support for the 88w8366](http://git.kernel.org/linus/6f6d1e9a8a7fea5e4400cad64bed717e322208e1)
- [NET: Add driver for Octeon MDIO buses.](http://git.kernel.org/linus/25d967b72a92d72b6e0263a0337dfc940bd6c044)
- [net: add Runtime PM to the sh_eth driver](http://git.kernel.org/linus/bcd5149ded6b2edbf3732fa1483600a716b1cba6)
- [net/appletalk: push down BKL into a atalk_dgram_ops](http://git.kernel.org/linus/ecced8ba8759c16337fc6785d7bab8931ca55cf6)
- [net: enable smsc911x on MIPS](http://git.kernel.org/linus/b4efc5610980bc4b65a6cb49b939cf5f7dfa2723)
- [net/ipx: push down BKL into a ipx_dgram_ops](http://git.kernel.org/linus/83927ba069a65326f39991a02d6a49ba3b7cea44)
- [NET/KS8695: add support NAPI for Rx](http://git.kernel.org/linus/31b73ab3efaa9c69bc72e04605c85ff8c8047b11)
- [net/ps3: Add support for gelic link negotiation](http://git.kernel.org/linus/55873ed87fe6d34bd6f3a303c2d2ec6632c14525)
- [netxen: add access to on chip memory for tools](http://git.kernel.org/linus/47abe35610cbbfb3cc92847efdf588a8be1f5ebc)
- [netxen: add PCI IDs for new chip](http://git.kernel.org/linus/f0e08fac06596a760f074c08521550d93b96336e)
- [netxen: add sysfs entries for diag tools](http://git.kernel.org/linus/70f9cf8951e5253cfef821f8dcb92f6fc3af50c6)
- [pasemi_mac: ethtool set settings support](http://git.kernel.org/linus/5402240c0bc621ef6865c80043bda30a29365948)
- [qlge: Add CBFC pause frame counters to ethtool stats.](http://git.kernel.org/linus/6abd23468deaf3f6215a80b564f85df934209721)
- [qlge: Add ethtool blink function.](http://git.kernel.org/linus/d8eb59dc8b9e77bb4fa5420ff80142759ad5cd7b)
- [qlge: Add ethtool get/set pause parameter.](http://git.kernel.org/linus/1d30df24ec85477368e6e38fe1b4d1b67b3be9d4)
- [qlge: Add ethtool register dump function.](http://git.kernel.org/linus/a61f80261306ad11d9c8a453307a56417cfeae03)
- [qlge: Add ethtool self-test.](http://git.kernel.org/linus/9dfbbaa6b0b9f7c4d6c9dc3a59006f44e6521138)
- [qlge: Add ethtool wake on LAN function.](http://git.kernel.org/linus/bc083ce98eeb42205e99495481c8616d30916f6e)
- [sfc: Add firmware protocol definitions (MCDI)](http://git.kernel.org/linus/f0d37f4228e440597d5d56c31292e2e1639c7539)
- [sfc: Add power-management and wake-on-LAN support](http://git.kernel.org/linus/89c758fa47b54d8ce10d2b39ed09de6da0ba4324)
- [sfc: Extend MTD driver for use with new NICs](http://git.kernel.org/linus/76884835684411264cda2f15585261eb02183541)
- [sfc: Move shared NIC code from falcon.c to new source file nic.c](http://git.kernel.org/linus/8e730c15e1560415f33d7301b617be26050ffb86)
- [sfc: Separate shared NIC code from Falcon-specific and rename accordingly](http://git.kernel.org/linus/152b6a62aea2d43359dd37004e9c218bf7bdeb3b)
- [sfc: Update hardware definitions for Siena](http://git.kernel.org/linus/3e6c4538542ab2103ab7c01f4458bc2e21b672a1)
- [sfc: Update version, copyright dates, authors](http://git.kernel.org/linus/906bb26c0624d87df74e6642f2d74cde176fcc12)
- [sky2: 88E8059 support](http://git.kernel.org/linus/0f5aac7070a01ec757ed243febe4fff7c944c4d2)
- [sky2: add register definitions for new chips](http://git.kernel.org/linus/e91cd2e65f22a80af87367178bed4957fdc45ecd)
- [sky2: add SK-9E21M device id](http://git.kernel.org/linus/e30a4ac243b1fd2714675fd451e718d9940b1bdd)
- [tc35815: Enable NAPI](http://git.kernel.org/linus/b75c6dbb45a49289b90f885c7fb6d9ac39a21688)
- [tg3: Add 50610M phy ID for 5785](http://git.kernel.org/linus/c73430d04ec75962e20e186d34c40b6d999f0968)
- [tg3: Add 5717 phy ID](http://git.kernel.org/linus/c2060fe1f36565e60e622662a4519babd3b72f68)
- [tg3: Add 57765 asic rev](http://git.kernel.org/linus/b703df6f628ab63eaa875232551b1f2f0503b9af)
- [tg3: Add AC131 power down support](http://git.kernel.org/linus/0e5f784c77197edf29d2770b518dc78777d5a480)
- [tg3 / broadcom: Add APD support for GPHYs](http://git.kernel.org/linus/c704dc23cac0e433796bfe0a1fe2f1a64da11ac7)
- [tg3: Fix DIDs, Enable 5717 support](http://git.kernel.org/linus/5001e2f638011859c1351f9fe57ca4e545a15c47)
- [tg3: Improve 5785 PCIe performance](http://git.kernel.org/linus/788a035e6061a66c6c77059c417fdc6234e140ff)
- [TI DaVinci EMAC: Add suspend/resume capability](http://git.kernel.org/linus/8d044fe6aacaf573112331847155211a56a12736)
- [via-velocity: Add ethtool interrupt coalescing support](http://git.kernel.org/linus/6dfc4b95b29d89dbdb45de04b1b1ff493ec8016d)
- [via-velocity: Implement NAPI support](http://git.kernel.org/linus/dfff7144b14bab3d8baaeba8926fab371fa4a01e)
- [via-velocity: Re-enable transmit scatter-gather support](http://git.kernel.org/linus/c79992fddee28bbd31b35ac297e1068d32930179)
- [vxge: Removed accessing non-supported registers.](http://git.kernel.org/linus/0f8f7d58eb4840ee8790e914a88b8a773aca9143)

**WLAN**

- [ar9170: Add support for D-Link DWA 160 A2](http://git.kernel.org/linus/15295380f45aa0d35665f6e5596ac98c081d95b9)
- [ath5k: add LED support for Acer Aspire One AO751h/AO531h](http://git.kernel.org/linus/77c8258ff7e6788d3889e7062607e891618d811f)
- [ath5k: add support for Dell Vostro A860 LED](http://git.kernel.org/linus/6a213afd058436dbbd01098d7422c6a0073c39b5)
- [ath5k: enable Power-Save Polls by setting the association ID](http://git.kernel.org/linus/8ce54c5a5f5d2f4f03993395d60f3110670002ca)
- [ath5k: use noise calibration from madwifi hal](http://git.kernel.org/linus/e5e2647fd6ceef2cdc479954b84517535eb7febd)
- [ath9k_common: add new module to share 802.11n driver helpers](http://git.kernel.org/linus/db86f07ec6cdea9670a0928bd1289109d2a989dc)
- [ath9k_hw: add AR9271 srev and device ID to allow hw to support ar9271](http://git.kernel.org/linus/7976b4263cb05dc638297d35f2a42375090ebaff)
- [ath9k_hw: print device ID if not supported](http://git.kernel.org/linus/3ca340381a1da26906dc766a1e4f8a5d0a613189)
- [ath9k: move hw code to its own module](http://git.kernel.org/linus/7322fd19295fa7f7d954a19a5f0b77687d441846)
- [atheros: add common debug printing](http://git.kernel.org/linus/c46917bb53a546f60c7d3103407fe953c418dd5b)
- [b43: LP-PHY: Begin implementing calibration and software RFKILL support](http://git.kernel.org/linus/2c0d6100da3ee9b0f0cc46add9bb8a8161299a92)
- [cfg80211: add firmware and hardware version to wiphy](http://git.kernel.org/linus/dfce95f51fe34fa18c87a7d0bea53594b9bf1b9a)
- [cfg80211: Add PMKSA wext compatibility handler](http://git.kernel.org/linus/2944b2c2d2dd884c550163c698577132588277d8)
- [gianfar: Basic Support for programming hash rules](http://git.kernel.org/linus/7a8b3372e29ff58ebdf94def26703afabd287f11)
- [i2400m: minimal ethtool support](http://git.kernel.org/linus/abb307338396bd58f5d9d32c4e56ef40ff668a74)
- [iwlwifi: add aggregation tables to the rate scaling algorithm](http://git.kernel.org/linus/e3949d62861b3fdef19e80080d670aa1153a23c4)
- [iwlwifi: add channel switch support to 5000 series and up](http://git.kernel.org/linus/4a56e9652ec2ffce87b099aa2fc5b4eb2d5b2666)
- [iwlwifi: add LED mode to support different LED behavior](http://git.kernel.org/linus/02f5dac08364d01a8b2c8e298b529b97f356b3f5)
- [iwlwifi: add module firmware info for 1000 series](http://git.kernel.org/linus/9554b34ad5817f424253aab265d0e2a54207f810)
- [iwlwifi: add SM PS support for 6x50 series](http://git.kernel.org/linus/3f3e0376bb14ac7bfd8ac3e9824b2ad04d945e18)
- [iwlwifi: Chain Noise Calibration for 6000 series](http://git.kernel.org/linus/d8c07e7a84950b5fdef424c6dabe6bed3a9ffa19)
- [iwlwifi: device tracing](http://git.kernel.org/linus/be1a71a128ed91372d4ad8d54d8fd972a1a356eb)
- [iwlwifi: drop lib80211 dependency](http://git.kernel.org/linus/c099752ae06784fcd9cd393cbf3dfbc6b54f4569)
- [iwlwifi: LED cleanup](http://git.kernel.org/linus/e932a609e9759cc75db0c234f465a5fd6e20d362)
- [iwlwifi: provide firmware version](http://git.kernel.org/linus/5ebeb5a676c864acf59caa166b3cc0a13b7cff93)
- [iwlwifi: reliable entering of critical temperature state](http://git.kernel.org/linus/7812b16730ccebce71a3b2228ac08dd4f8b39469)
- [iwlwifi: rework for static power save](http://git.kernel.org/linus/4ad177b5c860dc0b1083eccc55957daf4a116b90)
- [iwlwifi: support idle for 6000 series hw](http://git.kernel.org/linus/78f5fb7fc6c2c668a12fd6892c18baa20e4ffd27)
- [iwlwifi: update lowest API version support for 6x00 and 6x50 series](http://git.kernel.org/linus/442464218d93aa0aacc55c3a7ac908ae00abff5f)
- [iwmc3200wifi: 802.11n Tx aggregation support](http://git.kernel.org/linus/a7af530d45969a63e20708417b70c547596ce3a9)
- [iwmc3200wifi: add BGN sdio device id](http://git.kernel.org/linus/30315ff05fce99ef0c172a966b3ed71baa62219b)
- [iwmc3200wifi: Add wifi-wimax coexistence mode as a module parameter](http://git.kernel.org/linus/43b5ffe1162a7fbaa89f1c392a28ac54c2e932f7)
- [iwmc3200wifi: CT kill support](http://git.kernel.org/linus/e85498b21d0372a00f31ab9f7c0d215c32c9fad5)
- [iwmc3200wifi: Enable wimax core through module parameter](http://git.kernel.org/linus/159bcfeb9123c91f0dc885a42b6387a98192f896)
- [iwmc3200wifi: WPS support](http://git.kernel.org/linus/a82aedbf1b043f7a7474aa9b6d223104ac51827a)
- [KVM: x86 emulator: Add 'push/pop sreg' instructions](http://git.kernel.org/linus/0934ac9d135021bec7f877340a039104af233bf3)
- [libertas: Add auto deep sleep support for SD8385/SD8686/SD8688](http://git.kernel.org/linus/4912545472d71e3dd546b18b397aec4c89fd7403)
- [libertas: first stab at cfg80211 support](http://git.kernel.org/linus/ff9fc791940f9ff51387c35f9332efe5007154f1)
- [libipw: initiate cfg80211 API conversion (v2)](http://git.kernel.org/linus/a3caa99e6c68f466c13cfea74097f6fb01b45e25)
- [mac80211: add MAC80211_VERBOSE_MHWMP_DEBUG](http://git.kernel.org/linus/27db2e423fdeae8815087677261ab72cca7b3c28)
- [mac80211: async station powersave handling](http://git.kernel.org/linus/af81858172cc0f3da81946aab919c26e4b364efc)
- [MAINTAINERS: Add iwmc3200wifi entry](http://git.kernel.org/linus/f6cd53c6a4204a3d4a274546449a70a766a99b6e)
- [mwl8k: add support for enabling hardware sniffer mode](http://git.kernel.org/linus/a43c49a817f31ce1accc029239827b108319ecf9)
- [mwl8k: handle loading AP firmware images](http://git.kernel.org/linus/eae74e6545d995ab0baa8fb07309f714d9616293)
- [mwl8k: implement AP firmware antenna configuration](http://git.kernel.org/linus/08b063477e45cb366df7204cbcdc79ff86513ef9)
- [nl80211: PMKSA caching support](http://git.kernel.org/linus/67fbb16be69d138a3b6645ec5395b487cb915c58)
- [rt2x00: Add rt2x00soc bus module](http://git.kernel.org/linus/5d78d34ba2d4a044983b599a697dc1d71af38c96)
- [rt2x00: Add USB ID for Linksys WUSB 600N rev 2.](http://git.kernel.org/linus/5e31258945f60dff65952575625cac214a75893e)
- [rt2x00: Disable powersaving for rt61pci and rt2800pci.](http://git.kernel.org/linus/93b6bd26b74efe46b4579592560f9f1cb7b61994)
- [rt2x00: more ids to rt2800usb.c](http://git.kernel.org/linus/2edcb7ff8d7d84a3797bcecc7094da0fa9828a16)
- [rt2x00: Only initialize HT on rt2800 devices that support it.](http://git.kernel.org/linus/38a522e6bc0fcd9848b91366ec899f1c2cb23609)
- [wimax: allow specifying debug levels as command line option](http://git.kernel.org/linus/4c2b1a11646bf74e2926ce8b13a21884adc1e05c)
- [wimax/i2400m: implement passive mode as a module option](http://git.kernel.org/linus/55a662d6468005ec3cd799fbd8d0ad03dfae6d2a)
- [wimax/i2400m: Implement pre/post reset support in the USB driver](http://git.kernel.org/linus/3725d8c97436aeaa03eeb0c25361a7ec0f3f5bd2)
- [wimax/i2400m: rework bootrom initialization to be more flexible](http://git.kernel.org/linus/aba3792ac2d7c808a2d2fd2adf89531e083bdb90)
- [wimax/i2400m: support extended firmware format](http://git.kernel.org/linus/bfc44187bbaeabf597be6566a24e8fa7d689b984)
- [wimax/iwmc3200: add new sdio device ID to support iwmc3200 2.5GHz sku](http://git.kernel.org/linus/f8fc3295570115267ce1ce901f362d13d194aefc)
- [wireless: implement basic ethtool support for cfg80211 devices](http://git.kernel.org/linus/4890e3beddfb4a6859c4bb782c9cd05dd94ead82)
- [wireless: remove remaining qual code](http://git.kernel.org/linus/671adc93b6472eaa0142a88d096c945f7b07893a)
- [wireless: remove WLAN_80211 and WLAN_PRE80211 from Kconfig](http://git.kernel.org/linus/133d7c6a504c672011ebc24b26e05b15f7410c07)
- [wl1251: Add connection monitoring configuration](http://git.kernel.org/linus/474c48c9f2118e637477b3b1c70003cb5cbda983)
- [wl1251: add support for PG11 chips.](http://git.kernel.org/linus/2c759e03b3b7639fff23ec3b7bab64a35ca0914f)
- [wl1251: enable power save](http://git.kernel.org/linus/8c8746f9db8b1f644695050703e2d38cd5964ba7)
- [wl1271: Added 5 GHz parameters for wl1273](http://git.kernel.org/linus/1ebec3d750f2b5740e3c334dac06104d2f74a9b1)
- [wl1271: Added 5 GHz support to join and rx](http://git.kernel.org/linus/a410264553447ff90bf13e3662684e794e5ff83e)
- [wl1271: Added support to scan on 5 GHz band](http://git.kernel.org/linus/abb0b3bfb2d2411034b721df21c31964265b851e)
- [wl1271: Add retry implementation for PSM entries](http://git.kernel.org/linus/19ad0715d8d9acc259ef02f83df767df2cf1eafe)
- [wl1271: Enable ELP](http://git.kernel.org/linus/5d0af498c08b43566733d5c5fb8293ce3b109eab)
- [wl1271: Enable smart reflex](http://git.kernel.org/linus/3cfd6cf960b2b030ccae1144a5c0dcd91c7c56a8)
- [wl1271: Support for IPv4 ARP filtering](http://git.kernel.org/linus/01c09162cd6170f3671825d6d5f2c1ae7b27cbf3)

**Various others network drivers, network stack**

- [Bluetooth: Add L2CAP option for max transmit value](http://git.kernel.org/linus/5fbcd3d1a07e234583e17830e8aef47282c22141)
- [Bluetooth: Add RFCOMM option to use L2CAP ERTM mode](http://git.kernel.org/linus/eae38eede2e5f70d65f09327297bd698b0d3ea7e)
- [Bluetooth: Enable auto sleep mode for btmrvl driver](http://git.kernel.org/linus/32fd63981ed453bd882f22e3e9b0ccbc11fb47e5)
- [Bluetooth: Implement raw output support for HIDP layer](http://git.kernel.org/linus/2da31939a42f7a676a0bc5155d6a0a39ed8451f2)
- [bond: Add support for multiple network namespaces](http://git.kernel.org/linus/ec87fd3b4e111e8bc367d247a963e27e5b86df26)
- [bonding: introduce primary_reselect option](http://git.kernel.org/linus/a549952ad323d68daf5b50bf716db895479af84c)
- [bridge: Allow enable/disable UFO on bridge device via ethtool](http://git.kernel.org/linus/72dad218f872dbd53f5dc5df9df45709e4b77870)
- [can: add the driver for Analog Devices Blackfin on-chip CAN controllers](http://git.kernel.org/linus/bbb84619c378414118fd4f1778125cd246c71e53)
- [can: add TI CAN (HECC) driver](http://git.kernel.org/linus/3758bf25db8caeec667e4e56e030da0ec3060529)
- [can: Driver for the Microchip MCP251x SPI CAN controllers](http://git.kernel.org/linus/e0000163e30eeb112b41486ea113fd54f64e1f17)
- [ethtool: Add reset operation](http://git.kernel.org/linus/d73d3a8cb4723e161589864741d8528d70b350eb)
- [ethtool: Remove support for obsolete string query operations](http://git.kernel.org/linus/a9828ec6bc0b7e19a65f7e13daa8bd35a926a753)
- [fakehard: claim all 2.4 Ghz channels as supported](http://git.kernel.org/linus/478e87c23340e88e909aa749f4772838bc96a20b)
- [gigaset: add Kernel CAPI interface (v3)](http://git.kernel.org/linus/7bb5fdc2fb021e32703ed1ff0269876bde1fa962)
- [gigaset: allow building without I4L](http://git.kernel.org/linus/aaba2b3f8213e1d66e71c351fa7a2b1cbd974d3c)
- [gigaset: documentation amendments](http://git.kernel.org/linus/64f16603eae17e869d5fc8a60ae987394190e639)
- [gigaset: prepare for CAPI implementation](http://git.kernel.org/linus/088ec0cc96e2befd5f3c035123f95c17bdf26e64)
- [ieee802154: add LIST_PHY command support](http://git.kernel.org/linus/1eaa9d03d3ee9156c8c405b006ce892ae28290ad)
- [ieee802154: add support for creation/removal of logic interfaces](http://git.kernel.org/linus/bb1cafb8fc414d6dbe933f888df6540c2ef02101)
- [inet: rename some inet_sock fields](http://git.kernel.org/linus/c720c7e8383aff1cb219bddf474ed89d850336e3)
- [ip: update the description of rp_filter in ip-sysctl.txt](http://git.kernel.org/linus/1f5865e73fb18834f52bd6e1d27bce86ff372089)
- [ipv4 05/05: add sysctl to accept packets with local source addresses](http://git.kernel.org/linus/8153a10c08f1312af563bb92532002e46d3f504a)
- [ipv4: fib table algorithm performance improvement](http://git.kernel.org/linus/16c6cf8bb471392fd09b48b7c27e7d83a446b4bc)
- [ipv4: udp: Optimise multicast reception](http://git.kernel.org/linus/1240d1373cd7f874dd0f3057c3e9643e71ef75c6)
- [ipv4: udp: optimize unicast RX path](http://git.kernel.org/linus/5051ebd275de672b807c28d93002c2fb0514a3c9)
- [ipv6 sit: 6rd (IPv6 Rapid Deployment) Support.](http://git.kernel.org/linus/fa857afcf77da669eb6b7031ec07ad14b912c307)
- [ipv6: udp: Optimise multicast reception](http://git.kernel.org/linus/a1ab77f97ed03f5dae66ae4c64375beffab83772)
- [ipv6: udp: optimize unicast RX path](http://git.kernel.org/linus/fddc17defa22d8caba1cdfb2e22b50bb4b9f35c0)
- [net: Add sk_mark route lookup support for IPv4 listening sockets](http://git.kernel.org/linus/ffce908246c93b17304c313886d25cfa8aecd1d7)
- [net: Add support for batching network namespace cleanups](http://git.kernel.org/linus/72ad937abd0a43b7cf2c557ba1f2ec75e608c516)
- [net/can: add driver for mscan family and mpc52xx_mscan](http://git.kernel.org/linus/afa17a500a3667f66df450100538d06769529bba)
- [net/can/mpc52xx_can: improve properties and their description](http://git.kernel.org/linus/81593c1cea7afdcd653c77d626aa186993e39c91)
- [net: export device speed and duplex via sysfs](http://git.kernel.org/linus/d519e17e2d01a0ee9abe083019532061b4438065)
- [netfilter: nf_ct_tcp: improve out-of-sync situation in TCP tracking](http://git.kernel.org/linus/c4832c7bbc3f7a4813347e871d7238651bf437d3)
- [netfilter: xtables: document minimal required version](http://git.kernel.org/linus/7a92263705435d046d37a0990d0edfcb517f7ad3)
- [net: Generalize socket rx gap / receive queue overflow cmsg](http://git.kernel.org/linus/3b885787ea4112eaa80945999ea0901bf742707f)
- [net/irda: push BKL into proto_ops](http://git.kernel.org/linus/58a9d73202dd40076992154e9acfb98489cc8eab)
- [net: Remove BKL from tun](http://git.kernel.org/linus/deed49fbb68d7d07ec6c3dfd06bffc74e9abc6fa)
- [net: Support specifying the network namespace upon device creation.](http://git.kernel.org/linus/81adee47dfb608df3ad0b91d230fb3cef75f0060)
- [net/x25: push BKL usage into x25_proto](http://git.kernel.org/linus/91774904fbf0fe1c71441dd8299342a4654f7103)
- [sctp: remove deprecated SCTP_GET\_\*\_OLD stuffs](http://git.kernel.org/linus/a242b41dedfe0fd51ab1c906daa703c09b196744)
- [udp: dynamically size hash tables at boot time](http://git.kernel.org/linus/f86dcc5aa8c7908f2c287e7a211228df599e3e71)
- [usbnet: Set device type for wlan and wwan devices](http://git.kernel.org/linus/225794f8c33fd32721ae1cd3576db99810351d7b)
- [usbnet: Use wwan%d interface name for mobile broadband devices](http://git.kernel.org/linus/e1e499eef2200c2a7120c9ebf297d48b195cf887)
- [vlan: Add support to netdev_ops.ndo_fcoe_get_wwn for VLAN device](http://git.kernel.org/linus/d6534799410d2b53e5e80b8a90d6a8bab3de30ed)
- [vlan: support "loose binding" to the underlying network device](http://git.kernel.org/linus/5e7565930524410f097f5b04f8aba663089a6ffc)

For other articles on 2.6.33 and links to the rest of the "Coming in 2.6.33 " series, see [The H's Kernel Log - 2.6.33 Tracking page](../site/open/features/Linux-Kernel-2-6-33-tracking-890639.html "Linux Kernel 2.6.33 tracking – 21 December 2009, 10:18").

([thl](mailto:thl@ct.heise.de) /c't).

([crve](mailto:crve@h-online.com "Chris von Eitzen "))
