#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools
import shutil


NoStrip = ["/"]
IgnoreAutodep = True

def setup():
    shelltools.system("ar xf synology-drive-client-11078.x86_64.deb")
    shelltools.system("tar xf data.tar.xz")

def install():
    shutil.rmtree("usr/lib/nautilus/extensions-3.0/")
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "opt")
