#!/usr/bin/python
# -*- coding: utf-8 -*-
import io, os

path = "testFile" # 读取文件
testFile = open(path, 'r')
stringArray = testFile.readlines()

userHome = os.path.expanduser('~')
desktopPath = os.path.join(userHome, 'Desktop')
print("path: {0}".format(desktopPath))

newFilePath = '{0}/generationFile.md'.format(desktopPath)
newFile = open(newFilePath,'a') # 写入到桌面 generationFile.md

for currentString in stringArray:
    print(currentString)
    splitStringArray = currentString.split("\":") # worning
    lastString = splitStringArray[-1]
    lastString = lastString.strip(",\n")

    key = splitStringArray[0].replace('"', '')
    var = ""
    if currentString == stringArray[0]:
        var = "\n var"
    else:
        var = "var"

    if "\"" in lastString:
        newFile.write("{0} {1}: String? \n".format(var, key))
    elif "true" in lastString or "false" in lastString:
        newFile.write("%s %s: BOOL? \n"% (var, key))
    elif "." in lastString:
        newFile.write("{0} {1}: Double? \n".format(var, key))
    else:
        newFile.write("{0} {1}: Int? \n".format(var, key))
    # break

testFile.close()
newFile.close()
