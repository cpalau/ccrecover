---
title: "Kernel Log: What's coming in 2.6.28 - Part 6: Changes to the audio drivers"
date: 2008-12-15
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-6-Changes-to-the-audio-drivers-739369.html
pages: 1
---

# Kernel Log: What's coming in 2.6.28 - Part 6: Changes to the audio drivers

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/5/8/0/1/93e8ea3d0acdf147.jpg) As the development of Linux kernel 2.6.28 is [approaching completion](../site/news/item/Kernel-Log-New-kernel-versions-progress-with-Btrfs-and-Tux3-739341.html "Kernel Log: New kernel versions, progress with Btrfs and Tux3 – 13 December 2008, 11:07"), this kernel log will mention a few changes that haven't made it into the "What's coming in 2.6.28" series so far. This includes the changes to the audio drivers – these drivers were already raised to the status of the Alsa development branch early on in the current development cycle, but were then updated several times. While the audio drivers of Linux 2.6.28 will roughly correspond to the Alsa driver version 1.0.18, they already include several minor improvements and corrections not yet contained in the latest version of the [official Alsa driver archive](http://www.alsa-project.org/main/index.php/Main_Page).

The changes incorporated into the main development branch include a [new userspace interface](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e76d8ceaaff9d7fc1ba2b1963a9f34151832223b) used by applications to detect which audio input or output devices are connected to which audio jacks (Jack Sensing). Also new is the [snd-usb-us122l](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=030a07e441296c372f946cd4065b5d831d8dc40c) driver for the Tascam US-122L USB Audio/MIDI Interface; the snd-virtuoso driver [can now also handle the Asus Xonar](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=7407a2e4b9e1fb3528bb355a571ee3eb7e32c386) HDAV1.3 and the Xonar HDAV1.3 Deluxe.

There is also added or improved support for the AC97 and HD audio codecs by various vendors – for example for [AD1882A](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9e44c6e40fb383e6b1d0df0c9e375a98e11828d1) and [AD1980](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5f57dc8b2a05f1d69f913fd885539b8c1f8fb8a1) by Analog Devices, [ALC662 and 663](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f1d4e28b2dbd35191cc5097b716ec7fa49540b0b) by Realtek, as well as [VT1708S and VT1702](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d949cac1ea8596f61942437ad741a3fbb412846f) by VIA. There are also many new drivers for the [ASoC](http://www.alsa-project.org/main/index.php/ASoC) (ALSA System on Chip) framework used particularly in embedded systems – for example drivers for the [WM8903](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f1c0a02f32f86f604d811876e748a405c68cc57d), [WM8580](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e88ba01544f8b8cce64d08b2982715516793225c), [WM8900](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0e0e16a87a0b973702feb572c2552d82e1aec5b9) and [WM8971](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8bae3e2335132aadd29662694866a55d52bff850) codecs by Wolfson Microelectronics.

As in almost every new kernel version, the developers extended the whitelists for the automatic application of specific hardware workarounds, which allows drivers to automatically apply the special treatment for audio codecs required with many PCs, notebooks and mainboards for more types of hardware than before – in 2.6.28, this includes the [Dell Studio 15](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b0fc5e043401df4cd243352f1030c4d23e767347), the [HP Compaq 6730s](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=65b92e5cbc8acd14ea83190b4d016f765dce6075) and the [Medion MD96630](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=959973b92d3ba235edfa5dcb5df1be1e5d1deba2). On the other hand, the kernel developers removed the [hal2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2470e93c5515606a5cf44dd046f1a69e91ae23db) OSS driver. OSS emulation in the Alsa soundcore model is now [optional](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d886e87cb82b0f6636476c1104bb84d7c8dc87d9), which allows alternative implementations – like the as yet experimental [OSS proxy](http://userweb.kernel.org/~tj/ossp/), which is based on the equally experimental CUSE ([character devices in user space](http://thread.gmane.org/gmane.linux.kernel/759831/)) (see also the [article on LWN.net](http://lwn.net/Articles/308445/)). Apart from Jaroslav Kysela, who has been working for Red Hat for several months now, the kernel sources now also officially [list](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=281712fa02bfb196d915503787e3ad351ed1be0a) Alsa developer and Suse employee Takashi Iwai as an audio driver maintainer.

Further commits in connection with the audio drivers:

- [ALSA: ac97 - vt1618 7.1 Audio Support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9e285e1a58bcf957cde9c0c559a1b9b0f708bb2f)
- [ALSA: Add jack reporting API](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e76d8ceaaff9d7fc1ba2b1963a9f34151832223b)
- [ALSA: ALS4000 driver work, step 2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=cb780cdd85b8ae408245883ae44172ed1ed34439)
- [ALSA: ALSA-Configuration.txt: supported cards update](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6ef109050da99952b59397840e9b50cd6611e92a)
- [ALSA: ASoC: Add all CODECs Kconfig option](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0c94161580eee8137b868301434ea392083258b5)
- [ALSA: ASoC: Add mpc5200-psc I2S driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=dc641378b5ee220aa29ed8b8f51b7af9a19a7719)
- [ALSA: ASoC: Add OpenFirmware helper for matching bus and codec drivers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=84bc278b1f04920e867e4b46e094bcc066393d41)
- [ALSA: ASoC: Add SPI support for WM8731](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d2a403553ba7659d85dae2a05b1f3767d2fefcfe)
- [ALSA: ASoC: Add Texas Instruments TLV320AIC26 codec driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d8e3bb7385da0bcdda4ffa600489fa1439b14673)
- [ALSA: ASoC: Add TLV320AIC23 codec driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c1f27190a72e9310f1777261b33a05319ff2822c)
- [ALSA: atiixp - Add PCI ID for SB600 (1002:4382)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f4446ea046cf719a6d79449bb9175d50a64d963b)
- [ALSA: Build jack detection](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0d94e41abe271c86df06bcf72d24f9ca7ce771f0)
- [ALSA: cs46xx: Add PCI IDs for TerraTec and Hercules cards](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b636a1d947c7f1bb0e0a157663e08ce3e49b2e52)
- [ALSA: Fix commit: Add automatic model setting for the Acer Aspire 5920G laptop](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0b18cb1854152a62492aae088cb80cbeb5c0288d)
- [ALSA: hda: 92xx S/PDIF In support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b2c4f4d71f7a161630681678cbba84bd695bfd1e)
- [ALSA: hda - Add ALC1200 support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4442608d4b0071a00067dcbf64e7362ce08e91a5)
- [ALSA: hda - Add ALC887 support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a385a52925398e53bedf1a8b30a9a3e002569f27)
- [ALSA: hda - Add a quirk for another Acer Aspire (1025:0090)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=69e50282b726bab75c8050c4836dc89b7eb7bf1a)
- [ALSA: hda - Add another HP model for AD1884A](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5695ff44160e62d9193c0201706853bcfe2a077f)
- [ALSA: hda - Add definitions of HDMI-related verbs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=955d24881e13a08b9f523f36ae61a58245b8968e)
- [ALSA: hda - Add digital-mic for ALC269 auto-probe mode](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ee956e090e114ede6542c76a7465ed6ce118ad52)
- [ALSA: hda: added 92HD81/83 support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d0513fc6c37b009004cf5c7a8e90af0adb3755bc)
- [ALSA: hda: Add HDA vendor ID for Wolfson Microelectronics](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8199de3b29d7f22f3163fcf03f7a61644c93c2ea)
- [ALSA: hda - Add missing analog-mux mixer creation for STAC9200](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=355a0ec471377a8a907b79c8fba3f0f09b44656e)
- [ALSA: hda - Add model for Toshiba L305 laptop](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2346d0cde544179a8d235375f1bfbca5c141a31b)
- [ALSA: hda - Add PCI subsystem ID for MacBookPro4,1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9c95c43de81d5556237fbc82c4e90403dfe468db)
- [ALSA: hda - Add quirks for HP Pavilion DV models](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=80bf272468a8b63f5550304363e55c1ba06c13db)
- [ALSA: hda - Add reboot notifier](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0cbf00980f0fc4cc064a15ab3dfce19b5fae9130)
- [ALSA: hda: Add STAC_DELL_M4_3 quirk](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3a7abfd2ba26479615b81ac5e90d0122ef7f9fe0)
- [ALSA: hda: Add support for ECS/PC Chips boards with Sigmatel codecs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8c650087992f1d7a3a7be2e632f4e85a52d20619)
- [ALSA: hda - Add support of Acer Aspire One](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8ef355da64ff087b6f26c4c28a14753861e83e4b)
- [ALSA: hda - Add support of ALC272](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=01afd41f55524e8378601dbf33b858d8dd4b3f31)
- [ALSA: hda - Add support of HP DC7600](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3f8783084aa03d04e7757ced337fa415744489a5)
- [ALSA: hda - Add support of Quanta FL1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=60db6b53fb43421beb2ff3fe3e63412bf81620aa)
- [ALSA: hda - Add support of Toshiba RX1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9f99a6386eb1ad1197a401495669315de2f19039)
- [ALSA: hda - Add support of Toshiba S06](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4e555fe5475437f5c05b9e1812959bf6d5cd50b9)
- [ALSA: hda: appletv support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f3911c5ab93e4295938b2013104d2986ea601454)
- [ALSA: hda - Check model for Dell 92HD73xx laptops](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=661cd8fb5210af78f0763071642e0764a10389a6)
- [ALSA: hda: digital pc-beep support hd-audio codecs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1cd2224cd01898a13138f4ab476932cfb689839e)
- [ALSA: hda - Fix conflicting volume controls on ALC260](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=863b45180ef541a1990e4986d30fb7a93022a733)
- [ALSA: hda - Fix IDT/STAC multiple HP detection](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d7a8943635485597ae7c6d554a8ccf3ce5a42d2d)
- [ALSA: hda - Fix PCI SSID of ASUS M90V](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a01c30cb77aa7b80ea08d003783fb9f0470455ee)
- [ALSA: hda - Fix PCM type of Nvidia HDMI devices](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ec4e86ba0662ed85f3b3a38fb220dc51d951da84)
- [ALSA: hda - Fix quirk lists for realtek codecs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=80ffe86925a226f513b36d0ce13e049133841970)
- [ALSA: hda - Fix sound on NEC Versa S9100](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e8f9ae2a4a0654e7798b8c0ae956e3f0fdc23c8d)
- [ALSA: hda - Fix SPDIF mute on IDT/STAC codecs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c1e99bd9d6a0c82f4fa9078ed1f570e57b2f3944)
- [ALSA: hda: HP laptop quirk](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9a9e2359f484402c620f9a3748037fea65fa5af4)
- [ALSA: hda - Make the HP EliteBook 8530p use AD1884A model laptop](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=254248313aed7e6ff295ca21a82ca989b1f69c16)
- [ALSA: hda - Map ALC662 model for Foxconn 45CMX/45GMX/45CMX-K](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=95fe5f2cec831d73ee93227810ab95d05ced3416)
- [ALSA: hda - Map ALC662 model for Gigabyte 945GCM-S2L](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=cb55974cb461ff9c9c0675b2a8361d387212b64f)
- [ALSA: hda - mark Dell studio 1535 quirk](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c65574abad288d7123bd49e7906fa53b7e420239)
- [ALSA: hda - No 'Headphone as Line-out' swich without line-outs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=95026623da32848bc93fbfb472dc8737487df450)
- [ALSA: HDA patch_via.c: Fix inversion of surround and side channels](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fb4cb772c0b22f7bce0b151ef5712e80d434bc97)
- [ALSA: HDA patch_via.c: Second S/PDIF (HDMI) support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=98aa34c0501f78bf7d3de82d96d27f4a2b450477)
- [ALSA: hda - print a few HDMI information in proc](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c4920606757224d0c480f25839f1cef6901a2167)
- [ALSA: hda - put all HDA codec IDs to components for precise hw detection](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ba443687f2eb70d23e0466d4b7c0c3366b5cb5fb)
- [ALSA: hda - Restore default pin configs for realtek codecs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e044c39ae258678d6ebb09fccb2a0fdf7ec51847)
- [ALSA: hda - set up HDMI channels](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=862f76f86d64c2cf34a7ff5ddf0a175073b76534)
- [ALSA: hda: STAC_DELL_M6 EAPD](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0253fdcd8aec2f954c2950a7454c0a2f3207e9a1)
- [ALSA: hda - support more ALC888 devices](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e2757d5efad01dae6986e1f84590898e47231964)
- [ALSA: ice1724: enable MIDI on Terratec Aureon 7.1 Universe](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c1805dddc9fbd65e831963f671bfb79384e8b3b8)
- [ALSA: ice1724 - Support for Terrasoniq/MUSONIK TS22 PCI card](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=740dc9c4766b462ae88a630e969ddd3ef83a6125)
- [ALSA: intel8x0 - add Dell Optiplex GX620 (AD1981B) to AC97 clock whitelist](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=78fad343a4fd4c837e3034dcbca13269a783e0f6)
- [ALSA: intel8x0 - Add quirk for Fujitsu Lifebook P7010](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=37c34ffb3a9a6051236a4ee1acb7752bcc3f50fd)
- [ALSA: ps3: Add support for SPDIF/HDMI passthru](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1ee2a322b058f6399dc900603f9ebb392037ff77)
- [ALSA: snd-ad1816a: add different TerraTec EWS64 S model](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=36463a9660a69018c98f6bde93183a523667e598)
- [ALSA: snd-cs4236: add Techmakers MF-4236PW PnP card ID](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ebae22590dccd2b8495c97e85290f5e07af7dc62)
- [ALSA: sound/pci: supported cards update](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a2854dc5f0e1145a38e10c67064a776d84e56f5d)
- [ALSA: Support NVIDIA MCP78/7A HDMI audio](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9a10eb21e1e1c389a8cea3016157a7f471512645)
- [ALSA: usb-audio: add BOSS GT-10 support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b38addb2da26c0eeab5b538cfbd9d306c50a4726)
- [ASoC: Blackfin: board driver for AD1980/1 audio codec](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c4cf8c79c14b56e8025680b95ac7dc2583654212)
- [ASoC: Blackfin: board driver for SSM2602 sound chip](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a7e7f54f984a5c048c328216089e6cb8a9ca39bd)
- [ASoC: Blackfin: DMA Driver for AC97 sound chip](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=aff0510c00523bfd9fab20923a493ce8a6f27cda)
- [ASoC: Blackfin: SPORT peripheral interface driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8c9c198347e39b5bcf52399989885991a5cdbaff)
- [ASoC codec: SSM2602 audio codec driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b7138212a8aa90115bd9197d5b6cd89a282184f9)
- [ps3: Add passthru support for non-audio streams](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=64931a4be03dbc49bd50d10d211592cf98b523bb)

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: New kernel versions, progress with Btrfs and Tux3](../site/news/item/Kernel-Log-New-kernel-versions-progress-with-Btrfs-and-Tux3-739341.html "Kernel Log: New kernel versions, progress with Btrfs and Tux3 – 13 December 2008, 11:07")
- [Kernel Log: VIA co-operates with the open source developers of openChrome](../site/news/item/Kernel-Log-VIA-co-operates-with-the-open-source-developers-of-openChrome-738911.html "Kernel Log: VIA co-operates with the open source developers of openChrome – 21 November 2008, 14:56")
- [Kernel Log: New graphics drivers and Linux versions: Dom0 patches for 2.6.29?](../site/news/item/Kernel-Log-New-graphics-drivers-and-Linux-versions-Dom0-patches-for-2-6-29-738149.html "Kernel Log: New graphics drivers and Linux versions: Dom0 patches for 2.6.29? – 17 November 2008, 13:14")
- [Kernel Log: What's coming in 2.6.28 - Part 5: updates for netbooks and notebooks](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-5-updates-for-netbooks-and-notebooks-738121.html "Kernel Log: What's coming in 2.6.28 - Part 5: updates for netbooks and notebooks – 14 November 2008, 12:51")
- [Kernel Log: New kernels, open audio drivers for X-Fi](../site/news/item/Kernel-Log-New-kernels-open-audio-drivers-for-X-Fi-738061.html "Kernel Log: New kernels, open audio drivers for X-Fi – 11 November 2008, 10:03")
- [Kernel Log: Short video interviews with Torvalds, Kroah-Hartman and others](../site/news/item/Kernel-Log-Short-video-interviews-with-Torvalds-Kroah-Hartman-and-others-737833.html "Kernel Log: Short video interviews with Torvalds, Kroah-Hartman and others – 28 October 2008, 15:46")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
