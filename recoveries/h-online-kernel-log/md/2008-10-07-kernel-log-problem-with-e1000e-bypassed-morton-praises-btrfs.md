---
title: "Kernel Log: problem with e1000e bypassed, Morton praises Btrfs"
date: 2008-10-07
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-problem-with-e1000e-bypassed-Morton-praises-Btrfs-737561.html
pages: 1
---

# Kernel Log: problem with e1000e bypassed, Morton praises Btrfs

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/4/3/3/2/93e8ea3d0acdf147.jpg) Numerous changes, mainly developed by Intel developers, to protect the non-volatile memory, NVM, of Intel networking chips from accidental overwriting have been incorporated by kernel developers, have incorporated into the main development branch of Linux. The patches are designed to bypass a problem with the previous pre-release versions of 2.6.27 which has been [extensively discussed in the past two weeks](../site/news/item/Intel-e1000e-user-Don-t-install-the-new-SUSE-betas-737395.html "Intel e1000e user? Don't install the new SUSE betas – 23 September 2008, 09:14") and put some Intel networking chips out of action on boards which use the Intel's ICH8, ICH9 or ICH10 southbridges networking functionality.

The protection is mainly provided by a [driver patch](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4a7703582836f55a1cbad0e2c1c6ebbee3f9b3a7) integrated a few days ago which makes the driver enable write protection for the NVM almost immediately after being loaded. Numerous changes integrated during the following day ([1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=37f40239f49fbc0b489d0327a700fee5b3898ac2), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=a8f88ff5a5abc2ce9f7d7d2694178b2c617d713a), [3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=23033fad5be0a2c7838cb9e1579919b64af713f6), [4](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=4fa7553a075918e1e02a6039f9e826c8872b7049), [5](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=717d438d1fde94decef874b9808379d1f4523453), [6](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=95b866d5afcafee00fc9ad70665e48c86d8c4e0f)) further improve protection, correct minor flaws and facilitate troubleshooting. The developers don't yet appear to have found the actual cause for the involuntary overwriting of the non-volatile memory; the problem is not believed to be located in the e1000e driver. Several distributors already offer kernels which contain the protection feature – among them the recently released [second beta](../site/news/item/OpenSuse-11-1-second-beta-737555.html "OpenSuse 11.1 second beta – 06 October 2008, 14:32") of OpenSuse 11.1 and the kernel in the development branch of Fedora (Rawhide).

------------------------------------------------------------------------

Following the call for [Btrfs](http://btrfs.wiki.kernel.org/) to be integrated into the main development branch of Linux, as discussed in the [previous kernel log](../site/news/item/Kernel-Log-2-6-27-nearing-completion-Btrfs-to-be-added-to-the-kernel-737489.html "Kernel Log: 2.6.27 nearing completion; Btrfs to be added to the kernel? – 01 October 2008, 09:23"), [Andrew Morton](http://en.wikipedia.org/wiki/Andrew_Morton_%28computer_programmer%29) has now [issued a statement](http://thread.gmane.org/gmane.linux.file-systems/26246/focus%3D26317) in which he advocates the file system's speedy inclusion into linux-next and its subsequent integration into the main development branch for kernel version 2.6.29. At the end of his email, Morton emphasised that "Linux has needed a new local filesystem for some time, and btrfs might be The One, and hence is worth a bit of special-case treatment.".

Meanwhile, Daniel Phillips is continuing his work on the [Tux3](http://tux3.org/) file system announced at the [end of July](../site/news/item/Kernel-Log-Tux3-file-system-announced-X-org-updates-736707.html "Kernel Log : Tux3 file system announced, X.org updates – 01 August 2008, 09:17"). In the context of this project, he has sent [several emails](http://search.gmane.org/?query=tux3&author=Daniel+Phillips&group=gmane.linux.kernel&sort=date&DEFAULTOP=and&xP=Ztux3&xFILTERS=Glinux.kernel---A) detailing the operation and development progress of Tux3 to the Linux Kernel Mailing List (LKML) in the past few weeks – he has not received any replies on the LKML, to date.

------------------------------------------------------------------------

The developers of Netfilter recently met in Paris for their annual Netfilter Workshop; David S. Miller summarises the event in his [blog](http://vger.kernel.org/~davem/cgi-bin/blog.cgi/2008/10/05#nfws2008), also mentioning the packet filtering framework newly developed by Patrick McHardy. Links to some of the presentations can be found [on the Netfilter Workshop site](http://nfws.inl.fr/en/); they include a [presentation by David S. Miller](http://nfws.inl.fr/nfws_userday/David-Miller_Linux-Multiqueue-Networking.pdf) (PDF file) which discusses the [new "Linux TX Multiqueue Implementation"](../site/news/item/Kernel-Log-Centrino-2-WiFi-driver-iwl-5000-and-webcam-driver-gscpa-in-Linux-2-6-27-736569.html "Kernel Log: Centrino 2 WiFi driver iwl 5000 and webcam driver gscpa in Linux 2.6.27 – 23 July 2008, 16:46") first introduced with 2.6.27.

**In Brief**

- Intel has [released the ACPI Integrated Graphics Device OpRegion Specification](http://thread.gmane.org/gmane.comp.freedesktop.xorg/32614) under a Creative Commons Attribution License. The information will help developers evaluate ambient light sensors and hot keys for switching the display output correctly in graphics drivers.

<!-- -->

- In his blog, Jesse Barnes has published [an overview of the latest developments](http://virtuousgeek.org/blog/index.php/jbarnes/2008/10/03/title_1) around the PCI subsystem of Linux, of X.org's Intel graphics driver 2.5 and of GEM (Graphics Execution Manager). According to the blog, the latter will be integrated into Linux with version 2.6.28.

<!-- -->

- Red Hat employee and developer Nick Clifton intends to give a monthly summary of the most important developments around GCC, Binutils, Newlib and GDB [in his blog](http://nickclifton.livejournal.com/) from now on. The [September issue](http://nickclifton.livejournal.com/999.html) has been out since September 14th.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: 2.6.27 nearing completion; Btrfs to be added to the kernel?](../site/news/item/Kernel-Log-2-6-27-nearing-completion-Btrfs-to-be-added-to-the-kernel-737489.html "Kernel Log: 2.6.27 nearing completion; Btrfs to be added to the kernel? – 01 October 2008, 09:23")
- [Kernel Log: Kernel Summit info; Plumbers keynote online; the latest on the e1000e problem](../site/news/item/Kernel-Log-Kernel-Summit-info-Plumbers-keynote-online-the-latest-on-the-e1000e-problem-737443.html "Kernel Log: Kernel Summit info; Plumbers keynote online; the latest on the e1000e problem – 26 September 2008, 10:59")
- [Kernel Log: The second day of Kernel Summit 2008; criticism of Ubuntu at the opening of the Linux Plumbers Conference](../site/news/item/Kernel-Log-The-second-day-of-Kernel-Summit-2008-criticism-of-Ubuntu-at-the-opening-of-the-Linux-Plumbers-Conference-737379.html "Kernel Log: The second day of Kernel Summit 2008; criticism of Ubuntu at the opening of the Linux Plumbers Conference – 19 September 2008, 15:58")
- [Kernel Log: Hard core Linux developers discuss the future of Linux at the Kernel Summit](../site/news/item/Kernel-Log-Hard-core-Linux-developers-discuss-the-future-of-Linux-at-the-Kernel-Summit-737327.html "Kernel-Log: Hard core Linux developers discuss the future of Linux at the Kernel Summit – 17 September 2008, 11:48")
- [Kernel Log: New stable and developer kernel, Mesa 7.1 and X-Server 1.5 released](../site/news/item/Kernel-Log-New-stable-and-developer-kernel-Mesa-7-1-and-X-Server-1-5-released-737227.html "Kernel-Log: New stable and developer kernel, Mesa 7.1 and X-Server 1.5 released. – 09 September 2008, 15:02")
- [Kernel Log: New stable and pre-release kernels, Ubuntu 8.10 with 2.6.27?](../site/news/item/Kernel-Log-New-stable-and-pre-release-kernels-Ubuntu-8-10-with-2-6-27-737021.html "Kernel Log: New stable and pre-release kernels, Ubuntu 8.10 with 2.6.27? – 25 August 2008, 11:32")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
