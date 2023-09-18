#!/usr/bin/env python
import jinja2 as j, os, sys, yaml as y

with open(sys.argv[1]) as f:
    print(j.Template(f.read()).render({} if os.isatty() else y.load(sys.stdin.read())))
