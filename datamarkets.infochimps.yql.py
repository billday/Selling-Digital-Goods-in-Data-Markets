# This Python program accesses the Infochimps Twitter Influence Metrics for
# the specified Twitter screen name via a Yahoo! Query Language call.
#
# Copyright (c) 2011, Bill Day; for more information see http://billday.com

# Import the modules supporting Yahoo! Query Language operations.  For
# more information on the Python-YQL module, please refer to:
# http://python-yql.org/
#
import yql

# Setup public access to YQL (no authentication required).
#
y = yql.Public()

# Specify Twitter screen name for which we wish to retrieve influence metrics
# and the Infochimps apikey to use.
#
screenname = "billday"
apikey = "api_test-W1cipwpcdu9Cbd9pmm8D4Cjc469"

# Fetch the influence metrics.  Results are returned as a
# yql.YQLObj containing rows where each row contains a 
# dictionary whose value contains key:value pairs.
#
# For more information see:
# http://python-yql.org/code.html
#
influencequery = "select * from infochimps.influence where screen_name='" + screenname + "' and apikey='" + apikey + "';"

print "-----"
print "Retrieving influence metrics for Twitter screen name: ", screenname
print "-----"

# For some reason, YQL is currently returning:
# "No definition found for Table infochimps.influence"
# when we execute the YQL call below even though the exact 
# same YQL statement executes correctly in the YQL console
# via this call:
# http://yhoo.it/gYZ17r
#
# I am investigating and will update this example program as needed.
# 
metrics = y.execute(influencequery)

# Now that we have the data in our Python program, we can add code to
# do whatever else we want with the metrics.  Enjoy!
