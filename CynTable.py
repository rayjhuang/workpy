
class MTPTable:
    '''
    multiple-time programable table
    OTP-emulated table
    parse a given .txt file when init.
    '''
    def __init__ (me, mtptfile):
        me.parsed = []
        ln = 0 # line number
        f = open (mtptfile,'r')
        for xx in f.readlines ():
            ln += 1
            line = xx.split('#')[0]
            if line != '' and  line[0] >= ' ' and  line[0] != '#':
                line = [ln] + line.split()
                if line[2] == '=': me.parsed += [line]
                else: print '#%d: assignment required' % (ln)


    def GetValue (me, entryname, nbit, org, shf):
        ret = org
        value = []
        for xx in range(len(me.parsed)):
            if entryname == me.parsed[xx][1]: # found
                value = me.parsed[xx][3:]

        if len(value) > 1:
            print '#%d: ilegal parameter' % (me.parsed[xx][0])
        elif len(value) > 0:
            try:
                num = int(value[0])
                if num >= 2**nbit:
                    print '#%d: ilegal value' % (me.parsed[xx][0])
                else:
                    print entryname, ':', num
                    msk = 0xff >> (8-nbit)
                    ret = org & msk | (num << shf) # success
            except:
                print '#%d: ilegal format' % (me.parsed[xx][0])

        return ret


    def OptionTable (me):
        entry = [0x02, 0x08, 0x00, 0x00] # FW default
        entry[0] = me.GetValue ('OPTION_RP',    2, entry[0], 0)
        entry[1] = me.GetValue ('OPTION_DCP',   1, entry[1], 3)
        entry[2] = me.GetValue ('OPTION_SLPEN', 1, entry[2], 3)
        return entry


    def GetPDO (me, entryname):
        ret = []
        value = []
        for xx in range(len(me.parsed)):
            if entryname == me.parsed[xx][1]: # found
                value = me.parsed[xx][3:]
                print entryname, me.parsed[xx]

        return ret


    def PDOTable (me):
        entry = []
        for xx in range(1,7):
            yy = len(entry)
            entry += me.GetPDO ('PDO'+`xx`)
            if yy == len(entry):
                break

        if len(entry) == 0:
            entry = [[0x2c, 0x91, 0x01, 0x0a]] # FW default

        return entry


if __name__ == '__main__':

    mtt = MTPTable('CynTable.txt')
    print ['%02X' % xx for xx in mtt.OptionTable ()]
    pdo = mtt.PDOTable ()
    print [['%02X' % xx for xx in pdo[yy]] for yy in range(len(pdo))]
    
