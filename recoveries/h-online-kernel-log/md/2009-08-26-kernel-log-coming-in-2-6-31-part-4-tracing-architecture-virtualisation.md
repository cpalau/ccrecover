---
title: "Kernel Log - Coming in 2.6.31 â Part 4: Tracing, architecture, virtualisation"
date: 2009-08-26
author: "Terry Relph-Knight"
source: http://www.h-online.com/open/news/item/Kernel-Log-Coming-in-2-6-31-Part-4-Tracing-architecture-virtualisation-743099.html
pages: 1
---

# Kernel Log - Coming in 2.6.31 â Part 4: Tracing, architecture, virtualisation

**Terry Relph-Knight**

![Kernel Log Penguin](../site/imgs/43/3/6/9/5/2/9/13d6f7969aa8b06e.jpg)

#### by Thorsten Leemhuis

**New performance counters allow developers to take a detailed look at the runtime behaviour of program code to target specific areas for optimisation. The recently introduced tracing infrastructure has been further modified and improved. Other changes affect the architecture, the memory subsystem, and various virtualisation solutions.**

Last weekend, Linus Torvalds [released](http://thread.gmane.org/gmane.linux.kernel/880798) the seventh release candidate of Linux 2.6.31. In his release email, Torvalds highlights some of the corrections; two days earlier, the list of known new problems contained 29Â unsolved problems.

Unlike [the week before](../site/news/item/Kernel-Log-Coming-in-2-6-31-Part-3-Storage-and-file-systems-742967.html "Kernel Log – Coming in 2.6.31 - Part 3: Storage and file systems â 17 August 2009, 09:48"), Torvalds didn't make a statement about the final release of 2.6.31 â€“ it is likely to take another week or two. The Kernel Log continues its discussion of the major new features of 2.6.31 by looking at the areas of tracing, architecture, memory management and virtualisation.

### Detailed road test

Operating partly in the kernel and partly in the userspace, the "performance counters" code can be used for retrieving the performance data offered by modern processors. This performance data quantifies various CPU processes that have an impact on CPU performance â€“ providing an in-depth analysis and allowing developers to optimise the code segments relevant to processing speed down to the last detail for each CPU.

Occasionally abbreviated to "perf_counter", performance counters should not be confused with [Perfmon](http://perfmon2.sourceforge.net/) ("hardware-based performance monitoring interface for Linux"), which has offered similar functionality for years â€“ the kernel hackers didn't include it in the Linux source code because they were dissatisfied with some of Perfmon's properties. This is probably one of the reasons why Ingo Molnar and several other developers pursued the idea of performance counters, which use a slightly different approach. The chief developer of Perfmon repeatedly criticised some aspects of the performance counter concept when the counters were first introduced in late 2008 and during the months that followed; when the developers began to integrate the required more than 600Â patches into the kernel sources, he added further criticism which was [discussed in greatest detail](http://thread.gmane.org/gmane.linux.kernel/852806). The article "[Duelling performance monitors](http://lwn.net/Articles/310260/)" published on LWN.net in late 2008 provides some details concerning this competitive situation.

Use of the performance counters is described in the more recent article "[Perfcounters added to the mainline](http://lwn.net/Articles/339361/)" on LWN.net. Further background information can also be found in the [documentation](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=tree;f=tools/perf/Documentation;hb=HEAD). The relevant [userspace tools](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=tree;f=tools/perf/util;hb=HEAD) were integrated directly into the kernel sources in a newly established [tools/](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=tree;f=tools;hb=HEAD) subdirectory after a lengthy debate, during which Linus Torvalds expressed his opinion [in no uncertain terms](http://thread.gmane.org/gmane.linux.kernel/849935).

For other articles on 2.6.31 and links to the rest of the "Coming in 2.6.31" series, see The H's [Kernel Log - 2.6.31 Tracking](../site/open/features/Kernel-Log-2-6-31-Tracking-746446.html "Kernel Log - 2.6.31 Tracking â 02 July 2009, 11:21") page.

### A different kind of analysis

Ingo Molnar has introduced not only the performance counters, but also numerous other changes affecting the tracing area he maintains. In his [git-pull request](http://thread.gmane.org/gmane.linux.kernel/849499), he suggests that the main development phase of trace points is likely to be completed in the near future. He also highlights [improved filters](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0a19e53c1514ad8e9c3cbab40c6c3f52c86f403d), [internal restructuring measures](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f42c85e74faa422cf0bc747ed808681145448f88) and performance optimisation. Some of the possibilities offered by the tracing infrastructures of current kernels are explained in Sony developer Tim Bird's presentation "Measuring Function Duration with Ftrace", which we already mentioned in the article "[The nitty gritty â€“ The proceedings of the Linux Symposium 2009 ....](../site/open/features/The-nitty-gritty-proceedings-of-the-Linux-Symposium-2009-746605.html "The nitty gritty - proceedings of the Linux Symposium 2009 â 11 August 2009, 16:03")".

The kernel hackers also [integrated](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2521f2c228ad750701ba4702484e31d876dbc386) a profiling feature that uses the GCC Coverage Testing Tool ([gcov](http://gcc.gnu.org/onlinedocs/gcc/Gcov.html)). Kernel developers and testers can from now on use [Kmemleak](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3c7b4e6b8be4c16f1e6e5c558e33b7ff0db2dfaf) ([documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=04f70336c80c43a15e617b36c2043dfa0ad6ed0f)) to track down memory leaks â€“ however, the tool misinterprets certain situations and constructions, and the results it produces shouldn't be trusted implicitly. Another new tool, [Kmemcheck](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=dfec072ecd35ba6ecad2d51dde325253ac9a2936) ([documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e594c8de3bd4e7732ed3340fb01e18ec94b12df2)), detects the use of non-initialised memory areas.

### In brief

The changes described above are only the most significant of those recently made by kernel hackers in terms of the Linux architecture and infrastructure. Here is a short overview of further changes:

**Architecture code:**

- From [2.6.31](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c898faf91b3ec6b0f6efa35831b3984fa3331db0), Linux will address 2^46 instead of 2^44Â bytes of RAM on x86-64 CPUs â€“ however, this currently affects very few people, as systems offering 16 to 64Â Tbytes of RAM are still rather rare.

<!-- -->

- That hibernation (suspend-to-disk/software suspend/swsups) and power-saving techniques are important not just for notebooks, but also for mainframes, is demonstrated by several of Hans-Joachim Picht's patches to [provide](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=155af2f95f905c830688dd0ca7c7cac4107334fd) hibernation support for IBM's [S390](http://en.wikipedia.org/wiki/System/390) architecture (now SystemÂ z) being incorporated into the main development branch. Additional [changes introduced](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=62b7494209495847269a6ce0504cbefd23d42eb1) by Michael Holzheu further improve the use of several power-saving techniques for S390 systems.

**Memory management:**

- A number of [patches submitted](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d239171e4f6efd58d7e423853056b1b6a74f1446) by Mel Gorman are designed to optimise the page allocator responsible for memory allocation â€“ a few benchmark results can be found in the [commit comment](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d239171e4f6efd58d7e423853056b1b6a74f1446).

**Virtualisation:**

- The [KVM developers](http://thread.gmane.org/gmane.comp.emulators.kvm.devel/34923) have reworked the interrupt code and reportedly improved SMP performance.

<!-- -->

- The Xen code in the kernel now also provides some details of the [/sys/hypervisor](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cff7e81b3dd7c25cd2248cd7a04c5764552d5d55) directory. [A new addition to the kernel](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f7116284c734f3a47180cd9c907944a1837ccb3c) is the evtchn Xen driver for sending and receiving events on "event channels". The integration of Dom0 support, on the other hand, seems to have slipped away into the far future again â€“ there has been no further discussion of the topic on LKML since [the discussions](../site/open/Fine-tuning-What-s-new-in-Linux-2-6-30--/features/113478/6) just before and after the release of Linux 2.6.30.

<!-- -->

- After things went quiet around the [Lguest](http://lguest.ozlabs.org/) "Simple x86 Hypervisor", this time around developers have made [several](http://thread.gmane.org/gmane.linux.kernel.virtualization.lguest/836) further substantial changes; additions include [PAE support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=acdd0b6292b282c4511897ac2691a47befbf1c6a) and [improved](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=659a0e6633567246edcb7bd400c7e2bece9237d9) multi-threading.

### Minor gems

Many additional minor, but by no means insignificant, changes can be found in the list below. Like many of the references in the text above, the links lead to the relevant commits in the [web front end](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=summary) of the main Linux development branch, where the commit comments and the patches themselves provide extensive further information on the respective changes.

**Architecture Support**

...ARM:

- [Add core support for ARMv6/v7 big-endian](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=26584853a44c58f3d6ac7360d697a2ddcd1a3efa)
- [ARM: 5522/1: PalmLD: IDE support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5a9d25150c01bd140ca647b5e7ee75ae18a369a8)
- [ARM: add support for the EET board, based on the i.MX31 pcm037 module](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=574ec547c7771881e18e4e76ca970e323bcdc774)
- [ARM: GTA02/FreeRunner: Add machine definition](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9d76295ac6082449a64fd6fa981d2615a34e243d)
- [ARM: Kirkwood: add Marvell 88F6281 GTW GE board support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=91af7bb2f48e14892c5c961bca1fae5c7886532e)
- [ARM: MINI2440: Add machine support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5102aa4acdbde305646ae60c5eec7042b5016a0e)
- [ARM: MX35: Add PCM043 board support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=54df526819d3bfbc1af3f13aed7a3f9b9fdbdd04)
- [ARM: OMAP3: Add omap3 EVM defconfig](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1bfc3738c414a34a6cb81a2f2fddea8e131afa89)
- [ARM: OMAP3: Add omap3 EVM support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=53c5ec31e775d40e428a577de561211e11b08d74)
- [ARM: OMAP3: Add support for OMAP3 Zoom2 board](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=577145f45487b41b4d47eeaedb9d37e494f80715)
- [ARM: OMAP4: Add defconfig for 4430 SDP](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b04e8975e70d9b2bc27c017f92b356b312692544)
- [ARM: OMAP4: Add support for 4430 SDP](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=46ba0abfe1ac2bd9608d0fc9e914379be695aa5b)
- [ARM: pxa: add basic support for HP iPAQ hx4700 PDAs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d3ca1952e63ffbebab6f2f1c9551df7b3cb731f5)
- [ARM: pxa/em-x270: add ability to control GPS and GPRS power](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a37ed43115b70e832c7e8cc7dabd026d127ad9db)
- [ARM: pxa/hx4700: add Maxim 1587A voltage regulator](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6ea0414fc748ab5b1d83a414c7ee3a60190363aa)
- [ARM: pxa/mioa701: add Maxim 1586 voltage regulator](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9752e14898102063a67b44e6db5b758092e769a4)
- [ARM: pxa/mioa701: add V3 gain configuration for Maxim 1586 voltage regulator](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e567b74caff03c0ed66b3d3e11c0acd17fbcfb9a)
- [ARM: pxa/palm: Add Palm27x aSoC driver to PalmTE2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=37330efd4abb474b3fdfacea68beb37cf67564ed)
- [ARM: pxa: Stargate 2 board support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4036e1dea565207010408f5c6137a9d8d3c0ff5c)
- [ARM: pxa/treo680: initial support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e6c3f4b89bf3698a6994d30de7a16ae395a81dab)
- [ARM: remove arch-imx](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1341d34ffc296f98dc84876f35f3151525dc02a2)
- [ARM: S3C64XX: Add S3C6400 SDHCI setup support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4faf6867638cc21aa43b4ca4ed0bdf14a2d29762)
- [ARM: S3C64XX: Initial support for PM (suspend to RAM)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bd117bd161ea99826494983aef8c8e236ac129bd)
- [Atmark Armadillo 500 board support.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5e9145edcc368295cb353872b4a6026e13f5565e)
- [davinci: add SRAM allocator](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=20e9969b3aa5166d50c8df474967c9d80bf6d481)
- [davinci: DM355: add base SoC and board support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=95a3477fe57e0669dcb531516f2930fe1cf27e6b)
- [davinci: DM644x: add support for SFFSDR board](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f5ce6a67a78357da5e88782b1cf1cc10b36f102c)
- [davinci: DM646x: add base SoC and board support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e38d92fdcd04c79d28679682f63a83487c4c4c05)
- [davinci: INTC: add support for TI cp_intc](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0521444d497ee1f8a31314d2ce3c6b9edab25b51)
- [i.MX31: Add ethernet support to i.MX31 Litekit board.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3211705f76cccd52cd3f3c2744aef798bf705702)
- [imx: re-work of PWM, add i.MX21 support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c010dba89bc0f5585550877b1693d11d24063b6b)
- [IXP4xx: support for Goramo MultiLink router platform.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=11c79740d3c03cb81f84e98cf2e2dbd8d9bb53cd)
- [MAINTAINERS: add entry for Mitac Mio A701 board](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d78ff0a50aac6a1bfe445969dd963e6486e49f56)
- [MAINTAINERS: add entry for Palm Treo680](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=90af5811eb1fd69968f7c99e0cae6a5825dcf229)
- [MX27: Add basic support to MX27PDK](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ec9be0debd822d5bd1d5bfdf297144396d56ac6b)
- [MX35: Add basic support for MX35PDK board](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=aefa1c6e7b76fc428770fede6e8b86587fc2ce09)
- [mxc: Add i.MX27LITE board support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8c032ec337bdf6ca9b083345b265130a55100b69)
- [MXC: mx21ads base support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6b91edde09fadde2657b11b454b88ae89c5b4cae)
- [OMAP2/3: PM: push core PM code from linux-omap](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8bd229492209c0c7d050e2f9a600c12f035d72f7)
- [omap iommu: simple virtual address space management](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=69d3a84a646d6ad6cd693a7a3d5b9af414113d2c)

...Power:

- [83xx: add support for the kmeter1 board.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8159df72d43e237d5bfcff052a8337245b6ac53e)
- [powerpc/4xx: Sequoia: Enable NAND support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7b8d639cfc7967388d1cfe2a81e7e3c872a81a0d)
- [powerpc/85xx: Add dts files for X-ES MPC85xx boards](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=317bf653a6700b0ae34cef5028b287d5205bdaf1)
- [powerpc/85xx: Add eSDHC support for MPC8569E-MDS boards](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=28da456a480c6149fb1cdfa006c3fbff6b7b6bc2)
- [powerpc/85xx: Add MPC8569MDS board support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4b3b42b38af82e4815178d4762986f246adfe0ec)
- [powerpc/85xx: Add P2020DS board support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=01af9507ff36578dad89b1cc88ff37ac18e719cb)
- [powerpc/85xx: Add PCI IDs for MPC8569 family processors](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bfa568d19a3faed3b94978ad48ac15d1b0d7e5bc)
- [powerpc/85xx: Add platform support for X-ES MPC85xx boards](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3038acf9091ff265609af3524ed94cce797d8485)
- [powerpc/85xx: Add STMicro M25P40 serial flash support for MPC8569E-MDS](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bd78c33a096a73f09b1b998a481290e229382a8b)
- [powerpc: Add support for swiotlb on 32-bit](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ec3cf2ece22a8ede7478bf38e2a818986322662b)
- [powerpc: Introduce CONFIG_PPC_BOOK3S](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5b7c3c918c9c26c50d220b2b50359208cb5a1dbe)
- [powerpc: Make the NR_CPUS max 8192](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2d8ae638bb86a3c7e8a7e610ec5ae545327d146a)
- [powerpc/virtex: Add support for Xilinx PCI host bridge](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=64f16502475ddf663169369fffff6da9b10ea9fb)
- [powerpc/virtex: Add Xilinx ML510 reference design support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e52ba9c54176c9757ab6b18bea7b7ed51e2faf16)

...x86:

- [amd-iommu: implement suspend/resume](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=736501ee000757082a4f0832826ae1eda7ea106e)
- [docs, x86: add nox2apic back to kernel-parameters.txt](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2b2fd87a6ef56ba7647a578e81bb8c8efda166b8)
- [x86: Add cpu features MOVBE and POPCNT](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=069ebaa4644521e8e80b6849ace4dee53f93f55e)
- [x86: add extension fields for bootloader type and version](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5031296c57024a78ddad4edfc993367dbf4abb98)
- [x86: Add quirk for Intel DG45ID board to avoid low memory corruption](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6aa542a694dc9ea4344a8a590d2628c33d1b9431)
- [x86: Add quirk to make Apple MacBook5,2 use reboot=pci](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6c6c51e4cc11a5456fb1172008f7c69d955af9f6)
- [x86: Add reboot quirk for every 5 series MacBook/Pro](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3e03bbeac541856aaaf1ce1ab0250b6a490e4099)
- [x86: default CONFIG_PHYSICAL_START and CONFIG_PHYSICAL_ALIGN to 16 MB](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ceefccc93932b920a8ec6f35f596db05202a12fe)
- [x86/docs: add description for cache_disable sysfs interface](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2fad2d9bb8310889f3261035b594b4e068b6eb8b)
- [x86: document new bzImage fields](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d297366ba692faf1f0384811a6ff0b20c3470b1b)
- [x86, ds: support Core i7](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=017bc617657c928cb9a0c45a7a7e9f4e66695347)
- [x86: implement percpu_alloc kernel parameter](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fa8a7094ba1679b4b9b443e0ac9f5e046c79ee8d)
- [x86, intr-remap: add option to disable interrupt remapping](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=03ea81550676296d94596e4337c771c6ba29f542)
- [x86: make CONFIG_RELOCATABLE the default](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=26717808f93a27c22d4853c4fb17fa225f4ccc68)
- [x86, mce: add basic error injection infrastructure](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ea149b36c7f511d17dd89fee734cb09778a91fa0)
- [x86, mce: Add boot options for corrected errors](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=62fdac5913f71f8f200bd2c9bd59a02e9a1498e9)
- [x86, mce: add machine check exception count in /proc/interrupts](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=01ca79f1411eae2a45352709c838b946b1af9fbd)
- [x86, mce: add MCE poll count to /proc/interrupts](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ca84f69697da0f004135e45b63ca560b6bd3554e)
- [x86, mce: add table driven machine check grading](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=817f32d02a52dd7f5941534e0699883691e918df)
- [x86, mce: deprecate old 32bit machine check code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=45f458e9a8a216b02b76fe61d9e8bc40d659fbe8)
- [x86, mce: document new 32bit mcelog requirement in Documentation/Changes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=172d899db4bf0beb7766d583379e5ed552130e4a)
- [x86, mce: enable MCE_AMD for 32bit NEW_MCE](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=de5619dfef76ddb403eb7c6de39c0130166c5dc3)
- [x86, mce: enable MCE_INTEL for 32bit new MCE](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7856f6cce4a8cda8c1f94b99605c07d16b8d8dec)
- [x86, mce: improve documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8780e8e0f6b34862cdf2c62d4d2674d6bc3207db)
- [x86, mce: use 64bit machine check code on 32bit](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4efc0670baf4b14bc95502e54a83ccf639146125)
- [x86, mce: therm_throt: Don't log redundant normality](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4e5c25d405e18a2f279ca2bfc855508ec3a0186b)
- [x86, mce: don't log boot MCEs on Pentium M (model == 13) CPUs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c7f6fa44115d401e89db730f357629d39f8e4ba6)
- [x86, mce: Don't initialize MCEs on unknown CPUs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e412cd257e0d51e0ecbb89f50953835b5a0681b2)
- [x86: MSR: add methods for writing of an MSR on several CPUs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b034c19f9f61c8b6f2435aa2e77f52348ebde767)
- [x86: nmi: Add Intel processor 0x6f4 to NMI perfctr1 workaround](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fe955e5c793aab398794be4c5ede172d48446c4a)
- [x86/PCI: add description for check_enable_amd_mmconf boot parameter](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1298307736a5882352418b4dc7c65442ab3b8bd4)
- [x86: smarten /proc/interrupts output for new counters](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7333a8003cdc0470e8c0ae8b949cbc44f3165ff3)
- [x86, setup: "glove box" BIOS calls -- infrastructure](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7a734e7dd93b9aea08ed51036a9a0e2c9dfd8dac)
- [x86, setup: "glove box" BIOS interrupts in the APM code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d54ea252e4c92357226992cf65d94616a96e6fce)
- [x86, setup: "glove box" BIOS interrupts in the core boot code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=df7699c56421c0476704f24a43409ac8c505f3d2)
- [x86, setup: "glove box" BIOS interrupts in the EDD code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3435d3476c5ed955d56a6216ed2d156847b3a575)
- [x86, setup: "glove box" BIOS interrupts in the MCA code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0a706db320768f8f6e43bbf73b58d2aabdc93354)
- [x86, setup: "glove box" BIOS interrupts in the video code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cf06de7b9cdd3efee7a59dced1977b3c21d43732)

...Various:

- [Add Fenghua Yu as temporary co-maintainer for ia64](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fadfd2b6ba8838a6cc458dbae214993a177a3ee9)
- [amd64_edac: add DRAM address type conversion facilities](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=93c2df58b5b1a434cca8f60067e0e12d1942b7f1)
- [asm-generic: add a generic unistd.h](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e64a1617eca39d62b248a11699de9c1195369661)
- [asm-generic: add generic ABI headers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6103ec56c65c33774c7c38652c8204120c3c7519)
- [avr32: Add support for Mediama RMTx add-on board for ATNGW100](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4024533e60787a5507818b0c0fdb44ddb522cdf5)
- [Blackfin: add support for bzip2/lzma compressed kernel images](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=538067c822e2512d9a165c71c0c5722168470304)
- [Blackfin: initial support for ftrace](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1c873be744410e26fb91ee9228c90adff6eabe15)
- [Blackfin: initial support for ftrace grapher](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1ee76d7e169ff2b0ff1df4b40b9d5276eec9ffb4)
- [DMA: TXx9 Soc DMA Controller driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ea76f0b3759283ec3cc06c86e266bf0fa6a981d2)
- [MIPS: Add Cavium OCTEON PCI support.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e8635b484f644c7873e6091f15330c49396f2cbc)
- [MIPS: Add hibernation support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=363c55cae53742f3f685a1814912c6d4fda245b4)
- [MIPS: Add support for Texas Instruments AR7 System-on-a-Chip](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7ca5dc145bc7daddd8aed8bbda46b74af9cebefc)
- [MIPS: Allow suspend and hibernation again on uniprocessor kernels.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3f5b3e17f791ba27f91fc4fdc514e7704d4d6273)
- [MIPS: CMP: activate CMP support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0365070f05f12f1648b4adf22cfb52ec7a8a371c)
- [S390: ftrace: add dynamic ftrace support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=dfd9f7abc0fb67b5781f340d982384cea53b2884)
- [S390: ftrace: add function graph tracer support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=88dbd2037229bd2ed7543ffd0d8f2d9dec9d31d2)
- [S390: ftrace: add function trace mcount test support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8b4488f85d619253c9e631ec723368f400106771)
- [S390: ftrace: add system call tracer support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9bf1226b33dc2f94fc37ffd70ee161e2bda1ff5c)
- [S390: pm: memory hotplug power management callbacks](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=039979049834bde56f67f8078c802b416bd4763c)
- [S390: secure computing arch backend](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bcf5cef7db869dd3b0ec55ad99641e66b2f5cf02)
- [sh: Add ms7724se (SH7724) board support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=287c129716c2d4b75f3d8dd6e68732a3cd326ee6)
- [sh: Add support for SH7724 (SH-Mobile R2R) CPU subtype.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0207a2efb43d81e29e23662b5d035945688a103f)
- [sh: SH7786 SMP support.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2eb2a4368273e123d2716a704c86f3130aa14c22)
- [sparc64: Add proper dynamic ftrace support.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9be12f9b1c4fd5f18cc82c170a32bfe1713ba76d)
- [sparc64: Use new dynamic per-cpu allocator.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4fd78a5f1edf62ab1ca3d23efee4a8a336edb2b6)

**MM**

- [memcg: add file-based RSS accounting](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d69b042f3d7406ddba560143b1796020df760800)
- [memcg: add interface to reset limits](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c5b947b28828e82814605824e5db0bc58d66d8c0)
- [memcg: fix behavior under memory.limit equals to memsw.limit](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=22a668d7c3ef833e7d67e9cef587ecc78069d532)
- [mm: add swap cache interface for swap reference](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cb4b86ba47bb0937b71fb825b3ed88adf7a190f0)
- [mm: introduce PageHuge() for testing huge/gigantic pages](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=20a0307c0396c2edb651401d2f2db193dda2f3c9)
- [mm: Pass virtual address to \_\_p{te,ud,md}\_free_tlb()](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9e1b32caa525cb236e80e9c671e179bcecccc657)
- [mm: remove CONFIG_UNEVICTABLE_LRU config option](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6837765963f1723e80ca97b1fae660f3a60d77df)
- [mm, x86: remove MEMORY_HOTPLUG_RESERVE related code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=888a589f6be07d624e21e2174d98375e9f95911b)
- [oom: move oom_adj value from task_struct to mm_struct](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2ff05b2b4eac2e63d345fc731ea151a060247f53)
- [pagemap: add page-types tool](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=35efa5e993a7a00a50b87d2b7725c3eafc80b083)
- [pagemap: document 9 more exported page flags](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=17e895012f7fe9dc63144990da98c41bbc22d68f)
- [pagemap: document clarifications](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c9ba78e226057a1c2f19671383c496df187c02b5)
- [vmscan: make mapped executable pages the first class citizen](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8cab4754d24a0f2e05920170c845bd84472814c6)
- [vmscan: properly account for the number of page cache pages zone_reclaim() can reclaim](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=90afa5de6f3fa89a733861e843377302479fcf7e)
- [x86: add hooks for kmemcheck](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f85612967c93b67b10dd240e3e8bf8a0eee9def7)

**Tracing**

- [blktrace: add trace/ to /sys/block/sda](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1d54ad6da9192fed5dd3b60224d9f2dfea0dcd82)
- [blktrace: support per-partition tracing](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d0deef5b14af7d5bbd0003a0a2a1a32326e20a6d)
- [blktrace: support per-partition tracing for ftrace plugin](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9908c30997b8a73c95f836170b9998dae9aa3f4a)
- [ftrace: add kernel command line function filtering](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2af15d6a44b871ad4c2a651302374cde8f335480)
- [function-graph: add option to calculate graph time or not](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a2a16d6a3156ef7309ca7328a20c35df9418e670)
- [function-graph: add stack frame test](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=71e308a239c098673570d0b417d42262bb535909)
- [function-graph: disable when both x86_32 and optimize for size are configured](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=eb4a03780d4c4464ef2ad86d80cca3f3284fe81d)
- [gcov: fix documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=972c71a3183ab41c0b1a9e50842be7e3e980954f)
- [kernel: constructor support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b99b87f70c7785ab1e253c6220f4b0b57ce3a7f7)
- [oprofile: add support for Core i7 and Atom](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6adf406f0a0eaf37251018d15f51e93f5b538ee6)
- [oprofile: introduce module_param oprofile.cpu_type](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7e4e0bd50e80df2fe5501f48f872448376cdd997)
- [ring-buffer: add benchmark and tester](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5092dbc96f3acdac5433b27c06860352dc6d23b9)
- [ring-buffer: add total count in ring-buffer-benchmark](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7da3046d6ce6ea97494020081c509b642b7016af)
- [tracing: add average time in function to function profiler](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=34886c8bc590f078d4c0b88f50d061326639198d)
- [tracing: Add documentation for the power tracer](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=56c49951747f250d8398582509e02ae5ce1d36d1)
- [tracing: add function profiler](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bac429f037f1a51a74d62bad6d1518c3be065df3)
- [tracing: adding function timings to function profiler](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0706f1c48ca8a7ab478090b4e38f2e578ae2bfe0)
- [tracing: add irq tracepoint documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9ee1983c9aa18f12388ef660d0c76a23dc112959)
- [tracing: add new tracepoints docbook](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a76f8c6da1e48fd4ef025f42c736389532ff30ba)
- [tracing: Document the event tracing system](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=abd41443ac76d3e9c29a8c1d9e9a3312306cc55e)
- [tracing/events: Documentation updates](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=143c145e3a475065a4be661468d0df1bd0b25f74)
- [tracing/filters: support for filters of dynamic sized arrays](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e8808c1019b048a43686dbd25c188a035842c2e2)
- [tracing: make the function profiler per cpu](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cafb168a1c92e4c9e1731fe3d666c39611762c49)

**Virtualisation**

- [KVM: Add VT-x machine check support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a0861c02a981c943573478ea13b29b1fb958ee5b)
- [KVM: Enable MSI-X for KVM assigned device](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d510d6cc653bc4b3094ea73afe12600d0ab445b3)
- [KVM: Fix cpuid feature misreporting](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8d753f369bd28fff1706ffe9fb9fea4fd88cf85b)
- [KVM: SVM: Add NMI injection support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=95ba82731374eb1c2af4dd442526c4b314f0e8b6)
- [lguest: add support for indirect ring entries](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d1f0132e76a11b05167313c606a853953f416081)
- [lguest: Add support for kvm_hypercall4()](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cefcad1773197523e11e18b669f245e6a8d32058)
- [xen: add "capabilities" file](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=818fd20673df82031e604bb784d836f1fc2e2451)

For other articles on 2.6.31 and links to the rest of the "Coming in 2.6.31" series, see The H's [Kernel Log - 2.6.31 Tracking](../site/open/features/Kernel-Log-2-6-31-Tracking-746446.html "Kernel Log - 2.6.31 Tracking â 02 July 2009, 11:21") page.

([trk](mailto:trk@h-online.com "Terry Relph-Knight"))
