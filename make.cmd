@echo off
cd /d "%~dp0"
echo ==================================================================================
echo  Powered by PyInstaller, MiniConda and Visual Studio for Enterprise (with A.I.) 
echo ==================================================================================
goto start

:start
::Install the PyInstaller
echo Installing PyInstaller
python -m pip install pyinstaller tk
set ECHO
::Creating the executable
echo Creating the executable...
pyinstaller --noconfirm --onefile --windowed --icon "%~dp0media/icon.ico" "%~dp0To_Do_List.py"
goto copybin

:copybin
move "%~dp0dist\To_Do_List.exe" "%~dp0To_Do_List.exe"
rd "%~dp0build" /s /q
rd "%~dp0dist" /s /q