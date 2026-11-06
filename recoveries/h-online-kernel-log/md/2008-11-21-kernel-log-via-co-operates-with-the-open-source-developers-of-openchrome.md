---
title: "Kernel Log: VIA co-operates with the open source developers of openChrome"
date: 2008-11-21
author: "Terry Relph-Knight"
source: http://www.h-online.com/open/news/item/Kernel-Log-VIA-co-operates-with-the-open-source-developers-of-openChrome-738911.html
pages: 1
---

# Kernel Log: VIA co-operates with the open source developers of openChrome

**Terry Relph-Knight**

![Kernel Log logo](../site/imgs/43/3/6/5/3/4/3/a345f5e7c547062f.jpg) From now on, VIA intends to co-operate with the programmers of the open source [openChrome](http://www.openchrome.org/) project, who have, for years, developed open source graphics drivers for VIA's mainboard chipsets, to develop X.org graphics drivers. According to the vendor, a co-operation already exists for improving the RandR and multi-monitor support of the drivers which are part of many Linux distributions. This will most likely cause the openChrome driver to become the main driver for VIA hardware. The "via" driver by X.org/Xfree86, the outdated [unichrome driver](http://unichrome.sourceforge.net/) and the [VIA graphics driver](../site/news/item/VIA-open-source-Xorg-display-driver-released-737119.html) whose code was partially published in late August should, therefore, soon be forgotten. The publication of the latter already gave rise to the question why VIA should release another open source driver rather than co-operate with the developers of existing open source drivers – and also provided [suitable answers](http://laforge.gnumonks.org/weblog/2008/09/01/#20080901-via-xorg-opensource-faq).

Together with Harald Welte, who has worked at VIA as an [open source advisor](../site/news/item/VIA-appoints-Harald-Welte-as-open-source-liason-736611.html) since last summer, the chipset manufacturer also ensured that the documentation relating to the 2D and 3D features of the Chrome9 and UniChrome graphics cores was published – it can now be found on a freely accessible [server run by the X.org project](http://www.x.org/docs/via/). VIA also pointed out that a frame buffer driver for VIA graphics hardware has recently been integrated into the main development branch of Linux, which is to produce Linux 2.6.28 late this, or early next year.

Having for years laboured with proprietary drivers that sometimes presented major installation issues even for experienced Linux users, VIA now appears to be making an earnest effort to become an active member of the open source community. Intel has pursued this strategy for a long time and is often even willing to develop solutions or improvements that also considerably benefit the hardware of its fiercest competitors.

AMD has also been active in the open source arena for a long time, although its efforts haven't been quite as enthusiastic as those of Intel. Only yesterday (Wednesday), the company released a [CPUInfo tool for Linux](http://www.amd.com/us-en/Processors/TechnicalResources/0,,30_182_871_13118,00.html) – although it would have probably been less work and made more users happy if AMD had further improved existing programs like [x86info](http://www.codemonkey.org.uk/projects/x86info/), which come with many distributions. Since its merger with ATI, AMD has also put a lot of work into providing open source developers with all the information they need for programming the drivers for recent Radeon graphics chips. The vendor even actively supported the developers of open source graphics drivers. Both of these measures considerably improved the situation for Radeon hardware drivers, but AMD still continues to develop its proprietary graphics drivers for Linux.

Nvidia, on the other hand, continues to keep the information about its graphics chips under wraps and exclusively relies on proprietary drivers. While the vendor initially also tried to provide proprietary Linux audio and network drivers for its mainboard chipsets, this approach was quickly abandoned. Nowadays, Nvidia actively helps improve the storage, audio and network drivers contained in the Linux kernel. Multimedia specialist Creative had a similar experience and has recently [released an open source driver for the X-Fi](../site/news/item/Kernel-Log-New-kernels-open-audio-drivers-for-X-Fi-738061.html) series, after wasting a lot of effort on, and finally abandoning, the development of proprietary drivers for its X-Fi sound hardware.

**Kernel Log in brief**

- Arjan van de Ven [reports on the LKML](http://thread.gmane.org/gmane.linux.kernel/757886) that the [Kerneloops project](http://www.kerneloops.org) recently received its [one hundred thousandth error report](http://www.kerneloops.org/raw.php?rawid=100000). The Intel developer recently also released an evaluation of the latest kerneloops reports; according to the evaluation, most of the oopses were caused by the code of the [VirtualBox](http://www.virtualbox.org/) virtualisation software, which isn't even part of the Linux kernel.

<!-- -->

- The development version of the radeonhd graphics driver has [recently](http://lists.opensuse.org/radeonhd/2008-11/msg00245.html) started to support screen rotation. Alex Deucher reports about the progress made in connection with the 3D support of AMD's R6xx/R7xx GPUs [in his blog](http://www.botchco.com/agd5f/?p=32). These GPUs are part of the Radeon series 2000, 3000 and 4000 graphics hardware.

<!-- -->

- Peter Hutterer has released versions [2.0.8](http://lists.freedesktop.org/archives/xorg-announce/2008-November/000692.html) and [2.1.0](http://lists.freedesktop.org/archives/xorg-announce/2008-November/000693.html) of xf86-input-evdev; the latter version includes major changes to the input event interface code. The X.org developer explains these changes in detail [in his blog](http://who-t.blogspot.com/2008/11/evdev-21-is-out.html).

<!-- -->

- Nvidia has released the first [beta version 180.08](http://www.nvnews.net/vbulletin/showthread.php?t=123265) of its proprietary graphics card drivers for Linux. They temporarily support OpenGL 3.0 and contain corrections to [VDPAU](../site/news/item/Linux-API-harnesses-GeForce-GPU-s-HD-video-capabilities-738137.html).

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the Kernel Log at heise open:*

*Older Kernel Logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

- [Kernel Log: New graphics drivers and Linux versions: Dom0 patches for 2.6.29?](../site/news/item/Kernel-Log-New-graphics-drivers-and-Linux-versions-Dom0-patches-for-2-6-29-738149.html)
- [Kernel Log: What's coming in 2.6.28 - Part 5: updates for netbooks and notebooks](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-5-updates-for-netbooks-and-notebooks-738121.html)
- [Kernel Log: New kernels, open audio drivers for X-Fi](../site/news/item/Kernel-Log-New-kernels-open-audio-drivers-for-X-Fi-738061.html)
- [Kernel Log: Short video interviews with Torvalds, Kroah-Hartman and others](../site/news/item/Kernel-Log-Short-video-interviews-with-Torvalds-Kroah-Hartman-and-others-737833.html)
- [Kernel Log: 2.6.28-rc1 released, new graphics and camera drivers](../site/news/item/Kernel-log-2-6-28-rc1-released-new-graphics-and-camera-drivers-737795.html)
- [Kernel Log: What's coming in 2.6.28 - Part 4: Improved graphics support](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-4-Improved-graphics-support-737779.html)
- [Kernel Log: New Atheros WLAN drivers and stable kernels, radeon vs. radeonhd](../site/news/item/Kernel-Log-New-Atheros-WLAN-drivers-and-stable-kernels-radeon-vs-radeonhd-737773.html)
- [Kernel Log: What's coming in 2.6.28 - Part 3: Dodgy drivers](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-3-Dodgy-drivers-737747.html)
- [Kernel Log: More than 10 million lines of Linux source files](../site/news/item/Kernel-Log-More-than-10-million-lines-of-Linux-source-files-737731.html)
- [Kernel Log: Coming in 2.6.28 - Part 2: network infrastructure and network drivers](../site/news/item/Kernel-Log-Coming-in-2-6-28-Part-2-network-infrastructure-and-network-drivers-737711.html)
- [Kernel Log: Coming in 2.6.28 - Part 1: ATA support and block layer](../site/news/item/Kernel-Log-Coming-in-2-6-28-Part-1-ATA-support-and-block-layer-737699.html)
- [Kernel Log: new Catalyst drivers, 2.6.27.1 resolves cause of e1000e problem](../site/news/item/Kernel-Log-new-Catalyst-drivers-2-6-27-1-resolves-cause-of-e1000e-problem-737701.html)
- [Kernel Log: Ext4 completes development phase as interim step to btrfs](../site/news/item/Kernel-Log-Ext4-completes-development-phase-as-interim-step-to-btrfs-737697.html)
- [Kernel Log: Linux 2.6.27 Released](../site/open/features/Kernel-Log-Linux-2-6-27-Released-746496.html)
- [Kernel Log: problem with e1000e bypassed, Morton praises Btrfs](../site/news/item/Kernel-Log-problem-with-e1000e-bypassed-Morton-praises-Btrfs-737561.html)
- [Kernel Log: 2.6.27 nearing completion; Btrfs to be added to the kernel?](../site/news/item/Kernel-Log-2-6-27-nearing-completion-Btrfs-to-be-added-to-the-kernel-737489.html)
- [Kernel Log: Kernel Summit info; Plumbers keynote online; the latest on the e1000e problem](../site/news/item/Kernel-Log-Kernel-Summit-info-Plumbers-keynote-online-the-latest-on-the-e1000e-problem-737443.html)
- [Kernel Log: The second day of Kernel Summit 2008; criticism of Ubuntu at the opening of the Linux Plumbers Conference](../site/news/item/Kernel-Log-The-second-day-of-Kernel-Summit-2008-criticism-of-Ubuntu-at-the-opening-of-the-Linux-Plumbers-Conference-737379.html)
- [Kernel Log: Hard core Linux developers discuss the future of Linux at the Kernel Summit](../site/news/item/Kernel-Log-Hard-core-Linux-developers-discuss-the-future-of-Linux-at-the-Kernel-Summit-737327.html)
- [Kernel Log: New stable and developer kernel, Mesa 7.1 and X-Server 1.5 released](../site/news/item/Kernel-Log-New-stable-and-developer-kernel-Mesa-7-1-and-X-Server-1-5-released-737227.html)
- [Kernel Log: New stable and pre-release kernels, Ubuntu 8.10 with 2.6.27?](../site/news/item/Kernel-Log-New-stable-and-pre-release-kernels-Ubuntu-8-10-with-2-6-27-737021.html)
- [Kernel Log: New video drivers for AMD, Intel, Nvidia and VIA hardware](../site/news/item/Kernel-Log-New-video-drivers-for-AMD-Intel-Nvidia-and-VIA-hardware-736997.html)
- [Kernel Log: Kernel development explained, new Synaptics driver, Linux 2.6.27-rc3 published](../site/news/item/Kernel-Log-Kernel-development-explained-new-Synaptics-driver-Linux-2-6-27-rc3-published-736911.html)
- [Kernel Log: Ath9k driver for Atheros Wifi in 2.6.27; reading material and videos for Linux experts](../site/news/item/Kernel-Log-Ath9k-driver-for-Atheros-Wifi-in-2-6-27-reading-material-and-videos-for-Linux-experts-736829.html)
- [Kernel Log: Btrfs 0.16 released, new stable kernels released, Wifi drivers for 2.6.27 merged](../site/news/item/Kernel-Log-Btrfs-0-16-released-new-stable-kernels-released-Wifi-drivers-for-2-6-27-merged-736815.html)
- [Kernel Log: New Stable kernel, DRI2 postponed, Xgl removed from X.org](../site/news/item/Kernel-Log-New-Stable-kernel-DRI2-postponed-Xgl-removed-from-X-org-736743.html)
- [Kernel Log: New Nvidia drivers are still slow, Linux 2.6.26.1 soon](../site/news/item/Kernel-Log-New-Nvidia-drivers-are-still-slow-Linux-2-6-26-1-soon-736723.html)
- [Kernel Log : Tux3 file system announced, X.org updates](../site/news/item/Kernel-Log-Tux3-file-system-announced-X-org-updates-736707.html)
- [Kernel Log: 2.6.25.13 corrects a vulnerability, problems with ACPI](../site/news/item/Kernel-log-2-6-25-13-corrects-a-vulnerability-problems-with-ACPI-736703.html)
- [Kernel Log: First release candidate concludes the hot development phase of 2.6.27](../site/news/item/Kernel-Log-First-release-candidate-concludes-the-hot-development-phase-of-2-6-27-736695.html)
- Kernel Log: Practical Practices - Ottawa Linux Symposium Notes
- [Kernel Log: Centrino 2 WLAN driver iwl 5000 and webcam driver gscpa in Linux 2.6.27](../site/news/item/Kernel-Log-Centrino-2-WiFi-driver-iwl-5000-and-webcam-driver-gscpa-in-Linux-2-6-27-736569.html)
- [Kernel Log: ath9k driver for new Atheros WLAN chips, discussions of Nvidia drivers](../site/news/item/Kernel-log-ath9k-driver-for-new-Atheros-WLAN-chips-discussions-of-Nvidia-drivers-736563.html)
- [Kernel Log: No unstable series; Linux 2008.7, dealing with security fixes](../site/news/item/Kernel-Log-No-unstable-series-Linux-2008-7-dealing-with-security-fixes-736557.html "Kernel Log: No unstable series; Linux 2008.7; dealing with security fixes – 22 July 2008, 01:47")
- [Polish and add-ons; What's new in Linux 2.6.26](../site/open/features/Polish-and-add-ons-the-latest-updates-in-Linux-2-6-26-746492.html)
- [Kernel Log: Linux-staging branch will help with integration; Linux kernel 2.6.25.6 and 2.6.26-rc6](../site/news/item/Kernel-Log-Linux-staging-branch-will-help-with-integration-Linux-kernel-2-6-25-6-and-2-6-26-rc6-735507.html "Kernel Log: Linux-staging branch will help with integration; Linux kernel 2.6.25.6 and 2.6.26-rc6 – 17 June 2008, 11:31")
- [Kernel Log: New graphics drivers and stable kernels; details about Linux-staging](../site/news/item/Kernel-log-New-graphics-drivers-and-stable-kernels-details-about-Linux-staging-736303.html "Kernel log: New graphics drivers and stable kernels; details about Linux-staging – 26 June 2008, 15:45")
- [Kernel-Log: Users of 2.4 provide feedback, 2.4.36.5 and 2.6.26-rc5 released](../site/news/item/Kernel-Log-Users-of-2-4-provide-feedback-2-4-36-5-and-2-6-26-rc5-released-735437.html "Kernel-Log: Users of 2.4 provide feedback, 2.4.36.5 and 2.6.26-rc5 released – 10 June 2008, 15:20")
- [Kernel Log: new gfx drivers for GeForce & Radeon GPUs; Kernel Track at LinuxTAG](../site/news/item/Kernel-log-new-gfx-drivers-for-GeForce-Radeon-GPUs-Kernel-Track-at-LinuxTAG-735349.html "Kernel log: new gfx drivers for GeForce & Radeon GPUs; Kernel Track at LinuxTAG – 30 May 2008, 14:23")
- [Improvements throughout - Whats new in Linux 2.6.25](../site/open/features/Improvements-throughout-what-s-new-in-Linux-2-6-25-746484.html)
- [2.6.25 in the home stretch, discrepancies in the Linux Foundation study](../site/news/item/Kernel-Log-2-6-25-in-the-home-stretch-discrepancies-in-the-Linux-Foundation-study-734765.html "Kernel Log: 2.6.25 in the home stretch, discrepancies in the Linux Foundation study – 14 April 2008, 10:50")
- [Proprietary Linux drivers stumble and spark debate](../site/news/item/Kernel-log-Proprietary-Linux-drivers-stumble-and-spark-debate-734409.html "Kernel log: Proprietary Linux drivers stumble and spark debate – 07 March 2008, 11:07")
- [ATI graphics driver updated, discussions about when to integrate Linux drivers](../site/news/item/Kernel-Log-ati-graphics-driver-updated-discussions-about-when-to-integrate-Linux-drivers-734361.html "Kernel Log: ati graphics driver updated, discussions about when to integrate Linux drivers – 27 February 2008, 16:13")
- [New AMD, HP and SANE drivers; Linux Weather Forecast updated](../site/news/item/Kernel-log-New-AMD-HP-and-SANE-drivers-Linux-Weather-Forecast-updated-734285.html "Kernel log: New AMD, HP and SANE drivers; Linux Weather Forecast updated – 20 February 2008, 13:40")
- [Linux-next to speed development work](../site/news/item/Kernel-Log-Linux-next-to-speed-development-work-734227.html "Kernel Log: Linux-next to speed development work – 14 February 2008, 10:38")

([trk](mailto:trk@h-online.com "Terry Relph-Knight"))
