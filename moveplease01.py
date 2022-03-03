#!/usr/bin/env python3

#Import shell utility and os to manipulate files
import shutil
import os

def movePlease():
    #set starting directory
    os.chdir('/home/student/mycode/')

    #move file
    shutil.move('raynor.obj', 'ceph_storage/')

    #reaname the file that is moving
    xname = input('What is the new name for kerrigan.obj? ')
    
    #move the new file into the new directory
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

#call created function
movePlease()

