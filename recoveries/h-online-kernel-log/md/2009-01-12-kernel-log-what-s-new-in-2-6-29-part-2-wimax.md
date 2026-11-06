---
title: "Kernel Log: What's new in 2.6.29 - Part 2: WiMAX"
date: 2009-01-12
author:
source: http://www.h-online.com/open/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-2-WiMAX-739621.html
pages: 1
---

# Kernel Log: What's new in 2.6.29 - Part 2: WiMAX

![](../site/imgs/43/3/6/6/0/5/3/93e8ea3d0acdf147.jpg) *In Part 2 of the Kernel Log's coverage of the major changes happening in the main development branch for the Linux kernel 2.6.29 release, we look at a major new addition to Linux's networking capability, WiMAX support.*

USB sub-system maintainer [Greg Kroah-Hartman](http://thread.gmane.org/gmane.linux.usb.general/13618) has brought the WiMAX stack, developed primarily by Intel developers in the framework of the [Linux WiMAX project](http://www.linuxwimax.org/), into the Linux main development branch.

The stack gives Linux 2.6.29 a basic infrastructure for [WiMAX](http://en.wikipedia.org/wiki/WiMAX) wireless broadband networking technology based on the i2400m USB driver, which was also developed by the WiMAX project and concurrently integrated into the kernel. The WiMAX stack communicates with the [WiMAX Connection 2400](http://www.intel.com/technology/wimax/2400.htm?iid=tech_wimax_products+2400) chip in [Intel Wireless WiMAX/WiFi Link 5150 and 5350](http://www.intel.com/network/connectivity/products/wireless/wimax/wifi/index.htm) (codename: Echo Peak) WLAN/WiMAX modules, found mainly in newer Centrino notebooks.

As the change log in the ultimately successful [e-mail request for integration](http://lists.moblin.org/pipermail/wimax/2008-December/000356.html) shows, Linux WiMAX developers made a number of attempts before the network and USB sub-system administrators were satisfied with the code and gave it the green light for integration into the kernel. Numerous details and background information on the Linux kernel's new WiMAX infrastructure can be found in the e-mail mentioned above, by following the links at the end of this article to commits in the source code administration system, and on the [Linux WiMAX website](http://www.linuxwimax.org/).

Also, on the website you can [download the i2400m firmware](http://linuxwimax.org/Download) and the corresponding userspace software. However, the Intel WiMAX binary supplicant needed for authentication with the remote host, as well as the Intel WiMAX binary OMADM client are only available online as a pre-compiled archive ([license](http://linuxwimax.org/Licenses/IFDBL-WiMAX-Supplicant), [FAQ](http://linuxwimax.org/FAQ#head-0ea15b2ca62971641d34519700e71a13dda107e0)). Therefore, distributions based solely on open source software, such as Debian, Fedora and OpenSuse, will not yet include these parts of the userspace stack in their core distributions. However, in the e-mail mentioned above, Intel developers do say "For networks that require authentication (most), the Intel device requires a supplicant in user space – because of a set of issues we are working to resolve, it cannot be made open source yet, but it will".

See – [Part 1 of Whats new in 2.6.29](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-1-Dodgy-Wifi-drivers-and-AP-support-739619.html "Kernel Log: What's new in 2.6.29 - Part 1: Dodgy Wifi drivers and AP support – 11 January 2009, 16:08").

**The WiMAX Changes in detail**

- [i2400m: debugfs controls](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=c71228caf91ec6320b489dec5cd0087b64da9fb5)
- [i2400m: documentation and instructions for usage](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3e91029ae049852c153da3fc355ab255ea7e2e0a)
- [i2400m: firmware loading and bootrom initialization](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=467cc396fb4665957bc7d182c96e45a4d7c575e4)
- [i2400m: Generic probe/disconnect, reset and message passing](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=024f7f31ed15c471f80408d8b5045497e27e1135)
- [i2400m: host/device procotol and core driver definitions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ea24652d253eabfb83e955e55ce032228d9d99b9)
- [i2400m: linkage to the networking stack](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ce6cde92803e961d95ddacdf74bd8b067f82f7d4)
- [i2400m: Makefile and Kconfig](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=143ee2d5557c0598a97f3089eb29e8226e0e8cee)
- [i2400m: RX and TX data/control paths](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=aa5a7acabe31ec27a212cbd25cad9f72aa476591)
- [i2400m/SDIO: firmware upload backend](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=020bb6f30b636d563d4268116107d592550ddd0c)
- [i2400m/SDIO: header for the SDIO subdriver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=17d559af963995e483a51ec26697034431bcf2b9)
- [i2400m/SDIO: probe/disconnect, dev init/shutdown and reset backends](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a0848826bfaf0815ec9654d78c218a40f755ccd4)
- [i2400m/SDIO: TX and RX path backends](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=514ec71f7289c942f801bdbd309428c470bfc071)
- [i2400m/USB: firmware upload backend](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=795038107b0078ee5ad3ad33327fe1c3520f6bf2)
- [i2400m/USB: header for the USB bus driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=11a7d0e3140d2f3e8052a856e8582ce9b021972c)
- [i2400m/USB: probe/disconnect, dev init/shutdown and reset backends](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=f398e4240fce962d0dd74dc11c59fe20860e7a71)
- [i2400m/USB: TX and RX path backends](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a8ebf98f541463107bb9544a1b611981dc2477e7)
- [i2400m/usb: wrap USB power saving in \#ifdef CONFIG_PM](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=9fd7a1d92b4462acaa460bb0f58b12ede6ffe6b9)
- [i2400m: various functions for device management](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3a35a1d0bdf7cc32cddc234b956605e6d4db4673)
- [wimax: basic API: kernel/user messaging, rfkill and reset](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=3e65646bb12be03b14dff53907391095a52d5f49)
- [wimax: debugfs controls](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=617209ccf73b571953cf4c76519c65a5e52d15fd)
- [wimax: debug macros and debug settings for the WiMAX stack](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ea912f4e7f264981faf8665cfb63d46d7f948117)
- [wimax: documentation for the stack](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0d695913b0016b362a84a8bb6d6e28f8d90a70e2)
- [wimax: export linux/wimax.h and linux/wimax/i2400m.h with headers_install](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e30698743419d20dce03d033761f203b4d847ab0)
- [wimax: fix kconfig interactions with rfkill and input layers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=71f78afd67ca51d3656ba45aea293d6e2a27c8bc)
- [wimax: generic device management (registration, deregistration, lookup)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=15530dfd330bd19d14e096f88c70355a61fda3f2)
- [wimax: headers for kernel API and user space interaction](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=ace22f0881e1333d0c55ddf484e5352fe03a806a)
- [wimax/i2400m: add CREDITS and MAINTAINERS entries](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=8a70da82edc50aa7a4b54864babf2d72538ba1bb)
- [wimax: internal API for the kernel space WiMAX stack](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=60fa9ca6cfff2be4132ea93b7dd632801ec0c817)
- [wimax: Makefile, Kconfig and docbook linkage for the stack](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=b0c83ae1de01880075955c7224e751440688ec74)

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: What's new in 2.6.29 - Part 1: Dodgy Wifi drivers and AP support](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-1-Dodgy-Wifi-drivers-and-AP-support-739619.html "Kernel Log: What's new in 2.6.29 - Part 1: Dodgy Wifi drivers and AP support – 11 January 2009, 16:08")
- [Kernel Log: 2.6.29 development kicks off, improved 3D support](../site/news/item/Kernel-Log-2-6-29-development-kicks-off-improved-3D-support-739551.html "Kernel Log: 2.6.29 development kicks off, improved 3D support – 05 January 2009, 17:29")
- [Kernel Log: Higher and Further, The innovations of Linux 2.6.28](../site/open/features/Kernel-Log-Higher-and-Further-The-innovations-of-Linux-2-6-28-746519.html "Kernel Log: Higher and Further, The innovations of Linux 2.6.28 – 23 December 2008, 15:55")
- [Kernel Log: What's coming in 2.6.28 - Part 9: Fastboot and other remainders](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-9-Fastboot-and-other-remainders-739431.html "Kernel Log: What's coming in 2.6.28 - Part 9: Fastboot and other remainders – 19 December 2008, 12:45")
- [Kernel Log: What's coming in 2.6.28 - Part 7: architecture support, memory subsystem and virtualisation](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-7-architecture-support-memory-subsystem-and-virtualisation-739397.html "Kernel Log: What's coming in 2.6.28 - Part 7: architecture support, memory subsystem and virtualisation – 17 December 2008, 10:35")
- [Kernel Log: What's coming in 2.6.28 - Part 6: Changes to the audio drivers](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-6-Changes-to-the-audio-drivers-739369.html "Kernel Log: What's coming in 2.6.28 - Part 6: Changes to the audio drivers – 15 December 2008, 17:53")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
