
REM SET HEXFILE=z:\RD\Project\CAN1112\Ray\fw\cy2332r0_20181024_033.hex
    SET HEXFILE=Y:\project\can1112\svn\fw\uart_txrx\uart_txrx.hex

    python -B c:\Python27\Scripts\hex2bin.py %HEXFILE% temp.bin

REM DEL temp.bin
