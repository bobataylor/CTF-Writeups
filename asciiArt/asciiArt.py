import requests

# The URL the challenge is located at
base_url = "https://ringzer0team.com/challenges/119"

# Each of the numbers that will need to be parsed broken down into how they display in HTML
NUMBERS = {"&nbsp;xx&nbsp;&nbsp;<br />x&nbsp;x&nbsp;&nbsp;<br />&nbsp;&nbsp;x&nbsp;&nbsp;<br />&nbsp;&nbsp;x&nbsp;&nbsp;<br />xxxxx":1, "&nbsp;xxx&nbsp;<br />x&nbsp;&nbsp;&nbsp;x&nbsp;<br />&nbsp;&nbsp;xx&nbsp;<br />&nbsp;x&nbsp;&nbsp;&nbsp;<br />xxxxx":2, "&nbsp;x&nbsp;&nbsp;&nbsp;x<br />x&nbsp;&nbsp;&nbsp;&nbsp;x<br />&nbsp;xxxxx<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br />&nbsp;&nbsp;&nbsp;&nbsp;x":4, "xxxxx<br />x&nbsp;&nbsp;&nbsp;&nbsp;<br />&nbsp;xxxx<br />&nbsp;&nbsp;&nbsp;&nbsp;x<br />xxxxx":5, "&nbsp;xxx&nbsp;<br />x&nbsp;&nbsp;&nbsp;x<br />&nbsp;&nbsp;xx&nbsp;<br />x&nbsp;&nbsp;&nbsp;x<br />&nbsp;xxx&nbsp;":3, "&nbsp;xxx&nbsp;<br />x&nbsp;&nbsp;&nbsp;x<br />x&nbsp;&nbsp;&nbsp;x<br />x&nbsp;&nbsp;&nbsp;x<br />&nbsp;xxx&nbsp;":0}

# Needed for connecting to the challenge
cookie = {"PHPSESSID":"YOUR_ID_HERE"}

# Connect to the challenge and get the webpage
session = requests.session()
response = session.get(base_url, cookies=cookie)

# Find the begnning and ending tags that bookend the numbers to parse
BEGIN_MESSAGE = response.content.find("----- BEGIN MESSAGE -----<br />")
END_MESSAGE   = response.content.find("----- END MESSAGE -----<br />")

# Trim the content to just the data we need
MESSAGE = response.content[BEGIN_MESSAGE+41:END_MESSAGE-10]
SPLIT = MESSAGE.split("<br /><br />")

# Parse the data to pull out the numbers we defined earlier in the order they are read
nums = []
for x in SPLIT:
    if x.startswith("xxxxx<br"):
        nums.append(5)
        tmp = x[100:]
        nums.append(NUMBERS[tmp])
    elif x is not '':
        nums.append(NUMBERS[x])

print nums

# Take the numbers we parsed are send the data back to the server
url = '/'
for i in nums:
    url += str(i)
print base_url+url

session = requests.session()
response = session.get(base_url+'/'+url, cookies=cookie)

# Write the subsequent webpage to a file for easy viewing
f = open('flag.html', 'w')
f.write(response.content)
f.close()
