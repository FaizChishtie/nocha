@echo off

TITLE nocha v0.1.0 - Faizaan Chishtie, 2019

ECHO.
ECHO.
ECHO nocha,
ECHO by Faiz

:: Check for python

ECHO Checking python installation...

python3 --version 2>NUL 2>&1
IF %ERRORLEVEL% NEQ 0 (
    ECHO.
    ECHO Python 3 is not installed ): 
    ECHO Please run the installer and try again!
    PAUSE > NUL
    EXIT /b
)
ECHO.

ECHO python OK

SETLOCAL
CD /d %~dp0

ECHO.
ECHO.

ECHO starting nocha...

python3 "src\nocha.py"

ECHO.

ECHO nocha complete...

PAUSE > NUL

:: subroutines
