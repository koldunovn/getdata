import glob
import numpy as np
import os
import sh

cdo = sh.cdo

path = '/mnt/lustre01/work/ch0636/a270067/rom/ae06_ind'
exp = '419'
model = 'remo'
wildcards = ['qdboxs', 'qdboxu']
selmon = '6,7,8,9'
selyear = '1999/2001'
custom = ['sellevel,1']

opath = '/mnt/lustre01/work/ch0636/u241057/INDIA'

def make_ipath(path, exp, model):
    '''
    make path where to search for the input variables
    '''
    if model == 'remo':
        modelfolder = 'remodata'
    elif model == 'mpiom':
        modelfolder = 'mpiomdata'

    return os.path.join(path, exp, modelfolder)

def make_inames(path, wildcards):
    '''
    collect names of files with input variables
    '''
    inames = []
    for wildcard in wildcards:
        ifiles = glob.glob('{}/*{}*'.format(path, wildcard))
        for ffile in ifiles:
            inames.append(ffile)
    inames.sort()

    return inames

def make_onames(opath, inames):
    pass


def convert_function(custom=None, ymonmean = None, selyear=None, selmon=None):
    
    '''
    create convert line for cdo. 
    by default convert to netCDF4 and copy
    '''
    basic = ['-f', 'nc4', '-r']
    if not custom:
        custom = []
    print(custom)
    #if we forget to add dash for the first operator in custom line
    if len(custom)>=1:
        if not custom[0].startswith('-'):
            custom[0] = "-"+custom[0]

    if ymonmean:
        custom.append('-ymonmean')
    if selyear:
        custom.append('-selyear,{}'.format(selyear))
    if selmon:
        custom.append('-selmon,{}'.format(selmon))
    if not custom:
        custom.append('-copy')

    final_function = basic

    for operator in custom:
            final_function.append(operator)
    
    return final_function


def custom_finction(model, custom = None):
    '''
    Add predefined custom function for the model and
    combine it with user provided custom function.
    '''
    if not custom:
        custom = []

    if model == 'remo':
        pass
    elif model =='mpiom':
        custom.append('-setpartab,/work/ch0636/m222054/ds/mpiom.partab.nash')
        custom.append('-setgrid,/work/ch0636/m222054/ds/grids/AE06/AE06s.nc')
        custom.append('-selindexbox,2,723,1,424')
        custom.append('-setgrid,r724x424')
    else:
        custom = []
    return custom


def cdo_command(model, custom=None, ymonmean = None, selyear = None, selmon=None):
    custom = custom_finction(model)
    final_function = convert_function(custom, ymonmean, selyear, selmon)
    return final_function

def cdo_exe(final_function):
    pass


    



