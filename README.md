# ipLogParser
"""

Created on Tue Oct 26 19:10:26 2021

@author: GO-MCF

usage : python IPLogParser.py -i IPListFile -l logFile -o outputFileIPFound -c
  
or
  
IPLogParser.exe -i IPListFile -l logFile -o outputFileIPFound -c
  
"""

This script has been developped with python 3.8.8

This python script is used to find a list of ip adress in a log file.

IPListFile : File containig a list of ip adress
logFile : File we want to find ip adress from the IPListFile below
outputFileIPFound : All ip found will be saved in this file prefixed by datetime like 20210403_outputFileIPFound.txt
if we want to have the count of each ip adress found, add -c to the command line

I've generated the .exe file to run with windows 10.
the .exe has been generated with pyinstaller.
You can generate your own version with this command : pyinstaller IPLogParser.py --onefile

  
Screenshot "iplogparser_exe.jpg" shows the script in action with a log file containing 170948 lines.

Screenshot "iplogparser-_exe.jpg" shows the script in action with the "-c" activated
  
