# This Python program accesses the Infochimps Twitter Influence Metrics for
# the specified user_name via a Yahoo! Query Language call.
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

# Specify the user_name for which we wish to retrieve influence metrics
# and the Infochimps apikey to use.
#
user = "billday"
apikey = "api_test-W1cipwpcdu9Cbd9pmm8D4Cjc469"

# Fetch the influence metrics.  Results are returned as a
# yql.YQLObj containing rows where each row contains a 
# dictionary whose value contains key:value pairs.
#
# For more information see:
# http://python-yql.org/code.html
#
influencequery = "select * from infochimps.influence where screen_name='billday' and apikey='api_test-W1cipwpcdu9Cbd9pmm8D4Cjc469'"
metrics = y.execute(influencequery)
print "-----"
print "Retrieved the following influence metrics for Twitter user: ", user
print "-----"

# Print out the metrics
print metrics

#for row in metrics.rows:
#    print row
