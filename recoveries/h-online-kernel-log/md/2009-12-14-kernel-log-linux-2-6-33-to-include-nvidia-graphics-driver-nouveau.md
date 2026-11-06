---
title: "Kernel Log: Linux 2.6.33 to include NVIDIA graphics driver nouveau"
date: 2009-12-14
author:
source: http://www.h-online.com/open/news/item/Kernel-Log-Linux-2-6-33-to-include-NVIDIA-graphics-driver-nouveau-885001.html
pages: 1
---

# Kernel Log: Linux 2.6.33 to include NVIDIA graphics driver nouveau

#### ![](../site/imgs/43/4/5/6/4/3/4/KL.jpg-1f663d67fe8a53b0.jpeg) by Thorsten Leemhuis

Linus Torvalds has [merged](http://git.kernel.org/linus/6ee738610f41b59733f63718f0bdbcba7d3a3f12) the kernel code for the GeForce-compatible [nouveau](http://nouveau.freedesktop.org) open source graphics driver as a staging driver into the Linux main development tree – from which kernel version 2.6.33 will emerge in around two and a half months. The 2.6.33 kernel should therefore support kernel-based mode setting on the bulk of NVIDIA graphics chips (GPUs/graphics processing units) in addition to existing support for AMD and Intel chips.

The merger of nouveau into the kernel will allow for a flicker-free boot process, with the Linux kernel configuring a screen resolution suitable for the current monitor on initialising the hardware. The nouveau kernel code and the nouveau driver for X.org based on it also permit dual screen operation and, with the latest GeForce models, Xvideo acceleration – neither of which is supported by the [nv](http://xorg.freedesktop.org/wiki/nv) (or, to give it its full name, xf86-video-nv) driver used for Nvidia hardware by default in most distributions.

Neither, however, support 3D acceleration. The nv driver is primarily maintained by NVIDIA developers, whereas nouveau programmers have had to resort to reverse engineering in developing the driver. 3D support in nouveau is a work in progress and, according to the nouveau wiki, already usable in part, though still classed as experimental. ("*3D support is worked on using Gallium3D and can (depending on the Chip generation and the applications) be quite usable, but at the moment, the nv50 (GeForce 8 and up) gallium driver can actually run compiz to some extent already. There's some minor graphical issues, but it works. Still officially considered experimental.*")

Dave Airlie, who is employed by Red Hat, works on Fedora and is responsible for kernel graphics support, originally wanted to submit nouveau for a later kernel version. However, at the end of last week [Torvalds persistently pressed](http://thread.gmane.org/gmane.linux.kernel/925370%20Torvalds%20dr%C3%A4ngte%20allerdings%7C_blank) for its merger and repeatedly pointed out that the driver is included in the current Fedora distribution, but that Fedora developers were declining to pass on the code. This gave rise to a lengthy discussion on organisational and technical issues, with the upshot that, following some quick alterations by a Red Hat nouveau specialist, Dave Airlie was able to rapidly submit the code [for merger](http://thread.gmane.org/gmane.linux.kernel/925943), to which Torvalds' [response was equally prompt](http://thread.gmane.org/gmane.linux.kernel/925943/focus%3D926222).

The last minute changes allow the driver to load firmware ('ctx_voodoo'), which was previously intertwined with the driver, separately and for the firmware to be distributed independently of the kernel. There appear to be some doubts over whether this firmware can be distributed at all. The firmware code was obtained by nouveau developers from graphics cards initialised using Nvidia's proprietary drivers. However, the Fedora Project, which tends to be more conscientious about copyright issues than many other mainstream distributions and, with the exception of firmware, contains exclusively open source software, has not previously considered this an issue.

*See also:*

- [Kernel Log: New stable kernels, 2.6.33 with DRBD and RT2800PCI](../site/news/item/Kernel-Log-New-stable-kernels-2-6-33-with-DRBD-and-RT2800PCI-883212.html "Kernel Log: New stable kernels, 2.6.33 with DRBD and RT2800PCI – 11 December 2009, 13:33"), a report from The H.
- [What's new in Linux 2.6.32](../site/open/features/What-s-new-in-Linux-2-6-32-872271.html "What's new in Linux 2.6.32 – 03 December 2009, 08:22"), a feature from The H.

([crve](mailto:crve@h-online.com "Chris von Eitzen "))
