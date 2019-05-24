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
    ECHO Python 3 is not installed! Please install and try again...
    PAUSE > NUL
    EXIT /b
)

ECHO python OK

ECHO.
ECHO.

ECHO starting nocha...

python3 nocha.py

ECHO.

ECHO nocha complete...

PAUSE > NUL

:: subroutines
