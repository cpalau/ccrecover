---
title: "Kernel Log: Coming in 2.6.34 (Part 1) - Network Support"
date: 2010-04-13
author: "Thorsten Leemhuis"
source: http://www.h-online.com/open/features/Kernel-Log-Coming-in-2-6-34-Part-1-Network-Support-975937.html
pages: 1
---

# Kernel Log: Coming in 2.6.34 (Part 1) - Network Support

**Thorsten Leemhuis**

**Expected for release in May, Linux kernel version 2.6.34 contains several new network drivers and various advancements designed to improve network performance or increase network configuration flexibility, which will particularly impact virtualisation.**

The development of 2.6.34 has been slightly less smooth than usual: First, Torvalds baffled many developers with a [shorter merge window](../site/open/features/Kernel-Log-Linux-2-6-34-goes-into-testing-950563.html "Kernel Log: Linux 2.6.34 goes into testing – 10 March 2010"), then RC2 was released comparatively late and included [more changes than usual](../site/open/features/Kernel-Log-Ceph-file-system-in-2-6-34-kernel-and-KVM-presentations-at-the-CLT2010-961429.html "Kernel Log: Ceph file system in 2.6.34, kernel and KVM presentations at the CLT2010 – 23 March 2010"); furthermore, both versions contained significant problems, as Torvalds [had to admit when releasing RC3](../site/open/features/Kernel-Log-Graphics-drivers-and-Mesa3D-updated-four-new-stable-kernels-971885.html "Kernel Log: Graphics drivers and Mesa3D updated, four new stable kernels – 07 April 2010"). RC4 has now been released after two weeks, longer than the normal weekly release cycle. Torvalds [explained](http://article.gmane.org/gmane.linux.kernel/973119) that this was due to "hunting a really [annoying VM regression](http://thread.gmane.org/gmane.linux.kernel/968149/focus%3D969907)".

Despite this bumpy start, all the major changes for the next version in the main development line should have now made it into the Linux source code management system – therefore, the Kernel Log is already in a position to provide a comprehensive overview of the most important advancements of Linux 2.6.34, which is due for release in May. The Kernel Log will provide the usual multi-part series of articles which will cover the kernel's various functional areas step by step. This, the first part in the "Coming in 2.6.34" mini series discusses the changes that affect the kernel's network support; further articles in the coming weeks will deal with the improvements in terms of storage hardware, file systems, graphics support, architecture code, drivers and various other functional areas.

### LAN, WLAN, Network Stack, etc.

Among the [1,300 changes](http://thread.gmane.org/gmane.linux.kernel/955640) in the main Git-Pull request submitted by network subsystem maintainer David Miller are various new Ethernet drivers. The ixgbevf driver (for example [1](http://git.kernel.org/linus/92915f71201b43762fbe05dbfb1a1a0de9c8adb9), [2/documentation](http://git.kernel.org/linus/ecc6703cbb2bb648c7345c652a704f7af56322b8)), uses SR-IOV to communicate with guest systems via the virtual networking features offered by Intel's 82599 family of 10 Gigabit Ethernet controllers – for this purpose, the ixgbe driver, which supports these chips on the host system, was extended to include SR-IOV ([1](http://git.kernel.org/linus/096a58fdec72335d9cbee94bd10b312c5f14f8af), [2](http://git.kernel.org/linus/1cdd1ec8784399eef55a60887a45f3f46a1c240a), [3](http://git.kernel.org/linus/17367270b1d7f529f5d72e8f2cf76672829eb335)). The [qlcnic driver](http://git.kernel.org/linus/af19b49152bdb68fda894183e88096d6d1aa5c3d) has been added for Qlogic's QLE8240 and QLE8242 1G/10G CNA chips; other new drivers include [greth](http://git.kernel.org/linus/d4c41139df6e74c6fff0cbac43e51cab782133be) for 10/100/1G Ethernet chips in the Gaisler family by Aeroflex, [ksz884x](http://git.kernel.org/linus/8ca86fd83eae6c73db5f6b23ee3a63b77d52c8ee) for Micrel KSZ8841 and KSZ8842 Ethernet chips as well as the [smsc75xx](http://git.kernel.org/linus/d0cad871703b898a442e4049c532ec39168e5b57) driver suitable for USB Gigabit NICs with LAN75xx chips by SMSC. After releasing RC3, the kernel developers also incorporated the cxgb4 driver ([1](http://git.kernel.org/linus/b8ff05a9c3237f694a1c3bf8ceec3bf6c3c14b15), [2](http://git.kernel.org/linus/43e9da8d782b8a40d5127fcc59ac2e543cf16d7d)) for Chelsio T4 Gigabit Ethernet and 10 Gigabit Ethernet chips. The atl1c driver [has been extended](http://git.kernel.org/linus/496c185c9495629ef1c65387cb2594578393cfe0) to support the AR8152 and AR8152 Ethernet chips by Atheros.

Further additions to the kernel include [vhost-net](http://git.kernel.org/linus/3a4d5c94e959359ece6d6b55045c3f046677f55c), which is designed to increase performance in virtualisation solutions such as KVM or Lguest – vhost-net is a server for the Virtio framework outlined in the [commit comment](http://git.kernel.org/linus/3a4d5c94e959359ece6d6b55045c3f046677f55c) which operates in the kernel and is designed to reduce overheads when guest systems use virtual Virtio network hardware to exchange data with operating systems that run on different hardware. The new [macvtap](http://git.kernel.org/linus/20d29d7a916a47bf533b5709437fe735b6b5b79e) driver offers more flexible and faster network data exchange facilities between the guest systems on a host as well as various other options. The developers are preparing numerous other improvements for this driver and the Virtio server so that in the long term these components' performance and range of features will be further increased.

Various changes to the Wi-Fi stack were introduced to improve the utilisation of the power-saving mechanisms offered by modern Wi-Fi chips. Numerous patches modify the Wi-Fi drivers for the RT2800 generation and newer generations of Ralink chip-sets – however, these young drivers still don't run smoothly on many chips, which probably means that in the coming months the Ralink drivers from the staging area will remain the preferred option for many users.

The kernel's bridge code now [supports IGMP snooping](http://git.kernel.org/linus/eb1d16414339a6e113d89e2cca2556005d7ce919). The netfilter code now understands "[conntrack zones](http://git.kernel.org/linus/5d0aa2ccd4699a01cfdf14886191c249d7b45a01)" and offers [TCP connection tracking for SIP](http://git.kernel.org/linus/f5b321bd37fbec9188feb1f721ab46a5ac0b35da). The network stack now includes private VLAN proxy arp support as described in RFC3069. Jan Kiszka introduced about [30 further changes](http://thread.gmane.org/gmane.linux.kernel/941654) which considerably update the CAPI code in the kernel's ISDN subsystem and reportedly eliminate numerous problems.

### Minor gems

Many further minor, but by no means insignificant, changes can be found in the list below, which contains the commit headers referring to the respective changes. Like many of the references in the text above, the links point to the [web front end](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=summary) of the Git branch for the kernel sources maintained by Linus Torvalds at kernel.org. The commit comments and the patches themselves provide extensive further information on the respective changes.

*LAN*

- [axnet_cs: add new id](http://git.kernel.org/linus/60bbc725b5b3009bb1bf2628ce5033d9bc108881)
- [be2net: Add link test to list of ethtool self tests.](http://git.kernel.org/linus/4276e47e2d1c85a2477caf0d22b91c4f2377fba8)
- [e1000e: provide MAC-family-specific function to set LAN ID](http://git.kernel.org/linus/f4d2dd4cd4d001f5dc20fc76c780c0c20c000c23)
- [e1000e: use alternate MAC address on ESB2 if available](http://git.kernel.org/linus/608f8a0d014db6cd18d4f535934d4b5d556e3013)
- [e1000: Report link status in ethtool when interface is down](http://git.kernel.org/linus/b548192acaebcb05d6a87d1e94f19835b1a18a8b)
- [enic: feature add: add ethtool -c/C support](http://git.kernel.org/linus/7c8445991172cc17eaca9f7de0a300c02caaa49d)
- [fec: Add LAN8700 phy support](http://git.kernel.org/linus/fceb2919192d7a667be81c17c0bfa227fd7fa992)
- [fs_enet: Add support for MPC512x to fs_enet driver](http://git.kernel.org/linus/60ab4361adc188fb47da1c4892cc7a2bb621efef)
- [igb: add support for wake-on-link](http://git.kernel.org/linus/22939f0606e515799d83e1a29250917f94c8d07b)
- [igb: Report link status in ethtool when interface is down](http://git.kernel.org/linus/3145535ac6e4769e587a38a67d888a10f24a7af9)
- [igb: support for VF configuration tools](http://git.kernel.org/linus/8151d2948e088c20b7d29c793cf1fd744b6a2699)
- [ipg: Remove device claimed by dl2k from pci id table](http://git.kernel.org/linus/25cca5352712561fba97bd37c495593d641c1d39)
- [ixgbe: Add support for the new ethtool n-tuple programming interface](http://git.kernel.org/linus/9a713e7c7cca2f31c89367bb7b48310ab8a3e630)
- [lib/vsprintf.c: Add IPV4 options %pI4\[hnbl\] for host, network, big and little endian](http://git.kernel.org/linus/0159f24ee764927bf44c1a25473bd4517febd21c)
- [macvlan: allow multiple driver backends](http://git.kernel.org/linus/fc0663d6b5e6d8e9b57f872a644c0aafd82361b7)
- [macvtap: add GSO/csum offload support](http://git.kernel.org/linus/b9fb9ee07e67fce0b7bfd517a48710465706c30a)
- [MCS7830 USB-Ether: add Rx error support](http://git.kernel.org/linus/76802851b6e1b78b614ba611d6b5d27a83f60ded)
- [net: add ColdFire support to the smc91x driver](http://git.kernel.org/linus/717ea4b3474852057b1ce2c639ce219f4f8d3a8d)
- [net: Add netdev ops for SR-IOV configuration](http://git.kernel.org/linus/95c26df829ba4a25f40595cadb4c9433883cbe28)
- [NET: Add Qlogic ethernet driver for CNA devices](http://git.kernel.org/linus/0ec00f0392b807d57a2281576a96552d7694b6bb)
- [net: Delete isa-skeleton net driver](http://git.kernel.org/linus/8266d7127c1b0bdf924066c19c71be4d351e9583)
- [net: emaclite: adding MDIO and phy lib support](http://git.kernel.org/linus/5cdaaa12866e916d0ada8b56c5f0e543cfc7fe3d)
- [net: Kconfig change for KSZ884X driver](http://git.kernel.org/linus/1eb1cc7a209f9593312ba014f1b1f02c31eda4fb)
- [net/macvtap: add vhost support](http://git.kernel.org/linus/501c774cb13c3ef8fb7fc5f08fa19473f7d9a0db)
- [pcnet_cs: add new id](http://git.kernel.org/linus/1546a713ae1f066f83469cdd99ebdf500d6a65e4)
- [phy: SMSC device Energy Detect power-down mode](http://git.kernel.org/linus/698244ace8b63896565022143ab19f141bc48993)
- [qlge: Add basic firmware dump.](http://git.kernel.org/linus/8aae2600030f54494f9061d2cde141802d774be9)
- [qlge: Add module param to force firmware core dump.](http://git.kernel.org/linus/d5c1da56afb8a6b232393fb3fdef4909389d05fe)
- [sfc: Enable autonegotiated flow-control by default if supported](http://git.kernel.org/linus/7a6b8f6f7f74085a1330b0f9765d81bcea8c58b7)
- [stmmac: add documentation for the driver.](http://git.kernel.org/linus/a1d6f3f65512cc90a636e6ec653b7bc9e2238753)
- [tg3: Abort phy init for 5717 serdes devices](http://git.kernel.org/linus/ecf1410b9d70b3034e5955e92bb0c3e02ff21e9c)
- [tg3: Add 5717 serdes phy ID](http://git.kernel.org/linus/9b952f51d019db37276bdb2924e776ca09132fc1)
- [tg3: Add 57765 phy ID and enable devices.](http://git.kernel.org/linus/b0f752210c0aa5e3d9ece4cbfefdc43092a68b83)
- [tg3: Make 57791 and 57795 10/100 only](http://git.kernel.org/linus/d110114281fad580dd9ce629507d17b123169cff)
- [tg3: Turn off multiple DMA reads for 5717](http://git.kernel.org/linus/0339e4e3effeae71e2b19c6340ef9672fb7a2cb3)
- [via-velocity: Enable scatter/gather IO by default](http://git.kernel.org/linus/b6ca430599ea37843632b0eaa231dea5414dec25) [virtio: disable multiport console support.](http://git.kernel.org/linus/b7a413015d2986edf020fba765c906cc9cbcbfc9)

*WLAN*

- [Add a pci-id to the mwl8k driver](http://git.kernel.org/linus/e5868ba10c3c5d8a56c06bbafe098103356ac03f)
- [Add Station and AdHoc mode support to libertas_tf](http://git.kernel.org/linus/f32338319f10c4ca5499c19edc5b3618896920ba)
- [Add USB ID for Thomson SpeedTouch 120g to p54usb id table](http://git.kernel.org/linus/05a9a1617026977422c7c5ed3aeac6f46fa2132c)
- [ar9170: add support for NEC WL300NU-G USB dongle](http://git.kernel.org/linus/eb3d72c8b7e6bb6a55e15272c52eb4eadf7fb1f1)
- [ar9170usb: add Sphairon Homelink 1202 USB ID](http://git.kernel.org/linus/5b6e2f12edd6c46e87a2775321f1912d19be4b35)
- [ath5k: adding LED support for AR5BXB63 cards](http://git.kernel.org/linus/47db3a677b533489d1a5a027282aa33f46dffa79)
- [ath9k: add support for 802.11n bonded out AR2427](http://git.kernel.org/linus/5ffaf8a361b4c9025963959a744f21d8173c7669)
- [ath9k: implement coverage class support](http://git.kernel.org/linus/e239d8591843945630521ec85edca08289f1a751)
- [b43: add new SSB's core id for BCM4328](http://git.kernel.org/linus/003d6d2792bebb2b66966ce5f1da11849e855180)
- [b43: Allow PIO mode to be selected at module load](http://git.kernel.org/linus/b02914af4d7020828ce921a572589dd793517c09)
- [b43: Declare at least one real firmware file using MODULE_FIRMWARE.](http://git.kernel.org/linus/6021e08db47386507108a475e6c820a7006a4632)
- [b43: fall back gracefully to PIO mode after fatal DMA errors](http://git.kernel.org/linus/9e3bd9190800e8209b4a3e1d724c35f0738dcad2)
- [b43legacy: Declare all possible ucodeX.fw files](http://git.kernel.org/linus/c2f4f527edab37f2f2130bd7813cd41db907ab6b)
- [cfg80211: add regulatory hint disconnect support](http://git.kernel.org/linus/09d989d179d0c679043556dda77c51b41a2dae7e)
- [cfg80211: add remain-on-channel command](http://git.kernel.org/linus/9588bbd5529461a3dacd435bf239c84c3508f569)
- [cfg80211/mac80211: allow registering for and sending action frames](http://git.kernel.org/linus/026331c4d9b526561ea96f95fac4bfc52b69e316)
- [cfg80211: process the max power on a country IE](http://git.kernel.org/linus/08030db6e5275dda19ea1b3ab8a41c992799db4a)
- [iwlwifi: Add chain_noise support for 6050](http://git.kernel.org/linus/ed56a3f15a0561e900957ecca0dee42b9b453a9e)
- [iwlwifi: add continuous uCode event log capability](http://git.kernel.org/linus/a9e1cb6a78ea8a74c49bf76726a2942f636a833b)
- [iwlwifi: cleanup spectrum measurement command support](http://git.kernel.org/linus/81963d68575d497d626ce13e42c84518a931cc12)
- [iwlwifi: module parameter to enable/disable bt co-exist](http://git.kernel.org/linus/06702a735eacf8679e9ff0d49eb3c989bc6b96ce)
- [iwlwifi: optimize power saving](http://git.kernel.org/linus/49dcc819b077c2d473062e17d5a1373a8b660e02)
- [mac80211: add U-APSD client support](http://git.kernel.org/linus/ab13315af97919fae0e014748105fdc2e30afb2d)
- [mac80211: allow disabling 40MHz on 2.4GHz](http://git.kernel.org/linus/f38fd12fa7b7b98e158a9b31d388da34eef25c22)
- [mac80211/cfg80211: add station events](http://git.kernel.org/linus/98b6218388e345064c3f2d3c161383a18274c638)
- [mac80211: enable spatial multiplexing powersave](http://git.kernel.org/linus/0f78231bffb868a30e8533aace142213266bb811)
- [mac80211: generalise work handling](http://git.kernel.org/linus/af6b63741cc4e4dfd575d06beb333b11a8a6e0c0)
- [mac80211_hwsim: add fake hw scan handler](http://git.kernel.org/linus/690680360cd22b55235481ca3421a3450a96138a)
- [mac80211: improve powersave documentation](http://git.kernel.org/linus/c99445b14054e0c4ed4715df1dad1fc608cbab46)
- [mac80211: introduce flush operation](http://git.kernel.org/linus/a80f7c0b088187c8471b441d461e937991870661)
- [mac80211: let cfg80211 manage auth state](http://git.kernel.org/linus/63f170e0c80a131cdd549fab7afb5036009944fc)
- [mac80211: support remain-on-channel command](http://git.kernel.org/linus/b8bc4b0aa9bfba755c64b11b8f60e6cfab25dc9d)
- [MAINTAINERS: update mwl8k maintenance status](http://git.kernel.org/linus/a040d532b912b5dd7d88692b580cff9c88b987e3)
- [mwl8k: add 2.4GHz channels 12, 13 and 14](http://git.kernel.org/linus/647ca6b01a5289948e970ea7c1f656f9d90b0a27)
- [mwl8k: add 5 GHz band channels and rates](http://git.kernel.org/linus/4eae9edd38c0a9ce34e39100ccc69ff520bc1224)
- [mwl8k: add another 88w8366 PCI ID](http://git.kernel.org/linus/ca66527c60385dcec878ebd90749d1fdc43bc870)
- [mwl8k: add support for 88w8363 in STA mode](http://git.kernel.org/linus/9e1b17ead81e72d3db37b4cf15cde1f613603822)
- [mwl8k: bail out if there is no AP firmware image support for this chip](http://git.kernel.org/linus/91942230689c1758685499e82e53769d5e7f32eb)
- [mwl8k: basic AP interface support](http://git.kernel.org/linus/b64fe619e371fc17d8d686d6d44aef1b41317880)
- [mwl8k: update MODULE_FIRMWARE tags](http://git.kernel.org/linus/c92d4edecf489dbcbb2e5dd3c513790e57e2ea0e)
- [nl80211: Add new WIPHY attribute COVERAGE_CLASS](http://git.kernel.org/linus/81077e82c3f591578625805dd6464a27a9ff56ec)
- [nl80211: add power save commands](http://git.kernel.org/linus/ffb9eb3d8b450c22bbbc688c6b630141ac476fd9)
- [p54usb: Add the USB ID for Belkin (Accton) FD7050E ver 1010ec](http://git.kernel.org/linus/5b9a919a97ac8bdda8020c9b366491b5b91b196e)
- [p54usb: Add usbid for Corega CG-WLUSB2GT.](http://git.kernel.org/linus/15a69a81731d337a3d9db51692ff8704c1114f43)
- [ps3_gelic_wireless: Remove PS3 gelic legacy wpa support](http://git.kernel.org/linus/c1596b75c29eb5b32c65ef1e186c8b08c289bf05)
- [rt2x00: Add USB ID for CEIVA adapter to rt73usb](http://git.kernel.org/linus/51b2853fd91a3c8fd9f3adc1549569d2c1dc2a2d)
- [rt2x00: Disable powersaving by default in rt2500usb.](http://git.kernel.org/linus/9e76ad2a27f592c1390248867391880c7efe78b3)
- [rt2x00: Introduce SoC interface type.](http://git.kernel.org/linus/cea90e55969ff70b970d64d564076a5469331527)
- [rt2x00: Reorganize RT chipset setting for PCI/SOC devices.](http://git.kernel.org/linus/714fa6636331d33c6045efe394f36c964a6c14ee)
- [rt2x00: rework RT chipset and revision determination for PCI an SOC devices.](http://git.kernel.org/linus/49e721ec6ca74f90ee99089ad2de1c338a95c6d5)
- [rt2x00: rt2800 - Make rt30xx and rt35xx chipsets configurable.](http://git.kernel.org/linus/de1ebdceb6a4fe1b7073b81d273285b7c8bed312)
- [rt73usb: add WLI-U2-H54HP](http://git.kernel.org/linus/050e8a47dc8b056c880f380ffd01055669f8fe68)
- [wireless: remove CONFIG_WIRELESS_OLD_REGULATORY](http://git.kernel.org/linus/baeb66fe2306783e3b9a492b03882f2e249b2eeb)
- [wireless: support internal statically compiled regulatory database](http://git.kernel.org/linus/3b377ea9d4efc94dc52fe41b4dfdb463635ab298)
- [wl1251: add U-APSD support](http://git.kernel.org/linus/4ff6ffa107ba1c6ba9a1cc75a1f304eaa79e8bf4)
- [wl1251: enable WMM](http://git.kernel.org/linus/da2fb4e9c215b8f0f8954818691549f8a34135be)
- [wl1251: implement WMM](http://git.kernel.org/linus/49e1b9faed736b20ad9a785638919341b567a595)
- [wl1271: Add rudimentary ad-hoc support](http://git.kernel.org/linus/e0d8bbf0d23e6b82f13b29f39593d5d13d923b2b)
- [wl1271: add testmode support](http://git.kernel.org/linus/c8c90873520ef4c201cfd03b4892ca8bbf551e2e)
- [wl1271: Implement chipset boot retry](http://git.kernel.org/linus/9ccd921792e5b6719ff9e561438e095cba757727)

*Network-Stack, Netfilter, etc.*

- [Bluetooth: Add controller types for BR/EDR and 802.11 AMP](http://git.kernel.org/linus/943da25d95c7e8fd8c39dbf09e030f5da46f5d85)
- [Bluetooth: Convert debug files to actually use debugfs instead of sysfs](http://git.kernel.org/linus/aef7d97cc604309b66f6f45cce02cd734934cd4e)
- [bridge: Add hash elasticity/max sysfs entries](http://git.kernel.org/linus/b195167fcf089dbdc650bb874084555035f07f98)
- [bridge: Add multicast count/interval sysfs entries](http://git.kernel.org/linus/d902eee43f1951b358d7347d9165c6af21cf7b1b)
- [bridge: Add multicast data-path hooks](http://git.kernel.org/linus/c4fcb78cf8ae55667809e54e54872a21025dd073)
- [bridge: Add multicast forwarding functions](http://git.kernel.org/linus/5cb5e947d8f82011e3d7e7017e9d10db9a40ae9f)
- [bridge: Add multicast_router sysfs entries](http://git.kernel.org/linus/0909e11758bd28848aeb6646e021ec1e031a3f0f)
- [bridge: Add multicast_snooping sysfs toggle](http://git.kernel.org/linus/561f1103a2b70de7e06e1e7fd072a5b142a4278c)
- [bridge: Add multicast start/stop hooks](http://git.kernel.org/linus/3fe2d7c70b747d5d968f4e8fa210676d49d40059)
- [can: add support for CAN interface cards based on the PLX90xx PCI bridge](http://git.kernel.org/linus/24c4a3b29255f9f8bc48d93597a58256b5a1f83f)
- [can: mscan-mpc5xxx: add support for the MPC512x processor](http://git.kernel.org/linus/bf3af54732bea5894ccc2cbde3ab566f0af7da56)
- [can/netlink: add CAN_CTRLMODE_ONE_SHOT](http://git.kernel.org/linus/c1c5523dd1517250cac8b15a4acbc237c24a67d4)
- [can: Proper ctrlmode handling for CAN devices](http://git.kernel.org/linus/ad72c347e56bf3a0231b9d686e17764157d2961c)
- [can:ti_hecc: Add pm hook-up](http://git.kernel.org/linus/35e2da46d25a53e0e19956f533cc29272a6cceb2)
- [CAPI: Remove experimental tag from middleware feature](http://git.kernel.org/linus/771f4c87be909ad9feb6af26424485b02deed244)
- [CAPI: Rework locking of controller data structures](http://git.kernel.org/linus/0ca3a017a7373a4545dd7b345a8a0cecc16bc7e2)
- [CAPI: Sanitize capifs API](http://git.kernel.org/linus/90926f0e58dcd9f4ca877961000568a3be787f2f)
- [CAPI: Schedule capifs for removal](http://git.kernel.org/linus/79e95f4717767e9ddc4dbec5d778f0c9970eed34)
- [dccp: allow probing of CCID-array length](http://git.kernel.org/linus/69a6a0b38a139ccceef32222108caca8a9b0b795)
- [doc: document IPv6 parameters](http://git.kernel.org/linus/b0f83b280fcfa9cdd66b748f0c12fb26ce69e391)
- [ethtool: Introduce n-tuple filter programming support](http://git.kernel.org/linus/15682bc488d4af8c9bb998844a94281025e0a333)
- [gigaset: small documentation improvement](http://git.kernel.org/linus/2ac2ed5f2dfc97ae9ed9f446ad6e064fa821ef6d)
- [igb: Add support for 82576 ET2 Quad Port Server Adapter](http://git.kernel.org/linus/b894fa2627e28c078740dc7041cd08c7e2c353ab)
- [ipv4: allow warming up the ARP cache with request type gratuitous ARP](http://git.kernel.org/linus/6d955180b2f9ccff444df06265160868cabb289a)
- [IPVS: Allow boot time change of hash size](http://git.kernel.org/linus/6f7edb4881bf51300060e89915926e070ace8c4d)
- [ipvs: SCTP Trasport Loadbalancing Support](http://git.kernel.org/linus/2906f66a5682e5670a5eefe991843689b8d8563f)
- [ISDN: Add PCI ID for HFC-2S/4S Beronet Card PCIe](http://git.kernel.org/linus/d00561a2f64b381aefb41f4a140ff5dc373b52e7)
- [isdn: fix a few Kconfig imperfections](http://git.kernel.org/linus/e5f8d9ac46e0291594abaa76bf467a08367bcccf)
- [llc: optimize multicast delivery](http://git.kernel.org/linus/0f7b67dd9e1192976f5e5a78934c7a339ff7c45f)
- [llc: use a device based hash table to speed up multicast delivery](http://git.kernel.org/linus/6d2e3ea284463d5ab34e9cf2a41d0b8627b95d02)
- [net/9p: Add sysfs mount_tag file for virtio 9P device](http://git.kernel.org/linus/86c8437383acd85c05ec7c9a004f59fe7ac9821a)
- [net: add limit for socket backlog](http://git.kernel.org/linus/8eae939f1400326b06d0c9afe53d2a484a326871)
- [net: add scheduler sync hint to tcp_prequeue().](http://git.kernel.org/linus/c839d30a41dd92eb32d7fcfa2b4e99042fc64bf2)
- [netfilter: ctnetlink: add zone support](http://git.kernel.org/linus/ef00f89f1eb7e056aab9dfe068521e6f2320c94a)
- [netfilter: ctnetlink: netns support](http://git.kernel.org/linus/9592a5c01e79dbc59eb56fa26b124e94ffcd0962)
- [netfilter: ctnetlink: support selective event delivery](http://git.kernel.org/linus/0cebe4b4163b6373c9d24c1a192939777bc27e55)
- [netfilter: ebtables: add CONFIG_COMPAT support](http://git.kernel.org/linus/81e675c227ec60a0bdcbb547dc530ebee23ff931)
- [netfilter: nf_conntrack_sip: add T.38 FAX support](http://git.kernel.org/linus/9d288dffe3a276e1f06ba556845c456d696c5a4f)
- [netfilter: nf_conntrack: support conntrack templates](http://git.kernel.org/linus/b2a15a604d379af323645e330638e2cfcc696aff)
- [netfilter: nf_nat_sip: add TCP support](http://git.kernel.org/linus/48f8ac26537c1b7b1a2422f5232f45d06c945348)
- [netfilter: nf_nat: support mangling a single TCP packet multiple times](http://git.kernel.org/linus/010c0b9f34a4c567b431f8b49a58b7332ed42e47)
- [netfilter: nfnetlink: netns support](http://git.kernel.org/linus/cd8c20b650f49354722b8cc1f03320b004815a0a)
- [netfilter: xtables: add CT target](http://git.kernel.org/linus/84f3bb9ae9db90f7fb15d98b55279a58ab1b2363)
- [netfilter: xtables: optimize call flow around xt_ematch_foreach](http://git.kernel.org/linus/6bdb331bc6910d1ccb74dc9852fc858c5916c927)
- [netfilter: xtables: optimize call flow around xt_entry_foreach](http://git.kernel.org/linus/0559518b5b99c591226460c0bbf8e6a570c518a8)
- [netfilter: xt_connlimit: netns support](http://git.kernel.org/linus/83fc81024bd8572f31db784f8c0079e999a4fa44)
- [netfilter: xt_hashlimit: netns support](http://git.kernel.org/linus/e89fc3f1b06d9241f65e580b002789abaa6d11ac)
- [netfilter: xt_recent: netns support](http://git.kernel.org/linus/7d07d5632b672c892a65882c2a119345fd9596c9)
- [net/irda: sh_sir: Add SuperH IrDA driver](http://git.kernel.org/linus/2a6ace1b3d4dc65401e71fc01af100692b9f27f8)
- [net: TCP thin dupack](http://git.kernel.org/linus/7e38017557bc0b87434d184f8804cadb102bb903)
- [net: TCP thin linear timeouts](http://git.kernel.org/linus/36e31b0af58728071e8023cf8e20c5166b700717)
- [net: TCP thin-stream detection](http://git.kernel.org/linus/5aa4b32fc86408705337e941ed716880c63d1590)
- [packet: Add GSO/csum offload support.](http://git.kernel.org/linus/bfd5f4a3d605e0f6054df0b59fe0907ff7e696d3)
- [packet: Kill CONFIG_PACKET_MMAP.](http://git.kernel.org/linus/889b8f964f2f226b7cd5a0a515109e3d8d9d1613)
- [powerpc/mpc5xxx: add OF platform binding doc for FSL MSCAN devices](http://git.kernel.org/linus/959d20bfe8b90023c862dec3956054027a5a0912)
- [qeth: HiperSockets Network Traffic Analyzer](http://git.kernel.org/linus/76b11f8e270f04851774ff64b16e29e5a43d3a1a)
- [rfkill: Add support for KEY_RFKILL](http://git.kernel.org/linus/3082a2b7b1af1b1508c1c3fa589566064f926f40)
- [timestamping: fix example build](http://git.kernel.org/linus/f28f9e43b3d81d1e69da0ebf77c8a6780cb5e0c8) [tun: socket filter support](http://git.kernel.org/linus/99405162598176e830d17ae6d4f3d9e070ad900c)

*For other articles on 2.6.34 and links to the rest of the "Coming in 2.6.34" series, see [The H's Kernel Log - 2.6.34 Tracking page](../site/open/features/Linux-Kernel-2-6-34-tracking-962586.html "Linux Kernel 2.6.34 tracking – 24 March 2010"). Older Kernel Logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/). New editions of Kernel Logs are also mentioned on* [Identi.ca](http://identi.ca/kernellog2) *and* [Twitter](http://twitter.com/kernellog2) *via "@kernellog2". The Kernel Log author also posts updates about various topics on* [Identi.ca](http://identi.ca/kernellogauthor) *and* [Twitter](http://twitter.com/kernellogauthor) *via "@kernellogauthor".*

(*[thl](mailto:thl@ct.heise.de)*)
