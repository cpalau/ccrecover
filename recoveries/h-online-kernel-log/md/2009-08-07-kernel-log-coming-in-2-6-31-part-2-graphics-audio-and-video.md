---
title: "Kernel Log - Coming in 2.6.31 - Part 2: Graphics, audio and video"
date: 2009-08-07
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-Coming-in-2-6-31-Part-2-Graphics-audio-and-video-742867.html
pages: 1
---

# Kernel Log - Coming in 2.6.31 - Part 2: Graphics, audio and video

**Dj Walker-Morgan**

![Kernel Log Penguin](../site/imgs/43/3/6/9/2/9/8/93e8ea3d0acdf147.jpg)

#### Thorsten Leemhuis

**Linux 2.6.31 will offer Kernel-Based Mode-Setting for Radeon graphics cards up to model X1950. The developers have included new drivers for X-Fi sound cards and for Intel's "Next-Generation Graphics Device". Many further improvements affect the drivers for webcams and TV hardware.**

Despite the summer holiday season in the northern hemisphere, the development of the kernel has continued without interruption, and [the fifth release candidate](http://thread.gmane.org/gmane.linux.kernel/871932) of Linux 2.6.31 has already become available. This version contains the gspca/sn9c20x webcam driver, which still managed to sneak in although the merge window has long been closed. However, this is only one of many changes in the audio and video area of Linux 2.6.31.

For other articles on 2.6.31 and links to the rest of the "Coming in 2.6.31" series, see The H's [Kernel Log - 2.6.31 Tracking](../site/open/features/Kernel-Log-2-6-31-Tracking-746446.html "Kernel Log - 2.6.31 Tracking – 02 July 2009, 11:21") page.

### Flicker-free X startup for Radeon graphics chips

Having added the Intel-specific GEM (Graphics Execution Manager) to the kernel [with Linux 2.6.28](../site/open/features/Kernel-Log-Higher-and-Further-The-innovations-of-Linux-2-6-28-746519.html "Kernel Log: Higher and Further, The innovations of Linux 2.6.28 – 23 December 2008, 15:55") and Kernel-Based Mode-Setting (KMS) support, which is based on GEM, [with 2.6.29](../site/open/features/Steady-growth-What-s-new-in-Linux-2-6-29-746553.html "Steady growth - What's new in Linux 2.6.29 – 24 March 2009, 15:26"), the developers have now integrated [KMS code for Radeon graphics chips](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=771fe6b912fca54f03e8a72eb63058b582775362) by AMD/ATI. To benefit from the advantages of KMS – central graphics management in one place, improved suspend, and less complex graphics drivers – and get the X Server to work with KMS, it is necessary [to update](http://airlied.livejournal.com/66958.html) the X.org drivers, Libdrm, and Mesa3D. This involves considerable installation and tuning which is best left to the Linux distributor of your choice.

Masterminded by the programmers of the "radeon" X.org driver, the newly integrated KMS code supports Radeon GPUs up to series R5XX – this includes all Radeon models up to and including X1950. The development of KMS for the R6xx and R7xx GPUs of the Radeon HD series 2000, 3000 and 4000 is still in progress. However, even the Radeon KMS code integrated with 2.6.31 hasn't reached full maturity yet; as a result, the developers have marked it as a staging driver for now.

Instead of GEM, the Radeon KMS code uses another new addition, the [TTM GPU memory manager](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ba4e7d973dd09b66912ac4c0856add8b0703a997), for managing the memory and for coordinating access to the processing units. While TTM was originally also intended to be used with the Intel KMS driver, the Intel developers weren't too happy with it and [started GEM](http://lwn.net/Articles/283793/) as an alternative. However, the TTM code has since been overhauled and can now also be used via a GEM API.

### Drivers for next generation Intel GPUs

The [developers extended](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a4fc5ed69817c73e32571ad7837bb707f9890009) the Intel KMS driver to support monitor control via DisplayPort (DP). In addition, they made numerous corrections to improve the existing KMS and GEM code – as a result, the [recently released](../site/news/item/Kernel-Log-X-server-1-7-delayed-Compiz-runs-on-newer-Radeon-GPUs-DRBD-in-kernel-soon-742829.html "Kernel Log: X server 1.7 delayed; Compiz runs on newer Radeon GPUs; DRBD in kernel soon – 05 August 2009, 16:55") version 2.8 of the X.org driver reportedly works best with Linux 2.6.31.

The Intel crew also contributed further [KMS code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2c07245fb8f7f0a282282e5a9747e46defdb2cc7) and other patches to support a series of graphics chips named IGDNG. This is probably short for "Intel Graphics Device Next-Generation" and refers to the graphics cores of the processors expected early next year.

Information about these and other changes concerning the kernel's graphics support can be found at the end of this article and in several of Dave Airlie's git pull requests ([1](http://thread.gmane.org/gmane.comp.video.dri.devel/36317/), [2](http://thread.gmane.org/gmane.comp.video.dri.devel/36382), [3](http://thread.gmane.org/gmane.comp.video.dri.devel/36439), [4](http://thread.gmane.org/gmane.comp.video.dri.devel/37335)).

### Audio drivers for X-Fi

Suitable for [various sound cards of Creative's X-Fi series](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8cc72361481f00253f1e468ade5795427386d593) and mainly developed by Creative programmers, the [snd-ctxfi driver](../site/news/item/Kernel-Log-New-kernels-open-audio-drivers-for-X-Fi-738061.html "Kernel Log: New kernels, open audio drivers for X-Fi – 11 November 2008, 10:03") [has found its way into the kernel](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8cc72361481f00253f1e468ade5795427386d593) via the ALSA developers. This puts an end to a driver odyssey which had several mostly half-finished versions of both [open source and proprietary drivers](../site/news/item/Creative-Labs-opens-up-driver-development-734163.html "Creative Labs opens up driver development – 09 February 2008, 13:08") and gave us futile hopes for a half-way decent Linux driver for X-Fi sound chips in the past few years. However, the newly integrated driver is not fully mature yet; for instance, it doesn't support external I/O modules.

[Also new](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=02bec490450836ebbd628e97ec03f10b57def8ce) is the lx6464es audio driver for various LX6464ES models by Digigram. In addition, the kernel now supports [ESI's Maya44](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=72cbfd45fac627de4bd38c203baaac40cd26477c) as well as numerous PCs and notebooks – among them the [MacBook 5.1 (Aluminium)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=41d5545d23d2ccf4d34725094dccebd37f15c1c4). As in every other new kernel version, the developers have also considerably extended the whitelists for automatically applying special hardware-specific settings ("quirks") – most of the relevant commits are appended in a list at the end of this article. One of the maintainers of the audio subsystem has summarised the most important new aspects of 2.6.31 [in an email](http://thread.gmane.org/gmane.linux.kernel/849085).

### Video

As usual, hundreds of changes were made to the DVB/V4L subsystem. One new addition is the [stv090x](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e415c689a8842670e161581f060575c14957f073) driver for addressing the Intersil DVB-S/S2/DSS chips found on cards like the TechnoTrend TT-budget S2-1600. [Another addition](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=26e744b6b61066203fd57de0d3962353621e06f8) is the gspca-sn9c20x driver for sn9c201 and sn9c202 USB chips, which are used in the [webcams of various manufacturers](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blobdiff;f=Documentation/video4linux/gspca.txt;h=573f95b588079b6ae1ede70f479cf539e397e2eb;hp=2bcf78896e225a191cc58c23d8636ad92365ecd7;hb=26e744b6b61066203fd57de0d3962353621e06f8;hpb=af1d9afa75082663ea9e2b67b9381d1af403f52b). The new kernel will offer [improved support](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8668d504d72c384fbfb6ab6f5d02a9fe4d813554) for several webcams of Logitech's QuickCam Messenger series; the ov519 gspca driver now also works with the [ov511](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1876bb923c98c605eca69f0bfe295f7b5f5eba28) and [ov518](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=49809d6a511960e5ccfb85b780894f45ac119065) chips. Further background information about the changes to the Linux 2.6.31 webcam and TV drivers can be found in the git pull requests made by the maintainer of the V4L/DVB subsystem, Mauro Carvalho Chehab ([1](http://thread.gmane.org/gmane.linux.drivers.video-input-infrastructure/6914), [2](http://thread.gmane.org/gmane.linux.drivers.video-input-infrastructure/7262), [3](http://thread.gmane.org/gmane.linux.drivers.video-input-infrastructure/8201)).

### Minor gems

Many additional minor, but by no means insignificant, changes can be found in the list below. Like many of the references in the text above, the links lead to the relevant commits in the [web front end](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=summary) of the main Linux development branch, where the commit comments and the patches themselves provide extensive further information on the respective changes.

**Audio:**

- [ALSA: Add missing description of lx6464es to ALSA-Configuration.txt](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8338c300642f67af5a8cc279ca5e088c7055b7eb)
- [ALSA: bt87x - Add a quirk entry for Askey Computer Corp. MagicTView'99](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3f08a0e4ab1ce65bb882f6425ff482e5db025f78)
- [ALSA: ctxfi - Add depends on X86](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3e3ee6dc949d25423f72bb5ee5f58dfa79ac85c7)
- [ALSA: ctxfi - Add PM support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=29959a09cc1aabd2d5f4f03afc0305de6bd29248)
- [ALSA: ctxfi - Allow unknown PCI SSIDs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a8f4310be59a2e7fc80fba945bcb32b18f4ad54f)
- [ALSA: ctxfi - Fix endian-dependent codes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=42a0b31827e4c555efebda7d347cf4ea6b82913a)
- [ALSA: ctxfi - Remove PAGE_SIZE limitation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cd391e206f486955e216a61bd9ebcb0e142122e9)
- [ALSA: hda - Acer Aspire 8930G support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3b315d70b094e8b439358756a9084438fd7a71c2)
- [ALSA: hda - Acer Inspire 6530G model for Realtek ALC888](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d2fd4b09c07ae0c5ac288c0da6100c26ba9db15b)
- [ALSA: hda - Add 7.1 support for MSI GX620](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=64a8be74357477558183b43156c5536b642de134)
- [ALSA: hda - Add a quirk entry for Macbook Pro 5,1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7442f9dadb8626bd9e7e01445560499560b99f5d)
- [ALSA: hda - Add Creative CA0110-IBG support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4e01f54bfd3f423db8fd6c91c4f0471f18aa0c50)
- [ALSA: hda - Add digital-mic support to ALC262 auto model](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8c927b4acf819ed0170bff991bc9eaec4c85deb8)
- [ALSA: hda - Add GPIO1 control at muting with HP laptops](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=099db17e66294b02814dee01c81d9abbbeece93e)
- [ALSA: hda - Addition for HP dv4-1222nr laptop support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=514bf54cd8c7f172816d3c003a6d022e9165a29b)
- [ALSA: hda - Add missing initializations for ALC268 and ALC269](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1d955ebd4db7961dc4e772a23288b3d5c6f191be)
- [ALSA: hda - Add missing models for Realtek codecs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=01f2bd48d08c6bbde12d86b66c760612e33e49a9)
- [ALSA: hda - Add model=6530g option](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b1a914690c581f8f88b897d83a79b1c6eaf494c9)
- [ALSA: hda - Add pci-quirk for MSI MS-7350 motherboard.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=df01b8af5627b7e28c087559cbce4f359ce07c49)
- [ALSA: hda - Add pin-sense trigger when needed for Realtek codecs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=261c2407401ca26fa17f05667ea68f51e12c5303)
- [ALSA: hda - Add quirk for Acer Aspire 6935G](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e46b0c8c08cd97eb8f9a523986908add3ece0cc6)
- [ALSA: hda - Add quirk for Dell Studio 1555](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=626f5cefc60b281a00db1402b82deff82080c70a)
- [ALSA: hda - Add quirk for Gateway T6834c laptop](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=42b95f0c6b524b5a670dd17533a3522db368f600)
- [ALSA: hda - Add quirk for HP 6930p](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ff84847171508a3c76eb7e483204d1be7738729b)
- [ALSA: hda - Add quirk for Sony VAIO Z21MN](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=376b508ffde3b17e105265f89b83bdb044b1c1ae)
- [ALSA: hda - add quirk for STAC92xx (SigmaTel STAC9205)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a5c0f88678cd2fb1f649f7d366d756f2b2f97f0c)
- [ALSA: hda - Add support of Samsung NC10 mini notebook](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9541ba1d665542c96f7c0b5b836bbc1fd9d961b6)
- [ALSA: hda - Avoid conflicts with snd-ctxfi driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=313f6e2d40bd67e394a65e7d64acd0cf9c9d248d)
- [ALSA: hda - Clean up Realtek auto-mute unsol routines](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a9fd4f3fcdc7e5757424f7e5888f660cf34bb1a9)
- [ALSA: hda: Correct EAPD for Dell Inspiron 1525](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=84d3dc200fc8b878acf7c1840b238e6a0450e4d0)
- [ALSA: hda - Fix acer-aspire-6530g model quirk](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=320d592001acbfd76bf856b5370319f144285489)
- [ALSA: hda - Fix pin-setup for Sony VAIO with STAC9872 codecs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b04add956616b6d89ff21da749b46ad2bd58ef32)
- [ALSA: hda - Fix quirk for Toshiba Satellite A135-S4527](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ce577e8cf5ddb4216553c9d563a9835d6de70ffa)
- [ALSA: hda - Fix secondary SPDIF on VT1708S and VT1702 codecs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9da29271bea5d831d745f3ceb7f6f6b2def13a5b)
- [ALSA: hda - Fix support for Samsung P50 with AD1986A codec](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c912e7a58054304575fe88574c776be7e684098e)
- [ALSA: hda - Generalize the pin-detect quirk for Lenovo N100](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=03c405ad314d3c4e049b8d04500e54e833d16747)
- [ALSA: hda - Get back Input Source for ALC262 toshiba-s06 model](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ae14ef68e8e67ca5b8b29f0eb640f7c106617f4e)
- [ALSA: hda - Improve ASUS eeePC 1000 mixer](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=aa202455eec51699e44f658530728162cefa1307)
- [ALSA: hda - Improved MacBook 3,1 support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=eb4c41d30ba1f973c8b10be3644571ab997ae0d6)
- [ALSA: hda - Line In for Acer Inspire 6530G model](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=684a88429c5ab04d8b1894de9a1ef62de6f601b7)
- [ALSA: hda - Macbook\[Pro](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=92b9de8342c6ad0d930333851190ed25b88b190c) 5 6ch support\]
- [ALSA: hda - Make jack-plug notification selectable](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8c8145b8734028f6deb487f7d64748da4c6c39ac)
- [ALSA: hda - More Aspire 8930G fixes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=018df41861475595a51d327b83fb5830462f7a53)
- [ALSA: hda - Support NVIDIA 8 channel HDMI audio](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a3d6ab9723060e8d67e28a8d9142e6d08953d07b)
- [ALSA: hda - Use model=acer-aspire-6530g for Acer Aspire 6930G](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=dde6535686aa4e78e8b85850d1f3fccd8a581622)
- [ALSA: hdsp - Add a comment about external firmwares for hdsp](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=511b4c171a8054506e8898c40833e31270689b8b)
- [ALSA: hdsp: allow firmware loading from inside the kernel](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8e365f9b6e583e82dff96ff415ff9cc2106f5b3c)
- [ALSA: lx6464es - support standard alsa module parameters](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=de0525ca34aa7a65faf6902e3e00956ab80d2ede)
- [ALSA: pcm - Add logging of hwptr updates and interrupt updates](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cedb8118e8cef21a2b73fd9cb70660ac19124c16)
- [ALSA: sc6000: add support for SC-6600 and SC-7000](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c282866101bfde888a44da3babd2f9ab265ca6f9)
- [ALSA: support Sony Vaio TT](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3e1647c5b54a91a7182e121cfe569e6f0bf167ec)
- [ALSA: usb - Add boot quirk for C-Media 6206 USB Audio](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=92a43793a908f395dc687e6c5fc90d63f999d6d5)
- [ALSA: usb-audio - Add quirk for Roland/Edirol M-16DX](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6efd2cd5e8c566b9c2b4c19830e5e120b442d040)
- [ALSA: usb-audio - quirk for USB Aureon cards](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=93bfd01227408a62006a4e4f640a6056abc6af7a)
- [ALSA: usb-audio - Volume control quirk for QuickCam E 3500](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2cf313ee75ddf6220b5d623b749b1bb79458307f)
- [ALSA: via82xx: add option to disable 500ms delay in snd_via82xx_codec_wait](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=115551d98e4c05bb982bd940f08a489fa9b0a4a1)
- [sound: virtuoso: add another DX PCI ID](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=53bb705d12e0f642c131cdcab2c8e3be7364e505)
- [sound: virtuoso: add Xonar Essence ST support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=04f9890df1bad2115665b7027e664aaffa44088d)
- [sound: virtuoso: enable HDAV S/PDIF input](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b990ae963a3f80a659b30562c1e3214b386ecce3)
- [sound: virtuoso: fix Xonar D1/DX silence after resume](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=826390796d09444b93e1f957582f8970ddfd9b3d)

**Audio - Asoc:**

- [ASoC: AC97 driver for mpc5200](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=20d0e1520ed1ba8aad05f416245446de0f7ec4bb)
- [ASoC: Add driver for s6000 I2S interface](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4b166da939012905f4c36fedada62067db31948e)
- [ASoC: Added OMAP3 EVM support in ASoC.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=14610ce711a363028ffffad98947d57f21fa5372)
- [ASoC: Add TXx9 AC link controller driver (v3)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e24805dd85283ac0912b9c400768a4d171b400ff)
- [ASoC: Add WM8960 CODEC driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f2644a2c00a06236a9c5e85488b0680825bad39c)
- [ASoC: Add WM8988 CODEC driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5409fb4e327a84972483047ecf4fb41f279453e2)
- [ASoC: AFEB9260 driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b4df0a6c9d88cfff77c73d33873cd60f9ab909b6)
- [ASoC: em-x270: make the driver support also eXeda and CM-X300 machines](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=eaaa5328835d8085d24221a0e5ceaacbe14a7523)
- [ASoC: IMote2 ASoC Support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a195b51bc5abc745f12b7b2fe0e3422f55c1953f)
- [ASoC: remove BROKEN from Efika and pcm030 fabric drivers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=40d9ec14e7e1f62d2379ecc1b5ee00ddfc2a5d0c)
- [ASoC: s6105 IP camera machine specific ASoC code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2b7dbbe0c9491e62b50978d1615193bec33a8291)
- [ASoC: Support for AC97 on Phytec pmc030 base board.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a9262c4fd404654acd3684699047fa63206518c8)
- [ASoC: WM8940 Driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0b5e92c5e020ee7437fa5304a8451d6dd08d1a26)
- [ASoC: WM9081 mono DAC with integrated 2.6W class AB/D amplifier driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=86ed3669f068b514ab85ffd548456a342b3fb8d3)

**Graphics:**

- [agp/intel: Add support for new chipsets](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=32cb055b57eab803ea82b76dc913b0378e5af145)
- [agp: switch AGP to use page array instead of unsigned long array](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=07613ba2f464f59949266f4337b75b91eb610795)
- [drm/i915: Add chipset/feature defines for for new chipsets](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=280da227c870a50f669de0c8d46bfb2c62da9995)
- [drm/i915: Add Display Port register defines](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=040d87f15a0129242463d3ed7c48381505f596e2)
- [drm/i915: add FIFO watermark support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7662c8bd6545c12ac7b2b39e4554c3ba34789c50)
- [drm/i915: Add HDMI support on IGDNG](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=30ad48b7334a2eb2edf22f6c91f7b3f22a22a837)
- [drm/i915: Add LVDS support for IGDNG](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=541998a18b72d2cac48b3369fa4540116ff3f0a8)
- [drm/i915: Add new chipset register definitions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b9055052d3e0388b4a5e8c3e0bbab665c5996f50)
- [drm/i915: add per-output hotplug callback for KMS](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c31c4ba3437d98efa19710e30d694a1cfdf87aa5)
- [drm/i915: enable error detection Commit: 63eeaf38251183ec2b1caee11e4a2c040cb5ce6c state collection](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=63eeaf38251183ec2b1caee11e4a2c040cb5ce6c)
- [drm/i915: enable GEM on PAE.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=95934f939c46ea2b37f3c91a4f8c82e003727761)
- [drm/i915: Save/restore cursor state on suspend/resume.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1fd1c624362819ecc36db2458c6a972c48ae92d6)
- [drm/radeon: add rv740 drm support.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2a71ebcd85bcc4d6607f577f23a491f796c30e82)
- [drm/radeon: add some missing pci ids](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=069a9dce384e211784ce6fdfaf1f13921327480d)
- [drm/radeon: add some new r7xx pci ids](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7320700df1864b601cef5adbddce8654a0e3f78b)
- [drm/radeon: add support for RV790.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=715cbb05c935e8a4306a730d14a72d5af881523e)
- [drm/radeon: command stream checker for r3xx-r5xx hardware](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=068a117ca38f27c9641db7642f24fe9270d9424e)
- [drm/radeon: fix mobility flags on new PCI IDs.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=602c11a8ee62d49cddbc5972e5edb876dd415113)
- [drm/radeon/kms: add initial colortiling support.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e024e11070a0a0dc7163ce1ec2da354a638bdbed)
- [drm: Remove memory debugging infrastructure.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9a298b2acd771d8a5c0004d8f8e4156c65b11f6b)
- [fbdev: do not allow VESA modes without compiled-in drivers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4b1982896876872d30493cca9477975b62335f39)
- [fb/intelfb: conflict with DRM_I915 and hide by default](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ba0ab82358a12e7a7f2872d6b65c437157c6888f)
- [MAINTAINERS: fbdev is orphaned](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=36025a812eebb34a478cfc1d3a538472591498b0)
- [ps3av: Set 16:9 aspect ratio for 720p video modes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7a4a89c38960591fa6555d287f793bd592c07ebd)
- [s3c-fb: CPUFREQ frequency scaling support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0dac6ecdc056b83ac66e5b5c923fb73268f4332d)

**V4L/DVB:**

- [V4L/DVB (11239): sdio: add cards ids for sms (Siano Mobile Silicon) MDTV receivers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ecfe0cfa3cae9a8402df12d81b159d851b61cf29)
- [V4L/DVB (11394): cx88: Add support for stereo and sap detection for A2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e878cf3a47a5d99635edc564423a9a4469c17810)
- [V4L/DVB (11442): saa7134: BZ#7524: Add AVerTV Studio 507UA support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=df0dbbe24053b7c669f63341d3d3f090560c3217)
- [V4L/DVB (11483): gspca - mr97310a: Webcam 093a:010f added.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ebf58f70e853b9ffe50d6b194d3679b7dc2cac9c)
- [V4L/DVB (11486): em28xx: Add EmpireTV board support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e5db5d44432abc82b1250dd05bd0a4b011392d9d)
- [V4L/DVB (11491): af9015: support for AverMedia AVerTV Volar GPS 805 (A805)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1ed5fadec7728282466d0203851cf811864b42f7)
- [V4L/DVB (11492): af9015: support for Conceptronic USB2.0 DVB-T CTVDIGRCU V3.0](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=734dd236a6045ca764d12ed0fd6a7c1e9a928ac1)
- [V4L/DVB (11535): gspca - m5602-po1030: Add experimental QVGA support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=931a1c8dbf71d851d9d4e4dbdedc192bcc9e98c1)
- [V4L/DVB (11544): gspca - m5602-mt9m111: Add experimental QVGA support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=60ed6e4f4ec778b195efb92563021a376fa30524)
- [V4L/DVB (11559): Siano: add support for infra-red (IR) controllers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ebb6c22e80ccb2889b9c459df36d686d223911f5)
- [V4L/DVB (11567): saa7134: Added support for AVerMedia Cardbus Plus](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d46de9d2364cad55caddc04632707f5739b4cd87)
- [V4L/DVB (11571): Add Elgato EyeTV DTT deluxe to dibcom driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=513846ece644662dc0914f7b518ed1bd29953fc3)
- [V4L/DVB (11665): cx88: Add support for the Hauppauge IROnly board.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=501d8cd4e248feebd465b016a7d5b7bc084f5f1f)
- [V4L/DVB (11682): STV0900/STV0903: Add support for Silicon cut \>= 3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=27d403214317d42fbeaf626f2734a1028087fd16)
- [V4L/DVB (11684): gspca - m5602-s5k4aa: Add experimental SXGA support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4fcec145e9eaae26864731fd6a3120d34abcaffe)
- [V4L/DVB (11691): gspca - m5602-ov9650: Add ASUS A6K vflip quirk](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=951872a8198a5a336a49075320197ac5b2e5c6f1)
- [V4L/DVB (11717): gspca - sonixj: Webcams with bridge sn9c128 added](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ceec80e5a52580bd7b257c14c6c8355be58c971f)
- [V4L/DVB (11720): gspca - sonixj: Webcam 06f8:3008 added](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f8eaaf4f2a2810d6e486da2916ef07f7e00665c9)
- [V4L/DVB (11730): af9015: support for KWorld MC810](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6e9c1a2a6766df0cad1632812c6ad05eabf158e4)
- [V4L/DVB (11735): Enables the Winfast TV2000 XP Global TV IR](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3e9a489743ea87663e9ff638cb9b8fe13805a327)
- [V4L/DVB (11742): TI THS7303 video amplifier driver code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=40199c50b891d24d1a8f1d480f886680a3ac9b74)
- [V4L/DVB (11743): Analog Devices ADV7343 video encoder driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=06e61f8d5f5df68104168ac20d0527ecee13638a)
- [V4L/DVB (11767): cx23885: Add preliminary support for the HVR1270](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2074dffaedebbf5a8468fd37855d6d94ba34041c)
- [V4L/DVB (11768): cx23885: add ATSC/QAM tuning support for Hauppauge WinTV-HVR1270](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a5dbf45766a378cc00f341f7179befab1edae573)
- [V4L/DVB (11769): cx23885: add ATSC/QAM tuning support for Hauppauge WinTV-HVR1275](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d099becb0bd7ee01a13d58371b4ea5a2f7052c04)
- [V4L/DVB (11770): cx23885: add ATSC/QAM tuning support for Hauppauge WinTV-HVR1255](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=19bc57968cc854c7da4846c21b3ef2a39e43f97d)
- [V4L/DVB (11771): cx23885: add DVB-T tuning support for Hauppauge WinTV-HVR1210](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6b926eca9824568b18825d3eade5fb39e3b5a9fb)
- [V4L/DVB (11775): tuner: add support Philips MK5 tuner](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8475cbcb0f885189969915eb3680d10fc525d722)
- [V4L/DVB (11798): xc5000: add "no_poweroff" module option](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b6bd5eb871184dd976ce2d410888b2a29d90371a)
- [V4L/DVB (11800): tuner-xc2028: show the proper module description for no_poweroff option](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4900877b7cdcb88e24c4130cb3c25080c03c335c)
- [V4L/DVB (11803): xc5000: add support for DVB-T tuning](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6c99080d8eae64c51f8b44946eb47f995361c582)
- [V4L/DVB (11825): em28xx: add Terratec Grabby](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4557af9c5338605c85fe54f5ebba3d4b14a60ab8)
- [V4L/DVB (11827): Add support for Terratec Grabster AV350](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=766ed64de554fda08ceb927d36279eabcb08acb3)
- [V4L/DVB (11830): dib0700: add support for Leadtek WinFast DTV Dongle H](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f0f4ae763b3dc04de3745a75c3518925d1b8325e)
- [V4L/DVB (11831): dib0700: added USB IDs for Terratec T3 and T5](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a9b8fe30a6d2a49749327ff18c4daa488ef73ab3)
- [V4L/DVB (11838): uvcvideo: Add Lenovo Thinkpad SL400 to device list comments](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=849a3aba2d9830dc2a78a66078023e7e5ac26e15)
- [V4L/DVB (11861): saa7134: enable digital tv support for Hauppauge WinTV-HVR1110r3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1bc7f51c57c52cfac1a455d8f8ef99703e719e55)
- [V4L/DVB (11864): cx18: Complete support for Sliced and Raw VBI for 625 line systems](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=929a3ad1525895c394cbe97a6b74792da9a865a6)
- [V4L/DVB (11879): Adds support for Leadtek WinFast DTV-1800H](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3047a17639d499691c657772667f2c1e65edabfb)
- [V4L/DVB (11880): cx23885: support for card Mygica X8506 DMB-TH](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=493b7127aa56d0a5c041797639bf543d96f6261b)
- [V4L/DVB (11883): Siano: cards - add two additional (USB) devices](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d0b66180c3b288678853e31ec4330b2b5d01e2db)
- [V4L/DVB (11915): af9015: support for Genius TVGo DVB-T03](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=22d4645311689cd20967813775e492c786f2d3c6)
- [V4L/DVB (11925): em28xx: Add support for the K-World 2800d](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3ed58baf5db4eab553803916a990a3dbca4dc611)
- [V4L/DVB (11933): tuner-simple, tveeprom: Add Philips FQ1216LME MK3 analog tuner](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5ddc9b100fc96e8f3c6d435cecd9d09e5b9673f9)
- [V4L/DVB (11940): gspca - m5602-s5k4aa: Add vflip quirk for the Lenovo Y300](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f02c3944c1331f0b41c5d75b6d5d69d8858b169f)
- [V4L/DVB (11941): gspca - m5602-ov9650: Add vflip quirk for the ASUS A6VA](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=40a4f2fc6525f621f6f855e1d5506c3b14acf3cc)
- [V4L/DVB (11942): gspca - m5602-ov9650: Reorder quirk list and add A7V quirk](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=926b3b4122e4ebca52e67eecf9beb9a517e593f4)
- [V4L/DVB (11946): uvcvideo: Add support for Aveo Technology webcams](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2d2bf2a3a6c84f0b316764e521d5dcee557e9c65)
- [V4L/DVB (11947): uvcvideo: Add support for FSC V30S webcams](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ca4a3456858775081f172e89077aa65cf5dbc52a)
- [V4L/DVB (11950): cx18: Split LeadTek PVR2100 and DVR3100 H into 2 separate card entries](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9d5af8629255ef6e62481ee7dea8c6787facc579)
- [V4L/DVB (11951): cx18: Add DVB-T support for the Leadtek WinFast DVR3100 H](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8bb09db375fe4f15d16315947500e827caa0fe9c)
- [V4L/DVB (11971): gspca - doc: Add the 05a9:a518 webcam to the Documentation.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3d48f7d09aadccf570a871ce0d5eec34092b38c1)
- [V4L/DVB (11977): em28xx: Add Kworld 315 entry](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d7de5d8ff74efd01916b01af875a0e87419a3599)
- [V4L/DVB (11982): Add keymaps for TeVii and TBS USB DVB-S/S2 cards](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b42e1d71f52995f0a25f2b593fdb166326db3fd4)
- [V4L/DVB (11983): Add support for DVBWorld DVB-C USB Cable card.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1dac77c9d82f344b21c1d962d79875ec331f83cc)
- [V4L/DVB (11984): Add support for yet another SDMC DM1105 based DVB-S card.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=519a4bdcf8221c6b2d129b3c720761b7cab7f2c1)
- [V4L/DVB (11996): saa7134: add support for AVerMedia M103 (f736)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=27049dc30152ad0401082f32c33859821b4be029)
- [V4L/DVB (12010): cx88: Properly support Leadtek TV2000 XP Global](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=14422f9dd8515bfbe6fdbde37eadf59e2980f104)
- [V4L/DVB (12074): gspca_ov519: Add 320x240 and 160x120 support for cif sensor cams](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=124cc9c0c8acc77ac2f1114ee7eea961334020ba)
- [V4L/DVB (12084): ov511: mark as deprecated](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0220f8870e66628f19c36bad813e881ebfaae7a6)
- [V4L/DVB (12087): gspca_sonixj: enable support for 0c45:613e camera](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cc7b5b573feb5edfe68c028bc1ea383dab37dde2)
- [V4L/DVB (12088): Mark the v4l1 uvcvideo quickcam messenger driver as deprecated](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=119893b2dfb18515bfdcc5edb83422e6aa126a86)
- [V4L/DVB (12091): gspca_sonixj: Add light frequency control](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=37c6dbe290c05023b47f52528e30ce51336b93eb)
- [V4L/DVB (12101): em28xx: add support for EVGA inDtube](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=19859229d7d98bc2d582ff45045dd7f73d649383)
- [V4L/DVB (12102): em28xx: add Remote control support for EVGA inDtube](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a4c473033b6a100773a4fd8b7ba1e45baeb1e692)
- [V4L/DVB (12128): v4l2: update framework documentation.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2c0b19ac3b73199fe7b3fbff884051046554c048)
- [V4L/DVB (12135): Add a driver for mt9v011 sensor](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7dfba00d05f3c7db9510f3b54a472981cf1521af)
- [V4L/DVB (12138): em28xx: add support for Silvercrest Webcam](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=02e7804b2135ff941b8846f5820cf48fbfdadd54)
- [V4L/DVB (12139): em28xx: add other video formats](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=43cb9fe3291bb96390c1d188eb61c2d1581bb61e)
- [V4L/DVB (12172): em28xx: Add autodetection code for Silvercrest 1.3 mpix](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=791a08fc01aaa293a73c9dce260327fdee288faf)
- [V4L/DVB (12181): get_dvb_firmware: Add Yuan MPC718 MT352 DVB-T "firmware" extraction](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9f38a920b232800fd4000ba3d4617b41198e017e)
- [V4L/DVB (12182): cx18: Add DVB-T support for Yuan MPC-718 cards with an MT352 or ZL10353](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ff861fb21e44ab178eddc6a1dd7c5478e3eb2ec5)
- [V4L/DVB (12206): get_dvb_firmware: Correct errors in MPC718 firmware extraction logic](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0a6843483c256c859cd9542361812a29403f0fb5)
- [V4L/DVB (12245): em28xx: add support for mt9m001 webcams](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b80fd2d811b48a92051f86d257b00f373e69a6d7)
- [V4L/DVB (12260): em28xx: make support work for the Pinnacle Hybrid Pro (eb1a:2881)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d5b3ba9cb375620a109d79f2e3a7bc21e9b75d8f)
- [V4L/DVB (12263): em28xx: set demod profile for Pinnacle Hybrid Pro 320e](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e16e5a3739cfd208de00d49def10fcfa6ceff46f)

For other articles on 2.6.31 and links to the rest of the "Coming in 2.6.31" series, see The H's [Kernel Log - 2.6.31 Tracking](../site/open/features/Kernel-Log-2-6-31-Tracking-746446.html "Kernel Log - 2.6.31 Tracking – 02 July 2009, 11:21") page.

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
