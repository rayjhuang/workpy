REM ============================================
REM 1. work in .\ directory
REM    > install cynpy
REM    > python -mcynpy.csp
REM
REM 2. work in .\cynpy directory
REM    > python -B .\cynpy\csp.py
REM
REM ============================================

cd .\%1
rmdir /s/q .\build
python setup.py install --skip-build --no-compile
cd ..\
