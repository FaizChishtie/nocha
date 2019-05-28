@echo off

TITLE nocha installer - Faiz

ECHO.
ECHO.
ECHO.

ECHO nocha installer

NET SESSION >NUL 2>&1
IF %ERRORLEVEL% NEQ 0 (
    ECHO.
    ECHO Please run me as administrator (:
    PAUSE > NUL
    EXIT /b 
)
ECHO.
ECHO.
ECHO.

ECHO nocha installer

ECHO nocha installs starting...

CALL :check_req choco choco
CALL :check_req nodist nodist
ECHO .

ECHO installs complete...

ECHO.
ECHO.
ECHO.

PAUSE >NUL

:: subroutines

:check_req
    SET "MISSING_REQUIREMENT=true"
    
    WHERE %1 > NUL 2>&1 && SET "MISSING_REQUIREMENT=false"
    IF "%MISSING_REQUIREMENT%"=="true" (
        GOTO %2
    )
    EXIT /b

:choco
    ECHO installing chocolatey...
    @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
    ECHO done!

:nodist
    ECHO installing nodist...
    choco install nodist
    ECHO done!


ECHO nocha installs complete!