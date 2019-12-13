
REM plug CAN1108 into a CAN1110/2 source
REM with CC1 connected to CC
REM power CAN1108 by the VIN

REM python -mcynpy.isp stop
REM python -mcynpy.isp trim
REM python -mcynpy.csp 1 stop

REM set the VIN=6.56+V
    python -mcynpy.csp 1 write E5=52

REM while (1) {}
    python -mcynpy.isp prog_hex 1 008 FF 80 FE FF

REM set the VIN=5.04+V
    python -mcynpy.csp 1 write E5=3F




