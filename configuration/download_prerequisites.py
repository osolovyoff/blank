import os
import platform

if platform.system() == 'Windows':
    os.system('@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"')
    choro_script = @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
        '@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" '\
        '-NoProfile -InputFormat None -ExecutionPolicy Bypass -Command '

           && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
    choco_script = 'hello'\
        'privet'\
        'log'
    print(choco_script)
    # choco_script = '@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

if platform.system() == 'Darwin':
    os.system('ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
    os.system('brew install cmake')
    os.system('brew install python3')
    os.system('brew install conan')

# import os
# import platfor
m
# if platform.system() == 'Windows':
#     os.system("pip install --upgrade pip")
#     os.system("pip install -r requirements_windows.txt")

# class Prerequisites:




# if platform.system() == 'Windows':


# os.system('conan remote add conan-community https://api.bintray.com/conan/conan-community/conan')


# import os
# os.system("pip install --upgrade pip")
# os.system("pip install -r requirements_windows.txt")

# import shutil
# import urllib3
# http = urllib3.PoolManager()

# url = "https://images.girlsaskguys.com/custom/content_images/how-to-be-hot-2.jpg"
# path = "girl.jpg"
# with http.request('GET', url, preload_content=False) as r, open(path, 'wb') as out_file:       
#     shutil.copyfileobj(r, out_file)

# // LINUX
# pip
# wget
# urllib3
# tarfile

# // Windows
# pip
# urllib3


# pip list --format=freeze
# colorama==0.3.7
# docopt==0.6.2
# idlex==1.13
# jedi==0.9.0