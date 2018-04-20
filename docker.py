#!/usr/bin/python3
import cgi
import random
global subprocess
import subprocess
from subprocess import call

fs = cgi.FieldStorage()

lang = "CPP"

# Filename: Random number between 1 and 10^19
PROGRAM_File = str(random.randint(1,10**19))

def Docker_RMI():
	# Clear the clutter, delete old Docker Images
	process = subprocess.Popen(['docker', 'images'], stdout=subprocess.PIPE)
	Build_Images = process.communicate()	
	try:
		for i in range(1,len(Build_Images.split("\n"))):
			Image=Build_Images.split('\n')[i].split()[2]

			# Preserve important images used for building new images
			if(Image not in ['8ac48589692a','efb6baa1169f','8357b3fcbe41','1b3de68a7ff8']):
				subprocess.getoutput("docker rmi -f {image}".format(image = Image))
	except:
		print ("")		

def Process():
	if (lang == "C" or lang == "CPP"):
		 
		CPP_File = PROGRAM_File + ".{lang}".format(lang = "c" if lang == "C" else "cpp")
		Exec_Program = CPP_File.split('.')[0] + ".o"
		
		CPP_Program = """
		#include <iostream>
		using namespace std;

		int main(){
		cout<<"hello world!";
		return 0;
		}
		"""
		write_CPP_File = open("CPP_Files/" + CPP_File, "w")
		write_CPP_File.write(CPP_Program)
		write_CPP_File.close()

		
		Write_Dockerfile = open("CPP_Files/"+ PROGRAM_File, "w")

		# Absolute path needed for COPY as Docker executes a cache file from a tmp dir 
		Dockerfile = """
	FROM gcc:4.9
	COPY {CPP_File} /usr/src/mycpp/
	WORKDIR /usr/src/mycpp
	RUN {compile} -o {Exec_Program} {CPP_File}
	CMD ["./{Exec_Program}"]
		""".format(CPP_File = CPP_File, Exec_Program = Exec_Program, compile = "gcc" if lang == "C" else "g++")

		# Write the following Dockerfile contents to the location and file: [ "CPP_Files" + PROGRAM/File ]
		Write_Dockerfile.write(Dockerfile)
		Write_Dockerfile.close()

		call(["cd CPP_Files && docker build -t {label} -f {label} .".format(label = PROGRAM_File)],shell=True)
		
		call(["gotty -w --term PaaS docker run -it --rm {label}:latest ".format(label = PROGRAM_File)],shell=True)
		
	elif (lang == "Python2" or lang == "Python3"):
		# Python version to use in Dockerfile
		ver = ("{ver}").format(ver = 2 if lang == "Python2" else "3")

		# To use Python2 or 3 Docker container
		Dockerfile = """
		FROM python:{ver}
		COPY {File} /usr/src/mypy
		WORKDIR /usr/src/mypy
		CMD ["{PyVer} {File}"]
		""".format(File = File, ver = ver, PyVer = "Python2" if lang == "Python2" else "Python3")	
		print (Dockerfile)

def ttyOverBrowser(port, docker_cmd):
	subprocess.getoutput("ttyd -p {port} --once {cmd} &".format(port = port, cmd = docker_cmd))

def main():
	Docker_RMI()
	Process()

main()