---
title: "Kernel Log - Coming in 2.6.31 - Part 1: New Wi-Fi drivers and other network-related changes"
date: 2009-07-02
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-Coming-in-2-6-31-Part-1-New-Wi-Fi-drivers-and-other-network-related-changes-742309.html
pages: 1
---

# Kernel Log - Coming in 2.6.31 - Part 1: New Wi-Fi drivers and other network-related changes

**Dj Walker-Morgan**

![Kernel Log Penguin](../site/imgs/43/3/6/8/7/4/0/93e8ea3d0acdf147.jpg)

#### Thorsten Leemhuis

**Linux 2.6.31 will be IEEE 802.15.4 capable and will include a new Wi-Fi driver for Intel chips. Developers have also added support for recent Ralink Wi-Fi components and revamped the Rfkill framework. The Wi-fi stack and drivers are now better able to use newer power saving technologies.**

With the [release](../site/news/item/Kernel-Log-Main-development-phase-of-Linux-2-6-31-completed-742199.html "Kernel Log: Main development phase of Linux 2.6.31 completed – 25 June 2009, 11:15") of the first pre-release version of Linux 2.6.31, the kernel hackers last week brought the merge window to a close, heralding an end to the adoption of major changes in the main development line of the next kernel version. Kernel hackers generally restrict themselves to introducing minor changes only into the main development tree during the second phase of the development cycle, so as to fix as many existing bugs as possible and avoid introducing new ones.

Kernel Log can now, therefore, launch its "Coming in 2.6.31" series and is dedicating the first article to major changes relating to Linux' network support. Further articles in the Kernel Log series will be published on The H over the next few weeks, building up to a detailed description of all the major changes planned for 2.6.31 for the various functional areas within the Linux kernel, up until Linus Torvalds releases Linux kernel 2.6.31 in late August or early September. For other articles on 2.6.31 and links to the rest of the "Coming in 2.6.31" series, see The H's [Kernel Log - 2.6.31 Tracking](../site/open/features/Kernel-Log-2-6-31-Tracking-746446.html "Kernel Log - 2.6.31 Tracking – 02 July 2009, 11:21") page.

### Wirelessly happy

This time around, there are again many Wi-Fi related changes. The [iwmc3200wifi](http://wireless.kernel.org/en/users/Drivers/iwmc3200wifi) Wi-Fi driver for Intel's Wireless Multicomm 802.11 is one [new addition to the kernel](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bb9f8692f5043efef0dcef048cdd1db68299c2cb). The driver is not yet fully mature, however, as it does not yet support operation as an access point or data transfer using 802.11n. No information on the 802.11agn chip, a 'full MAC' chip expected in a few weeks to months, is currently available from the Intel website. Chips of this type appear, to the operating system, like normal network chips, but are able to deal with many tasks themselves using their built-in firmware – the 'soft MAC' chips commonly found in today's netbooks and laptops leave more of the work to the drivers and Wi-Fi stack.

The kernel developers have added [support for data transfer using 802.11n](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=35f00cfcc06bb85e0659f9847400518008d78145) to the basic infrastructure of the [rt2x00 family of drivers](http://rt2x00.serialmonkey.com/) for driving various Ralink Wi-Fi chips. Changes adding support for Ralink's RT2770, RT2870 and RT3070 USB Wi-Fi chips have also [moved into](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d53d9e67b55f6a9fc3f836c5c392eb41ce5676f4) the kernel. This code is, however, far from mature, with the [commit comments](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d53d9e67b55f6a9fc3f836c5c392eb41ce5676f4) listing a number of major problems, for which reason users may be better served by the staging drivers for these chips and the vendor's own drivers.

### Re-revamped, IEEE 802.15.4

Hot on the heels of the [first complete revamp in 2.6.27](../site/open/Kernel-Log-Linux-2-6-27-Released--/features/111671/1) comes a new '[rewrite](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=19d337dff95cbf76edd3ad95c0cee2732c3e1ec5)' of the Rfkill framework, which deals with the slide switch or keyboard shortcut for switching Wi-Fi or Bluetooth off and on usually found on laptops. This is aimed at improving the interaction between hardware, kernel and userspace programs such as NetworkManager, and fixing [numerous problems](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=19d337dff95cbf76edd3ad95c0cee2732c3e1ec5) in this area.

As the rewrite was largely driven by one of the main Wi-Fi driver developers and further major improvements to the code were made during peer review, it is to be hoped that this may be the last major revision to the Rfkill framework for the time being. Nevertheless, a few teething troubles with the new code are to be expected.

Developed primarily by developers working for Siemens, support for the [IEEE 802.15.4](http://en.wikipedia.org/wiki/IEEE_802.15.4) data transfer protocol for [Personal Area Networks](http://en.wikipedia.org/wiki/Wpan) (WPAN) has also now found its way into the main Linux development tree (e.g. [1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9ec7671603573ede31207eb5b0b3e1aa211b2854), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8459464f07cf67cab07b17d5736d75fb86adab22), [3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fcb94e422479da52ed90bab230c59617a0462416), [4](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2c21d11518b688cd4c8e7ddfcd4ba41482ad075b), [documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=02cf228639233aa227a152955a98564c7a18f9ee)).

### Pending

There have been numerous changes to the Wi-Fi drivers in the staging area, where drivers which do not yet meet the requisite quality standards are collected for further development. The [rtl8192su](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5f53d8ca3d5d6afa55011e1e858a4bf255a3abf4) driver for similarly named Realtek Wi-Fi chips is one new addition, and is joined by the vt6655 driver for the eponymous VIA chip range (e.g. [1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1cb648b34879b79975f68728be70bae05979ae13), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1d69a1c65b0d25739819caef6b1f0f6ddc2ab84c)).

Developers have also merged parts of the three staging drivers for Ralink's RT2770, RT2870 and RT3070 Wi-Fi chipsets, substantially reducing the amount of code in the staging area. In the long term, however, this work is probably irrelevant, as the standard rt2x00 Ralink driver should eventually also deal with these chips, with the result that the staging drivers may simply be abandoned. Kernel developers have now taken the first steps along this route with their changes to the rt2x00 driver.

### Network hardware and packet filtering

One [new arrival](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a463696039f7097ce87c21db3cf5c16cdcb3850d) is the cnic driver for Broadcom's NetXtremeII series Gigabit Ethernet cards. Thanks to [a number of changes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4edd473f208cff77ce1f7ef26d5a41f31fa198e0) to the bnx2 driver for Broadcom chips, Broadcom hardware now takes care of much of the iSCSI work itself, thereby reducing CPU load ("iSCSI offload").

[Another new arrival](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4510d7cb8b4e7d389652b8a4f89fad469a5ecc92) is the int51x1 driver for Intellon's USB-connected 14 Mbit/s INT51x1 and INT5200 chips, used by devices for transferring data via the power grid (power line communication/PLC), such as develo's dLAN.

Thanks to [passive OS fingerprinting](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=11eeef41d5f63c7d2f7fdfcc733eb7fb137cc384), the Netfilter code can now partially detect the operating system deployed on the system from which network packets originate and can then subject packets to operating system-specific rule sets. The OSF project [website](http://www.ioremap.net/projects/osf) includes example usages and links to a fingerprint collection. There is also a [short LWN.net article](http://lwn.net/Articles/336921/) with background information on the technology.

### In Brief

The changes described above are just some of the more significant of those recently undertaken by kernel hackers in the networking field. Among the other changes are:

**LAN:**

- [A new arrival](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a6286ee630f6d95f8466e19d7f1ae38d677028ae) is a network driver for Texas Instruments' DaVinci Ethernet Media Access Controller.

<!-- -->

- The e1000e driver [can now talk to](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a4f58f5455ba0efda36fb33c37074922d1527a10) Intel's 82577 and 82578 Gigabit LAN chips.

<!-- -->

- [There have been a number of changes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=720017623ab294b66c8a95d7bc5ccf75a581ebe4) to the e100 driver aimed at improving support for older Intel network chips, which had been worse with the e100 driver than with the recently removed eepro100 driver.

<!-- -->

- There have been many improvements and a few new drivers in the [Controller Area Network](http://en.wikipedia.org/wiki/Controller_Area_Network) (CAN) subsystem (e.g. [1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e20dad964aeac229a204e298c563b6ea7ff1e987), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=39549eef3587f1c1e8c65c88a2400d10fd30ea17), [3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=429da1cc841bc9f2e762fd7272fc2b80314b890a), [4](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f534e52f091a7b9f51fb6726710bdf731b663e94), [5](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a61a8423c71d6da6f1f6f854d8adcea24b80bef6), [6](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d1a277c584d0862dbf51991baea947ea5f2ce6bf)).

**Wi-Fi:**

- The [kernel now includes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2f01a1f58889fbfeb68b1bc1b52e4197f3333490) the [wl12xx](http://linuxwireless.org/en/users/Drivers/wl12xx) driver for Texas Instruments' wl1251 and wl1271 Wi-Fi chips, used primarily in embedded systems.

<!-- -->

- CFG80211 and NL80211 now offer an API for configuring ad-hoc networks using IBSS ([Independent Basic Service Set](http://en.wikipedia.org/wiki/Independent_Basic_Service_Set#Independent_Basic_Service_Set_.28IBSS.29)).

<!-- -->

- Various changes improve support for power saving features offered by newer Wi-Fi chips, in drivers such as [iwlwifi](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6da3a13e4fcab0ff58592087d28bd283caf23d88) and in the MAC80211 Wi-Fi stack (e.g. [1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=965bedadc01d34027455d5d5b67063ef0209c955), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5bb644a0fd25a5e083ecbfaa92a211db99aa6ef7), [3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5cff20e6c5a6591a79d3b027af222870f52bb550), [4](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=955394c98c9cb79bdb3e6b479695af3a90ea0623)).

<!-- -->

- The [ar9170](http://wireless.kernel.org/en/users/Drivers/ar9170) driver can now deal with some AVM Fritz cards [equipped with Atheros chips](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bdf6d32f933bf28dfdca325281ee5266c753dc67).

<!-- -->

- Support for operating as an access point has now been ["officially" enabled](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6f5f39c95af519c24c0187950147eb79d07d1940) in the [ath5k](http://wireless.kernel.org/en/users/Drivers/ath5k) driver for older Atheros chips.

**Miscellaneous:**

- Support for an XHFC embedded solution from Speech Design has been [added](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=db9bb63a1b5b65df41d112a8c21adbbfc6a4ac08) to the mISDN subsystem.

### Minor gems

Many less major, but in no way insignificant, changes can be found in the list below. The numerous links in the list below and text above lead directly to the relevant changes in the main Linux development tree web interface. The commit comments and the patches themselves provide extensive further information on changes. A brief overview of the major network-related changes and patches can also be found in the git pull requests from the network subsystem maintainer ([1](http://thread.gmane.org/gmane.linux.network/130767), [2](http://thread.gmane.org/gmane.linux.network/131078), [3](http://thread.gmane.org/gmane.linux.network/131310), [4](http://thread.gmane.org/gmane.linux.network/131455), [5](http://thread.gmane.org/gmane.linux.network/131797)).

**LAN:**

- [bnx2x: Separated FW from the source.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=94a78b79cb5f14c09a42522738d6694c6a1cdd20)
- [cxgb3: Add Aeluros 2020 phy support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=744514249f0656e2d50bb57585241670c2d4f32b)
- [e1000e: enable CRC stripping by default](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6e50912a442947d5fafd296ca6fdcbeb36b163ff)
- [e1000e: stop unnecessary polling when using msi-x](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=679e8a0f0ae3333e94b1d374d07775fce9066025)
- [fec: Add FEC support for MX35 processor](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=644233073458653e4b7fb474d9a8bdbbfd37739a)
- [forcedeth: addition of new mcp89 device id](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3df81c4e950a7e38a8ef98f818abc3eed76b3fb2)
- [ixgbe: Add FCoE Storage MAC Address support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0365e6e4373a5a447746fd7ac26074b92f180311)
- [macb: Add support of the netpoll API](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6e8cf5c069c6cb7b316e9b1715eac38873dd5cab)
- [mdio: Add generic MDIO (clause 45) support functions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1b1c2e95103ce391c2ea39a9460968fcb73deb30)
- [net: add Xilinx ll_temac device driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=92744989533cbe85e8057935d230e128810168ce)
- [netdev: Added KS8842 driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b07878e5471a8c880cb3cffee3a73048f38d2001)
- [NET/r8169: Rework suspend and resume](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=861ab44059350e5cab350238606cf8814abab93b)
- [net: sh_eth: Add support SH7724](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=65ac8851490ec97a96759af729132c96f925a795)
- [net: smsc911x: add power management functions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b6907b0c705b6db221f937b4d343e2a6b280c8c5)
- [openfirmware: Add OF phylib support code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8bc487d150b939e69830c39322df4ee486efe381)
- [s6gmac: xtensa s6000 on-chip ethernet driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8b0215aa5b01eb3cb54ca57bfa36e94a0d039ed9)
- [sky2: add GRO support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=37e5a2439b43bb90655e17f00c9db5759909a712)
- [The patch adds support for the PCI cards: PCIcan and PCIcanx (1, 2 or 4 channel) from Kvaser (http://www.kvaser.com).](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3878fb6fdbceecca20b15748f807340854220f06)
- [vxge: Enable SRIOV support in the driver.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5dbc901172fb952409940cd7ca55d8e6e5a7cc2c)

**Wi-Fi:**

- [Add LED support for AR5BXB6 IBM Thinkpad PCIe adapters](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=84379cba44042a4caf793f821be8bd1a9b8235c2)
- [Add support for CF8381 WiFi card.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=dc7d243d75b906cc964c12caa3b2eebe953a69be)
- [ar9170: add support for 1-stage firmware](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c768b58d62d3106f0f670d35d1e7820c14ba769a)
- [ar9170: support HT receive and channel config](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9e52b0623c6eb49c3f23a326c1fb97bdecc49ba1)
- [ath5k: Add Spur filter support on newer chips](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=57e6c56dbb52d680f61dd629759fe2974840ed93)
- [ath5k: add support for Fukato Datacask Jupiter LEDs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6a362bb1c9f900f7e6daeee52ff2d538badae49b)
- [ath5k: Implement antenna control](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2bed03ebf62f9d013a455209bf30d7e086120443)
- [ath5k: use regulatory infrastructure](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f769c36bd71ebe8d7a5f83764f0428d36ebced35)
- [ath9k: Disable autosleep feature for AR9285 based chipsets.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=882b709230246de3359b04b195ad3e80b93b73ef)
- [atheros: introduce ath module containing common ath5k/ath9k/ar9170 code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3a702e49c03ba959e3f5bb2b74ec9921a81c8c98)
- [atheros: put atheros wireless drivers into ath/](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=203c4805e91786f9a010bc7945a0fde70c9da28e)
- [b43: Add fw capabilities](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=403a3a136122457165321e90b7569a321cc9ac12)
- [cfg80211: allow adding/deleting stations on mesh](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=155cc9e4b1d60161ee53ffaf2c15b9411f086fa7)
- [iwlagn: co-exist with AMT](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=086ed117c918f07fd40323ab5adc64c52ea7c1b8)
- [iwlagn: disable PS support for iwlagn](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=286d94906587901851906a5e2ddc09bc1a7ba1d9)
- [iwlwifi: add Greenfield support for 11n](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2681b20ba2a255ea20a168c0ebe519c40b55e57e)
- [iwlwifi: improve scan support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1ecf9fc1317f8df91eb1d74360f408558d657478)
- [iwlwifi: support truly passive scanning](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b097ad29752f909ec1121ac3dc57d348f08dd8d7)
- [libertas: add support for Marvell SD8688 chip](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e45d8e534b67580eedd9b4910ccc16d6dd3cceff)
- [mac80211: add hardware restart function](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f2753ddbadb0873a98421415882318251bbd9eaa)
- [mac80211: Allow scan to be requested in AP mode](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=357303e2b61272b191f2e5d782d94fdd8f50fd71)
- [mac80211: disable powersave if pm_qos asks for low latency](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=10f644a47b76d3e61b98f2d02ce9690b94c51ee5)
- [mac80211: enable PS by default](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bbbdff9e00449928f228867076a07bdfecd3dca8)
- [mac80211: implement beacon filtering in software](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d91f36db51661018f6d54ff5966e283bcec4c545)
- [mac80211: improve scan timing](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=99c84cb0692729088788d8e1d1cee670154176e4)
- [mac80211: update injection documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=de2b3e864aa908e613dd9912def88af7877d85f3)
- [p54: add beacon filtering support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f13027af5cd567757c18b85776232e31a2ba55d4)
- [p54: deactivate broken powersave function (part 2)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fade5db4f227bf59874efd6023f39d345e17e2a4)
- [rt2x00: Add new rt2800usb USB ID's](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ce2ebc9b8ddac020aa06c83a6d084c34017d835d)
- [rt2x00: Add new rt2800usb USB ID's for Sweex](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3b91c3604d000205fb4e56b5ddd6b77b22ad4689)
- [rt2x00: Add new USB ID for rt2800usb](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e430d6074dede3b4d7d87e30296fe3894cb4709c)
- [rt2x00: Add USB ID for rt2800usb](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2c617b0324c4b05e8e08f14407a9be3b7756768f)
- [rtl8187: Implement TX/RX blink for LED](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a027087a6b4c7d985b872cac3e19ce023670792e)
- [zd1211rw: adding 083a:e503 as a ZD1211B device](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f72151fb6820e90ce12a15e2768aa41150c5186d)

**Wi-Fi, Rfkill:**

- [acer-wmi: fix rfkill conversion](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a878417cc576720d3c9ff5399522d06f226bad7d)
- [ath5k: added cfg80211 based rfkill support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e6a3b61681dcb963e6465ffbc4330b44824f35e3)
- [ath9k: port to cfg80211 rfkill](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3b319aae4244f9b4758212605f67cf63207a4fa1)
- [b43/legacy: port to cfg80211 rfkill](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f41f3f373dd72344c65d801d6381fe83ef3a2c54)
- [Bluetooth: Add native RFKILL soft-switch support for all devices](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=611b30f74b5d8ca036a9923b3bf6e0ee10a21a53)
- [cfg80211: add rfkill support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1f87f7d3a3b42b20f34cb03f0fd1a41c3d0e27f3)
- [eeepc-laptop: add rfkill support for the 3G modem in Eee PC 901 Go](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3cd530b5aaffd27b231f9717730f2f6684c00bda)
- [eeepc-laptop: read rfkill soft-blocked state on resume](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=96e9cfeb9692b0bc6e03f9b6f9cb3c67a40b76d1)
- [eeepc-laptop: rfkill refactoring](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7de39389d8f61aa517ce2a8b4d925acc62696ae5)
- [iwlwifi: port to cfg80211 rfkill](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a60e77e5a41330334fd0ca428f18919d1ea6ed62)
- [rfkill: add function to query state](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6081162e2ed78dfcf149b076b047078ab1445cc2)
- [rfkill: create useful userspace interface](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c64fb01627e24725d1f9d535e4426475a4415753)
- [rfkill: document /dev/rfkill](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f71fea23a27ba8ec53375832aab6a80fc14622e0)
- [rfkill: don't restore software blocked state on persistent devices](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=06d5caf47ef4fbd9efdceae33293c42778cb7b0c)
- [rfkill: export persistent attribute in sysfs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=464902e812025792c9e33e19e1555c343672d5cf)
- [rfkill: improve docs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ce0879e324df007f12cc25227102847b92fcafb7)
- [rfkill: remove user_claim stuff](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=621cac85297de5ba655e3430b007dd2e0da91da6)
- [rfkill: rewrite](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=19d337dff95cbf76edd3ad95c0cee2732c3e1ec5)

**ISDN:**

- [gigaset: documentation update](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b3fcb13f1c866ae0330c445c3cb481014c36a02f)
- [gigaset: remove UNDOCREQ config option](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b88bd95655c7bc059606529e01467594978d7b72)
- [isdn: clean up documentation index](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=952e57ba3769d6fc6139b8a99c32ea2bb63f23e9)
- [isdn: extend INTERFACE.CAPI document](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fe93299a008a7056fe1790744b3a425ddf79a16b)
- [ISDN: update Documentation/isdn/00-INDEX](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a0c31fdfb7f158780faa43ab83cc08b414bebd7e)
- [mISDN: Added layer-1-hold feature](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e73f6b2260daf02793071e5ce06ea87df762920a)
- [mISDN: Added PCI ID for new Junghanns.net Single E1 cards.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=daebafed7fef54fcc73d2d01431122cfd578d1e0)
- [mISDN: Add PCI ID for Junghanns 8S card](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7245a2fe3c10ed7c2e9b1c8a83af5919c0cc0a89)
- [mISDN: Add watchdog functionality to hfcmulti driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7df3bb8f59ca8e346bb834006c257cc367c6250a)
- [mISDN: Add XHFC support for embedded Speech-Design board to hfcmulti](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=db9bb63a1b5b65df41d112a8c21adbbfc6a4ac08)

**Miscellaneous:**

- [cdc_ether: additional PID's to the whitelist](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=68924920cb457ac44b14ca38343954bdcee046fc)
- [ethtool: Add port type PORT_OTHER](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0821c71751ef88f4251d7206e76ce497ee267a2d)
- [fcoe: adds spma mode support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=184dd3459bb334d9061b58faed3610d08d6c7ff8)
- [IPv6: Add 'autoconf' and 'disable_ipv6' module parameters](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=56d417b12e57dfe11c9b7ba4bea3882c62a55815)
- [irda: new Blackfin on-chip SIR IrDA driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d510fe70db4c62ac899c486506fdfb7f3b518c86)
- [irda-usb: suspend/resume support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e13f93188b8a3b418da2a02dfa1a46718cf4607b)
- [net: group address list and its count](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=31278e71471399beaff9280737e52b47db4dc345)
- [snmp: add missing counters for RFC 4293](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=edf391ff17232f097d72441c9ad467bcb3b5db18)
- [tcp: extend ECN sysctl to allow server-side only ECN](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=255cac91c3c9ce7dca7713b93ab03c75b7902e0e)

For other articles on 2.6.31 and links to the rest of the "Coming in 2.6.31" series, see The H's [Kernel Log - 2.6.31 Tracking](../site/open/features/Kernel-Log-2-6-31-Tracking-746446.html "Kernel Log - 2.6.31 Tracking – 02 July 2009, 11:21") page.

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
