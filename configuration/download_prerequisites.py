import os
import platform

if platform.system() == 'Windows':
	os.system('@"%SystemRoot%\System32\WindowsPowerShell\\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command \"iex ((New-Object System.Net.WebClient).DownloadString(\'https://chocolatey.org/install.ps1\'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\\chocolatey\\bin"')
	os.system('choco install cmake')
	os.system('choco install python3')
	os.system('choco install conan')

if platform.system() == 'Darwin':
    os.system('ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
    os.system('brew install cmake')
    os.system('brew install python3')
    os.system('brew install conan')

os.system('conan remote add conan-community https://api.bintray.com/conan/conan-community/conan')