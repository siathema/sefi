#!/usr/bin/python
# sefi: SEnd FIlenames
# Author: Matthias Linford
# email: nate.holaday@gmail.com
# version 0.3 7.29.16

import sys
import os
import json


def list_diff(list1, list2):
    diff_list = []
    for entry in list1:
        if not entry in list2:
            diff_list.append(entry)
    return diff_list

if len(sys.argv) != 2:
    print ("usage: python sefi.py [Path to directory]")
    sys.exit()



try:
    file_object = open("sefi_file_directories.json", "r")
except FileNotFoundError:
    file_object = open("sefi_file_directories.json", "w")
    json.dump(os.listdir(sys.argv[1]), file_object)
    print("No JSON file found in current directory! Generating one now!")
    file_object.close()
    sys.exit(0)


file_contents = json.load(file_object)
file_object.close()



directory_list = os.listdir(sys.argv[1])
if len(directory_list) < 1:
    print("No files in directory.");
    sys.exit()

diff_files = list_diff(directory_list, file_contents)

file_object = open("sefi_file_directories.json", "w")
json.dump(directory_list, file_object)
file_object.close()

if not diff_files:
    print("No new files!")
    sys.exit(0)




Message = """You have {0} new files in {1}!
the new files are:
""".format(str(len(diff_files)) ,sys.argv[1])

for entry in diff_files:
    Message += (entry + '\n')

print(Message)