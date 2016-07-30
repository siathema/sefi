#!/usr/bin/python
# sefi: SEnd FIlenames
# Author: Matthias Linford
# email: nate.holaday@gmail.com
# version 0.3 7.29.16

import sys
import os
import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def list_diff(list1, list2):
    diff_list = []
    for entry in list1:
        if not entry in list2:
            diff_list.append(entry)
    return diff_list

if len(sys.argv) != 3:
    print ("usage: python sefi.py [name@me.domain] [Path to directory]")
    sys.exit()
try:
    file_object = open("sefi_file_directories.json", "r")
except FileNotFoundError:
    file_object = open("sefi_file_directories.json", "w")
    json.dump(os.listdir(sys.argv[2]), file_object)
    print("No JSON file found in current directory! Generating one now!")
    file_object.close()
    sys.exit(0)


file_contents = json.load(file_object)
file_object.close()



mDirFiles = os.listdir(sys.argv[2])
if len(mDirFiles) < 1:
    print("No files in directory.");
    sys.exit()

diff_files = list_diff(mDirFiles, file_contents)

file_object = open("sefi_file_directories.json", "w")
json.dump(mDirFiles, file_object)
file_object.close()

if not diff_files:
    print("No new files!")
    sys.exit(0)


mSender = "sender@my.hostname"
mReceiver = sys.argv[1]


mMessage = MIMEMultipart('alternative')
mMessage['Subject'] = "New Files"
mMessage['From'] = mSender
mMessage['To'] = mReceiver

html = """\
<html>
  <head>
  </head>
  <body>
    <h1> You have {0} new files in {1}! <h1>
    <p>
        the new files are:
    </p>
    <ul>""".format(str(len(diff_files)) ,sys.argv[2])

for entry in diff_files:
    html += "<li>{0}</li>".format(entry)

html += "</ul></body></html>"

mMessage.attach(MIMEText(html, 'html'))


mServer = smtplib.SMTP('localhost')
mServer.sendmail(mSender, mReceiver, mMessage.as_string())
