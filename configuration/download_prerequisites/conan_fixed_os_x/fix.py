import os

LAST_VERSION_WITH_ERROR = 174

conan_version = int(filter(str.isdigit, os.popen('conan --version').read()))

if LAST_VERSION_WITH_ERROR >= conan_version :

	os.system('cp -r conan_fixed_os_x/default /Users/$USER/.conan/profiles/')
	os.system('cp -r conan_fixed_os_x/settings.yml /Users/$USER/.conan/')