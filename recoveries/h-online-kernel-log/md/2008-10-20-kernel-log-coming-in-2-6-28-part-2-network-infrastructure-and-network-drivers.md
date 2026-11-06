---
title: "Kernel Log: Coming in 2.6.28 - Part 2: network infrastructure and network drivers"
date: 2008-10-20
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-Coming-in-2-6-28-Part-2-network-infrastructure-and-network-drivers-737711.html
pages: 1
---

# Kernel Log: Coming in 2.6.28 - Part 2: network infrastructure and network drivers

**Dj Walker-Morgan**

The commit flood for 2.6.28 during the current merge window doesn't look like ending soon – in the last 24 hours alone, Linus Torvalds has integrated a further 700 patches, most of them contributed by other kernel developers, into Linux's main development tree. The changes to ATA support and the block layer were [described in a previous kernel log](../site/news/item/Kernel-Log-Coming-in-2-6-28-Part-1-ATA-support-and-block-layer-737699.html "Kernel Log: Coming in 2.6.28 - Part 1: ATA support and block layer – 19 October 2008, 08:02"). The networking changes described here found their way into the main tree a few days ago. The network subsystem administrator has even [recently](http://thread.gmane.org/gmane.linux.kernel.wireless.general/22051) been [insisting](http://thread.gmane.org/gmane.linux.network/108480/focus%3D743534) that all changes for the next kernel version should have been in linux-next, the staging tree for new changes, before the merge window was opened – because of this, the main development tree should already include all major network-related changes for Linux 2.6.28.

A rough overview of all the changes can be found in an [email sent by Torvalds to pull the networking changes](http://thread.gmane.org/gmane.linux.network/108375/). As expected the developers are integrating five new network drivers:

- [atl2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=452c1ce218a68b5dbd626397ecfc65ca89dd3cbb) – Atheros L2 10/100 Mbit NICs
- [enic](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=01f2e4ead2c51226ed1283ef6a8388ca6f4cff8f) – 10 Gbit NICs from Cisco
- [jme](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=95252236e73e789dd186ce796a2abc60b3a61ebe) – Gigabit NICs from JMicron
- [qlge](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c4e84bde1d595d857d3c74b49b9c45cc770df792) – 10 Gbit NICs from Qlogic
- [smsc95xx](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2f7ca802bdae2ca41022618391c70c2876d92190) – USB 2.0 10/100 Mbit adapter with SMSC LAN9500

Unlike many previous kernel versions, no new Wi-Fi drivers are being added to this version. Instead, more popular Wi-fi drivers have been worked on. The ath5k driver for Atheros WLAN chips now supports [mesh networks](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8e5f3d0aaa3ae5305613553f869727b0361cd472) and [the Atheros AR2417 v2 chip](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0d5f0316593df606515b17b037a1fd36c4b8bfdf); the rt2x00 driver now makes use of the encryption technology of various RaLink Wi-Fi chips ([1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2bb057d07a0bc17475a7bf897fc41667ab08b73f), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=61e754f44b57060464b1fcf261a8428ecfa23bed), [3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=906c110fcc24bdd5bf0fa22d89ac75d99c747e53), [4](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=008c44825db74c6cdcea13dfb1598896e74fe908)). A number of further improvements to LAN and WLAN drivers can be accessed via the links at the end of this article.

The generic [Wireless Regulatory Infrastructure](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b2e1b30290539b344cbaff0d9da38012e03aa347) should, in future, be more flexible and better ensure that Wi-Fi hardware does not infringe local rules and regulations on wireless connections. In a change from the previous kernel code, the new infrastructure makes considerable use of a program running in userspace, which can be updated much more easily and rapidly by the distributors than the kernel. Details of how it works and lots of background information on this issue can be found in the [commit notes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b2e1b30290539b344cbaff0d9da38012e03aa347), [kernel documentation](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob;f=Documentation/networking/regulatory.txt;h=a96989a8ff351c0a409187819175461cfa44f456;hb=b2e1b30290539b344cbaff0d9da38012e03aa347), an [article on LWN.net](http://lwn.net/Articles/237104/) and a [description of the Central Regulatory Domain Agent](http://wireless.kernel.org/en/developers/Regulatory/CRDA) in the [Linux wireless wiki](http://wireless.kernel.org/).

The developers have [made improvements to](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f07d1501292b3b0d3276ee0e537005526a45e242) the [Linux TX multiqueue implementation](http://www.heise-online.co.uk/open/Kernel-Log-Linux-2-6-27-Released--/features/111671/2#subsystems) ("multiqueue networking"), which was introduced in [2.6.27](../site/open/features/Kernel-Log-Linux-2-6-27-Released-746496.html "Kernel Log: Linux 2.6.27 Released – 10 October 2008, 08:38") and have added a "[PRIO based multiqueue packet scheduler](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=92651940ab00dbe64722e908f70d816713d677b7)". Additions to the main development tree include the Phonet Stack ([documentation](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob;f=Documentation/networking/phonet.txt;h=f3c72e0ca8d72f560bdb02775826aa0ec96b49ac;hb=953f551756a1275d9bfdbb70697323449305161a)), introduced by Nokia developers, and [transparent Ethernet bridging over GRE tunnels](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e1a8000228e16212c93b23cfbed4d622e2ec7a6b) from Herbert Xu. Jan Engelhardt has also introduced a number of wide-ranging revisions in the netfilter field, as a result of which Ebtables support is now [based on Xtables](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=043ef46c7690bfdbd5b012e15812a14a19ca5604). After five years of not working, the netfilter infrastructure now once more properly supports transparent proxy support with the developers saying ("*Proper transparent proxy support in netfilter. We sort of lost this feature 5 or so years ago, but hey better late than never to get it back :-)*").

Other commits in the network infrastructure and drivers include:

**Generic**:

- [bonding: add more ethtool support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fa53ebac42d3de04619c813f5f6628ca2a7ce97f)
- [IPVS: Add genetlink interface implementation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9a812198ae49967f239789164c55ec3e72b7e0dd)
- [net: Distributed Switch Architecture protocol support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=91da11f870f00a3322b81c73042291d7f0be5a17)

**LAN**

- [bnx2: Update 5706/5708 firmware.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d5321e309c2fd1a1d534fc7bb674a1fff9f25d94)
- [cassini: use request_firmware](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fcaa40669cd798ca2ac0d15441e8a1d1145f2b16)
- [cxgb3: Support for Aeluros 2005 PHY](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1e8820256f9921370cd7423396871e2d850e0323)
- [e1000e: add support for new 82574L part](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4662e82b2cb41c60826e50474dd86dd5c6372b0c)
- [e1000e: add support for the 82567LM-4 device](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2f15f9d60190a62bc8ac50fa84fea31fc0b00ecf)
- [e1000e: add support for 82567LM-3 and 82567LF-3 (ICH10D) parts](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f4187b56e1f8a05dd110875d5094b21b51ebd79b)
- [mv643xx_eth: transmit multiqueue support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e5ef1de198c7bf2ca10de82add06536ed6165f8b)
- [netxen: enable msi-x for quad-gig boards](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ec68db6930635b25ef5ba4983053635f5b4bf35e)
- [r8169: add 8168/8101 registers description](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f162a5d1b326d54b0be7e3100f69763d8a707721)
- [r8169: add hw start helpers for the 8168 and the 8101](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=dacf815434a4d5f5b45687873df46927c64cfb19)
- [r8169: additional 8101 and 8102 support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2857ffb7b8913ef713533ac5783abd70a20529e4)
- [r8169: new phy init parameters for the 8168b](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=236b8082aa239e91c3cd9cb466d0527a735e54db)
- [r8169: add a new 8168c flavor](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=197ff761dbf9fa5de9a4684a51ee5cb534cbb852)
- [r8169: add a new 8168c flavor (bis)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6fb07058d2b6c748c308e4ee453035433d34ca93)
- [r8169: add a new 8168cp flavor](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ef3386f00fcd18a40343047329ec7ed2eb98bbe8)
- [r8169: support additional 8168cp chipset](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=7f3e3d3a69da262016db6eec803881603c61ddf6)
- [r8169: preliminary 8168d support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5b538df9dedb3469b688b93ffab2a7efb64c88e3)
- [sfc: Export boot configuration in EEPROM through ethtool](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4a5b504d0c582db80813b70359b616ea30e91743)
- [smc911x: Add support for LAN921{5,7,8} chips from SMSC](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c6dcb8278876ebf266e2088b0b45b28aa66b7693)

**Wi-Fi**

- [ath5k: Update registers and SREV ids v2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1bef016a5a2c52de45b332c8fa797958becde9bf)
- [ath5k: rates cleanup](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=63266a653589e1a237527479f10212ea77ce7844)
- [ath9k: Allow AP mode to be enabled](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2ad67de3c8a21354b8b2721d5d2baabb7c5013c9)
- [ath9k: Add LED support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c83be6885e2f1ee6e0b290b6cfc82014c675e087)
- [ath9k: Add RF kill support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=500c064d3a5f9c8aa604ef63a1346ab70eed443a)
- [b43: Add LP-PHY radio register definitions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=400828c3da74a2e22b51bfc08d6db4697e3bce3e)
- [b43: Rewrite TX power adjustment](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=18c8adeb0244f823ba78a51e23f813fe68bc3c54)
- [cfg80211: fix static regdomains](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=762af43bda3d8281a2738d3920ae5ded170aaf39)
- [iwlwifi: Added support for 3 antennas](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3110bef78cb4282c58245bc8fd6d95d9ccb19749)
- [iwlwifi: update 5350 Wifi PCI IDs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e96a8495dcac965ef41a654fb456a72e56c87340)
- [mac80211: clean up rate control API](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4b7679a561e552eeda1e3567119bef2bca99b66e)
- [mac80211: make BA session handling independent of STA mode](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=de1ede7ac3bd300f9aa565d0f93f6cf9ba74bb1a)
- [mac80211: split off mesh handling entirely](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=472dbc45dc1966284de72d7de15690c17ed2cf33)
- [mac80211: use nl80211 interface types](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=05c914fe330fa8e1cc67870dc0d3809dfd96c107)
- [mac80211: share STA information with driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=17741cdc264e4d768167766a252210e201c1519a)
- [mac80211: add the 'minstrel' rate control algorithm](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=cccf129f820e431d84690729254a32f1709328fb)
- [orinoco: Invoke firmware download in main driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3994d502017a2239e30152d1231843ad05d04a7b)
- [p54: better firmware support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=19c19d54b6bfa57746f3ec805d1d7951eefa353b)
- [p54: control output power levels](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=09adf284039f896401df8ea219ee1d13e80333a8)
- [p54: 802.11a 5GHz phy support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1b9975347e852c22a7c4c67b68814403ef16d2bd)
- [p54usb: support LM87 firmwares](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2b80848e3818fb1c8ccddc105b065a86c68afa9d)
- [p54usb: Device ID updates](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ec366eba3b8d96fdb2e629c64fa2750be2723ba7)
- [rtl8187: add device ID 0bda:8198](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=746db510395e32ff57b9f8582e520df6b3fac618)
- [rtl8187: Add USB ID for Belkin F5D7050 with RTL8187B chip](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=eaca90dab6ab9853223029deffdd226f41b2028c)

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: Coming in 2.6.28 - Part 1: ATA support and block layer](../site/news/item/Kernel-Log-Coming-in-2-6-28-Part-1-ATA-support-and-block-layer-737699.html "Kernel Log: Coming in 2.6.28 - Part 1: ATA support and block layer – 19 October 2008, 08:02")
- [Kernel Log: new Catalyst drivers, 2.6.27.1 resolves cause of e1000e problem](../site/news/item/Kernel-Log-new-Catalyst-drivers-2-6-27-1-resolves-cause-of-e1000e-problem-737701.html "Kernel Log: new Catalyst drivers, 2.6.27.1 resolves cause of e1000e problem – 18 October 2008, 08:02")
- [Kernel Log: Ext4 completes development phase as interim step to btrfs](../site/news/item/Kernel-Log-Ext4-completes-development-phase-as-interim-step-to-btrfs-737697.html "Kernel Log: Ext4 completes development phase as interim step to btrfs – 17 October 2008, 09:52")
- [Kernel Log: Linux 2.6.27 Released](../site/open/features/Kernel-Log-Linux-2-6-27-Released-746496.html "Kernel Log: Linux 2.6.27 Released – 10 October 2008, 08:38")
- [Kernel Log: problem with e1000e bypassed, Morton praises Btrfs](../site/news/item/Kernel-Log-problem-with-e1000e-bypassed-Morton-praises-Btrfs-737561.html "Kernel Log: problem with e1000e bypassed, Morton praises Btrfs – 07 October 2008, 08:47")
- [Kernel Log: 2.6.27 nearing completion; Btrfs to be added to the kernel?](../site/news/item/Kernel-Log-2-6-27-nearing-completion-Btrfs-to-be-added-to-the-kernel-737489.html "Kernel Log: 2.6.27 nearing completion; Btrfs to be added to the kernel? – 01 October 2008, 09:23")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
