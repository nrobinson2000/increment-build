#!/usr/bin/env python3
import sys
import neopo
from subprocess import run, PIPE

# Create version string from commit number and hash
count = run(["git", "rev-list", "--count", "HEAD"], stdout=PIPE).stdout.splitlines()[0].decode('utf-8')
commit = run(["git", "rev-parse", "--short", "HEAD"], stdout=PIPE).stdout.splitlines()[0].decode('utf-8')
VERSION = "%s.%s" % (count, commit)

# Set the RELEASE_STRING flag
neopo.flags('-DRELEASE_STRING="%s"' % VERSION)

# Build or flash firmware
if len(sys.argv) < 2:
    print("You must specify whether to build or flash!")

if sys.argv[1] == "build":
    neopo.build()
elif sys.argv[1] == "flash":
    neopo.flash()