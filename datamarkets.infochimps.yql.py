# This Python program accesses the Infochimps Twitter Influence Metrics for
# the specified Twitter screen name via a Yahoo! Query Language call.
#
# Copyright (c) 2011, Bill Day; for more information see http://billday.com

# Import the package Python-YQL which supports Yahoo! Query Language
# operations.  For more information, please refer to:
# http://python-yql.org/
#
import yql

# Setup public access to YQL (no authentication required).
#
y = yql.Public()

# Specify Twitter screen name for which we wish to retrieve
# influence metrics and the Infochimps apikey to use.
#
screenname = "billday"
apikey = "api_test-W1cipwpcdu9Cbd9pmm8D4Cjc469"

# Fetch the influence metrics.  Results are returned as a
# yql.YQLObj containing rows where each row contains a 
# dictionary whose value contains key:value pairs.
#
# Note that we need to include the "use" portion of the
# YQL statement so that the Python YQL package knows it
# needs to reference that data table.  For more see:
# https://bugs.launchpad.net/python-yql/+bug/664360
#
influencequery = "use 'http://www.datatables.org/infochimps/infochimps.influence.xml'; select * from infochimps.influence where screen_name='" + screenname + "' and apikey='" + apikey + "'"
metrics = y.execute(influencequery)

# Print out what we fetched.
#
print "-----"
print "Retrieving influence metrics for Twitter screen name: ", screenname
print "-----"
for row in metrics.rows:
    print row

# Now that we have the data in our Python program, we can add code to
# do whatever else we want with the metrics.  Enjoy!
