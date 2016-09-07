# getdata
some automatisation for cdo postprocessing

Example:

```python
import getdata as gd
  
basepath = '/mnt/lustre01/work/ch0636/a270067/rom/ae06_ind'
exp = '551'
model = 'remo'
wildcards = ['*box*']
selmon = '6,7,8,9'
selyear = '1988/2001'
custom = ['-timmean']
extraname = '_ymm_1988_2001_JJAS' #a
opath = '/mnt/lustre01/work/ch0636/u241057/INDIA/qdb'
ymonmean = False

path   = gd.make_ipath(basepath, exp, model)
inames = gd.make_inames(path, wildcards)
onames = gd.make_onames(opath, inames, extraname)


commands = gd.cdo_commands(model, inames, onames, custom,  ymonmean, selyear, selmon)

#print commands
gd.cdo_exe(commands)
```
