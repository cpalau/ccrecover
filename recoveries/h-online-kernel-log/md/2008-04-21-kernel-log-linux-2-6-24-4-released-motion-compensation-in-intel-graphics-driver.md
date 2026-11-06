---
title: "Kernel log: Linux 2.6.24.4 released, motion compensation in Intel graphics driver"
date: 2008-04-21
author: "Terry Relph-Knight"
source: http://www.h-online.com/open/news/item/Kernel-log-Linux-2-6-24-4-released-motion-compensation-in-Intel-graphics-driver-734669.html
pages: 1
---

# Kernel log: Linux 2.6.24.4 released, motion compensation in Intel graphics driver

**Terry Relph-Knight**

![Kernel log logo](../site/imgs/43/3/6/1/4/4/4/a345f5e7c547062f.jpg) With Linux version 2.6.24.4, the administrators of the kernel's Stable Series have [released](http://thread.gmane.org/gmane.linux.kernel/657306) the fourth update of Linux kernel 2.6.24, which was [released](../site/open/features/What-s-new-in-Linux-2-6-24-746464.html "What's new in Linux 2.6.24 – 05 February 2008, 14:51") at the end of January. 2.6.24.4 includes about 75 changes which correct numerous kernel and driver flaws; however, this update does not address any security issues marked with CVE numbers and admins don't have to update to the latest version if the [corrections](http://thread.gmane.org/gmane.linux.kernel/657306) aren't relevant for their respective systems.

Meanwhile, X.org developers have been busy and have released a good number of [updated drivers](http://lists.freedesktop.org/archives/xorg-announce/2008-March/thread.html) in the last few days – some of them in preparation for X.org 7.4, which is expected for release at the end of April. The updated drivers include [graphics](http://lists.freedesktop.org/archives/xorg-announce/2008-March/000505.html) and [mouse](http://lists.freedesktop.org/archives/xorg-announce/2008-March/000525.html) drivers for VMware hosts as well as an updated [SIS graphics driver](http://lists.freedesktop.org/archives/xorg-announce/2008-March/000499.html). The preliminary version of the 2.3 driver series for Intel graphic chipsets was released and is the first to offer hardware support for motion compensation in MPEG playback via [XvMC](http://www.xfree86.org/~mvojkovi/XvMC_API.txt) – however, it is so far only available for the 915, 945 and G33 chipset varieties and not yet for G965.

The drivers for the latest Radeon graphics chips have also received some work. AMD's Alex Deucher has [integrated](http://gitweb.freedesktop.org/?p=mesa/drm.git;a=commit;h=d8af16d2a75f38dacb9b87a4b317790c88c6ba40) the microcode for Radeon graphics chips released by AMD into the development path of Mesa/DRM; a separate Git branch also received [first components](http://airlied.livejournal.com/58224.html) for 3D acceleration support for R5*xx* chips, which are used in Radeon's X1*xxx* series. The development branch of the "ati" driver was [recently](http://www.botchco.com/agd5f/?p=24) upgraded to include the EXA acceleration architecture for R3*xx*, R4*xx* and R5*xx* chips.

### Kernel log in brief

- The author of Kernel Log and other subscribers of the Linux Kernel Mailing List (LKML) were able to put their feet up for more than 24 hours last week when the server which handles the LKML was down due to a hardware defect. The defect has [now been fixed](http://vger.kernel.org/~davem/cgi-bin/blog.cgi/2008/03/19#vger_recovering) and LKML subscribers can again find their daily three to five hundred emails in their inboxes.
- Zach Brown has [released](http://www.zabbo.net/post/crfs-source-available-now-with-kernel-building-mostly/) the source code of his experimental [CRFS](http://oss.oracle.com/projects/crfs/) network file system which is based on Btrfs.

([trk](mailto:trk@h-online.com "Terry Relph-Knight"))
