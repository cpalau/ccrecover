---
title: "Kernel Log: Coming in 2.6.35 (Part 1) - Graphics"
date: 2010-07-07
author: "Thorsten Leemhuis"
source: http://www.h-online.com/open/features/Kernel-Log-Coming-in-2-6-35-Part-1-Graphics-1034168.html
pages: 1
---

# Kernel Log: Coming in 2.6.35 (Part 1) - Graphics

**Thorsten Leemhuis**

**![Kernel Log Graphics Penguin](../site/open/imgs/45/5/4/0/1/0/6/Kernel-Log_Graphics_Penguin-4ae621ef9772f158.png) Power management features for Radeon graphics chips, the first groundwork for supporting 3D with Evergreen GPUs, H264 decoding in Intel's Ironlake driver and the support of Intel's next generation of desktop and notebook chips, are some of the major graphics driver advancements of Linux 2.6.35.**

Linus Torvalds went on a two-week holiday in mid-June, which meant that no changes were integrated into the main development branch of Linux during that time. Torvalds started integrating patches again at the end of last month and released the fourth release candidate of Linux 2.6.35 last Sunday. In the [release email](http://thread.gmane.org/gmane.linux.kernel/1006390) for version 2.6.35-rc4, he indicated that focussing on bug fixes more strictly than usual worked quite well in this phase of the development cycle.

Therefore, RC4 of Linux 2.6.35 should match the final version even more closely than the RCs of previous versions, unless a bug is found which is serious enough to prompt the kernel developers to remove or temporarily suspend one of the major changes. Since this only happens very rarely, the Kernel Log can already provide a comprehensive overview of the most important changes of the forthcoming kernel release, which is expected to arrive in August.

We will publish the usual multi-part series of articles that will eventually cover all the kernel's individual functional areas. This first part of the "Coming in 2.6.35" mini series describes the changes to the kernel's graphics hardware support. Over the coming weeks, further articles will cover the advancements in terms of network support, storage hardware, file systems, architecture code, drivers and various other areas.

### AMD

The rudimentary support of the power management functions of Radeon graphics chips already [introduced](../site/open/features/Kernel-Log-Coming-in-2-6-34-Part-3-Graphics-994262.html "Kernel Log: Coming in 2.6.34 (Part 3) - Graphics – 06 May 2010") in Linux 2.6.34 has been [extended and optimised considerably](http://git.kernel.org/linus/ce8f53709bf440100cb9d31b1303291551cf517f) in 2.6.35. How aggressive the driver's power saving efforts will be can be determined via */sys/class/drm/card0/device/power_method*. For instance, writing "dynpm" to this file activates the fully automatic dynamic power management. Alternatively, by writing "profile" to the file, users can enable one of four profiles in the file */sys/class/drm/card0/device/power_profile*: "default" enables the standard GPU and memory clocks, "low" activates a power-saving mode, "high" a performance mode, and "auto" automatically switches between "low" and "high" depending on the power supply. Further details about the improvements and options can be found in the commit comment. In his [Git-Pull request](http://thread.gmane.org/gmane.comp.video.dri.devel/46146/focus%3D988668), however, DRM maintainer Dave Airlie explains that although the support of the run-time power management functions requires more work, this support has now been integrated into the kernel so developers can obtain feedback upstream; he also mentioned that the dynamic power saving mode, "dynpm", may cause screen glitches.

A rudimentary [Command Stream Parser](http://git.kernel.org/linus/cb5fcbd540b438a5d311bd15dc910841d01ed140) for the Evergreen graphics chips in the Radeon 5000 series has also been integrated by the kernel developers. It's a prerequisite for 3D support; according to the commit comment, developers are soon to release Mesa code that is based on the CS parser. The developers have also added [IRQ support for Evergreen GPUs](http://git.kernel.org/linus/45f9a39bedc3afab3fc85567792efc0103f34a55), which should allow them to implement features such as monitor detection without polling and eventually also page flipping.

### Intel

The kernel hackers have also merged various [changes](http://thread.gmane.org/gmane.linux.kernel/993523) to the driver for the graphics cores used in many Intel motherboard and notebook chip-sets. This means that the driver now includes all the basics (such as [the bit stream decoder ring buffer](http://git.kernel.org/linus/d1b851fc0d105caa6b6e3e7c92d2987dfb52cbe0)) required for using the H264 decoding functions offered by Ironlake CPUs, which have a graphics core. New userland software such as the libva as well as a player software which supports this library is also required to use these functions; further details and download links can be found on a [web page maintained](http://intellinuxgraphics.org/h264.html) by Intel.

The driver [now also supports](http://git.kernel.org/linus/8db9d77b1b14fd730561f64beea8c00e4478d7c5) a PCH code-named Cougar Point, which it's rumoured Intel plans to introduce together with its Sandy Bridge processors early next year. Further new additions include [multi-function SDVO device support](http://git.kernel.org/linus/14571b4c1ac9c109f5d6d6e95cfdb92339151fe0) as well as the [support of memory self-refresh](http://git.kernel.org/linus/7f8a85698f5c8a981641ec0bdf9926768786db9d) with Ironlake processors – according to tests by the developer, the latter reduced a test netbook's power consumption by one Watt.

### Independent

Intel employee Jesse Barnes has introduced some [documentation](http://git.kernel.org/linus/2d2ef822758e3f5da59c40a392d0c6d89394d4b4) which is aimed at developers and explains various internal aspects of the DRM subsystem to assist newcomers with the development of DRM drivers. The kernel is now said to cope better when no monitor is connected. Various further new additions are listed in the Git-Pull requests by [DRM maintainer Dave Airlie](http://thread.gmane.org/gmane.comp.video.dri.devel/46146/focus%3D988668) and by [Eric Anholt](http://thread.gmane.org/gmane.linux.kernel/993523), who maintains the Intel drivers. There have been hardly any noteworthy improvements to the fairly young Nouveau driver for NVIDIA graphics chips in this development cycle.

Another component [submitted](http://thread.gmane.org/gmane.linux.drivers.platform.x86.devel/216/) for integration into 2.6.35 was a driver for Intel's [Intelligent Power Sharing](http://software.intel.com/sites/oss/archives/1209/platform_turboboost_powersharing.htm) (IPS). This technology, which is used in mobile CPUs in the Ironlake series such as the Core i5, allows the graphics core to step up its core frequency in order to increase graphics performance while the CPU's x86 processor cores are not working to full capacity and the processor has not yet reached its specified maximum thermal budget. However, the code was submitted after the release of RC2 and was, therefore, [rejected by Torvalds](http://thread.gmane.org/gmane.linux.drivers.platform.x86.devel/216/focus%3D217) – this was not the only rejection in the current development cycle. As already mentioned earlier, Torvalds has been [much stricter](../site/open/features/Kernel-Log-Linus-resolves-to-apply-a-strict-policy-over-merging-changes-1026919.html "Kernel Log: Linus resolves to apply a strict policy over merging changes – 23 June 2010") than he used to be, and it seems likely he will keep up this strategy in the future.

### Minor gems

Many further minor, but by no means insignificant, changes can be found in the list below, which contains the commit headers referring to the respective change. Like many of the references in the text above, the links point to the relevant commit in the [web front end](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=summary) of the Git branch for the "official" kernel sources maintained by Linus Torvalds at kernel.org. The commit comments available at these links and the patches themselves provide extensive further information on the respective changes.

Every link is preceded by various letters and numbers in square brackets. The letter "C" identifies patches that modify Kconfig files, which contain the help texts and configuration options displayed by "make menuconfig", "make xconfig" and similar tools during kernel configuration. "D" is used for patches that modify the documentation available under *Documentation/* in the kernel branch. "N" identifies changes which create a new file. The numbers provide a rough idea of the patch size: For instance, "1" is used for changes between 10 and 20 KBytes including comment, "2" for patches between 20 and 30 KBytes; changes without a number are less than 10 KBytes, while patches marked "9" are 90 KBytes or more.

- \[`    `\] [add support for S3 Trio3D/1X/2X](http://git.kernel.org/linus/9966c4fea578bcf356c35cdf184cdacde495bc2c)
- \[`C N `\] [backlight: Add Cirrus EP93xx backlight driver](http://git.kernel.org/linus/08b3924b24cdb1942393dc3009335a2153bd2eac)
- \[`C N `\] [backlight: Add pcf50633 backlight driver](http://git.kernel.org/linus/2ddfd12f3584840f5190897214423061d8a0602f)
- \[`C   `\] [backlight: adp8860: add support for ADP8861 & ADP8863](http://git.kernel.org/linus/c7c06d8a95fd6b83d9f71a0cfecd3f91945d17e5)
- \[`    `\] [drm/edid: Add modes for Established Timings III section](http://git.kernel.org/linus/2255be14cb82370a6af4054edb3b4cd170d80752)
- \[`   1`\] [drm/edid: Add secondary GTF curve support](http://git.kernel.org/linus/7a37435008b0ffea2442eb1134ddd4adeea81e19)
- \[`    `\] [drm/edid: Add test for monitor reduced blanking support.](http://git.kernel.org/linus/d1ff6409b1cd2cd2a65df415648fa38b9fdf4cd8)
- \[`C  3`\] [drm/fbdev: rework output polling to be back in the core. (v4)](http://git.kernel.org/linus/eb1f8e4f3be898df808e2dfc131099f5831d491d)
- \[`    `\] [drm/i915: Add CxSR support on Pineview DDR3](http://git.kernel.org/linus/9553426372eef71c849499fb1d232f4b0577c0f9)
- \[`   2`\] [drm/i915: add power monitoring support](http://git.kernel.org/linus/7648fa99eb77a2e1a90b7beaa420e07d819b9c11)
- \[`    `\] [drm/i915: Add support for interlaced display.](http://git.kernel.org/linus/734b4157b367d66405f7dab80085d17c9c8dd3b5)
- \[`    `\] [drm/i915: Add support of SDVO on Ibexpeak PCH](http://git.kernel.org/linus/461ed3caee9b615393eb5beb9a8148d230354b41)
- \[`    `\] [drm/i915/dp: Only enable enhanced framing if the sink supports it](http://git.kernel.org/linus/9962c9252e46eda7058067cbe73bdf1ed74b0d37)
- \[`   3`\] [drm/i915: implement multifunction SDVO device support](http://git.kernel.org/linus/14571b4c1ac9c109f5d6d6e95cfdb92339151fe0)
- \[`  N5`\] [drm/i915: introduce intel_ring_buffer structure (V2)](http://git.kernel.org/linus/8187a2b70e34c727a06617441f74f202b6fefaf9)
- \[`  N3`\] [drm/i915: Move ringbuffer-related code to intel_ringbuffer.c.](http://git.kernel.org/linus/62fdfeaf8b1f487060b6e160e7b5cd90287607c9)
- \[`    `\] [drm/i915: Turn on 945 self-refresh only if single CRTC is active](http://git.kernel.org/linus/45ac22c81b1088f5ac08dc5367f78c192d68d756)
- \[`C   `\] [drm/kms/fb: add polling support for when nothing is connected.](http://git.kernel.org/linus/5c4426a782bc9509573fc7958a786ebd14fafdf3)
- \[`   2`\] [drm/kms/fb: use slow work mechanism for normal hotplug also.](http://git.kernel.org/linus/4abe35204af82a018ca3ce6db4102aa09719698e)
- \[`    `\] [drm/nouveau: Add ttm page pool debugfs file.](http://git.kernel.org/linus/bf62acdef89cb5b294668a6a747f7411dfe2ea7d)
- \[`  N `\] [drm/nv50: support fractional feedback divider on newer chips](http://git.kernel.org/linus/e9ebb68b86dd75fe2d61467f834dcf572e6859df)
- \[`    `\] [drm/radeon: add quirk to make HP nx6125 laptop resume.](http://git.kernel.org/linus/580b4fffbbdc3c899ee1f8189ba321bd60b48840)
- \[`    `\] [drm/radeon/kms: add support for evergreen power tables](http://git.kernel.org/linus/49f6598277635af13d60e7d2601963356bc48bd8)
- \[`   1`\] [drm/radeon/kms: add support for gui idle interrupts (v4)](http://git.kernel.org/linus/2031f77ca9c17133869b265210418959a909d259)
- \[`    `\] [drm/radeon/kms: Add ttm page pool debugfs file.](http://git.kernel.org/linus/8d7cddcd7f9e847cec44851ca53fd3e81e846c49)
- \[`  N1`\] [drm/radeon/kms/evergreen: add gart support](http://git.kernel.org/linus/0fcdb61e78050f8f0b31029eeafa5ae013ce0f35)
- \[`    `\] [drm/radeon/kms/evergreen: add hpd support](http://git.kernel.org/linus/0ca2ab52d451c25764e53d3d289e1be357c977d7)
- \[`    `\] [drm/radeon/kms/evergreen: add soft reset function](http://git.kernel.org/linus/747943ea187e5acceb7ffc762ff2c84cb3449745)
- \[`   2`\] [drm/radeon/kms/evergreen: implement gfx init](http://git.kernel.org/linus/32fcdbf4084544c3d8fa413004d57e5dc6f2eefe)
- \[`   2`\] [drm/radeon/kms: fence cleanup + more reliable GPU lockup detection V4](http://git.kernel.org/linus/225758d8ba4fdcc1e8c9cf617fd89529bd4a9596)
- \[`   1`\] [drm/radeon/kms: HDMI irq support](http://git.kernel.org/linus/f2594933df9719bd2b0aaaa8ea9b2b850d6e1c42)
- \[`   2`\] [drm/radeon/kms/pm: add additional asic callbacks](http://git.kernel.org/linus/49e02b7306cb7e01965fe5f41ba0f80085142f6e)
- \[`   4`\] [drm/radeon/kms/pm: add asic specific callbacks for getting power state (v2)](http://git.kernel.org/linus/a48b9b4edb8bb87deb13b9f088a595cf71457b69)
- \[`   1`\] [drm/radeon/kms/pm: add asic specific callbacks for setting power state (v2)](http://git.kernel.org/linus/bae6b5627387a950a8faf366d6027bd0a7a93078)
- \[`   1`\] [drm/radeon/kms/pm: add support for no display power states](http://git.kernel.org/linus/d7311171c4cc8d6231427f7ac5056b939a184b80)
- \[`    `\] [drm/radeon/kms/pm: add support for SetVoltage cmd table (V2)](http://git.kernel.org/linus/7ac9aa5a1f1b87adb69bcbec2b89e228f074103a)
- \[`   5`\] [drm/radeon/kms: simplify & improve GPU reset V2](http://git.kernel.org/linus/90aca4d2740255bd130ea71a91530b9920c70abe)
- \[`  N2`\] [drm/ttm: add pool wc/uc page allocator V3](http://git.kernel.org/linus/1403b1a38e8b19a4cc17e2c158e278628943a436)
- \[`    `\] [drm/ttm: Add sysfs interface to control pool allocator.](http://git.kernel.org/linus/c96af79e3463d5d3f865625baa8bb8aa4c0944a0)
- \[`  N1`\] [drm/vmwgfx: Add kernel throttling support. Bump minor.](http://git.kernel.org/linus/1925d4565888eb313cc923372da6a08bbfb3a859)
- \[`   1`\] [drm/vmwgfx: Support older hardware.](http://git.kernel.org/linus/d7e1958dbe4a7b81d4cab5fab545a068501b967e)
- \[`    `\] [i915: fix ironlake edp panel setup (v4)](http://git.kernel.org/linus/fe27d53e5c597ee5ba5d72a29d517091f244e974)
- \[`C N2`\] [OMAP: DSS2: Add ACX565AKM Panel Driver](http://git.kernel.org/linus/0188352b2774234575a41864fd0945be42975ee5)
- \[`    `\] [viafb: Add 1200x900 DCON/LCD panel modes for OLPC XO-1.5](http://git.kernel.org/linus/c205d932530719d2a6ddb9152650e5bbe80c9400)
- \[`C N1`\] [viafb: add a driver for GPIO lines](http://git.kernel.org/linus/7e0de022680f7899d33141f3ab5724a704f5669a)
- \[`    `\] [viafb: Add a simple interrupt management infrastructure](http://git.kernel.org/linus/94dd1a856b23bd51dfebf68e6dd63cfd4d4fd5ae)
- \[`    `\] [viafb: Add a simple VX855 DMA engine driver](http://git.kernel.org/linus/3d28eb42c52a799c806082e6d856f634ed1db902)
- \[`    `\] [viafb: complete support for VX800/VX855 accelerated framebuffer](http://git.kernel.org/linus/1317824376482781200980c6f026ef576d7ed1dd)
- \[`C   `\] [viafb: make procfs entries optional](http://git.kernel.org/linus/2b78a963c800252a0016785813cc5140c006145c)
- \[`   2`\] [viafb: rework the I2C support in the VIA framebuffer driver](http://git.kernel.org/linus/277d32a36cba0b42c9c6836ff07f9b978566e95c)

*Older Kernel Logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/). New editions of Kernel Logs are also mentioned on* [Identi.ca](http://identi.ca/kernellog2) *and* [Twitter](http://twitter.com/kernellog2) *via "@kernellog2". The Kernel Log author also posts updates about various topics on* [Identi.ca](http://identi.ca/kernellogauthor) *and* [Twitter](http://twitter.com/kernellogauthor) *via "@kernellogauthor".*

([crve](mailto:crve@h-online.com))
