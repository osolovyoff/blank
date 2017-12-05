import os
import platform

if platform.system() == 'Darwin':
	os.system('ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
	os.system('brew install cmake')
	os.system('brew install python3')
	os.system('brew install conan')

os.system('conan remote add conan-community https://api.bintray.com/conan/conan-community/conan')