#!/usr/bin/python3
import cgi
import random
global subprocess
import subprocess
from subprocess import call, DEVNULL, STDOUT, check_call, Popen, PIPE

fs = cgi.FieldStorage()

lang = "CPP"

# Filename: Random number between 1 and 10^19
filename = str(random.randint(1,10**19))

def Docker_RMI():
	# Clear the clutter, delete old Docker Images
	process = subprocess.Popen(['docker', 'images'], stdout=subprocess.PIPE)
	build_images = process.communicate()

	# Stop all stopped containers
	#Popen(['docker', 'rm', '$(docker ps -a -q)'])

	try:
		for i in range(1,len(build_images.split("\n"))):
			docker_image=build_images.split('\n')[i].split()[2]

			# Preserve important images used for building new images
			if(docker_image not in ['8357b3fcbe41', '8ac48589692a', 'efb6baa1169f', '8357b3fcbe41', '1b3de68a7ff8']):
				subprocess.getoutput("docker rmi -f {image}".format(image = docker_image))
	except:
		print ("")		

def Lang_C_CPP(lang):
		ext = "c" if lang == "C" else "cpp" 
		code_file = filename + ".{ext}".format(ext = ext)
		executable_file = filename + ".o"
		
		program_code = """
#include <iostream>
using namespace std;

int main(){
cout<<"hello world!\\n";
return 0;
}"""
		write_code_file = open("code_files/" + code_file, "w")
		write_code_file.write(program_code)
		write_code_file.close()

		
		#write_dockerfile = open("code_files/"+ code_file, "w")

		# Absolute path needed for COPY as Docker executes a cache file from a tmp dir 
		Dockerfile = """
	FROM gcc:7.3
	WORKDIR /home
	RUN apt-get update && \
    apt-get -y install gcc mono-mcs && \
    rm -rf /var/lib/apt/lists/*
	CMD ["./main"]
		""".format(code_file = code_file, executable_file = executable_file, compile = "gcc" if lang == "C" else "g++")

		# Write the following Dockerfile contents to the location and file: [ "code_files" + PROGRAM/File ]
		#write_dockerfile.write(Dockerfile)
		#write_dockerfile.close()
		# "sudo docker cp UTK28.CPP c1ce27253d7e:/main.cpp"
		compiler = "gcc" if lang == "C" else "g++"
		
		# Container ID to be smaller in digits and hash to be always positive
		container_id = abs(hash(filename))

		# Generate random number within userable port range, check availability and use it
		available = 0
		while available == 0:
			for i in range (1,200):
				port = random.randint(1234,65535)
				if PortCheck(port) == "available":
					port = port
					print (port)
					break
				break
			break


		#os.system("docker run -itd --rm --name {label} gcc".format(label = container_id))
		#os.system("cd code_files && docker cp {codefile} {container}:/{codefile}".format(codefile = code_file, container = container_id))
		#os.system("gotty -w --once docker attach {container}".format(container = container_id))
		
		#call(["docker run -itd --rm --name {label} gcc".format(label = container_id)],stdout=None,shell=True)
		#call(["cd code_files && docker cp {codefile} {container}:/{codefile}".format(codefile = code_file, container = container_id)],stdout=None,shell=True)
		#call(["gotty -w --once docker attach {container}".format(container = container_id)],stdout=None,shell=True)
		

		check_call(['docker', 'run', '-itd', '--rm', '--stop-timeout', '120','--name', '{label}'.format(label = container_id), '723924dec980'],stdout=DEVNULL,stderr=STDOUT)
		check_call(['docker', 'cp', 'code_files/{codefile}'.format(codefile = code_file), '{container}:/home/main.{ext}'.format(codefile = code_file,container = container_id, ext = ext)],stdout=DEVNULL,stderr=STDOUT)
		
		# to execute command and make it display to user gotty screen
		# docker exec -ti cfa856a1dda9 screen -S web -X stuff $'./main\n'
		check_call(['docker', 'exec', '-ti', '{container}'.format(container = container_id), '{compiler}'.format(compiler = compiler), 'main.{ext}'.format(ext = ext), '-o', 'main'],stdout=DEVNULL,stderr=STDOUT)
		call(['gotty', '-p', '{port}'.format(port = port), '-w', 'docker', 'attach', '{container}'.format(container = container_id)],stdout=DEVNULL,stderr=STDOUT)




		#call(["cd code_files && docker build -t {label} -f {label} .".format(label = code_file)],shell=True)
		#call(["gotty -w --term PaaS docker run -it --rm {label}:latest ".format(label = code_file)],shell=True)

def Lang_Python(ver):
		# To use Python2 or 3 Docker container
		Dockerfile = """
		FROM python:{ver}
		COPY {File} /usr/src/mypy
		WORKDIR /usr/src/mypy
		CMD ["{PyVer} {File}"]
		""".format(File = File, ver = ver, PyVer = "Python2" if ver == 2 else "Python3")	
		print (Dockerfile)


def ttyOverBrowser(port, docker_cmd):
	subprocess.getoutput("ttyd -p {port} --once {cmd} &".format(port = port, cmd = docker_cmd))

def PortCheck(port):
	p1 = subprocess.Popen(["netstat", "-an"], stdout=PIPE)
	p2 = subprocess.Popen(["grep", "{port}".format(port = port)], stdin=p1.stdout, stdout=PIPE)
	p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
	output = p2.communicate()[0]
	if (output):
		return ("unavailable")
	else:
		return ("available")

def choice():
	if (lang == "C" or lang == "CPP"):
		l = "c" if lang == "C" else "cpp"
		Lang_C_CPP(l)
	elif (lang == "Python2" or lang == "Python3"):
		ver = ("{ver}").format(ver = 2 if lang == "Python2" else "3")
		Lang_Python(ver)

def main():
	Docker_RMI()
	Lang_C_CPP(lang)

main()

