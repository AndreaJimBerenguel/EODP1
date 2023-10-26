from common.io.writeToa import readToa
import numpy as np
import matplotlib.pyplot as plt
from config import globalConfig

my_toa_path=r'C:\workbench\EODP_TER_2021\EODP-TS-L1C\my_output'
lucia_toa_path=r'C:\workbench\EODP_TER_2021\EODP-TS-L1C\output'

bands = ['VNIR-0','VNIR-1','VNIR-2','VNIR-3']

l1c_toa='l1c_toa_'

for band in bands:
    my_toa_output = readToa(my_toa_path, l1c_toa + band + '.nc')
    lucia_toa = readToa(lucia_toa_path, l1c_toa + band + '.nc')

    result = lucia_toa-my_toa_output

    difference=np.sort(result)/np.sort(my_toa_output*100)

    checking_difference=np.array(difference < 0.01)

    sum_trues=sum(checking_difference)

    sigma3_checking=np.all(sum_trues >= 0.997*len(result))

    if(sigma3_checking== True):
        print("yes, differences with output TOA (", l1c_toa + band,") are <0.01% for at least 3-sigma of the points.")
    else:
        print("no, differences with output TOA (", l1c_toa + band,") are not <0.01% for at least 3-sigma of the points.")
