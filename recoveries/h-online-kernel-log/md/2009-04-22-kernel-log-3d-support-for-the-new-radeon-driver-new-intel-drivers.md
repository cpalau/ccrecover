---
title: "Kernel Log: 3D support for the new Radeon driver; new Intel drivers"
date: 2009-04-22
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-3D-support-for-the-new-Radeon-driver-new-Intel-drivers-741271.html
pages: 1
---

# Kernel Log: 3D support for the new Radeon driver; new Intel drivers

**Dj Walker-Morgan**

![Kernel Log Penguin](../site/imgs/43/3/6/7/7/0/3/a345f5e7c547062f.jpg) Developers for AMD and Intel graphics chips have been extremely productive, having introduced a range of improvements, with others in the works. Late last week, AMD employee Alex Deucher [released](http://thread.gmane.org/gmane.comp.freedesktop.xorg.drivers.ati/8504) experimental drivers, DRM, and Mesa code that enables 3D acceleration in r6xx and r7xx graphics chips used in most of the Radeon graphics cards currently on the market. While the code is not fully mature, Glxgears should already work.

Following the [release](../site/news/item/Kernel-Log-New-stable-kernels-AMD-3D-documentation-and-Mesa-7-3-released-739845.html "Kernel Log: New stable kernels, AMD 3D documentation and Mesa 7.3 released – 28 January 2009, 11:41") several months ago of very rudimentary code to activate 3D support for these Radeon GPUs, the functionality finally appears to be within reach. However, it could be months before the code is mature enough to be included in the mainstream distributions.

Shortly before the release of the drivers, Alex Deucher announced [on his blog](http://www.botchco.com/agd5f/?p=41) that he was working on expanded support of the power-saving technology featured in the Radeon GPUs. That should be especially welcome news to users of Linux notebooks with ATI/AMD chips, since these chips draw a few watts more with the open source drivers than with the proprietary ones, noticeably shortening battery life. Improvements to video playback under the radeon driver are also [in the works](http://www.botchco.com/agd5f/?p=42).

**More driver games**

Just a few days ago, AMD [released](http://support.amd.com/us/gpudownload/Pages/index.aspx) version 9.4 of its proprietary driver, as well as the Linux driver known as fglrx, or Catalyst. The [release notes](http://www2.ati.com/drivers/linux/catalyst_94_linux.pdf)![PDF](../site/icons/file-pdf.gif "PDF document") provide an overview of the most important updates. The improvements include support for [X-Server 1.6](../site/news/item/X-Server-1-6-released-740261.html "X Server 1.6 released – 26 February 2009, 10:03"), which among other things will be included in Ubuntu 9.04 slated for release within the next few days. However, support for this version of Ubuntu will still be considered an "early look".

As [previously announced](../site/news/item/AMD-stops-maintaining-proprietary-Linux-drivers-for-older-graphics-hardware-740421.html "AMD stops maintaining proprietary Linux drivers for older graphics hardware – 09 March 2009, 15:02"), support for graphics hardware with R3xx, R4xx and R5xx series GPUs has been killed off. While version 9.3 of the driver for graphics cards with these chips will still be available for download, it already has trouble running on distributions that use the Linux 2.6.29 kernel.

<table>
<tbody>
<tr>
<td colspan="3">Radeon graphics hardware</td>
</tr>
<tr>
<td>GPU</td>
<td>Used on graphics card models¹</td>
<td>Corresponding OSS driver</td>
</tr>
<tr>
<td>r1xx</td>
<td>Radeon, Radeon 7xxx</td>
<td><a href="http://wiki.x.org/wiki/radeon">radeon</a></td>
</tr>
<tr>
<td>r2xx</td>
<td>Radeon 8500 – 9250</td>
<td><a href="http://wiki.x.org/wiki/radeon">radeon</a></td>
</tr>
<tr>
<td>r3xx</td>
<td>Radeon 9500 – x600, x1050</td>
<td><a href="http://wiki.x.org/wiki/radeon">radeon</a></td>
</tr>
<tr>
<td>r4xx</td>
<td>Radeon x700 – x850</td>
<td><a href="http://wiki.x.org/wiki/radeon">radeon</a></td>
</tr>
<tr>
<td>r5xx</td>
<td>Radeon x1300 – x1950</td>
<td><a href="http://wiki.x.org/wiki/radeon">radeon</a>, <a href="http://wiki.x.org/wiki/radeonhd">radeonhd</a></td>
</tr>
<tr>
<td>r6xx</td>
<td>Radeon HD 2400 – HD 3850</td>
<td><a href="http://wiki.x.org/wiki/radeon">radeon</a>, <a href="http://wiki.x.org/wiki/radeonhd">radeonhd</a></td>
</tr>
<tr>
<td>r7xx</td>
<td>Radeon HD 4350 – HD 4890</td>
<td><a href="http://wiki.x.org/wiki/radeon">radeon</a>, <a href="http://wiki.x.org/wiki/radeonhd">radeonhd</a></td>
</tr>
<tr>
<td colspan="3">¹ selected models</td>
</tr>
</tbody>
</table>

Programmers for the radeon (xf86-video-ati) and radeonhd (xf86-video-radeonhd) open source graphics drivers also recently released new versions of their drivers. [Version 6.12.2 of the radeon](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/595) driver essentially fixes bugs and contains improvements for textured video with Radeon R2xx and R3xx GPUs.

**Radeon graphics**

The [version 1.2.5](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/596) driver for graphics hardware with R5xx, R6xx and R7xx series Radeon GPUs, [radeonhd](http://wiki.x.org/wiki/radeonhd), seems to offer many more updates. Among the changes are 2D and Xv acceleration for R6xx and R7xx GPUs, for which users will need a kernel with a current DRM (direct rendering manager) or [updated DRM module](http://wiki.x.org/wiki/radeonhd%3Ar6xx_r7xx_branch). In versions 1.2.5 and above, DRI support is now active by default for cards with R5xx GPUs. Support for the RS880 (a new, yet to be released motherboard chip-set with integrated graphics) and RV790 (the Radeon HD 4890 GPU) is also new.

Both of these GPUs are also supported by the new version of the radeon driver, which has been able to handle 2D and Xv acceleration since version 6.12.0 was released in mid-March. It is still anyone's guess how long R5xx, R6xx and R7xx GPU owners will have the choice between radeon and radeonhd. Dave Airlie, Red Hat developer and one of two main radeon driver developers – the other is Alex Deucher of AMD – recently explained [in an email](http://thread.gmane.org/gmane.linux.redhat.fedora.devel/109688/focus%3D109730) how the two-driver situation came about. He said that radeonhd had no future and that radeon supported the new kernel-based mode setting systems (KMS), which practically made the 2D driver obsolete anyway – whatever else radeonhd did was based on code that it shared with radeon. ("*So radeonhd is going nowhere new, radeon is the only driver that supports the new kernel mode setting systems. With kernel mode setting the X.org 2D driver doesn't do very much any more, and everything that is left for it to do is shared code between the two drivers.*").

**Intel graphics**

Developers of the xf86-video-intel graphics driver – "intel" for short – have released [version 2.7.0](http://article.gmane.org/gmane.comp.freedesktop.xorg.announce/604) of the driver. According to the release e-mail, the version corrects a tidy number of bugs, but also has some new functions, such as TV-out support for the D945GCLF2, SDVO-LVDS support, and video playback without "tearing" between video frames (tear-free XV), although the latter does not always work. Still, the driver is supposed to be most reliable and fastest in combination with kernel-based mode setting (KMS) ("*We encourage users to use kernel mode setting and UXA acceleration with this release, which should give the best performance and robustness.*")

People interested in how GPUs work and how to program them can find numerous details about the graphics core of Intel's highest performance motherboard chip-set with integrated graphics to date in the [recently](http://thread.gmane.org/gmane.comp.video.dri.devel/35032) released [G45 Programmer’s Reference Manual](http://intellinuxgraphics.org/documentation.html). [Matthew Garrett](http://www.advogato.org/person/mjg59/diary.html?start=203) and [Adam Williamson](http://www.happyassassin.net/2009/04/16/whats-happening-on-the-poulsbo-front/) are currently complaining in their blogs that the [dodgy situation](../site/news/item/Kernel-Log-Stable-series-development-is-speeding-up-X-Server-1-6-available-soon-740203.html "Kernel Log: Stable series development is speeding up, X Server 1.6 available soon – 23 February 2009, 10:46") with the Linux driver for the US15W (Poulsbo) Intel chipset still has not improved and that there is no real remedy in sight in the near term.

**Kernel status**

- Willy Tarreau has [released Linux 2.4.37.1](http://thread.gmane.org/gmane.linux.kernel/824665), which plugs a number of security holes already corrected in the newer 2.6 series kernels.

<!-- -->

- Nearly a week ago, Linus Torvalds released the [second pre-release](http://thread.gmane.org/gmane.linux.kernel/822502) of Linux 2.6.30, indicating that 2.6.30-rc3 is likely on the way soon (see part 1 of the "[What's coming in 2.6.30](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-Network-New-Wi-Fi-drivers-and-other-network-novelties-741197.html "Kernel Log: What's coming in 2.6.30 - Network: New Wi-Fi drivers and other network novelties – 17 April 2009, 10:51")" Kernel Log series on The H).

**In Brief**

- Adam Jackson has released [version 1.6.1](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/601) of the X.org X-Servers, which is distinguished from its predecessor mainly by a number of small bug fixes.

<!-- -->

- Following the announcement of Oracle's takeover of Sun ([1](../site/open/features/With-Oracle-buying-Sun-what-will-become-of-Java-MySQL-and-OpenOffice-746434.html), 2), Oracle's Chris Mason, the main developer of Btrfs, made it clear [in an email](http://thread.gmane.org/gmane.comp.file-systems.btrfs/2880), that Oracle's takeover would in no way influence plans for Btrfs and that Btrfs would continue to be an important project ("*This does not change Oracle's plans for Btrfs at all, and Btrfs is still a key project for us.*")

<!-- -->

- X.org developers' decision [last autumn](../site/news/item/Kernel-Log-Short-video-interviews-with-Torvalds-Kroah-Hartman-and-others-737833.html "Kernel Log: Short video interviews with Torvalds, Kroah-Hartman and others – 28 October 2008, 15:46") to drop the ability to kill X-Server with CTRL+ALT+Backspace (DontZap) triggered lively discussion in web forums and mailing lists (see also: [LWN.net article](http://lwn.net/Articles/327141/)). In his blog, X.org programmer Peter Hutterer recently [introduced](http://who-t.blogspot.com/2009/04/zapping-server.html) a number of changes that allow the key combination to be switched on and off at run time.

<!-- -->

- [In another blog entry](http://who-t.blogspot.com/2009/04/synaptics-11-and-what-your-touchpad-can.html) Peter Hutterer gives an overview of some of the latest improvements in the xf86-input-synaptics touch pad driver – "synaptics" for short. Hutterer explains how to tell if a user's own touch pad supports multi-touch.

<!-- -->

- Till Kamppeter has [released version 4.0.1 of Foomatic](http://forums.linux-foundation.org/read.php?21,9146).

<!-- -->

- Glibc developer Ulrich Drepper gave a detailed description of the plans for Glibc version 2.10 [in his blog](http://udrepper.livejournal.com/20948.html). Among other things, the new version will support POSIX 2008 and C++ 201x.

<!-- -->

- The [X Developers' Conference (XDC) 2009](http://xorg.freedesktop.org/wiki/Events/XDC2009) will take place this year from the 28th to the 30th of September in Portland, Oregon, immediately following this year's [Linux Plumbers Conference](http://linuxplumbersconf.org/2009/).

<!-- -->

- [Gphoto project](http://gphoto.sourceforge.net/) developers [have released](http://gphoto.sourceforge.net/download/) version 2.4.5 of the libgphoto2 library, enabling connectivity with numerous different camera models. The new driver contains a [number of small improvements](http://gphoto.sourceforge.net/news/) for cameras and PTP devices from various manufacturers.

<!-- -->

- Christoph Hellwig recently sent out the [March issue](http://news.gmane.org/find-root.php?message_id=20090416201426.GA6035@infradead.org) of the monthly XFS status report to the LKML (Linux Kernel Mailing List)..

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the Kernel Log at The H Open Source:*

- [Kernel Log: What's coming in 2.6.30 - Network: New Wi-Fi drivers and other network novelties](../site/news/item/Kernel-Log-What-s-coming-in-2-6-30-Network-New-Wi-Fi-drivers-and-other-network-novelties-741197.html "Kernel Log: What's coming in 2.6.30 - Network: New Wi-Fi drivers and other network novelties – 17 April 2009, 10:51")
- [Kernel Log: Linux 2.6.30 is taking shape](../site/news/item/Kernel-Log-Linux-2-6-30-is-taking-shape-741093.html "Kernel Log: Linux 2.6.30 is taking shape – 09 April 2009, 06:41")
- [Kernel Log: Development of 2.6.30 is under way](../site/news/item/Kernel-Log-Development-of-2-6-30-is-under-way-740805.html "Kernel Log: Development of 2.6.30 is under way – 27 March 2009, 17:33")
- [Steady Growth: What's new in Linux 2.6.29](../site/open/features/Steady-growth-What-s-new-in-Linux-2-6-29-746553.html)
- [Kernel Log: Tasmanian devil to be Linux's temporary mascot, new Radeon drivers](../site/news/item/Kernel-Log-Tasmanian-devil-to-be-Linux-s-temporary-mascot-new-Radeon-drivers-740667.html "Kernel Log: Tasmanian devil to be Linux's temporary mascot, new Radeon drivers – 19 March 2009, 15:43")
- [Kernel Log: What's new in 2.6.29 - Part 8: Faster start-up and other behind the scenes changes](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-8-Faster-start-up-and-other-behind-the-scenes-changes-740591.html "Kernel Log: What's new in 2.6.29 - Part 8: Faster start-up and other behind the scenes changes – 18 March 2009, 08:33")

*Older Kernel Logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/).*

([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
