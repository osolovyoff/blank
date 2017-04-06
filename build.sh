sudo apt-get install git
sudo apt-get install cmake

mkdir -p _build
cd obj
cmake ..
make -j4