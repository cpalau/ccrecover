---
title: "Kernel Log: What's new in 2.6.29 - Part 4: ACPI, PCI, PM – notebooks and power saving improvements"
date: 2009-01-31
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-4-ACPI-PCI-PM-notebooks-and-power-saving-improvements-739889.html
pages: 1
---

# Kernel Log: What's new in 2.6.29 - Part 4: ACPI, PCI, PM – notebooks and power saving improvements

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/6/3/2/1/93e8ea3d0acdf147.jpg) Following a one-week pause due to the [LCA 2009](http://linux.conf.au/), Linus Torvalds restarted the integration of patches into the development branch a few days ago, and has now [released the third pre-release version of 2.6.29](http://thread.gmane.org/gmane.linux.kernel/786678). In his release email, Torvalds points out a few changes made to improve the reliability of the system: suspend modes – changes that allow one of his notebooks to wake up reliably from power-saving mode. Our "What's new in 2.6.29" Kernel Log takes this opportunity to discuss the changes that concern ACPI, PCI, power management and the corresponding notebook drivers expected for 2.6.29.

### Reinitialised

The changes to the handling of the suspend and resume modes, mentioned by Torvalds and mainly developed by Rafael J. Wysocki, weren't integrated in one go, but found their way into the kernel ([1](http://thread.gmane.org/gmane.linux.kernel.pci/2620), [2](http://thread.gmane.org/gmane.linux.acpi.devel/36731)) gradually via the maintainers of the ACPI and PCI subsystems. Most of the relevant commits are comparatively small and seem rather inconspicuous at first glance (for example [1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=adf094931ffb25ef4b381559918f1a34181a5273), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d67e37d7933ba3b28a63ff38c957e433aaca5dc4), [3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=98e6e286d7b01deb7453b717aa38ebb69d6cefc0), [4](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=90d25f246ddefbb743764f8d45ae97e545a6ee86)).

These changes, which have been [in preparation for a long time](http://lwn.net/Articles/274008/), are to allow the kernel to reliably re-initialise the system's PCI(e) hardware when waking up from suspend mode. [According to Torvalds](http://thread.gmane.org/gmane.linux.kernel/786678), suspend and resume have worked on many systems, but haven't always been reliable due to interrupt timings, especially with shared interrupts ("*We have historically been in a situation where suspend/resume often works, but may not be reliable due to interrupt timings, especially if there are any shared interrupts going on between drivers.*"). As these difficulties now seem resolved, Torvalds has called on users to report drivers that cause problems with suspend/resume. In addition, testers are to evaluate whether systems, whose system sleep states co-operate with previous kernels, work at least as well with the pre-release versions of 2.6.29 as they did before ("*...we'll really need user feedback on any drivers that now don't suspend/resume cleanly. So please, people - especially if you use suspend/resume, we want to hear about regressions,...*").

### Manual throttling disabled

In [their blogs](http://mjg59.livejournal.com/89111.html) and [elsewhere](http://www.codon.org.uk/~mjg59/power/good_practices.html), the kernel developers Matthew Garrett and Dave Jones have repeatedly described that the throttling of modern CPUs prevents overheating, but doesn't, as many people assume, lower the clock speed or reduce power consumption. They say that on the contrary, the overall power consumption for a calculation even increases, because the CPU can't switch to power saving mode, and because the system, with all its components that continuously consuming power, will take longer to compute the result.

To illustrate this to users, the two developers have removed the sysfs interface of the [p4-clockmod driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e088e4c9cdb618675874becb91b2fd581ee707e6); while the driver can still protect systems from overheating, it can no longer be used for manually slowing down the CPU. The [comment in the commit](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e088e4c9cdb618675874becb91b2fd581ee707e6) and an [entry in Dave Jones' blog](http://www.codemonkey.org.uk/2009/01/18/forthcoming-p4clockmod/) also explain the reasons for this measure; additional reasons can be found in the blog entry's comments, where the developer defends the measure and further discusses the myths about throttling.

In addition, the kernel developers have modified some of the PCI configuration information displayed during booting to give it more coherence and clarity ([1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=29935282f24a6ce2f0a65c3d77fb7f695461f583), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0663a36284586ac9a9781be8aa7e8ca9fff16d06)). There are numerous major changes to the ACPI code, for example, the restructuring of the include files ([1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=50df4d8b0f6e1971b930f3158c9ee0e4263e636d), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e2f7a7772880458edff1b1cc5a988947229fac26)) and [the relocation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=95b482a8d31116f3f5c2a5089569393234d06385) of the ACPI component architecture ([ACPICA](http://www.acpica.org/)) to a directory of its own.

### New notebook drivers

The maintainer of the ACPI subsystem has relocated the largely vendor-specific drivers for notebooks by Acer, Asus, IBM/Lenovo, MSI and others from drivers/misc/ to drivers/platform/x86/, which may result in a need to reactivate them when configuring 2.6.29 with a configuration file from a previous kernel ([1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=41b16dce390510f550a4d2b12b98e0258bbed6e2), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b4f9fe12157a33351d0df78e925dcacd13252783)). The i8k driver for Dell notebooks now supports the [Vostro](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=bef2a508b4276fd7897b2cb27df037d26361842c) and [Precision](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=7ab21a8692094872298df172f54d55cba72fd308) series; a new addition is the [dell-laptop driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ad8f07ccaddca1b0f52d0e9677855122a46cfafc), which supports brightness adjustments and WiFi/Bluetooth switch suppport via dcdbas (Dell Systems Management Base Driver). The developers extended the fujitsu-laptop driver for notebooks by Fujitsu-Siemens [to include several new features](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3a407086090bb4fa1908d4dc3739c9ebc8ad6686). They also made numerous improvements to the driver for Thinkpads by IBM and Lenovo – find these and a selection of further important changes in the areas of ACPI, PCI, and power management in these sections:

**ACPI:**

- [ACPICA: Add a mechanism to escape infinite AML While() loops](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fc37445733aeae4fd1a20385850620354263b1d5)
- [ACPICA: Add Buffer-String conversion for predefined methods](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a647b5c34047560d7efe7e53e756c6692ce67dc7)
- [ACPICA: Add support to externally execute \_OSI method](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a8fadc923d1659f1a322194d420808d5b255883c)
- [ACPICA: Emit warning if two FACS or DSDT tables found in the FADT](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c87609f31a8641009641fc1d19dac75e6de06fd4)
- [ACPICA: Move all public H/W interfaces to new hwxface](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=7db5d82d0278b506441ab6025f0c6ce2f2aa3019)
- [ACPICA: New: acpi_get_gpe_device interface](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e97d6bf1a01b7403d98aea95731863aab2e84064)
- [ACPICA: New: Public GPE group enable/disable interfaces](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=08ac07b826cfd9a9b28aa094f14e1c023bdc9864)
- [ACPICA: Optimize execution of AML While loops](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=96411a630412f057d365aa1e9de7d23c069d627a)
- [ACPICA: Update version to 20081204.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e8443c358c34f3fe65236e24147ddf0cd0e61b08)
- [ACPI: disable MPS when NO APIC-table found](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=7b37b5fd9ba32c0c5afc3537eed7e7466f2173e2)
- [ACPI: EC: Add some basic check for ECDT data](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c5279dee26c0e8d7c4200993bfc4b540d2469598)
- [ACPI: main.c: use new public GPE group enable/disable interfaces](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3d97e426aa97d60b3dac1b72923b90b491fbac20)
- [ACPI: Use RSDT instead of XSDT by adding boot option of "acpi=rsdt"](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=237889bf0a62f1399fb2ba0c2a259e6a96597131)
- [ACPI hibernate: Add a mechanism to save/restore ACPI NVS memory](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3f4b0ef7f2899c91b1d6958779f084b44dd59d32)
- [ACPI hibernate: Introduce new kernel parameter acpi_sleep=s4_nonvs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ba84ed9546e91348fdf3ff2bff859b0ee53b407a)
- [Newly inserted battery might differ from one just removed, so](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=50b178512b7d6e7724f87459f6bd06504c9c2da1)
- [/proc/acpi/alarm: handle day-of-month wraparound on readback](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=48452e5f99ab35d643df0463b6ad11aea8ea7bdc)
- [thermal fixup for broken BIOS which has invalid trip points.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0e4240d94628530a912d216cad1e32d2e3827327)
- [video: always update the brightness when poking "brightness"](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9e6dada9d255497127251c03aaa59296d186f959)

**Cpufreq:**

- [CPUFREQ: add to speedstep-lib additional fsb values for core processors](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c60e19eb21d9a0fb0d78969884f32d88354abca9)
- [CPUFREQ: Add Celeron Core support to p4-clockmod.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8529154ec3f3ac20344c65b7a040c604c7af7651)
- [cpuidle: Add decaying history logic to menu idle predictor](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=816bb611e41be29b476dc16f6297eb551bf4d747)

**Laptop-/Notebook-/Netbook-Driver:**

- [ACPI: EC: Don't trust ECDT tables from ASUS](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c6cb0e878446c79f42e7833d7bb69ed6bfbb381f)
- [ACPI: EC: Limit workaround for ASUS notebooks even more](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=235c4a59278eb07e61d909f1f0c233733034a8b3)
- [ACPI: thinkpad-acpi: add UWB radio support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0045c0aa7d5e787f78938e6a10927b8a516f0b83)
- [ACPI: thinkpad-acpi: bump up version to 0.22](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=aa2fbcec07b0d594808bc3058692395d24eba66e)
- [ACPI: thinkpad-acpi: debug facility to emulate the rf switches](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a73f30916ee524437253739eacc682f6fb0f3ea8)
- [ACPI: thinkpad-acpi: handle HKEY event 6030](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=54926ce8d2db7ebcbc4b80aae2cec571cd793e46)
- [ACPI: thinkpad-acpi: preserve radio state across shutdown](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=90d9d3c79c44bcf95bc487e9bbceaff2de370310)
- [ACPI: thinkpad-acpi: resume with radios disabled](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=153f82207c51193e4d6a7e6f0e3f9442eabeba1c)
- [ACPI: thinkpad-acpi: update documents for the new location](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9abf0eea877d6107d3a8a5c6913450e961fb7050)
- [dell-laptop: move to drivers/platform/x86/ from drivers/misc/](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=cad73120ab0dfd484682229346de8c16073577e1)
- [eeepc-laptop: enable Bluetooth ACPI details](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3af9bfcb433c110839e4c815a9928377f66bbd0e)
- [eeepc-laptop: use select and not depends on](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d9447183366ce849d7483bbd369752ac748e0422)
- [fujitsu-laptop: Simplify SBLL/SBL2 backlight handling](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f87a1a5f6cdaff6232fed2ef0ae0479df9e781e8)

**PCI:**

- [PCI/ACPI: acpiphp: Identify more removable slots](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=56ee325e25a0f76fc3267872867b3d70af179aad)
- [PCI: add a new function to map BAR offsets](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=613e7ed6f72b1a115f7ece8ce1b66cf095de1348)
- [PCI: Add legacy_io/mem to all busses](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d3a54014e2a94bd37b7dee5e76e03f7bc4fab49a)
- [PCI: add PCI Advanced Feature Capability defines](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f7b7baae6b30ff04124259ff8d7c0c0d281320e6)
- [PCI: Add pci_clear_master() as opposite of pci_set_master()](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=6a479079c07211bf348ac8a79754f26bea258f26)
- [PCI: add pci_common_swizzle() for INTx swizzling](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=68feac87de15edfc2c700d2d81b814288c93d003)
- [PCI: add pci_swizzle_interrupt_pin()](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=57c2cf71c12318b72ebaa5720d210476b6bac4d4)
- [PCI: extend on the ICH motherboard IO decode quirk list](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=894886e5d3de0bde2eded8a39bf7e76023fbd791)
- [PCI: handle PCI state saving with interrupts disabled](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=63f4898ace2788a89ed685672aab092e1c3e50e6)
- [PCI hotplug: introduce functions for ACPI slot detection](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e8c331e963c58b83db24b7d0e39e8c07f687dbc6)
- [PCI: keep ASPM link state consistent throughout PCIe hierarchy](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=46bbdfa44cfc0d352148a0dc33ba9f6db02ccdf0)
- [PCI: pciehp: add ACPI based slot detection](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c9ffa5a586a97da4d552f89b8f39eea79a63a612)
- [PCI: pciehp: add auto option to pciehp_detect_mode](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e046cbd6c05ee859244245d7beeac395cd0057b3)
- [PCI: pciehp: cleanup register and field definitions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=322162a71bd9fc4edb1b11236e7bc8aa27ccac22)
- [PCI: PCIe portdrv: Add kerneldoc comments to remining core funtions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d9347371c538544a7309d5b6475ec011d98d40e6)
- [PCI: PCIe portdrv: Add kerneldoc comments to some core functions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=facf6d1627a33badbbc154524c4a2c73c51bdc99)
- [PCI: PCIe portdrv: Fix suspend and resume of PCI Express port services](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e7ae88486670f3904f187d0fff9dcf469bcdd8ba)
- [PCI: pci-stub module to reserve pci device](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c70e0d9dfef3d826c8ae4f7544acc53887cb161d)
- [PCI PM: Add suspend counterpart of pci_reenable_device](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=fa58d305d9925b01830e535896a7227a868a9e15)
- [PCI PM: Avoid touching devices behind bridges in unknown state](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=734104292ff77dc71fe626b4ebd91b314547ca1b)
- [PCI PM: Fix poweroff and restore callbacks](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c9b9972b3c88272be02d971346285d1c67fbb95f)
- [PCI PM: Power-manage devices without drivers during suspend-resume](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=571ff7584bb9e05fca0eb79752ae55a46faf3a98)
- [PCI PM: Register power state of devices during initialization](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=98e6e286d7b01deb7453b717aa38ebb69d6cefc0)
- [PCI PM: Restore standard config registers of all devices early](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=aa8c6c93747f7b55fa11e1624fec8ca33763a805)
- [PCI PM: Run default PM callbacks for all devices using new framework](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d67e37d7933ba3b28a63ff38c957e433aaca5dc4)
- [PCI: Rework default handling of suspend and resume](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=355a72d75b3b4f4877db4c9070c798238028ecb5)
- [PCI: Suspend and resume PCI Express ports with interrupts disabled](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=90d25f246ddefbb743764f8d45ae97e545a6ee86)

**Power Management/Hibernate:**

- [Hibernate: Take overlapping zones into account (rev. 2)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=846705deb059c352cc0e5806d5964f815b8c6d98)
- [Hibernation: Introduce system_entering_hibernation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=abfe2d7b915c872f3a1fd203267cedebf90daa45)
- [PM: Simplify the new suspend/hibernation framework for devices](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=adf094931ffb25ef4b381559918f1a34181a5273)
- [Hibernate: Do not oops on resume if image data are incorrect](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=69643279a88dea000ac2f858091d0e365f778245)

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: New stable kernels, AMD 3D documentation and Mesa 7.3 released](../site/news/item/Kernel-Log-New-stable-kernels-AMD-3D-documentation-and-Mesa-7-3-released-739845.html "Kernel Log: New stable kernels, AMD 3D documentation and Mesa 7.3 released – 28 January 2009, 11:41")
- [Kernel Log: What's new in 2.6.29 - Part 3: Kernel controlled graphics modes](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-3-Kernel-controlled-graphics-modes-739697.html "Kernel Log: What's new in 2.6.29 - Part 3: Kernel controlled graphics modes – 17 January 2009, 07:36")
- [Kernel Log: main development phase for 2.6.29 ends, new X.org drivers](../site/news/item/Kernel-Log-main-development-phase-for-2-6-29-ends-new-X-org-drivers-739633.html "Kernel Log: main development phase for 2.6.29 ends, new X.org drivers – 12 January 2009, 17:09")
- [Kernel Log: What's new in 2.6.29 - Part 2: WiMax](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-2-WiMAX-739621.html "Kernel Log: What's new in 2.6.29 - Part 2: WiMAX – 12 January 2009, 10:19")
- [Kernel Log: What's new in 2.6.29 - Part 1: Dodgy Wifi drivers and AP support](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-1-Dodgy-Wifi-drivers-and-AP-support-739619.html "Kernel Log: What's new in 2.6.29 - Part 1: Dodgy Wifi drivers and AP support – 11 January 2009, 16:08")
- [Kernel Log: 2.6.29 development kicks off, improved 3D support](../site/news/item/Kernel-Log-2-6-29-development-kicks-off-improved-3D-support-739551.html "Kernel Log: 2.6.29 development kicks off, improved 3D support – 05 January 2009, 17:29")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
