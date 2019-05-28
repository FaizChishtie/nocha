@echo off

TITLE nocha installer - nodist

ECHO nocha installer,
ECHO by Faiz

NET SESSION >NUL 2>&1
IF %ERRORLEVEL% NEQ 0 (
    ECHO Please run me as administrator (:
    PAUSE
    EXIT /b 
)

ECHO installing nodist...

choco install nodist

ECHO done!



