import neopo
from subprocess import run, PIPE

count = run(["git", "rev-list", "--count", "HEAD"], stdout=PIPE).stdout.splitlines()[0].decode('utf-8')
commit = run(["git", "rev-parse", "--short", "HEAD"], stdout=PIPE).stdout.splitlines()[0].decode('utf-8')
VERSION = "%s.%s" % (count, commit)

neopo.flags('-DRELEASE_STRING="%s"' % VERSION)
neopo.build()