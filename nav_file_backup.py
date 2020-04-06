#!/home/navraj/env/bin/python
import os

path = "/home/navraj/nav_maintain_files/"
ends_with = ".txt"
subisu_nav = []  #LIST FOR SUBISU NAV FILES
subisu_prod = [] #LIST FOR SUBISU PROD FILES
file_list = os.listdir(path)
file_list = [x.rstrip(" ") for x in file_list]
len_del = 3 #SPECIFY THE BACKUP FILES TO RETAIN ASTER THE SCRIPT IS RUN

#*******************FUNCTION FOR DELETING THE FILE THAT ENDS WITH '.txt'*********************************
def delete_txt_files():
	print("DELETING TXT FILES IN THE DIRECTORY")
	for leaf in os.scandir(path):
			if ".txt" in leaf.name:
				print("DELETING FILE=>"+leaf.path)
				os.remove(leaf.path)
#**********************************************FUNCTION ENDS HERE****************************************

#*******************FUNCTION TO CLASSIFY TWO TYPES OF FILE AND SORT THEM*********************************
def classify_and_delete():
		subisu_nav = [x for x in file_list if 'SUBISU NAV' in x]  ##CLASSIFYING TWO TYPES
		subisu_prod = [x for x in file_list if 'SUBISU-PROD' in x] ##OF FILES BASED ON KEYWORDS THEY CONTAIN
		
		if len(subisu_nav) > len_del:
				print("\nORIGINAL ORDER OF SUBISU NAV FILES\n")
				print(subisu_nav)
				subisu_nav.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime,reverse=True)  ##SORTING THE TWO SEPERATE LISTS
				print("\nSORTED ORDER OF SUBISU NAV FILES\n")
				print(subisu_nav)


				print("\nOPERATION STARTS IN SUBISU NAV FILES\n")
				for item in subisu_nav[len_del:]:
						print("DELETING=>",path+item)
						os.remove(path+item)
		
		else:
				print("SUBISU NAV FILE IS ALREADY UP TO DATE")
		
		if len(subisu_prod) > len_del:
				print("\nORIGINAL ORDER OF SUBISU PROD FILES\n")
				print(subisu_prod)
				subisu_prod.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime,reverse=True)  ##ACCORDING TO THE CREATED TIME
				print("\nSORTED ORDER OF SUBISU PROD FILES\n")
				print(subisu_prod)

				print("\nOPERATION STARTS IN SUBISU PROD FILES\n")
				for item in subisu_prod[len_del:]:
						print("DELETING=>",path+item)
						os.remove(path+item)
		
		else:
				print("SUBISU PROD FILES ARE ALREADY UP TO DATE")
		
#***********************************FUNCTION ENDS HERE**************************************************

def main():
		delete_txt_files()
		classify_and_delete()

main()

