#!/usr/bin/env python
import argparse
import numpy as np
import matplotlib.pyplot as plt
import read_sam as rs


def fig_sfrmstar(sfr,mstar):
    plt.scatter(np.log10(mstar),np.log10(sfr),marker='.')
    plt.ylabel(r"log$_{10}$ sfr")
    plt.xlabel(r"log$_{10} M_{gal}")

def main():
    parser = argparse.ArgumentParser(description="Do Something.")
    parser.add_argument("fname",help='SAM output file name'
                        ,action="store",default='',type=str)
    parser.add_argument("--sfrm",help='sfr vrs. galaxy mass figure'
                        ,action="store_true")
    args=parser.parse_args()
    if args.sfrm==True:
        mass,sfr=rs.read(args.fname,fields=['mstar','sfr'])
        fig_sfrmass(sfr,mass)
        plt.savefig('fig_sfrmstar.pdf')


if __name__=='__main__':
    main()
