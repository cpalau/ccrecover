---
title: "Kernel Log: In future only GPL USB drivers to use internal kernel USB API, version 2.6.22.17 last in 22 series."
date: 2008-04-02
author: "Edward Henning"
source: http://www.h-online.com/open/news/item/Kernel-Log-In-future-only-GPL-USB-drivers-to-use-internal-kernel-USB-API-version-2-6-22-17-last-in-22-series-734092.html
pages: 1
---

# Kernel Log: In future only GPL USB drivers to use internal kernel USB API, version 2.6.22.17 last in 22 series.

**Edward Henning**

![image 1 \[224 x 297 Pixel @ 12,9 KB\]](../site/imgs/43/3/6/0/8/6/7/a345f5e7c547062f.jpg) [A patch](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=782e70c6fc2290a0395850e8e02583b8b62264d8) from well-known Linux developer Greg Kroah-Hartman, intended to clarify that in future only **USB drivers** licensed under GPL2 or a compatible license will be allowed to use the core functions of the kernel's internal USB driver API, has found its way into the Linux kernel source code control system. This change, which will be introduced in 2.6.25, was originally planned for kernel 2.6.16, in which Kroah-Hartman, as part of a larger revision of the USB subsystem, wanted to introduce a patch so that only GPL compatible drivers should be able to use the USB code (much of it penned by him) directly. This change was subsequently revoked prior to release of 2.6.16, but it was announced that the patch would be reintroduced in February 2008. This was intended to give companies like AVM two years to modify their proprietary Linux USB drivers, offered as kernel modules with wrapper code, such that they would work as normal programs in the user space and would access USB devices via the interface exported to the user space by the kernel - as is the case for printer and scanner drivers under Linux. These 'driver programs' would then not need to be released under open source licenses and, according to the developers, should be able to be ported to BSD and Windows without too much effort.

Just as occurred at the first attempt to introduce this patch two years ago, there has been some criticism of this development from users and developers in a [discussion](http://thread.gmane.org/gmane.linux.usb.general/835/) over the last ten days or so on the Linux kernel mailing list ([LKML](http://www.kernel.org/pub/linux/docs/lkml/)). The arguments resemble previous discussions over the use of proprietary Linux drivers as kernel modules - some see it as a legal grey area in general, Kroah-Hartman, however, [has a very different point of view](http://thread.gmane.org/gmane.linux.usb.general/835/focus%3D1207). The newly adopted additional USB API interface symbols are intended to make the situation a little clearer, at least for the USB field, but even this is [controversial](http://thread.gmane.org/gmane.linux.usb.general/835/focus%3D1193).

Pragmatists consider the action taken by Linux developers such as Kroah-Hartman detrimental, because it may discourage vendors from developing Linux drivers. Nonetheless, the resistance offered by some kernel developers and distributors to proprietary drivers does seem to have helped some vendors to get to grips with the concept of open source. AMD's decision to publish documentation is just one well known example. Due to pressure from customers, companies like Highpoint have made substantial moves in the direction of open source drivers. These are generally much easier for customers to install, maintain and use, as all Linux distributors include open source drivers and ensure their compatibility with other software included in their distributions.

As one of the administrators of the stable kernel series, Kroah-Hartman has meanwhile been [preparing](http://thread.gmane.org/gmane.linux.kernel/633377) the 17th version in the **2.6.22 series**. It should be released tomorrow or the day after and should be the final 2.6.22 version, as the administrators of the stable kernel series usually concentrate on the latest two kernel versions - currently 2.6.23 and 2.6.24.

**Kernel Log staccato**: The developers of the controversial Ndiswrapper have now released version 1.52. Sony [is due to release](http://thread.gmane.org/gmane.linux.kernel/476198/focus%3D633367) version 1.6.0 of the "PS3 Linux Distributor's Starter Kit" for the PlayStation 3. WLAN driver developers are planning on having [support](http://thread.gmane.org/gmane.linux.kernel.wireless.general/10831) for an access point (AP) function in the MAC80211 Linux WLAN stack.

*Further background information and information on developments in and relating to the Linux kernel can be found in previous editions of Kernel Log on Heise Open:*

([ehe](mailto:ehe@h-online.com "Edward Henning"))
