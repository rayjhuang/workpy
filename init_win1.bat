@echo off
rem Windows 7

    SET PYPATH=C:\Python27

    SET TOTALPHASEPATH=X:\project\tools\TotalPhase
rem SET TOTALPHASEPATH=D:\TotalPhase
rem SET TOTALPHASEPATH=%CD%\..\..\tools\TotalPhase

rem SET MYPYPATH=%HOMEDRIVE%%HOMEPATH%\Dropbox\script\python
rem SET MYPYPATH=E:\Dropbox\script\python
rem SET MYPY=%MYPYPATH%\rapy

rem SET PYTHONPATH=%TOTALPHASEPATH%\aardvark-api-windows-i686-v5.13\python

rem If like to X:\project\github\workpy\cynpy>python -B .\cynpy\aardv.py
rem Include current directory for module searching
    SET PYTHONPATH=%CD%;%TOTALPHASEPATH%\aardvark-api-windows-x86_64-v5.13\python

rem for DLL, EXE searching
    @PATH=%CD%;%PYPATH%;%TOTALPHASEPATH%\aardvark-api-windows-i686-v5.13\python;%PATH%

    dir/w %PYTHONPATH%
rem dir/w %MYPY%
