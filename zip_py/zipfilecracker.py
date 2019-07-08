#! usr/bin/env python3

import zipfile

zFile = zipfile.ZipFile("evil.zip")
zFile.extractall(pwd="secret")
