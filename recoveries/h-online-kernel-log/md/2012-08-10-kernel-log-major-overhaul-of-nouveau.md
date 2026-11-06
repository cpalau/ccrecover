---
title: "Kernel Log: Major overhaul of Nouveau"
date: 2012-08-10
author: "Thorsten Leemhuis"
source: http://www.h-online.com/open/features/Kernel-Log-Major-overhaul-of-Nouveau-1664869.html
pages: 1
---

# Kernel Log: Major overhaul of Nouveau

**Thorsten Leemhuis**

**The kernel driver for NVIDIA graphics chips is undergoing a major overhaul. KVM is now available for MIPS. The new "lslocks" lists locked files and displays the programs that locked them.**

In the past few days, the mainline Linux kernel has seen far fewer changes than usual [after the arrival](../site/news/item/First-release-candidate-of-Linux-kernel-version-3-6-1659576.html "First release candidate of Linux kernel version 3.6 â 03 August 2012") of a new kernel's first release candidate â€“ a consequence of Linus Torvalds being away on holiday. However, there are some noteworthy developments in other areas of the Linux kernel and the software close to it:

![Kernel Log Penguin](../site/open/imgs/45/9/0/2/6/6/4/Kernel_Log_Penguin.jpg-1f663d67fe8a53b0.jpeg)

### Graphics

- Nouveau developer Ben Skeggs has done major restructuring work in the developer branch of the Nouveau DRM graphics driver ([for example](http://cgit.freedesktop.org/nouveau/linux-2.6/log/) [1](http://cgit.freedesktop.org/nouveau/linux-2.6/commit/?id=2eac96152fb2b5a8ce9a9b34a17d51155bb13a4f), [2](http://cgit.freedesktop.org/nouveau/linux-2.6/commit/?id=d1e4909c72da4729ad0675df82742bf518e110a1), [3](http://cgit.freedesktop.org/nouveau/linux-2.6/commit/?id=d2ff00930ef2ea6df71cc070d322c319b5847914), [4](http://cgit.freedesktop.org/nouveau/linux-2.6/commit/?id=f52ec912f4fe530e61ca19ff637b6c9df51e59ae), [5](http://cgit.freedesktop.org/nouveau/linux-2.6/commit/?id=c2c0bf1a8af2d570e6f8f9fd9c0c1fccfccf15ff), [6](http://cgit.freedesktop.org/nouveau/linux-2.6/commit/?id=3bfc362f68789fa994213ead6e2f4e715d167ba3), [7](http://cgit.freedesktop.org/nouveau/linux-2.6/commit/?id=d5ef81e73fcbae7e78205f7239faf8ee43cc442c)). Commenting on [one of the changes](http://cgit.freedesktop.org/nouveau/linux-2.6/commit/?id=03d7aaaf3db3a3a50684e4748e4a9bf4adef1c38), Skeggs wrote that the restructuring measures are a result of all the things the Nouveau developers have learned in the past few years, and that the measures will lead to a cleaner and more maintainable driver architecture. He added that one of the main aims of his work was to reduce code complexity; other changes are designed to create the foundations for future features. Skeggs provides further information and tips for testers [in an email](http://lists.freedesktop.org/archives/nouveau/2012-August/010854.html) to the other Nouveau developers. The changes will likely be integrated into Linux 3.7; in the latest main Git pull request for the DRM graphics drivers, the developers [mentioned](http://article.gmane.org/gmane.linux.kernel/1333398) that there would only be minor changes to the Nouveau code in Linux 3.6 because Skeggs is working on a rewrite.

<!-- -->

- With the recently issued fourth release candidate of XÂ Server 1.13, the developers have closed the non-critical bug window. This version of X.org XÂ Server, which improves aspects such as the [hybrid graphics support](../site/news/item/X-Server-1-13-to-offer-better-support-for-hybrid-graphics-1635760.html "X Server 1.13 to offer better support for hybrid graphics â 10 July 2012"), is [scheduled](http://thread.gmane.org/gmane.comp.freedesktop.xorg.devel/30989/) to be completed in September.

<!-- -->

- The organisers of this year's [X.Org Developers Conference](http://www.x.org/wiki/Events/XDC2012) (XDC), to be held in Nuremberg in September, have [issued a call](http://article.gmane.org/gmane.comp.freedesktop.xorg.announce/1780) for papers and presentations.

<!-- -->

- Intel employee Chris Wilson has [released](http://article.gmane.org/gmane.comp.freedesktop.xorg.drivers.intel/13035) version 2.20.3 of the Intel driver for X.org's XÂ Server. His colleague Haihao Xiang has released [libva 1.0.16](http://lists.freedesktop.org/archives/libva/2012-August/001124.html) and [version 1.0.18](http://lists.freedesktop.org/archives/libva/2012-August/001125.html) of the libva driver for Intel hardware; these components, which give access to the video acceleration features of modern graphics cores, now support the decoding of JPEG data on Intel's Ivy Bridge processors. Meanwhile, Intel developer Ian Romanick [has announced on his blog](http://www.paranormal-entertainment.com/idr/blog/posts/2012-08-09T00%3A37%3A31Z-OpenGL_ES_3_0_announced_for_Intel_HD_Graphics_on_Linux/) that Intel is working on driver code to support the recently [released OpenGL ES 3.0](../site/news/item/OpenGL-ES-3-0-the-future-of-tablet-and-smartphone-graphics-1661118.html "OpenGL ES 3.0 – the future of tablet and smartphone graphics â 07 August 2012") and that the plan is to have it fully enabled for release by February.

<!-- -->

- Open source drivers that are suitable for production use continue to be unavailable for various Southern Islands GPUs introduced since late last year on series 7700, 7800 and 7900 Radeon HD graphics cards. According to the developers, [a recent fix](http://cgit.freedesktop.org/mesa/mesa/commit/?id=86490bc150dd108d5917bb0f4636a9545fbf1b8e) for the [Mesa 3D driver for these AMD graphics chips](http://cgit.freedesktop.org/mesa/mesa/log/?qt=grep&q=radeonsi), which is currently in development, has finally made the glxgears mini test program functional; also, a VDPAU target which uses the shader units on Southern Island GPUs to provide video acceleration has been [added to](http://cgit.freedesktop.org/mesa/mesa/commit/?id=41625afa2f7f30e5076c695ab3a16eabb5fe69f8) the Mesa 3D code.

### Linux

- Kyma Systems, a company that specialises in embedded products, has [announced](http://www.virtual-strategy.com/2012/08/07/kyma-systems-announces-open%E2%80%93source-kvm-hypervisor-mips32%C2%AE-processors) that it has ported the Linux kernel's KVM (Kernel-based Virtual Machine) virtualisation technology to the MIPS32 architecture.

<!-- -->

- Greg Kroah-Hartman released the stable and long-term kernels [3.0.40](http://thread.gmane.org/gmane.linux.kernel/1340839), [3.4.8](http://thread.gmane.org/gmane.linux.kernel/1340843) and [3.5.1](http://thread.gmane.org/gmane.linux.kernel/1340848). Ben Hutchings has published [Linux 3.2.26](http://thread.gmane.org/gmane.linux.kernel/1337888) and is [preparing 3.2.27](http://thread.gmane.org/gmane.linux.kernel/1338712) .

<!-- -->

- Kernel developer and RCU maintainer Paul E. McKenney has [released](http://paulmck.livejournal.com/33204.html) the August 2012 update of "[Is Parallel Programming Hard, And, If So, What Can You Do About It?](http://kernel.org/pub/linux/kernel/people/paulmck/perfbook/perfbook.html)", a book that he has been working on for some time.

### Userland

- [In a blog post](http://karelzak.blogspot.de/2012/08/lslocks8.html), Karel Zak explains the operation of "lslocks" â€“ a program that is scheduled to be part of [Util-Linux 2.22](../site/open/features/Kernel-Log-Development-of-Linux-3-6-under-way-1657742.html "Kernel Log: Development of Linux 3.6 under way â 02 August 2012"). Lslocks outputs a list of files that have been locked by programs; it is similar to "lslk", which hasn't been maintained since 2001.

<!-- -->

- Johannes Berg has [released](http://article.gmane.org/gmane.linux.kernel.wireless.general/95761) version 3.6 of the "iw" wireless hardware configuration tool.

<!-- -->

- The recently released [Iproute2 3.5.0](http://article.gmane.org/gmane.linux.kernel/1336584) supports the Codel network packet scheduler, a component integrated [in Linux 3.5](../site/open/features/Kernel-Log-Coming-in-Linux-3-5-Part-1-Networking-1625047.html "Kernel Log: Coming in Linux 3.5 (Part 1) - Networking â 26 June 2012") to held avoid buffer bloat.

### LKML

- There is currently some disagreement on the future development of Zcache: instead of making improvements to the staging branch version of this framework for compressing parts of the working memory, Dan Magenheimer has reimplemented the feature from scratch and has proposed that his code be used ([1](http://thread.gmane.org/gmane.linux.kernel.mm/83115/), [2](http://thread.gmane.org/gmane.linux.kernel.mm/83286)).

<!-- -->

- A recent [discussion](http://thread.gmane.org/gmane.linux.kernel/1336561/) on the kernel developers' mailing list revolved around a case in which a company may have been wrong to state that a certain kernel module was released under the GPL.

*Further background information about the developments in the Linux kernel area can be found using [the search function](../site/search/?sort=d;rm=search;mediatype=3;q=kernel-log) at [TheÂ H Open Source](../site/open/). Information about previous Linux kernel releases can be found in [TheÂ H's Linux Kernel History](../site/open/features/The-H-s-Linux-Kernel-History-1221120.html "The H's Linux Kernel History â 15 July 2011"). New editions of Kernel Logs are also mentioned on [Identi.ca](http://identi.ca/kernellog2) and [Twitter](http://twitter.com/#!/kernellog2) by @kernellog2. The Kernel Log author also posts updates about various topics on [Identi.ca](http://identi.ca/kernellogauthor) and [Twitter](http://twitter.com/#!/kernellogauthor) as @kernellogauthor.*
