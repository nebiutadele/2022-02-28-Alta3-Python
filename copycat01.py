#!/usr/bin/env python3

#import shell utility
import shutil
#import operating system module
import os

def copycat():
    # start in a specific directory
    os.chdir("/home/student/mycode/")

    #copy a file
    shutil.copy("5g_research/sdn_network.txt",
            "5g_research/sdn_network.txt.copy")
    
    #remove previous version of folder
    os.system("rm -rf /home/student/mycode/5g_research_backup/")

    #copy a directory
    shutil.copytree("5g_research/", "5g_research_backup/")
if __name__ == "__main__":
    copycat()

