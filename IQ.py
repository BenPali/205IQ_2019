#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## 204ducks
## File description:
## main
##

import sys
import locale
from math import exp
from math import modf

def check_help():
    if (len(sys.argv) == 2 and sys.argv[1] == "-h"):
        print("USAGE\n\t", sys.argv[0], " u s [IQ1] [IQ2]\n", sep='')
        print("DESCRIPTION")
        print("\tu\tmean (integer)")
        print("\tk\tstandard deviation (integer)")
        print("\tIQ1\tminimum IQ (integer)")
        print("\tIQ2\tmaximum IQ (integer)")
        exit(0)

def check_nbr_arg():
    if (len(sys.argv) < 3 or len(sys.argv) > 5):
        exit(84)

def get_iq(x):
    if (x < 0 or x > 200):
        exit(84)
    else:
        return (x)

def density_function(u, s):
    return
    #plot the density function of the IQ for every integer between 0 and 200

def calc_percentage(u, s, q1, q2 = 0):
    return
    # print the percentage of people with an IQ inferior to this q1 value
    # print the percentage of people with an IQ in between those q1, q2 values

def main():
    check_help()
    try:
        check_nbr_arg()
        u = int(sys.argv[1])
        s = int(sys.argv[2])
        if (len(sys.argv) == 4):
            iq1 = get_iq(int(sys.argv[3]))
            calc_percentage(u, s, iq1)
        elif (len(sys.argv) == 5):
            iq1 = get_iq(int(sys.argv[3]))
            iq2 = get_iq(int(sys.argv[4]))
            calc_percentage(u, s, iq1, iq2)
        else:
            density_function(u, s)
    except:
        print("Check -h for more information")
        exit(84)

if __name__ == '__main__':
    main()