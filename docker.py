#!/usr/bin/python3
import cgi
import random
import json

global subprocess
import subprocess


print("Content-type: application/json")
print ()

fs = cgi.FieldStorage()

#lang = str(fs.getvalue('language'))
code = str(fs.getvalue('code'))
lang = "CPP"

result = {}
url = ""
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
		ext = "c" if lang == "c" else "cpp" 
		code_file = filename + ".{ext}".format(ext = ext)
		executable_file = filename + ".o"
		
		program_code = "{0}".format(code)
		write_code_file = open("code_files/" + code_file, "w+")
		write_code_file.write(program_code)
		write_code_file.close()


		# Generate random number within userable port range, check availability and use it
		available = 0
		while available == 0:
			for i in range (1,200):
				port = random.randint(1234,65535)
				if PortCheck(port) == "available":
					port = port
					break
				break
			break

		compiler = "gcc" if lang == "c" else "g++"

		# Container ID to be smaller in digits and hash to be always positive
		container_id = abs(hash(filename))

		launch_container = "docker run -itd --rm --stop-timeout 120 --name {container} ef64c983448b && \
		docker cp code_files/{codefile} {container}:/home/main.{ext} && \
		docker exec {container} {compiler} main.{ext} -o main".format(codefile = code_file,container = container_id, ext = ext, compiler = compiler)
		web_shell = "ttyd -p {port} -r 2 -d 0 docker attach {container}".format(container = container_id, port = port)

		
		subprocess.Popen(launch_container, shell=True, close_fds=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		#subprocess.Popen(copy_code_to_container, shell=True, close_fds=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		#subprocess.Popen(compile_code_in_container,shell=True, close_fds=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.Popen(web_shell, shell=True, close_fds=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		
		url = 'http://54.69.112.75:' + str(port)
		
		result['url'] = url
		result['success'] = True
		print (json.dumps(result))		

		

		#docker build -t gcc-nano -f GCCDockerfile .
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
	p1 = subprocess.Popen(["netstat", "-an"], stdout=subprocess.PIPE)
	p2 = subprocess.Popen(["grep", "{port}".format(port = port)], stdin=p1.stdout, stdout=subprocess.PIPE)
	p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
	output = p2.communicate()[0]
	if (output):
		return ("unavailable")
	else:
		return ("available")

def choice():
	if (lang == "c" or lang == "cpp"):
		l = "c" if lang == "c" else "cpp"
		Lang_C_CPP(l)
	elif (lang == "Python2" or lang == "Python3"):
		ver = ("{ver}").format(ver = 2 if lang == "Python2" else "3")
		Lang_Python(ver)

def main():
	#Docker_RMI()
	Lang_C_CPP(lang)
main()

