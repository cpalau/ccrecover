---
title: "Kernel Log: Linux-next to speed development work"
date: 2008-02-14
author: "Jonathan Bennett"
source: http://www.h-online.com/open/news/item/Kernel-Log-Linux-next-to-speed-development-work-734227.html
pages: 1
---

# Kernel Log: Linux-next to speed development work

**Jonathan Bennett**

![Kernel Log](../site/imgs/43/3/6/1/0/0/2/a345f5e7c547062f.jpg) The developers working on the Linux kernel are to co-ordinate their efforts at an earlier stage in development, with the aim of streamlining the integration process. In collaboration with Andrew Morton, Stephen Rothwell has [set up the Linux-next kernel line](http://thread.gmane.org/gmane.linux.kernel/638189) aimed solely at Linux developers. Previously, maintainers of Linux subsystems such as IA64, PPC, PCI, USB, SCSI, ATA, IDE and Kbuild have generally prepared their improvements independently of one another in subsystem-specific development branches administered with git or quilt, from where they were then transferred to the [mm development kernel](http://kernel.org/patchtypes/mm.html) maintained by Andrew Morton. During the 'merge window', in the first two weeks of the Linux development cycle, Linus Torvalds then integrates major developments into the [Linux source code control system](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=summary). In doing so he in some cases accesses, not the subsystem-specific development branch, but development branches derived from these to which the subsystem maintainers add only those patches which they consider sufficiently mature for the official kernel.

At the end of the roughly two month test phase, the next version of the kernel then emerges from the Linux source code control system administered by Torvalds. The development branch administered by Torvalds thus represents the tip of the Linux development tree. The cycle then begins again. During these two months, Morton releases new mm kernels derived from the main trunk with the various subsystem-specific development branches. He also integrates some other experimental developments. The mm kernel thus contains lots of code which is still months or years from being mature enough for the official kernel. The Reiser4 file system, for example, has been in the mm kernels for more than two years. The inclusion of experimental additions may throw up minor or major problems in these kernels, which are thus not intended for end users.

The Linux-next branch is intended to close the gap between the kernel branches administered by Linus Torvalds and Andrew Morton by only including patches which are very likely to be mature enough for inclusion in the next-but-one kernel version. In the current situation, Stephen Rothwell would thus collect developments for version 2.6.26 in Linux-next, while Torvalds continued to work in parallel on 2.6.25 and Morton collected experimental developments not intended for release before 2.6.27 or later in the Linux-next-based mm kernel. This layered system makes Morton's work easier and should help subsystem maintains to better coordinate their work, as the subsystems are not always clearly separated and in some cases interfere. Linux-next should thus also ensure that at the start of the development cycle Torvalds is presented with mature patches which work properly together and which can be integrated into the main Linux development trunk without to much difficulty.

A similar idea was recently [mooted by SCSI subsystem maintainer James Bottomley](http://thread.gmane.org/gmane.linux.kernel/626055) in the form of the 'merge tree'. [It looks](http://thread.gmane.org/gmane.linux.kernel/638189/focus%3D638203), however, as if this work will be taken forward by Rothwell via Linux-next. The [discussion regarding Linux-next](http://thread.gmane.org/gmane.linux.kernel/638189) has quickly overflowed into a general discussion on how the subsystem maintainers can better coordinate their work and how they should use git without creating too many complications for other subsystem developers.

### Kernel Log in brief

Following the example of Intel, which recently published documentation on the graphics cores in its latest chipsets, AMD has now placed documentation for some GPUs, first distributed to developers just a few months ago, [on its website](http://ati.amd.com/developer/open_gpu_documentation.html). The company has also set up an e-mail address for queries regarding this documentation.

The debate over the adoption of KGDB, which has been discussed in previous issues of Kernel Log, has [been turned up a notch](http://thread.gmane.org/gmane.linux.kernel/637662) with participation from Torvalds, with no end in site.

The [debate on the blocking of proprietary USB drivers](http://thread.gmane.org/gmane.linux.usb.general/835/) planned for 2.6.25 has abated for now – there have been no great surprises, so that it still looks as if the patch will be retained in the official Linux kernel.

([jbe](mailto: "Jonathan Bennett"))
