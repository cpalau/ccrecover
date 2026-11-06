---
title: "Kernel Log: Long-term maintenance for 2.6.32, util-linux-ng extended"
date: 2010-01-22
author: "Chris von Eitzen"
source: http://www.h-online.com/open/news/item/Kernel-Log-Long-term-maintenance-for-2-6-32-util-linux-ng-extended-910616.html
pages: 1
---

# Kernel Log: Long-term maintenance for 2.6.32, util-linux-ng extended

**Chris von Eitzen**

#### by Thorsten Leemhuis

**![Kernel Log Logo](../site/imgs/43/4/7/0/9/6/8/KL.jpg-1f663d67fe8a53b0.jpeg) Linux 2.6.32 is to be maintained for 2 to 3 years within the stable series – the maintenance of 2.6.27, however, will probably soon be discontinued or at least downscaled considerably. The util-linux-ng tool collection now contains three additional programs; fdisk provides optimised partitioning. The configuration of X Server has become more flexible and now HAL is no longer needed.**

Shortly after releasing three new stable kernels, [2.6.27.44](http://thread.gmane.org/gmane.linux.kernel/939790), [2.6.31.12](http://thread.gmane.org/gmane.linux.kernel/939786) and [2.6.32.4](http://thread.gmane.org/gmane.linux.kernel/939788), stable series co-maintainer Greg Kroah-Hartman has presented his maintenance plan for the stable series kernels in [an email](http://thread.gmane.org/gmane.linux.kernel/939800) to the LKML.

The maintenance of the 2.6.27 series, which is the current "long-term stable release", is set to continue into the near future. However, the developer warns the users of series 27 kernels that this series is now ageing and losing viability ("*But, I do have to warn users of this tree, the older it gets, the less viable it becomes.*"). He said that Linux has changed quite dramatically in the two years since [2.6.27](../site/open/features/Kernel-Log-Linux-2-6-27-Released-746496.html "Kernel Log: Linux 2.6.27 Released – 10 October 2008, 08:38") was released, and that this makes it more and more difficult to port changes designed for newer kernels to 2.6.27. Although Kroah-Hartman intends to continue maintaining the series 27 kernels for at least another six to eight months, he doesn't know whether he will want to keep going after that time ("*I'll probably keep maintaining it for at least 6-8 more months, but after that, I can not guarantee its viability.*"). However, Willy Tarreau, who currently maintains the 2.4 series, is [considering](http://thread.gmane.org/gmane.linux.kernel/939800/focus%3D940310) whether to take on the maintenance of the series 27 kernels at that point; although if he does he only intends to fix critical flaws.

As 2.6.28, 2.6.29 and 2.6.30 have not been maintained for some time, the now released 2.6.31-based version is to be the final series 31 kernel – Greg Kroah-Hartman therefore advises all those who still use this series to switch to a kernel that is based on [Linux version 2.6.32](../site/open/features/What-s-new-in-Linux-2-6-32-872271.html "What's new in Linux 2.6.32 – 03 December 2009, 08:22"), which was released in December.

Series 2.6.32 is to become the next "long-term stable release" after the series 2.6.27 kernels. According to Kroah-Hartman, at least two distributors use Linux 2.6.32 in their "Enterprise" distributions with long-term maintenance. The developer hopes to maintain the series 32 kernels for two to three years, but pointed out that he will need the support of the distribution developers to do so. Kroah-Hartman said that, failing their support, he will have no problem with discontinuing the maintenance of this series.

### Linux version status

As is often the case in their release emails, the maintainers of the stable series have strongly advised users to switch to the new stable kernels, without mentioning whether any of the bug fixes and improvements actually address security issues. However, the new series 31 and 32 versions fix at least the [CVE-2010-0006](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2010-0006) [problem](http://seclists.org/oss-sec/2010/q1/25) for which some distributors have released a kernel update.

Meanwhile, the development of Linux 2.6.33 is progressing at the usual speed. The latest release candidate is [2.6.33-rc5](http://thread.gmane.org/gmane.linux.kernel/941205). Given the usual rate of development, 2.6.33 is likely to be released in late February or early March. Progress also continues in the stable series, as 2.6.32.5 is already [in preparation](http://thread.gmane.org/gmane.linux.kernel/940841) and will probably be released this weekend.

### Standard tools

Karel Zak has recently [released](http://thread.gmane.org/gmane.linux.file-systems/37606) version 2.17 of the util-linux-ng tool collection, which is used in all the major Linux distributions. The collection includes the fdisk program, which now attempts to align new partitions to sector or chunk size boundaries – this particularly optimises the performance of RAID arrays and of hard disks with a physical sector size of 4 Kbytes, which are expected to become available in the near future, and prevents redundant read/write operations. However, the developers [are already discussing](http://thread.gmane.org/gmane.linux.file-systems/37606/focus%3D37614) further changes in this area and are contemplating whether to align partitions to Megabyte boundaries by default, an approach that is familiar from Windows Vista and Windows 7.

The tool collection has been extended to include three command line tools. The "fallocate" tool allows pre-allocating a data storage area in file systems with fallocate support, enabling the file system's data to be stored in continuous portions – that is, with hardly any or with no fragmentation at all. The "wipefs" tool removes file system and RAID signatures to prevent them from becoming a problem when the storage medium is used at a later stage. The "unshare" tool allows file systems to be implemented in such a way that they are only visible within the context (namespace) of the respective shell – Zak offers a practical example of this [in his blog](http://karelzak.blogspot.com/2009/12/unshare1.html).

### X.org

At the beginning of the month, the X.org developers released the [xf86-video-vmware 10.16.9](http://lists.freedesktop.org/archives/xorg-announce/2009-December/001229.html) and [xf86-video-vesa 2.3.0](http://lists.freedesktop.org/archives/xorg-announce/2010-January/001230.html) graphics drivers. Shortly after, Intel [released](http://thread.gmane.org/gmane.comp.freedesktop.xorg/41865) version 2.10.0 of the X.org xf86-video-intel driver, which is usually just called "intel". This is the first version to require a kernel with KMS support. The developers recommend using at least Linux 2.6.32. With 2.6.33 or a patched 2.6.32, the driver is also said to support video overlays. The developer say they have also fixed a few performance glitches. The new driver is also a component of the "Intel 2009Q4 release", which [became available](http://thread.gmane.org/gmane.comp.freedesktop.xorg/41895) shortly afterwards and references suitable versions of Mesa and Libdrm.

Dave Airlie recently [released](http://lists.freedesktop.org/archives/xorg-announce/2010-January/001235.html) the first version of the xf86-video-qxl (short name: QXL) graphics driver, which was developed within the context of X.org and supports the virtual GPU feature of the [Spice](http://spice-space.org/) virtualisation protocol. Spice is, for instance, used in Red Hat Enterprise Linux.

### In brief

**Kernel**

- In his "[XFS status update for December 2009](http://thread.gmane.org/gmane.linux.kernel/936936)", Christoph Hellwig gives an overview of the latest developments in the XFS file system area.

**Kernel environment ("plumbing layer") and userland drivers**

- Lennart Poettering has presented the graphical [udev-browse](http://0pointer.de/blog/projects/udev-browse.html) UI for Sysfs, which saves having to type complex "udevadm info" calls. Sysfs is usually integrated at /sys level.
- Clark Williams has [released](http://thread.gmane.org/gmane.linux.rt.user/5434) version 0.6.0 of the rt-tests collection mainly used in real time environments.
- At Christmas, Stephen Hemminger [released](http://article.gmane.org/gmane.linux.network.general/13501) version 2.6.32 of the iproute collection of network configuration tools, which offers more comprehensive Linux 2.6.32 support than previous versions of iproute.

**Graphics**

- The developers of **nouveau** have [removed](http://cgit.freedesktop.org/nouveau/xf86-video-nouveau/commit/?id=17485c234ff191cee3dd19e3dd693a80b024e189) numerous code segments for kernels without Kernel-based Mode Setting (KMS) from the X.org driver. The driver will, therefore, from now on require a kernel with **nouveau** KMS support.
- The X developers have integrated several changes into the development branch that were mainly developed by Dan Nicholson and Julien Cristau and introduce considerable modifications to the code for hot plugging and configuring devices. As a result, X Server 1.8 now accesses Udev directly instead of using HAL. Like the current versions of X Server, version 1.8 is designed to work without a configuration file – however, if the need for manual configuration does arise, X Server can now assemble the configuration from individual files stored in /etc/X11/xorg.conf.d/. Find background information about these and other changes [in a blog post](http://who-t.blogspot.com/2010/01/new-configuration-world-order.html) by Peter Hutterer.

Older Kernel Logs can be found in *[the archives](../site/open/news/archive/)* or by using *[the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log)* at *[The H Open Source](../site/open/)*. New editions of Kernel Logs are also mentioned on [Identi.ca](http://identi.ca/kernellog2) and [Twitter](http://twitter.com/kernellog2) via "@kernellog2". The Kernel Log author also posts updates about various topics on [Identi.ca](http://identi.ca/kernellogauthor) and [Twitter](http://twitter.com/kernellogauthor) via "@kernellogauthor".

([thl](mailto:thl@ct.de)/c't)

([crve](mailto:crve@h-online.com "Chris von Eitzen "))
