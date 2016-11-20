#!/usr/bin/env python

import sys
import subprocess

class SlackDesc:

    def __init__(self):
        pass

    def slackdesc(
	    self,
	    output_dir,
	    package_name,
	    version,
	    short_desc,
	    long_desc,
            home_page="http://www.openstack.org",
	):

	# Run slackdesc to crete the slack-desc file
        p=subprocess.Popen(
	    [
	    "slackdesc",
	    package_name,
	    version,
	    short_desc,
	    long_desc,
	    home_page
	    ],
	    stdout=subprocess.PIPE,
	)
	stdout=p.stdout.readlines()

	# Write the slack-desc file
        slack_desc_filename = "%s/slack-desc" % output_dir
        slack_desc_file = open(slack_desc_filename,'w')
	slack_desc_file.writelines(stdout)


if __name__ == "__main__":
    output_dir = sys.argv[1]
    package_name= sys.argv[2]
    version= sys.argv[3]
    short_desc= sys.argv[4]
    long_desc= sys.argv[5]

    sd=SlackDesc()
    sd.slackdesc(
	output_dir,
	package_name,
	version,
	short_desc,
	long_desc,
    )
