'''
Author : Hari om Singh
Date : 06-June -2017
Description: This will convert the Text to Audio
'''

from shutil import copyfile
import os

#filename='Kung.Fu.Panda.3.2016..HCHDRip.XviD.AC3-EVO.avi'
#srcpath='C:\\Users\\Harry\\Desktop\\Kung.Fu.Panda.3'
#destpath='C:\\Users\\Harry\\Desktop\\Interview'


def LocalFileCopy(filename,srcpath,destpath):
    srcpath=srcpath + "\\" +filename
    destpath=destpath + "\\" + filename
    copyfile(srcpath, destpath)

def LocalFileDelete(filename,srcpath):
    srcpath = srcpath + "\\" + filename
    os.remove(srcpath)

'''def LocalFileSearch(filename):
    # This will help in finding the file in local system.

def CopyfromUsb(filename):
    # This will help to copy the file from USB to Harddisk
    # i need to decide the destination path for the same

def ShutDown():
    # this will shut down the system
'''
def LockMySystem():
    # this will simply lock the system
    command='rundll32.exe user32.dll,LockWorkStation'
    os.system(command)







#localfilecopy(filename,srcpath,destpath)
#LocalFileDelete(filename,destpath)
