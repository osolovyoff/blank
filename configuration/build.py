import os
from subprocess import call

build_directory = "build"

os.chdir("../")
if not os.path.exists(build_directory):
	os.mkdir(build_directory)
os.chdir(build_directory)

call('cmake ../', shell=True)
