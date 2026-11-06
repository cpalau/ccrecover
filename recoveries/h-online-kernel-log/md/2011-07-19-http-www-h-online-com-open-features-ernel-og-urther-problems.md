---
title: ""
date: 2011-07-19
author:
source: http://www.h-online.com/open/features/Kernel-Log-Further-problems-with-UEFI-1281549.html
pages: 1
---

# 

![Kernel Log](../site/open/imgs/45/6/8/9/6/2/2/kl19julsimplefutura-b8f9cb8de1d57fbc.png)

1.  [Further problems with UEFI](../site/open/features/Kernel-Log-Further-problems-with-UEFI-1281549.html)
2.  [In brief](../site/open/features/Kernel-Log-Further-problems-with-UEFI-1281549.html?page=2)

### In brief

*Kernel*

- A certain Linus Torvalds has [appeared](https://plus.google.com/102150693225130002912/) on the recently launched Google Plus service. While there are many indications that the account is authentic, there is, of course, no certain way of telling whether it really is Torvalds…
- Christoph Hellwig has [released](http://thread.gmane.org/gmane.linux.kernel/1167010) the "XFS Status Update" for June 2011.
- In a blog posting, Suse developer Michal Marek describes [various improvements](http://lizards.opensuse.org/2011/07/14/improved-kernel-package-retention-in-12-1/) to libzypp; from OpenSuse 12.1, these changes will reportedly allow developers to determine which of the old kernels will be removed after a kernel update.

*Graphics hardware support*

- NVIDIA has released version 275.19 of its proprietary Linux graphics drivers ([x86-32](http://www.nvidia.com/object/linux-display-ia32-275.19-driver.html), [x86-64](http://www.nvidia.com/object/linux-display-amd64-275.19-driver.html)); the new version fixes various bugs and supports the GeForce GT 540M. NVIDIA has also [released](http://www.nvnews.net/vbulletin/showthread.php?t=164017) the 280.04 beta drivers that offer "preliminary" support for X Server 1.11, which is still in development.
- Jeremy Huddleston has released [X Server 1.10.3](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/1440) to fix various bugs.

*Kernel environment ("plumbing layer"), userland drivers, developer tools, etc*

- Hand de Goede has [released](http://hansdegoede.livejournal.com/11006.html) the first "official" version of usbredir, which allows individual USB devices to be passed through to other systems – such as virtual machines. With this version 0.3, the current USB Redirection Protocol API has been frozen, but extensions will still be possible.
- Lennart Poettering has submitted for discussion various [patches](http://thread.gmane.org/gmane.comp.freedesktop.xorg/46554) that extend the X Server's multi-seat support; these improvements are based on [functions](http://www.freedesktop.org/wiki/Software/systemd/multiseat) included in systemd from version 30 to support systems with multiple active users.
- In [part 9](http://0pointer.de/blog/projects/on-etc-sysinit.html) of his "Systemd for Administrators" blog series, Poettering describes problems that exist when configuring systems via files in the /etc/sysconfig (Red Hat, SUSE, ...) and /etc/default (Debian) directories; in this context, the developer discusses some solutions he considers superior. [Part 2](http://0pointer.de/blog/projects/socket-activation2.html) of the "Systemd for Developers" series explains the socket activation concept in more detail, using Cups as an example.
- On his blog, David Zeuthen has released a five-part article series titled "Writing a C library" ([1](http://davidz25.blogspot.com/2011/06/writing-c-library-part-1.html), [2](http://davidz25.blogspot.com/2011/06/writing-c-library-part-2.html), [3](http://davidz25.blogspot.com/2011/06/writing-c-library-part-3.html), [4](http://davidz25.blogspot.com/2011/07/writing-c-library-part-4.html), [5](http://davidz25.blogspot.com/2011/07/writing-c-library-part-5.html)).
- The libvirt developers have [released](http://libvirt.org/news.html) version 0.9.3 of their library for accessing different virtualisation solutions.
- With the recently [released version 1.5.0](http://lists.gnupg.org/pipermail/gcrypt-devel/2011-June/001815.html), the [libgcrypt](http://www.gnu.org/s/libgcrypt/), which is accessed by such programs as GnuPG, has learnt to use the [AES NI instructions](http://software.intel.com/en-us/articles/intel-advanced-encryption-standard-aes-instructions-set/) of recent Intel processors.
- Stephen Hemminger has [released](http://thread.gmane.org/gmane.linux.network/200120) version 2.6.39 of the iproute2 collection of network tools.
- [Version 4.6.1](http://gcc.gnu.org/gcc-4.6/changes.html) of the GCC has been released.
- The KVM blog [describes](http://www.linux-kvm.com/content/qed-qemu-enhanced-disk-format) various characteristics of the QED (Qemu Enhanced Disk Format) file system, which is still in development.

*LKML discussions*

- Nao Nishijima [has submitted](http://thread.gmane.org/gmane.linux.scsi/68632) revised versions of his patches that allow storage media to be given aliases that won't change after a reboot or hardware modification. The approach continues to be controversial; LWN.net had described the problems with an earlier patch series [in an article](https://lwn.net/Articles/448505/).
- Nancy Yuen has submitted various BadRAM implementations used by Google [to the LKML](http://thread.gmane.org/gmane.linux.kernel/1161133). Several developers had expressed their interest in these patches after Google developers had criticised that Stefan Assmann's BadRAM patches, mentioned in the [previous Kernel Log](../site/open/features/Kernel-Log-BIOS-bugs-behind-greater-power-use-1269032.html "Kernel Log: BIOS bugs behind greater power use – 28 June 2011"), are not flexible enough for Google's purposes.

*New editions of Kernel Logs are also mentioned on [Identi.ca](http://identi.ca/kernellog2) and [Twitter](http://twitter.com/kernellog2) by @kernellog2. The Kernel Log author also posts updates about various topics on [Identi.ca](http://identi.ca/kernellogauthor) and [Twitter](http://twitter.com/kernellogauthor) as @kernellogauthor.*

[**Add your comment**](../site/open/news/forum/forum-118484/write/ "Kernel Log: Further problems with UEFI")
