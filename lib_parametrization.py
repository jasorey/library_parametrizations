import json
import os
import pdb
import sys
import numpy as np
import itertools as it
from scipy.interpolate import splev,splint
from collections import defaultdict
import tables


def h5setattr(obj, attr, val):
    """Set attribute in JSON format."""

    if isinstance(val, np.ndarray):
        kind = val.dtype.kind
        if kind == 'i':
            val = map(int, val)
        elif kind == 'f':
            val = map(float, val)
        else:
            raise ValueError('Not implemented')

    val = json.dumps(val)
 
    setattr(getattr(obj, 'attrs'), attr, val)


class observ:
      
    def parametrizations(self,obs):
        parametrization_name=obs['name_par']['method']
        if (parametrization_name == '3Dfid'):
            print(parametrization_name)
        if (parametrization_name == '2D'):
            print(parametrization_name)
            observ.nz = 4    
        if (parametrization_name == '3Dobs'):
            print(parametrization_name)


class lib_read:
    """Reads the files with the parametrization and correlations/covariance"""
    def __init__(self, file_name, info={}, root= '/', only_open=False):
        """Initializes the input of data."""
        """It uses the file_name and then root sets where
        """in the HDF5 hierarchy everything lies
        
 
        self._info = info 
        file_name = os.path.expanduser(file_name)

        assert file_name, 'No package file specified.'
        self.h5file = tables.openFile(file_name,mode='r+' title = 'Parametrizations',
                                      rootUEP=root)

        self.init_read()

            
    def read_meta(self,out_path,objdict):
        self._fb = tables.openFile(out_path, 'w')
        self._fb.createGroup('/', 'meta')
        obsobj=observ()
        obsobj.parametrizations(objdict)
        print(obsobj.nz)
        meta = self._fb.createArray('/meta', 'meta', np.zeros(0))


    def read_meta_parametrization(self, observ):
        """Add meta data for each parametrization to HDF5 files."""
        
        for i, pop_name in enumerate(wl.pop['meta']['pop']):
            group_pop = '/meta/'+parametrization_name
            meta_parametrization = self._fb.createArray(group_pop, 'meta', np.zeros(0),createparents=True)
       
            
            pop = wl.pop[pop_name]
            h5setattr(meta_parametrization, 'z_mean', parametrization['z_mean'])
            h5setattr(meta_parametrization, 'z_width', parametrization['z_width'])

    def init_read(self):

        parametrization = self.read

        
            
class lib_write:
    

    def add_meta(self,out_path,objdict):
        self._fb = tables.openFile(out_path, 'w')
        self._fb.createGroup('/', 'meta')
        obsobj=observ()
        obsobj.parametrizations(objdict)
        print(obsobj.nz)
        meta = self._fb.createArray('/meta', 'meta', np.zeros(0))


    def add_meta_parametrization(self, observ):
        """Add meta data for each parametrization to HDF5 files."""
        
        for i, pop_name in enumerate(wl.pop['meta']['pop']):
            group_pop = '/meta/'+parametrization_name
            meta_parametrization = self._fb.createArray(group_pop, 'meta', np.zeros(0),createparents=True)
       
            
            pop = wl.pop[pop_name]
            h5setattr(meta_parametrization, 'z_mean', parametrization['z_mean'])
            h5setattr(meta_parametrization, 'z_width', parametrization['z_width'])



def main():
    
    file_name="trial0.h5"
    #add_meta(file_name)   
    name_parametrization = '2D'
    objdict = {'name_par':{'method':name_parametrization,'nz':4}}
    #objdict['name_par'] = name_parametrization
    print(objdict['name_par'])   
    print(objdict['name_par']['method'])
    
    x=lib_write()
    x.add_meta(file_name,objdict)
    

    return
    
if __name__ == '__main__':
    main()

