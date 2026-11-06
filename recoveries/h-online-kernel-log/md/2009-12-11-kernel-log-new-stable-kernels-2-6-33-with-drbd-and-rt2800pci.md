---
title: "Kernel Log: New stable kernels, 2.6.33 with DRBD and RT2800PCI"
date: 2009-12-11
author: "Chris von Eitzen"
source: http://www.h-online.com/open/news/item/Kernel-Log-New-stable-kernels-2-6-33-with-DRBD-and-RT2800PCI-883212.html
pages: 1
---

# Kernel Log: New stable kernels, 2.6.33 with DRBD and RT2800PCI

**Chris von Eitzen**

#### by Thorsten Leemhuis

**![](../site/imgs/43/4/5/5/3/6/1/KL.jpg-4677d3004996dcc3.jpeg) Kernel versions 2.6.27.40, 2.6.27.41 and 2.6.31.7 offer minor improvements and correct several bugs – including one security hole. Torvalds has already incorporated more than 5,000 changes for Linux 2.6.33. Its merge window will probably be open for just over another week. Various developers are working on significant improvements to the open source Radeon graphics drivers.**

### Development of Linux 2.6.33 under way

As usual, Linus Torvalds began integrating the first changes for version 2.6.33 of the Linux kernel immediately after the [release of Linux 2.6.32](../site/open/features/What-s-new-in-Linux-2-6-32-872271.html "What's new in Linux 2.6.32 – 03 December 2009, 08:22") last Thursday. Up to now Torvalds merged more than 5000 commits – 2900 of them found their way into the public [Git tree of Linux](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=summary) on Thursday evening and so were flooding the in-boxes of those who receive email notifications of all the commits in the main development branch through the [git-commits-head@vger.kernel.org](http://dir.gmane.org/gmane.linux.kernel.commits.head) mailing list. The changes included components such as the [DRBD](http://git.kernel.org/linus/b411b3637fa71fce9cf2acf0639009500f5892fe) (Distributed Replicated Block Device) replication solution used in High Availability (HA) environments – on the other hand, the developers [removed](http://git.kernel.org/linus/492af6350a5ccf087e4964104a276ed358811458) the Anticipatory IO Scheduler (AS), because, reportedly, it only offers some of the features included in CFQ ("*AS is mostly a subset of CFQ, so there's little point in still providing this separate IO scheduler*"). Among the many new drivers is [rt2800pci](http://git.kernel.org/linus/a9b3a9f7214b3acc56330c2257aeaa5fa85bf520) for Ralink's RT2860 and RT3090 PCI Wi-Fi chips – until now, these chips could only be addressed via drivers which haven't yet reached the quality levels required by the kernel developers.

As usual, most of the changes were inspected by the various kernel subsystem maintainers, who collect them in separate Git branches and then ask Torvalds to merge them into the main development branch via a Git-Pull request. That the Father of Linux does check the things he is asked to merge can be seen in the LKML discussion around the Git-Pull request submitted by the maintainer of the power management subsystem. In this exchange, [Torvalds seriously criticised](http://thread.gmane.org/gmane.linux.acpi.devel/43304/focus%3D43305) some of the patches collected for integration, sparking a prolonged discussion which is still ongoing.

The maintainer of the power management subsystem has since put the criticised changes on hold and submitted a new Git-Pull request for the rest of the patches, which have now been merged by Torvalds. Numerous further changes in other areas are likely to be merged over the week the merge window of 2.6.33 is still likely to remain open.

### Linux version status

The maintainers of the Linux Stable Series released Linux versions [2.6.27.40](http://thread.gmane.org/gmane.linux.kernel/924405), [2.6.27.41](http://thread.gmane.org/gmane.linux.kernel/924566) and [2.6.31.7](http://thread.gmane.org/gmane.linux.kernel/924404) on Tuesday night. As usual, these versions mainly offer minor corrections and improvements, although version 2.6.27.41 only corrects a [flaw introduced](http://thread.gmane.org/gmane.linux.kernel/924508) in 2.6.27.40.

The new 2.6.31 variant is one of the stable kernels with a comparatively large number of changes, and just under 120 patches have been integrated since the previous version. In their release emails, the maintainers of the Stable Series advise that all users of self-compiled previous kernel versions should update to the new Linux kernel. The maintainers give no detailed reasons or point out any security patches ("*All users of the 2.6.31 kernel series are very strongly encouraged to upgrade.*"). At least [one of the patches merged for 2.6.31.7](http://thread.gmane.org/gmane.linux.kernel/923376), however, fixes a security hole known as [CVE-2009-1298](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-1298) which some distributions have already corrected via [kernel updates](https://www.redhat.com/archives/fedora-package-announce/2009-December/msg00496.html).

New stable kernels that fix a [recently discovered hole](../site/news/item/Linux-kernel-vulnerabilities-closed-882270.html "Linux kernel vulnerabilities closed – 10 December 2009, 12:06") in the Ext4-Filesystem_Code have yet to appear, although Git posts for [2.6.31.8](http://thread.gmane.org/gmane.linux.kernel/925767) and [2.6.32.1](http://thread.gmane.org/gmane.linux.kernel/925781) indicate these kernel version should be available soon.

### In brief

**Kernel**

- Clemens Ladisch [is promoting the integration](http://thread.gmane.org/gmane.linux.drivers.sensors/20721/) of the k10temp driver which reportedly allows reading the temperature sensors in modern AMD CPUs. However, since many CPUs produce incorrect readings, the code to be [introduced in 2.6.33](http://thread.gmane.org/gmane.linux.drivers.sensors/20721/focus%3D917919) only works after a special parameter has been set.
- According to a [blog posting](http://laforge.gnumonks.org/weblog/2009/12/07#20091207-palm_sued_over_gpl_violation) by Harald Welte about the [potential GPL infringements of the Palm Pre smartphone](../site/news/item/Palm-sued-by-Artifex-over-PDF-renderer-GPL-violation-878893.html "Palm sued by Artifex over PDF renderer GPL violation – 07 December 2009, 13:45"), Palm use numerous proprietary kernel drivers that pretend to be under the GPL – the vendor was not able to provide the driver sources when prompted for them.

**Kernel environment ("plumbing layer")**

- Richard Hughes has [released](http://lists.freedesktop.org/archives/hal/2009-November/013671.html) version 0.5.14 of HAL, the software layer that handles negotiations between applications and kernel. According to the release email, this will probably be its last version from the Linux side – instead of the abstraction layer, many of the applications that used to be based on HAL now directly use software such as udev or libudev, and HAL has become increasingly unimportant in the Linux world.
- Douglas Gilbert has [released](http://thread.gmane.org/gmane.linux.scsi/56159) version 0.23 of lsscsi.
- Karel Zak has [released](http://thread.gmane.org/gmane.linux.utilities.util-linux-ng/2811) version 2.16.2 of util-linux-ng, which contains some corrections and minor improvements to hwclock, libblkid, mkswap, mount and sfdisk.
- Following the problems with the [recalled version](../site/news/item/Kernel-Log-Coming-in-2-6-32-Part-3-Storage-864376.html "Kernel Log: Coming in 2.6.32 (Part 3) - Storage – 20 November 2009, 17:40") 3.1.0 of mdadm, in the second half of November Neil Brown released version 3.1.1 of the program. He explicitly points out the major differences to the 3.0 series in [his release email](http://thread.gmane.org/gmane.linux.raid/25545).
- Zak already is working on 2.17, which will bring the new command unshare – Zak explains its use [in a recent blog post](http://karelzak.blogspot.com/2009/12/unshare1.html).

**Graphics**

- X.org developer Peter Hutterer recently [released](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/943/) version 1.7.2 of the X Server, whose various and mostly minor changes were intended to fix some problems of the previous versions in the 1.7 series. However, there was [a problem](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/943/focus%3D944) with the new version, prompting Hutterer to [provide](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/948) version 1.7.3 to fix it at short notice.
- Kristian Høgsberg has [released](http://article.gmane.org/gmane.comp.video.dri.devel/40707) version 2.4.16 of the libdrm. The Intel developer writes that this version contains numerous changes – for instance, the developers have removed orphaned Linux and BSD drivers.
- The X developers also want to move on from the above-mentioned HAL and [recently](http://thread.gmane.org/gmane.comp.freedesktop.xorg.devel/3614) [summarised](http://www.x.org/wiki/XorgHAL) their plans to this effect in their wiki.
- Peter Hutterer has released versions [0.10.1](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/939) and [0.10.2](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/945) of the still emerging xf86-input-wacom driver. This driver is a fork [developed from](http://thread.gmane.org/gmane.linux.drivers.wacom.devel/50) the [linuxwacom](http://linuxwacom.sourceforge.net/) driver for Wacom graphics tablets at X.org and Freedesktop.org.
- Developer Alex Deucher, who works for AMD, has [introduced](http://thread.gmane.org/gmane.comp.video.dri.devel/40576) DRM patches which add interrupt support to the drivers for Radeon's series R600 and R700 GPUs – this allows monitor changes to be detected without polling and the display of new screen content to be better synchronised with the image changes. Rafal Milecki [has been working](http://thread.gmane.org/gmane.comp.video.dri.devel/40339) on code that dynamically adjusts the clock speed of Radeon GPUs and their memory depending on load; [in his blog](http://airlied.livejournal.com/68805.html), Dave Airlie reports about the progress made in terms of DisplayPort support in the driver code for Radeon graphics hardware.
- In their blogs, [Matthew Garrett](http://mjg59.livejournal.com/118588.html) and [Peter Hutterer](http://who-t.blogspot.com/2009/11/shm-config-in-synaptics.html) explain why it is unwise to enable the "SHMConfig" option in old versions of the synaptics touchpad driver.

For articles on the previous 2.6.32 kernel and links to the "Coming in 2.6.32 " series, see [The H's Kernel Log - 2.6.32 Tracking page](../site/open/features/2-6-32-Tracking-816707.html "2.6.32 Tracking – 05 October 2009, 17:04").

([thl](mailto:thl@ct.heise.de))

([crve](mailto:crve@h-online.com "Chris von Eitzen "))
