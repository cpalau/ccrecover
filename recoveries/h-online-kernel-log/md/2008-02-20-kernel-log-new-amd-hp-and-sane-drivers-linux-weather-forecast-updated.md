---
title: "Kernel log: New AMD, HP and SANE drivers; Linux Weather Forecast updated"
date: 2008-02-20
author: "Jonathan Bennett"
source: http://www.h-online.com/open/news/item/Kernel-log-New-AMD-HP-and-SANE-drivers-Linux-Weather-Forecast-updated-734285.html
pages: 1
---

# Kernel log: New AMD, HP and SANE drivers; Linux Weather Forecast updated

**Jonathan Bennett**

![Kernel Log logo](../site/imgs/43/3/6/1/0/6/0/a345f5e7c547062f.jpg) Following the release of 2.6.25-rc1, the flow of patches for the official Linux kernel has calmed down slightly. Instead, developers have been busy with driver maintenance projects which are independent of the Linux kernel. AMD followed the monthly publishing cycle and has published the Catalyst 8.02 graphics drivers for Windows and [Linux](http://ati.amd.com/support/drivers/linux/linux-radeon.html). The [release notes](https://a248.e.akamai.net/f/674/9206/0/www2.ati.com/drivers/linux/catalyst_82_linux.html) list some of the [corrections for the new Linux drivers](https://a248.e.akamai.net/f/674/9206/0/www2.ati.com/drivers/linux/catalyst_82_linux.html) - many of them correct problems which cause system crashes.

The [HPLIP](http://hplip.sourceforge.net/) open source project maintained by HP has released version 0.8.2 of the HPLIP drivers for HP printers and scanners for [download](http://hplip.sourceforge.net/downloads.html). [New features](http://hplip.sourceforge.net/release_notes.html) include first-time support for the HP P1005, P1006, P1505, P1505n and P2014 LaserJet models as well as the HP Officejet H470.

The SANE open source project ([Scanner Access Now Easy](http://www.sane-project.org/)), which specialises in drivers for scanners from various manufacturers, has [published](http://lists.alioth.debian.org/pipermail/sane-announce/2008/000025.html) [SANE backends](http://www.sane-project.org/source.html) 1.0.19. This is the first version to include the cardscan (Corex Cardscan 800c), epjitsu (Epson-based Fujitsu), epson2 (various Epson models), hp3900 (includes HP ScanJet 3970), hp5590 (includes HP ScanJet 5590), hpljm1005 (includes HP LaserJet M1005) and hs2p (Ricoh IS400 series) drivers, called backends. In addition, many of the older backends have been updated - sane-backends now offers support for [about 760 scanners](http://www.sane-project.org/sane-mfgs.html) (199 "Complete" and 444 "Good"). [Developers](http://lists.alioth.debian.org/pipermail/sane-announce/2008/000025.html) also announced that this latest version will probably be the last in the SANE 1.0 series; the next version is to be upgraded on a larger scale to improve support for modern scanner functionality.

Those who don't explicitly need the improvements offered by the new driver versions should consider carefully whether to manually install the drivers. While compiling the driver packages by AMD, HP and Sane isn't rocket science, the side effects of manual installations are often underestimated. Unless they are kept in check, driver installation routines can, for example, easily overwrite files managed by the Linux distribution's package management - a subsequent security or distribution update may overwrite these files again several days, weeks or months later, resulting in a muddle in which nothing ends up working as it should. Linux distributions also co-ordinate the software they provide and sometimes integrate additional functionality or drivers - undermining this arrangement by manually installing a driver or Linux kernel may cause problems similar to the ones PC old-timers may remember from the days of Windows 3.x.

Many difficulties can be avoided by being patient and installing the drivers with the respective distribution packages - some distributors publish them as a regular update sooner or later; otherwise, seasoned Linux users are advised to choose already compiled or translatable packages from the development branch of the next distribution version. These packages usually integrate well and with little effort into the current versions of the distribution. For proprietary drivers like those by AMD, larger distributions usually offer external RPM or DEB repository packages ("3rd party repositories") which are specifically co-ordinated to work with the respective distributions and integrate smoothly into them - however, it usually takes several days before new driver versions materialise there.

### Kernel log in brief

Stephen Rothwell has [set up](http://thread.gmane.org/gmane.linux.kernel/639831/) a git tree for the [Linux-next](http://www.heise.de/open/news/meldung/103425) kernel series and publishes the [results](http://kisskb.ellerman.id.au/kisskb/branch/9/) of test compilations. Linux kernel and X developer David Airlie has published his thoughts on [redesigning](http://dri.freedesktop.org/wiki/DRMRedesign) the DRM ([Direct Rendering Manager](http://de.wikipedia.org/wiki/Direct_Rendering_Manager)). The [Linux Weather Forecast](http://www.linux-foundation.org/en/Linux_Weather_Forecast) has been updated to include the phenomena which have occurred since Linux 2.6.25-rc1.

([jbe](mailto: "Jonathan Bennett"))
