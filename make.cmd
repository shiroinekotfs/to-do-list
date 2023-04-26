@echo off
cd /d "%~dp0"
echo ==================================================================================
echo  Powered by PyInstaller, MiniConda and Visual Studio for Enterprise (with A.I.) 
echo ==================================================================================
goto start

:start
::Install the PyInstaller
echo Installing PyInstaller
::Update the pip first
python -m pip install --upgrade pip
python -m pip install -r "%~dp0requirements.txt"
set ECHO
::Creating the executable
echo Creating the executable...
python -m pyinstaller --noconfirm --onefile --windowed --icon "%~dp0media/icon.ico" "%~dp0To_Do_List.py"
pause
goto copybin

:copybin
move "%~dp0dist\To_Do_List.exe" "%~dp0To_Do_List.exe"
rd "%~dp0build" /s /q
rd "%~dp0dist" /s /q
pause