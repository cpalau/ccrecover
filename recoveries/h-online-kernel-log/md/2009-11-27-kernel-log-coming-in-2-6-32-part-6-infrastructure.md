---
title: "Kernel Log: Coming in 2.6.32 (Part 6): Infrastructure"
date: 2009-11-27
author: "Chris von Eitzen"
source: http://www.h-online.com/open/news/item/Kernel-Log-Coming-in-2-6-32-Part-6-Infrastructure-869973.html
pages: 1
---

# Kernel Log: Coming in 2.6.32 (Part 6): Infrastructure

**Chris von Eitzen**

#### ![](../site/imgs/43/4/4/7/6/6/8/KL.jpg-f1b4876436255b3d.jpeg) by Thorsten Leemhuis

**Devtmpfs, aka 'devfs 2.0' to its detractors, should allow the Linux kernel to start faster and run without udev. Support has been added for ACPI 4.0 and there are two new make targets which generate kernel configurations attuned to the running system. Changes to the power management subsystem increase data throughput and allow better use of runtime power saving features on modern I/O devices.**

On releasing Linux 2.6.32-rc8, Linus Torvalds hinted that kernel version 2.6.32 could be released by the end of this month. The Kernel Log therefore brings its reporting on the changes in kernel 2.6.32 to an end, dedicating the sixth article in the 'What's coming in 2.6.32' series to changes in and around the kernel infrastructure. The first four articles in the series dealt with changes in the [networking subsystem](../site/news/item/Kernel-Log-Coming-in-2-6-32-Part-1-Network-subsystem-and-network-drivers-832229.html "Kernel Log: Coming in 2.6.32 (Part 1) – Network subsystem and network drivers â 19 October 2009, 13:50"), in the [graphics hardware](../site/news/item/Kernel-Log-Coming-in-2-6-32-Part-2-Graphics-858783.html "Kernel Log: Coming in 2.6.32 (Part 2) - Graphics â 12 November 2009, 18:00"), in [storage hardware and file systems](../site/news/item/Kernel-Log-Coming-in-2-6-32-Part-3-Storage-864376.html "Kernel Log: Coming in 2.6.32 (Part 3) - Storage â 20 November 2009, 17:40") and in [other drivers](../site/news/item/Kernel-Log-Coming-in-2-6-32-Part-4-Drivers-868263.html "Kernel Log: Coming in 2.6.32 (Part 4) - Drivers â 25 November 2009, 14:03"), while the fifth article looked at [architecture code, memory management, virtualisation and tracing](../site/news/item/Kernel-Log-Coming-in-2-6-32-Part-5-Architecture-code-memory-management-virtualisation-and-tracing-870357.html "Kernel Log: Coming in 2.6.32 (Part 5) - Architecture code, memory management, virtualisation and tracing â 27 November 2009, 10:10") .

### ACPI, PCI and PM

Various patches add support for ACPIÂ 4.0 to the Linux kernel. They are accompanied by a [driver](http://git.kernel.org/linus/de584afa5e188a2da484bb5373d449598cdb9f5e) for ACPIÂ 4.0-compliant power meters and an [ACPI Processor Aggregator Device Driver](http://git.kernel.org/linus/8e0af5141ab950b78b3ebbfaded5439dcf8b3a8d). The latter makes individual CPUs idle when instructed to do so via ACPIÂ 4.0, in order to temporarily reduce power consumption in the event, for example, of an electrical emergency or impending overheating. This allows a system to continuing running, albeit with reduced performance, rather than switching itself off. Its merger followed a long discussion in which Torvalds spoke out in favour of the driver â€“ details can be found in an [article on LWN.net](http://lwn.net/Articles/355934/).

[VGA arbitration patches](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=deb2d2ecd43dfc51efe71eed7128fda514da96c6) have now been integrated into the PCI subsystem. On systems with multiple graphics cards running X server version 1.7 or later, this code ensures that each graphics card receives the correct X server VGA command, offering a big increase in flexibility when setting up multi-seat environments. Details can be found in the [kernel documentation](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob_plain;f=Documentation/vgaarbiter.txt;hb=HEAD) and in two old blog entries by [Dave Airlie](http://airlied.livejournal.com/67628.html) and [Tiago Vignatti](http://vignatti.wordpress.com/2009/07/24/multiseat-with-multiple-x-servers-or-the-right-way/). PCI subsystem maintainer Jesse Barnes lists several further major changes within the PCI subsystem in his [main git pull request](http://thread.gmane.org/gmane.linux.kernel/889928). These include enhancements for PCI ASPM (Active State Power Management) and improved reset options for PCIe devices â€“ the changes implementing these enhancements are listed at the end of this article.

[Several major changes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5e928f77a09a07f9dd595bb8a489965d69a83458) to the power management code create the basis for making better use of the runtime power saving features on modern I/O devices â€“ details can be found in [this LWN.net article](http://lwn.net/Articles/347573/). An [enhancement](http://git.kernel.org/linus/69d25870f20c4b2563304f2b79c5300dd60a067e) to the Cpuidle framework, also explained [on LWN.net](http://lwn.net/Articles/352863/), should increase I/O throughput on larger servers in particular â€“ in some cases significantly. Further changes to the power management code are listed in Rafael J. Wysocki's [main git pull request](http://thread.gmane.org/gmane.linux.kernel/889249).

### Scheduling and security

There have been numerous enhancements to the kernel scheduler, which is responsible for allocating processor time to different applications ([1](http://thread.gmane.org/gmane.linux.kernel/888423),Â [2](http://thread.gmane.org/gmane.linux.kernel/891182)). After a fork, the kernel does not, now, [execute the child process first](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2bba22c50b06abe9fd0d23933b1e64d35b419262). There is also the new SCHED_RESET_ON_FORK flag â€“ if set, the kernel will reset the priority of child processes to the default â€“ background information on these two changes can be found in two [LWN.net](http://LWN.net) articles ([1](http://lwn.net/Articles/352863/),Â [2](http://lwn.net/Articles/339316/)).

Changes to the process scheduler also eliminate two weaknesses found in speed comparisons made using Con Kolivas' recently published and independently developed BFS ("Brain Fuck Scheduler"). One of these problems resulted in x264 encoding being significantly slowed on multi-core systems. One of the x264 developers explains the background to this problem [on a blog](http://x264dev.multimedia.cx/?p=185) and also takes the opportunity to make some recommendations on improving collaboration between developers.

Sysfs [now supports](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ddd29ec6597125c830f7badb608a86c98b936b64) security labels, allowing security frameworks such as SELinux to monitor access to the virtual file system. Crypto subsystem maintainer Herbert Xu has summarised some of the more significant cryptography-related changes in his [main git pull request for 2.6.32](http://thread.gmane.org/gmane.linux.kernel/772371/focus%3D887836).

### A second shot at devfs

Following lengthy discussions over the summer, [devtmpfs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2b2af54a5bb6f7e80ccf78f20084b93c398c3a8b), aka 'devfs 2.0' to its detractors, has now made it into the kernel. It allows the kernel, on booting, to itself create and mount a RAMdisk populated with a device file system. This can speed up boot time and makes it possible to boot without using an initrd populated with udev or similar.

These, however, are just some of the benefits of devtmpfs, which has come under [heavy fire](http://thread.gmane.org/gmane.linux.kernel/890291) from some quarters. Torvalds, however, liked the concept, in particular the fact that the kernel is now able to carry out the whole boot process autonomously. How it works is explained in [an old LWN.net article](http://lwn.net/Articles/331818/). Directly after it was merged, it was realised that udev would still be required after booting, in order (among other things) to [set](http://lwn.net/Articles/353849/) privileges for /dev/null and /dev/zero. A hastily [added patch](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e454cea20bdcff10ee698d11b8882662a0153a47) now allows the kernel to take care of this too.

### Suitably configured

Kernel testers can now use [the new 'localmodconfig' make target](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=281c9dadc31ffd9f3cf637553134fefe75e849da) to, relatively simply, create a kernel configuration attuned to the distribution and hardware being used, and which does not compile any unneeded modules. This uses the configuration file for the currently running kernel and deactivates all modules which are not loaded in the kernel when it is run.

As a consequence, drivers for hardware which is not connected when the make is called, such as USB devices, may be omitted. For testers, however, it has the potential to save a bunch of time when generating a kernel, as [explained](http://thread.gmane.org/gmane.linux.kbuild.devel/3750) in a git pull request by Steven Rostedt, the kernel hacker responsible for this change. Rostedt also explains how it works and describes the '[localyesconfig](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=281c9dadc31ffd9f3cf637553134fefe75e849da)' make target, which generates a kernel configuration into which all modules loaded when it is called are compiled.

### Minor Gems

Many further minor, but by no means insignificant, changes can be found in the list below. Like many of the references in the text above, the links point to the relevant commits in the [web front end](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git&a=summary) of the Git branch at kernel.org that Linus Torvalds uses for maintaining the kernel sources. There, the commit comments and the patches themselves provide extensive further information on the respective changes.

### ACPI

- [ACPI: add AC/DC notifier](http://git.kernel.org/linus/68b92b567c0c5e6f4d0b264d438f97ee5ccbdccc)
- [ACPI button: provide lid status functions](http://git.kernel.org/linus/7e12715ecc47a8a59154afe2746e48998225bb69)
- [ACPICA: ACPI 4.0 : Add new return package type, restructure module.](http://git.kernel.org/linus/53e9387bdd8bfef6cffff2d2eb6bd28eca812682)
- [ACPICA: ACPI 4.0: iASL/Disassembler - IPMI keyword support.](http://git.kernel.org/linus/3db20bed579bc4e7fe581c48ad1bde853aa9ff68)
- [ACPICA: ACPI 4.0: Interpreter support for IPMI.](http://git.kernel.org/linus/6557a49a443a347d24aed58076365432ded30edc)
- [ACPICA: ACPI 4: Add validation for new predefined names.](http://git.kernel.org/linus/999e08f99846a1fd6ee9642ec306a2d318925116)
- [ACPICA: Add 64-bit support to acpi_read and acpi_write](http://git.kernel.org/linus/c6b5774caafa4c12b6019366e2fdaaff117e95a4)
- [ACPICA: Add support for module-level executable AML code](http://git.kernel.org/linus/7f0c826a437157d2b19662977e9cf3b472cf24a6)
- [ACPICA: Major update for acpi_get_object_info external interface](http://git.kernel.org/linus/15b8dd53f5ffaf8e2d9095c423f713423f576c0f)
- [ACPICA: Update \_OSI with new Windows OS strings](http://git.kernel.org/linus/eb752552464dbb7a99f8a975ec3b9355893cedd4)
- [ACPICA: Windows compatibility: autoexecute root \_INI method](http://git.kernel.org/linus/9e64155eb1b6ab78980db58cfd21385fa5f6b024)
- [ACPI: Make ACPI processor proc I/F depend on the ACPI_PROCFS](http://git.kernel.org/linus/74cad4ee9839669ad920257678ea0bf0a818cd3b)
- [ACPI, PCI: Change PREFIX to "PCI" from "ACPI" in mmconfig-shared.c](http://git.kernel.org/linus/f4a2d5840e9f0e48d1a787b66e7346087a756029)
- [led: document sysfs interface](http://git.kernel.org/linus/5f634c6527249275df4199a294ee9cec2f3ff3b1)
- [Revert "ACPI: Attach the ACPI device to the ACPI handle as early as possible"](http://git.kernel.org/linus/f61f925859c57f6175082aeeee17743c68558a6e)
- [SFI: add capability to parse ACPI tables](http://git.kernel.org/linus/13e82d023c4c3f13ab1e665cbb917a7ebba8935c)
- [SFI: add platform-independent core support](http://git.kernel.org/linus/6ae6996a466e14bcf41618cde641a74ae03dc285)
- [SFI: create linux/sfi.h](http://git.kernel.org/linus/117a9ac777f8034d4675b821172d2ff71f6ec47a)
- [thermal: sysfs-api.txt - document passive attribute for thermal zones](http://git.kernel.org/linus/29226ed3c3b5cd0b2b0b1fb40ffeac3f796b80e9)
- [video/backlight: document sysfs interface](http://git.kernel.org/linus/3c4c1b69a2d76ac9a1c716233fde956dba757d76)
- [video/lcd: document sysfs interface](http://git.kernel.org/linus/243ca3e401bc62e704785d215931f1a51fd53bd7)

### Crypto

- [crypto: ahash - Convert to new style algorithms](http://git.kernel.org/linus/88056ec346ccf41f63dbc7080b24b5fd19d1358d)
- [crypto: api - Add new style spawn support](http://git.kernel.org/linus/97eedce1a64a57648ac5e39f03825528c47ba72e)
- [crypto: cryptd - Add support to access underlaying shash](http://git.kernel.org/linus/ace1366369841c9c3a9788f79baa4d73f1c53107)
- [crypto: gcm - Use GHASH digest algorithm](http://git.kernel.org/linus/9382d97af586a47dad312765e35c61aa7ad7fcdd)
- [crypto: mv_cesa - Add support for Orion5X crypto engine](http://git.kernel.org/linus/85a7f0ac5370901916a21935e1fafbe397b70f80)
- [crypto: padlock - Switch sha to shash](http://git.kernel.org/linus/bbbee4679afd7c29a58087f133ffe241597f3144)
- [crypto: sha256_generic - Add export/import support](http://git.kernel.org/linus/9b2fda7b94a769af13c24582739e50664b0e27a8)
- [crypto: shash - Add spawn support](http://git.kernel.org/linus/942969992d86330c9700e2cd9afe8a6bea42df78)
- [crypto: talitos - add support for 36 bit addressing](http://git.kernel.org/linus/81eb024c7e63f53b871797f6e2defccfd008dcd4)
- [crypto: vmac - New hash algorithm for intel_txt support](http://git.kernel.org/linus/f1939f7c56456d22a559d2c75156e91912a2e97e)

### LVM, SELinux, ..,

- [Add audit messages on type boundary violations](http://git.kernel.org/linus/44c2d9bdd7022ca7d240d5adc009296fc1c6ce08)
- [CRED: Add some configurable debugging \[try \#6\]](http://git.kernel.org/linus/e0e817392b9acf2c98d3be80c233dddb1b52003d)
- [KEYS: Add a keyctl to install a process's session keyring on its parent \[try \#6\]](http://git.kernel.org/linus/ee18d64c1f632043a02e6f5ba5e045bb26a5465f)
- [KEYS: Add garbage collection for dead, revoked and expired keys. \[try \#6\]](http://git.kernel.org/linus/5d135440faf7db8d566de0c6fab36b16cf9cfc3b)
- [lsm: Add hooks to the TUN driver](http://git.kernel.org/linus/2b980dbd77d229eb60588802162c9659726b11f4)
- [LSM/SELinux: inode\_{get,set,notify}secctx hooks to access LSM security context information.](http://git.kernel.org/linus/1ee65e37e904b959c24404139f5752edc66319d5)
- [security: introducing security_request_module](http://git.kernel.org/linus/9188499cdb117d86a1ea6b04374095b098d56936)
- [selinux: Support for the new TUN LSM hooks](http://git.kernel.org/linus/ed6d76e4c32de0c2ad5f1d572b948ef49e465176)

### PCI

- [agp: Add generic support for graphics dma remapping](http://git.kernel.org/linus/ff663cf8705bea101d5f73cf471855c85242575e)
- [genirq: Support nested threaded irq handling](http://git.kernel.org/linus/399b5da29b9f851eb7b96e2882097127f003e87c)
- [intel_agp: Use PCI DMA API correctly on chipsets new enough to have IOMMU](http://git.kernel.org/linus/176616814d700f19914d8509d9f65dec51a6ebf7)
- [intel-iommu: Kill DMAR_BROKEN_GFX_WA option.](http://git.kernel.org/linus/0c02a20ff7695f9c54cc7c013dda326270ccdac8)
- [intel-iommu: Support PCIe hot-plug](http://git.kernel.org/linus/99dcadede42f8898d4c963ef69192ef4b9b76ba8)
- [MAINTAINTERS: remove hotplug driver entries](http://git.kernel.org/linus/be3652b8a253346339ce32501dd48fb033258936)
- [PCI / ACPI PM: Propagate wake-up enable for devices w/o ACPI support](http://git.kernel.org/linus/0baed8da1ed91b664759f6c7f955b3a804457389)
- [PCI ASPM: support L1 only](http://git.kernel.org/linus/7557b5d63259d55f716e62e528978d4866318515)
- [PCI ASPM: support partial aspm enablement](http://git.kernel.org/linus/b7206cbf024dd43c42f9585e2017db1c1facd566)
- [PCI ASPM: support per direction l0s management](http://git.kernel.org/linus/ac18018a414a90d841ea81d38fecb913c0ec1880)
- [PCI: Document pci_ids.h addition policy.](http://git.kernel.org/linus/1d4a433fc4e9c7dbfc2069a8f1a1f4338b982427)
- [PCI hotplug: add pci_configure_slot()](http://git.kernel.org/linus/8838400db5193c37588813c2eb1249b821781950)
- [PCI hotplug: add support for 5.0G link speed](http://git.kernel.org/linus/825c423a35a80a8fd66398a3f9bde7f0b0187a76)
- [PCI: support for PCI Express fundamental reset](http://git.kernel.org/linus/260d703adc5f275e3ba7ddff6e2e0217bc613b35)
- [spi: add SPI driver for most known i.MX SoCs](http://git.kernel.org/linus/b5f3294f0be5496aec01e5aa709a5fab8bb2f225)
- [spi: add spi_ppc4xx driver](http://git.kernel.org/linus/44dab88e7cc99d1d2caa9a8936e09d9a98a6761a)
- [spi: add support for device table matching](http://git.kernel.org/linus/75368bf6c2876d8f33abfe77aa3864869a3893eb)
- [spi: Freescale STMP driver](http://git.kernel.org/linus/0644c48672a3146c01bf7314d440edecf8742d62)
- [spi: McSPI off-mode support](http://git.kernel.org/linus/a41ae1ad907655b2efbb9b1a97736ab1451e1649)
- [spi: remove i.MX SPI driver](http://git.kernel.org/linus/07fcaa2486ca4f5c67bebedfa56e705c4dd23fc2)
- [x86/amd-iommu: Support higher level PTEs in iommu_page_unmap](http://git.kernel.org/linus/a6b256b41357c33ccb2d105a4457e22bdc83e021)

### PM

- [CPUFREQ: Introduce global, not per core: /sys/devices/system/cpu/cpufreq](http://git.kernel.org/linus/8aa84ad8d6c740a04386f599694609ee4998e82e)
- [CPUFREQ: ondemand - Use global sysfs dir for tuning settings](http://git.kernel.org/linus/0e625ac153126a0a62b7635fa9dc91f87ff39e38)
- [CPUFREQ: Powernow-k8: Enable more than 2 low P-states](http://git.kernel.org/linus/db39d5529d347de5e2eec1a72d67fcfacae6c5a2)
- [CPUFREQ: update Doc for cpuinfo_cur_freq and scaling_cur_freq](http://git.kernel.org/linus/da470db16c703d7f9617c366a36c6670f89a9830)
- [cpuidle: menu governor: reduce latency on exit](http://git.kernel.org/linus/672917dcc781ead7652a8b11b1fba14e38ac15b8)
- [NOHZ: update idle state also when NOHZ is inactive](http://git.kernel.org/linus/fdc6f192e7e1ae80565af23cc33dc88e3dcdf184)
- [PM/Hibernate: Do not release preallocated memory unnecessarily (rev. 2)](http://git.kernel.org/linus/64a473cb74a88cb4991edf985d55a266e65292e1)
- [PM/Hibernate: Do not try to allocate too much memory too hard (rev. 2)](http://git.kernel.org/linus/ef4aede3f10d82adef1fb044b565ba5f08f851e0)
- [PM/Hibernate: Rework shrinking of memory](http://git.kernel.org/linus/4bb334353ebd821bc8eeabeb019eaac33c7307df)
- [tracing, x86, cpuidle: Move the end point of a C state in the power tracer](http://git.kernel.org/linus/288f023e708efd89d77ce9acf977a33a623ae83d)

### Process Scheduler

- [sched: Add come comments to the sched features](http://git.kernel.org/linus/e26af0e8b2c9916f1e8a12ddaf52057bbe8ff600)
- [sched: Add new wakeup preemption mode: WAKEUP_RUNNING](http://git.kernel.org/linus/ad4b78bbcbab66998b05d422ac6106b645796e54)
- [sched: Add SCHED_RESET_ON_FORK functionality for nice \< 0 tasks](http://git.kernel.org/linus/6c697bdf08a09ce461e305a22362973036e95db3)
- [sched: Add wait, sleep and iowait accounting tracepoints](http://git.kernel.org/linus/768d0c27226e6587cad2fcf543f9711da3f3774e)
- [sched: Clean up SCHED_RESET_ON_FORK](http://git.kernel.org/linus/b9dc29e72fd3dc2a739ce8eafd958220d0745734)
- [sched: Disable NEW_FAIR_SLEEPERS for now](http://git.kernel.org/linus/3f2aa307c4d26b4ed6509d0a79e8254c9e07e921)
- [sched: Ensure that a child can't gain time over it's parent after fork()](http://git.kernel.org/linus/b5d9d734a53e0204aab0089079cbde2a1285a38f)
- [sched: Implement a gentler fair-sleepers feature](http://git.kernel.org/linus/51e0304ce6e55a6e59658558916b4f74da085ff0)
- [sched: Introduce SCHED_RESET_ON_FORK scheduling policy flag](http://git.kernel.org/linus/ca94c442535a44d508c99a77e54f21a59f4fc462)
- [sched: Merge select_task_rq_fair() and sched_balance_self()](http://git.kernel.org/linus/c88d5910890ad35af283344417891344604f0438)
- [sched: Turn off child_runs_first](http://git.kernel.org/linus/2bba22c50b06abe9fd0d23933b1e64d35b419262)

### Various other changes

- [cgroups: add a read-only "procs" file similar to "tasks" that shows only unique tgids](http://git.kernel.org/linus/102a775e3647628727ae83a9a6abf0564c3ca7cb)
- [cgroups: let ss-\>can_attach and ss-\>attach do whole threadgroups at a time](http://git.kernel.org/linus/be367d09927023d081f9199665c8500f69f14d22)
- [cgroups: support named cgroups hierarchies](http://git.kernel.org/linus/c6d57f3312a6619d47c5557b5f6154a74d04ff80)
- [checkpatch: make -f alias --file, add --help, more verbose help message](http://git.kernel.org/linus/77f5b10a82bbd832c99ec4b120d5645342a5b140)
- [connector: Provide the sender's credentials to the callback](http://git.kernel.org/linus/7069331dbe7155f23966f5944109f909fea0c7e4)
- [docs: update patch size in SubmittingPatches](http://git.kernel.org/linus/4932be778952d4f3c278cbdef0d717358849aa8c)
- [Documentation: ABI: document /sys/devices/system/cpu/](http://git.kernel.org/linus/2ceb3fb0a78c671892b01319ac8e3baede33a78c)
- [Documentation: ABI: rename sysfs-devices-cache_disable properly](http://git.kernel.org/linus/468727ab1273a0f95562befa611a3ce39778599c)
- [Documentation: ABI: /sys/devices/system/cpu/cpuidle/](http://git.kernel.org/linus/c1fb5c475126b77b47ba762f5b48535cd0420d24)
- [Documentation: ABI: /sys/devices/system/cpu/cpu#/node](http://git.kernel.org/linus/657348a056eea4a27be20cf8e22c98a252597447)
- [Documentation: ABI: /sys/devices/system/cpu/cpu#/ topology files](http://git.kernel.org/linus/663fb2fc733006f685400fb44551303b72b61a88)
- [Documentation: ABI: /sys/devices/system/cpu/ topology files](http://git.kernel.org/linus/d93fc863d2d2cea1057996c39cef368f41741448)
- [Driver core: Add support for compatibility classes](http://git.kernel.org/linus/4622709445705c1e423d2addcfd8ccae052fe0ba)
- [exec: let do_coredump() limit the number of concurrent dumps to pipes](http://git.kernel.org/linus/a293980c2e261bd5b0d2a77340dd04f684caff58)
- [futex: Add memory barrier commentary to futex_wait_queue_me()](http://git.kernel.org/linus/9beba3c54dd180a26a1da2027cfbe9edfaf9c40e)
- [futex: Make function kernel-doc commentary consistent](http://git.kernel.org/linus/d96ee56ce0582967fba9f3f0ac4503957147bea6)
- [genirq: Add buslock support](http://git.kernel.org/linus/70aedd24d20e75198f5a0b11750faabbb56924e2)
- [genirq: Add oneshot support](http://git.kernel.org/linus/b25c340c195447afb1860da580fe2a85a6b652c5)
- [kbuild: add static to prototypes](http://git.kernel.org/linus/4356f4890792a678936c93c9196e8f7742e04535)
- [kbuild: introduce ld-option](http://git.kernel.org/linus/691ef3e7fdc1fe4dded169d9404f740987f67d66)
- [kbuild: rename ld-option to cc-ldoption](http://git.kernel.org/linus/f86fd306605287d7c7f4f0f8e8e2a9d49d28b396)
- [kbuild: set -fconserve-stack option for gcc 4.5](http://git.kernel.org/linus/8f7f5c9fc2966704579ff93f459ffa458bca6fc2)
- [kbuild: use INSTALLKERNEL to select customized installkernel script](http://git.kernel.org/linus/caa27b66bd7188fd063769eaf4b33533ef0709e6)
- [kconfig: add streamline_config.pl to scripts](http://git.kernel.org/linus/dcc60243e726978576cb02b74c84440629c69c87)
- [kconfig: add symbol value to help find the real depend](http://git.kernel.org/linus/544e433a9e2a8771b8281ac58acb5c794613e705)
- [kconfig: make local .config default for streamline_config](http://git.kernel.org/linus/a9024838d029ecd9a6d1389bec798b7296278d6b)
- [kconfig: make localmodconfig to run streamline_config.pl](http://git.kernel.org/linus/03fa25da8335a942161a8070b3298cfd4edf9b6a)
- [kconfig: test for /boot/config-uname after /proc/config.gz in localconfig](http://git.kernel.org/linus/810b2be65610af13d60f1e16c0a0f93cbc1f9d06)
- [kernel-doc: allow multi-line declaration purpose descriptions](http://git.kernel.org/linus/6423133bdee0e07d1c2f8411cb3fe676c207ba33)
- [kernel hacking: move STRIP_ASM_SYMS from General](http://git.kernel.org/linus/99657c7857fd47d6086682d4cf1194954170755a)
- [kmemleak: add clear command support](http://git.kernel.org/linus/30b3710105be0ba6bbdb7d7d126af76246b02eba)
- [kmemleak: Dump object information on request](http://git.kernel.org/linus/189d84ed54bbb05aac5b24d9d784d86c4d37f807)
- [memcg: add comments explaining memory barriers](http://git.kernel.org/linus/261fb61a8bf6d3bd964ae6f1e6af49585d30db51)
- [memcg: improve resource counter scalability](http://git.kernel.org/linus/0c3e73e84fe3f64cf1c2e8bb4e91e8901cbcdc38)
- [memcg: remove the overhead associated with the root cgroup](http://git.kernel.org/linus/4b3bde4c983de36c59e6c1a24701f6fe816f9f55)
- [memcg: show swap usage in stat file](http://git.kernel.org/linus/1dd3a27326d307952f8ad2499478c84dc7311517)
- [memory controller: soft limit documentation](http://git.kernel.org/linus/a6df63615b943dbef22df04c19f4506330fe835e)
- [memory controller: soft limit interface](http://git.kernel.org/linus/296c81d89f4f14269f7346f81442910158c0a83a)
- [memory controller: soft limit organize cgroups](http://git.kernel.org/linus/f64c3f54940d6929a2b6dcffaab942bd62be2e66)
- [memory controller: soft limit reclaim on contention](http://git.kernel.org/linus/4e41695356fb4e0b153be1440ad027e46e0a7ea2)
- [param: allow whitespace as kernel parameter separator](http://git.kernel.org/linus/26d052bfce799ef0e7262695b46e3525ca4d381d)
- [percpu: build first chunk allocators selectively](http://git.kernel.org/linus/08fc45806103e59a37418e84719b878f9bb32540)
- [percpu: implement optional weak percpu definitions](http://git.kernel.org/linus/7c756e6e19e71f0327760d8955f7077118ebb2b1)
- [percpu: introduce pcpu_alloc_info and pcpu_group_info](http://git.kernel.org/linus/fd1e8a1fe2b54df6c185b4fa65f181f50b9c4d4e)
- [percpu: use dynamic percpu allocator as the default percpu allocator](http://git.kernel.org/linus/e74e396204bfcb67570ba4517b08f5918e69afea)
- [printk: add printk_delay to make messages readable for some scenarios](http://git.kernel.org/linus/af91322ef3f29ae4114e736e2a72e28b4d619cf9)
- [rcu: Add synchronize_sched_expedited() rcutorture doc + updates](http://git.kernel.org/linus/240ebbf81f149b11a31e060ebe5ee51a3c775360)
- [rcu: Kconfig help needs to say that TREE_PREEMPT_RCU scales down](http://git.kernel.org/linus/bbe3eae8bb039b5ffd64a6e3d1a0deaa1f3cbae9)
- [rcu: Merge preemptable-RCU functionality into hierarchical RCU](http://git.kernel.org/linus/f41d911f8c49a5d65c86504c19e8204bb605c4fd)
- [rcu: Remove Classic RCU](http://git.kernel.org/linus/c17ef45342cc033fdf7bdd5b28615e0090f8d2e7)
- [rcu: Remove CONFIG_PREEMPT_RCU](http://git.kernel.org/linus/6b3ef48adf847f7adf11c870e3ffacac150f1564)
- [rcu: Renamings to increase RCU clarity](http://git.kernel.org/linus/d6714c22b43fbcbead7e7b706ff270e15f04a791)
- [scripts/get_maintainer.pl: add --git-blame](http://git.kernel.org/linus/f5492666a3b62344de9026a960c11888160362c9)
- [scripts/get_maintainer.pl: add .mailmap use, shell and email cleanups](http://git.kernel.org/linus/8cbb3a77e1a91073fb279a495a11d5093461dfe5)
- [scripts/get_maintainer.pl: add maintainers in order listed in matched section](http://git.kernel.org/linus/b781655a6f6d15bdcc96f2cc1d56b0658f9cf0b4)
- [scripts/get_maintainer.pl: add patch/file search for keywords](http://git.kernel.org/linus/dcf36a92f569b2c240129d8c6ae4c366c1658766)
- [scripts/get_maintainer.pl: add --pattern-depth](http://git.kernel.org/linus/3fb55652b9f754990e286723f209ce3c07c96d69)
- [scripts/get_maintainer.pl: add --remove-duplicates](http://git.kernel.org/linus/11ecf53c97863a0609db3816d82f1d0ddf3d2bc2)
- [scripts/get_maintainer.pl: add sections in pattern match depth order](http://git.kernel.org/linus/1d606b4e0bf8fe45e3f88543dfce83207ae0027d)
- [time: add function to convert between calendar time and broken-down time for universal use](http://git.kernel.org/linus/57f1f0874f426a9bdfc5cd3f886113dd5cd17834)
- [time: Introduce CLOCK_REALTIME_COARSE](http://git.kernel.org/linus/da15cfdae03351c689736f8d142618592e3cebc3)
- [timekeeping: Add timekeeper read_clock helper functions](http://git.kernel.org/linus/2ba2a3054fdffc8e6452f4ee120760322a6fbd43)
- [timekeeping: Add xtime_shift and ntp_error_shift to struct timekeeper](http://git.kernel.org/linus/23ce72117c714baab794e66c8daf343bf6a912bf)
- [timekeeping: Increase granularity of read_persistent_clock()](http://git.kernel.org/linus/d4f587c67fc39e0030ddd718675e252e208da4d7)
- [timekeeping: Introduce struct timekeeper](http://git.kernel.org/linus/155ec60226ae0ae2aadaa57c951a58a359331030)
- [Update flex_arrays.txt](http://git.kernel.org/linus/1243ba98e3abecd12e9e90dd390801b95ef070f2)

### Latecomers

The previous five parts of the Kernel Log mini series have already given a detailed overview of the many changes in of the Linux kernel. All of the major enhancements have already been mentioned there, as they entered the main development branch during the first phase of the development cycle. But some small, usually not quite as important changes that fall in the "minor gems" section entered the kernel later â€“ for completeness, we have included these changes in the following list.

### Graphics

- [drm: Add the basic check for the detailed timing in EDID](http://git.kernel.org/linus/f059d2ad69b056aeabad4460f706a3df2f77ce50)
- [drm/radeon/kms: add debugfs for power management for AtomBIOS devices](http://git.kernel.org/linus/7433874e31f7f2e6e942b1201279056%3D)
- [drm/radeon/kms: add quirk for acer 5102](http://git.kernel.org/linus/790cfb34ad645be3bf69265cb05d824aeabcfa11)
- [drm/radeon/kms: add quirk for hp dc5750](http://git.kernel.org/linus/fc7f7119d2ed97fff1aaddad6bf7d61ed446cf37)
- [drm/radeon/kms: add support for msi](http://git.kernel.org/linus/3e5cb98dfe87cc61d0a1119dd8aa2b1e4cfab424)
- [drm/radeon/kms/atom: add support for AdjustDisplayPll](http://git.kernel.org/linus/2606c88608122339cbd5c6b5c149a2eb74ccfe9e)
- [drm/radeon/kms/atom: add support for spread spectrum (v2)](http://git.kernel.org/linus/ebbe1cb936dfc96d809ccf4d64a9755f8ba0c0ff)
- [drm/radeon/kms: fix support for original r100](http://git.kernel.org/linus/d0c403e950d449c8c413a1fbf05dfec45ce03e55)
- [drm/radeon/kms: initial mode validation support](http://git.kernel.org/linus/a3fa6320ce964f799388b152a1b0f6e2c3b32a7f)

### Network

- [ath5k: add LED definition for BenQ Joybook R55v](http://git.kernel.org/linus/1e93bd4a132661f9403b61b821810df5ba2dc0f8)
- [ath5k: add LED support for HP Compaq CQ60](http://git.kernel.org/linus/6f9797ae22abbf6ade3eb53431e34c3c39214329)
- [e1000e: config PHY via software after resets](http://git.kernel.org/linus/f523d2114e93c559dbcf1b49d46b339fc0eda37a)
- [e100: e100_phy_init() isolates selected PHY, causes 10 second boot delay](http://git.kernel.org/linus/8fbd962e39517dfb2bfd363eba4b51cdfa299593)
- [iwlwifi: Use RTS/CTS as the preferred protection mechanism for 6000 series](http://git.kernel.org/linus/73871f7181a1406c67e93c8c83f5edb26057a2a6)
- [mlx4_core: Add a new supported 40 GigE device ID](http://git.kernel.org/linus/06c3aa5ef1c9491f4c94483ca52afc420bc58c5a)
- [netdev: usb: dm9601.c can drive a device not supported yet, add support for it](http://git.kernel.org/linus/06b71b657b03c33b8d919da29f33d326f1471b39)

For other articles on 2.6.32 and links to the rest of the "Coming in 2.6.32 " series, see [The H's Kernel Log - 2.6.32 Tracking page](../site/open/features/2-6-32-Tracking-816707.html "2.6.32 Tracking â 05 October 2009, 17:04"). ([thl](mailto:thl@ct.heise.de) /c't).

([crve](mailto:crve@h-online.com "Chris von Eitzen "))
