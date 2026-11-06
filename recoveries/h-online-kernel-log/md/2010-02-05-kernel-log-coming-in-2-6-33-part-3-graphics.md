---
title: "Kernel Log: Coming in 2.6.33 (Part 3) - Graphics"
date: 2010-02-05
author: "Chris von Eitzen"
source: http://www.h-online.com/open/news/item/Kernel-Log-Coming-in-2-6-33-Part-3-Graphics-922495.html
pages: 1
---

# Kernel Log: Coming in 2.6.33 (Part 3) - Graphics

**Chris von Eitzen**

#### ![Kernel Log Logo](../site/imgs/43/4/7/7/1/9/9/KL.jpg-1f663d67fe8a53b0.jpeg) by Thorsten Leemhuis

**The next version of Linux is not only the first to offer the Nouveau KMS graphics driver for NVIDIA graphics hardware, it also comes with a multitude of improvements for the two AMD/ATI and Intel graphics drivers which support Kernel-based Mode Setting (KMS).**

At the end of last week, Linus Torvalds [released](http://thread.gmane.org/gmane.linux.kernel/944249) Linux 2.6.33-rc6, the sixth release candidate of Linux 2.6.33; the final version is expected either at the end of this month, or early next month. As usual at this stage in the development cycle, the number of changes and their extent is beginning to decrease; Torvalds writes that development is reaching the point where most things "just work" ('\[...\]*we're getting to that stage of the release cycle where things mostly should "just work"*\[...\]')

The Kernel Log takes this opportunity to continue its report about the advancements of Linux 2.6.33 and discuss what's new in terms of graphics hardware support in part three of the "Coming in 2.6.33" mini series. The most important changes concerning the kernel's network support, file systems and storage subsystem were covered in part [one](../site/news/item/Kernel-Log-Coming-in-2-6-33-Part-1-Networking-898841.html "Kernel Log: Coming in 2.6.33 (Part 1) - Networking – 08 January 2010, 11:01") and [two](../site/news/item/Kernel-Log-Coming-in-2-6-33-Part-2-Storage-914669.html "Kernel Log: Coming in 2.6.33 (Part 2) - Storage – 27 January 2010, 18:01") of this series.

### New driver for NVIDIA GPUs

As [previously reported](../site/news/item/Kernel-Log-Linux-2-6-33-to-include-NVIDIA-graphics-driver-nouveau-885001.html "Kernel Log: Linux 2.6.33 to include NVIDIA graphics driver nouveau – 14 December 2009, 12:20"), the kernel developers have, at the urging of Linus Torvalds, [included](http://git.kernel.org/linus/6ee738610f41b59733f63718f0bdbcba7d3a3f12) the kernel code for the [Nouveau driver](http://nouveau.freedesktop.org/) for GeForce graphics cores (GPUs/Graphics Processing Units) in the Linux kernel's staging area. Version 2.6.33 of the kernel will, therefore, also offer Kernel-based Mode Setting (KMS) for many older as well as modern NVIDIA graphics chips; KMS has so far only been available with AMD/ATI and Intel GPUs. It allows flicker-free start-ups, faster switching between X Server and text console, and more reliable graphics hardware reinitialisation when waking up from system sleep states.

Based on the new kernel code, the Nouveau driver for X.org is capable of dual screen operation via RandR and offers Xvideo acceleration for recent GeForce models – these two features are not available with the "nv" (full name "xf86-video-nv") X.org driver many distributions configure for NVIDIA hardware. 3D acceleration, however, has not been mastered by either of the drivers – while it is currently under construction for Nouveau, it is still considered very experimental in this reverse engineered driver. Therefore, 3D support will for now continue to require NVIDIA's proprietary graphics driver, which some graphics cards also require to enable fan control. However, NVIDIA drivers only work if the Nouveau KMS code is disabled – one way of doing this at run-time is to set the "*nomodeset*" kernel parameter when booting.

Shortly before merging Nouveau, the developers modified the driver in such a way that the "ctxprogs" component, which was previously an integral part and often regarded as "firmware", is now only retrieved if required. Some distributions include this non-open source code for recent GPUs, which is sometimes called "Voodoo", even though the code was developed using proprietary graphics drivers and its inclusion might not be legal. The discussions around this problem prompted a developer to write open source code that replaces ctxprogs. This code was [included in Linux 2.6.33](http://git.kernel.org/linus/054b93e444550a72aef17115363cdef253b9ee7c) a few days after Nouveau – so far, however, it only supports [generation NV40](http://nouveau.freedesktop.org/wiki/HwIntroduction) GPUs, which are found on series 6000 and 7000 GeForce cards.

### KMS included as standard

In early January, the developers of Nouveau took the integration of the driver's KMS code as an opportunity to remove about fifteen thousand lines of code for setting video modes without KMS, from the Nouveau driver for X.org; this measure was taken to simplify the maintenance and ongoing development of Nouveau. The Nouveau team are not alone in this decision, as the developers of Intel's graphics driver for X.org also removed their driver's "User Mode Setting" (UMS) functionality:) before they released [version 2.10](http://thread.gmane.org/gmane.comp.freedesktop.xorg/41865) of the driver in early January. As a result, current and future versions of these drivers will rely on kernels which offer KMS support, which is likely to promote the fast and wide-spread acceptance of this relatively young technology.

When combined with the "[drmmode overlay support](http://git.kernel.org/linus/02e792fbaadb75dec8e476a05b610e49908fc6a4)" feature first integrated in the KMS driver for Intel GPUs with Linux 2.6.33, version 2.10 of the Intel graphics drivers now also supports video overlays. The developers have also included numerous improvements for Ironlake graphics cores, which are used in Westmere CPUs such as the series i3 und i5 dual core processors introduced at the beginning of the year. The Intel KMS driver now also [supports resolutions](http://git.kernel.org/linus/a4f45cf178f0d0ad4e516e020818b5f1c00e3d63) with a colour depth of 30 bits.

The kernel's DRM (Direct Rendering Manager), which is used by the KMS drivers, and the [Intel drivers](http://git.kernel.org/linus/6b95a207c1fd552e7d017837c5eaf1b0173a48c9) based on it will from now on offer an [interface](http://git.kernel.org/linus/d91d8a3f88059d93e34ac70d059153ec69a9ffc7) that improves the way graphics drivers synchronise the display of new screen content when flipping pages. This is to reduce or avoid "tearing", a type of image distortion which can be a particular nuisance when rendering video output. To make kernel-side "Page Flipping Support" available, the developers had to extend the DRI2 protocol. As a result, the technology will only be functional with Mesa 7.8, X Server 1.9 and with version 2.11 of the Intel graphics driver for X.org, which is still in development – [a comprehensive blog post](http://virtuousgeek.org/blog/index.php/jbarnes/2010/01/29/progress) by PCI subsystem maintainer and driver developer Jesse Barnes provides further details.

### Better rating for Radeon drivers

The kernel's DRM and KMS code for Radeon graphics chips now allows monitors to be controlled via DisplayPort ([1](http://git.kernel.org/linus/5801ead6bd6bddf5505d6eab55f84d8ee8106cd8), [2](http://git.kernel.org/linus/746c1aa4d100f7441423050f34be79f401fbf7d4)) and [eDP (embedded DisplayPort)](http://git.kernel.org/linus/196c58d21fc47fbabab6a98e23e5a6335f717e44); [audio output via HDMI](http://git.kernel.org/linus/dafc3bd515d6079406986f7748b48adb3c7170f2) is now also possible. Another new inclusion is the [IRQ support for r6xx and r7xx GPUs](http://git.kernel.org/linus/d8f60cfc93452d0554f6a701aa8e3236cbee4636), which allows monitor change overs to be detected without repeated polling and is a prerequisite for the previously mentioned page flipping support for Radeon cards – however, the whole set-up will only work when combined with a firmware update. The developers also made many minor corrections and improvements to the Radeon KMS driver. As a result, the code has now matured to a degree that allowed the developers to [remove](http://git.kernel.org/linus/f71d0187987e691516cd10c2702f002c0e2f0edc) it from the staging area, which is intended for incomplete and low quality drivers, and indicate in their commit comment that the driver is now stable enough to be used in the Linux distributions.

Another new addition to the kernel is the [vmwgfx KMS driver](http://git.kernel.org/linus/fb1d9738ca053ea8afa5e86af6463155f983b01c) for virtual "SVGA2" graphics hardware, which is visible to guest systems in some of the VMWare hypervisors. Like the KMS drivers for GeForce and Radeon graphics hardware, this driver will initially be placed in the staging area because, at least, the driver interfaces for 3D support still require adjustment. Furthermore, a display subsystem and drivers for OMAP2/3 processors have found their way into the kernel [via a Nokia developer](http://thread.gmane.org/gmane.linux.ports.arm.omap/27921) – such ARM CPUs are, for instance, included in Nokia's n900 and in the Beagle Board.

### Minor gems

Many further minor, but by no means insignificant, changes can be found in the list below, which contains the commit headers referring to the respective change. Like many of the references in the text above, the links point to the relevant commit in the [web front end](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git&a=summary) of the Git branch for the kernel sources maintained by Linus Torvalds at kernel.org. The commit comments and the patches themselves provide extensive further information on the respective changes.

- [backlight: mbp_nvidia_bl - add two more MacBookPro variants](http://git.kernel.org/linus/f7a297af49e5d9d2c577466307e8ef392750c9d9)
- [davinci: fb: add framebuffer blank operation](http://git.kernel.org/linus/312d97152faa30ac4c007937ea09c9c27b10e249)
- [davinci: fb : add suspend/resume suuport for DA8xx/OMAP-L1xx fb driver](http://git.kernel.org/linus/1d3c6c7b366bdc3406af96bf55d63b4aa24f400a)
- [drm: Add async event synchronization for drmWaitVblank](http://git.kernel.org/linus/c182be37ed7cb04c344501b88b8fdb747016e6cf)
- [drm: Add dirty ioctl and property](http://git.kernel.org/linus/884840aa3ce3214259e69557be5b4ce0d781ffa4)
- [drm: Add eDP connector type](http://git.kernel.org/linus/7970e677accb676f15e11468c60cb93ae477a513)
- [drm: convert drm_ioctl to unlocked_ioctl](http://git.kernel.org/linus/ed8b67040965e4fe695db333d5914e18ea5f146f)
- [drm/edid: Add new detailed block types from EDID 1.4](http://git.kernel.org/linus/2dbdc52c8162291aa7541b8ba6e1c1587f50c1dd)
- [drm/edid: Retry EDID fetch up to four times](http://git.kernel.org/linus/47ee4ccf745ea88ee1aadcf5895d91af3b73ea64)
- [drm/i915: Add ACPI OpRegion support for Ironlake](http://git.kernel.org/linus/01c66889c14aa163c49355b3be2ccfb214500599)
- [drm/i915: Add display hotplug event on Ironlake](http://git.kernel.org/linus/c650156af34bffa3d3a62c9fe26eee595aab3fd1)
- [drm/i915: Add HP nx9020/SamsungSX20S to ACPI LID quirk list](http://git.kernel.org/linus/40f33a92100f4d9b6e85ad642100cfe42d7ff57d)
- [drm/i915: add render standby support](http://git.kernel.org/linus/97f5ab6651a996ecefed73e41684422f3b29d9a8)
- [drm/i915: Check whether the LVDS downclock is found in VBT](http://git.kernel.org/linus/d1fcea6a529d22212b324f26cd660c85b289a026)
- [drm/i915: debugfs interface to manually reset the GPU](http://git.kernel.org/linus/f3cd474bb235f2331c1a6f579bdbf892386e5c7c)
- [drm/i915: disable LVDS downclock by default](http://git.kernel.org/linus/33814341f22f13cec17e8d7fbf6f7e8000e3efa4)
- [drm/i915: enable 36bit physical address for hardware status page](http://git.kernel.org/linus/9b974cc17166d31afed2638d56bdbf9829afbfaa)
- [drm/i915: Enable/disable the dithering for LVDS based on VBT setting](http://git.kernel.org/linus/898822ce9561ab9b58a7eb60580a162a83dadecd)
- [drm/i915: Enable LVDS downclock feature through EDID.](http://git.kernel.org/linus/18f9ed12f8c977e25d65a16af8e8d73f72417ba1)
- [drm/i915: enable self-refresh on 965](http://git.kernel.org/linus/1dc7546d1a73664e5d117715b214bea9cae5951c)
- [drm/i915: execbuf2 support](http://git.kernel.org/linus/76446cac68568fc7f5168a27deaf803ed22a4360)
- [drm/i915: Replace DRM_DEBUG with DRM_DEBUG_DRIVER](http://git.kernel.org/linus/44d98a614267c81a04ba9c7a0427c3a628985b7d)
- [drm/i915: warn if Pineview CxSR can't be enabled](http://git.kernel.org/linus/85364905f9ae12d19cb34099257d493e5d9a0c4e)
- [drm: Keep disabled outputs disabled after suspend / resume](http://git.kernel.org/linus/992dc9ae61f86db3b8ef9f8d6b7df898c90e8c08)
- [drm/kms: properly handle fbdev blanking](http://git.kernel.org/linus/731b5a15a3b1474a41c2ca29b4c32b0f21bc852e)
- [drm/modes: Fall back to 1024x768 instead of 800x600](http://git.kernel.org/linus/9632b41f00cc2fb2846569cc99dbeef78e5c94a0)
- [drm/modes: Limit fallback modes to 60Hz](http://git.kernel.org/linus/f985dedb57bae741b4326415f72fe1a1e556563b)
- [drm/nouveau: Pre-G80 tiling support.](http://git.kernel.org/linus/0d87c100312ce75d9bb75a456d8a542e84a1722f)
- [drm/nouveau: Pre-G80 tiling support.](http://git.kernel.org/linus/cb00f7c1419d09ee0daf7d8bed86f253d98db7b4)
- [drm/radeon/kms: add 3DC compression support](http://git.kernel.org/linus/512889f450c1851d9e3628f1894b9b64b0701eac)
- [drm/radeon/kms: add additional safe regs for r4xx/rs6xx and r5xx](http://git.kernel.org/linus/804c7559e9376c3ba78ae15a30337b1e24f8ae80)
- [drm/radeon/kms: add cvt mode if we only have lvds w/h and no edid (v4)](http://git.kernel.org/linus/d2efdf6d6f425950a61fa5cc3aa22e6718e7f3c8)
- [drm/radeon/kms: add definitions for v4 power tables](http://git.kernel.org/linus/0786201d8cd0730e72b0e087484dd47cc5f58409)
- [drm/radeon/kms: add HDP flushing for all GPUs.](http://git.kernel.org/linus/23956dfa82eab95931aab5fa9886c1e96c41e4dc)
- [drm/radeon/kms: add hpd support for r1xx-r4xx asics](http://git.kernel.org/linus/05a05c506f52041daa511f4899b63d21c9457474)
- [drm/radeon/kms: add hpd support for r5xx/rs600/rs690/rs740 asics](http://git.kernel.org/linus/dcfdd4083509f9c46b1e92c58c062d50da50580e)
- [drm/radeon/kms: add hpd support for r6xx/r7xx/rs780/rs880 asics](http://git.kernel.org/linus/e0df1ac5c2cf346f4cc335025734978a4d747aa0)
- [drm/radeon/kms: add irq mitigation code for sw interrupt.](http://git.kernel.org/linus/1614f8b17b8cc3ad143541d41569623d30dbc9ec)
- [drm/radeon/kms: add quirk for Acer laptop](http://git.kernel.org/linus/3e5f8ff3a9f4e7a71c5371b2122b32faf31c563a)
- [drm/radeon/kms: Add quirk for HIS X1300 board](http://git.kernel.org/linus/4e3f9b78ff917cc5c833858fdb5d96bc262e0bf3)
- [drm/radeon/kms: add quirk for MSI S270](http://git.kernel.org/linus/fd874ad0a0dcf715333a3f3564c6486a3a90bb22)
- [drm/radeon/kms: add support for external tmds on legacy boards](http://git.kernel.org/linus/fcec570b27a47e428a9bfc8572ae4c7c230d0488)
- [drm/radeon/kms: add tv standard property to tv connectors](http://git.kernel.org/linus/ed160143c6967e89aee05b0685e73c4103bb3e38)
- [drm/radeon/kms: AGP systems need PCI bus mastering enabled](http://git.kernel.org/linus/17e15b0c719b5ec0b344d3ebe3787b48315a0218)
- [drm/radeon/kms/avivo: add support for new pll selection algo](http://git.kernel.org/linus/b27b63750d912e80d61d2120c4a1664062d0f808)
- [drm/radeon/kms: enable hpd support](http://git.kernel.org/linus/d4877cf2293f5463f531769fd12300cb3417c778)
- [drm/radeon/kms: fix r100-\>r500 CS checker for compressed textures. (v2)](http://git.kernel.org/linus/d785d78bbdb53580b12c40e820af5a3281ce2fc8)
- [drm/radeon/kms: get HPD info for connectors](http://git.kernel.org/linus/eed45b30cd1423f8dc10b4312700773cac13c1c8)
- [drm/radeon/kms: init pm on all chipsets](http://git.kernel.org/linus/6234077d6bad4db25d516743b6723c1b26505341)
- [drm/radeon/kms: Workaround RV410/R420 CP errata (V3)](http://git.kernel.org/linus/62cdc0c20663ef840a94850892517b2b7f584904)
- [drm/radeon: r6xx/r7xx possible security issue, system ram access](http://git.kernel.org/linus/c8c15ff1e90bfc4a2db1ba77a01b3b2783e723fc)
- [drm/ttm: Add user-space objects.](http://git.kernel.org/linus/88071539a3f5195f9e9dae38a3e35b3ce4b9f9fc)
- [drm/ttm: Rework validation memory space allocation (V3)](http://git.kernel.org/linus/ca262a9998d46196750bb19a9dc4bd465b170ff7)
- [fbdev: bfin-lq035q1-fb: new Blackfin Landscape LCD EZ-Extender driver](http://git.kernel.org/linus/9cfe4a93e50bb36392c8d74432e4607f297cdbfc)
- [MAINTAINERS: Add OMAP2/3 DSS and OMAPFB maintainer](http://git.kernel.org/linus/178ff4c9175db447f93b7343954b1d44707c881b)
- [mb862xxfb: add acceleration support for Coral-P/Coral-PA. imageblt copyarea fillrect](http://git.kernel.org/linus/2ec509b96cce5e6d19ee43fdd818eab78e76328d)
- [offb: Add support for framebuffer handoff to offb.](http://git.kernel.org/linus/ceae8cbe94f3127253110e2d01b9334069e93177)
- [OMAP: Add support for VRFB rotation engine](http://git.kernel.org/linus/640f9ca5fd783393c832f6bb5c56368f4d18b820)
- [OMAP: Add VRAM manager](http://git.kernel.org/linus/afedec183e95bd5e126a7846a644acfdddb86a66)
- [OMAP: DSS2: Add generic and Sharp panel drivers](http://git.kernel.org/linus/3b8f29b4152899e91c210186a38bffb37ea1a226)
- [OMAP: DSS2: Add more core files](http://git.kernel.org/linus/eed07e0ed5367aede8d32758524f2dc2d252a291)
- [OMAP: DSS2: DISPC](http://git.kernel.org/linus/80c397120fd2436c79f6e0552882feb5ed4549c3)
- [OMAP: DSS2: Display Subsystem Driver core](http://git.kernel.org/linus/559d67018950ced65c73358cd69c4bdd2b0c5dd6)
- [OMAP: DSS2: DSI driver](http://git.kernel.org/linus/3de7a1dc0c9d29b138713ecb85df4b6ca3af2ef3)
- [OMAP: DSS2: omapfb driver](http://git.kernel.org/linus/b39a982ddecf1d95ed96f8457c39d3ea11df93f6)
- [OMAP: DSS2: RFBI driver](http://git.kernel.org/linus/5c18adb3736afe266d74bdb820d076da0e39ebeb)
- [OMAP: DSS2: Taal DSI command mode panel driver](http://git.kernel.org/linus/f133a9d7f27ebde5c11bb5d7d89ff66576682e65)
- [OMAP: DSS2: Video encoder driver](http://git.kernel.org/linus/b288627350c456fe4006c3c4419584969a7ae6a1)
- [OMAP: OMAPFB: add omapdss device](http://git.kernel.org/linus/dadd2bb931a08a4b6b17f9e82d9bbe7bedebbc98)
- [vc: Add support for hiding the cursor when creating VTs](http://git.kernel.org/linus/f6c06b6807ff9281295989ebad72523865325a4f)
- [vgacon: Add support for setting the default cursor state](http://git.kernel.org/linus/b434a680a29424856e0f40199daa9f65963c7cb4)
- [viafb: documentation update](http://git.kernel.org/linus/4562aea791e97aa0f2e342849daa18b588c46df1)
- [video: Allow selecting MSM framebuffer in Kconfig](http://git.kernel.org/linus/4e00dc762d68248c23c5fe1dfb4d06fbe75554b0)
- [vt: make the default cursor shape configurable](http://git.kernel.org/linus/9ea9a886b0e8630e12cff515955e7f0f5be32cb1)

*For other articles on 2.6.33 and links to the rest of the "Coming in 2.6.33 " series, see* [The H's Kernel Log - 2.6.33 Tracking page](../site/open/features/Linux-Kernel-2-6-33-tracking-890639.html "Linux Kernel 2.6.33 tracking – 21 December 2009, 10:18")*.*

([thl](mailto:thl@ct.heise.de))

([crve](mailto:crve@h-online.com "Chris von Eitzen "))
