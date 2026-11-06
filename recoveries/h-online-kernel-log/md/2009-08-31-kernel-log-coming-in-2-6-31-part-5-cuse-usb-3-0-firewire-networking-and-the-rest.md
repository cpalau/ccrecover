---
title: "Kernel Log: Coming in 2.6.31 - Part 5: CUSE, USB 3.0, FireWire networking and the rest"
date: 2009-08-31
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-Coming-in-2-6-31-Part-5-CUSE-USB-3-0-FireWire-networking-and-the-rest-743173.html
pages: 1
---

# Kernel Log: Coming in 2.6.31 - Part 5: CUSE, USB 3.0, FireWire networking and the rest

**Dj Walker-Morgan**

![Kernel Log Penguin](../site/imgs/43/3/6/9/6/0/2/93e8ea3d0acdf147.jpg)

#### by Thorsten Leemhuis

**Linux 2.6.31 will support USB 3.0, although the corresponding hardware is not yet available. Distributions are to use the new FireWire stack that now offers LAN support. CUSE emulates the Open Sound System via a userspace program. Another new addition is a driver for Acer's Aspire One netbook.**

Last Friday, Linus Torvalds released the eigth pre-release version of Linux 2.6.31. As the lead developer stressed in the [release announcement](http://thread.gmane.org/gmane.linux.kernel/883177), it will be the last pre-release version. He is on holiday diving for the next week and hopes to present the 2.6.31 release on the [Labor Day](http://en.wikipedia.org/wiki/Labor_day) US Holiday, which falls on September 7th this year.

Because, until then, only bug fixes will be fed into the main development branch, we are presenting the fifth and final part of the Kernel Log mini series now, concluding the detailed overview of the new features in the forthcoming kernel version. This edition will discuss all the subsystems that were left unmentioned in the previous parts – mainly the drivers and driver-related infrastructures like the ACPI and PCI subsystems. In the "Latecomers" section of this article we also mention a few stragglers from the areas already covered in previous editions.

For other articles on 2.6.31 and links to the other four parts of the "Coming in 2.6.31" series, see The H's [Kernel Log - 2.6.31 Tracking](../site/open/features/Kernel-Log-2-6-31-Tracking-746446.html "Kernel Log - 2.6.31 Tracking – 02 July 2009, 11:21") page.

### Fast transmissions

[As expected](../site/news/item/First-Linux-USB-3-0-drivers-emerge-741965.html "First Linux USB 3.0 drivers emerge – 10 June 2009, 10:06"), [changes to the USB subsystem](http://thread.gmane.org/gmane.linux.usb.general/18805) include the code to support USB 3.0 controllers with their Extensible Host Controller Interface (xHCI) (for example [1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=74c6874199af98e602bb7c5fb1beb9cffda98729), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3ffbba9511b4148cbe1f6b6238686adaeaca8feb), [3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d0e96f5a71a032ced0c35f521c1cbd67e816922a), [4](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0f2a79300a1471cf92ab43af165ea13555c8b0a5), [5](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c6515272b858742962c1de0f3bf497a048b9abd7)). Although various vendors have already released details about USB 3.0 hardware, so far, no actual products have become available. The USB 3.0 support in Linux is, therefore, not particularly relevant for now – but this will probably change in the long run; after all, the previous two USB interface generations have been resoundingly successful.

An overview of the changes to the FireWire code is available in the two main git-pull requests submitted by FireWire maintainer Stefan Richter ([1](http://thread.gmane.org/gmane.linux.kernel/852983), [2](http://thread.gmane.org/gmane.linux.kernel/852983/focus%3D13296)). Among other things, the maintainer highlights the [added support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c76acec6d55107b652a37c90b36c00bc8b04dabb) for "IPv4 over IEEE 1394" (networks via FireWire) in the more recent of the Linux kernel's two FireWire stacks. He also points out that the more recent "firewire" stack [is no longer classified as experimental](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0c53decdd0a9f9c459ccabe0b5f79660bde5375b), and that the distributions should, therefore, give it preference in the future. According to the maintainer, the new stack offers better performance, better compatibility, more features and improved security. However, he also points out that the old "ieee1394" stack is still the best choice for audio hardware and for the FireWire DVB devices supported by the firedtv driver.

### Drawing devices

With 2.6.31, the FUSE (Filesystem in Userspace)-based CUSE (Character device in Userspace) feature will be integrated into Linux. It allows userspace programs to emulate virtual devices that are accessible to other programs via the usual character-oriented device files in the same way as "proper" character devices implemented via a kernel driver.

This enables programmers to develop, for example, a userspace program that emulates the obsolete OSS (Open Sound System); it implements the devices expected by OSS programs via CUSE and then uses these devices to accept the data, process it and output it using the current ALSA sound system. The developer of CUSE, a Novell employee, has released such an [OSS proxy](http://userweb.kernel.org/~tj/ossp/) for testing. Find further background information about CUSE and its potential uses in an [article released on LWN.net](http://lwn.net/Articles/308445/) some time ago.

### Specials corner

The staging area with its drivers that don't live up to the kernel hackers' quality standards has reached quite a considerable size. However, in the current development cycle it has actually shrunk a bit, as Greg Kroah-Hartman pointed out in his [git-pull request](http://thread.gmane.org/gmane.linux.kernel/854461) for the changes to the staging area ("*We are removing more crap than we are adding, looks like progress to me! :)*"). This is mainly due to the reorganisation of several drivers for Ralink Wi-Fi chip-sets, as [already discussed](../site/news/item/Kernel-Log-Coming-in-2-6-31-Part-1-New-Wi-Fi-drivers-and-other-network-related-changes-742309.html "Kernel Log - Coming in 2.6.31 - Part 1: New Wi-Fi drivers and other network-related changes – 02 July 2009, 12:44") in the Kernel Log.

In addition to the rtl8192su and vt6655 Wi-Fi drivers mentioned there, the staging area now contains the new [octeon-ethernet](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=80ff0fd3ab6451407a20c19b80c1643c4a6d6434) network driver for SoCs (Systems on a Chip) from Cavium's Octeon family. Further kernel additions at the tail end of the current development cycle are the cpc-usb CPC-CAN-USB driver and the rudimentary udlfb framebuffer driver ([1](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=88e58b1a42f8c1e9ac8ecda23374cc241045d309), [2](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9a82e6df79f13a3489c50813c1edb4331a9400d3)) for [DisplayLink devices](../site/news/item/DisplayLink-plugs-into-Linux-741607.html "DisplayLink plugs into Linux – 18 May 2009, 11:16").

The developers [removed](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ba49d59ac4b0748c8d7be9d7a9f637c50592e977) serqt_usb because a kernel hacker has developed a completely new alternative driver for the same hardware – it is not the first and probably won't be the last time the kernel developers have decided to replace a staging driver with a completely new driver instead of trying to improve a ["dodgy" one](../site/news/item/Kernel-Log-What-s-coming-in-2-6-28-Part-3-Dodgy-drivers-737747.html "Kernel Log: What's coming in 2.6.28 - Part 3: Dodgy drivers – 22 October 2008, 09:29").

### In brief

The changes described above are only the most significant of those recently made by the kernel hackers. Here is a short overview of further changes:

**Notebooks:**

- The kernel hackers have [integrated](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e86435eb91b2bff114c5a02e46e16ce21b647ebe) the [acerhdf](http://piie.net/files/acerhdf_README.txt) driver, which provides temperature read-outs and fan control options for Acer's Aspire One netbook.

<!-- -->

- The asus_acpi driver has been [marked as "deprecated"](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6122af3743a48dddae19810626dd7c9c8e6c1df8) – developers recommend using asus-laptop instead.

**USB:**

- Several changes have been made to the USB code to [upgrade the way it supports](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=abb306416a7ec2386678de0da6b632a6cb068af0) current power saving techniques.

<!-- -->

- The kernel hackers have added a [generic USB audio gadget driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c6994e6f067cf0fc4c6cca3d164018b1150916f8) and a [USB gadget driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5b7d70c6dbf2db786395cbd21750a1a4ce222f84) for the HS/OtG block found in recent SoCs by Samsung.

<!-- -->

- Another new Linux addition is [a driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5be19a9daa2df2507adf5b4676a7db8d131cf56e) for the USB-OTG part in Intel's Langwell I/O component. This component is part of the Moorestown platform, which has been fully optimised for Linux use; while the driver for the corresponding transceiver was [added briefly](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=453f77558810ffa669ed5a510a7173ec49def396), it was later [removed for the time being](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1a74826fa1cd6c2e382f927403b4440675f0f55a).

**Miscellaneous:**

- As Jesse Barnes writes in his [git-pull request](http://thread.gmane.org/gmane.linux.kernel.pci/4822)Changes to the PCI subsystem have been less substantial than in Linux 2.6.30. One of the reported major additions is [the improved support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c465def6bfe834b62623caa9b98f2d4f4739875a) of PCI Express Root Port Advanced Error Reporting (AER). The PCI subsystem is now compatible with Address Translation Service (ATS) 1.0. The IOMMU code, which now supports [IOMMU pass through](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4ed0d3e6c64cfd9ba4ceb2099b10d1cf8ece4320), contains a more flexible workaround for graphics card drivers which [gets rid of](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c7ab48d2acaf959e4d59c3f55d12fdb7ca9afd7c) the CONFIG_DMAR_GFX_WA configuration option.

<!-- -->

- The kernel hackers working with Rafael J. Wysocki in the power management area primarily did some [clearing up](http://thread.gmane.org/gmane.linux.power-management.general/14914).

<!-- -->

- [Changes in the crypto area](http://thread.gmane.org/gmane.linux.kernel.cryptoapi/2397/focus%3D3135) include [one addition](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d1c8b0a7692e81b46550bcc493465ed10510cd33) which now allows the padlock driver to work on x86-64 systems.

<!-- -->

- A new addition to Linux 2.6.31 is the [LinuxPPS](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=eae9d2ba0cfc27a2ad9765f23efb98fb80d80234) (Linux Pulse Per Second) device, which provides one signal per second and is accessible to userspace applications like NTPD; further details about its potential uses and additional background information can be found in the [LinuxPPS wiki](http://wiki.enneenne.com/index.php/LinuxPPS_support) and in the [kernel documentation](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob;f=Documentation/pps/pps.txt;hb=HEAD).

### Minor gems

Many additional minor, but by no means insignificant, changes can be found in the list below. Like many of the references in the text above, the links lead to the relevant commits in the [web front end](http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=summary) of the main Linux development branch, where the commit comments and the patches themselves provide extensive further information on the respective changes.

**FireWire and USB**

*FireWire:*

- [firewire: core: add sysfs attribute for easier udev rules](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0210b66dd88a2a1e451901b00378a2068b6ccb35)
- [firewire: net: add Kconfig item, rename driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b9530fd6c3f057bda258c8e2631ad1a25959f4a2)
- [firewire: sbp2: add support for disks \>2 TB (and 16 bytes long CDBs)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=af2719415a5ceae06f2a6d33e78b555e64697fc8)
- [ieee1394: sbp2: add support for disks \>2 TB (and 16 bytes long CDBs)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ebbb16bffa646f853899ef3fdc0ac7abab888703)

*USB:*

- [musb: add high bandwidth ISO support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a483d7068f661213e9586d4d132fc0e0287118b4)
- [USB: Add SuperSpeed to the list of USB device speeds.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6b403b020c1f42180b14d28d832da61167cff822)
- [USB: add the usbfs devices file to debugfs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=97d7b7a41bd462abceee7dbb2b3afacfd52438ed)
- [USB: Add USB 3.0 roothub support to USB core.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d2e9b4d6734db2327af3149d8ca7555307e10828)
- [USB: add usb debugfs directory](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=00048b8bde5a6cbd9c3a76f272cc9ddb55705e37)
- [USB: audio: add USB audio class definitions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c47d7b09891abb4f8b222317c89c7469bed8db3a)
- [USB: CP210x Add new device IDs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8bf16ba7c8ea9d067914e270764c14020a26232f)
- [USB: Don't reset USB 3.0 devices on port change detection.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e7b7717247f61e2cf18ec47f91999065c59d1607)
- [USB: ftdi_sio: Add support for GN Otometrics Aurical USB Audiometer](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fca4404c55ab44c7413769f1d9c66451103711a5)
- [USB: FTDI-SIO new device ids](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d46130ab3ed3716db22bdd9881a60ec7e4365b63)
- [USB: gadget: Add i.MX3x support to the fsl_usb2_udc driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=54e4026b64a970303349b952866641a7804ef594)
- [USB: gadget: audio: provide correct device id](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=05cbc2d58224d01925bfb93a0c3f0ab1f11b1eea)
- [USB: new flag for resume-from-hibernation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6ec4beb5c701f728548b587082c83ef62eb36035)
- [USB: option: add Novatel Ovation MC760](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=71f9f6cc9eef47fddc05f34b3d32677ab2e0f1fa)
- [USB: option: Add USB ID for Novatel MC727/U727/USB727 refresh](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f1469fc3ef1d5a8a67146c1c72021f012a59dea6)
- [USB: option: add ZTE device ids and remove ONDA ids](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c420befde6b2747ebc2b8f015687a5dbd6e167ca)
- [USB: option.c: add A-Link 3GU device id](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c3325eb16d36a49f9a5ae09241c418cfd1d3f4f5)
- [USB: option.c: add Qualcomm/Option iCON 210 modem](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=83dfdaa362fd9f1ed8bfa0bba50fff08c063380b)
- [USB: option.c: add Toshiba 3G HSDPA SM-Bus Minicard device id](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=334f9b0f23c9bb90589213279c9cfe19ebe4c0c6)
- [USB: option.c to support Qisda H21/H20 usb modem](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e3a3174519bae99fe3a3d3b9dfda68d820527b44)
- [USB: pl2303: New vendor and product id for the prolific driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8540d66615c39010168ab97eaafb476ec2851298)
- [USB serial: Add ID for Turtelizer, an FT2232L-based JTAG/RS-232 adapter.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=145114125cf07afc91e5b132ec41c353284cdb2a)
- [USB: Serial: Add support for Arkham Technology adapters](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0601e116e30caf35520522cb621d05866663cab2)
- [USB: serial: option: Add ZTE AC8710 usb modem device.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=183791588efd416fc35a71819683b32dee92615b)

**Input Devices**

- [HID: add new multitouch and digitizer contants](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=89f536ccfa8b370ff4d054f4061858ca9322c25a)
- [HID: autocentering support for Logitech Force 3D Pro](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f0bca459829fd33d659c8cd0369ac86a3924a9bc)
- [HID: autocentering support for Logitech G25 Racing Wheel](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=92e0d896ce3087112602449efd87c6d7f4eae8d0)
- [HID: force feedback support for SmartJoy PLUS PS2/USB adapter](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fac733f029251a393c42a8313432f2d9fe43bb83)
- [HID: Multitouch support for the N-Trig touchscreen](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=57fd637ad9ac6b13c1c47b9a0ced4ee99bb26e76)
- [HID: Wacom Graphire Bluetooth driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ca2dcd40f54c8928b3994712a6cadd2078a087fa)
- [Input: add dm355evm_keys driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=eb990b5533cfbddfac6efe783a349525907d1c26)
- [Input: add driver for EETI touchpanels](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=10494dce0b43ed3212abde64bf759705ee3c56ef)
- [Input: add driver for Synaptics I2C touchpad](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=eef3e4cab72eaf5345e3c73b2975c194a714f6cd)
- [Input: add matrix keypad driver for Cirrus EP93xx](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e06003af56c386018f0c209608ac6c6662228cc0)
- [Input: add support for touchscreen on W90P910 ARM platform](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7e3f73754e489e8c7742eaba15b608757b5bbb28)
- [Input: add twl4030-pwrbutton driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=68d8bf0436001980461483f2d753206447f27685)
- [Input: add wm97xx accelerated driver for Atmel microprocessors](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=864fe73c312ca8e177da01207ce86fb1b80b3e54)
- [Input: ALPS - Dell Latitude D630/D800 have DualPoint](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=af27a69aaba2feaeb0b9eebdde2f0b71350c4789)
- [Input: ALPS - handle touchpoints buttons correctly](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d7ed5d883c09c5474f842dcb148515dfaef2a567)
- [Input: appletouch - improve finger detection](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=05e882f890038c702a4f15d385135d03cf74ad48)
- [Input: atkbd - add forced release keys quirk for FSC Amilo Pi 3525](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f0a14de2f82dd6aa13e04816da2091c7ed0f77cf)
- [Input: atkbd - add force relese key quirk for Soltech TA12](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=032e46cbf5fb1d768d7dec5631c224e22b4be46f)
- [Input: i8042 - add Asus G1S to noloop exception list](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=685aaca751271b2c5191901931a19ccaceeae1ce)
- [Input: i8042 - more reset quirks for MSI Wind-clone netbooks](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9230ccb1071d2d7e4ecb6314e67203b9f7f08140)
- [Input: iforce - support new revision of ACT LABS Force RS](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=68947b8f9a36f7f7f54ca95e0c6e169bb603e803)
- [Input: introduce lm8323 keypad driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a48b2d4a0091904b4cf57d667adc2faf689750d3)
- [Input: psmouse - ESD workaround fix for OLPC XO touchpad](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=535650fd7008caffad29f001bcda43f56bafea8e)
- [Input: rotary_encoder - add support for REL\_\* axes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bd3ce6556072bdc8ea66dfd5448e184f189bdc7f)
- [Input: wacom - add DTF720a support and fix rotation on Intuos3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c413ec446188ae53276eb60a60311b430448c6b0)
- [Input: wacom - add support for Intuos4 tablets](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6f660f12d703fa23069317f0a64c6b75d08c15c2)
- [Input: wistron_btns - recognize Maxdata Pro 7000 notebooks](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e705cee427e319665969ef7ac664f3612dec8899)
- [Input: wistron_btns - support Prestigio Wifi RF kill button](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=194934785a846e0a7b1b674b7b475a9d0125d2f8)

**Notebook-Drivers**

- [acpi4asus: update MAINTAINER and KConfig links](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=76593d6fb0a51cb0d666f37d91a990e36c068365)
- [asus-laptop: remove EXPERIMENTAL dependency](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=21ab01e2fcbfcc0d1faba2b7336b3c0f7f3c1ac8)
- [dell-wmi: add additional keyboard events](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5cab0098171712a9fd51399b06181c8dfdebe9c9)
- [eeepc-laptop: add rfkill support for the 3G modem in Eee PC 901 Go](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3cd530b5aaffd27b231f9717730f2f6684c00bda)
- [eeepc-laptop: cpufv updates](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b31d0fde89c905673ceed0404d5ae24f2261d7c7)
- [eeepc-laptop: enable camera by default](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cede2cb6ee9b0ddaa3dbc9939418ff177a831600)
- [eeepc-laptop: Register as a pci-hotplug device](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2b121bc262fa03c94e653b2d44356c2f86c1bcdc)
- [eeepc-laptop: rfkill refactoring](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7de39389d8f61aa517ce2a8b4d925acc62696ae5)
- [eeepc-laptop: sync eeepc-laptop with asus_acpi](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b7b700d4a473d56103e87e341ad555e8a7cce06d)
- [hp-wmi: Add support for reporting tablet state](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=871043bc463e7d191e7b5b00436a8852921dd833)
- [thinkpad-acpi: add quirklist engine](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7d95a3d564901e88ed42810f054e579874151999)
- [thinkpad-acpi: disable broken bay and dock subdrivers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=550e7fd8afb7664ae7cedb398c407694e2bf7d3c)
- [thinkpad-acpi: enhance led support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f21179a47ff8d1046a61c1cf5920244997a4a7bb)
- [thinkpad-acpi: forbid the use of HBRV on Lenovo ThinkPads](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d7880f10c5d42ba182a97c1fd41d41d0b8837097)
- [thinkpad-acpi: remove dock and bay subdrivers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1f6fc2de9525e34ee93bd392fa046369a8cfbf1e)
- [thinkpad-acpi: support the second fan on the X61](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d73772474f6ebbacbe820c31c0fa1cffa7160246)

**Edac, HW-Monitoring, I2C and Watchdog**

*Edac:*

- [amd64_edac: add driver header](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cfe40fdb4a46a68e45fa9a5ecbe588e94b89b4f3)
- [amd64_edac: add memory scrubber interface](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2bc65418724a0ddbb20c9eeb9de8285af7748c16)
- [amd64_edac: add DRAM error injection logic using sysfs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=eb919690be994386eac326f8c53c4540602de563)
- [edac: add CPC925 Memory Controller driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2a9036afffb3a174e980f90eb507c5aea6b540f6)

*HW-Monitoring:*

- [hwmon: (abituguru3) DMI probing for AB9, AB9 QuadQT and IX38 QuadGT](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ec05a8d75d0777cd221f61a88437a31e4cfb83d8)
- [hwmon: (f71882fg) Add support for the F71858F](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=09475d32e652fe60901fe8c9cd50f3f6db0c4933)
- [hwmon: (f71882fg) Add temp#\_fault sysfs attr for f8000](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b6858bca8d7bf52e2564cba5a5ed87e1019d3fd9)
- [hwmon: (ibmaem) Automatically load on HC10 blade](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8070408b5446232ba6eb6e0809a329da58a6ae52)
- [hwmon: (max6650) Add support for alarms](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=52b5226f481c09cc499cc28b1e9347d314b340f1)
- [hwmon: (tmp401) Add documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cd4e96c5dd4a72bdc54ea9981e02465708c204d3)
- [hwmon: (tmp401) Add support for TI's TMP401 sensor chip](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ab2b79d5e22d3cdd2b191e479c60e69df528369a)
- [hwmon: (tmp401) Add support for TI's TMP411 sensors chip](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fce0758f5990b34af4ffba589b23f25c700beb2f)
- [hwmon: (w83627ehf) Add W83627DHG-P support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c1e48dce05ff06266cdfd0cba55fc5367cd499a5)
- [lis3: add click function](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8f3128e714ded7cf1e8c786c204a4f253b5d8ff4)
- [lis3: add three new laptop models](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0093716e6dd18dad554bef81cc788a4c50d32a09)

*I2C:*

- [i2c: Add a sysfs interface to instantiate devices](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=99cd8e25875a109455b709b5a41d4891b8d8e58e)
- [i2c: driver for the Synopsys DesignWare I2C controller](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1ab52cf910bbbee92861227e6ed77c56b1dc233c)
- [i2c: Kill client_register and client_unregister methods](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=352da9820e5506e3b8496e6052a2ad9c488efae8)
- [i2c-ocores: Can add I2C devices to the bus](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=dd14be4c274fc484eccace03ae9726e516630331)
- [i2c: ST DDC I2C U300 bus driver v3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=18904c0ecdf2cf22347da2adc4b273e9570333d8)
- [i2c-viapro: Add new PCI device ID for VX855](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a231591f0427cfb91ae247be974a7fa0e6b37389)

*Watchdog:*

- [WATCHDOG: add bcm47xx watchdog driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=90074dce5537e87b27125505bb89a373567a7ede)
- [WATCHDOG: Add pnx833x_wdt](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=33c050c586fec34dae36eb314bfc3a2c44654c05)
- [WATCHDOG: Freescale STMP: watchdog driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=accde1684ff1ea607557fb7224d2dd57775117e1)
- [WATCHDOG: hpwdt: Add NMI priority option](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=44df75353bc8f32e26e049284053a61d4f1047d6)
- [WATCHDOG: hpwdt: Add NMI sourcing](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=47bece87b14b866872b52ff04d469832e4936756)
- [WATCHDOG: twl4030 watchdog driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=80e45b1e9edbca746618724d5b0a31500bdb6f39)
- [WATCHDOG: U300 COH 901 327 watchdog driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=01480701d5cef5b3b0f8406d2eab1eaff82f9d5c)
- [WATCHDOG: w83627hf_wdt.c: add support for the W83627EHF support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cf1eaab2525e8ae1d53eaf923981c96cb31e57c8)

**Staging Area**

- [Staging: add mailing list address for staging tree](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1c6ccf62706688efa035acbd7705d00d46cf698c)
- [Staging: add pata_rdc driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ad41a8a58e15bf4dee13b78bb3b77f4e1f417506)
- [Staging: Add serqt_usb2, a rewrite of serqt_usb for the usb-serial layer](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d75662e164d5175c5e5f9339ff4d6f6980613d96)
- [Staging: rt2870: Add USB ID for Linksys, Planex Communications, Belkin](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4d2da07bc876fc5bc455e0721df388a3db7e4ba5)
- [Staging: comedi: add vmk80xx USB driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3faad67335e16863b2a143a61eedb5ac055c74c6)
- [Staging: Comedi: vmk80xx: Add k8061 support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=985cafccbf9b7f862aa1c5ee566801e18b5161fb)
- [Staging: cpc-usb: add driver to the build](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=936b6230530a3605e99563dfd3a6845dc0343b6e)
- [Staging: cpc-usb: add TODO file](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=562bf4845fbd9240a1964734d769bb5f6973e759)
- [Staging: pata_rdc: add driver to the build system](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=89a2c2085bfddde2d4fe2264a3f040cb054ed145)
- [staging: remove aten2011 driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0bfc240575acb8769d0be78facedabd8e3d2c33a)
- [Staging: rt2870: Add USB ID for Sitecom WL-608](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8dfb00571819ce491ce1760523d50e85bcd2185f)
- [Staging: serqt_usb2 add the driver to the build](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8ba911c793c526c394eeddbe66f675c58a922449)
- [Staging: wlan-ng: Move firmware loading into driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=76e3e7c4095237ceeb962e3bd8bdc0797fb943e1)

**Various Drivers**

- [Add MAX17040 Fuel Gauge driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c6f4a42de60b981dd210de01cd3e575835e3158e)
- [gpio: driver for PrimeCell PL061 GPIO controller](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1e9c28599879040039f610c5b177e61ef65ff100)
- [leds: Add options to have GPIO LEDs start on or keep their state](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ed88bae6918fa990cbfe47316bd0f790121aaf00)
- [leds: alix-leds2 fixed for Award BIOS](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2216c6e83ccbc9d34f541621ff23f510cd8a256f)
- [leds: LED driver for National Semiconductor LP3944 Funlight Chip](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5054d39e327f76df022163a2ebd02e444c5d65f9)
- [LP3971 PMIC regulator driver (updated and combined version)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0cbdf7bce5b98807b946d1a96956f30dcae24a50)
- [Maxim 1586 regulator driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=55f4fa4e33e90c6b25b4c8ed038392a73b654fef)
- [mfd: add PCAP driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=13a09f93d2bf3a20c748e1d6a30160a00fc58169)
- [mfd: add U300 AB3100 core support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=14fa56917d73d823538151b0429d98211fa439c1)
- [msm_serial: serial driver for MSM7K onboard serial peripheral.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=04896a77a97b87e1611dedd61be88264ef4ac96c)
- [regulator: add userspace-consumer driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1d98cccf7f8b944ba4ea56d14bbb7c2eeee59bfe)
- [rtc: add stand-alone driver for RX8025 chip](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3c2b9075cbdb541dbe486bde45925c9610de6f35)
- [tty: Bring the usb tty port structure into more use](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=335f8514f200e63d689113d29cb7253a5c282967)
- [tty: rewrite the ldisc locking](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c65c9bc3efa5589f691276bb9db689119a711222)

**Security and Crypto**

- [crypto: aes-ni - Add support for more modes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2cf4ac8beb9dc50a315a6155b7b70e754d511958)
- [crypto: padlock - Enable on x86_64](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d1c8b0a7692e81b46550bcc493465ed10510cd33)
- [crypto: talitos - Add ablkcipher algorithms](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4de9d0b547b97e40c93a885ac6246c2c5fef05cb)
- [IMA: Minimal IMA policy and boot param for TCB IMA policy](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5789ba3bd0a3cd20df5980ebf03358f2eb44fd67)
- [hwrng: via_rng - Support VIA Nano hardware RNG](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=858576bdc5d65edf1fffd2e65b2165ec1dc68486)
- [hwrng: via_rng - Support VIA Nano hardware RNG on X86_64 builds](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e9736c16da9077728802f42393d18258e6685428)
- [hwrng: via_rng - The VIA Hardware RNG driver is for the CPU, not Chipset](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=608d1cd5d375580a49d01b5ed1f9944f5141ae19)
- [smack: implement logging V3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ecfcc53fef3c357574bb6143dce6631e6d56295c)
- [Security/SELinux: seperate lsm specific mmap_min_addr](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=788084aba2ab7348257597496befcbccabdc98a3)

**ACPI, PCI and Power Management**

*ACPI:*

- [ACPI: delete acpi.power_nocheck from kernel-parameters.txt](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=113b3a2b901573961509e81a28e9546cf9defef0)
- [ACPI: DMI to disable Vista compatibility on some Sony laptops](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=35a7c64fbc77bab4ca8ae477e8ab278ccd679ce2)
- [ACPI processor: force throttling state when BIOS returns incorrect value](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2a908002c7b1b666616103e9df2419b38d7c6f1f)
- [ACPI: video: DMI workaround broken Acer 7720 BIOS enabling display brightness](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=152a4e630f7ffdd7ff64427c4ba488dc0bce76af)
- [PNPACPI: parse Extended Address Space Descriptors](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8cb24c8fd70ea8431744de1ca0ca34ab45fbbdaa)

*PCI:*

- [dma-debug: add dma_debug_driver kernel command line](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1745de5e5639457513fe43440f2800e23c3cbc7d)
- [dma-debug: add documentation for the driver filter](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=016ea6874a6d58df85b54f56997d26df13c307b2)
- [intel-iommu: Make iommu=pt work on i386 too](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3238c0c4d68d9a9022b411a11a4b933fbdb53a14)
- [intel-iommu: Restore DMAR_BROKEN_GFX_WA option for broken graphics drivers](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=62edf5dc4a524e4cb525e6020b955a1ad593d9ba)
- [irqs: add IRQF_SAMPLE_RANDOM to the feature-removal-schedule.txt (deprecated) list](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9d9b8fb0e5ebf4b0398e579f6061d4451fea3242)
- [PCI: add power-state name strings](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=00240c3839d843ccf07abd52806f421f7b87bbdc)
- [PCI: Add support for turning PCIe ECRC on or off](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=43c16408842b0eeb367c23a6fa540ce69f99e347)
- [PCI: disable ASPM on VIA root-port-under-bridge configurations](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8e822df700694ca6850d1e0c122fd7004b2778d8)
- [PCI: expose SMBus on Asus notebook A6L](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4096ed0fc7c6ed83da44ab27ab7d1c7cd6e8e175)
- [PCI: handle Virtual Function ATS enabling](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e277d2fc79d6abb86fafadb58dca0b9c498a9aa7)
- [PCI hotplug: create symlink to hotplug driver module](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c825bc94c8c1908750ab20413eb639c6be029e2d)
- [PCI: More PATA quirks for not entering D3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7a661c6f1082693a7e9627e9ad2d1546a9337fdc)
- [PCI: PCIE AER: Document for PCIE AER software error injection](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bfe5a7401785f864a4f30b4f066bfa045a28b9f6)
- [PCI quirk: HP hides SMBus controller in Compaq nx9500 laptops](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=74c57428971d28863ec1804b1dd453930bbe1306)
- [PCI quirk: unhide 'Overflow' device on i828{6,7}5P/PE chipsets](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=26c56dc0c4fbdf3af12ebc48278f09ef65ddb4dd)
- [PCI: Remove untested Electromechanical Interlock (EMI) support in pciehp.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bd3d99c17039fd05a29587db3f4a180c48da115a)
- [PCI: use ACPI \_CRS data by default](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=9e9f46c44e487af0a82eb61b624553e2f7118f5b)
- [VT-d: add device IOTLB invalidation support](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6ba6c3a4cacfd68bf970e3e04e2ff0d66fa0f695)
- [VT-d: support the device IOTLB](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=93a23a7271dfb811b3adb72779054c3a24433112)

*Power Management:*

- [CPUFREQ: Enable acpi-cpufreq driver for VIA/Centaur CPUs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0de51088e6a82bc8413d3ca9e28bbca2788b5b53)
- [CPUFREQ: Mark e_powersaver driver as EXPERIMENTAL and DANGEROUS](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0fea615e526b4b7eff0363ee02d5753e5f924089)
- [CPUFREQ: ondemand: Uncouple minimal sampling rate from HZ in NO_HZ case](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cef9615a853ebc4972084f7e70b52892557420ac)
- [CPUFREQ: Only set sampling_rate_max deprecated, sampling_rate_min is useful](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=4f4d1ad6ee69027f51f9d137f7e7d3c863cbc53d)
- [CPUFREQ: Powernow-k8: support family 0xf with 2 low p-states](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a2e1b4c31257c07f148a89eb7eea7ca959fd0642)
- [mm, PM/Freezer: Disable OOM killer when tasks are frozen](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7f33d49a2ed546e01f7b1d0607661810f2421859)
- [NOHZ: Properly feed cpufreq ondemand governor](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f2e21c9610991e95621a81407cdbab881226419b)
- [PM core: rename suspend and resume functions](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=d161630297a20802d01c55847bfcba85d2118a9f)
- [PM/Hibernate: Move memory shrinking to snapshot.c (rev. 2)](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=fe419535d82724314bbf1244a0e740e4ea1bd3ae)
- [PM: Separate suspend to RAM functionality from core](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a9d7052363a6e06bb623ed1876c56c7ca5b2c6d8)
- [PM/Suspend: Do not shrink memory before suspend](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=c6f37f12197ac3bd2e5a35f2f0e195ae63d437de)

**Various others infrastructure changes**

- [Add '-fno-delete-null-pointer-checks' to gcc CFLAGS](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a3ca86aea507904148870946d599e07a340b39bf)
- [Alan doesn't want to maintain tty code any more](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=90a09c9cf78344d18e2438c3b87363b949629fa3)
- [console: make blank timeout value a boot option](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f324edc85e5c1137e49e3b36a58cf436ab5b1fb3)
- [cpusets: document adding/removing cpus to cpuset elaborately](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b37f2d4de6dfce4bfd6df311af80e4d61458ee1e)
- [docs: Encourage better changelogs in the development process document](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5d98932ab0acb699dc56d9e252f056b9b2cdab25)
- [Documentation: Add "how to write a good patch summary" to SubmittingPatches](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2ae19acaa50a09c1099956efb895c0aca74ab050)
- [Documentation/Changes: perl is needed to build the kernel](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=082196242e24ff13354a2d376b275e01c08e6799)
- [Document Reported-by in SubmittingPatches](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bbb0a4247aaf1eabbd6d87750eafe99c577920f7)
- [Document the debugfs API](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f89d7eaf6c34828070f407d0e04b73127f176ec5)
- [driver core: fix documentation of request_firmware_nowait](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7fcab099795812a8a08eb3b8c8ddb35c3685045f)
- [driver core: set default SYSFS_DEPRECATED=n](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f6ee649f4b191d316a463ce7e514f9d12fa31c01)
- [driver core: synchronize device shutdown](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=401097ea4b89846d66ac78f7f108d49c2e922d9c)
- [Driver Core: Warn driver authors about adding device attributes](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b22813b373749d0878e7140e9a6eadf182298709)
- [drivers: add support for the TI VLYNQ bus](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=55e331cf7ebe20665253770589cd9eb06048bf25)
- [edac: add DDR3 memory type for MPC85xx EDAC](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b1cfebc9231a69d46d66982a2c856ba41ef6d6b9)
- [firmware: speed up request_firmware(), v3](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6e03a201bbe8137487f340d26aa662110e324b20)
- [futex: add requeue-pi documentation](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b30505c81a9d4adea8b70ecff512b0216929b797)
- [kbuild: add generic --set-str option to scripts/config](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=1f990cf94559e0a7363d56aade1d5dc6c515b60b)
- [kbuild: finally remove the obsolete variable \$TOPDIR](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=112942353992d95099fb5b71c679ff1046fccfcf)
- [kconfig: handle comment entries within choice/endchoice](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=af6c159885537eb6582a61156ccfb73e83c0478d)
- [MAINTAINERS: mention scripts/get_maintainer.pl in the preface](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f70f873b8ffa0bca4aeccd20a3e4641b7645018a)
- [mmc: add the new linux-mmc mailing list to MAINTAINERS](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b2503a9408e44eb0531adc3436c513ea70f91c42)
- [modules: sysctl to block module loading](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3d43321b7015387cfebbe26436d0e9d299162ea1)
- [printk: add KERN_DEFAULT loglevel to print_modules()](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b231125af7811a2f68c455d3bda95ac170ee4fa6)
- [printk: Add KERN_DEFAULT printk log-level](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e28d713704117bca0820c732210df6075b09f13b)
- [RCU: make treercu be default](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=31c9a24ec82926fcae49483e53566d231e705057)
- [rcu: Mark Hierarchical RCU no longer experimental](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=f6faac71d502be1c29c81b2f45657662c3b84470)
- [Remove multiple KERN\_ prefixes from printk formats](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ad361c9884e809340f6daca80d56a9e9c871690a)
- [sched: rt: document the risk of small values in the bandwidth settings](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=60aa605dfce2976e54fa76e805ab0f221372d4d9)
- [sched: Document memory barriers implied by sleep/wake-up primitives](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=50fa610a3b6ba7cf91d7a92229177dfaff2b81a1)
- [signals: implement sys_rt_tgsigqueueinfo](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=62ab4505e3efaf67784f84059e0fb9cedb1728ea)
- [TTY: Maintainer change](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=57d7f282271a83fe4ca4bd15eee79be577210210)

### Latecomers

The previous four parts of the Kernel Log mini series have already given a detailed overview of the many changes in of the Linux kernel. All of the major enhancements have already been mentioned there, as the usual first phase of the development cycle moved into the main development branch. Some small, usually not quite as important changes have slipped into the "minor gems" section after we had reported on the relevant areas. For completeness, we have included these changes in the following list.

**Audio**

- [ALSA: hda: add model for Intel DG45ID/DG45FC boards](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ae709440edb2d36f51f5ea51cfab931f45c03e02)

**Graphics**

- [drm/i915: Add eDP support on IGDNG mobile chip](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=32f9d658aee5be09ebdd28fc730630e61d0b46db)
- [drm/i915: Add support for dual-channel LVDS on 8xx.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0c2e39525b3b53a97a0202c5f35058147e53977e)
- [drm/i915: Allow frame buffers up to 4096x4096 on 915/945 class hardware](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5e4d6fa72619aeea271d2ad704757717b06e291a)
- [drm/i915: enable DisplayPort support on IGDNG](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=5eb08b69f510fadaba77eb9a1bda0f7299c4ebcc)
- [drm/i915: hdmi detection according by reading edid](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2ded9e2747d0a390d281bb5b16ff7f640ec85f78)
- [drm/i915: ignore lvds on AOpen Mini PC MP-915](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=ed8c754b292f02d0550596481527b7bf2b52d024)
- [drm/i915: Set preferred mode for integrated TV according to TV format](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=bcae2ca81c4a085e3e0e8941b7c64f9aeb6fc05c)
- [drm/radeon/kms: Add specific rs690 authorized register table](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=616b8434688aa08bd6f019cc60c8dfe121e9e5ae)

**File Systems**

- [AFS: Documentation updates](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0dc9aa845c20ed1f46c85f229591b811dffc4b3b)
- [ext3: Update Kconfig description of EXT3_DEFAULTS_TO_ORDERED](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=6d41807614151829ae17a3a58bff8572af5e407e)

**Network**

LAN:

- [Add IDs for 3C905B-TX Fast Etherlink XL PCI](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=b4adbb4ddf63091f48668e7ff1b9b0f6f84d4b40)
- [Add mac driver for w90p910](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=a50a97d415d839e6db9df288ff0205528e52c03e)
- [mlx4_core: Add new ConnectX EN PCI ID 0x6764](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=92bd3bbfbe644ea0860cfe84cf175fffa5246423)
- [net: Micrel KS8851 SPI network driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=3ba81f3ece3cfa4ffb06d21ac93b8cad7fbe6a73)
- [New device ID for sc92031 \[1088:2031](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=90cb665937a2aab16d9aa60f22908195c16dcffd)\]
- [pegasus: Add new device ID.](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=7c1d15d736687057f4dc6e51fbf44b6f6e4320cb)
- [USB host CDC Phonet network interface driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=87cf65601e1709e57f7e28f0f7b3eb0a992c1782)

WLAN:

- [b43: Add support for 4318E](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=cff782cd94df7adea84af6aa9516c8088f7ea950)
- [iwlwifi: only show active power level via sysfs](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=872ed1902f511a8947021c562f5728a5bf0640b5)
- [mac80211: disable mesh](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=e2e414d92397c366396d13f627a98a20be92e509)
- [ssb: Add support for 4318E](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=2fbddeb5c409c90be4706ea2beb7f1fc02100c72)
- [zd1211rw: adding SONY IFU-WLM2 (054c:0257) as a zd1211b device](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=8b339d05805fb91cc0b5179af5b4d05d9f8b949c)

**V4L/DVB**

- [V4L/DVB (12340): mtv9v011: Add a missing chip version to the driver](http://git.kernel.org/git/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=296544e15a7126373851abd40acc526b79b91432)

For other articles on 2.6.31 and links to the rest of the "Coming in 2.6.31" series, see The H's [Kernel Log - 2.6.31 Tracking](../site/open/features/Kernel-Log-2-6-31-Tracking-746446.html "Kernel Log - 2.6.31 Tracking – 02 July 2009, 11:21") page. Older Kernel Logs can be found in [the archives](../site/open/news/archive/) or by using [the search function](../site/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [The H Open Source](../site/open/).

([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
