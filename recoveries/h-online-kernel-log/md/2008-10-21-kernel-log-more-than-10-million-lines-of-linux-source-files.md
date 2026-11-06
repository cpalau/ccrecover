---
title: "Kernel Log: More than 10 million lines of Linux source files"
date: 2008-10-21
author: "Dj Walker-Morgan"
source: http://www.h-online.com/open/news/item/Kernel-Log-More-than-10-million-lines-of-Linux-source-files-737731.html
pages: 1
---

# Kernel Log: More than 10 million lines of Linux source files

**Dj Walker-Morgan**

![](../site/imgs/43/3/6/4/5/0/2/a345f5e7c547062f.jpg) After the release of [Linux 2.6.27](../site/open/features/Kernel-Log-Linux-2-6-27-Released-746496.html "Kernel Log: Linux 2.6.27 Released – 10 October 2008, 08:38"), kernel developers are currently busily integrating patches for the next kernel version into the main development branch of Linux. This usually involves discarding some old code and adding new code though on balance, there are usually more new lines than old ones, making the kernel [grow continually](http://www.heise-online.co.uk/open/Kernel-Log-Linux-2-6-27-Released--/features/111671/6).

In this process, the kernel developers have now passed the 10 million line mark if blank lines, comments and text files are included in a current Git checkout of the Linux source code (`find . -type f -not -regex '\./\.git.*' | xargs cat | wc -l`). It is also worth noting that the lines of text in source code files as that number has recently passed 9 million (`find . -name *.[hcS] -not -regex '\./\.git.*' | xargs cat | wc -l`).

Programs like [SLOCCount](http://www.dwheeler.com/sloccount/) can be used to inspect the Linux kernel's source code in more detail. According to this tool, the source code line count is not 9 million but exactly 6,399,191 (Source Lines of Code/SLOC), as the program doesn't count blank lines, comments and several other types of input. More than half of the lines are part of hardware drivers; the second largest chunk is the arch/ directory which contains the source code of the various architectures supported by Linux.

SLOC   Directory   SLOC-by-Language (Sorted)\
3301081 drivers     ansic=3296641,yacc=1680,asm=1136,perl=829,lex=778,\
               sh=17\
1258638 arch        ansic=1047549,asm=209655,sh=617,yacc=307,lex=300,\
               awk=96,python=45,pascal=41,perl=28\
544871  fs      ansic=544871\
376716  net     ansic=376716\
356180  sound       ansic=355997,asm=183\
320078  include     ansic=318367,cpp=1511,asm=125,pascal=75\
74503   kernel      ansic=74198,perl=305\
36312   mm      ansic=36312\
32729   crypto      ansic=32729\
25303   security    ansic=25303\
24111   scripts     ansic=14424,perl=4653,cpp=1791,sh=1155,yacc=967,\
               lex=742,python=379\
17065   lib     ansic=17065\
10723   block       ansic=10723\
7616    Documentation   ansic=5615,sh=926,perl=857,lisp=218\
5227    ipc     ansic=5227\
2622    virt        ansic=2622\
2287    init        ansic=2287\
1803    firmware    asm=1598,ansic=205\
833 samples     ansic=833\
493 usr     ansic=491,asm=2\
0   top_dir     (none)

According to SLOCCount, 96.4 per cent of the code is written in C and 3.3 percent in Assembler. The other programming languages are only used marginally: Perl, for example, was used for some help scripts during kernel development and only accounts for a tiny 0.1 percent. In the Assembler-heavy architecture directory, SLOCCount also claims to have found 116 lines of Pascal code – but that could well be a misinterpretation by SLOCCount.

Totals grouped by language (dominant language first):\
ansic:      6168175 (96.39%)\
asm:         212699 (3.32%)\
perl:          6672 (0.10%)\
cpp:           3302 (0.05%)\
yacc:          2954 (0.05%)\
sh:        2715 (0.04%)\
lex:           1820 (0.03%)\
python:     424 (0.01%)\
lisp:       218 (0.00%)\
pascal:     116 (0.00%)\
awk:         96 (0.00%)

SLOCCount also tries to give a rough calculation of the source code's value; according to the program's estimates, it would take more than 200 developers about nine and a half years and cost \$267 million to rewrite the code from scratch. Given that the program has not been updated for four years, the accuracy of this calculation is arguable; especially the cost per developer would now surely need to be increased.

Total Physical Source Lines of Code (SLOC)       = 6,399,191\
Development Effort Estimate, Person-Years (Person-Months) = 1,983.63\
(23,803.60)\
(Basic COCOMO model, Person-Months = 2.4 \* (KSLOC\*\*1.05))\
Schedule Estimate, Years (Months)             = 9.59 (115.10)\
(Basic COCOMO model, Months = 2.5 \* (person-months\*\*0.38))\
Estimated Average Number of Developers (Effort/Schedule)  = 206.81\
Total Estimated Cost to Develop               = \$ 267,961,839\
(average salary = \$56,286/year, overhead = 2.40).\
\
Generated using David A. Wheeler's 'SLOCCount'

There is no end in sight for kernel growth which has been ongoing in the Linux 2.6 series for several years – with every new version, the kernel hackers extend the Linux kernel further to include new functions and drivers, improving the hardware support or making it more flexible, better or faster. A look at [the figures](http://www.heise-online.co.uk/open/Kernel-Log-Linux-2-6-27-Released--/features/111671/6) pertaining to the latest kernel versions also shows that it is not only the number of lines of source code which is continually increasing, but also the number of changes per kernel version.

*Further background and information about developments in the Linux kernel and its environment can also be found in previous issues of the kernel log at heise open:*

- [Kernel Log: Coming in 2.6.28 - Part 2: network infrastructure and network drivers](../site/news/item/Kernel-Log-Coming-in-2-6-28-Part-2-network-infrastructure-and-network-drivers-737711.html "Kernel Log: Coming in 2.6.28 - Part 2: network infrastructure and network drivers – 20 October 2008, 09:39")
- [Kernel Log: Coming in 2.6.28 - Part 1: ATA support and block layer](../site/news/item/Kernel-Log-Coming-in-2-6-28-Part-1-ATA-support-and-block-layer-737699.html "Kernel Log: Coming in 2.6.28 - Part 1: ATA support and block layer – 19 October 2008, 08:02")
- [Kernel Log: new Catalyst drivers, 2.6.27.1 resolves cause of e1000e problem](../site/news/item/Kernel-Log-new-Catalyst-drivers-2-6-27-1-resolves-cause-of-e1000e-problem-737701.html "Kernel Log: new Catalyst drivers, 2.6.27.1 resolves cause of e1000e problem – 18 October 2008, 08:02")
- [Kernel Log: Ext4 completes development phase as interim step to btrfs](../site/news/item/Kernel-Log-Ext4-completes-development-phase-as-interim-step-to-btrfs-737697.html "Kernel Log: Ext4 completes development phase as interim step to btrfs – 17 October 2008, 09:52")
- [Kernel Log: Linux 2.6.27 Released](../site/open/features/Kernel-Log-Linux-2-6-27-Released-746496.html "Kernel Log: Linux 2.6.27 Released – 10 October 2008, 08:38")
- [Kernel Log: problem with e1000e bypassed, Morton praises Btrfs](../site/news/item/Kernel-Log-problem-with-e1000e-bypassed-Morton-praises-Btrfs-737561.html "Kernel Log: problem with e1000e bypassed, Morton praises Btrfs – 07 October 2008, 08:47")

*Older Kernel logs can be found in [the archives](http://www.heise-online.co.uk/open/news/archive/) or by using [the search function](http://www.heise-online.co.uk/search/?rm=search;perpage=5999;filter_t1=1;q=kernel-log) at [heise open](http://www.heise-online.co.uk/open/).* ([thl](mailto:mailto%3Athl@ct.heise.de)/c't)

([djwm](mailto:djwm@h-online.com "Dj Walker-Morgan"))
