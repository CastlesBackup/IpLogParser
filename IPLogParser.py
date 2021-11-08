# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 19:10:26 2021
@author: GO-MCF
usage : python IPLogParser.py -i <IPListFile> -l <logFile> -o <outputFileIPFound> -c
or
IPLogParser.exe -i <IPListFile> -l <logFile> -o <outputFileIPFound> -c
"""

import sys, os, argparse
from datetime import datetime

def findIP(iPListFile,logFile,outputFileIPFound,countIP):
    os.system('cls')
    os.system('color 4')
        
    print("\033[1;33m")
    print("    ________  __                ____                           ")
    print("   /  _/ __ \/ /   ____  ____ _/ __ \____ ______________  _____")
    print("   / // /_/ / /   / __ \/ __ `/ /_/ / __ `/ ___/ ___/ _ \/ ___/")
    print(" _/ // ____/ /___/ /_/ / /_/ / ____/ /_/ / /  (__  )  __/ /    ")
    print("/___/_/   /_____/\____/\__, /_/    \__,_/_/  /____/\___/_/     ")
    print("                      /____/                                   ")
    print("")
      
    print("Version 1.0 - 2021-10-26 - GO-MCF\n")
    print("\033[1;33mStart to find IP in log file "+logFile+" : \033[0;0m")
    nbIP2Check=0
    nbIPFound=0
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d-%H%M%S_")
    outFile = open(dt_string+outputFileIPFound,'w')
    with open(logFile,'r') as lFile:
        LogLine = lFile.read()
    with open(iPListFile, 'r') as iFile:
        ipLines = iFile.readlines()
    for ipLine in ipLines:
        nbIP2Check +=1 
        if ipLine.strip() in LogLine:
            if countIP == True : 
                nbIP = LogLine.count(ipLine.strip())
                print("\033[0;32m==> "+ipLine.strip()+ " found ! ("+ str(nbIP) +")\033[0;0m")
                outFile.write(ipLine.strip()+";"+str(nbIP)+"\n")
            else :
                print("\033[0;32m==> "+ipLine.strip()+ " found ! \033[0;0m")
                outFile.write(ipLine)                
            nbIPFound +=1
        else :
            print("\033[0;31m"+ipLine.strip()+ " not found\033[0;0m")

    print("\033[1;33m-------------------------------\033[0;0m")
    print("\033[1;33mResult of the scan : \033[0;0m")
    print("\033[1;34m"+str(nbIP2Check)+" IP checked \033[0;0m")
    print("\033[1;34m"+str(nbIPFound)+" IP found \033[0;0m")
    print("\033[1;33mIp found have been saved in "+dt_string+outputFileIPFound+" file \033[0;0m")
    
def main(argv):
    parser = argparse.ArgumentParser(description='Find IP in log file')
    parser.add_argument("-i", help="IP List input file", required=True)
    parser.add_argument("-l", help="log input file", required=True)
    parser.add_argument("-o", help="IP List found output file", required=True)
    parser.add_argument("-c", action="store_true", help="Count how many times IP has been found, display the value and store in output file")
    args = parser.parse_args()
    
    findIP(args.i,args.l,args.o,args.c)

if __name__ == '__main__':
    main(sys.argv[1:])