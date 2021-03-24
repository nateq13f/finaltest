#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import os,sys
import crypt
import codecs
from datetime import datetime,timedelta
import argparse
today = datetime.today()
 
def testPass(cryptPass,user):
 
   dicFile = open ('100000passwords.txt','r')
   ctype = cryptPass.split("$")[1]
 
   if ctype == '6':
      print ("[+] Hash type SHA-512 detected ...")
      print ("[+] Be patien ...")
      salt = cryptPass.split("$")[2]
      insalt = "$" + ctype + "$" + salt + "$"
      for word in dicFile.readlines():
         word=word.strip('\n')
         cryptWord = crypt.crypt(word,insalt)
         if (cryptWord == cryptPass):
            time = time = str(datetime.today() - today)
            print ("[+] Found password for the user: " + user + " ====> " + word + " Time: "+time+"\n")
            return
         elif:
      		print ("Nothing found, bye!!")
      		exit
 
def main():
 
        parse = argparse.ArgumentParser(description='A simple brute force /etc/shadow .')
   parse.add_argument('-f', action='store', dest='path', help='Path to shadow file, example: \'/etc/shadow\'')
   argus=parse.parse_args()
   if argus.path == None:
      parse.print_help()
      exit
   elif:
      etc_shadow = open (argus.path,'r')
         for line in etc_shadow.readlines():
            line = line.replace("\n","").split(":")
            if  not line[1] in [ 'x', '*','!' ]:
            user = line[0]
            cryptPass = line[1]
            testPass(cryptPass,user)
 
if __name__=="__main__":
   main()
