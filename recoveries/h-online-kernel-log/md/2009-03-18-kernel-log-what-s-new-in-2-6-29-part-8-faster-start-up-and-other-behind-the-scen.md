---
title: "Kernel Log: What's new in 2.6.29 - Part 8: Faster start-up and other behind the scenes changes"
date: 2009-03-18
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-8-Faster-start-up-and-other-behind-the-scenes-changes-740591.html
pages: 1
---

# Kernel Log: What's new in 2.6.29 - Part 8: Faster start-up and other behind the scenes changes

**Dj Walker-Morgan**

![kernellogpenguin.jpg](../site/imgs/43/3/6/7/0/2/3/93e8ea3d0acdf147.jpg) Following the eighth pre-release version of 2.6.29, development of the next major kernel revision looks to have hit the home straight. A glance at the changed files and code makes it clear how hard the kernel hackers have been working on 2.6.29, with more new lines of code added over the current development cycle than ever before.

The bulk of the extra code is, as usual, made up of drivers and the sub-systems that surround them. The number of changes which improve behind-the-scenes aspects of the kernel infrastructure is, however, far from small and these are the subject of this Kernel Log, which concludes the ["What's coming in 2.6.29" series](../site/search/?filter_c3=4&filter_t1=1&q=kernel+log+2.6.29&search_submit=Search&rm=search) â€“ indeed it can't be long before Linus Torvalds releases Linux version 2.6.29.

### Fastboot

Following on from his ["Fastboot"](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-9-Fastboot-and-other-remainders-739431.html "Kernel Log: What's coming in 2.6.28 - Part 9: Fastboot and other remainders â 19 December 2008, 12:45") enhancements introduced in 2.6.28, which accelerate the kernel initialisation phase, and by extension, system start-up, Arjen van de Ven has generated further improvements in this area for 2.6.29. These now allow the kernel to initialise some mutually-independent subsystems [asynchronously](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=22a9d645677feefd402befd02edd59b122289ef1). This allows for the initialisation of one subsystem while code from another subsystem is still, for example, waiting for a response from the hardware it deals with. This kind of wait is especially common when initialising the Libata and SCSI subsystems, which at some points wait for tenths of a second or longer for drives to respond, when querying and setting up media.

This trick allows the boot phase between starting the kernel and transferring to userspace (/sbin/init) to become measurably and tangibly faster â€“ the magnitude of the benefit is, though, strongly system-dependent. [Due to some problems](http://thread.gmane.org/gmane.linux.kernel/777898), however, parallel initialisation will be largely deactivated in 2.6.29 unless the fastboot code is explicitly activated using the "fastboot" kernel parameter. Van de Ven is planning to take a second shot at the problem in 2.6.30 to allow more users to benefit from these changes. More details on how fastboot works can be found in an [article on LWN.net](http://lwn.net/Articles/314808/).

### Virtualisation and security

KVM developers have once again been busy, introducing around [150Â patches](http://thread.gmane.org/gmane.comp.emulators.kvm.devel/26924), which include enhancements to NMI, MSI and Kdump support and allow faster access to the MMU. [Changes](http://thread.gmane.org/gmane.linux.kernel/774794) to the IOMMU subsystem improve support for assigning PCI/PCIe devices to guest systems. A number of patches also improve support for container virtualisation. The new [Xenfs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1107ba885e46964316c083d441d5dd185b6c9e49) should improve the interaction between userspace and Xen.

The task credentials patches, which restructure the way the kernel deals with process-specific information (user and group ID, privileges, etc.), have been adopted in this kernel version ([LWN.net article](http://lwn.net/Articles/251469/), [kernel documentation](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob;f=Documentation/credentials.txt;hb=HEAD)). The LSM (Linux Security Modules) now offer [hooks](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=be6d3e56a6b9b3a4ee44a0685e39e595073c6f0d) for security frameworks such as AppArmor and Tomoyo, which may use file names to recognise programs â€“ SELinux and Smack, by contrast, rely on extended attributes. From 2.6.29, the kernel's cryptographic code will [be able to deal with shash](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=7b5a080b3c46f0cac71c0d0262634c6517d4ee4f).

### Behind the scenes

The Cpumask changes, driven primarily by Rusty Russell, now allow distributors to compile their kernels with support for up to 4096Â CPU cores without incurring major performance penalties on dual or quad core systems. Russell gives a rough overview of the background to the changes and how the code works on [his blog](http://ozlabs.org/~rusty/index.cgi/2009/01/07#2009-01-07).

The TreeÂ RCUÂ patches should allow the kernel to better scale to systems with "a few hundred processors" (e.g. [1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=64db4cfff99c04cd5f550357edcc8780f96b54a2)). Interested users can find a detailed explanation of how the new code works in an [LWN.net article](http://lwn.net/Articles/305782/) written by a patch author working for IBM.

There are also a [whole heap of changes](http://thread.gmane.org/gmane.linux.kernel/772439) relating to the ftrace tracking infrastructure. The kernel hackers have also included patches to allow the poll() function to sleep and introduced functions which can be used to protect exclusive access to I/O Memory. ([LWN.net article](http://lwn.net/Articles/308426/)). The latter allows drivers to protect I/O memory space used for communicating with hardware from unwanted write access by userspace programs, which can, in the worst case, make the hardware unusable â€“ as occurred with the "e1000e problem", where an [internal kernel error](../site/news/item/Kernel-Log-new-Catalyst-drivers-2-6-27-1-resolves-cause-of-e1000e-problem-737701.html "Kernel Log: new Catalyst drivers, 2.6.27.1 resolves cause of e1000e problem â 18 October 2008, 08:02") during [2.6.27 development](../site/news/item/Kernel-Log-problem-with-e1000e-bypassed-Morton-praises-Btrfs-737561.html "Kernel Log: problem with e1000e bypassed, Morton praises Btrfs â 07 October 2008, 08:47") disabled some Intel network cards.

The kernel can no longer be correctly compiled using GCC versions [3.0, 3.1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6680598b44ed3c0052d155522eb21fc5a00de5f3), [4.1.0 and 4.1.1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f9d14250071eda9972e4c9cea745a11185952114).

### Yet more changes

In addition to the new features described in this article, the kernel development team has also included a large number of additional patches in 2.6.29 â€“ the kernel hackers have, for example, combined the directories containing the code for supporting SPARC and SPARC64 and have extended the ARM code to add support for the i.MX31. Details of these and many less major, but in no way insignificant, changes can be found in the list below. The individual entries link to the relevant commit in the Linux source code control system, where further information on the change and the relevant patch can be found.

**Fastboot**

- [ahci: add a module parameter to ignore the SSS flags for async scanning](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f3d7f23f87723a0947164ec88fc40e08254a64d6)
- [async: don't do the initcall stuff post boot](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ad160d23198193135cb2bcc75222e0816b5838c0)
- [async: make async a command line option for now](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=cdb80f630be5cbc23d82331f24dc4704f75b64f4)
- [async: make the final inode deletion an asynchronous event](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=efaee192063a54749c56b7383803e16fe553630e)
- [bootchart: improve output based on Dave Jones' feedback](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=40c8c85a47552bd792b0ad49ddcc45ec18369134)
- [bootgraph: make the bootgraph script show async waiting time](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d3f8ddea444b3b5324d74144177a50557cd1f137)
- [fastboot: Make libata initialization even more async](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f29d3b23238e1955a8094e038c72546e99308e61)
- [fastboot: make scsi probes asynchronous](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4ace92fc112c6069b4fcb95a31d3142d4a43ff2a)
- [fastboot: make the libata port scan asynchronous](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=793180570ff2530d133343ceea85648de5f01b02)
- [libata: Add a per-host flag to opt-in into parallel port probes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=886ad09fc83342aa1c5a02a0b6d3298b78a8067f)
- [libata: only ports \>= 0 need to synchronize](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fa853a48413c2ca1a5dc6b539bf07cf8e7247f8e)
- [partial revert of asynchronous inode delete](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b32714ba29358a688ef337d5297bf4bdc9f596dc)

**Tracing**

- [blktrace: port to tracepoints](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5f3ea37c7716db4e894a480e0c18b24399595b6b)
- [ftrace: add function tracing to single thread](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=df4fc31558dd2a3a30292ddb3a64c2a5befcec73)
- [ftrace: add quick function trace stop](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=60a7ecf42661f2b22168751298592da6ee210c9e)
- [tracing: add a tracer to catch execution time of kernel functions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=15e6cb3673ea6277999642802406a764b49391b0)
- [tracing: add "power-tracer": C/P state tracer to help power optimization](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f3f47a6768a29448866da4422b6f6bee485c947f)
- [tracing/function-graph-tracer: enabled by default](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=764f3b95131a7ce5c992e3d00caf590fcada2f7b)
- [tracing/function-graph-tracer: support for x86-64](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=48d68b20d00865035b8b65e69af343d0f53fac9d)
- [tracing/function-return-tracer: change the name into function-graph-tracer](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fb52607afcd0629776f1dc9e657647ceae81dd50)
- [tracing/function-return-tracer: set a more human readable output](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=287b6e68ca7209caec40b2f44f837c580a413bae)
- [tracing: likely/unlikely branch annotation tracer](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=52f232cb720a7babb752849cbc2cab2d24021209)
- [tracing: profile likely and unlikely annotations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1f0d69a9fc815db82f15722bf05227190b1d714d)
- [tracing, x86: add low level support for ftrace return tracing](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=caf4b323b02a16c92fba449952ac6515ddc76d7a)

**Crypto/Security**

- [CRED: Documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=98870ab0a5a3f1822aee681d2997017e1c87d026)
- [CRED: Inaugurate COW credentials](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d84f4f992cbd76e8f39c488cf0c5d123843923b1)
- [CRED: Make execve() take advantage of copy-on-write credentials](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a6f76f23d297f70e2a6b3ec607f7aeeea9e37e8d)
- [CRED: Separate task security context from task_struct](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b6dff3ec5e116e3af6f537d4caedcad6b9e5082a)
- [CRED: Use RCU to access another task's creds and to release a task's own creds](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c69e8d9c01db2adc503464993c358901c9af9de4)
- [crypto: aes - Precompute tables](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0ee4a96902dd7858e65f378c86f428a0355bd841)
- [introduce new LSM hooks where vfsmount is available.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=be6d3e56a6b9b3a4ee44a0685e39e595073c6f0d)
- [libcrc32c: Move implementation to crypto crc32c](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=69c35efcf1576ab5f00cba83e8ca740923afb6c9)
- [netlabel: Update kernel configuration API](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6c2e8ac0953fccdd24dc6c4b9e08e8f1cd68cf07)
- [selinux: Deprecate and schedule the removal of the the compat_net functionality](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=277d342fc423fca5e66e677fe629d1b2f8f1b9e2)
- [smack: Add support for unlabeled network hosts and networks](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6d3dc07cbb1e88deed2e8710e215f232a56b1dce)
- [user namespaces: document CFS behavior](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=94d6a5f7341ebaff53d4e41cc81fab37f0d9fbed)

**Virtualisation**

- [Add DEVPTS_MULTIPLE_INSTANCES config token](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e4adca27bcbb8a73c4cf1dfa71392654cfa33345)
- [Add domain flag DOMAIN_FLAG_VIRTUAL_MACHINE](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1ce28feb22833645a0f3843cd873a0b56ed19ef0)
- [Add domain_flush_cache](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5331fe6f5627e06eec7d0dc154a0a3a9c27813c5)
- [add frontend implementation for the IOMMU API](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fc2100eb4d0960b56c2c705a97941c08fb1c0fd4)
- [Add global iommu list](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d9630fe941769dd050fbc38fbbac20a708ab9461)
- [Add/remove domain device info for virtual machine domain](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c7151a8dfefd11108de5b4293af2390962bcff71)
- [AMD IOMMU: add domain map function for IOMMU API](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c6229ca649aa9b312d1f1de20af8d2603b14eead)
- [AMD IOMMU: add Kconfig entry for statistic collection code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2e117604a4e8f3f9cee4aec3373b0382159e152a)
- [AMD IOMMU: add protection domain flags](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9fdb19d64c0247f23343b51fc85f438f8e7a2f3c)
- [cgroups: add a per-subsystem hierarchy_mutex](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=999cd8a450f8f93701669a61cac4d3b19eca07e8)
- [cgroups: clean up Kconfig](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=23964d2d02984d44aeb2d84d7ffb3359e728df43)
- [cgroups: consolidate cgroup documents](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=45ce80fb6b6f9594d1396d44dd7e7c02d596fef8)
- [cgroups: documentation updates](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=18e7f1f0d34be4a39f7f47324a3e26b43fddb714)
- [cgroups: make cgroup config a submenu](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5cdc38f98596662620b822a4e13f797c3f2f65e0)
- [Document usage of multiple-instances of devpts](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=784c4d8b1b1e66f8c45e8b889613f4982f525b2b)
- [Enable multiple instances of devpts](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2a1b2dc0c83bbfc24d72cafd5e69810a149b44e4)
- [introcude linux/iommu.h for an iommu api](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4a77a6cf6d9bf9f5c74b27f62bd2bfe6dcc88392)
- [KVM: change KVM to use IOMMU API](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=19de40a8472fa64693eab844911eec277d489f6c)
- [KVM: Enable MSI for device assignment](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6b9cc7fd469869bed38831c5adac3f59dc25eaf5)
- [KVM: Enable MTRR for EPT](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=64d4d521757117aa5c1cfe79d3baa6cf57703f81)
- [KVM: ia64: Re-organize data sturure of guests' data area](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a917f7af3905953329361d29b6db78eb17b4d44c)
- [KVM: MSI to INTx translate](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5319c662522db8995ff9276ba9d80549c64b294a)
- [KVM: ppc: Implement in-kernel exit timing statistics](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=73e75b416ffcfa3a84952d8e389a0eca080f00e1)
- [KVM: support device deassignment](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0a920356748df4fb06e86c21c23d2ed6d31d37ad)
- [KVM: use the new intel iommu APIs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=260782bcfdaaa7850f29d6bb2ec6603019168c57)
- [KVM: VMX: Add PAT support for EPT](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=468d472f3f65100d5fb88c8d45043c85b874c294)
- [KVM: VMX: Provide support for user space injected NMIs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=487b391d6ea9b1d0e2e0440466fb3130e78c98d9)
- [KVM: x86 emulator: add Src2 decode set](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0dc8d10f7d848b63c8d32cf6fd31ba7def792ac9)
- [KVM: x86 emulator: Extend the opcode descriptor](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=45ed60b371aeae6ed80f7e9d594a5e6412edc176)
- [KVM: x86: Support for user space injected NMIs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c4abb7c9cde24b7351a47328ef866e6a2bbb1ad0)
- [select IOMMU_API when DMAR and/or AMD_IOMMU is selected](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1aaf118352b85bb359ce28070bcc478f659a7031)
- [x86: vmware: look for DMI string in the product serial key](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fd8cd7e1919fc1c27fe2fdccd2a1cd32f791ef0f)

**Architecture**

*Generic*

- [CVE-2009-0029: Convert all system calls to return a long](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2ed7c03ec17779afb4fcfa3b8c61df61bd4879ba)
- [CVE-2009-0029: Make sys_pselect7 static](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c9da9f2129d6a421c32e334a83770a9e67f7feac)
- [CVE-2009-0029: Make sys_syslog a conditional system call](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f627a741d24f12955fa2d9f8831c3b12860635bd)
- [CVE-2009-0029: Move compat system call declarations to compat header file](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4c696ba7982501d43dea11dbbaabd2aa8a19cc42)
- [CVE-2009-0029: powerpc: Enable syscall wrappers for 64-bit](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ee6a093222549ac0c72cfd296c69fa5e7d6daa34)
- [CVE-2009-0029: Remove \_\_attribute\_\_((weak)) from sys_pipe/sys_pipe2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1134723e96f6e2abcf8bfd7a2d1c96fcc323ef35)
- [CVE-2009-0029: Rename old_readdir to sys_old_readdir](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e55380edf68796d75bf41391a781c68ee678587d)
- [CVE-2009-0029: s390: enable system call wrappers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ed6bb6194350dc6ae97a65dbf2d621a3dbe6bbe9)
- [CVE-2009-0029: s390 specific system call wrappers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=26689452f5ca201add63b1b1ff0dbcf82d6885e7)
- [CVE-2009-0029: sparc: Enable syscall wrappers for 64-bit](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=67605d6812691bbd2158d2f60259e0407611bc1b)
- [CVE-2009-0029: System call wrapper infrastructure](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1a94bc34768e463a93cb3751819709ab0ea80a01)
- [CVE-2009-0029: System call wrappers part 01](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=58fd3aa288939d3097fa04505b25c2f5e6e144d1)
- [CVE-2009-0029: System call wrappers part 02](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=dbf040d9d1cbf1ef6250bdb095c5c118950bcde8)
- [CVE-2009-0029: System call wrappers part 03](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ae1251ab785f6da87219df8352ffdac68bba23e4)
- [CVE-2009-0029: System call wrappers part 04](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b290ebe2c46d01b742b948ce03f09e8a3efb9a92)
- [CVE-2009-0029: System call wrappers part 05](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=362e9c07c7220c0a78c88826fc0d2bf7e4a4bb68)
- [CVE-2009-0029: System call wrappers part 06](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5add95d4f7cf08f6f62510f19576992912387501)
- [CVE-2009-0029: System call wrappers part 07](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=754fe8d297bfae7b77f7ce866e2fb0c5fb186506)
- [CVE-2009-0029: System call wrappers part 08](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=17da2bd90abf428523de0fb98f7075e00e3ed42e)
- [CVE-2009-0029: System call wrappers part 09](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a5f8fa9e9ba5ef3305e147f41ad6e1e84ac1f0bd)
- [CVE-2009-0029: System call wrappers part 10](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=bdc480e3bef6eb0e7071770834cbdda7e30a5436)
- [CVE-2009-0029: System call wrappers part 11](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=257ac264d69017270fbc3cf5536953525db4076c)
- [CVE-2009-0029: System call wrappers part 12](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=64fd1de3d821659ac0a3004fd5ee1de59e64af30)
- [CVE-2009-0029: System call wrappers part 13](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6a6160a7b5c27b3c38651baef92a14fa7072b3c1)
- [CVE-2009-0029: System call wrappers part 14](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3480b25743cb7404928d57efeaa3d085708b04c2)
- [CVE-2009-0029: System call wrappers part 15](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a26eab2400f0477bfac0255600552394855016f7)
- [CVE-2009-0029: System call wrappers part 16](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=002c8976ee537724b20a5e179d9b349309438836)
- [CVE-2009-0029: System call wrappers part 17](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ca013e945b1ba5828b151ee646946f1297b67a4c)
- [CVE-2009-0029: System call wrappers part 18](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a6b42e83f249aad723589b2bdf6d1dfb2b0997c8)
- [CVE-2009-0029: System call wrappers part 19](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=003d7ab479168132a2b2c6700fe682b08f08ab0c)
- [CVE-2009-0029: System call wrappers part 20](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3cdad42884bbd95d5aa01297e8236ea1bad70053)
- [CVE-2009-0029: System call wrappers part 21](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=20f37034fb966a1c35894f9fe529fda0b6440101)
- [CVE-2009-0029: System call wrappers part 22](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3e0fa65f8ba4fd24b3dcfaf14d5b15eaab0fdc61)
- [CVE-2009-0029: System call wrappers part 23](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5a8a82b1d306a325d899b67715618413657efda4)
- [CVE-2009-0029: System call wrappers part 24](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e48fbb699f82ef1e80bd7126046394d2dc9ca7e6)
- [CVE-2009-0029: System call wrappers part 25](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d5460c9974a321a194aded4a8c4daaac68ea8171)
- [CVE-2009-0029: System call wrappers part 26](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c4ea37c26a691ad0b7e86aa5884aab27830e95c9)
- [CVE-2009-0029: System call wrappers part 27](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1e7bfb2134dfec37ce04fb3a4ca89299e892d10c)
- [CVE-2009-0029: System call wrappers part 28](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=938bb9f5e840eddbf54e4f62f6c5ba9b3ae12c9d)
- [CVE-2009-0029: System call wrappers part 29](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2e4d0924eb0c403ce4014fa139d1d61bf2c44fee)
- [CVE-2009-0029: System call wrappers part 30](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6559eed8ca7db0531a207cd80be5e28cd6f213c5)
- [CVE-2009-0029: System call wrappers part 31](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=836f92adf121f806e9beb5b6b88bd5c9c4ea3f24)
- [CVE-2009-0029: System call wrappers part 32](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d4e82042c4cfa87a7d51710b71f568fe80132551)
- [CVE-2009-0029: System call wrappers part 33](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2b66421995d2e93c9d1a0111acf2581f8529c6e5)
- [CVE-2009-0029: System call wrapper special cases](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6673e0c3fbeaed2cd08e2fd4a4aa97382d6fedb0)
- [byteorder: make swab.h include asm/swab.h like a regular header](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=74d96f018673759d04d032c137d132f6447bfb1e)

*Generic â€“ Cpumasks*

- [cpumask: Add alloc_cpumask_var_node()](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=7b4967c532045a1983d6d4af5c69cc7c5109f62b)
- [cpumask: Add CONFIG_CPUMASK_OFFSTACK](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=aab46da0520af9c99b7802cebe4f14a81ff39415)
- [cpumask: add sysfs displays for configured and disabled cpu maps](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e057d7aea9d8f2a46cd440d8bfb72245d4e72d79)
- [cpumask: centralize cpu_online_map and cpu_possible_map](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=98a79d6a50181ca1ecf7400eda01d5dc1bc0dbf0)
- [cpumask: CONFIG_DISABLE_OBSOLETE_CPUMASK_FUNCTIONS](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8c384cdee3e04d6194a2c2b192b624754f990835)
- [cpumask: convert shared_cpu_map in acpi_processor \* structs to cpumask_var_t](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2fdf66b491ac706657946442789ec644cc317e1a)
- [cpumask: documentation for cpumask_var_t](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ec26b805879c7e77865b39ee91b737985e80006d)
- [cpumask: fix CONFIG_NUMA=y sched.c](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=62ea9ceb17a74bc7544211bfeecf4170c554ac4f)
- [cpumask: Introduce cpumask_of\_{node,pcibus} to replace {node,pcibus}\_to_cpumask](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f0b848ce6fe9062d504d997e9e97fe0f87d57217)
- [cpumask: Introduce topology_core_cpumask()/topology_thread_cpumask(): ia64](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=333af15341b2f6cd813c054e1b441d7b6d8e9318)
- [cpumask: Introduce topology_core_cpumask()/topology_thread_cpumask(): powerpc](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9150641dd17fe9e213ab3391c8ebfc228daa2d9d)
- [cpumask: Introduce topology_core_cpumask()/topology_thread_cpumask(): s390](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2bb23a63f22f0e2d91fee93ff5ca9c29e180b146)
- [cpumask: Introduce topology_core_cpumask()/topology_thread_cpumask(): sparc](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=78fd744f827586615da5b387fa9f0af1888601b6)
- [cpumask: make CONFIG_NR_CPUS always valid.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=278d1ed65e25d80af7c3a112d707b3f70516ddb4)
- [cpumask: sh: Introduce cpumask_of\_{node,pcibus} to replace {node,pcibus}\_to_cpumask](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=7479a2939df4957ba794cce814379b6d10914bdc)
- [cpumask: switch over to cpu_online/possible/active/present_mask: core](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b3199c025d1646e25e7d1d640dd605db251dccf8)
- [cpumask: Use accessors code in core](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=915441b601e6662e79f6c958e7be307967a96977)
- [sysfs: add documentation to cputopology.txt for system cpumasks](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d62720ade82c5e5b8f9585e5ed02c89573ebf111)
- [x86 smp: modify send_IPI_mask interface to accept cpumask_t pointers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e7986739a76cde5079da08809d8bbc6878387ae0)
- [x86: Update io_apic.c to use new cpumask API](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=22f65d31b25a320a5246592160bcb102d2791c45)

*ARM*

- [Add basic support for MX31PDK board.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1553a1ec833ddda51d57f66f8e00904b64b954c8)
- [Add default configuration for MX31PDK board.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=46c3d567af21cba107fef37b88a0d6ec6c35842f)
- [ARM: 5290/1: \[AT91](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ffc63b7d30370e23d7e052df2c1c2c4526464ba6) Add support for the Adeneo NeoCore 926 board\]
- [ARM: 5319/1: AT91: support AT91CAP9 revC CPUs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=7be90a6ba996e43902fc89704b60a57fd4659a63)
- [ARM: 5338/1: Add Nuvoton W90P910 Platform support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=7ec80ddf0455ff3854a5ca524952d91b5eb676b2)
- [ARM: Arrange for platforms to select appropriate CPU support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c750815e2d436f4379c7af8a8770ef2ae71c5607)
- [ARM: clps7500: remove support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=635f0258e5ae526034486b4ae9020e64bfb7d27e)
- [ARM: CPUFREQ: S3C24XX serial CPU frequency scaling support.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=305554768011707f33f437b96f999f812ba2a7e4)
- [ARM: DSM320: Add support for the DSM320](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6174dee5146dc2c7eca8f103b85be168dc564ffb)
- [ARM: MX2 pcm038: add 1-wire master support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d40a09920be4d64414c3e5396c6399ac96ad0e00)
- [ARM: MX31: basic support for mx31moboard platform](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=988d2d49f767c2e9c5a082257ec4ca2ff30c2b68)
- [ARM: OMAP3: Add basic support for Pandora handheld console](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=da177247e89c672fc910cbbc4e24d7d578e2e0b2)
- [ARM: OMAP3: LDP: Add Ethernet device support to make ldp boot succeess](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b1c056d20caa6fdd3481b348567f1f91e98aaa4b)
- [ARM: pcm037: add 1wire support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d517cab1c7fc92178e11c7ded2548b06b273d293)
- [ARM: pcm037: add support for the on-board LAN9217 network controller](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ba54b95899838610c8c23fb7ab88831016b81fb3)
- [ARM: pxa: add basic support for HP iPAQ h5000](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=bc2fd1c09c226ea47ab8301cde6dbcf9e5c78b73)
- [ARM: pxa/MioA701: add camera support for Mio A701 board.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8e7ccddf0fd22617a3edc28ab2ce2fac0fb94823)
- [ARM: S3C64XX: Basic CPU detection and map initialisation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=beda30f6a9c5f8e1eebd195019a537057cc556fd)
- [i.MX31: framebuffer driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=86528da229a448577a8401a17c295883640d336c)
- [i.MX31: Image Processing Unit DMA and IRQ drivers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5296b56d1b2000b60fb966be161c1f8fb629786b)

*Blackfin*

- [Blackfin arch: Add BF537-STAMP platform support for ENC28J60 SPI Ethernet MAC](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=85a192e92dcb67552ee3fcdf2e36c11688b61955)
- [Blackfin arch: Add document about bfin-gpio](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5e6d9f511e0188d34fa7a93ce2d0e6194442b0da)
- [Blackfin arch: add support for Blackfin latest processor family BF51x](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2f6f4bcdd611cb968b800f7569c4383727856668)
- [Blackfin arch: BF538/9 Linux kernel Support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=dc26aec25d1a4e2690df166dbe843344728994ce)
- [Blackfin arch: change HWTRACE Kconfig and set it on default](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e60cb8a9eb2d76ac072a45112dfaf365837d86aa)
- [Blackfin arch: Cleanup and unify Blackfin IRQ and GPIO IRQ handling](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8d0223744f531168d4ae87f33354d12a50402779)
- [Blackfin arch: Enable ISP1760 USB Host Driver in platform device initialization code.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3f37569044cb3d9ba4722710b84d018f573d4b0e)
- [Blackfin arch: Faster C implementation of no-MPU CPLB handler](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=dbdf20db537a5369c65330f878ad4905020a8bfa)
- [Blackfin arch: merge adeos blackfin part to arch/blackfin/](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6a01f230339321292cf065551f8cf55361052461)
- [Blackfin arch: smp patch cleanup from LKML review](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=dbc895f95500a73ebf1ff12fe85f2e2b3790f52f)
- [Blackfin arch: SMP supporting patchset: BF561 related code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c51b4488cd5bff08ed5690a8f303ff7f0894da2a)
- [Blackfin arch: SMP supporting patchset: Blackfin CPLB related code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b8a989893cbdeb6c97a7b5af5f38fb0e480235f9)
- [Blackfin arch: SMP supporting patchset: Blackfin header files and machine common code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6b3087c64a92a36ae20d33479b4df6d7afc910d4)
- [Blackfin arch: SMP supporting patchset: Blackfin kernel and memory management code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8f65873e47784a390949f0d61e5692dbf2a8253e)
- [Blackfin arch: SMP supporting patchset: some other misc code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=46fa5eecec58934902ea4a65d9c7b7a486ac6f6b)

*MIPS*

- [MIPS: Add Cavium OCTEON cop2/cvmseg state entries to processor.h.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b5e00af81f298f4ba2e41325042a7ce1ec022b1d)
- [MIPS: Add Cavium OCTEON processor constants and CPU probe.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0dd4781bca56871434507ed35d5bb8ef92077907)
- [MIPS: Add Cavium OCTEON processor CSR definitions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=54293ec3074a5fe61abd297502f68b2529a3dab3)
- [MIPS: Add Cavium OCTEON processor support files to arch/mips/cavium-octeon.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5b3b16880f404ca54126210ca86141cceeafc0cf)
- [MIPS: Add Cavium OCTEON processor support files to arch/mips/cavium-octeon/executive and asm/octeon.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=58f07778ce9d32c22cecb1d8ef348001f0e705c9)
- [MIPS: Add Cavium OCTEON slot into proper tlb category.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ec454d8c4fee3b2feb87e594d806c0987c5dd538)
- [MIPS: Add Cavium OCTEON specific register definitions to mipsregs.h](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ed918c2daf9ef4c3b52f75736c3a652e5160c8ad)
- [MIPS: Add Cavium OCTEON specific registers to ptrace.h and asm-offsets.c](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=babed555695fad25820fb5fb0b5068c56e375900)
- [MIPS: Add Cavium OCTEON to arch/mips/Kconfig](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a86c7f72454c4e855d5d6c80ed9f7f2ac55b001a)
- [MIPS: Add defconfig for Cavium OCTEON.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=551d9304de60229080b5bf97230728c1c1bc8260)
- [MIPS: Add SMP_ICACHE_FLUSH for the Cavium CPU family.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ddcdb1b4a46915b70dce3af3a78582b3ca79cf76)
- [MIPS: Alchemy: devboards: consolidate files](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=23ba25d56606eec6fabc37c1efcbd48837dc9adc)
- [MIPS: Alchemy: Move development board code to common subdirectory](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=58e75e86cf9af1130b3c628d924e6df0bc72832f)
- [MIPS: Alchemy: new userspace suspend interface for development boards.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=61f9c58da57a80b0df1ced18a28cbbaebd4d417a)
- [MIPS: Alchemy: RTC counter clocksource / clockevent support.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0c694de12b54fa96b9555e07603f567906ce21c8)
- [MIPS: Alchemy: update core interrupt code.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=785e3268e2951d4c0c21417c8e5d8004b2ab2480)
- [MIPS: IP27: Switch from DMA_IP27 to DMA_COHERENT](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=634286f127bef8799cd04799d3e1d5471e8fd91c)
- [MIPS: Use hardware watchpoints on all R1 and R2 CPUs.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f839490ab42a471f0b0a4b795df77a1af924fe05)

*Power*

- [powerpc/85xx: Enable SMP support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=00c4b95c44692f84b565cfea0af582c0677acaa7)
- [powerpc: Change u64/s64 to a long long integer type](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fe333321e2a71f706b794d55b6a3dcb5ab240f65)
- [powerpc/mm: Introduce MMU features](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=7c03d653cd257793dc40520c94e229b5fd0578e7)
- [powerpc/oprofile: IBM CELL: add SPU event profiling support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=883823291d22e06736f1056da6d8303291d6bbf9)
- [powerpc: Rewrite sysfs processor cache info code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=93197a36a9c16a85fb24cf5a8639f7bf9af838a3)
- [Update powerpc maintainers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=92cde4d5396c3b6cbf3192286b687f97a889dffe)

*S390*

- [S390: hvc_iucv: Update function documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=17e19f04ac73df05854ba2e7e945d51c494a3011)
- [S390: improve idle cputime accounting](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9cfb9b3c3a7361c793c031e9c3583b177ac5debd)
- [S390: introduce vdso on s390](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b020632e40c3ed5e8c0c066d022672907e8401cf)
- [S390: update documentation for hvc_iucv kernel parameter.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=555d61d6542d51563e50532ff604dcd31c96fb24)

*SH*

- [doc: Update sh cpufreq documentation.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8a655053ca1593dd160dac2a4ee638fdec037d86)
- [sh: Add platform-specific constants for SH7709](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8085ac753164f45fd23603e7cad85a4c985cbf75)
- [sh: Add support for SH7201 CPU subtype.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2825999e8a9bd7ab7e25a7e7475c7cdd10371a13)
- [sh: allow CONFIG_CPU_IDLE](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c6f17cb2272121475c87592560534b157b17544e)
- [sh: allow CONFIG_PM](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=af998a9a0ae3291e86ddcae8e196a1cbf82c2457)
- [sh: Generic kgdb stub support.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ab6e570ba33dbee18c2520d386e0f367a9b573c3)
- [sh: sh7760fb: Add support SH7720/SH7721 of Renesas](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5c72f303a2b7862dbba79f4176ddc922a440b567)

*SPARC*

- [MAINTAINERS: update sparc maintainer](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=473321fc373e712fbb9b88e2c0736e55fddadab8)
- [sparc64: Use unsigned long long for u64.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9018113649348c689da107166c05d436cd52e7bf)
- [sparc,sparc64: unify Kconfig files](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=26b4c912185a8902b0990166892d53be78ef8cfc)
- [sparc,sparc64: unify kernel/](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a88b5ba8bd8ac18aad65ee6c6a254e2e74876db3)
- [sparc,sparc64: unify Makefile](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5e53879008b9acefe9f43498fd36db7376e08739)
- [sparc: Use 64BIT config entry](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=761b602620b4627dbd8f1b0bd2896022dc168a6d)

*x86*

- [Documentation/x86/boot.txt: payload length was changed to payload_length](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2f6de3a199893ae3dd68e23bd79b55e1478c8268)
- [pci: add PCI IDs for devices that need boot irq quirks](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=747ada36ee23225d81657e4d633ac93b8ccbea7d)
- [x86, 64-bit: update address space documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a4c52791fa8c73e3cffe4a82865edb41e8fe8c3c)
- [x86-64: seccomp: fix 32/64 syscall hole](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5b1017404aea6d2e552e991b3fd814d839e9cd67)
- [x86-64: syscall-audit: fix 32/64 syscall hole](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ccbe495caa5e604b04d5a31d7459a6f6a76a756c)
- [x86: add cache descriptors for Intel Core i7](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9a8ecae87a2b698964b1db9ea504ba1099f479fc)
- [x86: add Dell XPS710 reboot quirk](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=dd4124a8a06bca89c077a16437edac010f0bb993)
- [x86: add memory hotremove config option](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3555105333ae55414d0fe051557bd7dc590f5255)
- [x86: add X86_FEATURE_HYPERVISOR feature bit](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=49ab56ac6e1b907b7dadb72a4012460359feaf0e)
- [x86: APIC: enable workaround on AMD Fam10h CPUs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=858770619debfb9269add63e4ba8b7c6b5538dd1)
- [x86, apm: remove CONFIG_APM_REAL_MODE_POWER_OFF in favor of a kernel parameter](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8daa19051e1c7369c89ace7b18e74fe1f55dfa29)
- [x86, bts: base in-kernel ds interface on handles](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ca0002a179bfa532d009a9272d619732872c49bd)
- [x86, bts: provide in-kernel branch-trace interface](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c2724775ce57c98b8af9694857b941dc61056516)
- [x86: change OPTIMIZE_INLINING help to say enabling makes smaller kernels](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=63fb70859f987f2b3b8028fa467fd63336315e9c)
- [x86: cleanup remaining cpumask_t ops in smpboot code](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c2d1cec1c77f7714672c1efeae075424c929e0d5)
- [x86: default to SWIOTLB=y on x86_64](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a1afd01c175324656d0e8f1c82ea94b474953c04)
- [x86: enable cpus display of kernel_max and offlined cpus](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=730cf27246225d56ca1603b2f3c4fdbf882d4e51)
- [x86: enable MAXSMP](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=36f5101a60de8f79c0d1ca06e50660bf5129e02c)
- [x86, mm: enable GBPAGES option by default](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9e899816d126cc6f7d405c349f65363214fe7399)
- [x86: MSI start irq numbering from nr_irqs_gsi](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=be5d5350a937cd8513b258739f1099420129e96f)
- [x86: offer frame pointers in all build modes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=da4276b8299a6544dc41ac2485d3ffca5811b3fb)
- [x86: only scan the root bus in early PCI quirks](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8659c406ade32f47da2c95889094801921d6330a)
- [x86/oprofile: fix pci_dev use count for AMD northbridge devices](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=83bd9243956f30d91851b272988a237999b35b10)
- [x86: PAT: update documentation to cover pgprot and remap_pfn related changes - v3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a2ced6e173e0c93870f79856e97825f4e180891e)
- [x86, pci: introduce config option for pci reroute quirks (was: PATCH 0/3 Boot IRQ quirks for Broadcom and AMD/ATI)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=41b9eb264c8407655db57b60b4457fe1b2ec9977)
- [x86, pci: introduce pci=ioapicreroute kernel cmdline option](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9197979b518573999d52d9e85bce1680682ed85c)
- [x86, pci: introduce pci=noioapicquirk kernel cmdline option](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a9322f6488b432ddc1e89be88242c827c633fb63)
- [x86: remove init_mm export as planned for 2.6.26](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9470565579f29486f4ed0ffa50774268b64994b0)
- [x86: Set CONFIG_NR_CPUS even on UP](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=78637a97b7fe1df51f40a460448df0b93d511176)
- [x86: some lock annotations for user copy paths](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c10d38dda1774ed4540380333cabd229eff37094)
- [x86: some lock annotations for user copy paths, v2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3ee1afa308f2a38e5d1e2ad3752ad7abcf480da1)
- [x86: some lock annotations for user copy paths, v3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1d18ef489509314506328b9e464dd47c24c1d68f)
- [x86, sparseirq: clean up Kconfig entry](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=973656fe1afb4adf95d7b9ab75d4660cd3821ea1)
- [x86: support always running TSC on Intel CPUs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=40fb17152c50a69dc304dd632131c2f41281ce44)
- [x86: turn CONFIG_SPARSE_IRQ off by default](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4e17fee24a39448f3a20e9cf98887b7665825848)
- [x86: update CONFIG_NUMA description](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fd51b2d7d5df932767b89e00d0871a38a2c53e74)
- [x86: use NR_IRQS_LEGACY](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=99d093d12897562a253540a902bbf65ec16042ac)
- [x86: use possible_cpus=NUM to extend the possible cpus allowed](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3b11ce7f542e415c90267b4482d4611410b468e6)

*Miscellaneous*

- [avr32: Hammerhead board support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=dd5e1339e528197abdb7827663ff0673797fa088)
- [IA64: enable setting DMAR on by default](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6b1ff036d4cde7834ef2f9dbea5747adaaac24e0)
- [xtensa: Add xt2000 support files.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8fa5723aa7e053d498336b48448b292fc2e0458b)

**mm**

- [Fix page writeback thinko, causing Berkeley DB slowdown](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3a4c6800f31ea8395628af5e7e490270ee5d0585)
- [memcg: explain details and test document](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9836d89191edd4887ed026a9ce53d9dfac62ec1c)
- [memcg: fix swap accounting leak](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=03f3c433648a97ae7c86be789edba67690f6ea60)
- [memcg: handle swap caches](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d13d144309d2e5a3e6ad978b16c1d0226ddc9231)
- [memcg: introduce charge-commit-cancel style of functions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=7a81b88cb53e335ff7d019e6398c95792c817d93)
- [memcg: memory cgroup hierarchy documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=52bc0d82100cd896213a9a25ec01c1ba87b939db)
- [memcg: mem+swap controller core](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8c7c6e34a1256a5082d38c8e9bd1474476912715)
- [memcg: mem+swap controller Kconfig](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c077719be8e9e6b55702117513d1b5f41d80404a)
- [memcg: move all acccounting to parent at rmdir()](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f817ed48535ac6510ebae7c4116f24a5f9268834)
- [memcg: new force_empty to free pages under group](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c1e862c1f5ad34771b6d0a528cf681e0dcad7c86)
- [memcg: show reclaim stat](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=7f016ee8b6a9a43f768e6252021f169abec4fa1f)
- [memcg: swappiness](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a7885eb8ad465ec9db99ac5b5e6680f0ca8e11c8)
- [memcg: synchronized LRU](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=08e552c69c6930d64722de3ec18c51844d06ee28)
- [mm: add_active_or_unevictable into rmap](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b5934c531849ff4a51ce0f290141efe564290e40)
- [mm: add add_to_swap stub](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=60371d971a3d01afd102f0bbf2681f32ecc31d78)
- [mm: add dirty_background_bytes and dirty_bytes sysctls](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2da02997e08d3efe8174c7a47696e6f7cbe69ba9)
- [mm: add Set,ClearPageSwapCache stubs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6d91add09f4bad5f4d4233b13faa392f0c4b16be)
- [mm: direct IO starvation improvement](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=48b47c561e41525061b5bc0cfd67d6367fd11dc4)
- [mm: further cleanup page_add_new_anon_rmap](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=cbf84b7add8103b92aaa84928e335df726bfc8da)
- [mm: OOM documentation update](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9e9e3cbc62da43c66e894d5a61fa08b427e25202)
- [mm: optimize get_scan_ratio for no swap](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b962716b459505a8d83aea313fea0abe76749f42)
- [mm: remove gfp_mask from add_to_swap](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ac47b003d03c2a4f28aef1d505b66d24ad191c4f)
- [mm: remove try_to_munlock from vmscan](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=63d6c5ad7fc27455ce5cb4706884671fb7e0df08)
- [mm: report the MMU pagesize in /proc/pid/smaps](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3340289ddf29ca75c3acfb3a6b72f234b2f74d5c)
- [mm: report the pagesize backing a VMA in /proc/pid/smaps](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=08fba69986e20c1c9e5fe2e6064d146cc4f42480)
- [mm: show node to memory section relationship with symlinks in sysfs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c04fc586c1a480ba198f03ae7b6cbd7b57380b91)
- [mm: vmalloc make lazy unmapping configurable](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=cd52858c73f9f7df859a08fb08496ca39b9b3d8d)
- [NOMMU: Make mmap allocation page trimming behaviour configurable.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=dd8632a12e500a684478fea0951f380478d56fed)
- [NOMMU: Make VMAs per MM as for MMU-mode linux](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8feae13110d60cc6287afabc2887366b0eb226c2)
- [NOMMU: Support XIP on initramfs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=cb6ff208076b5f434db1b8c983429269d719cef5)
- [Remove obsolete CONFIG_RESOURCES_64BIT](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=67faaada1ebcccf29745346f1d7cb5392f46500a)
- [shmem: unify regular and tiny shmem](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=853ac43ab194f5051b27a55060215d696dc9480d)
- [vmscan: improve reclaim throughput to bail out patch](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=01dbe5c9b1004dab045cb7f38428258ca9cddc02)

**Miscellaneous**

- [allow stripping of generated symbols under CONFIG_KALLSYMS_ALL](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9bb482476c6c9d1ae033306440c51ceac93ea80c)
- [bitmap: find_last_bit()](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ab53d472e785e51fdfc08fc1d66252c1153e6c0f)
- [checkpatch: Add warning for p0-patches](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1e85572697b348b1a126520349a29654f2ae6a12)
- [debug: add notifier chain debugging](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1b2439dbb703ae8d95a9ce7ece6b7800b80f41f0)
- [debugobjects: add boot parameter default value](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3ae7020543db0b769538e64d1ce8d51fceff60ca)
- [do_mounts: add device info to mount message](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=bca1033b092a6fab2ed00036e8a7f6e2df5d99a2)
- [driver core: add root_device_register()](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0aa0dc41bfd993491c2344870eee7a3b218551fb)
- [file capabilities: add no_file_caps switch (v4)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1f29fae29709b4668979e244c09b2fa78ff1ad59)
- [fix modules_install via NFS](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8b249b6856f16f09b0e5b79ce5f4d435e439b9d6)
- [kbuild: introduce \$(kecho) convenience echo](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5410ecc0def8955ab99810c5626cc7e156991896)
- [kbuild: reintroduce ALLSOURCE_ARCHS support for tags/cscope](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4f628248a578585472e19e4cba2c604643af8c6c)
- [kbuild: strip generated symbols from \*.ko](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ad7a953c522ceb496611d127e51e278bfe0ff483)
- [kbuild: use KECHO convenience echo](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fd54f502841c1caa7cfd5af564aad1bd017371fa)
- [kconfig: add script to manipulate .config files on the command line](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8e54701ea85b0ab0971637825a628f5aa2b678a4)
- [kconfig: improve error messages for bad source statements](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=7826005e5a53645d7aab7c13eda76126eadebf0b)
- [LOCKD: Make lockd_up() and lockd_down() exported GPL-only](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2de59872a7842143f4507832e7c1f5123c47feb7)
- [lockstat: contend with points](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c7e78cff6b7518212247fb20b1dc6411540dc9af)
- [module: add MODULE_STATE_LIVE notify](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0deddf436a37c18ceb26c6e3b632fb9b5f58a0c1)
- [modules: Use a better scheme for refcounting](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=720eba31f47aeade8ec130ca7f4353223c49170f)
- [NFS: add "no resvport" mount option](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d740351bf0960e89ce1aef45cfe00167cb0f9e5b)
- [NFS: "no resvport" mount option changes mountd client too](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=50a737f86dbf99daf3a8dcbdf778a3be36bb2a39)
- [oops: increment the oops UUID every time we oops](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d6624f996ae539344e8d748cce1117ae7af06fbf)
- [PATCH: fast vdso implementation for CLOCK_THREAD_CPUTIME_ID](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c742b31c03f37c5c499178f09f57381aa6c70131)
- [PATCH: idle cputime accounting](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=79741dd35713ff4f6fd0eafd59fa94e8a4ba922d)
- [PATCH: improve precision of idle time detection.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6f43092441bda528dd38f2dc6c1e2522c5079fb7)
- [PATCH: improve precision of process accounting.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=aa5e97ce4bbc9d5daeec16b1d15bb3f6b7b4f4d4)
- [proc: add /proc/\*/stack](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2ec220e27f5040aec1e88901c1b6ea3d135787ad)
- [proc: stop using BKL](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b4df2b92d8461444fac429c75ba6e125c63056bc)
- [regulator: sysfs attribute reduction (v2)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=7ad68e2f970fd84d15ad67ce3216aed05f944a9c)
- [resource: allow MMIO exclusivity for device drivers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e8de1481fd7126ee9e93d6889da6f00c05e1e019)
- [RTC: Remove the BKL.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=048cd5888f81713af4597bde5815f32d58fdf5b0)
- [Sanitize gcc version header includes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f153b82121b0366fe0e5f9553545cce237335175)
- [scripts: script from kerneloops.org to pretty print oops dumps](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=5aea50b5c76b07f2b6bda3426dba998156eaf6d0)
- [setlocalversion: add git-svn support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ff80aa97c9b4aae9449a608fe1bc3e7b5121cd66)
- [slab: introduce kzfree()](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3ef0e5ba467366125f04b423f4638baca54a4fc1)
- [SLUB: failslab support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=773ff60e841461cb1f9374a713ffcda029b8c317)
- [softlockup: increase hung tasks check from 2 minutes to 8 minutes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fb822db465bd9fd4208eef1af4490539b236c54e)
- [sparse irq_desc array: core kernel and x86 changes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0b8f1efad30bd58f89961b82dfe68b9edf8fd2ac)
- [swiotlb: add support for systems with highmem](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fb05a37929e0cd99016b4f5e5a5ef077fb10a947)
- [sysfs: clarify SYSFS_DEPRECATED help text](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fce3e804cfad49208fd2ff9db4bcb57481409e1d)
- [timers: split process wide cpu clocks/timers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4cd4c1b40d40447fb5e7ba80746c6d7ba91d7a53)
- [trivial: Update MAINTAINERS entry](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2b6a2f535dda8c60721b78699618d13d6799a29e)
- [UIO: Pass information about ioports to userspace (V2)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e70c412ee45332db2636a8f5a35a0685efb0e4aa)

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at The H Open Source:*

- [Kernel Log: What's new in 2.6.29 - Part 7: Audio, FireWire, USB, Video and more](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-7-Audio-FireWire-USB-Video-and-more-740561.html)
- \[ticker:uk_122832 Kernel Log: What's new in 2.6.29 - Part 6: Storage, IDE/PATA, SCSI\]
- [Kernel Log: What's new in 2.6.29 - Part 5: Filesystems Btrfs, SquashFS, Ext4 without journaling](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-5-Filesystems-Btrfs-SquashFS-Ext4-without-journaling-740499.html)
- [Kernel Log: Morton questions acceptance of Xen Dom0 code; file systems for SSDs](../site/news/item/Kernel-Log-Morton-questions-acceptance-of-Xen-Dom0-code-file-systems-for-SSDs-740375.html)
- [Kernel Log: Stable series development is speeding up, X Server 1.6 available soon](../site/news/item/Kernel-Log-Stable-series-development-is-speeding-up-X-Server-1-6-available-soon-740203.html "Kernel Log: Stable series development is speeding up, X Server 1.6 available soon â 23 February 2009, 10:46")
- [Kernel Log: What's new in 2.6.29 - Part 4: ACPI, PCI, PM â€“ notebooks and power saving improvements](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-4-ACPI-PCI-PM-notebooks-and-power-saving-improvements-739889.html "Kernel Log: What's new in 2.6.29 - Part 4: ACPI, PCI, PM – notebooks and power saving improvements â 31 January 2009, 15:01")
- [Kernel Log: New stable kernels, AMD 3D documentation and Mesa 7.3 released](../site/news/item/Kernel-Log-New-stable-kernels-AMD-3D-documentation-and-Mesa-7-3-released-739845.html "Kernel Log: New stable kernels, AMD 3D documentation and Mesa 7.3 released â 28 January 2009, 11:41")
- [Kernel Log: What's new in 2.6.29 - Part 3: Kernel controlled graphics modes](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-3-Kernel-controlled-graphics-modes-739697.html "Kernel Log: What's new in 2.6.29 - Part 3: Kernel controlled graphics modes â 17 January 2009, 07:36")
- [Kernel Log: main development phase for 2.6.29 ends, new X.org drivers](../site/news/item/Kernel-Log-main-development-phase-for-2-6-29-ends-new-X-org-drivers-739633.html "Kernel Log: main development phase for 2.6.29 ends, new X.org drivers â 12 January 2009, 17:09")
- [Kernel Log: What's new in 2.6.29 - Part 2: WiMax](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-2-WiMAX-739621.html "Kernel Log: What's new in 2.6.29 - Part 2: WiMAX â 12 January 2009, 10:19")
- [Kernel Log: What's new in 2.6.29 - Part 1: Dodgy Wifi drivers and AP support](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-1-Dodgy-Wifi-drivers-and-AP-support-739619.html "Kernel Log: What's new in 2.6.29 - Part 1: Dodgy Wifi drivers and AP support â 11 January 2009, 16:08")

*Older Kernel logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
