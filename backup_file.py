#!/home/navraj/env/bin/python
import os
import sys
import shutil
import datetime


path = "/home/navraj/hris/DBBackups/"  #KEEP THE PATH HERE 
len_del = 3    #SPECIFY THE NUMBER OF FILES TO RETAIN


def sort_dirs(file_list):  #SORTING THE FILES ACCORDING TO THEIR CREATED DATE
		file_list.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime,reverse=True)
		return file_list

def delete_folder(file_dir):
		print("Original Order of files")
		print(file_dir)
		list_files=sort_dirs(file_dir)
		print("Sorted Order of files")
		print(list_files)
		length=len(list_files)
		if length>len_del:
				print("Operation Deletion Files Lists")
				to_be_deleted=list_files[len_del:]
				print(to_be_deleted)
				del_files=len(list_files[len_del:])
				try:
						for i in range(del_files):
								print("File Deleted->",to_be_deleted[i])
								os.remove(path+"/"+to_be_deleted[i])
				except OSError as e:
						print("Error",e.strerror)
		else:
				print(path,"directory is already up to date!")

def get_files():
		tree=[]
		tree=os.listdir(path)
		return tree


def main():
		list_files = get_files()
		print("\n======================= OPERATION STARTS============================\n")
		delete_folder(list_files) #DELETING THE FOLDERS VIA FUNCTION delete_folder
		print("\n============================== OPERATION END ==================================================\n")

main()


