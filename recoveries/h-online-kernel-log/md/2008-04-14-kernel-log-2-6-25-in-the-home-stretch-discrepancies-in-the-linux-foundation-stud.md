---
title: "Kernel Log: 2.6.25 in the home stretch, discrepancies in the Linux Foundation study"
date: 2008-04-14
author: "Terry Relph-Knight"
source: http://www.h-online.com/open/news/item/Kernel-Log-2-6-25-in-the-home-stretch-discrepancies-in-the-Linux-Foundation-study-734765.html
pages: 1
---

# Kernel Log: 2.6.25 in the home stretch, discrepancies in the Linux Foundation study

**Terry Relph-Knight**

![Kernel Log logo:](../site/imgs/43/3/6/1/5/4/0/a345f5e7c547062f.jpg) In making **2.6.25-rc8** public last week, Linus Torvalds [released](http://thread.gmane.org/gmane.linux.kernel/660693) the eighth pre-release of Linux 2.6.25. In doing, so he was silent on when the next version of the main development line would be released, only mentioning that some of the errors that users had pointed out had been corrected. With the [2.6.25-rc7 release](http://thread.gmane.org/gmane.linux.kernel/657983) a week ago, Torvalds awakened hope that Linux 2.6.25 would soon be complete with the words, "*Give it a good testing, because we're hopefully now well on our way towards that eventual real 2.6.25 release!*" Indeed, this does not seem too far off – barring the appearance of some new, critical and difficult to remedy error, the Kernel Log author is aiming for a release within the next 14 days.

Greg Kroah-Hartmann emphasised [in his blog](http://www.kroah.com/log/diary/2008_03_01.html) that in the **Linux Foundation study** [released yesterday](../site/news/item/Linux-Foundation-study-goes-behind-the-scenes-of-kernel-development-734755.html "Linux Foundation study goes behind the scenes of kernel development – 02 April 2008, 01:05") on the background of Linux development, Andrew Morton, who is currently employed by Google, was falsely identified as working for the Linux Foundation. Other developers or their employers have also announced that either they, or their employees had been improperly associated; on this point, Kroah-Hartmann indicated that the notes used for the evaluation as well as the log files are available [for download](http://www.kernel.org/pub/linux/kernel/people/gregkh/kernel_history/) at Kernel.org.

One of the items located in the `config/` directory of the [notes archive](http://www.kernel.org/pub/linux/kernel/people/gregkh/kernel_history/gitdm-0.02.tar.bz2) (TAR file) is the file matching email addresses to employers. This allows a number of developers, who only use their private e-mails, to be associated with the hands that feed them. Al Viro and David S. Miller, who [according to the study](../site/news/item/Linux-Foundation-study-goes-behind-the-scenes-of-kernel-development-734755.html "Linux Foundation study goes behind the scenes of kernel development – 02 April 2008, 01:05") have added the most patches to the kernel over the past three years , get their pay checks from Red Hat; Miklos Szeredi, on the other hand, works for Novell, while H. Peter Anvin (hpa) switched recently to rPath.

Jeff Garzik, who among other things maintains the Libata subsystem, recently transferred information about the new Linux kernel SATA and PATA drivers from his website to a [Kernel.org Wiki](http://ata.wiki.kernel.org). In the course of this work, he created [a new document](http://ata.wiki.kernel.org/index.php/Libata_error_messages) that helps to interpret ATA specific error messages.

### Kernel Log in brief

- April fools day jokes made their appearance on the Linux Kernel Mailing List (LKML) too. One prankster posing as a Kernel.org admin announced that Fedora's servers were [switching to](http://thread.gmane.org/gmane.comp.version-control.git/78615) FreeBSD 7.0. One day prior to April 1st, someone on the Linux Kernel Mailing List (LKML) [opined](http://thread.gmane.org/gmane.linux.kernel/659973) that it sure would be cool if drivers written in Java for Solaris could be used under Linux too. The author had to put up with [all sorts](http://thread.gmane.org/gmane.linux.kernel/659973/focus%3D659992) of [razzing](http://thread.gmane.org/gmane.linux.kernel/659973/focus%3D660012) from the old timer developers in the discussion.
- Running a pre-release of Fedora 9 on his wife's computer, Linus Torvalds was not able to view YouTube videos with Swfdec, leading him to send a [comical error report](https://bugzilla.redhat.com/show_bug.cgi?id=439858) in which he makes an ardent appeal for help to Fedora developers, "*This is 'high' priority because the wife will kill me if she doesn't have her videos.*"
- With the [release](http://lists.freedesktop.org/archives/xorg-announce/2008-April/000531.html) of version 2.8.0, X developers [changed the name](http://lists.freedesktop.org/archives/xorg-announce/2008-April/000530.html) of the X.org driver responsible for the graphic unit in Geode CPUs from xf86-video-amd to xf86-video-geode.
- Programmer Val Henson, who specialises in file system programming, published a [presentation](http://valhenson.org/review/shdh.pdf) in [her blog](http://valhenson.livejournal.com/14486.html) aimed at helping Web 2.0 startups to select the right file system (*'What file system should I use?' for your typical web 2.0 startup*). Her pragmatic answer: employ a couple of tricks to make the file system irrelevant.
- AMD has released a [new version](http://www.x.org/docs/AMD/R5xx_Acceleration_v1.3.pdf) of the (3D) graphic chip documentation for R3*xx* to R5*xx* chips.
- Kristian Høgsberg has [integrated](http://sourceforge.net/mailarchive/forum.php?thread_name=59ad55d30803311434s2344ce80t5de9b7771a62cb89%40mail.gmail.com&forum_name=dri-devel) the last big piece of the still experimental DRI2 framework into the DRI developer branch. But DRI2 requires developer versions from X.org and Mesa, as well as other experimental programs; a special version of the graphic driver for Intel hardware is the only one that already supports the DRI2 framework.

*More information and background on developments in the Linux kernel and its environment can also be found in previous issues of the Kernel Log on heise Open:*

- 03.03.2008: [Proprietary Linux drivers stumble and spark debate](../site/news/item/Kernel-log-Proprietary-Linux-drivers-stumble-and-spark-debate-734409.html "Kernel log: Proprietary Linux drivers stumble and spark debate – 07 March 2008, 11:07")
- 22.02.2008: [ATI graphics driver updated, discussions about when to integrate Linux drivers](../site/news/item/Kernel-Log-ati-graphics-driver-updated-discussions-about-when-to-integrate-Linux-drivers-734361.html "Kernel Log: ati graphics driver updated, discussions about when to integrate Linux drivers – 27 February 2008, 16:13")
- 15.02.2008: [New AMD, HP and SANE drivers; Linux Weather Forecast updated](../site/news/item/Kernel-log-New-AMD-HP-and-SANE-drivers-Linux-Weather-Forecast-updated-734285.html "Kernel log: New AMD, HP and SANE drivers; Linux Weather Forecast updated – 20 February 2008, 13:40")
- 13.02.2008: [Linux-next to speed development work](../site/news/item/Kernel-Log-Linux-next-to-speed-development-work-734227.html "Kernel Log: Linux-next to speed development work – 14 February 2008, 10:38")

([trk](mailto:trk@h-online.com "Terry Relph-Knight"))
