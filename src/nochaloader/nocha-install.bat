@echo off

TITLE nocha installer - Faiz

NET SESSION >NUL 2>&1
IF %ERRORLEVEL% NEQ 0 (
    ECHO Please run me as administrator (:
    PAUSE
    EXIT /b 
)
ECHO.
ECHO.
ECHO.

ECHO nocha installer

ECHO nocha installs starting...

goto choco
goto nodist

ECHO.
ECHO.
ECHO.

:choco
    ECHO installing chocolatey...
    @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
    ECHO done!

:nodist
    ECHO installing nodist...
    choco install nodist
    ECHO done!


ECHO nocha installs complete!