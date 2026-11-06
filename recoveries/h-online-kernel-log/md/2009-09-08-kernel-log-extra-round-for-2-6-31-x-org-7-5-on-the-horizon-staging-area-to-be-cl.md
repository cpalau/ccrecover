---
title: "Kernel Log â Extra round for 2.6.31, X.org 7.5 on the horizon, staging area to be cleaned up"
date: 2009-09-08
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-Extra-round-for-2-6-31-X-org-7-5-on-the-horizon-staging-area-to-be-cleaned-up-743289.html
pages: 1
---

# Kernel Log â Extra round for 2.6.31, X.org 7.5 on the horizon, staging area to be cleaned up

**Dj Walker-Morgan**

![Kernel Log Penguin](../site/imgs/43/3/6/9/7/1/8/93e8ea3d0acdf147.jpg)

#### by Thorsten Leemhuis

**Linus Torvalds will release 2.6.31 a few days later than previously announced and has scheduled another release candidate, RC9. After some delay, the development of X.org 7.5 is now going ahead at full steam, and the developers plan to have the final version ready by the end of this month. Greg Kroah-Hartman wants to clean up the staging area â€“ this could also affect Microsoftâ€™s Hyper-V drivers. Con Kolivas has released BFS, a process scheduler specifically tailored for desktop systems.**

### Kernel status

The maintainers of the Linux Stable Series are preparing versions [2.6.27.32](http://thread.gmane.org/gmane.linux.kernel/885861) and [2.6.30.6](http://thread.gmane.org/gmane.linux.kernel/886047). The window for submitting comments already closed on Sunday night, which makes it likely that the two new versions will be released shortly. As usual, both versions correct several bugs and offer numerous, mostly minor improvements.

When releasing Linux 2.6.31 RC8, Linus Torvalds [indicated](../site/news/item/Kernel-Log-Coming-in-2-6-31-Part-5-CUSE-USB-3-0-FireWire-networking-and-the-rest-743173.html "Kernel Log: Coming in 2.6.31 - Part 5: CUSE, USB 3.0, FireWire networking and the rest â 31 August 2009, 08:02") that he intended to release 2.6.31, after his diving holiday, on US Labor Day which is on the 7th September this year. In his absence, however, quite a few subsystem maintainers submitted further corrections, which prompted him to [schedule RC9](http://thread.gmane.org/gmane.linux.kernel/886176). Torvalds said he wants to let the RC simmer for a few days before he releases the next version of the main development branch. There were still [27Â unsolved problems](http://thread.gmane.org/gmane.linux.power-management.general/15825) in the list of unknown bugs not contained in 2.6.30 last weekend. The [list](http://thread.gmane.org/gmane.linux.power-management.general/15826) of flaws introduced between 2.6.29 and 2.6.30 lists the same number of bugs.

German kernel developer Thomas Gleixner, who works for [Linutronix](http://www.linutronix.de) and is also known for his contribution to the [real-time support for Linux](http://rt.wiki.kernel.org), has [announced](http://thread.gmane.org/gmane.linux.rt.user/3911/focus%3D5004) that he intends to release 2.6.31-rt within 24Â hours after the release of Linux 2.6.31. Gleixner will deliver the [keynote address](http://www.osadl.org/RTLWS-Agenda-Community-Developers-Track.rtlws11-agenda-kernel-track.0.html) on the second day of the [Real Time Linux Workshops](http://www.osadl.org/Dresden-2009.rtlws11-dresden-2009.0.html) held in Dresden at the end of this month; his presentation will be followed by Jonathan Corbet of LWN.net, who will deliver his well-known "Kernel Report".

### Dodgy drivers to be thrown out

In an [email to the LKML](http://thread.gmane.org/gmane.linux.kernel/884983), Greg Kroah-Hartman provided a status overview for numerous drivers in the staging branch and outlined the changes scheduled for 2.6.32. Among them is the addition of rt3090, an additional driver for Realtek Wi-Fi hardware; further new drivers for Wi-Fi chip-sets by Realtek and VIA are also to be integrated into the staging branch, which became part of the [main development branch](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-3-Dodgy-drivers-737747.html "Kernel Log: What's coming in 2.6.28 - Part 3: Dodgy drivers â 22 October 2008, 09:29") with Linux 2.6.28. The staging area is a place for drivers that do not satisfy the kernel developers' quality requirements â€“ when loading such drivers the kernel is, therefore, marked as "TAINT_CRAP".

However, the maintainer of the staging branch also announced that several drivers will be thrown out because their code is no longer maintained by anyone â€“ as a result, the EPL (Ethernet Power Link) driver is scheduled to be removed from 2.6.32. In this context, Kroah-Hartman pointed out that the staging branch isn't a dumping area for unmaintained, dead code ("*First off, drivers/staging/ is NOT a dumping ground for dead code. If no one steps up to maintain and work to get the code merged into the main portion of the kernel, the drivers will be removed.*").

Many other drivers could sooner or later face the same fate. For instance, Kroah-Hartman is thinking about removing the [Hyper-V drivers](../site/news/item/Microsoft-GPLs-Linux-virtualisation-drivers-742565.html "Microsoft GPLs Linux virtualisation drivers â 20 July 2009, 17:22"), scheduled to be integrated with 2.6.32, in version 2.6.33. According to the maintainer, the Microsoft developers suddenly disappeared after making numerous changes and haven't even replied to his emails. Things also seem to be going badly for the drivers of the wlan-ng framework that used to be included in many distributions. While the hardware they support used to be quite popular with Linux users, the drivers never made it into the main development branch of Linux â€“ and as a result, are now missing from many distributions.

### Phoenix

Con Kolivas has [presented](http://ck.kolivas.org/patches/bfs/bfs-faq.txt) the BFS (Brain Fuck Scheduler), a process scheduler specifically tailored for desktop systems. Kolivas, who had already worked on such schedulers in the past, publicly resigned from kernel development when developers decided to integrate the Completely Fair Scheduler ([CFS](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob;f=Documentation/sched-design-CFS.txt;h=16feebb7bdc077f334964443235996a187a4cf90;hb=5e7eaade55d53da856f0e07dc9c188f78f780192)), instead of his Staircase CPU scheduler, into the kernel. CFS uses some of the ideas developed for the Staircase CPU scheduler.

Since the introduction of CFS, numerous developers have improved this scheduler, optimising it for various systems and areas of use. The main CFS developer, Ingo Molnar, has [taken a closer look](http://thread.gmane.org/gmane.linux.kernel/886319) at BFS and performed a few benchmarks â€“ Kolivas, however, was [very unhappy](http://thread.gmane.org/gmane.linux.kernel/886319/focus%3D886414) with Molnar's choices, the test system he used and several other aspects of his approach.

At present, the integration of BFS into the Linux main development branch seems very unlikely, as Linus Torvalds has already made it clear that he doesn't want to maintain multiple schedulers. In addition, the Linux distributors tend to prefer a single kernel image that achieves optimum performance on a wide variety of systems without requiring special configuration. It could be that the CFS developers will improve their scheduler in the areas covered by BFS â€“ a bonus for the user community.

### In Brief

- Peter Hutterer has released a snapshot of the [Synaptics 1.2 touch pad driver](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/765). It offers improvements like "Synaptics Capabilities", "Synaptics Area" and "Synaptics Gestures". However, the developer has removed the SHM (Shared Memory) configuration options â€“ better and more secure run-time configuration options have become available.

<!-- -->

- Following the [recently reported delays](../site/news/item/Kernel-Log-X-server-1-7-delayed-Compiz-runs-on-newer-Radeon-GPUs-DRBD-in-kernel-soon-742829.html "Kernel Log: X server 1.7 delayed; Compiz runs on newer Radeon GPUs; DRBD in kernel soon â 05 August 2009, 16:55") in the development of X.orgÂ 7.5 and the corresponding X ServerÂ 1.7, the developers have now picked up speed. According to their [latest schedule](http://lists.x.org/archives/xorg-devel/2009-August/001822.html), the new versions are planned to be released shortly before or during the [X Developers Conference (XDC) 2009](http://xorg.freedesktop.org/wiki/Events/XDC2009) at the end of September. The developers did, though, postpone the integration of XKB2 (X Keyboard ExtensionÂ 2) to X Server 1.8. Meanwhile, the X hackers have released a [first snapshot](http://lists.x.org/archives/xorg-devel/2009-August/001822.html) of X Server 1.7; the [release email](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/762) lists some of the new features scheduled for this version, which has been code-named "Depressed Dodo".

<!-- -->

- Atheros developer Luis R. Rodriguez (mcgrof) has [announced](http://article.gmane.org/gmane.linux.kernel.wireless.general/39135) a new [homepage](http://wireless.kernel.org/en/users/Drivers/Atheros) for Atheros Linux Wi-Fi drivers as well as two new driver projects; the latter are to provide Linux support for AR5523 and AR9271 chips.

<!-- -->

- Red Hat developer Rik van Riel, who specialises in the kernel's MM subsystem, has [released](http://surriel.com/presentations) [the slides](http://surriel.com/system/files/summit2009-riel-turtle-and-hare.pdf) of a presentation recently given at the Red Hat Summit. They provide insight into the Red Hat developers' approach to kernel development and their interactions with the kernel hackers of the Linux main development branch.

<!-- -->

- More than a week ago, the developers of the [ALSA project](http://www.alsa-project.org/) [released](http://thread.gmane.org/gmane.linux.alsa.devel/66204) version 1.0.21 of the various ALSA components. Among the [advancements](http://www.alsa-project.org/main/index.php/Changes_v1.0.20_v1.0.21) is the integration of a audio driver for various models of Creative's Sound Blaster X-Fi series. This driver will also be part of [Linux 2.6.31](../site/news/item/Kernel-Log-Coming-in-2-6-31-Part-2-Graphics-audio-and-video-742867.html "Kernel Log - Coming in 2.6.31 - Part 2: Graphics, audio and video â 07 August 2009, 15:53").

<!-- -->

- KVM developer Avi Kivity will from now on [share](http://thread.gmane.org/gmane.linux.kernel/884081) the maintenance of the kernel's KVM sources with Marcelo Tosatti, who's already made a name for himself as the maintainer of the 2.4 kernel series.

<!-- -->

- Chris Wilson has released numerous benchmark results with various graphics drivers and configurations [in his blog](http://ickle.wordpress.com/).

<!-- -->

- The developers of the [Gphoto project](http://gphoto.sourceforge.net/) have made version 2.4.7 of the libgphoto2 library for reading out camera data available [to download](http://gphoto.sourceforge.net/download/). The new version offers [a range of minor improvements](http://gphoto.sourceforge.net/news/) for cameras and PTP devices by various manufacturers.

<!-- -->

- Several statements and links provided by Harald Welte in [a blog entry](http://laforge.gnumonks.org/weblog/2009/08/28#20090828-helping_samasung_system_lsi) indicate that in future, Samsung's System LSI division will more actively pursue the integration of its extensions and Linux-specific improvements into the kernel's main development branch.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the Kernel Log at The H Open Source:*

- [Kernel Log - Coming in 2.6.31 - Part 5: CUSE, USB 3.0, FireWire networking and the rest](../site/news/item/Kernel-Log-Coming-in-2-6-31-Part-5-CUSE-USB-3-0-FireWire-networking-and-the-rest-743173.html "Kernel Log: Coming in 2.6.31 - Part 5: CUSE, USB 3.0, FireWire networking and the rest â 31 August 2009, 08:02")
- [Kernel Log - Coming in 2.6.31 â€“ Part 4: Tracing, architecture, virtualisation](../site/news/item/Kernel-Log-Coming-in-2-6-31-Part-4-Tracing-architecture-virtualisation-743099.html "Kernel Log - Coming in 2.6.31 – Part 4: Tracing, architecture, virtualisation â 26 August 2009, 10:36")
- [Kernel Log â€“ Coming in 2.6.31 - Part 3: Storage and file systems](../site/news/item/Kernel-Log-Coming-in-2-6-31-Part-3-Storage-and-file-systems-742967.html "Kernel Log – Coming in 2.6.31 - Part 3: Storage and file systems â 17 August 2009, 09:48")
- [Kernel Log - Coming in 2.6.31 - Part 2: Graphics, audio and video](../site/news/item/Kernel-Log-Coming-in-2-6-31-Part-2-Graphics-audio-and-video-742867.html "Kernel Log - Coming in 2.6.31 - Part 2: Graphics, audio and video â 07 August 2009, 15:53")
- [Kernel Log: X server 1.7 delayed; Compiz runs on newer Radeon GPUs; DRBD in kernel soon](../site/news/item/Kernel-Log-X-server-1-7-delayed-Compiz-runs-on-newer-Radeon-GPUs-DRBD-in-kernel-soon-742829.html "Kernel Log: X server 1.7 delayed; Compiz runs on newer Radeon GPUs; DRBD in kernel soon â 05 August 2009, 16:55")
- [Kernel Log: progress with free graphics drivers, three new stable kernels](../site/news/item/Kernel-Log-progress-with-free-graphics-drivers-three-new-stable-kernels-742411.html "Kernel Log: progress with free graphics drivers, three new stable kernels â 09 July 2009, 09:42")

*Older Kernel Logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/).*

([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
