---
title: "Kernel Log : Winding down the IDE subsystem, LinuxTag Kernel presentations"
date: 2009-06-23
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-Winding-down-the-IDE-subsystem-LinuxTag-Kernel-presentations-742159.html
pages: 1
---

# Kernel Log : Winding down the IDE subsystem, LinuxTag Kernel presentations

**Dj Walker-Morgan**

![Kernel Log Penguin](../site/imgs/43/3/6/8/5/9/0/93e8ea3d0acdf147.jpg)

#### by Thorsten Leemhuis

**David Miller has stepped in to maintain the IDE subsystem, but plans to make it maintenance only, with no major development work. On Friday, one LinuxTag venue will be dedicated entirely to the Linux kernel. An Intel developer has expressed wide-ranging criticism of various graphics benchmarks for Linux/X.org.**

### IDE subsystem frozen

David Miller, maintainer of the Linux kernel's SPARC and network support, is taking over responsibility for the IDE subsystem, largely comprising drivers for parallel ATA adapters (PATA/IDE). He has taken over the post at short notice from Bartlomiej Zolnierkiewicz. The change was prompted by [a discussion](http://thread.gmane.org/gmane.linux.ports.sparc/11845) on a bug report from a SPARC user who described a problem with one of the IDE drivers in recent kernel versions. In the course of the discussion, Miller noted that Zolnierkiewicz had introduced numerous changes, which had not been adequately tested, into the IDE subsystem.

For his part, [Zolnierkiewicz responded](http://thread.gmane.org/gmane.linux.ports.sparc/11845/focus%3D11864), ("*I'm really tired of this kind of hostility towards IDE changes,*") and suggested that Miller should take over the IDE subsystem. The latter [did not need to be asked twice](http://thread.gmane.org/gmane.linux.ports.sparc/11845/focus%3D11866) and set up a new Git development tree without further ado. He and other developers thanked Zolnierkiewicz for his many years of hard work. Zolnierkiewicz has offered the new maintainer [his "full support"](http://thread.gmane.org/gmane.linux.ports.sparc/11845/focus%3D11867).

Miller intimated that he was not planning on implementing any major changes to the IDE subsystem, "*I'm going to treat IDE as pure legacy.*" The future thus now looks definitively to belong to the PATA drives in the Libata subsystem, which were merged into Linux 2.6.19 in late 2006. Right from the off, some developers viewed these drivers as a replacement for the drivers in the older IDE subsystem, which has been a source of repeated strife between kernel developers for more than a decade. Zolnierkiewicz had introduced major revisions into the IDE subsystem in recent months and years and merged new drivers, with the result that, instead of the anticipated replacement of one system by the other, the two subsystems had become ongoing competitors.

Linus Torvalds has now asked Miller and Zolnierkiewicz to spend some time and effort on searching for a different solution [saying](http://thread.gmane.org/gmane.linux.ide/41509/focus%3D41527) "*I think you and Bartlomiej should spend a \_lot\_ more time and effort trying to resolve this*". In response, both developers said they were happy with the handover.

### LinuxTag

One of the biggest Linux conferences in Europe, [LinuxTag](http://www.linuxtag.org/2009/en.html) is taking place in Berlin from the 24th to the 27th of June. This Friday, a number of Linux kernel related talks will be bundled together at the [Kernel Track](http://www.linuxtag.org/2009/de/program/freies-vortragsprogramm/freitag.html#c440), which will take place in roomÂ 4 (â€™Europa Iâ€™) at LinuxTag. The event will begin at 10Â am with a talk entitled "[Creating drivers using Userspace I/O (UIO)](http://www.linuxtag.org/2009/de/program/freies-vortragsprogramm/mittwoch/vortragsdetails.html?talkid=561)" from Linuxtronix developer Hans-JÃ¼rgen Koch, in which he will elucidate the structure and programming of largely userspace-located UIO drivers.

He will be followed at 11 by the author of Kernel Log, standing in for LWN.net boss Jonathan Corbet, with an overview of the latest Linux kernel development. The talk will include detailed discussion of the changes in Linux 2.6.31 which kernel hackers are currently merging into the main development tree as part of the merge window. It is two weeks on Wednesday since the [release of 2.6.30](../site/open/features/Fine-tuning-What-s-new-in-Linux-2-6-30-746581.html "Fine tuning – What's new in Linux 2.6.30 â 10 June 2009, 09:34") and Linus Torvalds is likely to bring the initial all-action merge phase of the development cycle to a close shortly by releasing 2.6.31 rc1.

"[Demystifying Kernel development](http://www.linuxtag.org/2009/de/program/freies-vortragsprogramm/mittwoch/vortragsdetails.html?talkid=565)" from Wolfram Sang (Pengutronix) and Glibc administrator Ulrich Drepper's keynote ("[Of programmers and hardware: transcending the gap](http://www.linuxtag.org/2009/de/program/freies-vortragsprogramm/mittwoch/vortragsdetails.html?talkid=3)") in the 'London' room will be followed by Jan Blunck (Novell) at 3pm with "[State of the Union and when you don't want to use Union Mounts](http://www.linuxtag.org/2009/de/program/freies-vortragsprogramm/mittwoch/vortragsdetails.html?talkid=567)". Visitors to the conference wishing to familiarise themselves with the various 'union mounts' technologies beforehand should consult the [first](http://lwn.net/Articles/325369/) and [second](http://lwn.net/Articles/327738/) articles in LWN.net's "Unioning file systems: Implementations" series.

Ksplice developer Waseem Daher will give an overview of the [Ksplice](http://www.ksplice.com/) framework, which was released last year, in his talk "[Rebootless kernel updates](http://www.linuxtag.org/2009/de/program/freies-vortragsprogramm/mittwoch/vortragsdetails.html?talkid=569)". The day will close with [Kernel Kwestioning](http://www.linuxtag.org/2009/de/program/freies-vortragsprogramm/mittwoch/vortragsdetails.html?talkid=571), in which various kernel developers will take questions from the audience.

### All about graphics

- [On his blog](http://cworth.org/intel/performance_measurement/) Intel and X.org developer Carl Worth gives background information on speed measurements for graphics output. He reiterates (as have many others before him) why glxgears is completely unsuitable for measuring speed. He also notes that the results of micro-benchmarks such as x11perf and gtkperf, frequently used by some hardware websites, are also of little practical relevance. Worth presents an alternative in the form of cairo-perf-trace, which, he claims, is much more suitable for such measurements and which has already given good service during development of the Intel driver.

<!-- -->

- Peter Hutterer, an X.org developer employed by Red Hat, presents an overview of Xinput 2.0 (XI2) in his blog entries "XI2 Recipes, Parts [1](http://who-t.blogspot.com/2009/05/xi2-recipes-part-1.html), [2](http://who-t.blogspot.com/2009/06/xi2-recipies-part-2.html) and [3](http://who-t.blogspot.com/2009/06/xi2-recipes-part-3.html)". This has just been merged into the development tree for X.org's X server and should find its way into X server 1.7, which should in turn be a component of X.org 7.5. One of the main reasons for adopting XI2 is better support for Multi-PointerÂ X (MPX) â€“ parallel operation with multiple entry devices, such as a touchpad and mouse.

<!-- -->

- The X development team have [again revised](http://thread.gmane.org/gmane.comp.freedesktop.xorg/31957/focus%3D883) their plans for releasing version 7.5 and are now aiming for an August release. A [recent discussion](http://thread.gmane.org/gmane.comp.freedesktop.xorg/39297/focus%3D39298) sheds some light on the working practices of the X development team, and makes clear why occasional delays are to be expected.

<!-- -->

- Earlier this month, AMD developer Alex Deucher discussed the power saving technologies used by the latest Radeon graphics chips on [his blog](http://www.botchco.com/agd5f/?p=45). He explained which of these technologies the Linux graphics drivers were already supporting and which they would soon be supporting.

<!-- -->

- [On his blog](http://blog.fishsoup.net/2009/06/02/timing-frame-display/) GTK developer Owen Taylor discusses all the things that need to be considered when updating the display.

<!-- -->

- AMD last week released [version 9.6](http://www2.ati.com/drivers/linux/catalyst_96_linux.pdf)![PDF](../site/icons/file-pdf.gif "PDF document") of its proprietary Catalyst/Fglrx Linux graphics driver. It can be [downloaded here](http://support.amd.com/).

### Kernel status

- The stable series is now on versions [2.6.27.25](http://thread.gmane.org/gmane.linux.kernel/850257) and [2.6.29.5](http://thread.gmane.org/gmane.linux.kernel/852239), which incorporate around 60 and 85 minor changes and bug fixes respectively. As (almost) ever, the development team are advising users to switch to the new version without explicitly stating whether security vulnerabilities have been plugged.

<!-- -->

- Willy Tarreau, maintainer of the 2.4 kernel series, continues to take his job seriously and released Linux version [2.4.37.2](http://thread.gmane.org/gmane.linux.kernel/847606) just over two weeks ago.

### Kernel Log: In brief

- In his [XFS status update for May 2009](http://thread.gmane.org/gmane.comp.file-systems.xfs.general/29424), Christoph Hellwig gives an overview of the latest developments concerning the XFS file system.

<!-- -->

- Long-term Linux WLAN developer Luis R. Rodriguez, now employed by Atheros, has announced [the release](http://thread.gmane.org/gmane.linux.kernel.wireless.general/34151) of source code for the firmware for some Atheros USB WLAN chips with support for 802.11n.

<!-- -->

- PulseAudio developer Lennart Poettering has [announced](http://lalists.stanford.edu/lad/2009/06/0191.html) RealtimeKit, a small program which will run in the background in future versions of PulseAudio and assign real-time priorities to individual applications. In contrast to existing solutions for managing real-time priorities for individual applications, malicious users will not be able to freeze the system where the program, rtkit for short, is used.

<!-- -->

- The development team behind [HPLIP](http://hplipopensource.com/) have released [version 3.9.6](http://hplipopensource.com/hplip-web/release_notes.html) of the HPLIP driver for HP printers and multifunction printers. It includes support for a whole range of HP devices from various series. The 'HPCUPS' CUPS driver is now the main driver, but HPIJS is retained. HP is now supplying the program hp-wificonfig for printers with WLAN functionality.

<!-- -->

- The 'LKML Summary Podcast' launched by Jon Masters can now be found on the website [kernelpodcast.org](http://www.kernelpodcast.org/). For users who prefer reading to listening, the podcast scripts are also available from the website.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the Kernel Log at The H Open Source:*

- [Fine Tuning - What's new in Linux 2.6.30](../site/open/features/Fine-tuning-What-s-new-in-Linux-2-6-30-746581.html "Fine tuning – What's new in Linux 2.6.30 â 10 June 2009, 09:34")
- [Kernel Log: What's coming in 2.6.30 - Architecture and infrastructure](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-Architecture-and-infrastructure-741921.html "Kernel Log: What's coming in 2.6.30 - Architecture and infrastructure â 06 June 2009, 07:47")
- [Kernel Log: What's coming in 2.6.30 â€“ Drivers: New drivers for audio, video, USB hardware, netbooks and notebooks](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-Drivers-New-drivers-for-audio-video-USB-hardware-netbooks-and-notebooks-741837.html "Kernel Log: What's coming in 2.6.30 – Drivers: New drivers for audio, video, USB hardware, netbooks and notebooks â 01 June 2009, 18:52")
- [Kernel Log: ALSA driver for the X-Fi, debate over TuxOnIce](../site/news/item/Kernel-Log-ALSA-driver-for-the-X-Fi-debate-over-TuxOnIce-741673.html "Kernel Log: ALSA driver for the X-Fi, debate over TuxOnIce â 21 May 2009, 09:24")
- [Kernel Log: What's coming in 2.6.30 - Storage: RAID improvements, optimised CFQ Scheduler, SAS drivers](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-Storage-RAID-improvements-optimised-CFQ-Scheduler-SAS-drivers-741597.html "Kernel Log: What's coming in 2.6.30 - Storage: RAID improvements, optimised CFQ Scheduler, SAS drivers â 15 May 2009, 17:01")
- [Kernel Log: X.org 7.5 coming in summer, re-write for Intel's graphics driver](../site/news/item/Kernel-Log-X-org-7-5-coming-in-summer-re-write-for-Intel-s-graphics-driver-741405.html "Kernel Log: X.org 7.5 coming in summer, re-write for Intel's graphics driver â 04 May 2009, 07:09")
- [Kernel Log: What's coming in 2.6.30 - File systems: New and revamped file systems](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-File-systems-New-and-revamped-file-systems-741319.html "Kernel Log: What's coming in 2.6.30 - File systems: New and revamped file systems â 27 April 2009, 16:11")
- [Kernel Log: 3D support for the new Radeon driver; new Intel drivers](../site/news/item/Kernel-Log-3D-support-for-the-new-Radeon-driver-new-Intel-drivers-741271.html " Kernel Log: 3D support for the new Radeon driver; new Intel drivers â 22 April 2009, 17:06")

*Older Kernel Logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/).*

([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
