
cd .\%1
rmdir /s .\build
python setup.py install --skip-build --no-compile
cd ..\
