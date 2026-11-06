---
title: "Kernel Log: What's coming in 2.6.28 - Part 3: Dodgy drivers"
date: 2008-10-22
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-3-Dodgy-drivers-737747.html
pages: 1
---

# Kernel Log: What's coming in 2.6.28 - Part 3: Dodgy drivers

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/4/5/1/8/a345f5e7c547062f.jpg) At the Kernel Summit a few weeks ago, kernel hackers accepted the "linux-staging" development tree into the main development tree ([1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=350455891377250cf7e0eadc5f9635decc1628af), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=dbc6c2ccb9f0abd6a19406718730ce0f715b2998)) ([Kernel-Summit](../site/news/item/Kernel-Log-Kernel-Summit-info-Plumbers-keynote-online-the-latest-on-the-e1000e-problem-737443.html "Kernel Log: Kernel Summit info; Plumbers keynote online; the latest on the e1000e problem – 26 September 2008, 10:59")). Greg Kroah-Hartman started [linux-staging a few months ago](../site/news/item/Kernel-Log-Linux-staging-branch-will-help-with-integration-Linux-kernel-2-6-25-6-and-2-6-26-rc6-735507.html "Kernel Log: Linux-staging branch will help with integration; Linux kernel 2.6.25.6 and 2.6.26-rc6 – 17 June 2008, 11:31") as a place to bring together open source drivers that are maintained independently of the official Linux kernel but do not satisfy the kernel developers' quality requirements. The aim of linux-staging is to offer developers a central platform on which to prepare the drivers for acceptance into the official linux kernel.

Now the kernel developers want to accelerate the improvement of these drivers, which have some serious problems in their code or in their design, within the main development tree. The idea is that the kernel hackers will have the code for these drivers easily available to them and will be able to contribute improvements over their normal channels. In order to separate mature from immature drivers, the code brought in from linux-staging has landed up in a new driver/staging/ folder.

There is a problem, though: how to make users and developers aware that there are staging drivers present. To handle this, when a staging driver is loaded, moreover, the kernel is marked as "TAINT_CRAP", so that when bug reports come in from users, it is clearly visible that a "dodgy" driver was loaded and may have been, at least partly, responsible for any problems ([1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=061b1bd394ca8628b7c24eb4658ba3535da4249a), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a9860bf05f4cb94f60f8f3459908d5621f75dd06)).

Of the approximately ten staging drivers now accepted into the main development tree, some are well-known ones that linux distributions have been delivering for years such as the [prism2_usb](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=00b3ed1685089ff52169a715de11106ed37df087) driver developed by the [WLAN NG Project](http://www.linux-wlan.com/linux-wlan/) and the [at76_usb](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=99e06e372378c5833a0c60274b645dfb2e4a4b08) driver for wireless chips by Atmel. We'll have to see whether this acceptance into the staging area of the official kernel will now stimulate more kernel hackers than before to feel a call to improve the drivers. Where the old, complex wireless driver is concerned, writing a new driver starting from scratch might possibly be the better approach.

Further commits relating to the acceptance of linux-staging:

- [Staging: add Alacritech slicoss network driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4d6f6af8d6e76443f298ac030b0fc4fe84bdbd6a)
- [Staging: add Kconfig entries and Makefile infrastructure](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=350455891377250cf7e0eadc5f9635decc1628af)
- [Staging: add sxg network driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5db6b777f68603bf5a9eab891d83413ad894a074)
- [Staging: add me4000 firmware files](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=cff338a9bd9d1acd6067d3ec93e846830e0b5974)
- [Staging: add me4000 pci data collection driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c0f005888c6663898a040cd922947dd8caa55160)
- [Staging: USB/IP: add host driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4d7b5c7f8ad49b7f01fb8aed83c560ac43cfbda8)
- [Staging: USB/IP: add client driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=04679b3489e048cd5dae79e050a3afed8e4e42b6)
- [Staging: USB/IP: add common functions needed](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=05a1f28e879e3b4d6a9c08e30b1898943f77b6e7)
- [Staging: add the go7007 video driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=866b8695d67e83f47194731d3a7ba55826a7ec70)
- [Staging: add w35und wifi driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=66101de10957e07a6fd0365d5af9adf650246d14)
- [Staging: Fix gcc warnings in sxg](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d63d692a44c918723895f792ffd17eab7bcfb8ef)
- [Staging: go7007 v4l fixes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=df20d69ec968b33526461457c219ad4ba8ba8ac8)
- [Staging: add echo cancelation module](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=10602db812fa270fc923f5e48fb47202288828f3)
- [Staging: SLICOSS: Fix warnings due to static usage](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4578ca0fc2be611ea98618b028ecfbb2415cd990)
- [Staging: SLICOSS: Fix remaining type names](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=68cf95f3183c7bd60feab3bb774e1e4c7f36fe71)
- [Staging: SLICOSS: Call pci_release_regions at driver exit](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f25fda728dfb5c23d1147279fc6a537451603369)
- [Staging: workaround build system bug](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=86f69fe9c069dd8608d238581eea259caa1dfc99)
- [Staging: Lindent sxg.c](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5c7514e0610249a4e7710eefd801c2b0442eb8ea)
- [Staging: SLICOSS: lots of checkpatch fixes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e9eff9d6a0d14fa2e85953ce4115d243ff575e78)
- [Staging: add et131x network driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=cfb739b459a4d982b75f5b92cbe7d2631999e206)

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: More than 10 million lines of Linux source files](../site/news/item/Kernel-Log-More-than-10-million-lines-of-Linux-source-files-737731.html "Kernel Log: More than 10 million lines of Linux source files – 21 October 2008, 14:50")
- [Kernel Log: Coming in 2.6.28 - Part 2: network infrastructure and network drivers](../site/news/item/Kernel-Log-Coming-in-2-6-28-Part-2-network-infrastructure-and-network-drivers-737711.html "Kernel Log: Coming in 2.6.28 - Part 2: network infrastructure and network drivers – 20 October 2008, 09:39")
- [Kernel Log: Coming in 2.6.28 - Part 1: ATA support and block layer](../site/news/item/Kernel-Log-Coming-in-2-6-28-Part-1-ATA-support-and-block-layer-737699.html "Kernel Log: Coming in 2.6.28 - Part 1: ATA support and block layer – 19 October 2008, 08:02")
- [Kernel Log: new Catalyst drivers, 2.6.27.1 resolves cause of e1000e problem](../site/news/item/Kernel-Log-new-Catalyst-drivers-2-6-27-1-resolves-cause-of-e1000e-problem-737701.html "Kernel Log: new Catalyst drivers, 2.6.27.1 resolves cause of e1000e problem – 18 October 2008, 08:02")
- [Kernel Log: Ext4 completes development phase as interim step to btrfs](../site/news/item/Kernel-Log-Ext4-completes-development-phase-as-interim-step-to-btrfs-737697.html "Kernel Log: Ext4 completes development phase as interim step to btrfs – 17 October 2008, 09:52")
- [Kernel Log: Linux 2.6.27 Released](../site/open/features/Kernel-Log-Linux-2-6-27-Released-746496.html "Kernel Log: Linux 2.6.27 Released – 10 October 2008, 08:38")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
