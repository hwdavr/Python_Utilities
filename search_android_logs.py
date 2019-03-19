import zipfile
import gzip
import os
import mmap
import sys
from shutil import copyfile
import optparse
import subprocess

def searchZipFile(filename, keyword):
    filePath = os.path.join(folderPath, filename)
    print("Searching " + filePath)
    zip_ref = gzip.open(filePath, 'r')
    file_content = zip_ref.read()
    if keyword in file_content:
        desPath = os.path.join(targetFolder, filename+".txt")
        print("Found keyword in file:", filePath)
        #copyfile(filePath, desPath)
        with open(desPath, "w") as fw:
            fw.write(file_content)
    zip_ref.close()

if __name__ == '__main__':
    parser = optparse.OptionParser()

    parser.add_option('-s', dest='src', help='Path of android_logs folder, including android_logs itself', type='string')
    parser.add_option('-w', dest='keyword', help='The keyword to be searched', type='string')
    parser.add_option('-d', dest='target', help='The destination path of the found file to be copied, relative path of current location', type='string')

    try:
        (options, args) = parser.parse_args()

        folderPath = options.src
        if not options.keyword:
            raise optparse.OptionValueError('No keyword specified, please use -w to specify the keyword')

        # Get current working directory
        dir_path = os.path.dirname(os.path.realpath(__file__))
        if options.target:
            targetFolder = os.path.join(dir_path, options.target)
        else:
            targetFolder = os.path.join(dir_path, 'target')
        if not os.path.isdir(targetFolder):
            os.mkdir(targetFolder)

        isFound = False
        for (_, _, filenames) in os.walk(folderPath):
            for filename in filenames:
                if filename.startswith("applogcat-log.") and filename.endswith(".gz"):
                    isFound = True
                    searchZipFile(filename, options.keyword)
        if not isFound:
            raise optparse.OptionValueError('No applogcat-log file is found')
    except optparse.OptionValueError as e:
        parser.print_help()
        parser.error(e.msg)

