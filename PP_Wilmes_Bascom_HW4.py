#! /usr/local/bin/python2
import requests
import json

response = requests.get('https://WEATHERSERVICEANDKEYHERE.com')
data = json.load(response)
print data
print "Contest-type: text/html"
contents = '''
<html>
	<head>
	<title>HW #4 Wilmes Bascom</title>
	<script src="http://code.jquery.com/jquery-2.2.1.js"></script>
	<script>
	$(document).ready(function(){
		print "$('#CO').css('fill','red')"
	'''
print '''
	});

	</script> </head>
<body>
MapOfUnitedState.svg
</body>
</html>
'''
print contents
