#!/usr/bin/env python

import sys
import re
from datetime import datetime

class MkSlackbuildScript:

    def __init__(self):
	print self
        pass

    def mk_slackbuild_script(self,
		    appname,
		    tarfile,
		    ):

        tarfile = tarfile.replace('.tar.gz', '')
        version = re.sub( r'.*-', '', tarfile)
        print "appname: %s" % appname
        print "version: %s" % version

        year = str(datetime.today().year)
        print "year: %s" % year

        you="Don Perry"
        where_you_live="US"

        template_file = open('python-template.SlackBuild', 'r')
        template_file_lines=template_file.readlines()

        start_delete=False
        for item, line in enumerate(template_file_lines):
            if line.find('<appname>') > 1:
        	line = line.replace('<appname>', appname)
            if line.find('appname') > 1:
        	line = line.replace('appname', appname)
            if line.find('<year>') > 1:
        	line = line.replace('<year>', year)
            if line.find('<you>') > 1:
        	line = line.replace('<you>', you)
            if line.find('<where you live>') > 1:
        	line = line.replace('<where you live>', where_you_live)
            if line.find('# |-----') >= 0:
                start_delete = ~start_delete
                line  = ''
            if line.find('VERSION:') >= 0:
        	    line = line.replace('VERSION:-1.4.1}', 'VERSION:-' + version + '}')
            if start_delete:
                template_file_lines[item]  = ''
            else:
                template_file_lines[item]  = line
        file = open(appname+'.SlackBuild', 'w')
        file.writelines(["%s" % line for line in template_file_lines])

if __name__ == "__main__":
    appname = sys.argv[1]
    tarfile = sys.argv[2]
    mss = MkSlackbuildScript()
    mss.mk_slackbuild_script(appname, tarfile)

