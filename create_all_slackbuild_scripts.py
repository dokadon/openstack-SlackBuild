#!/usr/bin/env python

import sys
import re
import mk_slackbuild_script
import wget

class ReadTarfilesList:

    def __init__(self):
	print self
        pass

    def get_files(self,
		    ):
        tarfiles_list = open('openstack-tarfiles.list', 'r')
        tarfiles=tarfiles_list.readlines()

        for i, tarfile in enumerate(tarfiles):
	    tarfile=tarfile.rstrip()
	    print tarfile
	    wget.download(tarfile, out='/openstack/packages/openstack-SlackBuild')

            tarfile = re.sub( r'^.*tarballs.openstack.org/', '', tarfile.rstrip())
	    s = tarfile.split( '/', 2)
	    print "program: %s           tarfile: %s" % (s[0], s[1])
	    mss = mk_slackbuild_script.MkSlackbuildScript()
	    mss.mk_slackbuild_script(s[0],s[1])


if __name__ == "__main__":
    rtl = ReadTarfilesList()
    rtl.get_files()

