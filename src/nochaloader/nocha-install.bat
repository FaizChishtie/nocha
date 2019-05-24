@echo off

TITLE nocha installer - Faiz

AT > NUL
IF %ERRORLEVEL% NEQ 0 (
    ECHO Please run me as administrator (:
    PAUSE
    EXIT /b 
)

START /WAIT /B call.bat