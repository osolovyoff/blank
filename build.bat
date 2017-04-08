@echo off
color D
if not exist _build mkdir _build	
pushd "_build"
	cmake ..
popd
pause