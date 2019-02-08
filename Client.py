import requests
import json
import datetime
# Replace with the correct URL
url = "http://192.168.1.73:5000/getTime"

# It is a good practice not to hardcode the credentials. So ask the user to enter credentials at runtime
startTime = datetime.datetime.now()
rsp = requests.get(url)
endTime = datetime.datetime.now()
#print (myResponse.status_code)

# For successful API call, response code will be 200 (OK)
if(rsp.ok):
    # Loading the response data into a dict variable
    # json.loads takes in only binary or string variables so using content to fetch binary content
    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
    jData = json.loads(rsp.content)

    print("The response contains {0} properties".format(len(jData)))
    print(jData)
else:
  # If response code is not ok (200), print the resulting http error code with description
    rsp.raise_for_status()