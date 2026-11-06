---
title: "Kernel Log: Coming in 2.6.34 (Part 3) - Graphics"
date: 2010-05-06
author: "Thorsten Leemhuis"
source: http://www.h-online.com/open/features/Kernel-Log-Coming-in-2-6-34-Part-3-Graphics-994262.html
pages: 1
---

# Kernel Log: Coming in 2.6.34 (Part 3) - Graphics

**Thorsten Leemhuis**

**The AMD and Intel graphics drivers now support a wider range of chips and make better use of power saving features on the older chips. A major revamp of the recently introduced KMS driver for NVIDIA graphics hardware means that the Nouveau driver for X.org will in future make use of kernel-based mode setting.**

Having renamed [Linux kernel 2.6.34-rc5](http://thread.gmane.org/gmane.linux.kernel/975498) [Sheep on Meth](http://git.kernel.org/linus/01bf0b64579ead8a82e7cfc32ae44bc667e7ad0f), late last week Linus Torvalds [released](http://thread.gmane.org/gmane.linux.kernel/979606) the sixth pre-release version of Linux 2.6.34. The rate and scope of changes is, as usual at this stage in the development cycle, slowly declining, but, apart from a vague suggestion that 2.6.34 is close to completion, Torvalds has given no indication of when it will be released – expectations are that it will be out in one to three weeks.

The Kernel Log will continue its reporting on the changes in 2.6.34 – this article, Part 3 in the "Coming in 2.6.34" series looks at [changes](http://thread.gmane.org/gmane.comp.video.dri.devel/43659) to the code for supporting graphics hardware. Parts [one](../site/open/features/Kernel-Log-Coming-in-2-6-34-Part-1-Network-Support-975937.html "Kernel Log: Coming in 2.6.34 (Part 1) - Network Support – 13 April 2010") and [two](../site/open/features/Kernel-Log-Coming-in-2-6-34-Part-2-File-Systems-985128.html "Kernel Log: Coming in 2.6.34 (Part 2) - File Systems – 23 April 2010") were devoted to the major changes in the network support and file system fields.

### AMD

One of the changes with the greatest long-term significance is likely to be the merger of patches which [add](http://git.kernel.org/linus/bcc1c2a1d22974215e39dc87ce746ba9a39223e5) rudimentary support for the Evergreen/R800 graphics chip to the Radeon DRM driver responsible for kernel-based mode setting (KMS). This will allow the kernel to address many of the Radeon HD-5000 series graphics cards introduced since the autumn which use this graphics chip. The driver doesn't at present make use of the acceleration features offered by these GPUs, but the drivers for older Radeon graphics hardware also started out this way, and they now do a pretty fine job.

From 2.6.34, the KMS driver for older Radeon GPUs will be able to activate [some of the dynamic power saving features](http://git.kernel.org/linus/c913e23a145ae07b6f9f88aae8cd5ad06b5729ff) offered by Radeon hardware. [Many other enhancements](http://www.botchco.com/agd5f/?p=49) in this area are in preparation for forthcoming versions of the kernel. In order to protect against malicious code, the Radeon DRM driver will in future [check](http://git.kernel.org/linus/961fb597c17e2e4f55407d56b7211c188ab41eff) that commands forwarded to the graphics chip are legitimate.

### Intel

The Intel KMS driver in [2.6.34](http://git.kernel.org/linus/bad720ff3e8e47a04bd88d9bbc8317e7d7e049d3) will already support the graphics cores known only by the codename Sandybridge, which Intel is expected to release early next year. The driver now [activates](http://git.kernel.org/linus/ee980b8003a25fbfed50c3367f2b426c870eaf90) memory self-refresh on Intel 9xx series chip-sets when the CPU goes into deep sleep mode. According to the commit comments, this reduces power consumption on an idling netbook containing the 945GSE chip-set by 0.8 Watts.

The kernel can now [adjust](http://git.kernel.org/linus/f97108d1d0facc7902134ebc453b226bbd4d1cdb) the clock speed of 'Ironlake' graphics cores used in Intel i3 and i5 core series CPUs. This function is also required to turbo boost the graphics core clock speed above the nominal speed on the mobile version of these processors. However, further changes required to be able to use the intelligent power sharing feature are [currently in development](http://thread.gmane.org/gmane.linux.kernel/966922).

### NVIDIA

The Nouveau driver for GeForce graphics hardware now includes everything you need to dynamically generate [open source firmware for NV50 GPUs](http://git.kernel.org/linus/d5f3c90d4f3ad6b054f9855b7b69137b97bda131) on demand, so that 8xxx, 9xxx and GTX2x0 series GeForce graphics chips will now run without the [controversial](../site/news/item/Kernel-Log-Coming-in-2-6-33-Part-3-Graphics-922495.html "Kernel Log: Coming in 2.6.33 (Part 3) - Graphics – 05 February 2010") ctxprogs, generated using proprietary graphics drivers. Other [major rejigging](http://git.kernel.org/linus/a1606a9596e54da90ad6209071b357a4c1b0fa82) of the driver means that the Nouveau driver for X.org for Linux 2.6.33 will not work with the 2.6.34 kernel and nor will the reverse combination. This kind of incompatible change to driver interfaces with userspace is not normally permitted, but, kernel hackers have decreed, is acceptable in this case because Nouveau is still a staging driver. The Nouveau development team has nonetheless been forced to endure a torrent of criticism from Torvalds on the Linux kernel mailing list. He is particularly concerned that the change makes it harder for testers to switch between different kernel versions in order to find out when a particular bug arose.

One of the reasons for adapting the API was the removal of a number of interfaces which the X.org driver relied on for non-KMS operation. Because the development team has also removed their counterparts for user mode setting (UMS) from the development branch of the X-org driver, KMS will from now on be compulsory for Nouveau – just as it is for the latest version of the graphics driver for Intel GPUs. The latest versions of the Radeon X.org driver all still contain UMS code, but this too is likely to be removed at some point in the future.

### Switching

On some laptops equipped with both onboard graphics and a separate graphics chip, the kernel can now switch between the two and switch off whichever is not being used in order to save power. '[VGA Switcheroo](http://git.kernel.org/linus/6a9ee8af344e3bd7dbd61e67037096cdf7f83289)' currently only works on some laptops and does not offer the ease of use of Windows, as it only switches when X Server is restarted – something which is not expected to change in the near future. Background information on VGA Switcheroo can be found in several old blog postings by Dave Airlie ([1](http://airlied.livejournal.com/70348.html), [2](http://airlied.livejournal.com/70480.html), [3](http://airlied.livejournal.com/70828.html), [4](http://airlied.livejournal.com/71012.html), [5](http://airlied.livejournal.com/71434.html)).

### Minor gems

Many further minor, but by no means insignificant, changes can be found in the list below, which contains the commit headers referring to the respective change. Like many of the references in the text above, the links point to the relevant commit in the [web front end](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git&a=summary) of the Git branch for the kernel sources maintained by Linus Torvalds at kernel.org. The commit comments and the patches themselves provide extensive further information on the respective changes.

- [agp/intel: Add support for Sandybridge.](http://git.kernel.org/linus/1089e3009572e07a1fe12c3408828f27c96453be)
- [agp/intel: official names for Pineview and Ironlake](http://git.kernel.org/linus/af86d4b0f064413d2f353a41cdc23b7dbff0823d)
- [backlight: Enable backlight in 88pm860x](http://git.kernel.org/linus/d07e8bf83fd71567aaf9c27c3b133ab3cf8f3c4c)
- [backlight: Enable max8925 backlight](http://git.kernel.org/linus/4f811ef0d40048ae80b6ea77080b814725bffc58)
- [backlight: mbp_nvidia_bl - add five more MacBook variants](http://git.kernel.org/linus/36bc5ee6a8d13333980fa54e97d3469d3d4cda98)
- [broadsheetfb: support storing waveform](http://git.kernel.org/linus/b32bfc3843f7fd090d30853d98866d923cfb8fff)
- [drivers/video/efifb.c: support framebuffer for NVIDIA 9400M in MacBook Pro 5,1](http://git.kernel.org/linus/8a3bdfe6cd841880a5d849c40f90093b3817f6e0)
- [drm: Add generic multipart buffer.](http://git.kernel.org/linus/7a9f0dd9c49425e2b0e39ada4757bc7a38c84873)
- [drm/i915: Add a new mobile Sandybridge PCI ID.](http://git.kernel.org/linus/a13e4093cbd3db91cc65ac8b8c2baadffa603ee9)
- [drm/i915: Disable FBC on 915GM and 945GM.](http://git.kernel.org/linus/8d06a1e1e9c69244f08beb7d17146483f9dcd120)
- [drm/i915: enable/disable LVDS port at DPMS time](http://git.kernel.org/linus/469d129664c5b83f37ca74913700d416d584833b)
- [drm/i915: give up on 8xx lid status](http://git.kernel.org/linus/7b9c5abee98c54f85bcc04bd4d7ec8d5094c73f4)
- [drm/i915: Record batch buffer following GPU error](http://git.kernel.org/linus/9df30794f609d9412f14cfd0eb7b45dd64d0b14e)
- [drm/i915: Stop trying to use ACPI lid status to determine LVDS connection.](http://git.kernel.org/linus/6e6c822868f113dabe3c33bdd91e883cc28fa11b)
- [drm/i915: Use a dmi quirk to skip a broken SDVO TV output.](http://git.kernel.org/linus/6070a4a928f8c92b9fae7d6717ebbb05f425d6b2)
- [drm/i915: use PIPE_CONTROL instruction on Ironlake and Sandy Bridge](http://git.kernel.org/linus/e552eb7038a36d9b18860f525aa02875e313fe16)
- [drm/nouveau: add module option to disable TV detection](http://git.kernel.org/linus/f4053509669f904aec70c51e2ff75563ba7ae823)
- [drm/nouveau: add option to allow override of dcb connector table types](http://git.kernel.org/linus/da647d5bf3c0a4b7ad150803910cb1d737ac522e)
- [drm/nouveau: Fix noaccel/nofbaccel option descriptions.](http://git.kernel.org/linus/81e2d42200cd8fa37ec4ebdc66373d0db0e05678)
- [drm/nouveau: Gigabyte NX85T connector table lies, it has DVI-I not HDMI](http://git.kernel.org/linus/53c44c3a065ac48c4ccb38f811cf7c5d305c9d4e)
- [drm/nv40: add LVDS table quirk for Dell Latitude D620](http://git.kernel.org/linus/2eb92c80074ecfbc691741720382007417f64523)
- [drm/radeon: add new RS880 pci id](http://git.kernel.org/linus/338e2b1d571e4873908b199c90d6a31f65137fe3)
- [drm/radeon/kms: add a power state type based on power state flags](http://git.kernel.org/linus/0ec0e74f784ca08eab0354ab1dada46924c39b73)
- [drm/radeon/kms: add code to select power state](http://git.kernel.org/linus/516d0e46c80d2d20391f4145c2c5e3915253b8bf)
- [drm/radeon/kms: add functions to get current pcie lanes](http://git.kernel.org/linus/c836a4126768cd76af9ee33b3c11f57695d5fda6)
- [drm/radeon/kms: add HDMI code for pre-DCE3 R6xx GPUs](http://git.kernel.org/linus/5715f67cecee3617c7a6ff84ee44da46d525559e)
- [drm/radeon/kms: add hw_i2c module option](http://git.kernel.org/linus/e2b0a8e1e697dbcd62574a32f4f96151d21bdd36)
- [drm/radeon/kms: add LVDS pll quirk for Dell Studio 15](http://git.kernel.org/linus/8e0d84a63af351f5367103b83478f2cd4d9a3727)
- [drm/radeon/kms: add support for hardcoded edids in rom (v2)](http://git.kernel.org/linus/3c537889e17232e9073f75ae8710ea0f008c5a29)
- [drm/radeon/kms: add support for hw i2c on r1xx-r5xx](http://git.kernel.org/linus/40bacf1631a3e8654b1128aa9b72e73ca801c9e4)
- [drm/radeon/kms: add workaround for rn50/rv100 servers](http://git.kernel.org/linus/2739d49cd7f1f44876cad614b072da698967b370)
- [drm/radeon/kms: bump the KMS version number for square tiling support.](http://git.kernel.org/linus/0de1a57bedce0899c98da4c0910d4f38c9b7c8f4)
- [drm/radeon/kms: disable MSI on IGP chips](http://git.kernel.org/linus/c414a117c6094c3f86b533f97beaf45ef9075f03)
- [drm/radeon/kms: display watermark updates (v2)](http://git.kernel.org/linus/f46c01208da1881591e3f55ca77d37f54469f8e4)
- [drm/radeon/kms: dynclks fixes](http://git.kernel.org/linus/6d7f2d8da106ecf794a5a3e98c4239f348119e3c)
- [drm/radeon/kms: enable ACPI powermanagement mode on radeon gpus.](http://git.kernel.org/linus/d668046c13024d74af7d04a124ba55f406380fe7)
- [drm/radeon/kms/evergreen: get DP working](http://git.kernel.org/linus/fb668c2fed628179c7aa409a0de39a2b96bed18c)
- [drm/radeon/kms: expose thermal/fan i2c buses](http://git.kernel.org/linus/29fb52ca78b4e265ec6c626b0c7b2927953949cf)
- [drm/radeon/kms: print GPU family and device id when loading](http://git.kernel.org/linus/1b5331d9c6ae1f68db6359d227531ec42bc40d47)
- [drm/radeon/kms/r600: reduce gpu cache flushing](http://git.kernel.org/linus/44224c3f455886190b101dbb00befbaff5e98466)
- [drm/radeon/kms: update new pll algo](http://git.kernel.org/linus/383be5d1789d9a7a2e77dca1cb0aca89507d069e)
- [drm/radeon/kms: use power states for dynamic reclocking](http://git.kernel.org/linus/530079a8f3f35828a80ba4981c1be902982363e7)
- [fbdev: remove obsolete CONFIG_FB_SOFT_CURSOR](http://git.kernel.org/linus/91d4e0a4c889e3e8078c26542b8f5a322b87adf4)
- [fbdev: rename imacfb.txt to efifb.txt and change imacfb to efifb.](http://git.kernel.org/linus/a8557dc71949e80c298ec298b902ac6ebbc5d9dd)
- [NUC900 LCD Controller Driver](http://git.kernel.org/linus/8661970875d7d27e4de233d357327fffdb4a5e3d)
- [vgaarb: Add user selectability of the number of GPUS in a system](http://git.kernel.org/linus/36028f3383872eefb558a4aae4c12ec2b5fa640f)
- [vga_switcheroo: disable default y by new rules.](http://git.kernel.org/linus/d424b925f7092b9d95e0a8556872349abe79d9b6)
- [viafb: support color depth 15 and 30](http://git.kernel.org/linus/e17cea3cece6d3ec47a5b358821505943abe6541)

*For other articles on 2.6.34 and links to the rest of the "Coming in 2.6.34" series, see [The H's Kernel Log - 2.6.34 Tracking page](../site/open/features/Linux-Kernel-2-6-34-tracking-962586.html "Linux Kernel 2.6.34 tracking – 24 March 2010"). New editions of Kernel Logs are also mentioned on [Identi.ca](http://identi.ca/kernellog2) and [Twitter](http://twitter.com/kernellog2) via "@kernellog2". The Kernel Log author also posts updates about various topics on [Identi.ca](http://identi.ca/kernellogauthor) and [Twitter](http://twitter.com/kernellogauthor) via "@kernellogauthor".*

([crve](mailto:crve@h-online.com))
