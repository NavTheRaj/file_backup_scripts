#!/home/navraj/env/bin/python
import os
import sys
import shutil

def delete_folder(file_dir):
    FILE_DIR=file_dir
    list_files=os.listdir(FILE_DIR)
    length=len(list_files)
    if length>5:
        list_files.sort(reverse=True) #ARRANGING IN DESCENDING ORDER FOR FILE FORMAT EXAMPLE 03Feb2020
        print("Original Files")
        print(list_files)
        print("Operation Deletion Files Lists")
        to_be_deleted=list_files[5:]
        print(to_be_deleted)
        del_files=len(list_files[5:])
        try:
            for i in range(len(list_files[5:])):
                print("File Deleted->",to_be_deleted[i])
                shutil.rmtree(FILE_DIR+"/"+to_be_deleted[i])
        except OSError as e:
            print("Error",e.strerror)
    else:
        print("No files to be deleted!")

def main():
    #directory for the server_backup files
    #insert here full directory
    list_dirs=[
     #add the necessary directories here
    ] 
    for i in range(len(list_dirs)):
        delete_folder(list_dirs[i])

main()

