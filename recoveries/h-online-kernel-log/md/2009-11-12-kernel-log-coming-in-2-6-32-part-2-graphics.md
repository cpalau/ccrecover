---
title: "Kernel Log: Coming in 2.6.32 (Part 2) - Graphics"
date: 2009-11-12
author: "Chris von Eitzen"
source: http://www.h-online.com/open/news/item/Kernel-Log-Coming-in-2-6-32-Part-2-Graphics-858783.html
pages: 1
---

# Kernel Log: Coming in 2.6.32 (Part 2) - Graphics

**Chris von Eitzen**

#### ![](../site/imgs/43/4/4/1/1/2/6/kernellogpenguin.jpg-cdb99630db3e76d3.jpeg)

#### by Thorsten Leemhuis

Earlier this month, Linus Torvalds [released](http://thread.gmane.org/gmane.linux.kernel/909203) 2.6.32-rc6 â€“ due to the [Kernel Summit](../site/news/item/Kernel-Log-Discussions-at-the-2009-Kernel-Summit-FatELF-in-the-firing-line-new-graphics-drivers-850044.html " Kernel Log - Discussions at the 2009 Kernel Summit, FatELF in the firing line, new graphics drivers â 04 November 2009, 13:44"), RC6 was not released the usual week after RC5, but two weeks after. As usual at this point in the development cycle, mostly minor patches have been merged over the past few days to avoid making changes that might introduce new bugs in the three to six weeks that remain until the final release of Linux 2.6.32.

Having looked at the [network subsystem changes](../site/news/item/Kernel-Log-Coming-in-2-6-32-Part-1-Network-subsystem-and-network-drivers-832229.html "Kernel Log: Coming in 2.6.32 (Part 1) – Network subsystem and network drivers â 19 October 2009, 13:50") in the previous issue, the Kernel Log will now discuss the most important advancements in the field of graphics hardware support. Some of these changes have probably been eagerly awaited by many users since AMD resumed closer cooperation with the open source developers.

### 3D and KMS for Radeon

The kernel and its Direct Rendering Manager (DRM) will now [offer](http://git.kernel.org/linus/3ce0a23d2d253185df24e22e3d5f89800bb3dd1c) 3D support and kernel-based mode setting (KMS) for AMD's series R600 and R700 GPUs. These are used in the Radeon series 2000, 3000 and 4000 models â€“ which includes most of the Radeon graphics cards sold in the past couple of years as well as various AMD series 700 motherboard chip-sets.

For the 3D support and KMS to function, however, [suitable](http://airlied.livejournal.com/68097.html) (developer) versions of Libdrm and MesaÂ 3D as well as Radeon graphics drivers for X.org need to be installed. Compiling this software stack is a task for advanced users â€“ however, the Fedora project plans to provide all the necessary components in an experimental package with FedoraÂ 12, which is scheduled for release in mid November.

The Radeon KMS will also offer [basic support](http://git.kernel.org/linus/4ce001abafafe77e5dd943d1480fc9f87894e96f) for activating TV outputs. While the KMS driver for Intel graphics chips already offered this feature, it now supports a greater number of SDVO chips and more of their respective features ([1](http://git.kernel.org/linus/ce6feabd1b38f9adf4a962d71bc4762047e8f889), [2](http://git.kernel.org/linus/b9219c5e8be99ddd697e3f9b61069d7ea477ddec), [3](http://git.kernel.org/linus/213c2e643145fc7d8a67f2d5d54ee0f6d7193e2e)).

From version 2.6.32, the Intel KMS code [will also compress](http://git.kernel.org/linus/8082400327d8d2ca54254b593644942bed0edd25) the frame buffer, which reportedly reduces power consumption by up to 0.5 watts; in addition, [the new "Dynamic Clock Frequency Control"](http://git.kernel.org/linus/652c393a3368af84359da37c45afc35a91144960) feature is to further reduce power consumption by reducing the LCD refresh rate, the memory's self refresh and the clock rate to prolong notebook battery life. The Intel driver now handles the graphics memory more efficiently, ([1](http://git.kernel.org/linus/07f73f6912667621276b002e33844ef283d98203), [2](http://git.kernel.org/linus/31169714fc928aed4e945b959dca2bedd259b9c9)) and will attempt to [re-initialise](http://git.kernel.org/linus/11ed50ec2a316928c2bacc1149bded86c6a96068) [crashed](http://git.kernel.org/linus/f65d94211e2bcba17faf05a6a3809af0e4217767) GPUs.

### Coordinated

The kernel hackers have also integrated the VGA arbitration patches ([1](http://git.kernel.org/linus/deb2d2ecd43dfc51efe71eed7128fda514da96c6), [2](http://git.kernel.org/linus/28d520433b6375740990ab99d69b0d0067fd656b), [documentation](http://git.kernel.org/linus/0737c4e4897ecae4cce3db0cc075efad791e1c21)). In systems with several graphics cards, the patches cooperate with X Servers from version 1.7 to ensure that the respective graphics card will actually receive the VGA commands sent to it by the X Server â€“ which reportedly allows much more flexibility when implementing multi-seat environments.

Further changes to the kernel code responsible for graphics support:

- The "video=" parameter can now be used for [setting](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git&a=commit&h=d50ba256b5f1478e15accfcfda9b72fd7a661364) a specific output screen resolution for individual monitors, or all monitors, in the KMS code.
- The firmware previously tied in with the code for Radeon drivers has been [shifted](http://git.kernel.org/linus/70967ab9c0c9017645d167d33675eab996633631) into separate files and will from now on be loaded using the firmware loader. The developers also made a [similar change](http://git.kernel.org/linus/ece2be7993cc5e269cbf0cad6442b401a2c31915) to the driver code for Matrox graphics cards.
- A new addition is the [frame buffer driver](http://git.kernel.org/linus/d480ace08d5b59133575e672a0bd1c97b0f8400f) for Qualcomm MSM/QSD SoCs, which are used in devices like the HTC Dream (aka T-Mobile G1, aka ADP1).
- The developers have reworked the code paths used for initialisation by the kernel's Radeon drivers. This is intended both to facilitate maintenance and improve suspend and resume behaviour â€“ the relevant commits are listed at the end of this article. These driver maintenance measures should also simplify [the merging](http://git.kernel.org/linus/785b93ef8c309730c2de84ce9c229e40e2d01480) of several KMS code segments for AMD and Intel GPUs.
- The frame buffer driver for VIA graphics hardware [now also supports](http://git.kernel.org/linus/0306ab11c396f93056009152464ff104e4721817) the VX855 chip-set. Furthermore, the kernel hackers have [rewritten](http://git.kernel.org/linus/c3e25673843153ea75fda79a47cf12f10a25ca37) the VIA driver's 2D engine.
- The new [tracepoint support](http://git.kernel.org/linus/1c5d22f76dc721f3acb7a3dadc657a221e487fb7) offers enhanced DRM code monitoring for Intel's current graphics chip-sets.
- The developers say they [have also fixed](http://thread.gmane.org/gmane.linux.kernel/894139) numerous bugs with Intel series 8xx chip-sets that have occurred since GEM was introduced in 2.6.27.
- The KMS code for Radeon graphics hardware [now supports](http://git.kernel.org/linus/b442962a9e826e6d408886b3e52c88b774201983) Surround View â€“ which involves running a Radeon graphics card in parallel with the chip-set graphics.

### Minor gems

Many further minor, but by no means insignificant, changes can be found in the list below. Like many of the references in the text above, the links point to the relevant commits in the [web front end](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=summary) of the Git branch at kernel.org Linus Torvalds uses for maintaining the kernel sources. There, the commit comments and the patches themselves provide extensive further information on the respective changes.

- [Add G33 series in VGA hotplug support category](http://git.kernel.org/linus/af729a26ccc3ff9ad834a5e96f455aab20f176cd)
- [agp/intel: Add B43 chipset support](http://git.kernel.org/linus/38d8a95621b20ed7868e232a35a26ee61bdcae6f)
- [davinci: fb: Frame Buffer driver for TI DA8xx/OMAP-L1xx](http://git.kernel.org/linus/4ed824d9aead77a6a4eb1e89c3b3d270ba386fad)
- [drm: Add more standard TV properties.](http://git.kernel.org/linus/a75f0236292a5fca65f26efedca48bd07db1834d)
- [drm: Add the basic check for the detailed timing in EDID](http://git.kernel.org/linus/fcb45611448098a36b893bda71e72bd39730a3dd)
- [drm/edid: Fix standard timing parse for EDID \<= 1.2](http://git.kernel.org/linus/f066a17d9f8d0a20d01d1aa9badce7f43c7bd6ad)
- [drm/edid: Ignore bad standard timings.](http://git.kernel.org/linus/23425caeebc2e06629ef04f6197543cfe3f7d7b2)
- [drm: Enable drm drivers to add drm sysfs devices.](http://git.kernel.org/linus/327c225bd548bf7871f116a0baa5ebdac884e452)
- [drm/i915: add B43 chipset support](http://git.kernel.org/linus/7839c5d5519b6d9e2ccf3cdbf1c39e3817ad0835)
- [drm/i915: add FIFO watermark support for G4x](http://git.kernel.org/linus/0e442c60dd39ac6924b11a20497734bd2303744c)
- [drm/i915: disable powersave feature for Ironlake currently](http://git.kernel.org/linus/c03342fa6d4617a77cb867ee0ec71665d520eb69)
- [drm/i915: do dynamic clock freq control only in kernel modesetting](http://git.kernel.org/linus/5e17ee74b541b56b5d4cfab6502a5116f224e32c)
- [drm/i915: Fix FDI M/N setting according with correct color depth](http://git.kernel.org/linus/58a27471d00dc09945cbcfbbc5cbcdcd3c28211d)
- [drm/i915: fix startup hang on some non-mobile platforms](http://git.kernel.org/linus/c1a1cdc159e211f045290f61ac95092e9708f5bc)
- [drm/i915: force mode set at lid open time](http://git.kernel.org/linus/c1c7af60892070e4b82ad63bbfb95ae745056de0)
- [drm/i915: framebuffer compression for GM45+](http://git.kernel.org/linus/74dff282237ea8c0a5df1afd8526eac4b6cee063)
- [drm/i915: generate a KMS uevent at lid open/close time](http://git.kernel.org/linus/06324194eee97a51b5f172270df49ec39192d6cc)
- [drm/i915: Ironlake suspend/resume support](http://git.kernel.org/linus/4204878179c99d419d392d78d817729992b4c442)
- [drm/i915: Save and restore the GM45 FBC regs on suspend and resume.](http://git.kernel.org/linus/06027f9111b9f3244ddc40752428f7847b0b867e)
- [drm/i915: Support IGD EOS](http://git.kernel.org/linus/043029655816ed4cfc2ed247020ef97e5d637392)
- [drm/kms: add a function that can add the mode for the output device without EDID](http://git.kernel.org/linus/f0fda0a47b26aba986fe65897891956c1792b526)
- [drm/kms: Add the default mode table](http://git.kernel.org/linus/aa9eaa1f0962152d0bde821149d82fe7b70a6f92)
- [drm/kms: fix kms helper license + Kconfig](http://git.kernel.org/linus/6fcefd56f5060ca99ab03c9f2ad1f17c3a543ca1)
- [drm/kms/i915: Add the default mode for CRT output without EDID](http://git.kernel.org/linus/50fe4cfdc759fb3c0cffc3b90281efb139631fb7)
- [drm/kms/radeon: make kms default a runtime option](http://git.kernel.org/linus/a0cdc6495bdd0ea12390b9edaf13c8cb653df109)
- [drm/mode: add the CVT algorithm in kernel space](http://git.kernel.org/linus/d782c3f95c9263dc0b98e7115f75f1e%3D)
- [drm/mode: add the GTF algorithm in kernel space](http://git.kernel.org/linus/26bbdadad356ec02d33657858d91675%3D)
- [drm/mode: get the modeline for standard timing in EDID by using CVT/GTF](http://git.kernel.org/linus/5c61259e6c7290082108e93815f7f72f27da14f4)
- [drm/r128: Use request_firmware() to load CCE microcode](http://git.kernel.org/linus/52f97df5da1f94d2b7db1bb53a2f053ae162b649)
- [drm/radeon/kms: add 32/64 ioctl support.](http://git.kernel.org/linus/70ba2a374704e00df8868a7ac3d7350329d28924)
- [drm/radeon/kms: add common lvds modes in the ddc case](http://git.kernel.org/linus/7747b713049e63aa64bcac679535ddfff92b312d)
- [drm/radeon/kms: add common scaled modes for TV and LVDS](http://git.kernel.org/linus/923f6848e1686059ef8d272d1fca4d3577911a41)
- [drm/radeon/kms: add initial connector properties](http://git.kernel.org/linus/445282db9e815e7f5e82761c3c971dc9ea988d85)
- [drm/radeon/kms: add rn50/r100/r200 CS tracker.](http://git.kernel.org/linus/551ebd837c75fc75df81811a18b7136c39cab487)
- [drm/radeon/kms: Convert R100 to new init path (V2)](http://git.kernel.org/linus/d4550907157d8b3d5286157c15f1200c44842269)
- [drm/radeon/kms: Convert R300 to new init path](http://git.kernel.org/linus/207bf9e90cd40f91d4662127b8ae3b64e6b101c4)
- [drm/radeon/kms: Convert RS400/RS480 to new init path](http://git.kernel.org/linus/ca6ffc64cba0cdd0a2b3fcad0e1d19edcf277ccc)
- [drm/radeon/kms: Convert RS400/RS480 to new init path & fix legacy VGA (V3)](http://git.kernel.org/linus/ca6ffc64cba0cdd0a2b3fcad0e1d19edcf277ccc)
- [drm/radeon/kms: Convert RS600 to new init path](http://git.kernel.org/linus/c010f8000a925e08d84d9391e13dd297b9fdc393)
- [drm/radeon/kms: Convert RS690/RS740 to new init path (V2).](http://git.kernel.org/linus/3bc6853593bd4fba357dc252b3cf60cd86a1d2ec)
- [drm/radeon/kms: enable r600 tv outputs.](http://git.kernel.org/linus/4bbd4973703bf8a5f00f05eff30a99cd9814f37f)
- [drm/radeon/kms: Fix AGP support for R600/RV770 family (v2)](http://git.kernel.org/linus/1a029b768f9d4a001501bd18d6ba08297ae912fd)
- [drm/radeon/kms: Remove old init path as no hw use it anymore](http://git.kernel.org/linus/62a8ea3f7bb61e5f92db0a648b7cc566852c36ec)
- [drm: split crtc/fb helpers into a separate module](http://git.kernel.org/linus/13a8195b148615b15a4f4385f695f2a232095414)
- [drm/ttm: Add a virtual ttm sysfs device.](http://git.kernel.org/linus/e9840be8c23601285a70520b4898818f28ce8c2b)
- [drm/ttm: Memory accounting rework.](http://git.kernel.org/linus/5fd9cbad3a4ae82c83c55b9c621d156c326724ef)
- [ep93xx video driver](http://git.kernel.org/linus/88017bda96a5fd568a982b01546c8fb1782dda62)
- [i915: fix intel graphics suspend breakage due to resume/lid event confusion](http://git.kernel.org/linus/c9354c85c1c7bac788ce57d3c17f2016c1c45b1d)
- [matroxfb: make CONFIG_FB_MATROX_MULTIHEAD=y mandatory](http://git.kernel.org/linus/0728bacbba3b0267fa8ca8be69aa43d81b57ab51)
- [omapfb: add FB manual update option to Kconfig](http://git.kernel.org/linus/b1d51dbb79c6398c88b45d4211545621b4d1a11c)
- [omapfb: add support for rotation on the Blizzard LCD ctrl](http://git.kernel.org/linus/2f21a62f16136f369788795a98aa5c313261f07b)
- [omapfb: add support for the 2430SDP LCD](http://git.kernel.org/linus/3a76a819dda9a6de0ab83d04b48b3735a4d10b89)
- [omapfb: add support for the 3430SDP LCD](http://git.kernel.org/linus/fb49b78452503f6cdf8b243ccb40cda81aae9998)
- [omapfb: add support for the Amstrad Delta LCD](http://git.kernel.org/linus/92e0ed074a4f134084bef47a44e948b6c6429a89)
- [omapfb: add support for the Apollon LCD](http://git.kernel.org/linus/28ff0c12b7069f076f08a936df66f1d5052e9121)
- [omapfb: add support for the OMAP2EVM LCD](http://git.kernel.org/linus/42acff34f85c5892c8c762145441e993a5596a13)
- [omapfb: add support for the OMAP3 Beagle DVI output](http://git.kernel.org/linus/27969ccc2840c42bfbe4f55d08f0c7ec254d4e93)
- [omapfb: add support for the OMAP3 EVM LCD](http://git.kernel.org/linus/2a8729c47a9dfe5c8ba55883b86b719b33e6e099)

For other articles on 2.6.32 and links to the rest of the "Coming in 2.6.32" series, see [The H's Kernel Log - 2.6.32 Tracking](../site/open/features/2-6-32-Tracking-816707.html "2.6.32 Tracking â 05 October 2009, 17:04") page.

([crve](mailto:crve@h-online.com "Chris von Eitzen "))
