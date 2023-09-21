from common.io.writeToa import readToa
import numpy as np
from config import globalConfig

my_toa_path=r"C:\workbench\EODP-TS-L1B\00my_outputs"
reference_toa_path=r"C:\workbench\EODP-TS-L1B\output"
bands = ['VNIR-0','VNIR-1','VNIR-2','VNIR-3']
l1b_toa = 'l1b_toa_'

for band in bands:
    my_toa = readToa(my_toa_path, l1b_toa + band + '.nc')

    reference_toa = readToa(reference_toa_path, l1b_toa + band + '.nc')
    result = reference_toa-my_toa

    difference=result/my_toa*100

    # plotear la linea central
    #



