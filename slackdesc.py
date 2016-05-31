#!/usr/bin/env python

import subprocess

class SlackDesc:

    def __init__(self):
        pass

    def slackdesc(
	    self,
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
        slack_desc_file = open('slack-desc','w')
	slack_desc_file.writelines(stdout)


if __name__ == "__main__":
    package_name= sys.argv[1]
    version= sys.argv[2]
    short_desc= sys.argv[3]
    long_desc= sys.argv[4]

    sd=SlackDesc()
    sd.slackdesc(
	package_name,
	version,
	short_desc,
	long_desc,
    )
