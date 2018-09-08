import sys
from generators import *

def main():
    seed = 729150385 # gerado aleatoriamente
    length = 16
    bbs = BBS(seed, length)
    if bbs.generate_number():
        print bbs.generated_number
    else:
        print "Error generating number"

    # lcg = LCG(seed)
    # mt = MT(seed)


if __name__ == '__main__':
    main()
