#!/usr/bin/env python3
import neopo
from subprocess import run, PIPE

# Create version string from commit number and hash
count = run(["git", "rev-list", "--count", "HEAD"], stdout=PIPE).stdout.splitlines()[0].decode('utf-8')
commit = run(["git", "rev-parse", "--short", "HEAD"], stdout=PIPE).stdout.splitlines()[0].decode('utf-8')
VERSION = "%s.%s" % (count, commit)

# Set the RELEASE_STRING flag
neopo.flags('-DRELEASE_STRING="%s"' % VERSION)

# Build or flash firmware
# neopo.build()
neopo.flash()