#! usr/bin/env Python3

import crypt
import os
import sys

def testPass(cryptPass):
    # We are slicing the first two characters in the salt.
    salt = cryptPass[0:2]
    dictFile = open('dictionary.txt', 'r')
    # we iterate throught he words in the file and strip the result
    for word in dictFile.readlines():
        word = word.strip('\n') # strip space at the end of the word
        cryptWord = crypt.crypt(word, salt)
        if (cryptWord == cryptPass):
            print('[+] Found Password: ' + word + '\n')
            return
    print('[-] Password Not Found. \n')
    return

def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ": " in line:
            # we get split the user and encrypted password and get passwd.
            user = line.split(': ')[0]
            # here we get the encrypted passwd
            cryptPass = line.split(': ')[1].strip(' ')
            print('[*] Cracking password For: '+ user)
            # we call the testPass function and pass in the pswd
            testPass(cryptPass)

if __name__=="__main__":
    main()


