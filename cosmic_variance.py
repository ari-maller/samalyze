import glob
import numpy as np
import argparse
import matplotlib.pyplot as plt
import ytree
import samalyze as sml
ytree.utilities.logger.ytreeLogger.setLevel(50)
#For a simulation that has been split into many sub volumes
#takes a look at how many subvolumes one needs to reduce cosmic variance

def mass_name(arbor):
    #since mass name differs in outputs search for the right one
    mass_name='sam_mvir'
    field_names=arbor.field_list
    if mass_name not in field_names:
        mass_name='sam_Mvir'
    if mass_name not in field_names:
        print(f"Error: {mass_name} not in field list")
    return(mass_name)

def main(args):
    if args.dname[-1]!='/':
        dname=args.dname+'/'
    else:
        dname=args.dname
    treefiles=glob.glob(dname+"tree_?_?_?.dat")
    treefiles=treefiles[0:2]
    print(treefiles)
    mass_list=[]
    for tfile in treefiles:
        a=ytree.load(tfile)
        mname=mass_name(a)
        masses=a[mname]
        mass_list.append(masses)

    for i in range(len(mass_list)):
        mass = np.log10(mass_list[i])
        f,axis=plt.subplots()
        volume=args.bs**3
        sml.xyhistplot(mass,axis,weight=1./volume,Nbins=20)
        plt.savefig("cosmic_variance.pdf")


if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Do Something.")
    parser.add_argument("dname",action="store",default='',type=str
                    ,help='Directory containing multiple treefiles')
    parser.add_argument("--bs",action="store",default=71.4286,type=float
                    ,help="Boxsize of each subvolume")
    args=parser.parse_args()
    main(args)
