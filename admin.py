import setup_path
import os
from sys import platform
import win32com as shell

global file_path
file_path=os.path.abspath("Datasets.py")
print(file_path)
def RunAsAdmin(path_to_file,*args):
	if platform=="win32":
    	#Run Powershell and give the file path
		os.system(r'Powershell -Command "powershell "'+file_path+
				' -ArgumentList @('+str(args)[1:-1]+')'+ # Arguments. [1:-1] to remove brackets
				' -Verb RunAs /user:Administrator '+file_path # Run file as administrator
		)
	elif platform=="darwin":
		os.system("sudo bash Dataset.py")

	else:
		os.system("sudo bas Dataset.py")