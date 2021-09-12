@ECHO OFF
pushd %~d0
cd %~dp0
python.exe %~dpn0.py %1 %2 %3 %4 %5 %6 %7 %8
@pause