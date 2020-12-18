[![](https://img.shields.io/badge/built_with-neopo-informational)](https://neopo.xyz)

# increment-build

A demo project using Python and neopo to create a version string based on the latest commit and pass it to Particle firmware.


## USAGE


Creates the version string and passes it to the compiler using `EXTRA_CFLAGS`. The firmware is then built or flashed using neopo.
```
$ ./build.py build
$ ./build.py flash
```

Automated testing. Runs `build.py flash` and attaches the serial monitor to confirm that the device prints the version string:
```
$ ./test.sh
```

## EXAMPLE OUTPUT

```
$ ./test.sh 

:::: PUTTING DEVICE INTO DFU MODE

Done.

:::: FLASHING APPLICATION

   text    data     bss     dec     hex filename
   3548     108    1216    4872    1308 /home/nrobinson/code/increment-build/target/photon/increment-build.elf
dfu-suffix (dfu-util) 0.9

Copyright 2011-2012 Stefan Schmidt, 2013-2014 Tormod Volden
This program is Free Software and has ABSOLUTELY NO WARRANTY
Please report bugs to http://sourceforge.net/p/dfu-util/tickets/

Suffix successfully added to file
Serial device PARTICLE_SERIAL_DEV : not available
Flashing using dfu:
dfu-util 0.9

Copyright 2005-2009 Weston Schmidt, Harald Welte and OpenMoko Inc.
Copyright 2010-2016 Tormod Volden and Stefan Schmidt
This program is Free Software and has ABSOLUTELY NO WARRANTY
Please report bugs to http://sourceforge.net/p/dfu-util/tickets/

Opening DFU capable USB device...
ID 2b04:d006
Run-time device DFU version 011a
Claiming USB DFU Interface...
Setting Alternate Setting #0 ...
Determining device status: state = dfuIDLE, status = 0
dfuIDLE, continuing
DFU mode device DFU version 011a
Device returned transfer size 4096
DfuSe interface name: "Internal Flash   "
Downloading to address = 0x080a0000, size = 3656
Download        [=========================] 100%         3656 bytes
Download done.
File downloaded successfully

*** FLASHED SUCCESSFULLY ***

Opening serial monitor for com port: "/dev/ttyACM0"
Serial monitor opened successfully:
Build version: 3.da4c286
```
