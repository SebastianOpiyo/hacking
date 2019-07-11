#! usr/bin/env python3
import optparse
import zipfile
from threading import Thread 

def extractFile(zFile, password): # picks args* from the main function.
    try:
        zFile.extractall(pwd=password) # Doing the brute force here!
        print('[+] Found Password ' + password + '\n')
    except:
        pass

def main():
    parser = optparse.OptionParser("usage%prog "+\
            "-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string',\
            help='specify the zip file')
    parser.add_option('-d', dest='dname', type='string',\
            help='specify dictioanary file')
    (options, args) = parser.parse_args()
    if(options.zname == None) | (options.dname == None):
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zFile = zipfile.ZipFile("evil.zip")
    passFile = open('dictionary.txt')
    for line in passFile.readlines():
        password = line.strip('\n') # we brute force using each word from dict.
        # Running multiple threads. 
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()

if __name__=='__main__':
    main()
