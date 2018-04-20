#!/usr/bin/python3
import cgi
import random
global subprocess
import subprocess
from subprocess import call

fs = cgi.FieldStorage()

lang = "CPP"

# Filename: Random number between 1 and 10^19
code_file = str(random.randint(1,10**19))

def Docker_RMI():
	# Clear the clutter, delete old Docker Images
	process = subprocess.Popen(['docker', 'images'], stdout=subprocess.PIPE)
	build_images = process.communicate()	
	try:
		for i in range(1,len(build_images.split("\n"))):
			docker_image=build_images.split('\n')[i].split()[2]

			# Preserve important images used for building new images
			if(docker_image not in ['8ac48589692a','efb6baa1169f','8357b3fcbe41','1b3de68a7ff8']):
				subprocess.getoutput("docker rmi -f {image}".format(image = docker_image))
	except:
		print ("")		

def CCPP(lang):
		cpp_file = code_file + ".{lang}".format(lang = "c" if lang == "C" else "cpp")
		cpp_executable = cpp_file.split('.')[0] + ".o"
		
		CPP_Program = """
		#include <iostream>
		using namespace std;

		int main(){
		cout<<"hello world!";
		return 0;
		}
		"""
		write_cpp_file = open("cpp_files/" + cpp_file, "w")
		write_cpp_file.write(CPP_Program)
		write_cpp_file.close()

		
		write_dockerfile = open("cpp_files/"+ code_file, "w")

		# Absolute path needed for COPY as Docker executes a cache file from a tmp dir 
		Dockerfile = """
	FROM gcc:4.9
	COPY {cpp_file} /usr/src/mycpp/
	WORKDIR /usr/src/mycpp
	RUN {compile} -o {cpp_executable} {cpp_file}
	CMD ["./{cpp_executable}"]
		""".format(cpp_file = cpp_file, cpp_executable = cpp_executable, compile = "gcc" if lang == "C" else "g++")

		# Write the following Dockerfile contents to the location and file: [ "cpp_files" + PROGRAM/File ]
		write_dockerfile.write(Dockerfile)
		write_dockerfile.close()

		call(["cd cpp_files && docker build -t {label} -f {label} .".format(label = code_file)],shell=True)
		
		call(["gotty -w --term PaaS docker run -it --rm {label}:latest ".format(label = code_file)],shell=True)

def Lang

def Process():
	if (lang == "C" or lang == "CPP"):
		 

		
	elif (lang == "Python2" or lang == "Python3"):
		

def ttyOverBrowser(port, docker_cmd):
	subprocess.getoutput("ttyd -p {port} --once {cmd} &".format(port = port, cmd = docker_cmd))

def main():
	Docker_RMI()
	Process()

main()