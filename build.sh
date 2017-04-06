function download(){
	sudo apt-get -y install $1
	echo $1 installed
}

download git
download cmake
download make

mkdir -p _build
cd _build
cmake ..
make -j4
pause