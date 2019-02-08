import requests
import json
import datetime
import subprocess

# Replace with the correct URL
url = "http://192.168.1.73:1330/getTime"

# Calculate round trip travel time
startTime = datetime.datetime.now()
rsp = requests.get(url)
endTime = datetime.datetime.now()

# Calculate round trip travel time
rtt = endTime - startTime
offset = rtt / 2
print("Start sending request at {0}".format(startTime))
print("Get the response at {0}".format(endTime))
print("Round trip travel time is {0}".format(rtt))
print("Offset is {0}".format(offset))

# For successful API call, response code will be 200 (OK)
if (rsp.ok):
    jData = json.loads(rsp.content)

    print("Server time is {0}".format(jData['time']))
    # parse json timestring into datetime
    result = datetime.datetime.strptime(jData['time'], '%Y-%m-%d %H:%M:%S.%f') + offset
    print("Result is {0}".format(result))
    subprocess.run(["date", "-s", str(result)])
else:
    # If response code is not ok (200), print the resulting http error code with description
    rsp.raise_for_status()
