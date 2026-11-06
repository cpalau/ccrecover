---
title: "Kernel-Log: Users of 2.4 provide feedback, 2.4.36.5 and 2.6.26-rc5 released"
date: 2008-06-10
author: "Terry Relph-Knight"
source: http://www.h-online.com/open/news/item/Kernel-Log-Users-of-2-4-provide-feedback-2-4-36-5-and-2-6-26-rc5-released-735437.html
pages: 1
---

# Kernel-Log: Users of 2.4 provide feedback, 2.4.36.5 and 2.6.26-rc5 released

**Terry Relph-Knight**

![Kernel log logo](../site/imgs/43/3/6/2/2/1/2/a345f5e7c547062f.jpg) Having [requested](http://thread.gmane.org/gmane.linux.kernel/672383) feedback from users of series 2.4 on the LKML a few weeks ago, kernel series 2.4 maintainer Willy Tarreau recently published [an evaluation](http://thread.gmane.org/gmane.linux.kernel/672383/focus%3D688527) of the 22Â relevant replies. About half of those who replied use the 2.4 kernel on "general purpose" servers (WWW, Mail, DNS, Samba, NFS). According to the information received by Tarreau most of them see no reason why they should switch to a more recent kernel. Survey respondents said that often there just isn't enough time and switching to a new kernel might cause problems.

According to the survey, 20Â per cent of the installed 2.4 kernels run on application-specific servers which require an involved set up procedure and are vitally important. One tenth of those who replied use the 2.4 kernel with embedded systems, routers, firewalls or VPN servers. Only about 5Â per cent of users run series 2.4 kernels on old notebooks and desktop PCs.

In early June, Tarreau released another new series 2.4 kernel, [Linux 2.4.36.5](http://thread.gmane.org/gmane.linux.kernel/688509). Among other things, this version fixes three "medium" security holes: One is located in the [Code for SIT](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2008-2136) (Simple Internet Transition), another in [Sparc support](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2008-2137) and the third in the [Moxa driver](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2005-0504). On the 5th of June, Linus Torvalds released [Linux 2.6.26-rc5](http://thread.gmane.org/gmane.linux.kernel/690130), the fifth pre-release version of 2.6.26. A release date for the finished version has not yet been established. It will probably take another two or three weeks to finalise. A few days ago the list of errors not contained in 2.6.25 was still [115 entries](http://thread.gmane.org/gmane.linux.kernel/688163) long.

**Kernel log in brief**:

- [In his blog](http://kernelslacker.livejournal.com/124084.html), kernel developer Dave Jones criticises processor and chipset manufacturer VIA for not providing any source code or developers' documentation one month after the launch with a lot of publicity of the new [Linux portal](http://linux.via.com.tw/). This was set up to promote co-operation with the open source community. He also critically notes that VIA sells precompiled kernel modules labelled as GPL releases without providing the respective sources.
- On the DRI mailing list, the developers of the Radeon and Radeonhd graphics drivers [are discussing](http://sourceforge.net/mailarchive/forum.php?thread_name=20080604185939.GA27106%40suse.de&forum_name=dri-devel) how to best integrate 3D support for the R600 chips used in the series 2000 and 3000 Radeon HD models.
- Chris Mason has [published](http://thread.gmane.org/gmane.linux.file-systems/24103) version 0.15 of the experimental Btrfs file system.
- Matthew Garrett has [presented](http://thread.gmane.org/gmane.linux.kernel.input/4993/focus%3D31276) a driver for the WMI interface found in modern HP notebooks in the form of a patch; among other things, the driver enables or disables light sensors, WLANs or Bluetooth via selected keys or key combinations.
- Xen programmers have set up a [new page](http://wiki.xensource.com/xenwiki/XenParavirtOps) in their wiki to deal specifically with the current and future development of the Xen version based on Paravirt_ops which has been part of the kernel since Linux 2.6.23.
- Mark Lord has released [Version 8.7](http://thread.gmane.org/gmane.linux.ide/32003) of [hdparm](http://sourceforge.net/projects/hdparm/).
- Intel developers of the [Linuxwimax project](http://linuxwimax.org/) have [released](http://thread.gmane.org/gmane.linux.kernel.wireless.general/15483) version 1.2 of the Linux-Wimax driver for Intel hardware.

*Find more background information about the developments around the Linux kernel and its environment in previous editions of the kernel log at heise Open:*

- 29.05.2008: [Kernel log: new gfx drivers for GeForce & Radeon GPUs; Kernel Track at LinuxTAG](../site/news/item/Kernel-log-new-gfx-drivers-for-GeForce-Radeon-GPUs-Kernel-Track-at-LinuxTAG-735349.html "Kernel log: new gfx drivers for GeForce & Radeon GPUs; Kernel Track at LinuxTAG â 30 May 2008, 14:23")
- 16.05.2008: [Kernel log: the latest Linux versions provide better security and patch flaws](../site/news/item/Kernel-log-the-latest-Linux-versions-provide-better-security-and-patch-flaws-735237.html "Kernel log: the latest Linux versions provide better security and patch flaws â 19 May 2008, 15:41")

<!-- -->

- 17.04.2008: [Improvements throughout â€“ What's new in Linux 2.6.25](../site/open/features/Improvements-throughout-what-s-new-in-Linux-2-6-25-746484.html "Improvements throughout – what's new in Linux 2.6.25 â 21 April 2008, 08:49")

*Find previous editions of the kernel log in [the archive](http://www.heise-online.co.uk/open/news/archive/) or through [the search function](http://www.heise-online.co.uk/open/search/?rm=search&q=&search_submit=Search) at [heise open](http://www.heise-online.co.uk/open/).*

([trk](mailto:trk@h-online.com "Terry Relph-Knight"))
