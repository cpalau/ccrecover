---
title: "Kernel Log: 2.6.27 nearing completion; Btrfs to be added to the kernel?"
date: 2008-10-01
author:
source: http://www.h-online.com/open/news/item/Kernel-Log-2-6-27-nearing-completion-Btrfs-to-be-added-to-the-kernel-737489.html
pages: 1
---

# Kernel Log: 2.6.27 nearing completion; Btrfs to be added to the kernel?

Linus Torvalds [hinted](http://thread.gmane.org/gmane.linux.kernel/738562) that the eighth release candidate (RC) of Linux 2.6.27, would be the last RC prior to release of the next major kernel revision saying "So yet another week, another -rc. This one should be the last one". Usually, once such a hint is dropped, it takes one to two weeks for the next version to be released, but then it is not unusual for yet another RC to appear despite such signals.

Torvalds pointed out, however, that there are still [regressions](http://thread.gmane.org/gmane.linux.power-management.general/11850), new issues which were not apparent problems on 2.6.26. His comments led to [further discussion](http://thread.gmane.org/gmane.linux.kernel/738562/focus%3D738578) about the problem of damaged Intel network hardware believed to be associated with the e1000e driver and the version 2.6.27 release candidates ([1](../site/news/item/Intel-e1000e-user-Don-t-install-the-new-SUSE-betas-737395.html "Intel e1000e user? Don't install the new SUSE betas – 23 September 2008, 09:14"), [2](../site/news/item/Kernel-Log-Kernel-Summit-info-Plumbers-keynote-online-the-latest-on-the-e1000e-problem-737443.html "Kernel Log: Kernel Summit info; Plumbers keynote online; the latest on the e1000e problem – 26 September 2008, 10:59")). According to the latest [status report](http://thread.gmane.org/gmane.linux.kernel/738484), posted by Intel developer Jesse Brandeburg, developers still have not found the exact cause of the problem. That is why no one is really sure if the [patches](http://thread.gmane.org/gmane.linux.kernel/738629/) that Brandeburg and other kernel hackers have developed actually prevent damage to data in the network EEPROM.

While Brandeburg and numerous other kernel hackers\]continue to search for the cause of the bug, other developers have already announced wish lists of new functions and improvements that they would like to incorporate into version 2.6.28. In future, the Libata subsystem [will support disk shock protection](http://thread.gmane.org/gmane.linux.ide/34792), for instance, and four new drivers for network chips manufactured by [Atheros, Cisco, Jmicron and Qlogic will be added](http://thread.gmane.org/gmane.linux.network/106250). KVM's developers have already prepared three series of patches ([1](http://thread.gmane.org/gmane.comp.emulators.kvm.devel/22083), [2](http://thread.gmane.org/gmane.comp.emulators.kvm.devel/22312), [3](http://thread.gmane.org/gmane.comp.emulators.kvm.devel/22505)); patches contained in this series will give KVM guests access to PCI devices.

------------------------------------------------------------------------

Chris Mason has transferred the source code of the experimental [Btrfs file system](http://btrfs.wiki.kernel.org/) into a Git repository. This move is [intended to make it easier for other kernel hackers to evaluate the file system](http://thread.gmane.org/gmane.linux.file-systems/26246) and to stimulate discussions about incorporating it into the Linux main development branch. Mason believes that it would be best to continue development of the file system from now on within the framework of the official Linux kernel. If this were to happen, it should be with the caveat that Btrfs is not intended for everyday use, in much the same way that developers treat the Ext4 file system, which kernel hackers have been working to complete within the framework of the Linux main development branch since version 2.6.19.

While the main development phase of Ext4 draws to a close in tandem with version 2.6.27, Btrfs still needs quite a bit of work before the file system is ready for users. For example, the on-disk format of the file system has not been finalised yet – Mason is hoping to nail down the format by the end of this year. The system for handling bugs is also in need of improvement. The [to-do list](http://btrfs.wiki.kernel.org/index.php/Development_timeline) on the [Btrfs wiki](http://btrfs.wiki.kernel.org/) lists numerous functions planned for the [file system](../site/news/item/Kernel-Log-Btrfs-0-16-released-new-stable-kernels-released-Wifi-drivers-for-2-6-27-merged-736815.html "Kernel Log: Btrfs 0.16 released, new stable kernels released, Wifi drivers for 2.6.27 merged – 08 August 2008, 14:32"), which has caught the attention of kernel developers and has been praised by Ext file system developer Theodore Ts'o and others.

**In Brief**

- Linux developers want to use the [newly established linux-api mailing list](http://thread.gmane.org/gmane.linux.ltp/5658/) to discuss changes to the API ([application programming interface](http://en.wikipedia.org/wiki/API)) and ABI ([application binary interface](http://en.wikipedia.org/wiki/Application_binary_interface)) between the kernel and userland.

<!-- -->

- Following the [release of the HAL source code](../site/news/item/Open-source-Atheros-HAL-to-help-Wifi-developers-under-Linux-737467.html "Open source Atheros HAL to help Wifi developers under Linux – 29 September 2008, 13:42") for various Atheros WiFi chips, the first [patches](https://lists.ath5k.org/pipermail/ath5k-devel/2008-September/001311.html) for the ath5k driver developed with the help of information found in the source code [are appearing](http://thread.gmane.org/gmane.linux.kernel.wireless.general/21379/focus%3D1253).

<!-- -->

- [Hplip project](http://hplipopensource.com/) developers have released [version 2.8.9](http://hplipopensource.com/hplip-web/release_notes.html) of the Hplip driver for HP printers and multifunction devices. It supports the scan function of certain LaserJet series devices for the first time, as well as five new Photosmart series printers.

<!-- -->

- Recently, Nvidia has been releasing new beta drivers for Linux on an almost weekly basis – the [newest](http://www.nvnews.net/vbulletin/showthread.php?t=120052) carry the version number, 177.78.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: Kernel Summit info; Plumbers keynote online; the latest on the e1000e problem](../site/news/item/Kernel-Log-Kernel-Summit-info-Plumbers-keynote-online-the-latest-on-the-e1000e-problem-737443.html "Kernel Log: Kernel Summit info; Plumbers keynote online; the latest on the e1000e problem – 26 September 2008, 10:59")
- [Kernel Log: The second day of Kernel Summit 2008; criticism of Ubuntu at the opening of the Linux Plumbers Conference](../site/news/item/Kernel-Log-The-second-day-of-Kernel-Summit-2008-criticism-of-Ubuntu-at-the-opening-of-the-Linux-Plumbers-Conference-737379.html "Kernel Log: The second day of Kernel Summit 2008; criticism of Ubuntu at the opening of the Linux Plumbers Conference – 19 September 2008, 15:58")
- [Kernel Log: Hard core Linux developers discuss the future of Linux at the Kernel Summit](../site/news/item/Kernel-Log-Hard-core-Linux-developers-discuss-the-future-of-Linux-at-the-Kernel-Summit-737327.html "Kernel-Log: Hard core Linux developers discuss the future of Linux at the Kernel Summit – 17 September 2008, 11:48")
- [Kernel Log: New stable and developer kernel, Mesa 7.1 and X-Server 1.5 released](../site/news/item/Kernel-Log-New-stable-and-developer-kernel-Mesa-7-1-and-X-Server-1-5-released-737227.html "Kernel-Log: New stable and developer kernel, Mesa 7.1 and X-Server 1.5 released. – 09 September 2008, 15:02")
- [Kernel Log: New stable and pre-release kernels, Ubuntu 8.10 with 2.6.27?](../site/news/item/Kernel-Log-New-stable-and-pre-release-kernels-Ubuntu-8-10-with-2-6-27-737021.html "Kernel Log: New stable and pre-release kernels, Ubuntu 8.10 with 2.6.27? – 25 August 2008, 11:32")
- [Kernel Log: New video drivers for AMD, Intel, Nvidia and VIA hardware](../site/news/item/Kernel-Log-New-video-drivers-for-AMD-Intel-Nvidia-and-VIA-hardware-736997.html "Kernel Log: New video drivers for AMD, Intel, Nvidia and VIA hardware – 22 August 2008, 11:59")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
