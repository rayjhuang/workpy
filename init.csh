#!/bin/csh

   if ( -e ~/Desktop/project/tools/TotalPhase ) than
      echo 
   endif

   setenv TOTALPHASEPATH ~/Desktop/project/tools/TotalPhase
   setenv PYTHONPATH $TOTALPHASEPATH/aardvark-api-macosx-x86_64-v5.13/python
   ls -l $PYTHONPATH

