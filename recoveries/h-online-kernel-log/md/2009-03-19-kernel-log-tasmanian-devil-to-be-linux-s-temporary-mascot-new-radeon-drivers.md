---
title: "Kernel Log: Tasmanian devil to be Linux's temporary mascot, new Radeon drivers"
date: 2009-03-19
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-Tasmanian-devil-to-be-Linux-s-temporary-mascot-new-Radeon-drivers-740667.html
pages: 1
---

# Kernel Log: Tasmanian devil to be Linux's temporary mascot, new Radeon drivers

**Dj Walker-Morgan**

![Tuz](../site/imgs/43/3/6/7/0/9/9/8dec25a68156dc3d.jpg) Tuz, a Tasmanian devil, is temporarily taking over the role of Tux Source: Linux Kernel: Created by Andrew McGown and Josh Bush With a [commit introduced](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8032b526d1a3bd91ad633dd3a3b5fdbc47ad54f1) on Tuesday evening into the main development tree, Linus Torvalds granted [the Linux mascot](http://en.wikipedia.org/wiki/Tux,), a [three-month sabbatical](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob_plain;f=Documentation/logo.txt;h=a2e62445e28ee523c02f5f93f80c06a431e369e3). Tuz, an image of a [Tasmanian devil](http://en.wikipedia.org/wiki/Tux) wearing a false yellow nose as a reminder of the Linux penguin, will replace Tux in Linux version 2.6.29.

Tuz has already served as a mascot for the Linux conference [linux.conf.au](http://linux.conf.au/) (LCA) held earlier this year in Hobart, Tasmania, and its temporary role as the Linux mascot is intended to highlight the threat to the survival of the species, which lives exclusively on the island of Tasmania, from the relatively new [Devil Facial Tumour Disease](http://en.wikipedia.org/wiki/Devil_facial_tumour_disease)" (DFTD). Torvalds recommends the [URL](http://tassiedevil.com.au) for further background information about an appeal for donations by its [supporters](http://tassiedevil.com.au/supporters.html).

### Kernel status

On Tuesday 17 Marth, Greg Kroah-Hartman released the stable kernels [2.6.27.20](http://thread.gmane.org/gmane.linux.kernel/808157) and [2.6.28.8](http://thread.gmane.org/gmane.linux.kernel/808156), each containing around a hundred small corrections and extensions. In his release email for the new 2.6.28 version, Kroah-Hartman emphatically advises all users of self-compiled kernels to update to the new version. As so often before, however, he doesn't say whether this gets rid of security vulnerabilities or other serious errors.

The development of 2.6.29 has now reached rc8. [When releasing it](http://thread.gmane.org/gmane.linux.kernel/806262) last Friday, Torvalds intimated that this could be the last RC of 2.6.29, as the main development tree of the kernel is stabilising, but he's unwilling to exclude the possibility of further pre-release versions: "*\[...\]it seems to be stabilizing to the point where I'm hoping that we're approaching a final 2.6.29, and this might be the last -rc. We'll have to see."*.

However, in view of the number and extent of the changes accepted in recent days, a further pre-release version looks likely. Among the last-minute changes, besides Tuz, there are also two new network drivers: [be2net](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6b7c5b947c671a96e39f9526a5fd70c178b8dfd1) for the BladeEngineÂ 2 10-Gigabit LAN chips by ServerEngines, and [dnet](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4796417417a62e2ae83d92cb92e1ecf9ec67b5f5) for the Dave DNET Ethernet controller integrated into the Dave/DENX QongEVB-LITE field-programmable gate array (FPGA).

Shortly after the Kernel Log addressed the [changes](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-6-Storage-IDE-PATA-SCSI-740501.html "Kernel Log: What's new in 2.6.29 - Part 6: Storage, IDE/PATA, SCSI â 13 March 2009, 13:45"), some of them far-reaching, to the old Integrated Device Electronics (IDE) subsystem as part of the "What's new in 2.6.29" miniseries, Bartlomiej Zolnierkiewicz explained his motives for the changes and explained his future plans in more detail [in an email to the Linux Kernel Mailing List (LKML)](http://thread.gmane.org/gmane.linux.ide/39009): "*The subsystem is in good shape now so I think that no more radical changes like the ones that happened recently will be needed. We will just concentrate on keeping things working till better solutions take over.*".

### All about X.org

The AMD developer Alex Deucher has released version 6.12.0 of the [xf86-video-ati](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/583) driver package, usually called "ati" for short. The "[radeon](http://wiki.x.org/wiki/radeon)" driver it contains, together with a current DRM (Direct Rendering Manager), is said now to support the EXA and Xv (Xvideo) acceleration methods for the R6xx and R7xx GPUs that are found on Radeon graphics hardware in the 2000, 3000 and 4000 series. According to the release email, the driver can now also handle rotating the image on these GPUs, and enable output via DisplayPort. However, the information [given in the X.org Wiki](http://www.x.org/wiki/DisplayPort) says this doesn't work with older Radeon GPUs, or with all DisplayPort devices.

The developers of the Intel graphics driver are now working on the next big milestone, and have issued the first two pre-release versions of the 2.7 driver range ([1](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/581) and [2](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/582)). Fedora developer Will Woods meanwhile explains [in his blog](http://qa-rockstar.livejournal.com/7869.html) why he doesn't think much of glxgears as a benchmark. Testers of Fedora 11 pre-release versions had previously found that KMS and DRI2 gave great breakthroughs in frame rates.

### In Brief

- An [article at LinuxDevices.com](http://linuxdevices.com/articles/AT9599126972.html) explains some internal details of the V4L2 APIs

<!-- -->

- The code of the definitive Tux3 filing system created by Daniel Phillips can now be found [in a git tree](http://thread.gmane.org/gmane.linux.kernel/805382/). He's hoping it will soon be accepted into the main development tree, and has already received some advice for review [from Andrew Morton](http://thread.gmane.org/gmane.linux.kernel/805382/focus%3D767)

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at The H Open Source:*

- [Kernel Log: What's new in 2.6.29 - Part 8: Faster start-up and other behind the scenes changes](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-8-Faster-start-up-and-other-behind-the-scenes-changes-740591.html "Kernel Log: What's new in 2.6.29 - Part 8: Faster start-up and other behind the scenes changes â 18 March 2009, 08:33")
- [Kernel Log: What's new in 2.6.29 - Part 7: Audio, FireWire, USB, Video and more](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-7-Audio-FireWire-USB-Video-and-more-740561.html "Kernel Log: What's new in 2.6.29 - Part 7: Audio, FireWire, USB, Video and more â 16 March 2009, 13:07")
- [Kernel Log: What's new in 2.6.29 - Part 6: Storage, IDE/PATA, SCSI](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-6-Storage-IDE-PATA-SCSI-740501.html "Kernel Log: What's new in 2.6.29 - Part 6: Storage, IDE/PATA, SCSI â 13 March 2009, 13:45")
- [Kernel Log: What's new in 2.6.29 - Part 5: Filesystems Btrfs, SquashFS, Ext4 without journaling](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-5-Filesystems-Btrfs-SquashFS-Ext4-without-journaling-740499.html "Kernel Log: What's new in 2.6.29 - Part 5: Filesystems Btrfs, SquashFS, Ext4 without journaling â 12 March 2009, 15:13")
- [Kernel Log: Morton questions acceptance of Xen Dom0 code; file systems for SSDs](../site/news/item/Kernel-Log-Morton-questions-acceptance-of-Xen-Dom0-code-file-systems-for-SSDs-740375.html "Kernel Log: Morton questions acceptance of Xen Dom0 code; file systems for SSDs â 06 March 2009, 08:57")
- [Kernel Log: Stable series development is speeding up, X Server 1.6 available soon](../site/news/item/Kernel-Log-Stable-series-development-is-speeding-up-X-Server-1-6-available-soon-740203.html "Kernel Log: Stable series development is speeding up, X Server 1.6 available soon â 23 February 2009, 10:46")
- [Kernel Log: What's new in 2.6.29 - Part 4: ACPI, PCI, PM â€“ notebooks and power saving improvements](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-4-ACPI-PCI-PM-notebooks-and-power-saving-improvements-739889.html "Kernel Log: What's new in 2.6.29 - Part 4: ACPI, PCI, PM – notebooks and power saving improvements â 31 January 2009, 15:01")

*Older Kernel logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/).*

([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
