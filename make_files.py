#!/home/navraj/env/bin/python
import os

dest_path = "/home/navraj/nav_maintain_files/"
source_path = "/home/navraj/bak_scripts/files.txt"

f=open(source_path,"r+")

file_name = f.readlines()

file_name = [x.strip("\n") for x in file_name]

for leaf in file_name:
		print(leaf)
		os.system(f"touch '{dest_path}{leaf}'")

