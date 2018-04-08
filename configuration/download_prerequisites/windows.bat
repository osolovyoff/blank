@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%PROGRAMFILES%\Chocolatey\bin"
setx ChocolateyInstall "%PROGRAMFILES%\Chocolatey"
setx ChocolateyToolsLocation "%PROGRAMFILES%\Chocolatey\Tools"

choco install python3 --yes
choco install cmake --yes
choco install conan --yes

conan remote add bincraftes      https://api.bintray.com/conan/bincrafters/public-conan
conan remote add pocoproject     https://api.bintray.com/conan/pocoproject/conan
conan remote add conan-community https://api.bintray.com/conan/conan-community/conan