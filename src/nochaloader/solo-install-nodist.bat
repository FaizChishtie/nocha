@echo off

TITLE nocha installer - nodist

ECHO nocha installer,
ECHO by Faiz

AT > NUL
IF %ERRORLEVEL% NEQ 0 (
    ECHO Please run me as administrator (:
    PAUSE
    EXIT /b 
)

ECHO installing nodist...

choco install nodist

ECHO done!



