@ECHO OFF

SET _IN=%1

IF "%_IN%"=="html" (
    GOTO :html
)

IF "%_IN%"=="server" (
    GOTO :server
)

:html
ECHO generate HTML output
start %~dp0env\Scripts\pelican.exe content -o output -s pelicanconf.py
ECHO Done
GOTO :end

:server
cd output
start %~dp0env\Scripts\Python.exe -m pelican.server
pause
GOTO :end


:end
ENDLOCAL