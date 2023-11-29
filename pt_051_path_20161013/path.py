#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os.path

for path in ['/c/Users/gregor.redelonghi', 'c:/Users/Gregor.redelonghi/','/one/two/three/', '/', '.','']:
	print('"%s" : "%s"' % (path, os.path.split(path)))

