---
title: "Kernel Log: What's coming in 2.6.30 - Architecture and infrastructure"
date: 2009-06-06
author: "Terry Relph-Knight"
source: http://www.h-online.com/open/news/item/Kernel-Log-What-s-coming-in-2-6-30-Architecture-and-infrastructure-741921.html
pages: 1
---

# Kernel Log: What's coming in 2.6.30 - Architecture and infrastructure

**Terry Relph-Knight**

![Kernel Log logo](../site/imgs/43/3/6/8/3/5/2/a345f5e7c547062f.jpg)

#### by Thorsten Leemhuis

**Linux 2.6.30 can be compressed using Bzip2 and LZMA, includes security framework Tomoyo and should boot faster. Tasmanian devil Tuz, who stood in for Tux as Linux mascot in 2.6.29, has been relieved of his duties.**

Linus Torvalds [recently released](http://thread.gmane.org/gmane.linux.kernel/845322) the eighth and probably last pre-release version of Linux 2.6.30 â€“ the sage of Linux has announced that Linux 2.6.30 will be released shortly, (probably this weekend). Not that he always sticks religiously to such pronouncements; nonetheless it is unlikely to be more than a few days before kernel version 2.6.30 hits the shelves. Kernel Log thus concludes the "What's coming in 2.6.30" series with this overview of architecture support and infrastructure-related changes.

**Compacted**

In Linux 2.6.30, the developers have [removed](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5e47c478b0b69bc9bc3ba544e4b1ca3268f98fef) support for the "zImage" build target on x86 systems, which has long since ceased to be used. One new feature is a [kernel library](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bc22c17e12c130dc929218a95aa347e0f3fd05dc) for decompressing Gzip, Bzip and Lzma. The kernel accesses these in order to unpack [parts of the kernel image](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ae03c49964af5033534e518eebe439c3b90f43a7) or [Initramfs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=30d65dbfe3add7f010a075991dc0bfeaebb7d9e1) during the boot process. Previously only Gzip could be used for compression. A kernel image packed with Bzip2 [should](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=30d65dbfe3add7f010a075991dc0bfeaebb7d9e1#patch2) be around 10Â per cent, or with Lzma a whole 33Â per cent, smaller.

There have been a [number of changes](http://thread.gmane.org/gmane.linux.kernel/812893) to the CFS process scheduler to simplify the code, accelerate processing and optimise CFS for real time environments. For the latter in particular, the option of having interrupt handlers with separate threads, for which some of the groundwork has now been done, should prove of some interest ([1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3aa551c9b4c40018f0e261a178e3d25478dc04a9), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=935bd5b971f0df7c06d214d022cf8392e2f37952), [3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f48fe81e5b032914183e9a17052313720c2cac56)). There have also been [a number of enhancements](http://thread.gmane.org/gmane.linux.kernel/814767) in the code for locking. A [somewhat different approach](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0d66bf6d3514b35eb6897629059443132992dbd7) when attempting to get a lock should deliver a slight performance boost â€“ something in which the [Btrfs developer team](http://lwn.net/Articles/313682/) in particular have shown an interest.

#### Kernel Log â€“ What's coming in 2.6.30

Further articles in the "What's coming in 2.6.30" Kernel Log series, which summarises major developments in the forthcoming kernel version:

1\. [Network: New Wi-Fi drivers and other network novelties](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-Network-New-Wi-Fi-drivers-and-other-network-novelties-741197.html "Kernel Log: What's coming in 2.6.30 - Network: New Wi-Fi drivers and other network novelties â 17 April 2009, 10:51")

2\. [File systems: New and revamped file systems](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-File-systems-New-and-revamped-file-systems-741319.html "Kernel Log: What's coming in 2.6.30 - File systems: New and revamped file systems â 27 April 2009, 16:11")

3\. [Storage: RAID improvements, optimised CFQ Scheduler, SAS drivers](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-Storage-RAID-improvements-optimised-CFQ-Scheduler-SAS-drivers-741597.html "Kernel Log: What's coming in 2.6.30 - Storage: RAID improvements, optimised CFQ Scheduler, SAS drivers â 15 May 2009, 17:01")

4\. [Drivers: New drivers for audio, video, USB hardware, netbooks and notebooks](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-Drivers-New-drivers-for-audio-video-USB-hardware-netbooks-and-notebooks-741837.html "Kernel Log: What's coming in 2.6.30 – Drivers: New drivers for audio, video, USB hardware, netbooks and notebooks â 01 June 2009, 18:52")

The article '[Steady growth â€“ What's new in Linux 2.6.29](../site/open/features/Steady-growth-What-s-new-in-Linux-2-6-29-746553.html "Steady growth - What's new in Linux 2.6.29 â 24 March 2009, 15:26")' gives an overview of new features in the main development line of the current kernel version.

**Security**

Thanks to major [changes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=254eff771441f4ee7aa9cf770a6e4820492c9dab) to cryptd, the [cryptographic subsystem](http://thread.gmane.org/gmane.linux.kernel.cryptoapi/2397/focus%3D2805) now runs better using more threads. On the developer's test CoreÂ 2 Duo E6400 system, data throughput on a volume encrypted using the device-mapper increased by [19Â percent](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=254eff771441f4ee7aa9cf770a6e4820492c9dab). [Also new is support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=54b6a1bd5364aca95cd6ffae00f2b64c6511122c) for [Intel's AES-NI](http://softwarecommunity.intel.com/isn/downloads/intelavx/AES-Instructions-Set_WP.pdf)![PDF](../site/icons/file-pdf.gif "PDF document") (Advanced Encryption Standard) and the [crypt4xx](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=049359d655277c382683a6030ae0bac485568ffc) driver for AMCC PPC4xx series cryptographic accelerators.

SELinux and Smack are joined by [Tomoyo](http://tomoyo.sourceforge.jp/), a further security framework which offers MAC (Mandatory Access Control). The Tomoyo developers have provided a helpful [table on the Tomoyo wiki](http://tomoyo.sourceforge.jp/wiki-e/?WhatIs#yf491ee8) which explains how, from their point of view, it differs from the above two frameworks and AppArmor. A significant practical difference is that SELinux and Smack work with extended attributes, whilst Tomoyo and AppArmor work with paths and file names. This was and is not entirely uncontroversial, but is good enough for some developers â€“ details are given in the article '[Tomoyo Linux and pathname-based security](http://lwn.net/Articles/277833/)' on LWN.net.

Another new feature is the integrity management architecture (IMA) (e.Â g. [1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3323eec921efd815178a23107ab63588c605c0b2), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4af4662fa4a9dc62289c580337ae2506339c4729), [3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6146f0d5e47ca4047ffded0fb79b6c25359b386c), [4](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=659aaf2bb5496a425ba14036b5b5900f593e4484)). Using a Trusted Platform Module (TPM), IMA is able to ensure that programs are not changed either accidently or with nefarious intent â€“ details on the IBM-developed technology can be found in the LWN.net articles '[System integrity in Linux](http://lwn.net/Articles/309441/)' and '[Integrity management in the kernel](http://lwn.net/Articles/227937/)'.

**Power management and PCI**

There have been lots of big changes in the PCI subsystem; these are [detailed](http://thread.gmane.org/gmane.linux.kernel.pci/3862) in the PCI subsystem administrator's Git pull requests. He has highlighted items such as improved support for hotplugging and [MSI](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1c8d7b0a562da06d3ebe83f01b1ed553205d1ae4) (message-signalled interrupts). The PCI subsystem now also offers everything required for single root I/O virtualisation (SR-IOV). This allows PCI devices which support SR-IOV to be divided into multiple virtual devices which can be assigned to virtualised guest systems.

Following major changes to the code for switching into and out of system-wide hibernation (suspend and resume) in 2.6.29, there have been [further](http://thread.gmane.org/gmane.linux.kernel.pci/3839) adjustments aimed at rounding off some of the new design's rough edges. In particular, the developers have [revamped](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2ed8d2b3a81bdbb0418301628ccdb008ac9f40b7) interrupt handling in order to make suspend more robust.

**Fast boot, Tuz, maintainers**

Numerous kernel changes aimed at improving boot times were introduced in Linux 2.6.28 and 2.6.29 ([fastboot patches](http://lwn.net/Articles/314808/)). Due to a number of problems however, some of the more promising enhancements were only used when explicitly activated on start-up by setting the appropriate kernel parameters. In 2.6.30 this code will finally [be used in anger](http://thread.gmane.org/gmane.linux.kernel/813882). The extent to which parallel initialisation of certain kernel subsystems during booting will deliver speed gains is highly dependent on a system's hardware components and how they are configured.

Temporary mascot [Tuz](../site/news/item/Kernel-Log-Tasmanian-devil-to-be-Linux-s-temporary-mascot-new-Radeon-drivers-740667.html "Kernel Log: Tasmanian devil to be Linux's temporary mascot, new Radeon drivers â 19 March 2009, 15:43") has now served its honorary term and is [making way](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3d4f16348b77efbf81b7fa186a18a0eb815b6b84) for Linux' long-term penguin mascot Tux.

The [maintainers](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob;f=MAINTAINERS;h=cf4abddfc8a40dcc161e851c26294480fff3076f;hb=HEAD) file has seen major [restructuring](http://thread.gmane.org/gmane.linux.kernel/820975). Using the information added to this file, a [new script](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cb7301c7a3b2216c93b148fec0718d24f4ee2a99) is now able to list which developers are responsible for a specific area or file within the kernel.

**Architecture code and virtualisation**

Linux 2.6.30 has also seen major work on the structure of the code for x86 systems, which now no longer support 'sub-architectures' [1](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6bda2c8b32febeb38ee128047253751e080bad52), [2](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7b38725318f4517af6168ccbff99060d67aba1c8). Following on from this, [the developers have removed](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=965c7ecaf2e2b083d711a01ab33735a4bdeee1a4) support for 32-bit Voyager systems â€“ anyway since 2.6.27 the code has been uncompilable. Alternative code for supporting this specific x86 architecture [may](http://thread.gmane.org/gmane.linux.kernel/822179), however, be in the pipeline. [Also new](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cec5455e457928153f5a51668dad3d68176feab5) is [support](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=tree;f=arch/microblaze;hb=HEAD) for the Microblaze architecture. The code for the Xtensa architecture is also now able to deal with Stretch S6000 chips ([1](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=eff35af9c0c83a24376a67ff88c65679c25c7a51), [2](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=000af2c5a8913ebd763313d0c9ebc66c2c4765b1)).

Things were relatively quiet on the virtualisation front this time out. One of the [bigger changes](http://thread.gmane.org/gmane.comp.emulators.kvm.devel/29706) was support for nested virtualisation â€“ running a guest system within a guest system â€“ on more recent AMD CPUs. Debugging options in KVM have also been enhanced. As in pretty much every new version, the KVM development team claim to have improved both performance and emulation in general ("*better performance and improved emulation accuracy*"). There have been [changes](http://thread.gmane.org/gmane.linux.kernel/814680) in the Xen DomU code. The Dom0 code is still left out in the cold however â€“ as things stand at present it looks unlikely that it will be merged in the near future, with [Torvalds](http://thread.gmane.org/gmane.linux.kernel/836008/focus%3D845139) and a number of other key kernel developers having recently strongly criticised the code put forward for merging.

**On close examination**

Other changes will in future allow more information to be obtained on the status of modern CPUs â€“ useful for debugging and performance optimisation purposes ([1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9b779edf4b97798d037bb44fca2719ac184d0f14), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f4c3c4cdb1de232ff37cf4339eb2f36c84e20da6)). The developers have also merged the infrastructure for debugging DMA transfers ([1](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=712b0006bf3a9ed0b14a56c3291975e582127766), [documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=187f9c3f05373df4f7cbae2e656450acdbba7558)).

Tracing framework Ftrace [now works](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d3e75ff14bc1453c4762428395aac9953a023efc) on IA64 CPUs (Itanium). There are new trace plugins in the form of [kmemtrace](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b9ce08c01020eb28bfbfa6faf1c740281c5f418e) (memory), [blktrace](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c71a896154119f4ca9e89d6078f5f63ad60ef199) (block devices such as storage media) and a [workqueue tracer](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e1d8aa9f1dd655a3534b22fcfbecb70cdb125766). A number of other tracers and even Ftrace have been extended and enhanced. Details can be found in the Git pull requests for the [tracing infrastructure](http://thread.gmane.org/gmane.linux.kernel/816810) and the list of further commits at the end of this article.

**Latecomers and minor gems**

There have been further changes in some of the areas on which Kernel Log has already reported as part of the "What's coming in 2.6.30" series. Despite the stabilisation phase already being at a fairly advanced stage, Torvalds has nonetheless merged a new driver by the name of [fnic](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5df6d737dd4b0fe9eccf943abb3677cfea05a6c4) into the SCSI subsystem. It is suitable for Cisco's PCI Express FCoE (fibre channel over Ethernet) HBA (host bus adapter). 2.6.30 has already seen one change for ancient, dusty hardware in the form of an ISA sound driver â€“ now it's the turn of the 3c509 driver, which addresses some 3com network chips [found in EISA systems](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cf9f6e21c155d5add733b969c695837ead79eeab). Other late arrivals can be found in the list at the end of this article.

The changes described are just some of the more significant changes made to architecture code and infrastructure by kernel hackers. Numerous further changes can be found from the list of commit headers from the main development tree below. The links take you directly to the changes in the main development tree [web interface](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=summary), where commit comments and the patches themselves provide extensive additional information on these perhaps less major, but in no way insignificant, changes.

**Architechure-Code**

*x86 (x86-32, x86-64)*

- [docs, x86: add nox2apic back to kernel-parameters.txt](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8b5b94e4e9813cdd77103827f48d58c806ab45c6)
- [Documentation/x86/boot.txt: modify fieldname](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e56d0cfe7790fd3218ae4f6aae1335547fea8763)
- [percpu: add optimized generic percpu accessors](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6dbde3530850d4d8bfc1b6bd4006d92786a2787f)
- [stackprotector: use canary at end of stack to indicate overruns at oops time](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7c9f8861e6c9c839f913e49b98c3854daca18f27)
- [x86: add linux kernel support for YMM state](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a30469e7921a6dd2067e9e836d7787cfa0105627)
- [x86: allow more than 8 cpus to be used on 32-bit](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4272ebfbefd0db40073f3ee5990bceaf2894f08b)
- [x86: cleanup, rename CONFIG_X86_NON_STANDARD to CONFIG_X86_EXTENDED_PLATFORM](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c5c606d9dce6e0852a401c57a8b0542acdbb6796)
- [x86: convert to the new dynamic percpu allocator](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=11124411aa95827404d6bfdfc14c908e1b54513c)
- [x86: disable X86_PTRACE_BTS for now](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d45b41ae8da0f54aec0eebcc6f893ba5f22a1e8e)
- [x86: DMI match for the Sony VGN-Z540N as it needs BIOS reboot](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=88dff4936c0a5fa53080cca68dc963a8a2a674b0)
- [x86/doc: mini-howto for using earlyprintk=dbgp](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a1aade478862fca8710904532cbc6efed97fd05a)
- [x86, documentation: kernel-parameters replace X86-32,X86-64 with X86](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6cececfcece2b072d29886ed7140495f3af17153)
- [x86: Fix performance regression caused by paravirt_ops on native kernels](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b4ecc126991b30fe5f9a59dfacda046aeac124b2)
- [x86: fully honor "nolapic"](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f11826385b63566d98c02d35f592232ee77cd791)
- [x86: hpet: allow force enable on ICH10 HPET](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=42bb8cc5e81028e217105299001070d57eb84ad7)
- [x86: implement x86_32 stack protector](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=60a5317ff0f42dd313094b88f809f63041568b08)
- [x86: improve the help text of X86_EXTENDED_PLATFORM](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8425091ff8af2addae118fc510a523b84ce51115)
- [x86: introduce noxsave boot parameter](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0c752a93353d9b17dbe148312d732fbe06d235e1)
- [x86, kexec: x86_64: add kexec jump support for x86_64](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fee7b0d84cc8c7bc5dc212901c79e93eaf83a5b5)
- [x86: make lazy %gs optional on x86_32](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ccbeed3a05908d201b47b6c3dd1a373138bba566)
- [x86: make Voyager use x86 per-cpu setup.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=89c9c4c58ee86e6e8802597271f23679e0c46647)
- [x86, mce, cmci: add CMCI support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=88ccbedd9ca85d1aca6a6f99df48dce87b7c02d4)
- [x86, mce: implement dynamic machine check banks support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0d7482e3d76522157c9d741d79fce22c401fa0c5)
- [x86: replace CONFIG_X86_SMP with CONFIG_SMP](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3e5095d15276efd14a45393666b1bb7536bf179f)
- [x86: set X86_FEATURE_TSC_RELIABLE](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=83ce400928680a6c8123d492684b27857f5a2d95)
- [x86: unify stackprotector features](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=113c5413cf9051cc50b88befdc42e3402bb92115)
- [x86: update description for memtest boot parameter](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9e5f6cf5f755ca5c52071c317421fae19966a658)

*ARM*

- [ARM: 5353/1: fbdev: add E-Ink Broadsheet controller support v3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0d4ff4df341208b1b75e01feca27301c0dcbf490)
- [ARM: 5354/1: mach-pxa: add AM300 platform driver v3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4ce255c1420dd7c4b97ad4dabd13fa5d862ad700)
- [ARM: 5355/1: Adding support for the HTC Himalaya and its framebuffer](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b7eb1a5ed50c6f622664bb8a7113313fa8b6dd1e)
- [ARM: 5372/1: ACS5K: Core board support for the ACS-5000](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b74788d8c118a48585ad5342560e0aea6ed0ccd4)
- [ARM: 5412/1: XSCALE: add ice dcc support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c633c3cfcf41efe720020553aa3d4782fa0b9bd5)
- [ARM: add CONFIG_HIGHMEM option](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=053a96ca11a9785a7e63fc89eed4514a6446ec58)
- [ARM: Add Gemini architecture v3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=59d3a193f1ec1639db447aa1ceb39cd1811fb36e)
- [ARM: add i.MX35 build support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cb8ebb0223a5a2ec6f2e0b46ef5812113847df61)
- [ARM: Add support for FA526 v2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=28853ac8fe5221de74a14f1182d7b2b383dfd85c)
- [ARM: Add Synertronixx scb9328 board support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2420563227897ed3900606e720f886e122944d2c)
- [ARM: Kirkwood: Marvell SheevaPlug support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4640fa606bf996d275a6e208e3654e9e943afe60)
- [ARM: mv78xx0: Add Marvell RD-78x00-mASA Reference Design support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=569106c70e49ad67c69fa7d43a2a5218e63a4619)
- [ARM: MX31/MX35: Add l2x0 cache support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cb88214d726b337d49c1f65cbc5e5ac85837b11b)
- [ARM: OMAP3: Add support for 3430 SDP, v4](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6fdc29e262f9a776a77f50ca9157f7c0dcfbbbc8)
- [ARM OMAP3: Initial support for Nokia RX-51, v3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ffe7f95bb1a4d1e9ca5d252445dc38476e1a208e)
- [ARM: pxa: add base support for Marvell's PXA168 processor line](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=49cbe78637eb0503f45fc9b556ec08918a616534)
- [ARM: pxa: add base support for pxa910-based TavorEVB](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a3929f31cb2300f1ab190a0168e55bb55222ee40)
- [ARM: pxa: add base support for pxa910-based TTC_DKB](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=01215e35c28a719f38e2cafe90a2806f0e452de6)
- [ARM: pxa: add eXeda platform support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7f14a78713e0b4517f785402accaccca22df93c1)
- [ARM: pxa: Add support for suspend on PalmTX, T5 and LD](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=81854f82c5c1a203b2f5c94f6aa2ed8b8e19f025)
- [ARM: pxa: PalmLD initial support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a645072a608356990b2737a48ecc1bfb66981599)
- [ARM: pxa: PalmT5 initial support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0f6ff0f06cc126e8dfaa20c8c6da53537e352378)
- [ARM: pxa: Palm Tungsten E2 basic support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=54088bf50f31e5f20e005922dae8948f9f856b79)
- [Gemini: Add support for Teltonika RUT100](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=839e642f3dda44a35c6a91780bff41d84c288022)
- [Gemini: gpiolib based GPIO support v2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1df621ae2f3b03d557d962a7afec2b1d04558986)
- [mx31ads: Initial support for Wolfson Microelectronics 1133-EV1 module](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fe7316bff119a11e68f895ecf9a5a713ed30004c)

*Power*

- [AMCC PPC 460SX redwood SoC platform initial framework](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6c7120902305b3a21460cd2f0f917a39307df566)
- [powerpc/5200: Add support for the Media5200 board from Freescale](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bfee95bb830ff0260f3e2e0b1aa6b7492573fe4d)
- [powerpc/83xx: Add power management support for MPC837x boards](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=125a00d74ea57a901fd4cc3d84baf2e825704b68)
- [powerpc/85xx: Add support for the "socrates" board (MPC8544).](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=393adcacadeea407925348b1a59ae8509ecffb3c)
- [powerpc/amigaone: Add platform support for AmigaOne](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=54b318aa5211ab7bba617a27d9cbd7fd759dcfd0)
- [powerpc/device-tree: Document MTD nodes with multiple "reg" tuples](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c5a88dd90cf243a17c4a8c10e1ed973192ea5825)
- [powerpc: Hook up rtc-generic, and kill rtc-ppc](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bcd68a70cb0eee556d86d93133aa150319bd9f53)
- [powerpc/of-device-tree: Factor MTD physmap bindings out of booting-without-of](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=efcc2da3fd148c9acb7d7cf1d9800e0649f950fc)
- [powerpc/ps3: Add rtc-ps3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0b5f037a4dc495f9c40eed7f076fc6c23af3359b)

*Various*

- [Add Merisc board support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a16fffdd8eb95ebab7dc22414896fe6493951e0e)
- [m68k: mac - Add SWIM floppy support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8852ecd97488249ca7fe2c0d3eb44cae95886881)
- [Move dtc and libfdt sources from arch/powerpc/boot to scripts/dtc](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9fffb55f66127b52c937ede5196ebfa0c0d50bce)
- [S390: dasd: add High Performance FICON support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f3eb5384cf0325c02e306b1d81e70f81a03d7432)
- [sh: Add in PCI bus for DMA API debugging.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e588a00fe546695e93077b3f7b7009f0c31d9370)
- [sh: Add support for DMA API debugging.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f802d969b6a89d3f9b67ef879179824d53420ebe)
- [sh: Add support for SH7786 CPU subtype.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=55ba99eb211a06709237cb322ecd8c8b6faf6159)
- [sh: add support for SMSC Polaris platform](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=eaeed5d31d8ded02fa0a4b608f57418cc0e65b07)
- [sh: dma-sh updates for multi IRQ and new SH-4A CPUs.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=71b973a42c5456824c8712e00659d9616d395919)
- [sh: espt-giga board support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=32910e2c52cae552f2651c5360bae8033adb8aac)
- [sh: hibernation support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2ef7f0dab6b3d171b6aff00a47077385ae3155b5)
- [sh: Plug in support for ARCH=sh64 using sh SRCARCH.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3cc000b58360d8df402e31277c3dc0ebe34ad110)
- [sh: urquell: Add smc91x support and update defconfig accordingly.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=929ef1a1f566087e4b362e3a56c50bf9db30e3c5)
- [sh: Urquell board support.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5ac072e110ff358a9ebc318a1b54f0182b799f72)
- [xtensa: beat Kconfig into shape](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=35f9cd083b350ad4eb3b5f159c7738fa9ddff40a)
- [xtensa: nommu support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e5083a63b6a8546c5fe1e571fe529e3939787ec2)
- [xtensa: platform: s6105](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f82e939fb75ad01da8f0d3024fc678111ddb4ac7)

*Virtualization*

- [KVM: Add support to disable MSI for assigned device](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=17071fe74fe0fbfdb03cd9b82f2490447cf1f986)
- [KVM: New guest debug interface](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d0bfb940ecabf0b44fb1fd80d8d60594e569e5ec)
- [KVM: ppc: E500 core-specific code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bc8080cbcc8870178f0910edd537d0cb5706d703)
- [KVM: SVM: Add helper functions for nested SVM](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c0725420cfdcf6dd9705b164a8c6cba86684080d)
- [KVM: Userspace controlled irq routing](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=399ec807ddc38ecccf8c06dbde04531cbdc63e11)
- [lguest: use KVM hypercalls](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4cd8b5e2a159f18a1507f1187b44a1acbfa6341b)
- [xen: mask XSAVE from cpuid](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=191216b9289ed02256086e6bab4f668112109399)

**Infrastructure**

*bzip2/lzma*

- [bzip2/lzma: centralize format detection](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=889c92d21db40be0b7d22a59395060237895bb85)
- [bzip2/lzma: clarify the meaning of the CONFIG_RD\_ options](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=337bed413e9c134c5bf45ad3ec50012a593c603a)
- [bzip2/lzma: comprehensible error messages for missing decompressor](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=23a22d57a8962479ca630c9542e62d6f86fdf927)
- [bzip2/lzma: consistently capitalize LZMA in Kconfig](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=55d1d26f23383163a256d0de2aaf2b8fca83e611)
- [bzip2/lzma: DECOMPRESS_GZIP should select ZLIB_INFLATE](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7856a16ea03ed9b17860d756ee6473c2e57882b2)
- [bzip2/lzma: don't ask for compression mode for the default initramfs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=40297927575a50b1d0d308d735c445924d33fba6)
- [bzip2/lzma: don't leave empty files around on failure](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ab59d3b70f7a47987f80e153d828363faec643fe)
- [bzip2/lzma: don't stop search at first unconfigured compression](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e4aa7ca5a2e6d44f07ceb87d9448113f5b48a334)
- [bzip2/lzma: fix built-in initramfs vs CONFIG_RD_GZIP](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a26ee60f90daffe1de6be0d093af86e7279b3dfd)
- [bzip2/lzma: fix constant in decompress_inflate](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5619448fc55650cb76cbb825e16e4bb5d1390399)
- [bzip2/lzma: fix decompress_inflate.c vs multi-block-with-embedded-filename](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6c11b12ac6f101732d43b5682f5b3ae4dda4205f)
- [bzip2/lzma: handle failures from bzip2 and lzma correctly](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0f5e2d2484ccd3062bb1f63083bafa37041bc868)
- [bzip2/lzma: make config machinery an arch configurable](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2e9f3bddcbc711bb14d86c6f068a779bf3710247)
- [bzip2/lzma: make flush_buffer() unconditional](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=736f93236ce786d1bcf09ad4dcb38a360d35ea1b)
- [bzip2/lzma: make internal initramfs compression configurable](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ab76f3d771590d5c89faa3219559c5d3fc0ce0c2)
- [bzip2/lzma: move CONFIG_RD\_\* options under CONFIG_EMBEDDED](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=73d8a12f05292d86623b4ec7bf5fd75d5ad5f687)
- [bzip2/lzma: move initrd/ramfs options out of BLK_DEV](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fb9a4ca9820fd4d7c4906bd393004662451e273e)
- [bzip2/lzma: proper Kconfig dependencies for the ramdisk options](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c8531ab343dec88ed8005e403b1b304c710b7494)
- [bzip2/lzma: update boot protocol specification](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ee287587dafd77fd211e50637561224605c214b4)
- [bzip2/lzma: use a table to search for initramfs compression formats](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b172fd882d201cf8aa67cddd9c1a023421fd4956)

*Crypto*

- [crypto: aes - Export x86 AES encrypt/decrypt functions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=07bf44f86989f5ed866510374fe761d1903681fb)
- [crypto: api - Use dedicated workqueue for crypto subsystem](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=25c38d3fb92fc23af7730a1601bc20af8216ae44)
- [crypto: compress - Add pcomp interface](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a1d2f09544065b60598b8167d94a6371bff3e892)
- [crypto: zlib - New zlib crypto module, using pcomp](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bf68e65ec9ea61e32ab71bef59aa5d24d255241f)
- [hwrng: timeriomem - New driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9c3c133b1ed6e6d01bfabb6de29bf3d0f0886354)

*Fastboot*

- [ACPI: battery: asynchronous init](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0f66af530116e9f4dd97f328d91718b56a6fc5a4)
- [async: remove the temporary (2.6.29) "async is off by default" code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9710794383ee5008d67f1a6613a4717bf6de47bc)
- [driver synchronization: make scsi_wait_scan more advanced](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d4d5291c8cd499b1b590336059d5cc3e24c1ced6)
- [fastboot: remove duplicate unpack_to_rootfs()](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=df52092f3c97788592ef72501a43fb7ac6a3cfe0)
- [ide/net: flip the order of SATA and network init](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0c406263f0a22b9fad65404cf2b14eced0739485)
- [PM/Hibernate: Wait for SCSI devices scan to complete during resume](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c751085943362143f84346d274e0011419c84202)

*MM*

- [memcg: fix documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c863d835b7cd9a3c08a941d4ae59b8faefa31422)
- [mm: add documentation describing what tsk-\>active_mm means vs tsk-\>mm](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a55ce6dc705c9ed0bb0d4f629dbcaf3b3ced5172)
- [mm: add /proc controls for pdflush threads](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fafd688e4c0c34da0f3de909881117d374e4c7af)
- [mm: close page_mkwrite races](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b827e496c893de0c0f142abfaeb8730a2fd6b37f)
- [mm: reformat the Unevictable-LRU documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c24b720188e9a1f83caa5b6d49b4cb5b843256f1)
- [nommu: make the initial mmap allocation excess behaviour Kconfig configurable](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fc4d5c292b68ef02514d2072dcbf82d090c34875)
- [percpu: implement new dynamic percpu allocator](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fbf59bc9d74d1fb30b8e0630743aff2806eafcea)
- [percpu, module: implement reserved allocation and use it for module percpu variables](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=edcb463997ed7b2ffa3bac76e3e75957318f2e01)
- [slub: add Documentation/ABI/testing/sysfs-kernel-slab](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=51e95bed6263f6a2e558ca04fc4ff877f3b0cca3)
- [slub: add min_partial sysfs tunable](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=73d342b169db700b5a6ad626fe4b86911efec8db)
- [writeback: double the dirty thresholds](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1b5e62b42b55c509eea04c3c0f25e42c8b35b564)
- [x86, percpu: setup reserved percpu area for x86_64](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6b19b0c2400437a3c10059ede0e59b517092e1bd)

*PCI and ACPI*

- [ACPI: acpi_enforce_resource=strict by default](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7e90560c50f754d65884e251e94c1efa2a4b5784)
- [ACPI: add /sys/firmware/acpi/interrupts/sci_not counter](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=88bea188b85f9cefefbbd56b8a48d0f798409177)
- [ACPI: Adjust Kelvin offset to match local implementation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=13614e37e94da4606a300ee6fe25c8c4a19ee670)
- [ACPICA: Add function to handle PM1 control registers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=32c9ef994d91352b710b948ec369cd18d6bca51b)
- [ACPICA: Add override for dynamic tables](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d3ccaff827cef5a5c5a0f3c97e1e2e6d99f618cb)
- [ACPICA: Allow OS override of all ACPI tables](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ac5f98db7be34cefc244026f882cf030debb7431)
- [ACPICA: New: I/O port protection](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7f0719039085cc40114abce84cf29fe57da226f4)
- [ACPI: cap off P-state transition latency from buggy BIOSes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a59d1637eb0e0a37ee0e5c92800c60abe3624e24)
- [acpi: fix of pmtimer overflow that make Cx states time incorrect](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ff69f2bba67bd45514923aaedbf40fe351787c59)
- [ACPI: Idle C-states disabled by max_cstate should not disable the TSC](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a0bf284bfedd6dc95bbee7ebf5ccf3b5f753a008)
- [ACPI: move thermal trip handling to generic thermal layer](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b1569e99c795bf83b4ddf41c4f1c42761ab7f75e)
- [ACPI processor: introduce module parameter processor.ignore_tpc](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=56c213fa012f2bad9eff908292ff2500f840b020)
- [ACPI processor: reset the throttling state once it's invalid](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4973b22aa8c70fe036e3e0039f104cf5bb7fe2b1)
- [ACPI: video: DMI workaround another broken Acer BIOS enabling display brightness](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5afc4abe7902b8453c248321daa9b13b12d9c838)
- [Enable PNPACPI \_PSx Support, v3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6328a57401dc5f5cf9931738eb7268fcd8058c49)
- [genirq: add doc to struct irqaction](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a9d0a1a38352c4fb8946e73b3e42ba4ada29e733)
- [genirq: deprecate \_\_do_IRQ](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0e57aa11abb15b70db53d1f95ae70b3c980ac885)
- [genirq: deprecate obsolete typedefs and defines](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cb065c06b6cc615a58860d619d7fa7952cd6a18b)
- [intel-iommu: Enable DMAR on 32-bit kernel.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4cf2e75d0bec15d945972b005056c4a8731b82cf)
- [intel-iommu: fix PCI device detach from virtual machine](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3199aa6bc8766e17b8f60820c4f78d59c25fce0e)
- [Intel IOMMU Suspend/Resume Support - DMAR](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f59c7b69bcba31cd355ababe067202b9895d6102)
- [Intel IOMMU Suspend/Resume Support - Interrupt Remapping](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b24696bc55f66fecc30715e003f10fc2555a9271)
- [Intel IOMMU Suspend/Resume Support - Queued Invalidation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=eb4a52bc660ea835482c582eaaf4893742cbd160)
- [intel-iommu: VT-d page table to support snooping control bit](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9cf0669746be19a4906a6c48920060bcf54c708b)
- [I/O port protection: update for windows compatibility.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a65131e942e25c707a652fa4ec2cfcd8b63fec11)
- [PCI: add remove_id sysfs entry](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0994375e9614f78657031e04e30019b9cdb62795)
- [PCI: add SR-IOV API for Physical Function driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=dd7cc44d0bcec5e9c42fe52e88dc254ae62eac8d)
- [PCI: allow assignment of memory resources with a specified alignment](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=32a9a682bef2f6fce7026bd94d1ce20028b0e52d)
- [PCI: document SR-IOV sysfs entries](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=01db4957179c92fda7d9a06e49b7ae56fb7c925b)
- [PCI: handle SR-IOV Virtual Function Migration](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=74bb1bcc7dbbc9ddef773bf3395d7ff92aaaad2e)
- [PCI Hotplug: restore fakephp interface with complete reimplementation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=83dbf66f04b96e65c6c18436c16d40f9cf8630aa)
- [PCI Hotplug: schedule fakephp for feature removal](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f110ca489c9b7cf3f6c9656e383e787f3aee217f)
- [PCI: initialize and release SR-IOV capability](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d1b054da8f599905f3c18a218961dcf17f9d5f13)
- [PCI: Introduce pci_rescan_bus()](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3ed4fd96b3188406ac5357d9290bcffa08c65cf6)
- [PCI: Introduce /sys/bus/pci/devices/.../remove](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=77c27c7b49d69d45ccb94e481653f024f1ac6650)
- [PCI: Introduce /sys/bus/pci/devices/.../rescan](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=738a6396c223b486304dda778119dbbca563f019)
- [PCI: Introduce /sys/bus/pci/rescan](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=705b1aaa823e800490f157cd9366ad8cff385f5f)
- [PCI: manual for SR-IOV user and driver developer](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=15b49bee3a2b228370194f1b3ebc3db427cc9c94)
- [PCI MSI: Add example request loop to MSI-HOWTO.txt](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fafad5bf06c3a3bb8b24b28b6f065367e7411872)
- [PCI quirk: disable MSI on VIA VT3364 chipsets](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=162dedd39dcc6eca3fc0d29cf19658c6c13b840e)
- [PCI: Setup disabled bridges even if buses are added](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=296ccb086dfb89b5b8d73ef08c795ffdff12a597)
- [PCI: SR-IOV quirk for Intel 82576 NIC](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7eb93b175d4de9438a4b0af3a94a112cb5266944)
- [PCI/x86: detect host bridge config space size w/o using quirks](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=dfadd9edff498d767008edc6b2a6e86a7a19934d)
- [PCI/x86: document pci=earlydump argument](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1cc0ca26c57221f5aa0f49a311a8fc83413dfe97)
- [Rewrite MSI-HOWTO](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c41ade2ee1dc146d2de2ee470a87cd6b878a08f4)
- [ssb: Add PMU support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c9703146158c0415a60799570397e488bc982af5)
- [thermal: support forcing support for passive cooling](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=03a971a2899886006f19f3495973bbd646d8bdae)
- [x86 ACPI: Add support for Always Running APIC timer](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=db954b5898dd3ef3ef93f4144158ea8f97deb058)
- [x86, ACPI: add support for x2apic ACPI extensions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7237d3de78ff89ec2e18eae5fe962d063024fef5)

*Power management*

- [CPUFREQ: Change link order of x86 cpufreq modules](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=de3ed81d746d7cfc22a0c645244ed9fa71e4a833)
- [CPUFREQ: Introduce /sys/devices/system/cpu/cpu\*/cpufreq/cpuinfo_transition_latency](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ed12978453a3845c947695e7ad32bb3ede444813)
- [CPUFREQ: ondemand/conservative: deprecate sampling_rate{min,max}](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9411b4ef7fcb534fe1582fe02738254e398dd931)
- [CPUFREQ: ondemand/conservative: sanitize sampling_rate restrictions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=112124ab0a9f507a0d7fdbb1e1ed2b9a24f8c4ea)
- [CPUFREQ: Prevent p4-clockmod from auto-binding to the ondemand governor.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=36e8abf3edcd2d207193ec5741d1a2a645d470a5)
- [PCI PM: Make pci_set_power_state() handle devices with no PM support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4a865905f685eaefaedf6ade362323dc52aa703b)
- [PCI PM: Put devices into low power states during late suspend (rev. 2)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=46939f8b15e44f065d052e89ea4f2adc81fdc740)
- [PCI PM: Restore config spaces of all devices during early resume](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=931ff68a5a53fa84bcdf9b1b179a80e54e034bd0)
- [PM: Change hibernation code ordering](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4aecd6718939eb3c4145b248369b65f7483a8a02)
- [PM: Change suspend code ordering](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=900af0d973856d6feb6fc088c2d0d3fde57707d3)
- [PM: Introduce functions for suspending and resuming device interrupts](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0a0c5168df270a50e3518e4f12bddb31f8f5f38f)
- [PM/Suspend: Introduce two new platform callbacks to avoid breakage](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6a7c7eaf71b636f197d73b381a2ab729ebdcfb2e)

*Scheduler*

- [sched: activate active load balancing in new idle cpus](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ad273b32e482cdef306eac32b28d97f513a022f4)
- [sched: add hierarchical accounting to cpu accounting controller](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=934352f214b3251eb0793c1209d346595a661d80)
- [sched: add SD_BALANCE_NEWIDLE at MC and CPU level for sched_mc\>0](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=100fdaee70ebf5f31b9451fbc01300c627091328)
- [sched: allow architectures to specify sched_clock_stable](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b342501cd31e5546d0c9ca8ceff5ded1832f9e5b)
- [sched, documentation: update scheduler header file paths](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=90080bf4b803efbc9b9cd3a7ed1639f1e036238e)
- [sched: favour lower logical cpu number for sched_mc balance](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d5679bd11916eba5c8ee9033003e1a5ce56ece9a)
- [sched: framework for sched_mc/smt_power_savings=N](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=afb8a9b70b86866a60e08b2956ae4e1406390336)
- [sched: improve preempt debugging](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=7317d7b87edb41a9135e30be1ec3f7ef817c53dd)
- [sched, latencytop: incorporate review feedback from Andrew Morton](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ad0b0fd554dfc126b5750d14908dccc3bbf602be)
- [sched: nominate preferred wakeup cpu](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=7a09b1a27b1e5a4957e4af9951420fea02c44fba)

*Security*

- [netlabel: Label incoming TCP connections correctly in SELinux](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=389fb800ac8be2832efedd19978a2b8ced37eb61)
- [proc: avoid information leaks to non-privileged processes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f83ce3e6b02d5e48b3a43b001390e2b58820389d)
- [TPM: sysfs functions consolidation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0883743825e34b81f3ff78aaee3a97cba57586c5)

*Tomoyo*

- [Common functions for TOMOYO Linux.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9590837b89aaa4523209ac91c52db5ea0d9142fd)
- [Domain transition handler.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=26a2a1c9eb88d9aca8891575b3b986812e073872)
- [File operation restriction part.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b69a54ee582373d76e4b5560970db5b8c618b12a)
- [Kconfig and Makefile](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=00d7d6f840ddc947237307e022de5e75ded4105f)
- [LSM adapter functions.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f7433243770c77979c396b4c7449a10e9b3521db)
- [MAINTAINERS info](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d74db3b22a75fac474abe711f582ffe25eacce25)
- [Memory and pathname management functions.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c73bd6d473ceb5d643d3afd7e75b7dc2e6918558)
- [tomoyo: add Documentation/tomoyo.txt](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=17a7b7b39056a82c5012539311850f202e6c3cd4)
- [tomoyo: version bump to 2.2.0.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=39826a1e17c1957bd7b5cd7815b83940e5e3a230)

*Tracing*

- [blkftrace: binary tracing, synthesizing old format](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=08a06b83ff8b2779289f733348c669f31cb65d51)
- [blktrace: print human-readable act_mask](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=093419971e03362a00f499960557c119982ea09f)
- [debug_objects: add boot-parameter toggle to turn object debugging off again](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3e8ebb5c433f016dff5824587436642d87fc2e6c)
- [doc: add trace_buf_size description to kernel-parameters.txt](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=631595fbf4aeac260e664a8a002897e4db6a50dd)
- [doc: mmiotrace.txt, buffer size control change](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5d2ad3316e29ad218f98d66b9c0ce6d4bcd05b77)
- [Documentation/ftrace.txt: update](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5752674e140db5bce08c6bc60021a9bc3b960800)
- [ftrace: add pretty print function for traceon and traceoff hooks](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e110e3d1eaa0f9628918be67ddd32e8ad65a2871)
- [ftrace: add stack trace to function tracer](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5361499101306cfb776c3cfa0f69d0479bc63868)
- [ftrace: add traceon traceoff commands to enable/disable the buffers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=23b4ff3aa479c9e3bb23cb6b2d0a97878399784a)
- [ftrace: event profile hooks](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ac199db0189c091f2863312061c0575937f68810)
- [ftrace: fix documentation typo s/trace_max_latency/tracing_max_latency/](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=42b40b3d55f5782b00b74d9105c3565fbfa5cb80)
- [ftrace, ia64: IA64 dynamic ftrace support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a14a07b8018b714e03a39ff2180c66e307ef4238)
- [ftrace: trace different functions with a different tracer](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=59df055f1991c9fc0c71a9230663c39188f6972f)
- [function-graph: add option for include sleep times](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=be6f164a02f394675e2ac2077dd354cebef5b4c0)
- [function-graph: add proper initialization for init task](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5ac9f62267dc92c7735c642a5942d9e6c1190308)
- [function-graph: show binary events as comments](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5087f8d2a2f2daff5a913d72d8ea3ad601948e10)
- [kmemtrace: Additional documentation.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=aa46a7e0228c0477708ce44a0c5621902b3c157c)
- [kmemtrace: Fix typos in documentation.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4a80b24bb2ec66a5cb7fa5ff8335907f09288200)
- [kmemtrace: remove config option for enabling tracing at boot](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bf6803d6fd654d9a73cd90308b5225d78655d027)
- [kprobes: support kretprobe and jprobe per-probe disabling](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8f9b15286a8ea49e997e845d02d357ed33ebd090)
- [kprobes: support per-kprobe disabling](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=de5bd88d5a5cce3cacea904d3503e5ebdb3852a2)
- [sysrq: fix ftrace help msg Commit: 3871f2ffe53db3cef4fe0c18993ad9e6e0f69408 doc.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3871f2ffe53db3cef4fe0c18993ad9e6e0f69408)
- [trace: let boot trace be chosen by command line](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=79fb0768fbd371f3b94d909f51f587b3a24ab272)
- [trace: mmiotrace to the tracer menu in Kconfig](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fe6f90e57fd31af8daca534ea01db2e5666c15da)
- [tracing: add binary buffer files for use with splice](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2cadf9135eb3b6d84b6427314be827ddd443c308)
- [tracing: add event trace infrastructure](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b77e38aa240c3bd9c55c98b9f7c81541e042eae5)
- [tracing: add format files for ftrace default entries](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=770cb24345c0f6e0d47bd2b94aa6d67bea6f8b54)
- [tracing: add global-clock option to provide cross CPU clock to traces](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=af4617bdba34aa556272b34c3986b0a4d588f568)
- [tracing: add options directory and core option files](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a8259075074fb09c230b4cd2c8d3ee3c49d6ecd1)
- [tracing: add per-event filtering](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7ce7e4249921d5073e764f7ff7ad83cfa9894bd7)
- [tracing: add per-subsystem filtering](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cfb180f3e71b2a280a254c8646a9ab1beab63f84)
- [tracing: add run-time field descriptions for event filtering](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cf027f645e6aee4f0ca6197a6b6a57f327fdb13f)
- [tracing: add schedule events to event trace](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f3fe8e4a38fd19dbb3f8ffb1826aa840ae304a65)
- [tracing: add subsystem level to trace events](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6ecc2d1ca39177edb6fbdb7412948b0e9f409d02)
- [tracing: consolidate documents](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=66bb74888eb4bef4ba7c87c931ecb7ecca3a240c)
- [tracing/core: drop the old trace_printk() implementation in favour of trace_bprintk()](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=769b0441f438c4bb4872cb8560eb6fe51bcc09ee)
- [tracing: Documentation / sample code fixes for tracepoints](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0a5d649018b151cb9331c213a843ac4a3e7e44ab)
- [tracing: Don't use tracing_record_cmdline() in workqueue tracer](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c3ffc7a40b7e94b094efe1c8ab4e24370a782b65)
- [tracing: explain why stack tracer is empty](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e447e1df2e568cd43d1918963c9f09fae85aea57)
- [tracing/ftrace: handle more than one stat file per tracer](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=034939b65ad5ff64b9709210b3469a95153c51a3)
- [tracing/ftrace: provide the base infrastructure for histogram tracing](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=dbd0b4b33074aa6b7832a9d9a5bd985eca5c1aa2)
- [tracing/ftrace: syscall tracing infrastructure, basics](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ee08c6eccb7d1295516f7cf420fddf7b14e9146f)
- [tracing/function-graph-tracer: provide documentation for the function graph tracer](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=985ec20ad531f2641ab9d5193e37891fe959fc7d)
- [tracing/function-graph-tracer: various fixes and features](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9005f3ebebfcfe9ccd731d16c468907a35ac1f9a)
- [tracing, genirq: add irq enter and exit trace events](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=af39241b90a345556b8884adff87096afe71b050)
- [tracing: infrastructure for supporting binary record](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1427cdf0592368bdec57276edaf714040ee8744f)
- [tracing/kmemtrace: normalize the raw tracer event to the unified tracing API](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=36994e58a48fb8f9651c7dc845a6de298aba5bfc)
- [tracing: make event directory structure](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1473e4417c79f12d91ef91a469699bfa911f510f)
- [tracing/syscalls: core infrastructure for syscalls tracing, enhancements](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bed1ffca022cc876fb83161d26670e9b5d3cf36b)
- [tracing/x86: basic implementation of syscall tracing for x86](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1b3fa2ce64363c289b3b14723cca7290bf91cfce)
- [Update /debug/tracing/README](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bc2b6871c17b3aff79fb14e1a1c06c5f5a187f76)
- [x86, ftrace, hw-branch-tracer: documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e2ea5399bb4fb7aaafb08f846db453f4eec55160)

*Various*

- [Add README.AddingFirmware file. Basically telling people not to.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0f8e5c298fc801e8eca69e1409604c05d36e0cc4)
- [cgroup: CSS ID support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=38460b48d06440de46b34cb778bd6c4855030754)
- [cgroups: more documentation for remount and release_agent](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b6719ec1ad54e47e40633b19703f2c1254708842)
- [cpuacct: add per-cgroup utime/stime statistics](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ef12fefabf94b6a902ad3abd3eb124b00560c445)
- [dma-debug: add checks for kernel text and rodata](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2e34bde18576a02c897ae6b699ea26301d92be1b)
- [dma-debug: add core checking functions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2d62ece14fe04168a7d16688ddd2d17ac472268c)
- [dma-debug: add debugfs interface](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=788dcfa6f17424695823152890d30da09f62f9c3)
- [dma-debug: add header file and core data structures](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f2f45e5f3c921c73c913e9a9c00f21ec01c86b4d)
- [dma-debug: add Kconfig entry](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5ee00bd4691e7364bb7b62e2068d473cd5cb9320)
- [dma-debug: add kernel command line parameters](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=59d3daafa17265f01149df8eab3fb69b9b42cb2e)
- [dma-debug: Documentation update](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=187f9c3f05373df4f7cbae2e656450acdbba7558)
- [dma-debug: x86 architecture bindings](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2118d0c548e8a2205e1a29eb5b89e5f2e9ae2c8b)
- [dma-mapping: update the old macro DMA_nBIT_MASK related documentations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2c5510d4e84988ea95f86488d1e23244284bc1ed)
- [dynamic debug: combine dprintk and dynamic printk](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e9d376f0fa66bd630fe27403669c6ae6c22a868f)
- [dynamic debug: update docs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=86151fdf38b3795f292b39defbff39d2684b9c8c)
- [init: make initrd/initramfs decompression failure a KERN_EMERG event](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=73310a169aebe257efdd35a763cce1c7658f40c9)
- [kbuild: introduce destination-y for exported headers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c7bb349e7c25df1ae1bbb72675b9bb02e1d9c464)
- [kbuild: introduce subdir-ccflags-y](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=720097d895956c0bf15b8440f7845159a04b74da)
- [kbuild: make it possible for the linker to discard local symbols from vmlinux](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5d7d18f5bc507b60d3d8967e2739d5e6ffdd630f)
- [kbuild: support include/generated](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f14875a3e0cc35d7dbe15ee39763a6ae922e7034)
- [kexec: add dmesg log symbols to /proc/vmcoreinfo lists](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=04d491ab2a53008a1aa98ac09561768c7f3adda3)
- [Ksplice: Add functions for walking kallsyms symbols](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=75a66614db21007bcc8c37f9c5d5b922981387b9)
- [LANANA: Change of management and resync](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=04c860c188ebdcf396fd50751592fb5a9f51287a)
- [memcg: fix OOM killer under memcg](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0b7f569e45bb6be142d87017030669a6a7d327a1)
- [memcg: use CSS ID](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=04046e1a0a34286382e913f8fc461440c21d88e8)
- [module: clarify the force-loading taint message.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c6e665c8f0c18ab3686117905765b5139efd6ebd)
- [module: Export symbols needed for Ksplice](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c6b37801911d7f4663c99cad8aa230bc934cea82)
- [printk: introduce printk_once()](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f036be96dd9ce442ffb9ab33e3c165f5178815c0)
- [res_counter: update documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5341cfab94ec05b8a45726f9fe15e71c0cd9b915)
- [UIO: Add name attributes for mappings and port regions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8205779114e8f612549d191f8e151526a74ab9f2)
- [uio: add the uio_aec driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1bafeb378e915f39b1bf44ee0871823d6f402ea5)
- [vsprintf: add binary printf](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4370aa4aa75391a5e2e06bccb0919109f725ed8e)
- [vsprintf: unify the format decoding layer for its 3 users](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fef20d9c1380f04ba9492d6463148db07b413708)

**Late arrivals**

*File systems*

- [CIFS: Add new nostrictsync cifs mount option to avoid slow SMB flush](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=be652445fdccb8e5d4391928c3b45324ea37f9e1)
- [CIFS: DFS no longer experimental](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=10e70afa75c90702b2326abaaa757d6b7835636f)
- [cifs: vary timeout on writes past EOF based on offset (try \#5)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fbec9ab952d4810960e620035c8e95f0fbbae4be)
- [Enable dfs submounts to handle remote referrals.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1af28ceb923d04357733642a3dbc4497da4db1c2)

*Documentation*

- [doc: fix kernel-parameters.txt mistaken deletions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4af94f39004a0d1a074e7573457e238a29557848)
- [kernel-doc: restrict syntax for private: and public:](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=52dc5aec9fe2eb591f1490278ae767448860118b)
- [hwmon: Update documentation on fan_max](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d54d462472a16fc07adb53a2fcd6c0c2a9a8dd1d)
- [Input: multitouch - augment event semantics documentation](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f9fcfc3b4627a1ec9b50411060f1b384926d6610)

*Network*

- [Add reference to CAPI 2.0 standard](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2296e5a0136f7ba64c99f3a48a55a687aa9abcc8)
- [ar9170: add Cace Airpcap NX usb_id](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4fc298b86635c60061bbd81cef8de2b031e5c4a7)
- [at76c50x-usb: Add device ID for OQO model 01+](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=02a9a39294017f105aedebcca5f49d552b18dbaa)
- [ath1e: add new device id for asus hardware](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bdb0e010bf0061a73027cc84dd7ad192c663eca3)
- [be2net: add two new pci device ids to pci device table](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c4ca2374312b4de819dd700e72a68395eddb5fcb)
- [Doc: fixed descriptions on /proc/sys/net/core/\* and /proc/sys/net/unix/\*](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=705efc3b03cbee449e4d83b230423894152f7982)
- [Documentation/isdn/INTERFACE.CAPI](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=554f200e22a13e19bd407d0037e41be0ec8a0a2e)
- [iwlwifi: DMA fixes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=df833b1d73680f9f9dc72cbc3215edbbc6ab740d)
- [iwlwifi: fix device id registration for 6000 series 2x2 devices](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=542cc7937e6af73cb2edc455a0e456d22e254abb)
- [netfilter: revised locking for x_tables](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=942e4a2bd680c606af0211e64eb216be2e19bf61)
- [p54: deactivate broken powersave function](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c3b93c878d7912a01467890bc0785071c2dc4bc1)
- [p54usb: add Telsey 802.11g USB2.0 Adapter](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e3062403f5f71c48cf26e791e576f4feca4c9c0f)
- [phylib: Basic support for the M88E1121R Marvell chip](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=140bc92903287cff4545e358c1651e4b7312cbd3)
- [rt2x00: Add rt73usb USB IDs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6aabd4c4441133836ac969a9488458b37f83b677)
- [rtl8187: add USB ID for Linksys WUSB54GC-EU v2 USB wifi dongle](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=aeeab4ff06b8e29cfe2fe730ba626f7e2487ba03)
- [smsc95xx: add support for LAN9512 and LAN9514](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=726474b8cd0f0f49c570b1dbbab44be898797550)

*Storage*

- [via82cxxx: Add VIA VX855 PCI Device ID](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5993856e53fbc4b4f28e2d481deaebeb715b1267)

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the Kernel Log at The H Open Source:*

- [Kernel Log: What's coming in 2.6.30 â€“ Drivers: New drivers for audio, video, USB hardware, netbooks and notebooks](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-Drivers-New-drivers-for-audio-video-USB-hardware-netbooks-and-notebooks-741837.html "Kernel Log: What's coming in 2.6.30 – Drivers: New drivers for audio, video, USB hardware, netbooks and notebooks â 01 June 2009, 18:52")
- [Kernel Log: ALSA driver for the X-Fi, debate over TuxOnIce](../site/news/item/Kernel-Log-ALSA-driver-for-the-X-Fi-debate-over-TuxOnIce-741673.html "Kernel Log: ALSA driver for the X-Fi, debate over TuxOnIce â 21 May 2009, 09:24")
- [Kernel Log: What's coming in 2.6.30 - Storage: RAID improvements, optimised CFQ Scheduler, SAS drivers](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-Storage-RAID-improvements-optimised-CFQ-Scheduler-SAS-drivers-741597.html "Kernel Log: What's coming in 2.6.30 - Storage: RAID improvements, optimised CFQ Scheduler, SAS drivers â 15 May 2009, 17:01")
- [Kernel Log: X.org 7.5 coming in summer, re-write for Intel's graphics driver](../site/news/item/Kernel-Log-X-org-7-5-coming-in-summer-re-write-for-Intel-s-graphics-driver-741405.html "Kernel Log: X.org 7.5 coming in summer, re-write for Intel's graphics driver â 04 May 2009, 07:09")
- [Kernel Log: What's coming in 2.6.30 - File systems: New and revamped file systems](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-File-systems-New-and-revamped-file-systems-741319.html "Kernel Log: What's coming in 2.6.30 - File systems: New and revamped file systems â 27 April 2009, 16:11")
- [Kernel Log: 3D support for the new Radeon driver; new Intel drivers](../site/news/item/Kernel-Log-3D-support-for-the-new-Radeon-driver-new-Intel-drivers-741271.html " Kernel Log: 3D support for the new Radeon driver; new Intel drivers â 22 April 2009, 17:06")
- [Kernel Log: What's coming in 2.6.30 - Network: New Wi-Fi drivers and other network novelties](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-Network-New-Wi-Fi-drivers-and-other-network-novelties-741197.html "Kernel Log: What's coming in 2.6.30 - Network: New Wi-Fi drivers and other network novelties â 17 April 2009, 10:51")
- [Kernel Log: Linux 2.6.30 is taking shape](../site/news/item/Kernel-Log-Linux-2-6-30-is-taking-shape-741093.html "Kernel Log: Linux 2.6.30 is taking shape â 09 April 2009, 06:41")

*Older Kernel Logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/).*

([trk](mailto:trk@h-online.com "Terry Relph-Knight"))
