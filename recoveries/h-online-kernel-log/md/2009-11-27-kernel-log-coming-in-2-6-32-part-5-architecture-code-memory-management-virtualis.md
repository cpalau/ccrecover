---
title: "Kernel Log: Coming in 2.6.32 (Part 5) - Architecture code, memory management, virtualisation and tracing"
date: 2009-11-27
author:
source: http://www.h-online.com/open/news/item/Kernel-Log-Coming-in-2-6-32-Part-5-Architecture-code-memory-management-virtualisation-and-tracing-870357.html
pages: 1
---

# Kernel Log: Coming in 2.6.32 (Part 5) - Architecture code, memory management, virtualisation and tracing

#### ![](../site/imgs/43/4/4/7/8/7/8/KL.jpg-f1b4876436255b3d.jpeg) by Thorsten Leemhuis

**The forthcoming kernel version will support Intel's Moorestown platform, SFI - the alternative to ACPI, and the Trusted Execution Technology, which used to be called "LaGrande Technology". If required, the new KSM can now reduce memory loads by combining identical memory content in virtual machines. The new kernel also includes Timechart, a new tool for visualising what's going on in the system and kernel.**

Since Linus Torvalds has been [on the road](http://thread.gmane.org/gmane.linux.kernel/916278) this week, there have been no changes to the main development branch in the past few days. However, numerous developers have already sent emails to the LKML, asking the father of Linux to merge corrections. As the number of bug fixes increases, so does the likelihood that Torvalds will throw in another release candidate of 2.6.32 when he returns – when releasing [Rc8](http://thread.gmane.org/gmane.linux.kernel/916278), the father of Linux had still hoped this might be the last release candidate.

Therefore, the Kernel Log will wrap up its report about the new features of 2.6.32 with parts 5 and 6. This issue discusses the changes in terms of architecture code, memory management, virtualisation and tracing in the penultimate part of its "Coming in 2.6.32" series. The previous four parts of the series discussed the advancements in the [network subsystem](../site/news/item/Kernel-Log-Coming-in-2-6-32-Part-1-Network-subsystem-and-network-drivers-832229.html "Kernel Log: Coming in 2.6.32 (Part 1) – Network subsystem and network drivers – 19 October 2009, 13:50") as well as those in the fields of [graphics hardware](../site/news/item/Kernel-Log-Coming-in-2-6-32-Part-2-Graphics-858783.html "Kernel Log: Coming in 2.6.32 (Part 2) - Graphics – 12 November 2009, 18:00"), [storage hardware, filesystems](../site/news/item/Kernel-Log-Coming-in-2-6-32-Part-3-Storage-864376.html "Kernel Log: Coming in 2.6.32 (Part 3) - Storage – 20 November 2009, 17:40") and [further drivers](../site/news/item/Kernel-Log-Coming-in-2-6-32-Part-4-Drivers-868263.html "Kernel Log: Coming in 2.6.32 (Part 4) - Drivers – 25 November 2009, 14:03").

### X86 systems

A [new addition to the kernel](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3162534069597e34dd0ac9eb711be8dc23835ae7) is the support of Intel's [Trusted Execution Technology](http://www.intel.com/technology/security/) (TXT), formerly known as LaGrande Technology. Together with the components of the [Trusted Boot](http://tboot.sourceforge.net/) (tboot) project, TXT systems can ensure that a kernel hasn't been attacked and compromised before executing it. Details about this technology can be found in the [kernel documentation](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob_plain;f=Documentation/intel_txt.txt;hb=HEAD) and in an [article on LWN.net](http://lwn.net/Articles/326747/).

The Linux kernel can now be [optimised](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=366d19e181be873c70f4aafca3931d77d781ccd7) for Atom CPUs during compilation. The kernel hackers have also [integrated](http://git.kernel.org/linus/6349d9979beba240fe7182872cb547250264b865) code to support Intel's Simple Firmware Interface ([SFI](http://simplefirmware.org/)) – an alternative to ACPI developed by Intel and intended for use with the Moorestown platform Intel plans to introduce next year. Moorestown is heavily geared towards Linux use and is intended for smartphones, Mobile Internet Devices (MIDs) and embedded environments. Details about SFI can be found in [a presentation](../site/open/features/The-nitty-gritty-proceedings-of-the-Linux-Symposium-2009-746605.html "The nitty gritty - proceedings of the Linux Symposium 2009 – 11 August 2009, 16:03") given by the ACPI subsystem's maintainer, Intel employee Len Brown, at the Linux Symposium 2009. Further components to support Moorestown have also been integrated into the kernel – they are based on Thomas Gleixner's [partial overhaul](http://thread.gmane.org/gmane.linux.kernel/891591) of the x86 support that allows an [improved abstraction](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=57844a8f8e29802f37ad9a0f94eb11d6ae358603) of x86 platforms like Moorestown.

### Virtualised

KVM [now supports](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3a624e29c7587b79abab60e279f9d1a62a3d4716) the "unrestricted guest" mode of Intel's next generation of desktop and notebook processors (Westmere), which is scheduled for release under product names such as Core i3 or Core i5 in early 2010. The [main Git-Pull request](http://thread.gmane.org/gmane.comp.emulators.kvm.devel/40164) by KVM developer Avi Kivity discusses further improvements to KVM – including [improved tracing facilities](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=229456fc34b1c9031b04f7581e7b755d1cebfe9c) and the eventfd-based [irqfd](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=721eecbf4fe995ca94a9edec0c9843b1cc0eaaf3) and [ioeventfd](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d34e6b175e61821026893ec5298cc8e7558df43a) mechanisms for integrating user software and kernel software with guest systems.

That paravirtualisation is losing importance is indicated by a [change introduced](http://git.kernel.org/linus/d0153ca35d344d9b640dc305031b0703ba3f30f0) by VMWare developers which announces that the Virtual Machine Interface ([VMI](http://www.vmware.com/technical-resources/interfaces/paravirtualization.html)) will no longer be supported from Linux 2.6.37. VMWare used to advocate the VMI. The developers say the reason for this [extensively discussed step](http://thread.gmane.org/gmane.linux.kernel/891237/) is that the virtualisation techniques offered by modern CPUs have become so sophisticated that VMI-based paravirtualisation often adds no significant further performance improvements.

### Memory management

[Another new addition](http://git.kernel.org/linus/31dbd01f314364b70c2e026a5793a29a4da8a9dc) is [KSM](http://www.linux-kvm.com/content/using-ksm-kernel-samepage-merging-kvm), which originates from the KVM developer circle. The acronym is short for "Kernel Shared Memory" or "Kernel SamePage Merging" and describes a framework which scans the memory of multiple userland processes for identical areas; if it finds matching areas, it combines them and reduces the memory load by deallocating the redundant copies. This is, for instance, interesting for KVM virtualisations where multiple similar guest operating systems that share the same software libraries and programs run on a computer, causing large areas of the data stored in the guests' memory to be identical.

An [article about the Linux Symposiums 2009 in The H Open](../site/open/features/The-nitty-gritty-proceedings-of-the-Linux-Symposium-2009-746605.html "The nitty gritty - proceedings of the Linux Symposium 2009 – 11 August 2009, 16:03") and the text version of an OLS 2009 presentation it links to, describe the technology in detail and explain how KSM ensures that there is no chaos when a process modifies a shared memory segment. The PDF document also mentions how CERN used KSM for reducing its hardware requirements when processing the data generated by the LHC (Large Hadron Collider).

The new HWPOISON, which was [introduced](http://thread.gmane.org/gmane.linux.kernel/890301) by Intel developer Andi Kleen, adds some techniques for handling and avoiding memory errors. These techniques are planned to be included in Intel's Nehalem EX series of server processors, which is expected in early 2010. Details can be found in the [commit comment](http://git.kernel.org/linus/6a46079cf57a7f7758e8b926980a4f852f89b34d), the [kernel documentation](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob_plain;f=Documentation/vm/hwpoison.txt;hb=HEAD), and in an [article on LWN.net](http://lwn.net/Articles/348886/).

### Tracing

The emerging Performance Counters have been [renamed](http://git.kernel.org/linus/cdd6c482c9ff9c55475ee7392ec8f672eddb7be6) Performance Events, because this apparently better describes this technology, which has seen major advancements in the past few months. The extent to which the kernel's performance and runtime analysis infrastructure is transforming is also indicated by the lengthy Git-Pull requests submitted for the Performance Counters/Events ([1](http://thread.gmane.org/gmane.linux.kernel/888421), [2](http://thread.gmane.org/gmane.linux.kernel/891927)), for the [tracing subsystem](http://thread.gmane.org/gmane.linux.kernel/888426) and for [Oprofile](http://thread.gmane.org/gmane.linux.kernel/888418), which briefly mention the most important changes in the respective subsystems. Among them is the ring-buffer, which is now [completely lockless](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=77ae365eca895061c8bf2b2e3ae1d9ea62869739) and utilises the tracing code to a large degree – once again background information about this can be found [on LWN.net](http://lwn.net/Articles/340400/).

Also new is the "[perf sched](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0a02ad9331dd4db56c29c60db2e99c4daaad8a48)" sub-program, which adds convenience to the task of analysing the process scheduler. Another new addition is the [Timechart tool](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=10274989fd595db455874fc2c83272fb33f6b27b) mainly developed by Arjan van de Ven, which allows traces recorded via "perf record" to be visualised as SVGs for easy analysis – [in his blog](http://blog.fenrus.org/?p=5), van de Ven explains the whole procedure in detail and gives various examples of use.

### Minor Gems

Many further minor, but by no means insignificant, changes can be found in the list below. Like many of the references in the text above, the links point to the relevant commits in the [web front end](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git&a=summary) of the Git branch at kernel.org that Linus Torvalds uses for maintaining the kernel sources. There, the commit comments and the patches themselves provide extensive further information on the respective changes.

### Architecture

*ARM*

- [Add i.MX25 support](http://git.kernel.org/linus/8c25c36f33157a2e2a1fcd60b6dc00feace80631)
- [Add support for Eukrea's CPUIMX27](http://git.kernel.org/linus/af5b1df7136570dae9ac4c1cd193053c61b0ed8f)
- [Add support for Eukrea's MBIMX27](http://git.kernel.org/linus/a961bf380b93741c2191f8efc8f5f1c65224b216)
- [ARM: 5570/1: at91: Support for at91sam9g10: core chip board support](http://git.kernel.org/linus/b319ff80852e823c3a18778c839151784990f80b)
- [ARM: 5572/1: at91: Support for at91sam9g45 series: core chip board support](http://git.kernel.org/linus/789b23bc40a67d9a19bedc2655c6bcab79bcabd8)
- [ARM: 5580/2: ARM TCM (Tightly-Coupled Memory) support v3](http://git.kernel.org/linus/bc581770cfdd8c17ea17d324dc05e2f9c599e7ca)
- [ARM: 5590/1: Add basic support for ST Nomadik 8815 SoC and evaluation board](http://git.kernel.org/linus/28ad94ec61dc60207dbffdb95ff870c617fbb832)
- [ARM: 5629/1: Add support for Eukrea's CPU9260 CPU9G20](http://git.kernel.org/linus/41a353d126ca332c20cfd97683b6261992743840)
- [ARM: 5630/1: Add support for Eukrea's CPUAT91](http://git.kernel.org/linus/10233a939812450e4fe07cf529585bab5b4d99ec)
- [ARM: 5641/1: bcmring: add Kconfig and Makefile entries in arch/arm](http://git.kernel.org/linus/6288e28dce9bae24068b7341ebd72a7d176a3539)
- [ARM: 5667/3: U300 SSP/SPI board setup and test](http://git.kernel.org/linus/c7c8c78fdf6e9bd65d8ee879115dc2cd5d9fd0dc)
- [ARM: BAST: CPUFREQ: Add board support](http://git.kernel.org/linus/ca0b4901d8faaf98cf254e25cd2784bcb21e46d5)
- [ARM: implement highpte](http://git.kernel.org/linus/65cec8e3db606608fd1f8dfc4a1c7c37bfba9173)
- [ARM: Kirkwood: Marvell OpenRD-Base board support](http://git.kernel.org/linus/7eeae54c68e91c46ec170e764d1cceac81f35969)
- [ARM: orion5x: Add LaCie NAS 2Big Network support](http://git.kernel.org/linus/54782674084ed9dc829050a8c18298db6847679d)
- [ARM: OSIRIS: CPUFREQ: Add CPU frequency scaling support](http://git.kernel.org/linus/baf6b281cfa7259ab2d1148b879850f699520bc6)
- [ARM: pxa: balloon3 (http://balloonboard.org/) base machine support](http://git.kernel.org/linus/2a23ec3679d84ac243add761fa3d3872cf6dcb11)
- [ARM: S3C2410: CPUFREQ: Add core support.](http://git.kernel.org/linus/a24c091db988551e2c350cfde9eb80ab6e791ffb)
- [ARM: S3C2412: CPUFREQ: Add core support.](http://git.kernel.org/linus/22d4239973bbd3738b3cfe6048c55f885f3f6256)
- [ARM: S3C2440: CPUFREQ: Add core support.](http://git.kernel.org/linus/342e20f10294aca4097ae2a056c72a202221a75f)
- [ARM: S3C24XX: CPUFREQ: Add core support.](http://git.kernel.org/linus/2e4ea6e8209e0c1d93c69c34c32002337b3f747e)
- [ARM: S3C6410: airgoo hmt board support](http://git.kernel.org/linus/2896bda4824c1e4d34852e355916e34671e38a11)
- [ARM: S3C: CPUFREQ: Add debugfs support for cpufreq](http://git.kernel.org/linus/e6d197a6954c8a9ff85727c31ca61fc1da78628a)
- [ARM: S3C: CPUFREQ: Add documentation for system](http://git.kernel.org/linus/dfff4e95d749c414af3f7350835139103408a50d)
- [ARM: S5PC100: Board and configuration file](http://git.kernel.org/linus/e119766f4e15274e2cd9bb5f25119c8b008d920b)
- [ARM: S5PC100: Clock and PLL support](http://git.kernel.org/linus/c1cc3db8e9fcf1c9d2db3f34552c73996d3d8a13)
- [ARM: S5PC100: CPU initialization](http://git.kernel.org/linus/8acd1ade2ede18408303c968e1449220c427a182)
- [ARM: S5PC100: Kconfigs and Makefiles](http://git.kernel.org/linus/5a7652f2032b88106c9ba41edf0fb795397008bd)
- [ep93xx video driver platform support](http://git.kernel.org/linus/c6012189a40d33213ead5d15769fab615443206f)
- [Freescale i.MX25 PDK (3ds) board support](http://git.kernel.org/linus/635baf6b40ebaef683abf87d677467cba71a0d50)
- [MAINTAINERS: move ARM lists to infradead](http://git.kernel.org/linus/efc03ecb9d674588a13aee27289c2af2afe5e6b4)
- [mx27: add support for phytec pca100 (phyCARD-s) board](http://git.kernel.org/linus/337316986f0531e1681c409de9b73af0bc6dc7bb)
- [MXC: add basic MXC91231 support](http://git.kernel.org/linus/fd6ac7bb9d671d36fd7536c68fde977d197756ab)
- [MXC: add iomux pins configuration support for MXC91231](http://git.kernel.org/linus/94da274b4982f5b36b55bde0c76d3ef8233bceda)
- [nommu: Add MMU-less support for Integrator platforms](http://git.kernel.org/linus/365f7a43497dfdfdc05ca03896a8e22ee6944179)
- [nommu: Add MMU-less support for the RealView boards](http://git.kernel.org/linus/5d57795e26c413656725c26bd053dbee3711adee)
- [nommu: ptrace support](http://git.kernel.org/linus/68b7f7153fa58df710924fbb79722717d2d16094)
- [OMAP2: add board file for Nokia N800 and N810](http://git.kernel.org/linus/6313881292c238190bc119404ae13f65c61b2daa)
- [OMAP3: Zoom2: Add TWL4030 support](http://git.kernel.org/linus/70ac51ab2cd9ddc7ded24adbe63fc6fd3557e44c)

*Power*

- [mpc5200: support for the MAN mpc5200 based board mucmc52](http://git.kernel.org/linus/830cb6fafc12af6c105aaaf794543e4423ca79c3)
- [PCI: document PCIe fundamental reset interfaces](http://git.kernel.org/linus/fe14acd4e7c8178dfb172c1e7a88356657378128)
- [PCI/powerpc: support PCIe fundamental reset](http://git.kernel.org/linus/6e19314cc98ab9ccc22c30d1c414984ac6de5ce2)
- [powerpc/40x: Add support for the ESTeem 195E (PPC405EP) SBC](http://git.kernel.org/linus/0cdf50a7c65df894fb5fd0ef181fe18b8fec6137)
- [powerpc/44x: Add Eiger AMCC (AppliedMicro) PPC460SX evaluation board support.](http://git.kernel.org/linus/c9f75093a497bdc7389df983e914da17fad20d95)
- [powerpc/83xx: Add support for MPC8377E-WLAN boards](http://git.kernel.org/linus/fda4bd9bac78efd2f9d566c52956d297bc03e8d9)
- [powerpc/85xx: Add support for P2020RDB board](http://git.kernel.org/linus/fb8e3e1fe1df963b6c1ab8610682737ccae96ef0)
- [powerpc: Enable GCOV](http://git.kernel.org/linus/a15098c90df1ac2b1bfe1d33dd1c47063213aa9a)
- [powerpc: Fix some late PowerMac G5 with PCIe ATI graphics](http://git.kernel.org/linus/cede3930f0ca6fef353fa01306c72a01420bd45e)
- [powerpc: introduce and document sdhci,wp-inverted property for eSDHC](http://git.kernel.org/linus/50dfe70fe9e216cf356830194630f9a39e498d76)
- [powerpc/powermac: Thermal control turns system off too eagerly](http://git.kernel.org/linus/b8e4a7dae53760b9791aca96e74366078692d90f)
- [powerpc: Remaining 64-bit Book3E support](http://git.kernel.org/linus/2d27cfd3286966c04d4192a9db5a6c7ea60eebf1)

*x86*

- [ACPI, x86: expose some IO-APIC routines when CONFIG_ACPI=n](http://git.kernel.org/linus/2a4ab640d3c28c2952967e5f63ea495555bf2a5f)
- [intel_txt: Force IOMMU on for Intel TXT launch](http://git.kernel.org/linus/a59b50e995465911ba580df0bd10cf64aa81fc43)
- [Revert "x86, timers: Check for pending timers after (device) interrupts"](http://git.kernel.org/linus/e7ab0f7b50bc4688fb5cf65de5d42e3b882fb8d1)
- [x86: Add early platform detection](http://git.kernel.org/linus/47a3d5da70f411bc044ecd3c0593b158b09d0efa)
- [x86: Add hardware_subarch ID for Moorestown](http://git.kernel.org/linus/162bc7ab01a00eba1c5d614e64a51e1268ee3f96)
- [x86: Add Moorestown early detection](http://git.kernel.org/linus/3f4110a48a749a1aa1c54fb807afb3f32f49711c)
- [x86: Add Phoenix/MSC BIOSes to lowmem corruption list](http://git.kernel.org/linus/f1b291d4c47440cbfc1a478e88800e2742d60a80)
- [x86: Add reboot quirk for 3 series Mac mini](http://git.kernel.org/linus/05154752cf3767c544b65b5e340793d40b3f1229)
- [x86/amd-iommu: replace "AMD IOMMU" by "AMD-Vi"](http://git.kernel.org/linus/4c6f40d4e0f0bba77a5f27eec4e1c6d1c457d324)
- [x86/amd-iommu: Workaround for erratum 63](http://git.kernel.org/linus/c5cca146aa03e1f60fb179df65f0dbaf17bc64ed)
- [x86, EDAC: Provide function to return NodeId of a CPU](http://git.kernel.org/linus/6a8126911a5ab167783fce18ae9cc70ec9b84fe2)
- [x86, intel_txt: Intel TXT reboot/halt shutdown support](http://git.kernel.org/linus/840c2baf2d4cdf35ecc3b7fcbba7740f97de30a4)
- [x86, intel_txt: Intel TXT Sx shutdown support](http://git.kernel.org/linus/86886e55b273f565935491816c7c96b82469d4f8)
- [x86, mce: fix reporting of Thermal Monitoring mechanism enabled](http://git.kernel.org/linus/f3a0867b12e0cf1512c0bd0665f2339fc75ed2a8)
- [x86, mce: Support specifying context for software mce injection](http://git.kernel.org/linus/5b7e88edc6193f36941bccbfd5ed9ed5fe27d2e1)
- [x86, mce: Support specifying raise mode for software MCE injection](http://git.kernel.org/linus/0dcc66851f1091af421416c28a9458836885f522)
- [x86: mce: Update X86_MCE description in x86/Kconfig](http://git.kernel.org/linus/bab9bc6583fe6c1660d6ed36dd14bbb4edfaf393)
- [x86, msr: Export the register-setting MSR functions via /dev/\*/msr](http://git.kernel.org/linus/ff55df53dfdd338906c8ba9d1f4a759b86b869d5)
- [x86/oprofile: Enable multiplexing only if the model supports it](http://git.kernel.org/linus/5280514471c2803776701c43c027038decac1103)
- [x86, pat/mtrr: Rendezvous all the cpus for MTRR/PAT init](http://git.kernel.org/linus/d0af9eed5aa91b6b7b5049cae69e5ea956fd85c3)
- [x86, perf_counter, bts: Add BTS support to perfcounters](http://git.kernel.org/linus/30dd568c912602b7dbd609a45d053e01b13422bb)
- [x86: Remove STACKPROTECTOR_ALL](http://git.kernel.org/linus/14a3f40aafacde1dfd6912327ae14df4baf10304)
- [x86, timers: Check for pending timers after (device) interrupts](http://git.kernel.org/linus/9bcbdd9c58617f1301dd4f17c738bb9bc73aca70)
- [x86,percpu: use embedding for 64bit NUMA and page for 32bit NUMA](http://git.kernel.org/linus/4518e6a0c038b98be4c480e6f4481e8676bd15dd)
- [x86: Provide an alternative() based cmpxchg64()](http://git.kernel.org/linus/79e1dd05d1a22e95ab6d54d21836f478b3b56976)

*Others*

- [core generic GPIO support for Freescale Coldfire processors.](http://git.kernel.org/linus/af39bb8b07af83b579c90c09ba3943123cdb4132)
- [davinci: Adding DM365 SOC Support](http://git.kernel.org/linus/fb8fcb891390639d6258c816abb537663495da0c)
- [davinci: Add support for DA850/OMAP-L138 EVM board](http://git.kernel.org/linus/0fbc5592158db4e1ca2037178e1ea6733ccc6f61)
- [davinci: da8xx: Add base DA830/OMAP-L137 SoC support](http://git.kernel.org/linus/55c79a40e34566e9d198f6205b0cf06e3d89ac0a)
- [davinci: da8xx: Add support for DA830/OMAP-L137 EVM board](http://git.kernel.org/linus/8593790d604c29a717d5914159ce78c7bb9899fb)
- [IA64: implement ticket locks for Itanium](http://git.kernel.org/linus/2c86963b093c1a0887dfc6b32c6e5ea3a80f2922)
- [m32r: bzip2/lzma kernel compression support](http://git.kernel.org/linus/337214e8c6b0c777713b2483749f9c03102a416c)
- [MAINTAINERS: add entry for TI DaVinci machine support](http://git.kernel.org/linus/4c5adde7943b982d22a7bf711654fbb5cb810667)
- [microblaze: Add architectural support for USB EHCI host controllers](http://git.kernel.org/linus/afc26cb39e1e74c87a1b5eb013ead2590b91489c)
- [microblaze: Add checking mechanism for MSR instruction](http://git.kernel.org/linus/2622434ee0108c65808a63f067e72d0bbc75b372)
- [MIPS: BCM63xx: Add integrated ethernet mac support.](http://git.kernel.org/linus/9b1fc55a05006523bced65f4d99f7072831ff56a)
- [MIPS: BCM63xx: Add PCMCIA Cardbus support.](http://git.kernel.org/linus/553d6d5f5b84f11fad8043688137dac96df1a06d)
- [MIPS: BCM63xx: Add serial driver for bcm63xx integrated UART.](http://git.kernel.org/linus/9fcd66e572b94974365a9119b073e0a43d496eb7)
- [MIPS: BCM63xx: Add support for the Broadcom BCM63xx family of SOCs.](http://git.kernel.org/linus/e7300d04bd0809eb7ea10a2ed8c729459f816e36)
- [MIPS: Loongson: Add GCC 4.4 support for Loongson2E](http://git.kernel.org/linus/3702bba5eb4f7a0c89107089af6fd9bc2966b65a)
- [MIPS: Loongson: Add oprofile support](http://git.kernel.org/linus/67b35e5d01aba7a83f2161b0c90acb08afa01e3e)
- [OMAP2/3/4 core: create omap_device layer](http://git.kernel.org/linus/b04b65ab5b4fc86af073424af6295be4e067adf3)
- [OMAP2/3/4: create omap_hwmod layer](http://git.kernel.org/linus/63c852384125ca0eff0e695f92cbbd439bed4aa3)
- [OMAP: PM counter infrastructure.](http://git.kernel.org/linus/ba20bb126940ce4847e146a0d00b7f7b0868d773)
- [S390: 64-bit register support for 31-bit processes](http://git.kernel.org/linus/ea2a4d3a3a929ef494952bba57a0ef1a8a877881)
- [S390: add call home support](http://git.kernel.org/linus/c114728af2acdca0bd8b1d2f5792e393c775f5fc)
- [S390: Enable guest page hinting by default.](http://git.kernel.org/linus/2ddddf3e0a55a7fcd6f240a7416cfcb12dd38b7e)
- [score: add maintainers for score architecture](http://git.kernel.org/linus/6bcf67374137f433e85aa42a18fde9f0e8562901)
- [score: Add support for Sunplus S+core architecture](http://git.kernel.org/linus/6bc9a3966f0395419b09b2ec90f89f7f00341b37)
- [sh: Add CEU support for EcoVec24](http://git.kernel.org/linus/2153ad3294e3e1e89d27a78d65932352b80a4f78)
- [sh: Add EcoVec (SH7724) board support](http://git.kernel.org/linus/4138b74066cc33ede31bfd6cb2b7a5e685cfd327)
- [sh: add FSI driver support for ms7724se](http://git.kernel.org/linus/3e9ad52b95e259e68c7dcb69a25d58047ed51094)
- [sh: Add ftrace syscall tracing support](http://git.kernel.org/linus/c652d780c9cf7f860141de232b37160fe013feca)
- [sh: Add initial support for SH7757 CPU subtype](http://git.kernel.org/linus/c01f0f1a4a96eb3acc5850e18cc43f24366966d0)
- [sh: Add support DMA Engine to SH7722](http://git.kernel.org/linus/8255fff45b2a9b53f8bf39147157ddaf9c72a585)
- [sh: Add support DMA Engine to SH7780](http://git.kernel.org/linus/ecb6fd529942c143c8837dfb11262009c77e9c77)
- [sh: bzip2/lzma zImage support.](http://git.kernel.org/linus/07e88e1bfc128681a80578724fde6a872f413862)
- [sh: Function graph tracer support](http://git.kernel.org/linus/327933f5d6cdf083284d3c06e0370d1de464aef4)
- [sh: kfr2r09 board support - mach-type and defconfig](http://git.kernel.org/linus/5bdef865eb358b6f3760e25e591ae115e9eeddef)
- [sparc: add basic support for 'perf'](http://git.kernel.org/linus/825c9fb47a0837db12fecf8d360e0e1d284ddb49)
- [sparc: Add CONFIG_DMA_API_DEBUG support](http://git.kernel.org/linus/451d7400a34cb679369e337d67f0238ed410f484)
- [sparc,leon: CONFIG_SPARC_LEON option and leon specific files.](http://git.kernel.org/linus/5213a780295895630530aebacdd19217a5379c9a)
- [sparc,leon: Introduce the sparc-leon CPU type.](http://git.kernel.org/linus/0fd7ef1fe0e6e70c7851ce65a2eb8a8d3f49147e)
- [sparc: Niagara1 perf event support.](http://git.kernel.org/linus/7eebda60d57a0862a410f45122c73b8bbe6e260c)
- [sparc: Support all ultra3 and ultra4 derivatives.](http://git.kernel.org/linus/28e8f9bead060aafc630a4256d23e2a55fb8b97d)

### Memory Management (MM)

- [cgroups: update documentation of cgroups tasks and procs files](http://git.kernel.org/linus/7823da36ce8e42d66941887eb922768d259763f2)
- [Documentation/memory.txt: remove some very outdated recommendations](http://git.kernel.org/linus/3b2b9a875ddcbf9fcd667db9f961a6a163bd083f)
- [hugetlb: add MAP_HUGETLB example](http://git.kernel.org/linus/94bf5ceac095c7d4cb5e4d40fa7e2dd81d722b75)
- [hugetlb: clean up and update huge pages documentation](http://git.kernel.org/linus/41a25e7e67b8be33d7598ff7968b9a8b405b6567)
- [HWPOISON: Add basic support for poisoned pages in fault handler v3](http://git.kernel.org/linus/d1737fdbec7f90edc52dd0c5c3767457f28e78d8)
- [HWPOISON: Add new SIGBUS error codes for hardware poison signals](http://git.kernel.org/linus/ad5fa913991e9e0f122b021e882b0d50051fbdbc)
- [HWPOISON: Add page flag for poisoned pages](http://git.kernel.org/linus/d466f2fcb32cd97fd586bfa33f5dba3ac78aadb0)
- [HWPOISON: Add poison check to page fault handling](http://git.kernel.org/linus/a3b947eacfe783df4ca0fe53ef8a764eebc2d0d6)
- [HWPOISON: Add support for poison swap entries v2](http://git.kernel.org/linus/a7420aa54dbf699a5a05feba3c859b6baaa3938c)
- [HWPOISON: x86: Add VM_FAULT_HWPOISON handling to x86 page fault handler v2](http://git.kernel.org/linus/a6e04aa92965565968573a220a35b4e907385697)
- [kmemcheck: update documentation](http://git.kernel.org/linus/e3c6c4a8af9e3c4588235444774e66b6483b10ad)
- [ksm: add mmu_notifier set_pte_at_notify()](http://git.kernel.org/linus/828502d30073036a486d96b1fe051e0f08b6df83)
- [ksm: add some documentation](http://git.kernel.org/linus/7701c9c0f54feb682d0cefa2ae1f4a1e00e0ba09)
- [ksm: change default values to better fit into mainline kernel](http://git.kernel.org/linus/2c6854fdadf940678fd54779b778f6faafb870bb)
- [ksm: more on default values](http://git.kernel.org/linus/c73602ad31cdcf7e6651f43d12f65b5b9b825b6f)
- [ksm: sysfs and defaults](http://git.kernel.org/linus/2ffd8679c8e4ec226718bff58b50b226dd477015)
- [ksm: the mm interface to ksm](http://git.kernel.org/linus/f8af4da3b4c14e7267c4ffb952079af3912c51c5)
- [mm: allow memory hotplug and hibernation in the same kernel](http://git.kernel.org/linus/6ad696d2cf535772dff659298ec7e7260e344595)
- [mm: fix NUMA accounting in numastat.txt](http://git.kernel.org/linus/5d3bc2709114b416cab588c577e02c2470e40a6c)
- [mm: fix sparsemem configuration](http://git.kernel.org/linus/1a83e175dc2c7be931a3ea9c7fb0769e6de55e90)
- [mm: oom analysis: add buffer cache information to show_free_areas()](http://git.kernel.org/linus/71de1ccbe1fb40203edd3beb473f8580d917d2ca)
- [mm: oom analysis: add per-zone statistics to show_free_areas()](http://git.kernel.org/linus/4a0aa73f1d613bf19bc8610bf090c941ef49d720)
- [mm: oom analysis: add shmem vmstat](http://git.kernel.org/linus/4b02108ac1b3354a22b0d83c684797692efdc395)
- [mm: vmstat: add isolate pages](http://git.kernel.org/linus/a731286de62294b63d8ceb3c5914ac52cc17e690)
- [nommu: add support for Memory Protection Units (MPU)](http://git.kernel.org/linus/eb8cdec4a984fde123a91250dcc9e0bddf5eafdc)
- [oom: make oom_score to per-process value](http://git.kernel.org/linus/495789a51a91cb8c015d8d77fecbac1caf20b186)
- [pagemap clear_refs: modify to specify anon or mapped vma clearing](http://git.kernel.org/linus/398499d5f3613c47f2143b8c54a04efb5d7a6da9)
- [pagemap: document KPF_KSM and show it in page-types](http://git.kernel.org/linus/a1bbb5ec39042fb762e7f4bcc634da0d87834193)
- [pagemap: export KPF_HWPOISON](http://git.kernel.org/linus/253fb02d62571e5455eedc9e39b9d660e86a40f0)
- [page-types: add feature for walking process address space](http://git.kernel.org/linus/0b4b2ad5307c76c7105d6e7c724b1c14b8daf482)
- [page-types: add hwpoison/unpoison feature](http://git.kernel.org/linus/a54fed9f70a2765f4476e1ce3d691a2f31df258f)
- [page-types: introduce checked_open()](http://git.kernel.org/linus/31bbf66eaaaf50ba79e50ab7d3c89531b31c0614)
- [page-types: introduce kpageflags_flags()](http://git.kernel.org/linus/48640d69f5f06fe951a4de065a7f374cb9ee6040)
- [page-types: make standalone pagemap/kpageflags read routines](http://git.kernel.org/linus/4a1b6726feee3132905996ae4cd1c7dc2104e721)
- [page-types: make voffset local variables](http://git.kernel.org/linus/e577ebde9fb161bdc87511763c75dfad291059e2)
- [proc: document \`guest' column in /proc/stat](http://git.kernel.org/linus/c574358e8b48adf646f9d5ef70dc76c5d4ad9387)
- [slub: add option to disable higher order debugging slabs](http://git.kernel.org/linus/fa5ec8a1f66f3c2a3af723abcf8085509c9ee682)
- [tracing, documentation: Add a document on the kmem tracepoints](http://git.kernel.org/linus/8fbb398f5c78832ee61e0d5ed0793fa8857bd853)
- [truncate: new helpers](http://git.kernel.org/linus/25d9e2d15286281ec834b829a4aaf8969011f1cd)
- [truncate: use new helpers](http://git.kernel.org/linus/c08d3b0e33edce28e9cfa7b64f7fe5bdeeb29248)
- [vm: document that setting vfs_cache_pressure to 0 isn't a good idea](http://git.kernel.org/linus/55c37a840d9ec0ebed5c944355156d490b1ad5d1)

### Tracing

- [Add a tracepoint for block request remapping](http://git.kernel.org/linus/b0da3f0dada78832c9da03ad2152ae76bd9a2496)
- [drm/i915: Add tracepoints](http://git.kernel.org/linus/1c5d22f76dc721f3acb7a3dadc657a2%3D)
- [ext4: Add a tracepoint for ext4_alloc_da_blocks()](http://git.kernel.org/linus/fb40ba0d98968bc3454731360363d725b4f1064c)
- [ftrace: document function and function graph implementation](http://git.kernel.org/linus/555f386c98cc93890f48fdea098936755270304b)
- [hrtimer: Add tracepoint for hrtimers](http://git.kernel.org/linus/c6a2a1770245f654f35f60e1458d4356680f9519)
- [itimers: Add tracepoints for itimer](http://git.kernel.org/linus/3f0a525ebf4b8ef041a332bbe4a73aee94bb064b)
- [oprofile: Implement performance counter multiplexing](http://git.kernel.org/linus/4d4036e0e7299c6cbb2d2421b4b30b7a409ce61a)
- [perf: Add a SVG helper library file](http://git.kernel.org/linus/f48d55ce7871824eae3065f4d81956d7113eff19)
- [perf: Add a timestamp to fork events](http://git.kernel.org/linus/393b2ad8c757ba3ccd2a99ca5bbcd6db4d3fa53d)
- [perf: Add timechart help text and add timechart to "perf help"](http://git.kernel.org/linus/151750cec5db3c7ea45255d2901e581e2162317a)
- [perf_counter: powerpc: Add callchain support](http://git.kernel.org/linus/20002ded4d937ca87aca6253b874920a96a763c4)
- [perf_counter, sched: Add sched_stat_runtime tracepoint](http://git.kernel.org/linus/f977bb4937857994312fff4f9c2cad336a36a932)
- [perf report: Add raw displaying of per-thread counters](http://git.kernel.org/linus/9f8666971185b86615a074bcac67c90fdf8af8bc)
- [perf report: Fix and improve the displaying of per-thread event counters](http://git.kernel.org/linus/8d51327090ac025d7f4ce6c059786b5e93513321)
- [perf sched: Account for lost events, increase default buffering](http://git.kernel.org/linus/dc02bf7178c8e2cb3d442ae19027b736d51c7dd5)
- [perf sched: Add --input=file option to builtin-sched.c](http://git.kernel.org/linus/4b77a7297795229eca96c41e1709a3c87909fabe)
- [perf sched: Add involuntarily sleeping task in work atoms](http://git.kernel.org/linus/c6ced61112f1e6139914149fab65695801a74f0f)
- [perf sched: Add 'perf sched latency' and 'perf sched replay'](http://git.kernel.org/linus/f2858d8ad9858e63c87257553c5721cba5db95ae)
- [perf sched: Add 'perf sched map' scheduling event map printout](http://git.kernel.org/linus/0ec04e16d08b69d8da46abbcfa3e3f2cd9738852)
- [perf sched: Add 'perf sched trace', improve documentation](http://git.kernel.org/linus/c13f0d3c8165e9592102687fa999da0a0d9c3724)
- [perf sched: Add runtime stats](http://git.kernel.org/linus/ea92ed5a8f4e6c638efe7de2efe8a875d580ad3f)
- [perf sched: Add sched latency profiling](http://git.kernel.org/linus/cdce9d738b91e1ec686e4ef6ca46d46e2891e208)
- [perf sched: Add support for sched:sched_stat_runtime events](http://git.kernel.org/linus/39aeb52f99f2380c1f16036deed2f7bb8b2e0559)
- [perf sched: Display time in milliseconds, reorganize output](http://git.kernel.org/linus/d9340c1db3f52460a8335eeb127a2728c5bba6ce)
- [perf sched: Implement the 'perf sched record' subcommand](http://git.kernel.org/linus/1fc35b29b4098aa3bf9fc9acb4c1615d0b5dd95d)
- [perf sched: Implement the scheduling workload replay engine](http://git.kernel.org/linus/fbf9482911825f965829567aea8acff3bbc5279c)
- [perf sched: Import schedbench.c](http://git.kernel.org/linus/ec156764d424dd67283c2cd5e9f6f1b8388364ac)
- [perf sched: Make it easier to plug in new sub profilers](http://git.kernel.org/linus/419ab0d6a959f41ec7fde807fe311aaafb05c3be)
- [perf sched: Output runtime and context switch totals](http://git.kernel.org/linus/3e304147cdb404ce6d1dd0e50cb19f52142bb363)
- [perf sched: Print PIDs too](http://git.kernel.org/linus/08f69e6c2e59b3d73343f8c9ecf758e0133dbc22)
- [perf: Tidy up after the big rename](http://git.kernel.org/linus/57c0c15b5244320065374ad2c54f4fb%3D)
- [perf timechart: Add a power-only mode](http://git.kernel.org/linus/39a90a8ef17fe6fbf4b45e46e3c10d3b8b4a3dea)
- [perf timechart: Add "perf timechart record"](http://git.kernel.org/linus/3c09eebd61eaacca866cd60b50416f18640bc731)
- [perf timechart: Show the duration of scheduler delays in the SVG](http://git.kernel.org/linus/a92fe7b3063db2caa578872fce975ff53aa56214)
- [perf timechart: Show the name of the waker/wakee in timechart](http://git.kernel.org/linus/4f1202c8e61478984ed2d0df616149faf84c2a7f)
- [perf tools: Add an option to multiplex counters in a single channel](http://git.kernel.org/linus/d13025222cdb0043e2239b3b819389358bb31bc0)
- [perf tools: Add missing parameters documentation](http://git.kernel.org/linus/ec7ba4ea1d605029fb09601ab4ad3053bc1f519c)
- [perf tools: Add perf trace](http://git.kernel.org/linus/5f9c39dca52d3e639ac899e169f408c6fd8396cc)
- [perf tools: Add trace event debugfs IO handler](http://git.kernel.org/linus/520509436417901f30106e021e037c75dfe5386c)
- [perf tools: Add trace event information parser](http://git.kernel.org/linus/ea4010d1363699770a9894493bafe556a59a144c)
- [perf tools: Allow the specification of all tracepoints at once](http://git.kernel.org/linus/bcd3279f465cdcc1e0454b5f605f021c4ff4dbb5)
- [perf tools: Complete support for dynamic strings](http://git.kernel.org/linus/561f732c1233f6bf7c3c5c5fb9b4d90bb6c107aa)
- [perf tools: Factorize the thread code in a dedicated file](http://git.kernel.org/linus/6baa0a5ae0954fb2486c480a20556a9f1aee0965)
- [perf tools: Implement counter output multiplexing](http://git.kernel.org/linus/ea57c4f5203d82c7844c54cdef54e972cf4e9d1f)
- [perf util: Make the timechart SVG width dynamic](http://git.kernel.org/linus/5094b655452dd48367fb28af74ffc76019b93dc2)
- [perf util: SVG performance improvements](http://git.kernel.org/linus/611a546bec3e1af2a87af0862398fc711dc47aef)
- [powerpc/sputrace: Use the generic event tracer](http://git.kernel.org/linus/ae142e0c52b38e44d28b12f77c6e7faa96f7a069)
- [ring-buffer: add design document](http://git.kernel.org/linus/8b2c70d1e43074cc06afe99b0de12b686d9c9d02)
- [ring-buffer: make lockless](http://git.kernel.org/linus/77ae365eca895061c8bf2b2e3ae1d9ea62869739)
- [sched: Add wait, sleep and iowait accounting tracepoints](http://git.kernel.org/linus/768d0c27226e6587cad2fcf543f9711da3f3774e)
- [sched: Provide iowait counters](http://git.kernel.org/linus/8f0dfc34e9b323a028c2ec41abb7e9de477b7a94)
- [timers: Add tracepoints for timer_list timers](http://git.kernel.org/linus/2b022e3d4bf9885f781221c59d86283a2cdfc2ed)
- [tracing: Add individual syscalls tracepoint id support](http://git.kernel.org/linus/64c12e0444fcc6b75eb49144ba46d43dbdc6bc8f)
- [tracing: add latency format to function_graph tracer](http://git.kernel.org/linus/49ff590390a22c49e9063dcdec4cd5903127526b)
- [tracing: add lock depth to entries](http://git.kernel.org/linus/637e7e864103a7a68c1ce43ada27dfc25c0d113f)
- [tracing: Add more namespace area to 'perf list' output](http://git.kernel.org/linus/48c2e17f1f668fe6691bad965beb2b0b25239c5f)
- [tracing: Add perf counter support for syscalls tracing](http://git.kernel.org/linus/f4b5ffccc83c82947f5d9f15d6f1b6edb1b71cd7)
- [tracing: Add syscall tracepoints](http://git.kernel.org/linus/a871bd33a6c0bc86fb47cd02ea2650dd43d3d95f)
- [tracing: Add trace events for each syscall entry/exit](http://git.kernel.org/linus/fb34a08c3469b2be9eae626ccb96476b4687b810)
- [tracing: Add vim script to enable folding for function_graph traces](http://git.kernel.org/linus/6591b493871cf9b17de2ba272edb8ab529a8058b)
- [tracing: create generic trace parser](http://git.kernel.org/linus/b63f39ea50330f836e301ddda21c6a93dcf0d6a3)
- [tracing, documentation: add a document describing how to do some performance analysis with tracepoints](http://git.kernel.org/linus/bb72222086260695d71afe60fa105649c1ea9463)
- [tracing/events: Add module tracepoints](http://git.kernel.org/linus/7ead8b8313d92b3a69a1a61b0dcbc4cd66c960dc)
- [tracing/events: Add trace_event boot option](http://git.kernel.org/linus/020e5f85cb087a40572c8b8b2dd06292a14fa212)
- [tracing/filters: add filter Documentation](http://git.kernel.org/linus/95b696088c1cf152c3bb62560bbe3a441922d68b)
- [tracing/filters: improve subsystem filter](http://git.kernel.org/linus/1f9963cbb0280e0cd554161e00f1a0eeddbf1ae1)
- [tracing: make testing syscall events a separate configuration](http://git.kernel.org/linus/1f5a6b45416694ff8c0d04625f1a438a0e380add)
- [tracing, page-allocator: add a postprocessing script for page-allocator-related ftrace events](http://git.kernel.org/linus/c9d05cfc001fef3d6d37651e19ab9227a32b71f5)
- [tracing: pass around ring buffer instead of tracer](http://git.kernel.org/linus/e77405ad80f53966524b5c31244e13fbbbecbd84)
- [tracing, perf: Convert the power tracer into an event tracer](http://git.kernel.org/linus/6161352142d5fed4cd753b32e5ccde66e705b14e)
- [tracing: Remove markers](http://git.kernel.org/linus/fc5377668c3d808e1d53c4aee152c836f55c3490)
- [tracing: Remove mentioning of legacy latency_trace file from documentation](http://git.kernel.org/linus/4a88d44ab17da5f8a238050d1b43dfd2e204bc2f)
- [tracing: Rename FTRACE_SYSCALLS for tracepoints](http://git.kernel.org/linus/667000011927b4fcc359beac4a2447889db6d349)
- [tracing: Support for syscall events raw records in perfcounters](http://git.kernel.org/linus/19007a67a64f9b3cbbd7024f972654ebf14daade)
- [tracing/syscalls: Add fields format for exit events](http://git.kernel.org/linus/10a5b66f625904ad5a2867cf7a28073e1236ff32)
- [tracing/syscalls: Add filtering support](http://git.kernel.org/linus/540b7b8d65575c80162f2a0f38e1d313c92a6042)
- [tracing: trace parser support for function and graph](http://git.kernel.org/linus/689fd8b65d669b96d612ccc37d6fb87bf7ed6907)
- [tracing: trace parser support for set_event](http://git.kernel.org/linus/489663644c35d50a20f58d468a7cbc705e6a29ce)
- [x86, perf_counter, bts: Add BTS support to perfcounters](http://git.kernel.org/linus/30dd568c912602b7dbd609a45d053e01b13422bb)

### Virtualization

- [Documentation: Update KVM list email address](http://git.kernel.org/linus/0aaeb3b1087b21fef434f1bae6e6495c12ee2f55)
- [KVM: Add Directed EOI support to APIC emulation](http://git.kernel.org/linus/fc61b800f9506ca47bf1439342a79847f2353562)
- [KVM: Add MCE support](http://git.kernel.org/linus/890ca9aefa78f7831f8f633cab9e4803636dffe4)
- [KVM: add module parameters documentation](http://git.kernel.org/linus/fef07aae9cd9ed82f94228c311b35360f1f38902)
- [KVM: add support for change_pte mmu notifiers](http://git.kernel.org/linus/3da0dd433dc399a8c0124d0614d82a09b6a49bce)
- [KVM: Add trace points in irqchip code](http://git.kernel.org/linus/1000ff8d893765d7b56e32fe16dbe4814f172588)
- [KVM: Cache pdptrs](http://git.kernel.org/linus/6de4f3ada40b336522250a7832a0cc4de8856589)
- [KVM: Document basic API](http://git.kernel.org/linus/9c1b96e34717d001873b603d85434aa78e730282)
- [KVM: Document KVM_CAP_IRQCHIP](http://git.kernel.org/linus/5dadbfd64724c41716d4fc82df6f01b023d5b15d)
- [KVM: Implement MSRs used by Hyper-V](http://git.kernel.org/linus/3c5d0a44b011e0a1d857452f05c698e1008b4b4a)
- [KVM: introduce module parameter for ignoring unknown MSRs accesses](http://git.kernel.org/linus/ed85c0685321a139cefd6622b21467643f0159e1)
- [KVM: MMU: enable gbpages by increasing nr of pagesizes](http://git.kernel.org/linus/04326caacff2b162d359c15a2edf634448897d1a)
- [KVM: MMU: shadow support for 1gb pages](http://git.kernel.org/linus/7e4e4056f72da51c5dede48515df0ecd20eaf8ca)
- [KVM: Move common KVM Kconfig items to new file virt/kvm/Kconfig](http://git.kernel.org/linus/0ba12d10817a8db1fd7d96d3283ec6c0b294aeab)
- [KVM: PIT support for HPET legacy mode](http://git.kernel.org/linus/e9f4275732add046fed4a548b8dbb98dbe500d2f)
- [KVM: powerpc: convert marker probes to event trace](http://git.kernel.org/linus/46f43c6ee022c3aeb9686b104234b9f27fac03c2)
- [KVM: report 1GB page support to userspace](http://git.kernel.org/linus/344f414fa0f16254dd07195d4cd11b2f92931d3d)
- [KVM: SVM: enable nested svm by default](http://git.kernel.org/linus/4b6e4dca7011613c8508640c10a091b3ed2cd215)
- [KVM: SVM: Improve nested interrupt injection](http://git.kernel.org/linus/219b65dcf6c0bad83d51bfa12e25891c02de2414)
- [KVM: x86 emulator: Add missing EFLAGS bit definitions](http://git.kernel.org/linus/b1d861431ed58f752b31e8c07da029072989bec7)
- [KVM: x86 emulator: add syscall emulation](http://git.kernel.org/linus/e66bb2ccdcf76d032bbb464b35c292bb3ee58f9b)
- [KVM: x86 emulator: Add sysenter emulation](http://git.kernel.org/linus/8c60435261deaefeb53ce3222d04d7d5bea81296)
- [KVM: x86 emulator: Add sysexit emulation](http://git.kernel.org/linus/4668f050787015805a7e8ea29cc4f81d8f07cedb)
- [virtio: add virtio IDs file](http://git.kernel.org/linus/3ca4f5ca73057a617f9444a91022d7127041970a)
- [xen: make -fstack-protector work under Xen](http://git.kernel.org/linus/577eebeae34d340685d8985dfdb7dfe337c511e8)

For other articles on 2.6.32 and links to the rest of the "Coming in 2.6.32 " series, see [The H's Kernel Log - 2.6.32 Tracking page](../site/open/features/2-6-32-Tracking-816707.html "2.6.32 Tracking – 05 October 2009, 17:04"). ([thl](mailto:thl@ct.heise.de) /c't).

([crve](mailto:crve@h-online.com "Chris von Eitzen "))
