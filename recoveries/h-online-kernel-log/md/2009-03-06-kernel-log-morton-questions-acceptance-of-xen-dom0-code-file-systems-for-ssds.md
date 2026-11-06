---
title: "Kernel Log: Morton questions acceptance of Xen Dom0 code; file systems for SSDs"
date: 2009-03-06
author: "Terry Relph-Knight"
source: http://www.h-online.com/open/news/item/Kernel-Log-Morton-questions-acceptance-of-Xen-Dom0-code-file-systems-for-SSDs-740375.html
pages: 1
---

# Kernel Log: Morton questions acceptance of Xen Dom0 code; file systems for SSDs

**Terry Relph-Knight**

![Kernel Log logo](../site/imgs/43/3/6/6/8/0/7/a345f5e7c547062f.jpg) In his [response](http://thread.gmane.org/gmane.linux.kernel/800658/) to the invitation on the Linux Kernel Mailing list (LKML) for comments on the recently submitted Xen Dom0 patches, [Andrew Morton](http://thread.gmane.org/gmane.linux.kernel/800658/focus%3D800714) asks whether accepting these kernel extensions into the main Linux development tree to operate as the leading Xen domain (Dom0) still makes sense. He has suggested that Xen may be the "old" way to achieve virtualisation, whereas the world is moving in a "new" direction, towards [KVM](http://kvm.qumranet.com). He also suggests that Linux developers could regret accepting Xen Dom0 support in three years' time ("*I hate to be the one to say it, but we should sit down and work out whether it is justifiable to merge any of this into Linux. I think it's still the case that the Xen technology is the "old" way and that the world is moving off in the "new" direction, KVM? In three years' time, will we regret having merged this?* ").

This has prompted a [debate](http://thread.gmane.org/gmane.linux.kernel/800658/focus%3D800714) on the pros and cons, and the relative advantages and drawbacks of Xen and KVM. Jeremy Fitzhardinge, a long-standing Xen developer who sent Xen Dom0 patches developed by him and others to the LKML, [campaigned](http://thread.gmane.org/gmane.linux.kernel/800658/focus%3D62079) strongly for Xen, but was to some extent rebuffed by other well known Linux developers, including [Nick Piggin](http://thread.gmane.org/gmane.linux.kernel/800658/focus%3D62056) and [Ingo Molnar](http://thread.gmane.org/gmane.linux.kernel/800658/focus%3D62044). As one of the managers of the kernel code for supporting the x86 architecture, Molnar could have an important say in the decision whether to accept Xen support. A decision has probably not been made yet, but in spite of the discussion stimulated by Morton and the objections of other kernel hackers, it's perfectly possible that the next-but-one Linux version (2.6.30) will incorporate Xen Dom0 code, based on these patches.

**How the situation arose**

In any case, it's difficult to make any predictions for the development model of the Linux kernel, because many developers, not least Linus Torvalds, can considerably speed up or hold back the acceptance of patches. Originally, Morton prophesied four years ago that acceptance of Xen support into the Linux kernel was imminent. At that time, however, kernel developers were already dissatisfied with some aspects of integrating it into the kernel sources, and asked for changes before it could be accepted.

While Xen developers were working on this, other Linux-specific virtualisation solutions appeared, such as [KVM](http://kvm.qumranet.com) (Kernel-based Virtual Machine) and Lguest (originally called Lhype). The kernel developers are consequently pressing for an interface that lets the Linux kernel work as efficiently as possible as a paravirtualised guest under all of these and other virtualisation solutions, without large quantities of special code having to be included in the kernel for each hypervisor. The paravirt_ops abstraction layer then emerged, largely under the leadership of the Lguest developer, and found its way into the main Linux development tree with Linux 2.6.20.

That same version also saw the developers accept the KVM virtualisation framework into Linux. Though only a few months old at the time, it fitted into the kernel much better than Xen support and, in the opinion of many kernel hackers, was clearly the technically more elegant solution, since it used the kernel itself as hypervisor and thus had recourse to the infrastructure of the kernel (scheduler, memory management, drivers), while the Xen hypervisor is positioned upstream of the Linux kernel.

On the other hand, KVM requires CPUs with virtualisation functions, like the AMD-V and Intel VT. Xen can also use these functions in order to virtualise unmodified guest systems, but if the CPU doesn't provide these functions, an operating system adapted to Xen can alternatively run as a guest under the Xen hypervisor using paravirtualisation. Fitzhardinge is now citing this difference as one of the advantages of Xen, though all recent x86 server processors and many desktop and notebook CPUs now provide virtualisation functions.

**Second attempt** ![Kernel Log logo - tiny](../site/imgs/43/3/6/6/8/0/7/19225e6e200286d6.jpg)

While KVM underwent further constant and rapid speedy development within normal work on the kernel, acquiring functions like migration and PCI device pass-through for guests, Xen developers were slow to move ahead with integrating Xen into the Linux kernel. Instead, they paid a lot of attention to further development of the Xen code, which is also used in commercial Xen products. It sits on top of Linux kernel 2.6.18, and doesn't satisfy the quality requirements of kernel developers. The 2.6.18 kernel however lacks many drivers for more recent PC components, so the distribution developers are porting this Xen code to later kernels. This was and still is extremely laborious and, in practice, the result only works after a fashion. This is probably one of the reasons that motivated Red Hat to buy Qumranet, a company specialising in KVM, and subsequently (according to \[ticker:uk_133390 recently divulged plans\]) to use KVM in various Red Hat products.

In parallel with their further development of the "old" Xen code, Fitzhardinge and others worked on Xen patches that fit better into the kernel and make more use of paravirt_ops. First, they developed the code for Xen guest systems (DomU), which the kernel developers incorporated into Linux version 2.6.23. This code is active in the standard kernel in many distributions, so these now also work without any problem as guest kernels under a modern Xen hypervisor.

But the Xen hypervisor doesn't do a lot on its own: instead, it collaborates intensively with a Dom0 kernel. Previously, these two could only be set on top of the old Xen code base, which kernel developers reject for its lack of quality. The patches now published by Fitzhardinge are intended to eliminate this deficiency and permit operation as a Dom0 system. As [he himself writes](http://thread.gmane.org/gmane.linux.kernel/800658/focus%3D62046), this has involved rewriting large chunks of the Xen code. The present patches only lay the foundations for Dom0 support, and are far from providing the range of functions that the older Xen code base offers. Fitzhardinge is accordingly planning further series of patches. Some time is likely to go by before these are ready and the most egregious errors in the (still young or even non-existent) code have been eliminated â€“ if indeed the kernel developers accept Dom0 support at all.

**SSDs and file systems**

Theodore Ts'o (also known as Ted Tso or Tytso) has blogged diligently in recent days on the subject of SSDs (solid state disks) and the Ext file systems in his care - Ext2, Ext3 and Ext4. He started off with "[Should File Systems Be Optimised for SSDs?](http://tytso.livejournal.com/60487.html)", going into detail on the mode of operation of SSDs and their wear-levelling functions. Tso's blog entry was inspired by Torvalds' recent discussion of that subject [in a web forum](http://www.realworldtech.com/forums/index.cfm?action=detail&id=93409&threadid=92678&roomid=2). But Tso hasn't found a simple answer to the question of whether file systems have to be optimised for SSDs, because that depends on the SSD in use, as well as on the further development of the still young and constantly changing technology of SSD.

In a [further blog entry](http://thunk.org/tytso/blog/2009/03/01/ssds-journaling-and-noatimerelatime/) he discusses in detail whether Ext2 is actually more suitable for SSDs than Ext3 or Ext4, as folk wisdom and some blog and forum entries claim. He has made many tests in the process, and also uses the support [for using Ext4 without a journal](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=0390131ba84fd3f726f9e24fc4553828125700bb) that was substantially prepared by Google developers and has been accepted into Linux 2.6.29. His tests show the differences between the various file systems and the various mounting options such as "noatime" and "relatime", finding the effect on performance of "noatime" is much greater than the choice of file system.

Ted's blog entry, "[Fast ext4 fsck times, revisited](http://tytso.livejournal.com/61600.html)", contains much additional material for anyone wishing to investigate file systems further, including information about the fsck times tested with different code paths, in order to arrange data within the file system and/or on the data medium. Christoph Hellwig gave a survey [in an email](http://thread.gmane.org/gmane.comp.file-systems.xfs.general/28461) of changes affecting the XFS file system that have recently been implemented or are planned for the near future. And if that isn't enough, while the developers of the btrfs file system [are working diligently](http://thread.gmane.org/gmane.linux.kernel/797450) on optimising its performance, Daniel Phillips continues to tinker with Tux3, keeping the public at large happy with snippets of information. For example, he recently [put online](http://thread.gmane.org/gmane.linux.file-systems/29826) a PDF version of a [presentation](http://tux3.org/docs/tux3.scale.7x.pdf)![PDF](../site/icons/file-pdf.gif "PDF document") he gave at SCALEÂ 7x, explaining the mode of operation of the Tux3 file system.

**Kernel status** ![Kernel Log logo - tiny](../site/imgs/43/3/6/6/8/0/7/19225e6e200286d6.jpg)

The managers of the stable kernel series published many new stable kernels in the first three weeks of February, but in recent days things have slowed down a little, so versions [2.6.27.19 and 2.6.28.7](http://marc.info/?l=linux-kernel&m=123517083213875&w=2), which were already mentioned in the previous Kernel Log and appeared shortly afterwards, are for the moment, up to date.

Development of version 2.6.29 has now reached [rc7](http://thread.gmane.org/gmane.linux.kernel/802158). On releasing it, Torvalds said an eighth pre-release version would probably be required, because [the list of newly introduced errors](http://thread.gmane.org/gmane.linux.power-management.general/13446) (regressions) was still fairly long. It may therefore take at least around one-and-a-half to two weeks for Linux 2.6.29 to appear.

**In brief:**

*Kernel*

- J.Â R.Â Okajima has initiated a [second attempt](http://thread.gmane.org/gmane.linux.file-systems/29813/) to get the [Aufs2](http://aufs.sf.net/) (Advanced Multi Layered Unification File System VersionÂ 2/Another Unionfs) file system accepted into the main Linux development tree. This prompted a [brief discussion](http://thread.gmane.org/gmane.linux.file-systems/29813/focus%3D29831) on whether the Linux developers should concentrate more on Aufs2 or on the older [Unionfs](http://www.filesystems.org/project-unionfs.html), which has been waiting for acceptance into the kernel for a long time.

<!-- -->

- The kernel developers [are working on support](http://thread.gmane.org/gmane.linux.kernel/799552) for ATA data media with 4Â kilobyte sectors.

<!-- -->

- The [Ksplice](http://www.ksplice.com/) developers are also working intensively for the acceptance\] of that framework in order to fix runtime kernel errors in the official kernel branch. Some fundamental patches are already in the developer branches that have been prepared for 2.6.30.

<!-- -->

- A recent article at IBM developerWorks describes the [way Linux SCSI drivers operate](http://www.ibm.com/developerworks/linux/library/l-scsi-api/index.html) in detail.

*X.org*

- The AMD developer Alex Deucher reports in his blog [on progress](http://www.botchco.com/agd5f/?p=39) with driver support for the graphic core in RS600 motherboard chip sets (Radeon Xpress X1200/X1250 for Intel CPUs) as well as [new code to support](http://www.botchco.com/agd5f/?p=40) EXA and Xv on R6xx and R7xx GPUs (Radeon 2000 series and later).

<!-- -->

- X.org developer Peter Hutterer describes in his blog how to emulate mouse wheel support with evdev 2.1 and Xinput 1.4, as well as the recently [released X Server 1.6](../site/news/item/X-Server-1-6-released-740261.html "X Server 1.6 released â 26 February 2009, 10:03").

<!-- -->

- The [driver packages](http://lists.freedesktop.org/archives/xorg-announce/2009-February/thread.html) recently released by the X.org developers include a new version of the graphics driver for Intel's graphics chip sets that incorporates many [important bug fixes](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/557/) for the 2.6 driver series. Some [new errors crept in](http://thread.gmane.org/gmane.comp.freedesktop.xorg.announce/557/focus%3D567), however, and these are corrected in the recently issued version 2.6.3.

<!-- -->

- AMD recently released [version 9.2](http://support.amd.com/us/gpudownload/linux/Pages/radeon_linux.aspx) of its proprietary Linux graphics driver fglrx.

*Miscellaneous*

- The [HPLIP project](http://hplipopensource.com) has released [version 3.9.2](http://hplipopensource.com/hplip-web/release_notes.html) of the HPLIP drivers for HP printers and multi-function devices [for downloading](http://hplipopensource.com/hplip-web/gethplip.html). These extend the list of supported printers to include three LaserJets, five Officejets and one Photosmart.

<!-- -->

- Mark Lord has [released](http://thread.gmane.org/gmane.linux.kernel/799552/focus%3D38698) version 9.12 of hdparm.

<!-- -->

- The developers of the LM sensors project have released [version 3.1.0](http://lists.lm-sensors.org/pipermail/lm-sensors/2009-March/025457.html) of this framework for triggering hardware monitoring chips. It contains a completely new script, sensors-detect, for setting up LM sensors.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at The H Open Source:*

- [Kernel Log: Stable series development is speeding up, X Server 1.6 available soon](../site/news/item/Kernel-Log-Stable-series-development-is-speeding-up-X-Server-1-6-available-soon-740203.html "Kernel Log: Stable series development is speeding up, X Server 1.6 available soon â 23 February 2009, 10:46")
- [Kernel Log: What's new in 2.6.29 - Part 4: ACPI, PCI, PM â€“ notebooks and power saving improvements](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-4-ACPI-PCI-PM-notebooks-and-power-saving-improvements-739889.html "Kernel Log: What's new in 2.6.29 - Part 4: ACPI, PCI, PM – notebooks and power saving improvements â 31 January 2009, 15:01")
- [Kernel Log: New stable kernels, AMD 3D documentation and Mesa 7.3 released](../site/news/item/Kernel-Log-New-stable-kernels-AMD-3D-documentation-and-Mesa-7-3-released-739845.html "Kernel Log: New stable kernels, AMD 3D documentation and Mesa 7.3 released â 28 January 2009, 11:41")
- [Kernel Log: What's new in 2.6.29 - Part 3: Kernel controlled graphics modes](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-3-Kernel-controlled-graphics-modes-739697.html "Kernel Log: What's new in 2.6.29 - Part 3: Kernel controlled graphics modes â 17 January 2009, 07:36")
- [Kernel Log: main development phase for 2.6.29 ends, new X.org drivers](../site/news/item/Kernel-Log-main-development-phase-for-2-6-29-ends-new-X-org-drivers-739633.html "Kernel Log: main development phase for 2.6.29 ends, new X.org drivers â 12 January 2009, 17:09")
- [Kernel Log: What's new in 2.6.29 - Part 2: WiMax](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-2-WiMAX-739621.html "Kernel Log: What's new in 2.6.29 - Part 2: WiMAX â 12 January 2009, 10:19")
- [Kernel Log: What's new in 2.6.29 - Part 1: Dodgy Wifi drivers and AP support](../site/news/item/Kernel-Log-What-s-new-in-2-6-29-Part-1-Dodgy-Wifi-drivers-and-AP-support-739619.html "Kernel Log: What's new in 2.6.29 - Part 1: Dodgy Wifi drivers and AP support â 11 January 2009, 16:08")

*Older Kernel logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/).*

([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([trk](mailto:trk@h-online.com "Terry Relph-Knight"))
