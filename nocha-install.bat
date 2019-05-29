@echo off

TITLE nocha installer - Faiz

ECHO.
ECHO.
ECHO.

ECHO nocha installer

SETLOCAL
CD /d %~dp0

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
:: CALL :check_req pip pip
ECHO.

CALL :setup

ECHO.
ECHO.
ECHO installs complete...

ECHO.
ECHO.
ECHO.

PAUSE >NUL

EXIT /b

:: subroutines

:setup
    ECHO.
    ECHO setting nocha up...
    py --version 2>NUL 2>&1
    IF %ERRORLEVEL% NEQ 0 (
        ECHO.
        ECHO Python 3 is not installed! Please install and try again...
        PAUSE > NUL
        GOTO bad_install
    )
    
    py setup.py install

    EXIT /b

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
    ECHO uninstalling nodejs from programs and replacing it with nodist...
    CALL :uninstaller "nodejs"
    ECHO installing nodist...
    choco install nodist
    ECHO done!

:python
    ECHO installing python3
    choco install python
    ECHO done!

:pip
    ECHO installing pip...
    choco install pip
    ECHO done!

:uninstaller
    WMIC "where name="%1" call uninstall"

:path_setter
    ECHO Setting path for %1 under %2
    FOR /f %%p in ('where python') do SET PYTHONPATH=%%p
    ECHO %PYTHONPATH%

:bad_install
    ECHO.
    ECHO nocha install failed ):
    PAUSE > NUL
    EXIT

ECHO nocha installs complete!