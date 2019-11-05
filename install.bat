REM ============================================
REM 1. work in .\ directory
REM    > install cynpy
REM    > python -mcynpy.csp
REM
REM 2. work in .\cynpy directory
REM     N.A.
REM
REM 3. work with Lib
REM       ...editing...
REM    > python C:\Python27\Lib\site-packages\cynpy-0.209-py2.7.egg\cynpy\csp.py
REM
REM ============================================

cd .\%1
rmdir /s/q .\build
python setup.py install --skip-build --no-compile
cd ..\
