import sys
from generators import *
import time


all_lengths = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

def main():
    seed = 729150385 # gerado aleatoriamente
    for length in all_lengths:
        print 'length:',length
        start = time.time()
        print("----------------------------")
        # print("BBS")
        bbs = BBS(seed, length)
        if bbs.generate_number():
            print bbs.generated_number
            # pass
        else:
            print "Error generating number"
        end = time.time()
        # print "Elapsed time:"
        print((end - start) * 1000)
        # print("----------------------------")
        # print("LCG")
        start = time.time()
        lcg = LCG(length, 32, 7, 0, seed)
        lcg.generate_number()
        print lcg.generated_number
        end = time.time()
        # print "Elapsed time:"
        print((end - start) * 1000)
        print("----------------------------")


if __name__ == '__main__':
    main() 
