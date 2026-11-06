---
title: "Kernel Log: Centrino 2 WiFi driver iwl 5000 and webcam driver gscpa in Linux 2.6.27"
date: 2008-07-23
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-Centrino-2-WiFi-driver-iwl-5000-and-webcam-driver-gscpa-in-Linux-2-6-27-736569.html
pages: 1
---

# Kernel Log: Centrino 2 WiFi driver iwl 5000 and webcam driver gscpa in Linux 2.6.27

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/3/3/4/2/93e8ea3d0acdf147.jpg) Before leaving for the weekend, Torvalds wrote a few [friendly words](http://thread.gmane.org/gmane.linux.kernel/708190) to the Linux testers in response to some [blunt statements](../site/news/item/Kernel-log-ath9k-driver-for-new-Atheros-WLAN-chips-discussions-of-Nvidia-drivers-736563.html "Kernel log: ath9k driver for new Atheros WLAN chips, discussions of Nvidia drivers – 22 July 2008, 15:48") elsewhere. He is now back working on Linux version 2.6.27. The approximately 2,000 revisions made to 2.6.27 over the past 48  hours will add a host of new features, many of which will be of real benefit to users.

Torvalds has integrated [numerous patches](http://thread.gmane.org/gmane.comp.video.video4linux/39126) from the administrator of the V4L-/DVB subsystem into the main development branch. These include the [gspca](http://mxhaard.free.fr/) webcam drivers, developed with the assistance of reverse engineering, which are suitable for use with cameras from [a large number of manufacturers](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob;f=Documentation/video4linux/gspca.txt;hb=HEAD) including models from Aiptek, Creative, Logitech and Philips. Alongside the [uvcvideo](http://linux-uvc.berlios.de/) USB video driver, which was integrated into Linux 2.6.26 at the last minute, the Linux kernel will provide support for a wide range of video cameras. Linux users previously had to accept the inconvenience of installing these drivers separately.

Torvalds has also made [major changes](http://thread.gmane.org/gmane.linux.network/100274) to the network subsystem, including the "[Linux TX Multiqueue Implementation](http://vger.kernel.org/~davem/davem_seattle08.pdf)", written in large part by network administrator David S. Miller. This now gives the network stack the ability to function with several hardware transmit queues. Many of the modern Wifi chips provide these to allow [priority to be given](http://lwn.net/Articles/289137/) to the transmission of video or audio data. There have also been major changes in the drivers for the newer WiFi chips from Intel. Driver iwl4965 has been substantially rewritten, allowing parts of it to be reused by the iwl5000 driver, introduced at the same time. The latter supports the new "[Wireless WiFi Link 5000AGN](http://www.intel.com/network/connectivity/products/wireless/adapters/5000/index.htm)" series of wireless network adapters from Intel, which are used by the [recently launched Centrino 2 platform](../site/news/item/Intel-launches-Centrino-2-736483.html "Intel launches Centrino 2 – 16 July 2008, 12:31"). However, the new driver cannot handle WiMAX which is supported by some of Intel's wireless modules. Intel is helping with [several projects](http://linuxwimax.org/) aimed at providing patches and utility programs to deal with this limitation. The kernel hackers are reworking the rtl8187 driver for the Realtek USB wireless chip of the same name (which has been part of the kernel since Linux 2.6.23) to ensure that it can deal with the Realtek RTL8187B chip. With budget laptops, we have found that we had to persuade the wireless chip to work with a driver provided by the manufacturer, which proved extremely complicated to install. A major rewrite of the rfkill framework was also undertaken for 2.6.27, designed to improve the interaction between hardware, kernel and userspace programs when using the key and key combinations (found on laptops in particular) used to turn wireless communications on and off.

The kernel developers have integrated numerous [improvements](http://thread.gmane.org/gmane.comp.emulators.kvm.devel/19733) to the KVM virtualization solution and provided support for the Hypervisor paravirt_ops interface in the IA64 architecture used on Intel's Itanium. Xen DomU support for x86-64 systems finds its way into the kernel by way of [phase \#2](http://thread.gmane.org/gmane.linux.kernel/709758/) of updates for the x86 architecture – from 2.6.23 onwards, the kernel code has only supported x86-32 Linux under a Xen hypervisor The kernel still does not contain code for running a privileged Xen domain (Dom0).

AMD has released [Version 8.7](http://ati.amd.com/support/drivers/linux/linux-radeon.html) of the proprietary Linux graphics driver for newer Radeon graphics chips. The [Release Notes](http://www2.ati.com/drivers/linux/catalyst_87_linux.html) contain information on the limited number of new features provided. Unfortunately, the driver still does not support the pre-release version of the X-server scheduled for X.Org 7.4, which is used in Fedora  9 and in the current alpha release of Ubuntu 8.10.

**Kernel Log In Brief**:

- Adrian Bunk has [released version 2.6.16.62](http://thread.gmane.org/gmane.linux.kernel/709907) of the kernel, which corrects two security holes in CVE entries.

<!-- -->

- Following another request for ZFS support [in Linux](http://thread.gmane.org/gmane.linux.kernel/708280/), it looks as if [a programmer assisted by Christoph Hellwig](http://thread.gmane.org/gmane.linux.kernel/708280/focus%3D24977) will attempt to develop ZFS read-only support for the kernel code.

<!-- -->

- The recently announced [udev version 125](http://thread.gmane.org/gmane.linux.hotplug.devel/12844) uses a new location for the default udev rules.

<!-- -->

- [In his blog, Intel and X.org developer Keith Packard](http://keithp.com/blogs/X_output_status_july_2008/) provides a useful overview of the background and development status of kernel mode setting, initial mode selection, output hotplug, GEM DRI2 and other developments that the X.org and kernel developers are working on in an attempt to improve support for modern graphics hardware.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel log: ath9k driver for new Atheros wireless chips, discussions of Nvidia drivers](../site/news/item/Kernel-log-ath9k-driver-for-new-Atheros-WLAN-chips-discussions-of-Nvidia-drivers-736563.html "Kernel log: ath9k driver for new Atheros WLAN chips, discussions of Nvidia drivers – 22 July 2008, 15:48")
- [Kernel Log: No unstable series; Linux 2008.7, dealing with security fixes](../site/news/item/Kernel-Log-No-unstable-series-Linux-2008-7-dealing-with-security-fixes-736557.html "Kernel Log: No unstable series; Linux 2008.7; dealing with security fixes – 22 July 2008, 01:47")
- [Polish and add-ons; What's new in Linux 2.6.26](../site/open/features/Polish-and-add-ons-the-latest-updates-in-Linux-2-6-26-746492.html "Polish and add-ons; the latest updates in Linux 2.6.26 – 18 July 2008, 10:22")
- [Kernel Log: Linux-staging branch will help with integration; Linux kernel 2.6.25.6 and 2.6.26-rc6](../site/news/item/Kernel-Log-Linux-staging-branch-will-help-with-integration-Linux-kernel-2-6-25-6-and-2-6-26-rc6-735507.html "Kernel Log: Linux-staging branch will help with integration; Linux kernel 2.6.25.6 and 2.6.26-rc6 – 17 June 2008, 11:31")
- [Kernel log: New graphics drivers and stable kernels; details about Linux-staging](../site/news/item/Kernel-log-New-graphics-drivers-and-stable-kernels-details-about-Linux-staging-736303.html "Kernel log: New graphics drivers and stable kernels; details about Linux-staging – 26 June 2008, 15:45")
- [Kernel-Log: Users of 2.4 provide feedback, 2.4.36.5 and 2.6.26-rc5 released](../site/news/item/Kernel-Log-Users-of-2-4-provide-feedback-2-4-36-5-and-2-6-26-rc5-released-735437.html "Kernel-Log: Users of 2.4 provide feedback, 2.4.36.5 and 2.6.26-rc5 released – 10 June 2008, 15:20")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).*

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
