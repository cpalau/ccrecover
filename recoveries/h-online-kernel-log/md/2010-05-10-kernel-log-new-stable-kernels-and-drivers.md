---
title: "Kernel Log: New stable kernels and drivers"
date: 2010-05-10
author: "Thorsten Leemhuis"
source: http://www.h-online.com/open/features/Kernel-Log-New-stable-kernels-and-drivers-995820.html
pages: 1
---

# Kernel Log: New stable kernels and drivers

**Thorsten Leemhuis**

**While new stable kernel releases seem to have become somewhat less frequent, they now include more changes. Although the most recent version of AMD's proprietary graphics drivers finally work with X Server 1.7, NVIDIA's drivers already work with version 1.8. Videos of the Linux Audio Conference and the Collaboration Summit provide insights into audio and kernel topics.**

At the end of April, the maintainers of the Linux kernel's Stable Series released [2.6.32.12](http://thread.gmane.org/gmane.linux.kernel/978119) and [2.6.33.3](http://thread.gmane.org/gmane.linux.kernel/978120). Both versions were released three-and-a-half weeks after their respective predecessors, one containing almost [200](http://thread.gmane.org/gmane.linux.kernel/976743) and the other more than [130](http://thread.gmane.org/gmane.linux.kernel/976956) patches – it seems that the intervals between new stable kernel releases are becoming slightly longer, and that the number of changes integrated into the new versions is getting somewhat larger.

A review for the next Stable Kernels hasn't been started on LKML yet, but Greg Kroah-Hartman has already integrated a few patches for the next versions to [his Git-Tree](http://git.kernel.org/?p=linux/kernel/git/stable/stable-queue.git;a=summary). Among those for the next variants for the 32 and 33 series is the one-line change that fixes the recently discovered [performance problem on AMD processors with Turbo Core](../site/news/item/Performance-problem-in-AMD-s-Phenom-II-X6-under-Linux-993127.html "Performance problem in AMD's Phenom II X6 under Linux – 04 May 2010").

Meanwhile the release of 2.6.34 is getting closer, as Torvalds indicated in the [release announcement](http://thread.gmane.org/gmane.linux.kernel/982971) for the seventh pre-release. Having dubbed Linux 2.6.30 the "[Man-Eating Seals of Antiquity](http://torvalds-family.blogspot.com/2009/05/yet-more-reading.html)", Torvalds issued a new kernel name with [RC5 of 2.6.34](http://git.kernel.org/linus/01bf0b64579ead8a82e7cfc32ae44bc667e7ad0f): "Sheep on Meth".

### Graphics drivers

At the end of April, AMD [released](http://support.amd.com/us/Pages/drivers.aspx) version 10.4 of its proprietary graphics drivers, known as fglrx or Catalyst, for modern Radeon graphics cards. The main advancement listed in the new version's [release notes](http://www2.ati.com/drivers/linux/catalyst_104_linux.pdf)![PDF](../site/icons/file-pdf.gif "PDF document") is the "Early Look" support for the recently [released Ubuntu 10.04](../site/open/features/What-s-new-in-Ubuntu-10-04-LTS-982993.html "What's new in Ubuntu 10.04 LTS – 29 April 2010"). This change allows the driver to work with series 1.7 X Servers, which became available [last October](../site/news/item/X-org-Server-1-7-0-released-812407.html "X.org Server 1.7.0 released – 02 October 2009") and are part of X.org. As a result, the driver is now also functional in many other distributions that use such an X Server. However, it still doesn't support [X Server 1.8](../site/news/item/X-Server-1-8-with-new-configuration-mechanisms-970683.html "X Server 1.8 with new configuration mechanisms – 06 April 2010"), which was released a month ago – time will tell whether AMD will need another six months to provide this support.

NVIDIA tends to respond much faster. A version of the proprietary GeForce driver, functional with X Server 1.8 after setting a special Xorg.conf option, was already available when the new X Server was released. Version 195.36.24 ([x86-32](http://www.nvidia.com/object/linux-display-ia32-195.36.24.html), [x86-64](http://www.nvidia.com/object/linux-display-amd64-195.36.24.html)), which was released at the end of April, no longer requires this trick and also supports the GeForce GTX 470 and 480 models introduced in March.

### In brief

*Kernel*

- [Part 2](../site/open/features/Kernel-Log-Coming-in-2-6-34-Part-2-File-Systems-985128.html "Kernel Log: Coming in 2.6.34 (Part 2) - File Systems – 23 April 2010") of the Kernel Log's "Coming in 2.6.34" mini series discussed various background details of the Ceph Distributed File system. IBM Developerworks have now also released [an article](http://www.ibm.com/developerworks/linux/library/l-ceph/index.html?ca=dgr-lnxw07CEPHdth-LX) about this new file system that is being added to Linux 2.6.34.
- The recently released [overview](http://thread.gmane.org/gmane.linux.acpi.devel/45838) of unresolved regressions in release candidates of Linux 2.6.34 lists 22 problems that didn't exist in Linux 2.6.33.
- Google developer Arve Hjønnevåg has submitted a [revised](http://thread.gmane.org/gmane.linux.kernel/979957) version of the [patches we've already mentioned](../site/news/item/Google-to-hire-two-Android-developers-to-work-with-the-kernel-community-988166.html "Google to hire two Android developers to work with the kernel community – 27 April 2010") to the LKML, adding various functions for Android and Android drivers to the kernel.
- The series of articles entitled "Collecting and analyzing Linux kernel crashes" describes how to use [LKCD](http://www.dedoimedo.com/computers/lkcd.html), [Kdump](http://www.dedoimedo.com/computers/kdump.html) and [Crash](http://www.dedoimedo.com/computers/crash.html) to collect and analyse crash dumps when kernel problems are encountered.
- Facebook employees have recently [released](http://www.facebook.com/note.php?note_id=388112370932) Flashcache – a [kernel extension originally designed for](http://github.com/facebook/flashcache) Linux 2.6.18 and 2.6.20 which temporarily saves (caches) the data stored on a slow storage medium to a fast medium (such as an SSD) to improve data throughput. [Similar functionality](http://thread.gmane.org/gmane.linux.kernel/979977) is also provided by Bcache, which has recently been resubmitted to the [LKML for inspection](http://thread.gmane.org/gmane.linux.kernel/979976) to prepare for its integration into the main development branch.
- The [video footage](http://video.linuxfoundation.org/categories/conferences-symposiums/2010-collaboration-summit) of the Linux Foundation Collaboration Summit 2010 includes a [video by the Kernel Panel](http://video.linuxfoundation.org/video/1712) in which well-known kernel hackers James Bottomley, Jon Corbet, Christoph Hellwig, Greg Kroah-Hartman and Andrew Morton discuss various kernel topics with each other and with the audience.
- At LinuxTAG 2010, Kernel developer and LWN.Net boss Jon Corbet will present his "[kernel report](http://www.linuxtag.org/2010/de/program/freies-vortragsprogramm/mittwoch/vortragsdetails.html?talkid=7)" as one of the two Saturday keynotes; on the same day, the kernel track in the London auditorium will offer [numerous further presentations](http://www.linuxtag.org/2010/de/program/freies-vortragsprogramm/samstag.html) of kernel-related topics.
- Christoph Hellwig discusses the most recent changes to the XFS filesystem in his "[XFS status update for March 2010](http://thread.gmane.org/gmane.linux.kernel/975038)".

*Graphics*

- Peter Hutterer recently [released](http://thread.gmane.org/gmane.comp.freedesktop.xorg/43345) version 1.7.7 of X.org's X Servers to fix several bugs; he is currently also preparing the release of [X Server 1.8.1](http://thread.gmane.org/gmane.comp.freedesktop.xorg/43340).
- On his blog, AMD developer Alex Deucher has launched a series of articles describing how the kernel's Radeon DRM driver was extended to support Evergreen GPUs. His [first post](http://www.botchco.com/agd5f/?p=52) also describes the patches integrated into Linux 2.6.34 to support the GPUs used in Radeon HD 5000 graphics cards.
- Matthew Garrett's blog [explains some of the problems](http://www.advogato.org/person/mjg59/diary.html?start=244) developers may encounter due to the changes made to support the power saving features of Radeon GPUs.

*Kernel environment ("plumbing layer"), userland drivers, developer tools*

- The [program overview](http://lac.linuxaudio.org/2010/?page=program) of the [Linux Audio Conference 2010](http://lac.linuxaudio.org/2010/) held at the beginning of the month now offers slides and video recordings of some of the presentations. These include the presentation "Pro Audio is Easy, Consumer Audio is Hard" by PulseAudio developer Lennart Poettering. After attending the conference, the developer recently [explained in his blog](http://0pointer.de/blog/projects/when-pa-and-when-not.html) why, in his opinion, PulseAudio and Jack don't compete and why he thinks that having both systems isn't necessarily bad.
- In the article "[Linux on 4KB-sector disks: Practical advice"](http://www.ibm.com/developerworks/linux/library/l-4kb-sector-disks/index.html?ca=dgr-lnxw074KB-Disksdth-LX), IBM developerWorks recently discussed some aspects that have already been [mentioned several times](../site/open/features/Kernel-Log-Ceph-file-system-in-2-6-34-kernel-and-KVM-presentations-at-the-CLT2010-961429.html "Kernel Log: Ceph file system in 2.6.34, kernel and KVM presentations at the CLT2010 – 23 March 2010") in the Kernel Log that concern the interaction between Linux and hard disks with 4-Kbyte sectors.
- The Sane developers recently [released version 1.0.21 of the Sane backends](http://thread.gmane.org/gmane.comp.graphics.scanning.sane.devel/17753), then [added](http://thread.gmane.org/gmane.comp.graphics.scanning.sane.devel/17778) a correction shortly afterwards. New features include improvements for scanning via a network as well as three new drivers: kodak (Kodak i18xx), kvs1025 (Panasonic KV-S10xx) and p5 (Primax PagePartner).
- Junio C Hamano has [released Git 1.7.1](http://thread.gmane.org/gmane.linux.kernel/977720).

*For other articles on 2.6.34 and links to the rest of the "Coming in 2.6.34" series, see [The H's Kernel Log - 2.6.34 Tracking page](../site/open/features/Linux-Kernel-2-6-34-tracking-962586.html "Linux Kernel 2.6.34 tracking – 24 March 2010"). New editions of Kernel Logs are also mentioned on [Identi.ca](http://identi.ca/kernellog2) and [Twitter](http://twitter.com/kernellog2) via "@kernellog2". The Kernel Log author also posts updates about various topics on [Identi.ca](http://identi.ca/kernellogauthor) and [Twitter](http://twitter.com/kernellogauthor) via "@kernellogauthor".*

([crve](mailto:crve@h-online.com))
