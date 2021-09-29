
###include<stdint.h>
###include<stdio.h>
##int main() {
##  unsigned int p = 0x04C11DB7, r = 0;
##  void f(char c) {
##    for(int i = 7; i >= 0; i--) {
##      int msb = r & (1<<31);
##      r <<= 1;
##      if (msb) r = r ^ p;
##    }
##    r ^= c;
##  }
##  int c, len = 0;
##  while(EOF != (c = getchar())) {
##    len++;
##    f(c);
##  }
##  int n = len;
##  do {
##    f(n & 0xff);
##    n >>= 8;
##  } while(n);
##  f(0), f(0), f(0), f(0);
##  printf("%u %u\n", ~r, len);
##  return 0;
##}

class CRC32:
    '''
    posix cksum, CRC-32-IEEE 802.3 (0x04C11DB7)
    '''
    def __init__(me, colst=[32,26,23,22,16,12,11,10,8,7,5,4,2,1,0]):
        me.shift_register = []
        me.generator_polynomial = colst
        me.clear()

    def clear (me):
        me.shift_register = []
        for ii in range(me.generator_polynomial[0]):
            me.shift_register += [0]

    def string_complement (me):
        str = ''
        for ii in range(len(me.shift_register)-1,-1,-1):
            str += '1' if me.shift_register[ii]==0 else '0'
            if (ii%8==0 and ii>0):
                str += '_'
        return str

    def string_binary (me):
        str = ''
        for ii in range(len(me.shift_register)-1,-1,-1):
            str += '1' if me.shift_register[ii]==1 else '0'
            if (ii%8==0 and ii>0):
                str += '_'
        return str

    def shift_in_bit (me, bit):
        msb = me.shift_register[-1]
        for ii in range(len(me.shift_register)-1,-1,-1):
            me.shift_register[ii] = bit if ii==0 else me.shift_register[ii-1]
        if msb==1:
            for ii in me.generator_polynomial[1:]:
                me.shift_register[ii] = 0 if me.shift_register[ii]==1 else 1

    def shift_in_oct (me, octets):
        for cc in octets:
            for ii in range(7,-1,-1):
                me.shift_in_bit (1 if (cc & (1<<ii)) > 0 else 0)



if __name__ == '__main__':

    cksum = CRC32()
#   cksum.shift_in_oct ([ord('0'),ord('\n'),2,0,0,0,0])
    cksum.shift_in_oct ([ord('0'),0,0,0,0])
    print '%08X' % (int(cksum.string_complement().replace('_',''),2))
