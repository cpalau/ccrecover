---
title: "Kernel Log: What's coming in 2.6.28 - Part 4: Improved graphics support"
date: 2008-10-25
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-4-Improved-graphics-support-737779.html
pages: 1
---

# Kernel Log: What's coming in 2.6.28 - Part 4: Improved graphics support

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/4/5/5/0/93e8ea3d0acdf147.jpg) Two collections of patches ([1](http://thread.gmane.org/gmane.comp.video.dri.devel/32212), [2](http://thread.gmane.org/gmane.comp.video.dri.devel/32275)) proposed by the maintainer of the [Direct Rendering Infrastructure](http://dri.freedesktop.org/) (DRI) have incorporated numerous graphics hardware support improvements into the main development branch. This is the development branch which will produce Linux version 2.6.28 at the end of this year or at the beginning of next year.

[The developers included the Graphics Execution Manager](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=673a394b1e3b69be886ff24abfd6df97c52e8d08) (GEM) which takes over some of the graphics drivers' memory management tasks and co-ordinates the access to the graphics chip's processing units; this is designed to take care of some limitations in the current driver design and to improve performance. GEM was [started several months ago](http://thread.gmane.org/gmane.comp.video.dri.devel/30488) by Intel developers as a short term alternative to Translation Table Maps ([TTM](http://www.tungstengraphics.com/wiki/index.php/TTM_Memory_Manager)), the memory manager by Tungsten Graphics which was originally intended for this job – a driver which is now much less likely to become a standard component of Linux kernel. So far, only the [recently released version 2.5.0 of the X.org "intel" graphics driver](http://lists.freedesktop.org/archives/xorg/2008-October/039555.html) uses GEM; some developers of the X.org "radeon" graphics driver are also working on an experimental driver which makes use some of the GEM's functionality.

Also added to the official Linux kernel have been [extensive improvements to the Vblank mechanism](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0a3e67a4caac273a3bfc4ced3da364830b1ab241). With these changes, AMD and Intel graphics chips operating in 3D mode will only trigger interrupts when a program is waiting for a Vblank event, avoiding such visible effects like display flickering. Due to the lower number of interrupts, the system processor can stay in deep sleep longer while there are no other processing requests – this lowers the power consumption of modern CPUs and prolongs the battery life of netbooks and notebooks.

Since Intel [released](http://thread.gmane.org/gmane.comp.freedesktop.xorg/32614) the [ACPI Integrated Graphics Device OpRegion Specification](http://www.intellinuxgraphics.org/ACPI_IGD_OpRegion_%20Spec.pdf)![PDF](../site/icons/file-pdf.gif "PDF document") under a Creative Commons Attribution licence [several weeks ago](../site/news/item/Kernel-Log-problem-with-e1000e-bypassed-Morton-praises-Btrfs-737561.html "Kernel Log: problem with e1000e bypassed, Morton praises Btrfs – 07 October 2008, 08:47"), support for this technology [has now been added to the kernel](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8ee1c3db9075cb3211352e737e0feb98fd733b20). In recent notebooks with Intel graphics chipset, the display brightness can now be adjusted via ACPI, and has been successfully tested by the developers on a Thinkpad T61 and a HP 2510p. The new code also improves the interception and forwarding of function key events for switching display outputs.

Eric Anholt talks about the newly integrated kernel technologies and other developments around the Intel graphics driver in a [blog entry](http://anholt.livejournal.com/39921.html). A feature that has not made it into the kernel yet is [Kernel Mode Setting](http://thread.gmane.org/gmane.linux.kernel/531149) (KMS). This is designed to considerably speed up the switching between text consoles and the X Server and eliminate the related flickering that is currently clearly noticeable. It also gives the kernel more control over the graphics chip. This in principle enables the kernel to switch to a text console and display error messages there if a critical error in the X Server is encountered – a function that was mockingly dubbed the "Blue Penguin of Death" by some developers.

Other commits related to the support of graphics hardware that have been included in the main development branch of Linux:

- [agp/amd-k7: Suspend support for AMD K7 GART driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2a32c3c894bcd3b3f8cc7e23f5ecbebca4a9f8e8)
- [drm/radeon: add support for RS740 IGP chipsets.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f0738e92403466d45cfb5008da668260c77fff4b)
- [radeon: add RS400 family support.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b2ceddfa52cbeb244b90096f1e8d3e9f7e0ce299)
- [i915: Disable MSI on GM965 (errata says it doesn't work)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=d1ed629f44b3a4108d5c445971535f05f441fce7)
- [separate i915 suspend/resume functions into their own file](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=317c35d1446f68b34d4de4e1100fc01680bd4877)

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: New Atheros WLAN drivers and stable kernels, radeon vs. radeonhd](../site/news/item/Kernel-Log-New-Atheros-WLAN-drivers-and-stable-kernels-radeon-vs-radeonhd-737773.html "Kernel Log: New Atheros WLAN drivers and stable kernels, radeon vs. radeonhd – 24 October 2008, 10:59")
- [Kernel Log: What's coming in 2.6.28 - Part 3: Dodgy drivers](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-3-Dodgy-drivers-737747.html "Kernel Log: What's coming in 2.6.28 - Part 3: Dodgy drivers – 22 October 2008, 09:29")
- [Kernel Log: More than 10 million lines of Linux source files](../site/news/item/Kernel-Log-More-than-10-million-lines-of-Linux-source-files-737731.html "Kernel Log: More than 10 million lines of Linux source files – 21 October 2008, 14:50")
- [Kernel Log: Coming in 2.6.28 - Part 2: network infrastructure and network drivers](../site/news/item/Kernel-Log-Coming-in-2-6-28-Part-2-network-infrastructure-and-network-drivers-737711.html "Kernel Log: Coming in 2.6.28 - Part 2: network infrastructure and network drivers – 20 October 2008, 09:39")
- [Kernel Log: Coming in 2.6.28 - Part 1: ATA support and block layer](../site/news/item/Kernel-Log-Coming-in-2-6-28-Part-1-ATA-support-and-block-layer-737699.html "Kernel Log: Coming in 2.6.28 - Part 1: ATA support and block layer – 19 October 2008, 08:02")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
