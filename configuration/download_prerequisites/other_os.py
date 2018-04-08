import os
import platform

pm = 'apt'

if platform.system() == 'Windows':
	os.system('@"%SystemRoot%\System32\WindowsPowerShell\\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command \"iex ((New-Object System.Net.WebClient).DownloadString(\'https://chocolatey.org/install.ps1\'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\\chocolatey\\bin"')
	pm = 'choco'

if platform.system() == 'Darwin':
    os.system('ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
    pm = 'brew'

dependencies = ['cmake','python3', 'conan']
for dep in dependencies:
	os.system(pm + ' install ' + dep)
	
os.system('conan remote add conan-community https://api.bintray.com/conan/conan-community/conan')