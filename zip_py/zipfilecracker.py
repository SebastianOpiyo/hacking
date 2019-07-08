#! usr/bin/env python3

# the zip file for zipping and unzipping.
import zipfile

# To enable for similar processes to run at a time we utilize the `threading` module
from threading import Thread 

# in the function below we pass in zFile and password
# resulting from the main() and then recursively call the function within the thread module
def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print('[+] Found Password ' + password + '\n')
    except:
        pass

def main():
    zFile = zipfile.ZipFile("evil.zip")
    passFile = open('dictionary.txt')
    for line in passFile.readlines():
        password = line.strip('\n')
        # we call the thread module below 
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()

if __name__=='__main__':
    main()
