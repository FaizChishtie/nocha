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
CALL :check_req node node
CALL :check_req nodist nodist
CALL :check_req py python
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
    ECHO depencencies OK
    ECHO setting nocha up...
    
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
    CALL :installer nodist

:python
    CALL :installer python

:pip
    CALL :installer pip

:installer 
    ECHO installing %1
    choco install %1
    ECHO done!

:uninstaller
    ECHO uninstalling %1
    choco uninstall %1
    ECHO done!

:bad_install
    ECHO.
    ECHO nocha install failed ):
    PAUSE > NUL
    EXIT

ECHO nocha installs complete!