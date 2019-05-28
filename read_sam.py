import h5py
import numpy as np

def fields(fname):
    hf=h5py.File(fname,'r')
    f=[]
    for key in hf.keys():
        f.append(key)
    return f

def read(fname,fields=[]):
    hf=h5py.File(fname,'r')
    results=[]
    if (fields==[]):
        for key in hf.keys():
            fields.append(key)
    for name in fields:
        data = hf.get(name)
        results.append(np.array(data))

    return results

def logsum(array):
    array=np.array(array)
    return np.sum(10**array)
    
def gal2halo(fname,field='mcold'):
    gdata=read_all(fname)
    hids,hids_indices=np.unique(gdata['halo_id'],return_index=True)
    Nhalos=len(hids)
    halo_sum=np.zeros(Nhalos)
    for i in range(Nhalos-1):
        halo_sum[i]=logsum(gdata[field][hids_indices[i]:hids_indices[i+1]])

    return halo_sum
    
